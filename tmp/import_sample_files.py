#!/usr/bin/env python3
"""
Import a sample of XBRL files from each Magnificent Seven company.
"""

import os
import sys
import sqlite3

# Add the tools and cli directories to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tools'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'xbrl_analyzer', 'cli'))

from importer import import_xbrl_file, find_xbrl_files_in_magnificent_seven

def import_sample_files(db_path, max_files_per_company=3):
    """Import sample files from each company."""
    # Initialize database
    os.system(f"python init_db.py {db_path}")
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    
    try:
        # Get all files
        all_files = find_xbrl_files_in_magnificent_seven('magnificent_seven_10k_optimized')
        
        # Group files by company
        files_by_company = {}
        for file_path in all_files:
            # Extract company from path (e.g., magnificent_seven_10k_optimized/AAPL/...)
            parts = file_path.split('/')
            if len(parts) >= 3:
                company = parts[1]
                if company not in files_by_company:
                    files_by_company[company] = []
                files_by_company[company].append(file_path)
        
        # Import sample files from each company
        total_imported = 0
        for company, files in files_by_company.items():
            if company in ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA']:
                print(f"\nProcessing {company}:")
                print("-" * 30)
                
                # Take the most recent files (sorted by path which includes date)
                sample_files = sorted(files, reverse=True)[:max_files_per_company]
                
                for i, file_path in enumerate(sample_files, 1):
                    print(f"[{i}/{len(sample_files)}] Importing: {file_path}")
                    try:
                        import_xbrl_file(conn, file_path)
                        total_imported += 1
                        print(f"✅ Successfully imported")
                    except Exception as e:
                        print(f"❌ Error: {e}")
    
    finally:
        conn.close()
    
    print(f"\nTotal files imported: {total_imported}")

def main():
    """Main function."""
    db_path = "magnificent_seven_complete.db"
    print(f"Importing sample files to {db_path}...")
    import_sample_files(db_path, max_files_per_company=3)

if __name__ == "__main__":
    main()