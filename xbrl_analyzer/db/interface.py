#!/usr/bin/env python3
"""
Database Query Interface for XBRL Data

This module provides functions to query XBRL data stored in the database,
matching the functionality of the CLI tools.
"""

import sqlite3
import sys
import os

# Add the tools directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))

import translation

FINANCIAL_TERMS = translation.FINANCIAL_TERMS


class XBRLDatabaseQuery:
    """Interface for querying XBRL data from the database."""
    
    def __init__(self, db_path):
        """
        Initialize the database query interface.
        
        Args:
            db_path (str): Path to the SQLite database file
        """
        self.db_path = db_path
        self.conn = None
    
    def connect(self):
        """Connect to the database."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            return True
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return False
    
    def disconnect(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None
    
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
    
    def list_all_contexts(self, file_id=None):
        """
        List all contexts in the database, optionally filtered by file ID.
        
        Args:
            file_id (int, optional): Filter contexts by file ID
            
        Returns:
            list: List of context IDs
        """
        if not self.conn:
            raise Exception("Not connected to database")
        
        cursor = self.conn.cursor()
        
        if file_id:
            cursor.execute("""
                SELECT context_id 
                FROM contexts 
                WHERE xbrl_file_id = ?
                ORDER BY context_id
            """, (file_id,))
        else:
            cursor.execute("""
                SELECT context_id 
                FROM contexts 
                ORDER BY context_id
            """)
        
        contexts = cursor.fetchall()
        return [context[0] for context in contexts]
    
    def get_context_info(self, context_id, file_id=None):
        """
        Get detailed information about a specific context.
        
        Args:
            context_id (str): Context ID to get information for
            file_id (int, optional): Filter by file ID
            
        Returns:
            dict: Context information including period and dimensions, or None if not found
        """
        if not self.conn:
            raise Exception("Not connected to database")
        
        cursor = self.conn.cursor()
        
        # Get context details
        if file_id:
            cursor.execute("""
                SELECT c.id, c.period_type, c.start_date, c.end_date, c.instant_date
                FROM contexts c
                WHERE c.context_id = ? AND c.xbrl_file_id = ?
            """, (context_id, file_id))
        else:
            cursor.execute("""
                SELECT c.id, c.period_type, c.start_date, c.end_date, c.instant_date
                FROM contexts c
                WHERE c.context_id = ?
            """, (context_id,))
        
        context_row = cursor.fetchone()
        if not context_row:
            return None
        
        # Format period information
        period_info = "No period info"
        if context_row[1] == 'instant' and context_row[4]:
            period_info = f"Instant: {context_row[4]}"
        elif context_row[1] == 'duration' and context_row[2] and context_row[3]:
            period_info = f"Period: {context_row[2]} to {context_row[3]}"
        
        # Get dimensions
        cursor.execute("""
            SELECT dimension_name, member_name
            FROM dimensions
            WHERE context_id = ?
            ORDER BY dimension_name
        """, (context_row[0],))
        
        dimensions = []
        for dim_row in cursor.fetchall():
            dimensions.append({
                'dimension': dim_row[0],
                'member': dim_row[1]
            })
        
        return {
            'period_info': period_info,
            'dimensions': dimensions
        }
    
    def list_facts_for_context(self, context_id, file_id=None):
        """
        List all facts for a specific context ID.
        
        Args:
            context_id (str): Context ID to list facts for
            file_id (int, optional): Filter by file ID
            
        Returns:
            str: Formatted list of facts
        """
        if not self.conn:
            raise Exception("Not connected to database")
        
        cursor = self.conn.cursor()
        
        # Get context information
        context_info = self.get_context_info(context_id, file_id)
        if context_info is None:
            return f"Context ID '{context_id}' not found in the database."
        
        # Build result lines
        result_lines = [f"Facts for Context ID: {context_id}"]
        result_lines.append(f"Period: {context_info['period_info']}")
        
        # Add dimension information if available
        if context_info['dimensions']:
            result_lines.append("Dimensions:")
            for dim in context_info['dimensions']:
                result_lines.append(f"  {dim['dimension']}: {dim['member']}")
        
        result_lines.append("=" * 80)
        result_lines.append(f"{'Tag Name':<40} {'Chinese Name':<30} {'Value':<20}")
        result_lines.append("-" * 80)
        
        # Get facts for this context
        if file_id:
            cursor.execute("""
                SELECT t.tag_name, f.value
                FROM financial_facts f
                JOIN financial_tags t ON f.tag_id = t.id
                JOIN contexts c ON f.context_id = c.id
                WHERE c.context_id = ? AND c.xbrl_file_id = ?
                ORDER BY t.tag_name
            """, (context_id, file_id))
        else:
            cursor.execute("""
                SELECT t.tag_name, f.value
                FROM financial_facts f
                JOIN financial_tags t ON f.tag_id = t.id
                JOIN contexts c ON f.context_id = c.id
                WHERE c.context_id = ?
                ORDER BY t.tag_name
            """, (context_id,))
        
        facts = cursor.fetchall()
        for tag_name, value in facts:
            # Get Chinese translation
            chinese_name = FINANCIAL_TERMS.get(tag_name, "")
            result_lines.append(f"{tag_name:<40} {chinese_name:<30} {value or '':<20}")
        
        result_lines.append("=" * 80)
        result_lines.append(f"Total Facts: {len(facts)}")
        
        return "\n".join(result_lines)
    
    def get_company_list(self):
        """
        Get list of all companies in the database.
        
        Returns:
            list: List of company information
        """
        if not self.conn:
            raise Exception("Not connected to database")
        
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, company_name, filing_type, fiscal_year, fiscal_period, period_end_date 
            FROM xbrl_files
        """)
        
        companies = cursor.fetchall()
        return [{
            'id': company[0],
            'company_name': company[1],
            'filing_type': company[2],
            'fiscal_year': company[3],
            'fiscal_period': company[4],
            'period_end_date': company[5]
        } for company in companies]
    
    def search_facts_by_tag(self, tag_pattern, file_id=None):
        """
        Search for facts by tag name pattern.
        
        Args:
            tag_pattern (str): Pattern to search for in tag names (can include % for wildcards)
            file_id (int, optional): Filter by file ID
            
        Returns:
            list: List of matching facts
        """
        if not self.conn:
            raise Exception("Not connected to database")
        
        cursor = self.conn.cursor()
        
        if file_id:
            cursor.execute("""
                SELECT x.company_name, c.context_id, t.tag_name, f.value
                FROM financial_facts f
                JOIN financial_tags t ON f.tag_id = t.id
                JOIN contexts c ON f.context_id = c.id
                JOIN xbrl_files x ON f.xbrl_file_id = x.id
                WHERE t.tag_name LIKE ? AND f.xbrl_file_id = ?
                ORDER BY x.company_name, c.context_id
            """, (tag_pattern, file_id))
        else:
            cursor.execute("""
                SELECT x.company_name, c.context_id, t.tag_name, f.value
                FROM financial_facts f
                JOIN financial_tags t ON f.tag_id = t.id
                JOIN contexts c ON f.context_id = c.id
                JOIN xbrl_files x ON f.xbrl_file_id = x.id
                WHERE t.tag_name LIKE ?
                ORDER BY x.company_name, c.context_id
            """, (tag_pattern,))
        
        facts = cursor.fetchall()
        return [{
            'company_name': fact[0],
            'context_id': fact[1],
            'tag_name': fact[2],
            'value': fact[3]
        } for fact in facts]


def main():
    """Example usage of the database query interface."""
    # Example usage:
    # with XBRLDatabaseQuery('db/xbrl.db') as db:
    #     contexts = db.list_all_contexts()
    #     print("All contexts:", contexts)
    #     
    #     context_info = db.get_context_info('c-46')
    #     print("Context c-46 info:", context_info)
    #     
    #     facts = db.list_facts_for_context('c-46')
    #     print("Facts for context c-46:")
    #     print(facts)
    pass


if __name__ == "__main__":
    main()