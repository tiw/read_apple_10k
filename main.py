#!/usr/bin/env python3

import argparse
import os
import sys

# Add the tools directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))

from tools.context_analyzer import (
    list_all_contexts as list_contexts, 
    list_facts_for_context as get_facts_for_context, 
    list_facts_by_presentation,
    calculate_formulas
)
from tools.html_table_parser import extract_financial_data_from_html
from tools.financial_statements import generate_financial_statements
from tools.revenue_analyzer import analyze_revenue_by_product

def main():
    parser = argparse.ArgumentParser(description='Process Apple 10-K XBRL files')
    parser.add_argument('--file', help='XBRL instance document file path')
    parser.add_argument('--list-contexts', action='store_true', help='List all contexts in the instance document')
    parser.add_argument('--context-id', help='Context ID to analyze')
    parser.add_argument('--presentation', help='Presentation linkbase file path')
    parser.add_argument('--calculation', help='Calculation linkbase file path')
    parser.add_argument('--calculation-filter-zero', action='store_true', help='Filter out zero-value calculations')
    parser.add_argument('--parse-html-table', help='HTML file path to parse tables from')
    parser.add_argument('--generate-statements', action='store_true', help='Generate financial statements from XBRL data')
    parser.add_argument('--xsd', help='XSD schema file path')
    parser.add_argument('--definition', help='Definition linkbase file path')
    parser.add_argument('--analyze-revenue', action='store_true', help='Analyze revenue by product')
    
    args = parser.parse_args()
    
    # HTML table parsing
    if args.parse_html_table:
        with open(args.parse_html_table, 'r') as f:
            html_content = f.read()
        result = extract_financial_data_from_html(html_content)
        print(result)
        return

    # Check if file argument is provided
    if not args.file:
        print("Error: --file argument is required")
        return

    # List contexts
    if args.list_contexts:
        result = list_contexts(args.file)
        print("Contexts in XBRL instance document:")
        for context in result:
            print(f"  - {context}")
        return

    # Context analysis
    if args.context_id:
        # With presentation linkbase
        if args.presentation:
            result = list_facts_by_presentation(args.file, args.context_id, args.presentation)
            print(result)
            return
        # With calculation linkbase
        elif args.calculation:
            result = calculate_formulas(args.file, args.context_id, args.calculation, args.calculation_filter_zero)
            print(result)
            return
        # Basic context facts
        else:
            result = get_facts_for_context(args.file, args.context_id)
            print(result)
            return

    # Generate financial statements
    if args.generate_statements:
        if not args.xsd or not args.definition:
            print("Error: --xsd and --definition arguments are required for --generate-statements")
            return
        result = generate_financial_statements(args.file, args.xsd, args.definition, args.context_id)
        print(result)
        return

    # Analyze revenue by product
    if args.analyze_revenue:
        if not args.xsd or not args.definition:
            print("Error: --xsd and --definition arguments are required for --analyze-revenue")
            return
        result = analyze_revenue_by_product(args.file, args.xsd, args.definition, args.context_id)
        print(result)
        return
    
    # If no arguments provided, show help
    parser.print_help()

if __name__ == "__main__":
    main()