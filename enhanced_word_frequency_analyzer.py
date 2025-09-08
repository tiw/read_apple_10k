#!/usr/bin/env python3
"""
Enhanced word frequency analyzer for XBRL files using spaCy for better tokenization.
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

try:
    import spacy
    from spacy.tokenizer import Tokenizer
    from spacy.util import compile_prefix_regex, compile_suffix_regex, compile_infix_regex
    from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER, CONCAT_QUOTES
    SPACY_AVAILABLE = True
except ImportError:
    SPACY_AVAILABLE = False
    print("Warning: spaCy not available. Using basic tokenizer. Install with: pip install spacy")

class AdvancedWordTokenizer:
    """Advanced tokenizer using spaCy with custom rules for financial terms."""
    
    def __init__(self, min_length=4):
        self.min_length = min_length
        self.nlp = None
        self._setup_spacy()
        
    def _setup_spacy(self):
        """Setup spaCy with custom tokenization rules for financial data."""
        if not SPACY_AVAILABLE:
            return
            
        try:
            # Load a small English model or create blank one
            try:
                self.nlp = spacy.load("en_core_web_sm")
            except OSError:
                # If model not available, create blank one
                self.nlp = spacy.blank("en")
            
            # Custom infix patterns for financial data
            # Don't split on common financial patterns
            infixes = [
                r"(?<=[0-9])[+\-*/^](?=[0-9-])",  # Keep mathematical expressions together
                r"(?<=[{al}{q}])\.(?=[{au}{q}])".format(
                    al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
                ),
                r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
                # Keep camelCase words together for special handling
                r"(?<=[a-z])(?=[A-Z])",  # camelCase boundaries
            ]
            
            infix_re = compile_infix_regex(infixes)
            self.nlp.tokenizer.infix_finditer = infix_re.finditer
            
            # Add special cases for common financial terms
            financial_terms = {
                "EBITDA": [{"ORTH": "EBITDA"}],
                "GAAP": [{"ORTH": "GAAP"}],
                "IFRS": [{"ORTH": "IFRS"}],
                "XBRL": [{"ORTH": "XBRL"}],
                "SEC": [{"ORTH": "SEC"}],
                "FASB": [{"ORTH": "FASB"}],
                "IASB": [{"ORTH": "IASB"}],
                "EPS": [{"ORTH": "EPS"}],
                "ROI": [{"ORTH": "ROI"}],
                "EBIT": [{"ORTH": "EBIT"}],
                "NOPAT": [{"ORTH": "NOPAT"}],
                "WACC": [{"ORTH": "WACC"}],
                "ROE": [{"ORTH": "ROE"}],
                "ROA": [{"ORTH": "ROA"}],
                "P/E": [{"ORTH": "P/E"}],
                "EPS": [{"ORTH": "EPS"}],
            }
            
            for term, case in financial_terms.items():
                self.nlp.tokenizer.add_special_case(term, case)
                
        except Exception as e:
            print(f"Warning: Failed to setup spaCy: {e}")
            self.nlp = None
    
    def tokenize_camel_case(self, word: str) -> List[str]:
        """Split camelCase words into components."""
        # Split on capital letters preceded by lowercase letters
        parts = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)', word)
        return [part.lower() for part in parts if len(part) >= self.min_length]
    
    def tokenize_with_spacy(self, text: str) -> List[str]:
        """Tokenize using spaCy with additional financial term processing."""
        words = []
        
        if self.nlp is None:
            # Fallback to basic tokenization
            return self._basic_tokenize(text)
        
        try:
            doc = self.nlp(text)
            
            for token in doc:
                word = token.text.lower().strip()
                
                # Skip tokens that are too short or pure numbers
                if len(word) < self.min_length:
                    continue
                    
                if word.isdigit():
                    continue
                
                # Skip XML artifacts and common non-financial terms
                if self._should_skip_word(word):
                    continue
                
                # Handle camelCase in tokens
                camel_parts = self.tokenize_camel_case(token.text)
                if len(camel_parts) > 1:
                    words.extend(camel_parts)
                else:
                    words.append(word)
                    
        except Exception as e:
            # Fallback to basic tokenization
            words.extend(self._basic_tokenize(text))
        
        return words
    
    def _basic_tokenize(self, text: str) -> List[str]:
        """Basic tokenization fallback."""
        words = []
        
        # Extract words using regex
        word_pattern = re.compile(r'\b[a-zA-Z][a-zA-Z0-9]*\b')
        for match in word_pattern.finditer(text):
            word = match.group().lower()
            
            if len(word) < self.min_length:
                continue
                
            if word.isdigit():
                continue
                
            if self._should_skip_word(word):
                continue
            
            # Handle camelCase
            camel_parts = self.tokenize_camel_case(word)
            if len(camel_parts) > 1:
                words.extend(camel_parts)
            else:
                words.append(word)
        
        return words
    
    def _should_skip_word(self, word: str) -> bool:
        """Check if word should be skipped."""
        skip_patterns = {
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
        
        return word.lower() in skip_patterns
    
    def tokenize_file_content(self, content: str) -> List[str]:
        """Tokenize file content with various extraction methods."""
        all_words = []
        
        # Extract XML tags and attributes
        xml_tags = re.findall(r'<([^>]+)>', content)
        xml_attrs = re.findall(r'(\w+)=["\'][^"\']*["\']', content)
        
        # Extract concept names from href attributes
        concepts = re.findall(r'href=["\']([^"\']*\.xsd#([^"\']*))["\']', content)
        
        # Process XML tags
        for tag in xml_tags:
            # Remove attributes from tag
            tag_clean = re.sub(r'\s+[^=]*=["\'][^"\']*["\']', '', tag)
            words = self.tokenize_with_spacy(tag_clean)
            all_words.extend(words)
        
        # Process attributes
        for attr in xml_attrs:
            words = self.tokenize_with_spacy(attr)
            all_words.extend(words)
        
        # Process concepts
        for full_concept, concept in concepts:
            words = self.tokenize_with_spacy(concept)
            all_words.extend(words)
        
        # Process any remaining text content
        text_content = re.sub(r'<[^>]+>', ' ', content)
        words = self.tokenize_with_spacy(text_content)
        all_words.extend(words)
        
        return all_words

class EnhancedWordFrequencyAnalyzer:
    """Enhanced analyzer with spaCy integration and better financial term recognition."""
    
    def __init__(self, db_path: str = "enhanced_word_frequencies.db"):
        self.db_path = db_path
        self.tokenizer = AdvancedWordTokenizer(min_length=4)
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
                    last_updated TIMESTAMP,
                    is_financial BOOLEAN DEFAULT 0
                )
            ''')
            
            conn.execute('''
                CREATE INDEX IF NOT EXISTS idx_word_count ON word_frequencies(count DESC)
            ''')
            
            conn.execute('''
                CREATE INDEX IF NOT EXISTS idx_financial ON word_frequencies(is_financial, count DESC)
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
                
            # Tokenize content
            words = self.tokenizer.tokenize_file_content(content)
            
            # Count words
            for word in words:
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
    
    def identify_financial_terms(self, word_counts: Dict[str, int]) -> Set[str]:
        """Identify likely financial terms based on patterns and frequency."""
        financial_terms = set()
        
        # Known financial term patterns
        financial_patterns = {
            # Accounting terms
            r'.*asset.*', r'.*liabilit.*', r'.*equity.*', r'.*revenue.*', r'.*expense.*',
            r'.*income.*', r'.*profit.*', r'.*loss.*', r'.*cash.*', r'.*debt.*',
            # Financial ratios
            r'.*ratio.*', r'.*margin.*', r'.*return.*', r'.*yield.*', r'.*growth.*',
            # Business operations
            r'.*operating.*', r'.*financing.*', r'.*investing.*', r'.*acquisition.*',
            r'.*merger.*', r'.*dividend.*', r'.*earnings.*', r'.*share.*',
            # Financial instruments
            r'.*derivative.*', r'.*security.*', r'.*bond.*', r'.*stock.*', r'.*option.*',
            # Time periods
            r'.*quarter.*', r'.*annual.*', r'.*fiscal.*', r'.*period.*', r'.*year.*',
            # Specific financial concepts
            r'.*amortization.*', r'.*depreciation.*', r'.*impairment.*', r'.*provision.*',
            r'.*reserve.*', r'.*allowance.*', r'.*receivable.*', r'.*payable.*',
        }
        
        for word in word_counts.keys():
            word_lower = word.lower()
            for pattern in financial_patterns:
                if re.match(pattern, word_lower):
                    financial_terms.add(word)
                    break
        
        return financial_terms
    
    def save_final_results(self, word_counts: Dict[str, int]):
        """Save final word frequencies to database with financial term identification."""
        financial_terms = self.identify_financial_terms(word_counts)
        
        with sqlite3.connect(self.db_path) as conn:
            # Clear existing data
            conn.execute('DELETE FROM word_frequencies')
            
            # Insert new data
            for word, count in word_counts.items():
                is_financial = word in financial_terms
                conn.execute('''
                    INSERT OR REPLACE INTO word_frequencies (word, count, last_updated, is_financial)
                    VALUES (?, ?, ?, ?)
                ''', (word, count, datetime.now(), is_financial))
    
    def get_top_words(self, limit: int = 100, financial_only: bool = False) -> List[Tuple[str, int]]:
        """Get top N words by frequency."""
        with sqlite3.connect(self.db_path) as conn:
            if financial_only:
                cursor = conn.execute('''
                    SELECT word, count FROM word_frequencies 
                    WHERE is_financial = 1
                    ORDER BY count DESC 
                    LIMIT ?
                ''', (limit,))
            else:
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
            
        print(f"Starting enhanced analysis with {num_processes} processes...")
        print(f"Using spaCy: {SPACY_AVAILABLE}")
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
        
        # Final analysis - identify financial terms
        print("Identifying financial terms...")
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('SELECT word, count FROM word_frequencies')
            all_word_counts = {row[0]: row[1] for row in cursor.fetchall()}
        
        self.save_final_results(all_word_counts)
        
        print("Enhanced analysis complete!")
        
        # Show final results
        self.show_results()
    
    def show_results(self):
        """Display final results."""
        print("\n" + "="*60)
        print("ENHANCED FINAL RESULTS")
        print("="*60)
        
        # Get top 100 words overall
        top_words = self.get_top_words(100)
        top_financial = self.get_top_words(50, financial_only=True)
        
        print(f"\nTop 20 Overall Words:")
        print("-" * 40)
        for i, (word, count) in enumerate(top_words[:20], 1):
            print(f"{i:3d}. {word:<25} {count:>8}")
        
        print(f"\nTop 20 Financial Terms:")
        print("-" * 40)
        for i, (word, count) in enumerate(top_financial[:20], 1):
            print(f"{i:3d}. {word:<25} {count:>8}")
        
        # Save to files
        with open("enhanced_vocabulary_ranked.txt", 'w', encoding='utf-8') as f:
            f.write("Enhanced Financial Vocabulary - Ranked by Frequency\n")
            f.write("=" * 60 + "\n\n")
            f.write("Top 100 Overall Words:\n")
            f.write("-" * 40 + "\n")
            for i, (word, count) in enumerate(top_words, 1):
                f.write(f"{i:3d}. {word:<25} {count:>8}\n")
            
            f.write("\n\nTop 50 Financial Terms:\n")
            f.write("-" * 40 + "\n")
            for i, (word, count) in enumerate(top_financial, 1):
                f.write(f"{i:3d}. {word:<25} {count:>8}\n")
        
        print(f"\nResults saved to: enhanced_vocabulary_ranked.txt")
        print(f"Database: {self.db_path}")

def main():
    parser = argparse.ArgumentParser(description='Enhanced word frequency analyzer for XBRL files')
    parser.add_argument('--dir', '-d', default='magnificent_seven_10k_optimized',
                       help='Directory to analyze')
    parser.add_argument('--processes', '-p', type=int,
                       help='Number of processes to use')
    parser.add_argument('--db', default='enhanced_word_frequencies.db',
                       help='Database file path')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.dir):
        print(f"Directory {args.dir} does not exist!")
        sys.exit(1)
    
    if SPACY_AVAILABLE:
        print("✓ spaCy is available - using enhanced tokenization")
    else:
        print("⚠ spaCy not available - using basic tokenization")
        print("  Install spaCy for better results: pip install spacy")
    
    analyzer = EnhancedWordFrequencyAnalyzer(args.db)
    analyzer.process_directory(args.dir, args.processes)

if __name__ == '__main__':
    main()