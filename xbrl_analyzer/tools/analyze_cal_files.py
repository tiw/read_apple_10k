#!/usr/bin/env python3
"""
Script to analyze all cal.xml files in magnificent_seven_10k_optimized directory
and extract financial calculation logic organized by company and year.
"""

import os
import xml.etree.ElementTree as ET
import re
from pathlib import Path
from collections import defaultdict
import argparse

def parse_cal_xml(file_path):
    """Parse a cal.xml file and extract financial calculation relationships."""
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
        
        calculations = []
        
        # Find all calculation links
        for calculation_link in root.findall('.//{http://www.xbrl.org/2003/linkbase}calculationLink'):
            role = calculation_link.get('{http://www.w3.org/1999/xlink}role', '')
            
            # Find all calculation arcs (relationships)
            for arc in calculation_link.findall('.//{http://www.xbrl.org/2003/linkbase}calculationArc'):
                from_label = arc.get('{http://www.w3.org/1999/xlink}from', '')
                to_label = arc.get('{http://www.w3.org/1999/xlink}to', '')
                weight = arc.get('weight', '')
                order = arc.get('order', '')
                
                # Find the corresponding loc elements to get concept names
                from_loc = calculation_link.find(f".//{{http://www.xbrl.org/2003/linkbase}}loc[@{{http://www.w3.org/1999/xlink}}label='{from_label}']")
                to_loc = calculation_link.find(f".//{{http://www.xbrl.org/2003/linkbase}}loc[@{{http://www.w3.org/1999/xlink}}label='{to_label}']")
                
                if from_loc is not None and to_loc is not None:
                    from_href = from_loc.get('{http://www.w3.org/1999/xlink}href', '')
                    to_href = to_loc.get('{http://www.w3.org/1999/xlink}href', '')
                    
                    # Extract concept names from href
                    from_concept = extract_concept_name(from_href)
                    to_concept = extract_concept_name(to_href)
                    
                    calculations.append({
                        'from_concept': from_concept,
                        'to_concept': to_concept,
                        'weight': weight,
                        'order': order,
                        'role': role
                    })
        
        return calculations
    
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
    
    # Expected format: .../COMPANY/YYYYMMDD/filename_cal.xml
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

def get_role_category(role):
    """Categorize calculation role by financial statement type."""
    role_lower = role.lower()
    
    if 'operations' in role_lower or 'income' in role_lower or 'earnings' in role_lower:
        return '损益表计算逻辑 (Income Statement Calculations)'
    elif 'balance' in role_lower or 'position' in role_lower or 'asset' in role_lower or 'liability' in role_lower:
        return '资产负债表计算逻辑 (Balance Sheet Calculations)'
    elif 'cash' in role_lower or 'flow' in role_lower:
        return '现金流量表计算逻辑 (Cash Flow Calculations)'
    elif 'comprehensive' in role_lower:
        return '全面收益计算逻辑 (Comprehensive Income Calculations)'
    elif 'earningspershare' in role_lower or 'diluted' in role_lower:
        return '每股收益计算逻辑 (Earnings Per Share Calculations)'
    elif 'financial' in role_lower and 'instrument' in role_lower:
        return '金融工具计算逻辑 (Financial Instruments Calculations)'
    else:
        return '其他计算逻辑 (Other Calculations)'

def format_calculation_relationship(calc):
    """Format a calculation relationship for display."""
    weight = float(calc['weight']) if calc['weight'] else 1.0
    operator = '+' if weight > 0 else '-'
    
    return f"{calc['from_concept']} {operator} {calc['to_concept']}"

