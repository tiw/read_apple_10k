#!/usr/bin/env python3
"""
Script to analyze all pre.xml files in magnificent_seven_10k_optimized directory
and extract financial relationship knowledge organized by company and year.
"""

import os
import xml.etree.ElementTree as ET
import re
from pathlib import Path
from collections import defaultdict
import argparse

def parse_pre_xml(file_path):
    """Parse a pre.xml file and extract financial relationships."""
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse XML with string approach to avoid namespace issues
        root = ET.fromstring(content)
        
        # Register namespaces
        ET.register_namespace('link', 'http://www.xbrl.org/2003/linkbase')
        ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
        ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        
        # Get all elements without namespace prefix
        relationships = []
        
        # Find all presentationLink elements
        for presentation_link in root.findall('.//{http://www.xbrl.org/2003/linkbase}presentationLink'):
            role = presentation_link.get('{http://www.w3.org/1999/xlink}role', '')
            
            # Find all presentationArc elements
            for arc in presentation_link.findall('.//{http://www.xbrl.org/2003/linkbase}presentationArc'):
                from_label = arc.get('{http://www.w3.org/1999/xlink}from', '')
                to_label = arc.get('{http://www.w3.org/1999/xlink}to', '')
                order = arc.get('order', '')
                preferred_label = arc.get('preferredLabel', '')
                
                # Find the corresponding loc elements
                from_loc = presentation_link.find(f".//{{http://www.xbrl.org/2003/linkbase}}loc[@{{http://www.w3.org/1999/xlink}}label='{from_label}']")
                to_loc = presentation_link.find(f".//{{http://www.xbrl.org/2003/linkbase}}loc[@{{http://www.w3.org/1999/xlink}}label='{to_label}']")
                
                if from_loc is not None and to_loc is not None:
                    from_href = from_loc.get('{http://www.w3.org/1999/xlink}href', '')
                    to_href = to_loc.get('{http://www.w3.org/1999/xlink}href', '')
                    
                    # Extract concept names from href
                    from_concept = extract_concept_name(from_href)
                    to_concept = extract_concept_name(to_href)
                    
                    # Check if it's a total label
                    is_total = preferred_label.endswith('totalLabel') or 'total' in to_concept.lower()
                    
                    relationships.append({
                        'from_concept': from_concept,
                        'to_concept': to_concept,
                        'order': order,
                        'role': role,
                        'is_total': is_total,
                        'preferred_label': preferred_label
                    })
        
        return relationships
    
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return []

def extract_concept_name(href):
    """Extract concept name from href."""
    if not href:
        return ''
    
    # Extract the part after the last # or /
    if '#' in href:
        concept = href.split('#')[-1]
    else:
        concept = href.split('/')[-1]
    
    # Remove any UUID or random identifier
    concept = re.sub(r'_[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}', '', concept)
    
    return concept

def extract_company_year_from_path(file_path):
    """Extract company and year from file path."""
    path_parts = Path(file_path).parts
    
    # Expected format: .../COMPANY/YYYYMMDD/filename_pre.xml
    company = None
    year = None
    
    for i, part in enumerate(path_parts):
        if part in ['AAPL', 'AMZN', 'GOOGL', 'META', 'MSFT', 'NVDA', 'TSLA']:
            company = part
            # Next part should be the date folder
            if i + 1 < len(path_parts):
                date_folder = path_parts[i + 1]
                if date_folder.isdigit() and len(date_folder) == 8:
                    year = date_folder[:4]
            break
    
    return company, year

def categorize_relationships(relationships):
    """Categorize relationships by financial statement type."""
    categories = {
        'income_statement': [],
        'balance_sheet': [],
        'cash_flow': [],
        'equity': [],
        'other': []
    }
    
    for rel in relationships:
        from_concept = rel['from_concept'].lower()
        to_concept = rel['to_concept'].lower()
        role = rel['role'].lower()
        
        # Income statement indicators
        if any(indicator in role for indicator in ['income', 'revenue', 'earnings', 'profit']) or \
           any(indicator in from_concept for indicator in ['revenue', 'income', 'expense', 'profit']):
            categories['income_statement'].append(rel)
        
        # Balance sheet indicators
        elif any(indicator in role for indicator in ['position', 'balance', 'asset', 'liability']) or \
             any(indicator in from_concept for indicator in ['asset', 'liability', 'equity', 'cash']):
            categories['balance_sheet'].append(rel)
        
        # Cash flow indicators
        elif any(indicator in role for indicator in ['cash', 'flow']) or \
             any(indicator in from_concept for indicator in ['cash', 'flow', 'operating', 'investing', 'financing']):
            categories['cash_flow'].append(rel)
        
        # Equity indicators
        elif any(indicator in role for indicator in ['equity', 'stock']) or \
             any(indicator in from_concept for indicator in ['equity', 'stock', 'share']):
            categories['equity'].append(rel)
        
        else:
            categories['other'].append(rel)
    
    return categories

