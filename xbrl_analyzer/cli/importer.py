#!/usr/bin/env python3

import argparse
import sqlite3
import os
import sys
from xml.etree import ElementTree as ET

# Add the tools and db directories to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'db'))

from context_analyzer import (
    list_all_contexts,
    get_context_info
)

def get_xbrl_file_info(xbrl_file_path):
    """
    Extract basic information from XBRL file.
    
    Args:
        xbrl_file_path (str): Path to the XBRL file
        
    Returns:
        dict: File information
    """
    tree = ET.parse(xbrl_file_path)
    root = tree.getroot()
    
    # 动态提取命名空间
    namespaces = {}
    for elem in root.iter():
        if elem.tag.startswith('{'):
            ns_uri = elem.tag[1:].split('}')[0]
            # 提取命名空间的后缀部分（例如从'http://xbrl.sec.gov/dei/2024'提取'dei'）
            if '/' in ns_uri:
                ns_suffix = ns_uri.split('/')[-1]
                # 如果是dei命名空间，提取'dei'部分
                if 'dei' in ns_uri:
                    namespaces['dei'] = ns_uri
                elif 'us-gaap' in ns_uri:
                    namespaces['us-gaap'] = ns_uri
                elif 'xbrli' in ns_uri:
                    namespaces['xbrli'] = ns_uri
                # 也可以通过其他方式提取命名空间
    
    # 备用命名空间定义
    if 'dei' not in namespaces:
        namespaces['dei'] = 'http://xbrl.sec.gov/dei/2024'
    if 'xbrli' not in namespaces:
        namespaces['xbrli'] = 'http://www.xbrl.org/2003/instance'
    
    file_info = {
        'file_path': xbrl_file_path,
        'company_name': None,
        'filing_type': None,
        'fiscal_year': None,
        'fiscal_period': None,
        'period_end_date': None
    }
    
    # Extract company name
    entity_name = root.find('.//dei:EntityRegistrantName', namespaces)
    if entity_name is not None and entity_name.text:
        file_info['company_name'] = entity_name.text.strip()
    
    # Extract filing type
    doc_type = root.find('.//dei:DocumentType', namespaces)
    if doc_type is not None and doc_type.text:
        file_info['filing_type'] = doc_type.text.strip()
    
    # Extract fiscal year
    fiscal_year = root.find('.//dei:DocumentFiscalYearFocus', namespaces)
    if fiscal_year is not None and fiscal_year.text:
        try:
            file_info['fiscal_year'] = int(fiscal_year.text.strip())
        except ValueError:
            pass
    
    # Extract fiscal period
    fiscal_period = root.find('.//dei:DocumentFiscalPeriodFocus', namespaces)
    if fiscal_period is not None and fiscal_period.text:
        file_info['fiscal_period'] = fiscal_period.text.strip()
    
    # Extract period end date
    period_end = root.find('.//dei:DocumentPeriodEndDate', namespaces)
    if period_end is not None and period_end.text:
        file_info['period_end_date'] = period_end.text.strip()
    
    return file_info

def insert_xbrl_file(conn, file_info):
    """
    Insert XBRL file information into the database.
    
    Args:
        conn: SQLite database connection
        file_info (dict): File information
        
    Returns:
        int: Inserted file ID
    """
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT OR REPLACE INTO xbrl_files 
        (file_path, company_name, filing_type, fiscal_year, fiscal_period, period_end_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        file_info['file_path'],
        file_info['company_name'],
        file_info['filing_type'],
        file_info['fiscal_year'],
        file_info['fiscal_period'],
        file_info['period_end_date']
    ))
    
    file_id = cursor.lastrowid
    conn.commit()
    
    return file_id

