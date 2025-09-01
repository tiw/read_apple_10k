#!/usr/bin/env python3

import argparse
import sys
import os

# Add the db directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'db'))

from interface import XBRLDatabaseQuery

def connect_to_db(db_path):
    """Connect to the SQLite database."""
    try:
        conn = XBRLDatabaseQuery(db_path)
        conn.connect()
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

def list_companies(conn):
    """List all companies in the database."""
    companies = conn.get_company_list()
    if not companies:
        print("No companies found in the database.")
        return
    
    print("Companies in the database:")
    print("=" * 80)
    print(f"{'ID':<5} {'Company Name':<25} {'Filing Type':<12} {'Fiscal Year':<12} {'Period':<8} {'End Date':<12}")
    print("-" * 80)
    
    for company in companies:
        print(f"{company['id']:<5} {company['company_name'] or 'N/A':<25} {company['filing_type'] or 'N/A':<12} {company['fiscal_year'] or 'N/A':<12} {company['fiscal_period'] or 'N/A':<8} {company['period_end_date'] or 'N/A':<12}")

def list_contexts(conn, file_id=None):
    """List all contexts for a given file ID."""
    contexts = conn.list_all_contexts(file_id)
    
    if not contexts:
        print("No contexts found.")
        return
    
    if file_id:
        print(f"Contexts for file ID {file_id}:")
        print("=" * 30)
        for context in contexts:
            print(f"  {context}")
    else:
        print("All contexts:")
        print("=" * 30)
        for context in contexts:
            print(f"  {context}")

def get_context_info_cli(conn, context_id, file_id=None):
    """Get detailed information about a specific context."""
    context_info = conn.get_context_info(context_id, file_id)
    if not context_info:
        print(f"Context '{context_id}' not found.")
        return
    
    print(f"Context Information for '{context_id}':")
    print("=" * 50)
    print(f"Period: {context_info['period_info']}")
    
    if context_info['dimensions']:
        print("\nDimensions:")
        print("-" * 30)
        for dimension in context_info['dimensions']:
            print(f"  {dimension['dimension']}: {dimension['member']}")

def list_facts_for_context_cli(conn, context_id, file_id=None):
    """List all facts for a specific context."""
    facts = conn.list_facts_for_context(context_id, file_id)
    print(facts)

def search_facts_by_tag(conn, tag_name, file_id=None):
    """Search for facts by tag name across contexts."""
    facts = conn.search_facts_by_tag(f"%{tag_name}%", file_id)
    
    if not facts:
        print("No facts found matching the search criteria.")
        return
    
    print(f"Searching for facts with tag name containing: '{tag_name}'")
    print("=" * 100)
    print(f"{'Company':<20} {'Context ID':<10} {'Tag Name':<30} {'Value':<15}")
    print("-" * 100)
    
    for fact in facts:
        company_name = fact['company_name'] or "N/A"
        context_id = fact['context_id']
        tag_name_full = fact['tag_name']
        value = fact['value'] or ""
        
        # Format large numbers for better readability
        try:
            if '.' not in str(value) and len(str(value)) > 6:  # Likely a large integer
                value = f"{int(value):,}"
            elif '.' in str(value):  # Float
                value = f"{float(value):,}"
        except (ValueError, TypeError):
            pass  # Keep original value if conversion fails
            
        print(f"{company_name:<20} {context_id:<10} {tag_name_full:<30} {str(value):<15}")
    
    print("=" * 100)
    print(f"Total Facts Found: {len(facts)}")

def main():
    parser = argparse.ArgumentParser(description='Query XBRL database')
    parser.add_argument('--db', required=True, help='Path to SQLite database file')
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List companies command
    subparsers.add_parser('list-companies', help='List all companies in the database')
    
    # List contexts command
    list_contexts_parser = subparsers.add_parser('list-contexts', help='List all contexts')
    list_contexts_parser.add_argument('--file-id', type=int, help='Filter by file ID')
    
    # Context info command
    context_info_parser = subparsers.add_parser('context-info', help='Get detailed context information')
    context_info_parser.add_argument('--context-id', required=True, help='Context ID to get information for')
    context_info_parser.add_argument('--file-id', type=int, help='Filter by file ID')
    
    # List facts command
    list_facts_parser = subparsers.add_parser('list-facts', help='List all facts for a context')
    list_facts_parser.add_argument('--context-id', required=True, help='Context ID to list facts for')
    list_facts_parser.add_argument('--file-id', type=int, help='Filter by file ID')
    
    # Search facts command
    search_facts_parser = subparsers.add_parser('search-facts', help='Search facts by tag name')
    search_facts_parser.add_argument('--tag-name', required=True, help='Tag name to search for (can use % for wildcards)')
    search_facts_parser.add_argument('--file-id', type=int, help='Filter by file ID')
    
    args = parser.parse_args()
    
    # Connect to database
    db_query = connect_to_db(args.db)
    
    try:
        if args.command == 'list-companies':
            list_companies(db_query)
        elif args.command == 'list-contexts':
            list_contexts(db_query, args.file_id)
        elif args.command == 'context-info':
            get_context_info_cli(db_query, args.context_id, args.file_id)
        elif args.command == 'list-facts':
            list_facts_for_context_cli(db_query, args.context_id, args.file_id)
        elif args.command == 'search-facts':
            search_facts_by_tag(db_query, args.tag_name, args.file_id)
        else:
            parser.print_help()
    finally:
        db_query.disconnect()

if __name__ == "__main__":
    main()