def generate_markdown_report(company, year, calculations):
    """Generate a markdown report for a company's financial calculations."""
    # Group calculations by role
    role_groups = defaultdict(list)
    for calc in calculations:
        role_groups[calc['role']].append(calc)
    
    report = f"# {company} {year} 财务计算逻辑分析\n\n"
    
    # Group by category
    category_groups = defaultdict(list)
    for role, calcs in role_groups.items():
        category = get_role_category(role)
        category_groups[category].append((role, calcs))
    
    for category, role_calcs in category_groups.items():
        report += f"## {category}\n\n"
        
        for role, calcs in role_calcs:
            # Clean up role name for display
            role_name = role.split('/')[-1] if '/' in role else role
            role_name = role_name.replace('_', ' ')
            report += f"### {role_name}\n\n"
            
            # Group calculations by parent concept
            parent_groups = defaultdict(list)
            for calc in calcs:
                parent_groups[calc['from_concept']].append(calc)
            
            for parent, child_calcs in parent_groups.items():
                report += f"#### {parent}\n\n"
                
                # Sort by order
                child_calcs.sort(key=lambda x: int(x['order']) if x['order'].isdigit() else 0)
                
                for calc in child_calcs:
                    formula = format_calculation_relationship(calc)
                    report += f"- {formula}\n"
                
                report += "\n"
    
    # Add summary section
    report += "## 主要计算公式总结\n\n"
    
    # Extract key formulas from each category
    key_formulas = extract_key_formulas(calculations)
    for formula in key_formulas:
        report += f"- {formula}\n"
    
    return report

def extract_key_formulas(calculations):
    """Extract key financial formulas from calculations."""
    key_concepts = {
        'GrossProfit': '毛利',
        'OperatingIncomeLoss': '营业利润',
        'NetIncomeLoss': '净利润',
        'Assets': '总资产',
        'Liabilities': '总负债',
        'StockholdersEquity': '股东权益',
        'ComprehensiveIncomeNetOfTax': '全面收益',
        'CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecrease': '现金变动'
    }
    
    formulas = []
    concept_map = defaultdict(list)
    
    # Build concept mapping
    for calc in calculations:
        concept_map[calc['from_concept']].append(calc)
    
    # Extract formulas for key concepts
    for concept, chinese_name in key_concepts.items():
        if concept in concept_map:
            calcs = concept_map[concept]
            components = []
            
            for calc in calcs:
                weight = float(calc['weight']) if calc['weight'] else 1.0
                operator = '+' if weight > 0 else '-'
                components.append(f"{operator} {calc['to_concept']}")
            
            if components:
                formula = f"{chinese_name} ({concept}): {concept} = {' '.join(components)}"
                formulas.append(formula)
    
    return formulas

def main():
    parser = argparse.ArgumentParser(description='Analyze cal.xml files and extract financial calculation logic')
    parser.add_argument('--input-dir', default='/Users/wangting/work/read_apple_10k/magnificent_seven_10k_optimized',
                       help='Input directory containing cal.xml files')
    parser.add_argument('--output-dir', default='/Users/wangting/work/read_apple_10k/financial_calculations',
                       help='Output directory for generated reports')
    
    args = parser.parse_args()
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Find all cal.xml files
    cal_files = []
    for root, dirs, files in os.walk(args.input_dir):
        for file in files:
            if file.endswith('_cal.xml'):
                cal_files.append(os.path.join(root, file))
    
    print(f"Found {len(cal_files)} cal.xml files")
    
    # Process each file
    company_year_data = defaultdict(list)
    
    for file_path in cal_files:
        print(f"Processing {file_path}")
        
        company, year = extract_company_year_from_path(file_path)
        if not company or not year:
            print(f"  Warning: Could not extract company/year from {file_path}")
            continue
        
        calculations = parse_cal_xml(file_path)
        if calculations:
            company_year_data[(company, year)].extend(calculations)
    
    # Generate reports
    for (company, year), calculations in company_year_data.items():
        print(f"Generating report for {company} {year}")
        
        report = generate_markdown_report(company, year, calculations)
        
        # Create company directory
        company_dir = output_dir / company
        company_dir.mkdir(exist_ok=True)
        
        # Write report
        report_file = company_dir / f"{company}_{year}_financial_calculations.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"  Report saved to {report_file}")
    
    print(f"Analysis complete. Reports saved to {output_dir}")

if __name__ == "__main__":
    main()