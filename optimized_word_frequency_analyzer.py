#!/usr/bin/env python3
"""
Optimized word frequency analyzer for XBRL files - high performance version.
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
import pickle

class OptimizedWordTokenizer:
    """High-performance tokenizer for financial terms."""
    
    def __init__(self, min_length=4):
        self.min_length = min_length
        self._compile_regexes()
        self._load_skip_words()
        
    def _compile_regexes(self):
        """Pre-compile all regex patterns for performance."""
        # Pre-compiled patterns for better performance
        self.word_pattern = re.compile(r'\b[a-zA-Z][a-zA-Z0-9]*\b')
        self.camel_pattern = re.compile(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)')
        self.digit_pattern = re.compile(r'^\d+$')
        
        # XML extraction patterns
        self.xml_tag_pattern = re.compile(r'<([^>]+)>')
        self.xml_attr_pattern = re.compile(r'(\w+)=["\'][^"\']*["\']')
        self.concept_pattern = re.compile(r'href=["\']([^"\']*\.xsd#([^"\']*))["\']')
        
        # Text cleaning patterns
        self.attr_clean_pattern = re.compile(r'\s+[^=]*=["\'][^"\']*["\']')
        
    def _load_skip_words(self):
        """Load skip words into a set for O(1) lookup."""
        self.skip_words = {
            # XML artifacts
            'xml', 'xsd', 'xlink', 'xmlns', 'xsi', 'xbrl', 'link', 'type', 'role', 'label',
            'loc', 'href', 'arcrole', 'from', 'to', 'lang', 'preferred', 'terse', 'verbose',
            # HTML artifacts
            'style', 'colspan', 'rowspan', 'bgcolor', 'valign', 'align', 'width', 'height',
            'border', 'cellpadding', 'cellspacing', 'class', 'id', 'div', 'span', 'table',
            'tr', 'td', 'th', 'p', 'br', 'hr', 'ul', 'li', 'ol',
            # Common non-financial terms
            'http', 'https', 'www', 'com', 'org', 'net', 'gov', 'edu', 'html', 'htm',
            # Years and numbers
            '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015',
            '2014', '2013', '2012', '2011', '2010',
            # Schema elements
            'schema', 'element', 'attribute', 'simpletype', 'complextype', 'restriction',
            'extension', 'sequence', 'choice', 'all', 'annotation', 'documentation',
            # Namespace prefixes
            'us', 'gaap', 'dei', 'xbrldi', 'xbrli', 'link', 'xlink',
            # File extensions
            'xml', 'xsd', 'htm', 'html', 'txt', 'pdf', 'doc', 'docx',
            # Common attributes
            'id', 'name', 'type', 'value', 'default', 'required', 'optional', 'fixed',
            'nillable', 'abstract', 'substitution', 'block', 'final',
            # Units
            'usd', 'eur', 'gbp', 'jpy', 'cny', 'shares', 'units',
        }
        
        # Financial term patterns for identification
        self.financial_patterns = [
            'asset', 'liabilit', 'equit', 'revenue', 'expense', 'income', 'profit', 'loss',
            'cash', 'debt', 'ratio', 'margin', 'return', 'yield', 'growth', 'operating',
            'financing', 'investing', 'acquisition', 'merger', 'dividend', 'earnings',
            'share', 'derivative', 'security', 'bond', 'stock', 'option', 'quarter',
            'annual', 'fiscal', 'period', 'year', 'amortization', 'depreciation',
            'impairment', 'provision', 'reserve', 'allowance', 'receivable', 'payable'
        ]
    
    def tokenize_camel_case_fast(self, word: str) -> List[str]:
        """Fast camelCase splitting."""
        parts = self.camel_pattern.findall(word)
        return [part.lower() for part in parts if len(part) >= self.min_length]
    
    def should_skip_fast(self, word: str) -> bool:
        """Fast word skipping using set lookup."""
        return word.lower() in self.skip_words
    
    def is_financial_term(self, word: str) -> bool:
        """Check if word is a financial term."""
        word_lower = word.lower()
        return any(pattern in word_lower for pattern in self.financial_patterns)
    
    def tokenize_text_fast(self, text: str) -> List[str]:
        """Fast text tokenization."""
        words = []
        for match in self.word_pattern.finditer(text):
            word = match.group()
            
            if len(word) < self.min_length:
                continue
                
            if self.digit_pattern.match(word):
                continue
                
            if self.should_skip_fast(word):
                continue
            
            # Fast camelCase processing
            camel_parts = self.tokenize_camel_case_fast(word)
            if len(camel_parts) > 1:
                words.extend(camel_parts)
            else:
                words.append(word.lower())
        
        return words
    
    def tokenize_file_content_optimized(self, content: str) -> List[str]:
        """Optimized file content tokenization."""
        all_words = []
        
        # Extract XML tags
        for tag in self.xml_tag_pattern.finditer(content):
            tag_clean = self.attr_clean_pattern.sub('', tag.group(1))
            words = self.tokenize_text_fast(tag_clean)
            all_words.extend(words)
        
        # Extract attributes
        for attr in self.xml_attr_pattern.finditer(content):
            words = self.tokenize_text_fast(attr.group(1))
            all_words.extend(words)
        
        # Extract concepts
        for match in self.concept_pattern.finditer(content):
            concept = match.group(2)  # Get the concept part
            words = self.tokenize_text_fast(concept)
            all_words.extend(words)
        
        # Extract remaining text
        text_content = self.xml_tag_pattern.sub(' ', content)
        words = self.tokenize_text_fast(text_content)
        all_words.extend(words)
        
        return all_words

class OptimizedWordFrequencyAnalyzer:
    """High-performance analyzer with optimized processing."""
    
    def __init__(self, db_path: str = "optimized_word_frequencies.db"):
        self.db_path = db_path
        self.tokenizer = OptimizedWordTokenizer(min_length=4)
        self._init_database()
        
    def _init_database(self):
        """Initialize SQLite database with optimized schema."""
        with sqlite3.connect(self.db_path) as conn:
            # Use WAL mode for better concurrent access
            conn.execute('PRAGMA journal_mode=WAL')
            conn.execute('PRAGMA synchronous=NORMAL')
            conn.execute('PRAGMA cache_size=10000')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS checkpoints (
                    file_path TEXT PRIMARY KEY,
                    processed_at TIMESTAMP,
                    file_size INTEGER,
                    word_counts BLOB
                )
            ''')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS word_frequencies (
                    word TEXT PRIMARY KEY,
                    count INTEGER,
                    last_updated TIMESTAMP,
                    is_financial BOOLEAN DEFAULT 0
                )
            ''')
            
            conn.execute('CREATE INDEX IF NOT EXISTS idx_word_count ON word_frequencies(count DESC)')
            conn.execute('CREATE INDEX IF NOT EXISTS idx_financial ON word_frequencies(is_financial, count DESC)')
    
    def get_unprocessed_files(self, root_dir: str) -> List[str]:
        """Get unprocessed files with file size checking."""
        all_files = []
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file.endswith(('.xml', '.xsd', '.htm', '.txt')):
                    file_path = os.path.join(root, file)
                    all_files.append(file_path)
        
        # Get processed files with sizes
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('SELECT file_path, file_size FROM checkpoints')
            processed_files = {row[0]: row[1] for row in cursor.fetchall()}
        
        # Check for modified files
        unprocessed_files = []
        for file_path in all_files:
            file_size = os.path.getsize(file_path)
            if file_path not in processed_files or processed_files[file_path] != file_size:
                unprocessed_files.append(file_path)
        
        return unprocessed_files
    
    def process_file_optimized(self, file_path: str) -> Tuple[Dict[str, int], int]:
        """Optimized file processing."""
        word_counts = {}
        file_size = 0
        
        try:
            file_size = os.path.getsize(file_path)
            
            # Read file in chunks for memory efficiency
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            # Tokenize content
            words = self.tokenizer.tokenize_file_content_optimized(content)
            
            # Count words using Counter for better performance
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
        
        return word_counts, file_size
    
    def process_file_with_checkpoint(self, file_path: str) -> Dict[str, int]:
        """Process file with optimized checkpoint."""
        word_counts, file_size = self.process_file_optimized(file_path)
        
        # Save checkpoint using pickle for better performance
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT OR REPLACE INTO checkpoints (file_path, processed_at, file_size, word_counts)
                VALUES (?, ?, ?, ?)
            ''', (file_path, datetime.now(), file_size, pickle.dumps(word_counts)))
            
        return word_counts
    
    def batch_update_database(self, word_counts_batch: List[Dict[str, int]]):
        """Batch update database for better performance."""
        merged_counts = {}
        
        # Merge all word counts
        for word_counts in word_counts_batch:
            for word, count in word_counts.items():
                merged_counts[word] = merged_counts.get(word, 0) + count
        
        # Batch insert
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('BEGIN TRANSACTION')
            try:
                for word, count in merged_counts.items():
                    conn.execute('''
                        INSERT INTO word_frequencies (word, count, last_updated)
                        VALUES (?, ?, ?)
                        ON CONFLICT(word) DO UPDATE SET count = count + ?
                    ''', (word, count, datetime.now(), count))
                conn.execute('COMMIT')
            except Exception as e:
                conn.execute('ROLLBACK')
                raise e
    
    def identify_financial_terms_batch(self, words: List[str]) -> Set[str]:
        """Batch identify financial terms."""
        financial_terms = set()
        for word in words:
            if self.tokenizer.is_financial_term(word):
                financial_terms.add(word)
        return financial_terms
    
    def process_directory_optimized(self, root_dir: str, num_processes: int = None):
        """Optimized directory processing."""
        if num_processes is None:
            num_processes = min(cpu_count(), 8)
            
        print(f"Starting optimized analysis with {num_processes} processes...")
        print(f"Database: {self.db_path}")
        
        # Get unprocessed files
        unprocessed_files = self.get_unprocessed_files(root_dir)
        total_files = len(unprocessed_files)
        
        if total_files == 0:
            print("All files have been processed!")
            return
            
        print(f"Found {total_files} unprocessed files")
        
        # Process files in larger batches for better performance
        batch_size = 200  # Increased batch size
        start_time = time.time()
        
        for i in range(0, total_files, batch_size):
            batch_end = min(i + batch_size, total_files)
            batch_files = unprocessed_files[i:batch_end]
            
            print(f"Processing batch {i//batch_size + 1}/{(total_files + batch_size - 1)//batch_size}")
            print(f"Files {i+1}-{batch_end} of {total_files}")
            
            batch_start = time.time()
            
            # Process batch in parallel
            with Pool(num_processes) as pool:
                batch_results = pool.map(self.process_file_with_checkpoint, batch_files)
            
            # Batch update database
            self.batch_update_database(batch_results)
            
            # Progress update
            batch_time = time.time() - batch_start
            elapsed = time.time() - start_time
            files_processed = batch_end
            files_per_second = files_processed / elapsed if elapsed > 0 else 0
            
            print(f"Batch time: {batch_time:.1f}s")
            print(f"Progress: {files_processed}/{total_files} files ({files_processed/total_files*100:.1f}%)")
            print(f"Overall speed: {files_per_second:.1f} files/second")
            
            # Show current top words
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute('SELECT word, count FROM word_frequencies ORDER BY count DESC LIMIT 10')
                top_words = cursor.fetchall()
            
            print(f"Current top words: {', '.join([f'{word}({count})' for word, count in top_words])}")
            print("-" * 50)
        
        # Final analysis - identify financial terms
        print("Identifying financial terms...")
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('SELECT word FROM word_frequencies')
            all_words = [row[0] for row in cursor.fetchall()]
        
        financial_terms = self.identify_financial_terms_batch(all_words)
        
        # Update financial terms in database
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('BEGIN TRANSACTION')
            try:
                for word in financial_terms:
                    conn.execute('''
                        UPDATE word_frequencies SET is_financial = 1 WHERE word = ?
                    ''', (word,))
                conn.execute('COMMIT')
            except Exception as e:
                conn.execute('ROLLBACK')
                raise e
        
        print("Optimized analysis complete!")
        
        # Show final results
        self.show_results()
    
    def get_all_words(self, financial_only: bool = False) -> List[Tuple[str, int]]:
        """Get all words by frequency."""
        with sqlite3.connect(self.db_path) as conn:
            if financial_only:
                cursor = conn.execute('''
                    SELECT word, count FROM word_frequencies 
                    WHERE is_financial = 1
                    ORDER BY count DESC
                ''')
            else:
                cursor = conn.execute('''
                    SELECT word, count FROM word_frequencies 
                    ORDER BY count DESC
                ''')
            return cursor.fetchall()
    
    def get_top_words(self, limit: int = 100, financial_only: bool = False) -> List[Tuple[str, int]]:
        """Get top words by frequency."""
        all_words = self.get_all_words(financial_only)
        return all_words[:limit]
    
    def show_results(self):
        """Display final results."""
        print("\n" + "="*60)
        print("OPTIMIZED FINAL RESULTS")
        print("="*60)
        
        # Get all words
        all_words = self.get_all_words()
        all_financial = self.get_all_words(financial_only=True)
        
        print(f"\nTotal unique words: {len(all_words)}")
        print(f"Total financial terms: {len(all_financial)}")
        
        print(f"\nTop 20 Overall Words:")
        print("-" * 40)
        for i, (word, count) in enumerate(all_words[:20], 1):
            print(f"{i:3d}. {word:<25} {count:>8}")
        
        print(f"\nTop 20 Financial Terms:")
        print("-" * 40)
        for i, (word, count) in enumerate(all_financial[:20], 1):
            print(f"{i:3d}. {word:<25} {count:>8}")
        
        # Save complete results to files
        with open("complete_vocabulary_ranked.txt", 'w', encoding='utf-8') as f:
            f.write("Complete Financial Vocabulary - Ranked by Frequency\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Total unique words: {len(all_words)}\n")
            f.write(f"Total financial terms: {len(all_financial)}\n\n")
            
            f.write("ALL WORDS RANKED BY FREQUENCY:\n")
            f.write("=" * 60 + "\n")
            for i, (word, count) in enumerate(all_words, 1):
                f.write(f"{i:5d}. {word:<30} {count:>10}\n")
            
            f.write("\n\nFINANCIAL TERMS RANKED BY FREQUENCY:\n")
            f.write("=" * 60 + "\n")
            for i, (word, count) in enumerate(all_financial, 1):
                f.write(f"{i:5d}. {word:<30} {count:>10}\n")
        
        # Also save separate files for easier access
        with open("all_words.txt", 'w', encoding='utf-8') as f:
            for word, count in all_words:
                f.write(f"{word}\t{count}\n")
        
        with open("financial_terms.txt", 'w', encoding='utf-8') as f:
            for word, count in all_financial:
                f.write(f"{word}\t{count}\n")
        
        print(f"\nComplete results saved to:")
        print(f"  - complete_vocabulary_ranked.txt (formatted)")
        print(f"  - all_words.txt (tab-separated)")
        print(f"  - financial_terms.txt (tab-separated)")
        print(f"Database: {self.db_path}")

def main():
    parser = argparse.ArgumentParser(description='Optimized word frequency analyzer for XBRL files')
    parser.add_argument('--dir', '-d', default='magnificent_seven_10k_optimized',
                       help='Directory to analyze')
    parser.add_argument('--processes', '-p', type=int,
                       help='Number of processes to use')
    parser.add_argument('--db', default='optimized_word_frequencies.db',
                       help='Database file path')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.dir):
        print(f"Directory {args.dir} does not exist!")
        sys.exit(1)
    
    analyzer = OptimizedWordFrequencyAnalyzer(args.db)
    analyzer.process_directory_optimized(args.dir, args.processes)

if __name__ == '__main__':
    main()