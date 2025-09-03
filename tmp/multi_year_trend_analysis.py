#!/usr/bin/env python3
"""
Comprehensive multi-year trend analysis for Magnificent Seven companies.
Extracts correct revenue totals using context analysis.
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Define the Magnificent Seven companies
MAGNIFICENT_SEVEN = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA']

def connect_db(db_path):
    """Connect to SQLite database."""
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

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

def extract_revenue_trends(conn):
    """Extract revenue trends with proper context filtering."""
    cursor = conn.cursor()
    
    query = """
    SELECT 
        xf.company_name,
        xf.fiscal_year,
        ft.tag_name,
        ff.value,
        c.context_id,
        c.start_date,
        c.end_date
    FROM financial_facts ff
    JOIN financial_tags ft ON ff.tag_id = ft.id
    JOIN contexts c ON ff.context_id = c.id
    JOIN xbrl_files xf ON ff.xbrl_file_id = xf.id
    WHERE ft.tag_name = 'SalesRevenueNet'
    AND c.period_type = 'duration'
    AND c.context_id LIKE '%_364_%'  -- Full fiscal year contexts
    AND xf.fiscal_year IS NOT NULL
    ORDER BY xf.company_name, xf.fiscal_year
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    revenue_data = []
    for row in results:
        company_name, fiscal_year, tag_name, value, context_id, start_date, end_date = row
        
        # Convert value to numeric
        try:
            numeric_value = float(value) if value else None
        except (ValueError, TypeError):
            numeric_value = None
            
        if numeric_value is None:
            continue
            
        data = {
            'company': company_name,
            'fiscal_year': fiscal_year,
            'revenue': numeric_value,
            'context_id': context_id,
            'start_date': start_date,
            'end_date': end_date
        }
        revenue_data.append(data)
    
    return revenue_data

def generate_trend_report(revenue_data, output_file=None):
    """Generate comprehensive trend analysis report."""
    df = pd.DataFrame(revenue_data)
    
    if df.empty:
        print("No revenue data found for trend analysis.")
        return None
    
    # Group by company and year
    trend_df = df.groupby(['company', 'fiscal_year'])['revenue'].first().unstack().T
    
    print("=" * 100)
    print("MAGNIFICENT SEVEN - REVENUE TREND ANALYSIS")
    print("=" * 100)
    
    # Print trend for each company
    for company in trend_df.columns:
        company_data = trend_df[company].dropna()
        if not company_data.empty:
            print(f"\n{company.upper()}:")
            print("-" * 60)
            
            for year, revenue in company_data.items():
                print(f"FY {year}: ${revenue/1e9:.2f}B")
            
            # Calculate growth rates if multiple years
            if len(company_data) > 1:
                years = sorted(company_data.index)
                first_year = years[0]
                last_year = years[-1]
                
                first_revenue = company_data[first_year]
                last_revenue = company_data[last_year]
                
                if first_revenue > 0:
                    cagr = ((last_revenue / first_revenue) ** (1/(last_year - first_year)) - 1) * 100
                    total_growth = ((last_revenue - first_revenue) / first_revenue) * 100
                    
                    print(f"  CAGR ({first_year}-{last_year}): {cagr:.1f}%")
                    print(f"  Total Growth: {total_growth:.1f}%")
    
    # Create visualization
    plt.figure(figsize=(12, 8))
    
    # Pivot for plotting
    pivot_df = df.pivot_table(index='fiscal_year', columns='company', values='revenue', aggfunc='first')
    
    # Convert to billions for plotting
    plot_df = pivot_df / 1e9
    
    # Plot each company
    for company in plot_df.columns:
        plt.plot(plot_df.index, plot_df[company], marker='o', label=company, linewidth=2)
    
    plt.title('Magnificent Seven - Revenue Trends (Billions USD)', fontsize=16, fontweight='bold')
    plt.xlabel('Fiscal Year', fontsize=12)
    plt.ylabel('Revenue (Billions USD)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    
    # Format y-axis
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:.0f}B'))
    
    plt.tight_layout()
    
    # Save plot
    plot_file = "revenue_trends.png"
    plt.savefig(plot_file, dpi=300, bbox_inches='tight')
    print(f"\nTrend visualization saved to: {plot_file}")
    
    # Save to CSV if requested
    if output_file:
        trend_df.to_csv(output_file)
        print(f"Trend data saved to: {output_file}")
    
    return trend_df

def main():
    """Main function."""
    db_path = "magnificent_seven_complete.db"
    
    if not os.path.exists(db_path):
        print(f"Database file {db_path} not found.")
        return
    
    print("Connecting to database...")
    conn = connect_db(db_path)
    
    if not conn:
        return
    
    try:
        print("Extracting revenue trends with context analysis...")
        revenue_data = extract_revenue_trends(conn)
        
        if not revenue_data:
            print("No revenue data found for trend analysis.")
            return
        
        print(f"Found {len(revenue_data)} revenue data points")
        
        # Generate comprehensive trend report
        output_file = "revenue_trend_analysis.csv"
        trend_df = generate_trend_report(revenue_data, output_file)
        
    finally:
        conn.close()

if __name__ == "__main__":
    main()