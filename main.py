#!/usr/bin/env python3
"""
Main entry point for the XBRL analysis tool
"""

import argparse
import sys
from tools.context_analyzer import analyze_contexts, list_facts_for_context


def main():
    parser = argparse.ArgumentParser(description='Analyze XBRL files for GAAP facts and contexts')
    parser.add_argument('--file', required=True, help='Path to the XBRL file to analyze')
    parser.add_argument('--output', help='Output file path (optional, prints to console if not specified)')
    parser.add_argument('--context-id', help='List all facts for a specific context ID')
    
    args = parser.parse_args()
    
    try:
        if args.context_id:
            result = list_facts_for_context(args.file, args.context_id)
        else:
            result = analyze_contexts(args.file)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(result)
            print(f"Results written to {args.output}")
        else:
            print(result)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()