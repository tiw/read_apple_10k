#!/usr/bin/env python3
"""
Detailed financial analysis of Magnificent Seven companies with data validation.
"""

import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys

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

def extract_detailed_financials(conn):
    """Extract detailed financial data with validation."""
    cursor = conn.cursor()
    
    query = """
    SELECT 
        xf.file_path,
        xf.fiscal_year,
        ft.tag_name,
        ff.value,
        ff.unit,
        ff.decimals
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
    query += " ORDER BY xf.file_path, ft.tag_name"
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    financial_data = []
    company_mapping = get_company_mapping()
    
    for row in results:
        file_path, fiscal_year, tag_name, value, unit, decimals = row
        
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
            
        # Handle units (convert millions/billions to actual values)
        if numeric_value is not None:
            if unit and 'USD' in unit:
                if 'millions' in unit.lower() or 'M' in unit:
                    numeric_value *= 1e6
                elif 'billions' in unit.lower() or 'B' in unit:
                    numeric_value *= 1e9
        
        data = {
            'company': company_name,
            'ticker': company_ticker,
            'fiscal_year': fiscal_year,
            'tag_name': tag_name,
            'value': numeric_value,
            'metric_category': metric_category,
            'file_path': file_path
        }
        financial_data.append(data)
    
    return financial_data

def validate_financial_data(data):
    """Validate financial data for consistency."""
    df = pd.DataFrame(data)
    
    if df.empty:
        return df
    
    # Group by company and year, taking the first value for each metric
    validated_df = df.groupby(['company', 'ticker', 'fiscal_year', 'metric_category'])['value'].first().unstack()
    
    # Data validation checks
    for idx, row in validated_df.iterrows():
        # Check if gross profit makes sense relative to revenue
        if 'revenue' in row and 'gross_profit' in row:
            revenue = row['revenue']
            gross_profit = row['gross_profit']
            if pd.notna(revenue) and pd.notna(gross_profit):
                if gross_profit > revenue:
                    # This is illogical, likely data error
                    validated_df.loc[idx, 'gross_profit'] = None
                
        # Check if net income is reasonable relative to revenue
        if 'revenue' in row and 'net_income' in row:
            revenue = row['revenue']
            net_income = row['net_income']
            if pd.notna(revenue) and pd.notna(net_income):
                if abs(net_income) > abs(revenue) * 2:  # Net income shouldn't be more than 2x revenue
                    validated_df.loc[idx, 'net_income'] = None
    
    return validated_df

def generate_comprehensive_report(df, output_file=None):
    """Generate a comprehensive financial report."""
    if df.empty:
        print("No financial data found.")
        return
    
    print("=" * 100)
    print("MAGNIFICENT SEVEN - COMPREHENSIVE FINANCIAL ANALYSIS")
    print("=" * 100)
    
    # Print summary by company
    for company in df.index.get_level_values('company').unique():
        company_data = df.xs(company, level='company')
        
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
        df.to_csv(output_file)
        print(f"\nDetailed data saved to: {output_file}")

def main():
    """Main function."""
    db_path = "magnificent_seven_complete.db"
    
    if not os.path.exists(db_path):
        print(f"Database file {db_path} not found.")
        return
    
    print("Connecting to database...")
    conn = connect_db(db_path)
    
    try:
        print("Extracting detailed financial data...")
        financial_data = extract_detailed_financials(conn)
        
        if not financial_data:
            print("No financial data found.")
            return
        
        print(f"Found {len(financial_data)} financial data points")
        
        # Validate and process data
        validated_df = validate_financial_data(financial_data)
        
        # Generate comprehensive report
        output_file = "magnificent_seven_detailed_analysis.csv"
        generate_comprehensive_report(validated_df, output_file)
        
    finally:
        conn.close()

if __name__ == "__main__":
    main()