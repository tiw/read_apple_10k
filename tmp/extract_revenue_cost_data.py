#!/usr/bin/env python3
"""
Extract revenue and cost data for Magnificent Seven companies from XBRL database.

This script extracts the following financial data for the past 10 years:
- Revenue
- Cost of Revenue / Cost of Goods Sold  
- Gross Profit
- Operating Expenses
- Net Income
"""

import sqlite3
import pandas as pd
from datetime import datetime, timedelta
import os
import sys

# Add the tools directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tools'))
import translation

FINANCIAL_TERMS = translation.FINANCIAL_TERMS

# Define the Magnificent Seven companies
MAGNIFICENT_SEVEN = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA']

# Key financial metrics to extract
FINANCIAL_METRICS = {
    'revenue': ['Revenue', 'Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax'],
    'cost_of_revenue': ['CostOfRevenue', 'CostOfGoodsSold'],
    'gross_profit': ['GrossProfit'],
    'operating_expenses': ['OperatingExpenses', 'SellingGeneralAndAdministrativeExpense'],
    'net_income': ['NetIncomeLoss', 'NetIncome'],
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

def extract_company_financials(conn, company_name=None):
    """
    Extract financial data for companies from the database.
    
    Args:
        conn: SQLite database connection
        company_name: Optional specific company to filter by
        
    Returns:
        list: List of financial data dictionaries
    """
    cursor = conn.cursor()
    
    # Build the query
    query = """
    SELECT 
        xf.company_name,
        xf.filing_type,
        xf.fiscal_year,
        xf.fiscal_period,
        xf.period_end_date,
        xf.file_path,
        ft.tag_name,
        ff.value,
        ff.unit,
        ff.decimals,
        c.context_id,
        c.period_type,
        c.instant_date,
        c.start_date,
        c.end_date
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
    
    # Add company filter if specified
    if company_name:
        query += f" AND xf.company_name LIKE '%{company_name}%'"
    
    # Filter for annual reports and recent years
    current_year = datetime.now().year
    query += f" AND xf.fiscal_year >= {current_year - 10}"
    query += " AND xf.filing_type = '10-K'"
    query += " ORDER BY xf.company_name, xf.fiscal_year DESC, ft.tag_name"
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    financial_data = []
    for row in results:
        # Extract company name from file path if not available in database
        company_name = row[0]
        if not company_name and row[5]:  # row[5] is file_path
            file_path = row[5]
            # Extract company from path (e.g., magnificent_seven_10k_optimized/AAPL/...)
            parts = file_path.split('/')
            if len(parts) >= 3 and parts[1] in MAGNIFICENT_SEVEN:
                company_name = parts[1]
            
        data = {
            'company': company_name,
            'filing_type': row[1],
            'fiscal_year': row[2],
            'fiscal_period': row[3],
            'period_end_date': row[4],
            'tag_name': row[6],
            'value': row[7],
            'unit': row[8],
            'decimals': row[9],
            'context_id': row[10],
            'period_type': row[11],
            'instant_date': row[12],
            'start_date': row[13],
            'end_date': row[14],
            'metric_category': get_metric_category(row[6])
        }
        financial_data.append(data)
    
    return financial_data

def get_metric_category(tag_name):
    """Categorize the tag into a financial metric category."""
    tag_name_lower = tag_name.lower()
    
    for category, tags in FINANCIAL_METRICS.items():
        for tag in tags:
            if tag.lower() in tag_name_lower:
                return category
    
    return 'other'

def format_financial_data(data):
    """Format the financial data into a structured format."""
    df = pd.DataFrame(data)
    
    if df.empty:
        return df
    
    # Convert value to numeric
    df['value_numeric'] = pd.to_numeric(df['value'], errors='coerce')
    
    # Filter out non-numeric values
    df = df.dropna(subset=['value_numeric'])
    
    # Group by company, year, and metric
    grouped = df.groupby(['company', 'fiscal_year', 'metric_category'])['value_numeric'].first().unstack()
    
    return grouped

def generate_report(financial_data, output_file=None):
    """Generate a comprehensive financial report."""
    df = format_financial_data(financial_data)
    
    if df.empty:
        print("No financial data found for the specified criteria.")
        return
    
    print("=" * 80)
    print("MAGNIFICENT SEVEN - REVENUE & COST DATA (PAST 10 YEARS)")
    print("=" * 80)
    
    # Print data for each company
    for company in df.index.get_level_values('company').unique():
        company_data = df.xs(company, level='company')
        
        print(f"\n{company.upper()}:")
        print("-" * 40)
        
        for year in sorted(company_data.index, reverse=True):
            year_data = company_data.loc[year]
            print(f"FY {year}:")
            
            for metric in ['revenue', 'cost_of_revenue', 'gross_profit', 'net_income']:
                if metric in year_data:
                    value = year_data[metric]
                    if pd.notna(value):
                        # Format large numbers
                        if abs(value) >= 1e9:
                            formatted = f"${value/1e9:.2f}B"
                        elif abs(value) >= 1e6:
                            formatted = f"${value/1e6:.2f}M"
                        else:
                            formatted = f"${value:,.0f}"
                        
                        metric_name = metric.replace('_', ' ').title()
                        print(f"  {metric_name:<20}: {formatted}")
            
            # Calculate gross margin if both revenue and cost available
            if 'revenue' in year_data and 'cost_of_revenue' in year_data:
                revenue = year_data['revenue']
                cost = year_data['cost_of_revenue']
                if pd.notna(revenue) and pd.notna(cost) and revenue > 0:
                    gross_margin = (revenue - cost) / revenue * 100
                    print(f"  Gross Margin %       : {gross_margin:.1f}%")
            
            print()
    
    # Save to CSV if output file specified
    if output_file:
        df.to_csv(output_file)
        print(f"\nData saved to: {output_file}")

def main():
    """Main function to extract and display financial data."""
    db_path = "magnificent_seven_complete.db"
    
    if not os.path.exists(db_path):
        print(f"Database file {db_path} not found.")
        sys.exit(1)
    
    print("Connecting to database...")
    conn = connect_db(db_path)
    
    try:
        print("Extracting financial data for Magnificent Seven companies...")
        financial_data = extract_company_financials(conn)
        
        if not financial_data:
            print("No financial data found in the database.")
            return
        
        print(f"Found {len(financial_data)} financial data points")
        
        # Generate report
        output_file = "magnificent_seven_financials.csv"
        generate_report(financial_data, output_file)
        
    finally:
        conn.close()

if __name__ == "__main__":
    main()