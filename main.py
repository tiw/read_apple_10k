#!/usr/bin/env python3

import argparse
import sys
import os

# Add the tools directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))

from tools.context_analyzer import (
    list_all_contexts, 
    list_facts_for_context, 
    list_facts_by_presentation,
    calculate_formulas
)
from tools.financial_statements import generate_financial_statements
from tools.html_table_parser import extract_financial_data_from_html
from tools.translation import FINANCIAL_TERMS

def main():
    parser = argparse.ArgumentParser(description='Process XBRL files.')
    parser.add_argument('--file', help='Path to the XBRL file')
    parser.add_argument('--list-contexts', action='store_true', help='List all contexts')
    parser.add_argument('--context-id', help='Context ID to list facts for')
    parser.add_argument('--presentation', help='Path to the presentation XML file')
    parser.add_argument('--calculation', help='Path to the calculation XML file')
    parser.add_argument('--calculation-filter-zero', action='store_true', help='Filter out calculations where the result is zero')
    parser.add_argument('--generate-statements', action='store_true', help='Generate financial statements')
    parser.add_argument('--xsd', help='Path to the XSD schema file')
    parser.add_argument('--definition', help='Path to the definition linkbase file')
    parser.add_argument('--parse-html-table', help='Path to HTML file containing tables to parse')
    
    args = parser.parse_args()
    
    if args.parse_html_table:
        try:
            with open(args.parse_html_table, 'r', encoding='utf-8') as f:
                html_content = f.read()
            result = extract_financial_data_from_html(html_content)
            print(result)
        except Exception as e:
            print(f"Error parsing HTML table: {e}")
        return
    
    if args.list_contexts:
        if not args.file:
            print("Error: --file is required when using --list-contexts")
            sys.exit(1)
        contexts = list_all_contexts(args.file)
        print("Available Contexts:")
        for context in contexts:
            print(f"  {context}")
        return
    
    if args.generate_statements:
        if not args.file:
            print("Error: --file is required when using --generate-statements")
            sys.exit(1)
        if not args.xsd or not args.definition:
            print("Error: --xsd and --definition are required when using --generate-statements")
            sys.exit(1)
        result = generate_financial_statements(args.file, args.xsd, args.definition, args.context_id)
        print(result)
        return
    
    if args.calculation:
        if not args.file:
            print("Error: --file is required when using --calculation")
            sys.exit(1)
        if not args.context_id:
            print("Error: --context-id is required when using --calculation")
            sys.exit(1)
        result = calculate_formulas(args.file, args.context_id, args.calculation, args.calculation_filter_zero)
        print(result)
        return
    
    if args.presentation:
        if not args.file:
            print("Error: --file is required when using --presentation")
            sys.exit(1)
        if not args.context_id:
            print("Error: --context-id is required when using --presentation")
            sys.exit(1)
        result = list_facts_by_presentation(args.file, args.context_id, args.presentation)
        print(result)
        return
    
    if args.context_id:
        if not args.file:
            print("Error: --file is required when using --context-id")
            sys.exit(1)
        result = list_facts_for_context(args.file, args.context_id)
        print(result)
        return
    
    # If no arguments provided, show help
    parser.print_help()

if __name__ == "__main__":
    main()