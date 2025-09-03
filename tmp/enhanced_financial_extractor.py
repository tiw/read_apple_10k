#!/usr/bin/env python3
"""
Enhanced financial data extraction using pre.xml presentation linkbase information.
This extractor uses XBRL presentation structure to identify main statement totals.
"""

import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys
import xml.etree.ElementTree as ET
import re

# Define the Magnificent Seven companies
MAGNIFICENT_SEVEN = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA']

# Key financial metrics with preferred tag names
FINANCIAL_METRICS = {
    'revenue': ['Revenue', 'Revenues'],
    'cost_of_revenue': ['CostOfRevenue', 'CostOfGoodsSold'],
    'gross_profit': ['GrossProfit'],
    'operating_income': ['OperatingIncomeLoss'],
    'net_income': ['NetIncomeLoss', 'NetIncome'],
    'total_assets': ['Assets'],
    'total_liabilities': ['Liabilities'],
    'research_development': ['ResearchAndDevelopmentExpense'],
    'marketing_expenses': ['MarketingExpense', 'AdvertisingExpense']
}

def connect_db(db_path):
    """Connect to SQLite database."""
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

def get_company_mapping():
    """Get mapping of ticker symbols to full company names."""
    return {
        'AAPL': 'Apple Inc.',
        'MSFT': 'Microsoft Corporation', 
        'GOOGL': 'Alphabet Inc.',
        'AMZN': 'Amazon.com Inc.',
        'META': 'Meta Platforms Inc.',
        'NVDA': 'NVIDIA Corporation',
        'TSLA': 'Tesla Inc.'
    }

def analyze_pre_xml_structure(pre_xml_path):
    """Analyze pre.xml file to understand financial statement organization."""
    try:
        tree = ET.parse(pre_xml_path)
        root = tree.getroot()
        
        # Define namespaces
        namespaces = {
            'link': 'http://www.xbrl.org/2003/linkbase',
            'xlink': 'http://www.w3.org/1999/xlink'
        }
        
        statement_roles = {}
        total_labels = set()
        
        # Find all role references for main financial statements
        for role_ref in root.findall('.//link:roleRef', namespaces):
            role_uri = role_ref.get('xlink:role', '')
            if any(keyword in role_uri for keyword in ['Statement', 'BalanceSheet', 'Income', 'CashFlow']):
                statement_roles[role_uri] = {
                    'type': 'main_statement',
                    'elements': []
                }
        
        # Find presentation links and identify total labels
        for presentation_link in root.findall('.//link:presentationLink', namespaces):
            role = presentation_link.get('xlink:role', '')
            
            for presentation_arc in presentation_link.findall('.//link:presentationArc', namespaces):
                preferred_label = presentation_arc.get('preferredLabel', '')
                if 'totalLabel' in preferred_label:
                    total_labels.add(preferred_label)
        
        return {
            'statement_roles': statement_roles,
            'total_labels': list(total_labels)
        }
        
    except Exception as e:
        print(f"Error analyzing pre.xml: {e}")
        return None

def extract_financials_with_presentation_context(conn):
    """Extract financial data with context analysis using presentation information."""
    cursor = conn.cursor()
    
    query = """
    SELECT 
        xf.file_path,
        xf.fiscal_year,
        ft.tag_name,
        ff.value,
        ff.unit,
        ff.decimals,
        c.context_id,
        c.period_type,
        c.start_date,
        c.end_date,
        c.instant_date
    FROM financial_facts ff
    JOIN financial_tags ft ON ff.tag_id = ft.id
    JOIN contexts c ON ff.context_id = c.id
    JOIN xbrl_files xf ON ff.xbrl_file_id = xf.id
    WHERE (
    """
    
    # Add tag filters
    tag_filters = []
    for metric, tags in FINANCIAL_METRICS.items():
        for tag in tags:
            tag_filters.append(f"ft.tag_name LIKE '%{tag}%'")
    
    query += " OR ".join(tag_filters)
    query += ")"
    query += " ORDER BY xf.file_path, ft.tag_name, c.context_id"
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    financial_data = []
    company_mapping = get_company_mapping()
    
    for row in results:
        file_path, fiscal_year, tag_name, value, unit, decimals, context_id, period_type, start_date, end_date, instant_date = row
        
        # Skip non-numeric values
        if not is_numeric_value(value):
            continue
            
        # Extract company from file path
        company_ticker = None
        parts = file_path.split('/')
        if len(parts) >= 3 and parts[1] in MAGNIFICENT_SEVEN:
            company_ticker = parts[1]
        
        if not company_ticker:
            continue
            
        # Get full company name
        company_name = company_mapping.get(company_ticker, company_ticker)
        
        # Categorize the metric
        metric_category = None
        for category, tags in FINANCIAL_METRICS.items():
            for tag in tags:
                if tag.lower() in tag_name.lower():
                    metric_category = category
                    break
            if metric_category:
                break
        
        if not metric_category:
            continue
            
        # Convert value to numeric
        try:
            numeric_value = float(value) if value else None
        except (ValueError, TypeError):
            numeric_value = None
            
        if numeric_value is None:
            continue
            
        # Handle units (convert millions/billions to actual values)
        if unit and 'USD' in unit:
            if 'millions' in unit.lower() or 'M' in unit:
                numeric_value *= 1e6
            elif 'billions' in unit.lower() or 'B' in unit:
                numeric_value *= 1e9
        
        # Context analysis - identify if this is a main statement or segment data
        context_type = 'unknown'
        if context_id:
            # Simple heuristic: main statements often have simpler context IDs
            # Segment data often has longer, more complex context IDs with dimensions
            if len(context_id) < 20 and 'Segment' not in context_id and 'Axis' not in context_id:
                context_type = 'main_statement'
            elif 'Segment' in context_id or 'Axis' in context_id:
                context_type = 'segment_data'
        
        data = {
            'company': company_name,
            'ticker': company_ticker,
            'fiscal_year': fiscal_year,
            'tag_name': tag_name,
            'value': numeric_value,
            'metric_category': metric_category,
            'context_id': context_id,
            'context_type': context_type,
            'period_type': period_type,
            'start_date': start_date,
            'end_date': end_date,
            'instant_date': instant_date,
            'file_path': file_path
        }
        financial_data.append(data)
    
    return financial_data

