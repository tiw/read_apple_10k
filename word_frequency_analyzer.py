#!/usr/bin/env python3
"""
Word frequency analyzer for XBRL files with parallel processing and checkpoint support.
"""

import re
import sqlite3
import os
import sys
import argparse
from pathlib import Path
from multiprocessing import Pool, cpu_count
from typing import Dict, List, Set, Tuple
import time
from datetime import datetime
import json

class WordTokenizer:
    """Tokenizer for camelCase, underscore, and hyphen separated words."""
    
    def __init__(self, min_length=4):
        self.min_length = min_length
        # Patterns for different word separators
        self.camel_case_pattern = re.compile(r'([a-z])([A-Z])')
        self.underscore_pattern = re.compile(r'_')
        self.hyphen_pattern = re.compile(r'-')
        self.number_pattern = re.compile(r'^\d+$')
        self.uuid_pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
        self.alphanumeric_pattern = re.compile(r'^[a-zA-Z0-9]+$')
        
    def tokenize(self, text: str) -> List[str]:
        """Extract words from text using various splitting strategies."""
        words = []
        
        # Remove common prefixes/suffixes that aren't meaningful
        text = re.sub(r'^loc_', '', text)
        text = re.sub(r'^loc-', '', text)
        text = re.sub(r'Member$', '', text)
        text = re.sub(r'Domain$', '', text)
        text = re.sub(r'Axis$', '', text)
        text = re.sub(r'Table$', '', text)
        
        # Clean up XML artifacts
        text = re.sub(r'xlink:href="[^"]*"', '', text)
        text = re.sub(r'xlink:label="[^"]*"', '', text)
        text = re.sub(r'xlink:type="[^"]*"', '', text)
        text = re.sub(r'xmlns:[^=]*="[^"]*"', '', text)
        text = re.sub(r'xml:lang="[^"]*"', '', text)
        text = re.sub(r'preferredLabel="[^"]*"', '', text)
        text = re.sub(r'xlink:arcrole="[^"]*"', '', text)
        text = re.sub(r'xlink:from="[^"]*"', '', text)
        text = re.sub(r'xlink:to="[^"]*"', '', text)
        text = re.sub(r'xsi:schemaLocation="[^"]*"', '', text)
        text = re.sub(r'roleURI="[^"]*"', '', text)
        
        # Split by underscores first
        parts = self.underscore_pattern.split(text)
        
        for part in parts:
            # Split by hyphens
            sub_parts = self.hyphen_pattern.split(part)
            
            for sub_part in sub_parts:
                # Handle camelCase
                camel_parts = self.camel_case_pattern.split(sub_part)
                
                for word in camel_parts:
                    word = word.strip()
                    if self._is_valid_word(word):
                        words.append(word.lower())
        
        return words
    
    def _is_valid_word(self, word: str) -> bool:
        """Check if word meets criteria for inclusion."""
        if len(word) < self.min_length:
            return False
        
        # Skip pure numbers
        if self.number_pattern.match(word):
            return False
            
        # Skip UUIDs
        if self.uuid_pattern.match(word):
            return False
            
        # Skip words with no letters
        if not re.search(r'[a-zA-Z]', word):
            return False
            
        # Skip common non-financial terms and XML artifacts
        common_skip = {
            'http', 'www', 'com', 'org', 'xml', 'xhtml', 'xlink', 'schema', 
            'xsi', 'xmlns', 'xbrl', 'link', 'type', 'role', 'label', 
            'loc', 'href', 'arcrole', 'from', 'to', 'lang', 'preferred',
            'ters', 'ef', 'xsd', 'id', 'uni', 'decimals', 'contex', 'abel',
            'usd', 'resource', 'namespace', 'locus', 'locusd', 'loclabel',
            '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015',
            'xbrldi', 'elts', 'sec', 'gov', 'fasb', 'us', 'gaap', 'dei',
            'style', 'colspan', 'order', 'preferre', 'weight', 'value', 'default',
            'reports', 'name', 'abstract', 'nillable', 'period', 'group', 'report',
            'short', 'long', 'instance', 'text', 'block', 'inline', 'table'
        }
        if word.lower() in common_skip:
            return False
            
        # Skip fragments that look like XML artifacts
        if re.search(r'^[\'"/\\=]', word) or re.search(r'[\'"/\\=]$', word):
            return False
            
        return True

