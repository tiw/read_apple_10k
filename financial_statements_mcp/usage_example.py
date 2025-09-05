#!/usr/bin/env python3
"""
Usage example for Financial Statements MCP Service

This script demonstrates how to use the financial statements service
to retrieve financial data for major companies.
"""

import sys
import os

# Add the parent directory to the path to import from the mcp package
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from financial_statements_mcp.financial_statements_service import FinancialStatementsService
import json


def main():
    """Main function to demonstrate service usage"""
    print("💰 Financial Statements MCP Service - Usage Example")
    print("=" * 60)
    
    # Initialize the service
    service = FinancialStatementsService()
    
    # Example 1: Get supported companies
    print("\n📋 Supported Companies:")
    companies = service.get_supported_companies()
    for company in companies:
        info = service.get_company_info(company)
        print(f"   {company}: {info['name']} (CIK: {info['cik']})")
    
    # Example 2: Get complete financial statements
    print(f"\n📊 Complete Financial Statements for Apple Inc. (2024):")
    print("-" * 50)
    
    statements = service.get_financial_statements("AAPL", 2024)
    if statements:
        print(f"Company: {statements.company_name}")
        print(f"CIK: {statements.cik}")
        print(f"Fiscal Year: {statements.fiscal_year}")
        print(f"Data Quality Score: {statements.data_quality_score:.1%}")
        print(f"Validation Errors: {len(statements.validation_errors)}")
        
        # Display balance sheet summary
        bs = statements.balance_sheet
        print(f"\n💼 Balance Sheet Summary:")
        print(f"   Total Assets: ${bs['total_assets']:,.0f}")
        print(f"   Total Liabilities: ${bs['total_liabilities']:,.0f}")
        print(f"   Total Equity: ${bs['total_equity']:,.0f}")
        
        # Display income statement summary
        inc = statements.income_statement
        print(f"\n📈 Income Statement Summary:")
        print(f"   Revenue: ${inc['revenue']:,.0f}")
        print(f"   Cost of Goods Sold: ${inc['cost_of_goods_sold']:,.0f}")
        print(f"   Gross Profit: ${inc['gross_profit']:,.0f}")
        print(f"   Operating Income: ${inc['operating_income']:,.0f}")
        print(f"   Net Income: ${inc['net_income']:,.0f}")
        print(f"   EPS Basic: ${inc['eps_basic']:.2f}")
        print(f"   EPS Diluted: ${inc['eps_diluted']:.2f}")
        
        # Display detailed balance sheet
        print(f"\n🏦 Detailed Balance Sheet:")
        print("   Assets:")
        print(f"     Current Assets: ${bs['assets']['current_assets']:,.0f}")
        print(f"     Cash & Equivalents: ${bs['assets']['cash_and_equivalents']:,.0f}")
        print(f"     Non-current Assets: ${bs['assets']['noncurrent_assets']:,.0f}")
        print(f"     PPE: ${bs['assets']['property_plant_equipment']:,.0f}")
        
        print("   Liabilities:")
        print(f"     Current Liabilities: ${bs['liabilities']['current_liabilities']:,.0f}")
        print(f"     Non-current Liabilities: ${bs['liabilities']['noncurrent_liabilities']:,.0f}")
        
        print("   Equity:")
        print(f"     Common Stock: ${bs['equity']['common_stock']:,.0f}")
        print(f"     Retained Earnings: ${bs['equity']['retained_earnings']:,.0f}")
        
        # Display detailed income statement
        print(f"\n📊 Detailed Income Statement:")
        print("   Operating Expenses:")
        print(f"     R&D: ${inc['operating_expenses']['research_development']:,.0f}")
        print(f"     SG&A: ${inc['operating_expenses']['selling_general_administrative']:,.0f}")
        print(f"     Total Operating Expenses: ${inc['operating_expenses']['total_operating_expenses']:,.0f}")
    
    # Example 3: Get individual statements
    print(f"\n🔍 Individual Statement Retrieval:")
    print("-" * 40)
    
    # Balance sheet
    balance_sheet = service.get_balance_sheet("AAPL", 2024)
    if balance_sheet:
        print("✅ Balance sheet retrieved successfully")
    
    # Income statement
    income_statement = service.get_income_statement("AAPL", 2024)
    if income_statement:
        print("✅ Income statement retrieved successfully")
    
    # Cash flow statement
    cash_flow = service.get_cash_flow_statement("AAPL", 2024)
    if cash_flow:
        print("✅ Cash flow statement retrieved successfully")
    
    # Example 4: Compare multiple companies
    print(f"\n🔄 Company Comparison (2024):")
    print("-" * 40)
    
    comparison_companies = ["AAPL", "MSFT", "GOOGL"]
    
    for company in comparison_companies:
        statements = service.get_financial_statements(company, 2024)
        if statements:
            bs = statements.balance_sheet
            inc = statements.income_statement
            print(f"{company}:")
            print(f"   Revenue: ${inc['revenue']:,.0f}")
            print(f"   Net Income: ${inc['net_income']:,.0f}")
            print(f"   Total Assets: ${bs['total_assets']:,.0f}")
            print(f"   Data Quality: {statements.data_quality_score:.1%}")
            print()
    
    # Example 5: Error handling
    print("❌ Error Handling:")
    print("-" * 20)
    
    invalid_result = service.get_financial_statements("INVALID", 2024)
    if invalid_result is None:
        print("✅ Invalid company handled correctly")
    
    invalid_year = service.get_financial_statements("AAPL", 1900)
    if invalid_year is None:
        print("✅ Invalid year handled correctly")
    
    print("\n🎉 Usage example completed!")


if __name__ == "__main__":
    main()