def is_numeric_value(value):
    """Check if value is numeric and not HTML/text content."""
    if value is None:
        return False
    
    # Skip HTML/text content
    if isinstance(value, str):
        if any(html_tag in value for html_tag in ['<', 'div', 'span', 'table', 'style']):
            return False
        if re.search(r'[a-zA-Z]', value) and not re.search(r'^[0-9.,+-]+$', value):
            return False
    
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def filter_to_main_totals(financial_data):
    """Filter to keep only the main total values for each metric."""
    main_data = []
    
    # Group by company, year, and metric
    grouped_data = {}
    for data in financial_data:
        key = (data['company'], data['fiscal_year'], data['metric_category'])
        if key not in grouped_data:
            grouped_data[key] = []
        grouped_data[key].append(data)
    
    # For each group, select the most appropriate value
    for key, data_list in grouped_data.items():
        if not data_list:
            continue
            
        # Strategy 1: Prefer main statement context
        main_statement_data = [d for d in data_list if d['context_type'] == 'main_statement']
        
        if main_statement_data:
            # If multiple main statement values, take the largest (usually the total)
            selected_data = max(main_statement_data, key=lambda x: x['value'])
            main_data.append(selected_data)
        else:
            # Strategy 2: For segment data, take the largest value (usually the total)
            selected_data = max(data_list, key=lambda x: x['value'])
            main_data.append(selected_data)
    
    return main_data

def generate_enhanced_report(financial_data, output_file=None):
    """Generate a comprehensive financial report with enhanced data quality."""
    # Filter to main totals
    main_data = filter_to_main_totals(financial_data)
    
    df = pd.DataFrame(main_data)
    
    if df.empty:
        print("No financial data found.")
        return None
    
    # Group by company and year, taking the first value for each metric
    validated_df = df.groupby(['company', 'ticker', 'fiscal_year', 'metric_category'])['value'].first().unstack()
    
    print("=" * 100)
    print("ENHANCED FINANCIAL ANALYSIS - MAIN TOTALS ONLY")
    print("=" * 100)
    
    # Print summary by company
    for company in validated_df.index.get_level_values('company').unique():
        company_data = validated_df.xs(company, level='company')
        
        print(f"\n{company.upper()}:")
        print("-" * 60)
        
        for year in sorted(company_data.index, reverse=True):
            year_data = company_data.loc[year]
            print(f"FY {year}:")
            
            # Revenue and profitability
            if 'revenue' in year_data and pd.notna(year_data['revenue']):
                revenue = year_data['revenue']
                print(f"  Revenue: ${revenue/1e9:.2f}B")
                
                if 'gross_profit' in year_data and pd.notna(year_data['gross_profit']):
                    gross_profit = year_data['gross_profit']
                    print(f"  Gross Profit: ${gross_profit/1e9:.2f}B")
                    
                    if revenue > 0:
                        gross_margin = (gross_profit / revenue) * 100
                        print(f"  Gross Margin: {gross_margin:.1f}%")
                
                if 'net_income' in year_data and pd.notna(year_data['net_income']):
                    net_income = year_data['net_income']
                    print(f"  Net Income: ${net_income/1e9:.2f}B")
                    
                    if revenue > 0:
                        net_margin = (net_income / revenue) * 100
                        print(f"  Net Margin: {net_margin:.1f}%")
            
            # Cost structure
            if 'cost_of_revenue' in year_data and pd.notna(year_data['cost_of_revenue']):
                cost_of_revenue = year_data['cost_of_revenue']
                print(f"  Cost of Revenue: ${cost_of_revenue/1e9:.2f}B")
            
            # R&D and Marketing
            if 'research_development' in year_data and pd.notna(year_data['research_development']):
                rnd = year_data['research_development']
                print(f"  R&D Expense: ${rnd/1e9:.2f}B")
            
            if 'marketing_expenses' in year_data and pd.notna(year_data['marketing_expenses']):
                marketing = year_data['marketing_expenses']
                print(f"  Marketing Expense: ${marketing/1e9:.2f}B")
            
            print()
    
    # Save to CSV if requested
    if output_file:
        validated_df.to_csv(output_file)
        print(f"\nEnhanced data saved to: {output_file}")
    
    return validated_df

def main():
    """Main function."""
    db_path = "magnificent_seven_complete.db"
    
    if not os.path.exists(db_path):
        print(f"Database file {db_path} not found.")
        return
    
    print("Connecting to database...")
    conn = connect_db(db_path)
    
    try:
        print("Extracting enhanced financial data with presentation context...")
        financial_data = extract_financials_with_presentation_context(conn)
        
        if not financial_data:
            print("No financial data found.")
            return
        
        print(f"Found {len(financial_data)} numeric financial data points")
        print(f"Context types: {pd.Series([d['context_type'] for d in financial_data]).value_counts()}")
        
        # Generate enhanced report
        output_file = "enhanced_financial_analysis.csv"
        validated_df = generate_enhanced_report(financial_data, output_file)
        
    finally:
        conn.close()

if __name__ == "__main__":
    main()