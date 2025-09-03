#!/usr/bin/env python3

import sqlite3
import os
import sys

# Add the tools directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tools'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'xbrl_analyzer', 'cli'))

from importer import import_xbrl_file, find_xbrl_files_in_magnificent_seven

def test_import_subset():
    # Initialize database
    db_path = "test_subset.db"
    if os.path.exists(db_path):
        os.remove(db_path)
    
    # Run init_db to create schema
    os.system(f"python init_db.py {db_path}")
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    
    try:
        # Get all files but only process first 3
        files = find_xbrl_files_in_magnificent_seven('magnificent_seven_10k_optimized')
        subset = files[:3]
        
        print(f"Testing import of {len(subset)} files:")
        
        for i, xbrl_file in enumerate(subset, 1):
            print(f"\n[{i}/{len(subset)}] Importing: {xbrl_file}")
            try:
                import_xbrl_file(conn, xbrl_file)
                print(f"✅ Successfully imported {xbrl_file}")
            except Exception as e:
                print(f"❌ Error importing {xbrl_file}: {e}")
    
    finally:
        conn.close()

if __name__ == "__main__":
    test_import_subset()