def insert_contexts(conn, xbrl_file_path, xbrl_file_id):
    """
    Insert contexts from XBRL file into the database.
    
    Args:
        conn: SQLite database connection
        xbrl_file_path (str): Path to the XBRL file
        xbrl_file_id (int): ID of the XBRL file in the database
        
    Returns:
        dict: Mapping of context IDs to database IDs
    """
    cursor = conn.cursor()
    
    # Get all contexts
    context_ids = list_all_contexts(xbrl_file_path)
    context_mapping = {}
    
    for context_id in context_ids:
        # Get context info
        context_info = get_context_info(xbrl_file_path, context_id)
        if context_info is None:
            continue
            
        # Parse period information
        period_type = None
        start_date = None
        end_date = None
        instant_date = None
        
        period_info = context_info['period_info']
        if period_info.startswith('Instant: '):
            period_type = 'instant'
            instant_date = period_info[9:]  # Remove 'Instant: ' prefix
        elif period_info.startswith('Period: '):
            period_type = 'duration'
            period_part = period_info[8:]  # Remove 'Period: ' prefix
            if ' to ' in period_part:
                start_date, end_date = period_part.split(' to ', 1)
        
        # Insert context
        cursor.execute("""
            INSERT OR REPLACE INTO contexts 
            (xbrl_file_id, context_id, period_type, start_date, end_date, instant_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (xbrl_file_id, context_id, period_type, start_date, end_date, instant_date))
        
        context_db_id = cursor.lastrowid
        context_mapping[context_id] = context_db_id
        
        # Insert dimensions
        for dimension in context_info['dimensions']:
            dimension_name = dimension['dimension']
            member_name = dimension['member']
            
            # Extract clean names (remove namespace prefixes)
            if ':' in dimension_name:
                dimension_name = dimension_name.split(':')[-1]
            if ':' in member_name:
                member_name = member_name.split(':')[-1]
            
            cursor.execute("""
                INSERT OR REPLACE INTO dimensions 
                (context_id, dimension_name, member_name)
                VALUES (?, ?, ?)
            """, (context_db_id, dimension_name, member_name))
    
    conn.commit()
    return context_mapping

def insert_financial_facts(conn, xbrl_file_path, xbrl_file_id, context_mapping):
    """
    Insert financial facts from XBRL file into the database.
    
    Args:
        conn: SQLite database connection
        xbrl_file_path (str): Path to the XBRL file
        xbrl_file_id (int): ID of the XBRL file in the database
        context_mapping (dict): Mapping of context IDs to database IDs
    """
    cursor = conn.cursor()
    
    # Parse the XBRL file
    tree = ET.parse(xbrl_file_path)
    root = tree.getroot()
    
    # Define namespaces
    namespaces = {
        'xbrli': 'http://www.xbrl.org/2003/instance',
        'dei': 'http://xbrl.sec.gov/dei/2024',
        'us-gaap': 'http://fasb.org/us-gaap/2024',
        'aapl': 'http://www.apple.com/20240928',
        'country': 'http://xbrl.sec.gov/country/2024',
        'ecd': 'http://xbrl.sec.gov/ecd/2024',
        'iso4217': 'http://www.xbrl.org/2003/iso4217',
        'srt': 'http://fasb.org/srt/2024',
        'xbrldi': 'http://xbrl.org/2006/xbrldi'
    }
    
    # Collect all facts
    facts_count = 0
    for elem in root.iter():
        if 'contextRef' in elem.attrib:
            context_ref = elem.attrib['contextRef']
            
            # Check if we have this context in our mapping
            if context_ref not in context_mapping:
                continue
                
            context_db_id = context_mapping[context_ref]
            
            # Get the tag name
            tag_name = elem.tag
            if tag_name.startswith('{'):
                # Handle namespaced elements like {http://www.apple.com/20240928}TagName
                ns_uri, local_name = tag_name[1:].split('}', 1)
                tag_name = local_name
            
            # Get the value
            value = elem.text if elem.text else ""
            
            # Get unit and decimals
            unit_ref = elem.attrib.get('unitRef', '')
            decimals = elem.attrib.get('decimals', '')
            
            # Try to convert decimals to integer
            try:
                decimals = int(decimals) if decimals else None
            except ValueError:
                decimals = None
            
            # Insert or update financial tag
            cursor.execute("""
                INSERT OR IGNORE INTO financial_tags 
                (tag_name)
                VALUES (?)
            """, (tag_name,))
            
            # Get tag ID
            cursor.execute("SELECT id FROM financial_tags WHERE tag_name = ?", (tag_name,))
            tag_result = cursor.fetchone()
            if tag_result:
                tag_id = tag_result[0]
            else:
                continue
            
            # Insert or replace financial fact
            cursor.execute("""
                INSERT OR REPLACE INTO financial_facts 
                (xbrl_file_id, context_id, tag_id, value, unit, decimals)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (xbrl_file_id, context_db_id, tag_id, value, unit_ref, decimals))
            
            facts_count += 1
    
    conn.commit()
    print(f"Inserted {facts_count} financial facts")

def import_xbrl_file(conn, xbrl_file_path):
    """
    Import XBRL file into the database.
    
    Args:
        conn: SQLite database connection
        xbrl_file_path (str): Path to the XBRL file
    """
    print(f"Importing XBRL file: {xbrl_file_path}")
    
    # Get file info
    file_info = get_xbrl_file_info(xbrl_file_path)
    print(f"File info: {file_info}")
    
    # Insert file info
    file_id = insert_xbrl_file(conn, file_info)
    print(f"Inserted XBRL file with ID: {file_id}")
    
    # Insert contexts
    context_mapping = insert_contexts(conn, xbrl_file_path, file_id)
    print(f"Inserted {len(context_mapping)} contexts")
    
    # Insert financial facts
    insert_financial_facts(conn, xbrl_file_path, file_id, context_mapping)
    
    print("Import completed successfully")

def main():
    parser = argparse.ArgumentParser(description='Import XBRL files into database')
    parser.add_argument('--db', required=True, help='Path to SQLite database file')
    parser.add_argument('--xbrl-file', help='Path to a single XBRL file to import')
    parser.add_argument('--xbrl-dir', help='Directory containing XBRL files to import')
    
    args = parser.parse_args()
    
    # Connect to database
    conn = sqlite3.connect(args.db)
    
    try:
        if args.xbrl_file:
            # Import single file
            if os.path.exists(args.xbrl_file):
                import_xbrl_file(conn, args.xbrl_file)
            else:
                print(f"Error: File not found: {args.xbrl_file}")
                sys.exit(1)
        
        elif args.xbrl_dir:
            # Import all XBRL files in directory
            if os.path.exists(args.xbrl_dir):
                for filename in os.listdir(args.xbrl_dir):
                    if filename.endswith('.xml'):
                        file_path = os.path.join(args.xbrl_dir, filename)
                        try:
                            import_xbrl_file(conn, file_path)
                        except Exception as e:
                            print(f"Error importing {file_path}: {e}")
            else:
                print(f"Error: Directory not found: {args.xbrl_dir}")
                sys.exit(1)
        
        else:
            print("Error: Either --xbrl-file or --xbrl-dir must be specified")
            sys.exit(1)
            
    finally:
        conn.close()

if __name__ == "__main__":
    main()