class WordFrequencyAnalyzer:
    """Main analyzer class with parallel processing and checkpoint support."""
    
    def __init__(self, db_path: str = "word_frequencies.db"):
        self.db_path = db_path
        self.tokenizer = WordTokenizer(min_length=4)
        self._init_database()
        
    def _init_database(self):
        """Initialize SQLite database for checkpoints and results."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS checkpoints (
                    file_path TEXT PRIMARY KEY,
                    processed_at TIMESTAMP,
                    word_counts TEXT
                )
            ''')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS word_frequencies (
                    word TEXT PRIMARY KEY,
                    count INTEGER,
                    last_updated TIMESTAMP
                )
            ''')
            
            conn.execute('''
                CREATE INDEX IF NOT EXISTS idx_word_count ON word_frequencies(count DESC)
            ''')
            
    def get_unprocessed_files(self, root_dir: str) -> List[str]:
        """Get list of files that haven't been processed yet."""
        all_files = []
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file.endswith(('.xml', '.xsd', '.htm', '.txt')):
                    file_path = os.path.join(root, file)
                    all_files.append(file_path)
        
        # Get already processed files
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('SELECT file_path FROM checkpoints')
            processed_files = {row[0] for row in cursor.fetchall()}
        
        # Return unprocessed files
        return [f for f in all_files if f not in processed_files]
    
    def process_file(self, file_path: str) -> Dict[str, int]:
        """Process a single file and return word frequencies."""
        word_counts = {}
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            # Extract XML tags (without attributes)
            xml_tags = re.findall(r'<([^>]+)>', content)
            
            # Extract attribute names
            xml_attrs = re.findall(r'(\w+)=["\'][^"\']*["\']', content)
            
            # Extract namespace prefixes and values
            namespaces = re.findall(r'xmlns:([^=]+)=["\'][^"\']*["\']', content)
            
            # Extract concept names from href attributes
            concepts = re.findall(r'href=["\']([^"\']*\.xsd#([^"\']*))["\']', content)
            
            # Process all text components
            all_words = []
            
            # Process XML tags
            for tag in xml_tags:
                # Remove attributes from tag
                tag = re.sub(r'\s+[^=]*=["\'][^"\']*["\']', '', tag)
                all_words.extend(self.tokenizer.tokenize(tag))
            
            # Process attributes
            for attr in xml_attrs:
                all_words.extend(self.tokenizer.tokenize(attr))
            
            # Process namespaces
            for ns in namespaces:
                all_words.extend(self.tokenizer.tokenize(ns))
            
            # Process concepts
            for full_concept, concept in concepts:
                all_words.extend(self.tokenizer.tokenize(concept))
            
            # Count words
            for word in all_words:
                word_counts[word] = word_counts.get(word, 0) + 1
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            
        return word_counts
    
    def process_file_with_checkpoint(self, file_path: str) -> Dict[str, int]:
        """Process file and save checkpoint."""
        word_counts = self.process_file(file_path)
        
        # Save checkpoint
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT OR REPLACE INTO checkpoints (file_path, processed_at, word_counts)
                VALUES (?, ?, ?)
            ''', (file_path, datetime.now(), json.dumps(word_counts)))
            
        return word_counts
    
    def merge_word_counts(self, results: List[Dict[str, int]]) -> Dict[str, int]:
        """Merge word counts from multiple files."""
        merged = {}
        for word_counts in results:
            for word, count in word_counts.items():
                merged[word] = merged.get(word, 0) + count
        return merged
    
    def save_final_results(self, word_counts: Dict[str, int]):
        """Save final word frequencies to database."""
        with sqlite3.connect(self.db_path) as conn:
            # Clear existing data
            conn.execute('DELETE FROM word_frequencies')
            
            # Insert new data
            for word, count in word_counts.items():
                conn.execute('''
                    INSERT OR REPLACE INTO word_frequencies (word, count, last_updated)
                    VALUES (?, ?, ?)
                ''', (word, count, datetime.now()))
                
    def get_top_words(self, limit: int = 100) -> List[Tuple[str, int]]:
        """Get top N words by frequency."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT word, count FROM word_frequencies 
                ORDER BY count DESC 
                LIMIT ?
            ''', (limit,))
            return cursor.fetchall()
    
    def process_directory(self, root_dir: str, num_processes: int = None):
        """Process all files in directory with parallel processing."""
        if num_processes is None:
            num_processes = min(cpu_count(), 8)
            
        print(f"Starting analysis with {num_processes} processes...")
        print(f"Database: {self.db_path}")
        
        # Get unprocessed files
        unprocessed_files = self.get_unprocessed_files(root_dir)
        total_files = len(unprocessed_files)
        
        if total_files == 0:
            print("All files have been processed!")
            return
            
        print(f"Found {total_files} unprocessed files")
        
        # Process files in batches
        batch_size = 100
        start_time = time.time()
        
        for i in range(0, total_files, batch_size):
            batch_end = min(i + batch_size, total_files)
            batch_files = unprocessed_files[i:batch_end]
            
            print(f"Processing batch {i//batch_size + 1}/{(total_files + batch_size - 1)//batch_size}")
            print(f"Files {i+1}-{batch_end} of {total_files}")
            
            # Process batch in parallel
            with Pool(num_processes) as pool:
                batch_results = pool.map(self.process_file_with_checkpoint, batch_files)
            
            # Merge results and save
            batch_merged = self.merge_word_counts(batch_results)
            
            # Update global counts
            with sqlite3.connect(self.db_path) as conn:
                for word, count in batch_merged.items():
                    conn.execute('''
                        INSERT INTO word_frequencies (word, count, last_updated)
                        VALUES (?, ?, ?)
                        ON CONFLICT(word) DO UPDATE SET count = count + ?
                    ''', (word, count, datetime.now(), count))
            
            # Progress update
            elapsed = time.time() - start_time
            files_processed = batch_end
            files_per_second = files_processed / elapsed if elapsed > 0 else 0
            
            print(f"Progress: {files_processed}/{total_files} files ({files_processed/total_files*100:.1f}%)")
            print(f"Speed: {files_per_second:.1f} files/second")
            
            # Show current top words
            top_words = self.get_top_words(10)
            print(f"Current top words: {', '.join([f'{word}({count})' for word, count in top_words])}")
            print("-" * 50)
        
        print("Analysis complete!")
        
        # Show final results
        self.show_results()
    
    def show_results(self):
        """Display final results."""
        print("\n" + "="*60)
        print("FINAL RESULTS")
        print("="*60)
        
        # Get top 100 words
        top_words = self.get_top_words(100)
        
        print(f"\nTop 100 Financial Vocabulary Words:")
        print("-" * 40)
        
        for i, (word, count) in enumerate(top_words, 1):
            print(f"{i:3d}. {word:<25} {count:>8}")
        
        # Save to file
        output_file = "financial_vocabulary_ranked.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Financial Vocabulary - Ranked by Frequency\n")
            f.write("=" * 50 + "\n\n")
            for i, (word, count) in enumerate(top_words, 1):
                f.write(f"{i:3d}. {word:<25} {count:>8}\n")
        
        print(f"\nResults saved to: {output_file}")
        print(f"Database: {self.db_path}")

def main():
    parser = argparse.ArgumentParser(description='Analyze word frequencies in XBRL files')
    parser.add_argument('--dir', '-d', default='magnificent_seven_10k_optimized',
                       help='Directory to analyze')
    parser.add_argument('--processes', '-p', type=int,
                       help='Number of processes to use')
    parser.add_argument('--db', default='word_frequencies.db',
                       help='Database file path')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.dir):
        print(f"Directory {args.dir} does not exist!")
        sys.exit(1)
    
    analyzer = WordFrequencyAnalyzer(args.db)
    analyzer.process_directory(args.dir, args.processes)

if __name__ == '__main__':
    main()