def generate_markdown_report(company, year, relationships):
    """Generate a markdown report for a company's financial relationships."""
    categories = categorize_relationships(relationships)
    
    report = f"# {company} {year} 财务关系分析\n\n"
    
    for category_name, category_rels in categories.items():
        if not category_rels:
            continue
            
        # Translate category name to Chinese
        category_titles = {
            'income_statement': '损益表结构 (Income Statement Structure)',
            'balance_sheet': '资产负债表结构 (Balance Sheet Structure)',
            'cash_flow': '现金流量表结构 (Cash Flow Structure)',
            'equity': '股东权益结构 (Equity Structure)',
            'other': '其他结构 (Other Structure)'
        }
        
        report += f"## {category_titles[category_name]}\n\n"
        
        # Group by role
        role_groups = defaultdict(list)
        for rel in category_rels:
            role_groups[rel['role']].append(rel)
        
        for role, role_rels in role_groups.items():
            report += f"### {role}\n\n"
            
            # Build hierarchy
            hierarchy = build_hierarchy(role_rels)
            report += format_hierarchy(hierarchy)
            report += "\n"
    
    return report

def build_hierarchy(relationships):
    """Build a hierarchy from relationships."""
    # Create mapping from concept to its children
    concept_map = defaultdict(list)
    concepts = set()
    
    for rel in relationships:
        concepts.add(rel['from_concept'])
        concepts.add(rel['to_concept'])
        concept_map[rel['from_concept']].append(rel)
    
    # Find root concepts (concepts that are not children of any other concept)
    child_concepts = set(rel['to_concept'] for rel in relationships)
    root_concepts = concepts - child_concepts
    
    # Build hierarchy
    hierarchy = {}
    for root in root_concepts:
        hierarchy[root] = build_concept_hierarchy(root, concept_map)
    
    return hierarchy

def build_concept_hierarchy(concept, concept_map):
    """Recursively build hierarchy for a concept."""
    result = {'concept': concept, 'children': []}
    
    for rel in concept_map.get(concept, []):
        child_concept = rel['to_concept']
        child_info = {
            'concept': child_concept,
            'order': rel['order'],
            'is_total': rel['is_total'],
            'children': build_concept_hierarchy(child_concept, concept_map)['children']
        }
        result['children'].append(child_info)
    
    # Sort children by order
    result['children'].sort(key=lambda x: int(x['order']) if x['order'].isdigit() else 0)
    
    return result

def format_hierarchy(hierarchy, indent=0):
    """Format hierarchy as markdown."""
    result = ""
    indent_str = "  " * indent
    
    for concept, children_dict in hierarchy.items():
        # Add main concept
        result += f"{indent_str}- {concept}\n"
        
        # Add children
        for child in children_dict['children']:
            total_label = " [totalLabel]" if child.get('is_total', False) else ""
            result += f"{indent_str}  - {child['concept']}{total_label}\n"
            
            # Add grandchildren recursively
            if child.get('children', []):
                # Format grandchildren with increased indentation
                for grandchild in child['children']:
                    gc_total_label = " [totalLabel]" if grandchild.get('is_total', False) else ""
                    result += f"{indent_str}    - {grandchild['concept']}{gc_total_label}\n"
                    
                    # Add great-grandchildren if they exist
                    if grandchild.get('children', []):
                        for ggchild in grandchild['children']:
                            ggc_total_label = " [totalLabel]" if ggchild.get('is_total', False) else ""
                            result += f"{indent_str}      - {ggchild['concept']}{ggc_total_label}\n"
    
    return result

def main():
    parser = argparse.ArgumentParser(description='Analyze pre.xml files and extract financial relationships')
    parser.add_argument('--input-dir', default='/Users/wangting/work/read_apple_10k/magnificent_seven_10k_optimized',
                       help='Input directory containing pre.xml files')
    parser.add_argument('--output-dir', default='/Users/wangting/work/read_apple_10k/financial_relationships',
                       help='Output directory for generated reports')
    
    args = parser.parse_args()
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Find all pre.xml files
    pre_files = []
    for root, dirs, files in os.walk(args.input_dir):
        for file in files:
            if file.endswith('_pre.xml'):
                pre_files.append(os.path.join(root, file))
    
    print(f"Found {len(pre_files)} pre.xml files")
    
    # Process each file
    company_year_data = defaultdict(list)
    
    for file_path in pre_files:
        print(f"Processing {file_path}")
        
        company, year = extract_company_year_from_path(file_path)
        if not company or not year:
            print(f"  Warning: Could not extract company/year from {file_path}")
            continue
        
        relationships = parse_pre_xml(file_path)
        if relationships:
            company_year_data[(company, year)].extend(relationships)
    
    # Generate reports
    for (company, year), relationships in company_year_data.items():
        print(f"Generating report for {company} {year}")
        
        report = generate_markdown_report(company, year, relationships)
        
        # Create company directory
        company_dir = output_dir / company
        company_dir.mkdir(exist_ok=True)
        
        # Write report
        report_file = company_dir / f"{company}_{year}_financial_relationships.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"  Report saved to {report_file}")
    
    print(f"Analysis complete. Reports saved to {output_dir}")

if __name__ == "__main__":
    main()