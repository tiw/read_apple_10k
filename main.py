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
from tools.translation import FINANCIAL_TERMS


def main():
    parser = argparse.ArgumentParser(description='Process XBRL files.')
    parser.add_argument('--file', required=True, help='Path to the XBRL file')
    parser.add_argument('--list-contexts', action='store_true', help='List all contexts')
    parser.add_argument('--context-id', help='Context ID to list facts for')
    parser.add_argument('--presentation', help='Path to the presentation XML file')
    parser.add_argument('--calculation', help='Path to the calculation XML file')
    parser.add_argument('--calculation-filter-zero', action='store_true', help='Filter out calculations where all factors are zero')
    parser.add_argument('--namespaces', action='store_true', help='Extract namespaces')
    
    args = parser.parse_args()
    
    
    if args.namespaces:
        namespaces = extract_namespaces(args.file)
        print("Namespaces in the XBRL file:")
        for prefix, uri in namespaces.items():
            print(f"  {prefix}: {uri}")
        return
    
    if args.list_contexts:
        contexts = list_all_contexts(args.file)
        print("Available Contexts:")
        for context in contexts:
            print(f"  {context}")
        return
    
    if args.calculation:
        if not args.context_id:
            print("Error: --context-id is required when using --calculation")
            sys.exit(1)
        result = calculate_formulas(args.file, args.context_id, args.calculation, args.calculation_filter_zero)
        print(result)
        return
    
    if args.presentation:
        if not args.context_id:
            print("Error: --context-id is required when using --presentation")
            sys.exit(1)
        result = list_facts_by_presentation(args.file, args.context_id, args.presentation)
        print(result)
        return
    
    if args.context_id:
        result = list_facts_for_context(args.file, args.context_id)
        print(result)
        return
    
    # If no arguments provided, show help
    parser.print_help()


if __name__ == "__main__":
    main()