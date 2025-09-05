#!/usr/bin/env python3
"""
Test script for Financial Statements MCP Service
"""

import sys
import os

# Add the parent directory to the path to import from the mcp package
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from financial_statements_mcp.financial_statements_service import FinancialStatementsService


def test_service():
    """Test the financial statements service"""
    print("🧪 Testing Financial Statements Service")
    print("=" * 50)
    
    service = FinancialStatementsService()
    
    # Test 1: Get supported companies
    print("\n📋 1. Testing get_supported_companies()")
    companies = service.get_supported_companies()
    print(f"   Supported companies: {companies}")
    
    # Test 2: Get company info
    print("\n📋 2. Testing get_company_info()")
    company_info = service.get_company_info("AAPL")
    print(f"   AAPL info: {company_info}")
    
    # Test 3: Get complete financial statements
    print("\n📋 3. Testing get_financial_statements() for AAPL 2024")
    statements = service.get_financial_statements("AAPL", 2024)
    
    if statements:
        print(f"   ✅ Found data for {statements.company_name}")
        print(f"   📅 Fiscal Year: {statements.fiscal_year}")
        print(f"   📊 Data Quality Score: {statements.data_quality_score:.1%}")
        print(f"   ❓ Validation Errors: {len(statements.validation_errors)}")
        
        if statements.validation_errors:
            print("   Validation Errors:")
            for error in statements.validation_errors:
                print(f"     - {error}")
        
        # Display key financial metrics
        bs = statements.balance_sheet
        inc = statements.income_statement
        
        print(f"\n   💰 Key Financial Metrics:")
        print(f"     Total Assets: ${bs.get('total_assets', 0):,.0f}")
        print(f"     Total Liabilities: ${bs.get('total_liabilities', 0):,.0f}")
        print(f"     Total Equity: ${bs.get('total_equity', 0):,.0f}")
        print(f"     Revenue: ${inc.get('revenue', 0):,.0f}")
        print(f"     Net Income: ${inc.get('net_income', 0):,.0f}")
        print(f"     EPS Basic: ${inc.get('eps_basic', 0):.2f}")
        
    else:
        print("   ❌ No data found for AAPL 2024")
    
    # Test 4: Get individual statements
    print("\n📋 4. Testing individual statement retrieval")
    
    balance_sheet = service.get_balance_sheet("AAPL", 2024)
    if balance_sheet:
        print("   ✅ Balance sheet retrieved successfully")
    else:
        print("   ❌ Failed to retrieve balance sheet")
    
    income_statement = service.get_income_statement("AAPL", 2024)
    if income_statement:
        print("   ✅ Income statement retrieved successfully")
    else:
        print("   ❌ Failed to retrieve income statement")
    
    cash_flow = service.get_cash_flow_statement("AAPL", 2024)
    if cash_flow:
        print("   ✅ Cash flow statement retrieved successfully")
    else:
        print("   ❌ Failed to retrieve cash flow statement")
    
    # Test 5: Test error handling
    print("\n📋 5. Testing error handling")
    
    invalid_company = service.get_financial_statements("INVALID", 2024)
    if invalid_company is None:
        print("   ✅ Invalid company handled correctly")
    else:
        print("   ❌ Invalid company not handled correctly")
    
    print("\n🎉 Service testing completed!")


def test_database_connection():
    """Test database connection"""
    print("\n🔌 Testing Database Connection")
    print("=" * 40)
    
    try:
        from financial_statements_service import DataExtractor
        extractor = DataExtractor()
        
        # Test connection
        extractor.connect()
        
        # Simple query
        result = extractor.conn.execute("SELECT COUNT(*) FROM companies").fetchone()
        print(f"   ✅ Database connected successfully")
        print(f"   📊 Companies in database: {result[0]}")
        
        # Test sample data
        sample_query = """
        SELECT comp.name, comp.cik, xf.fiscal_year, COUNT(ft.tag_name) as metrics_count
        FROM companies comp
        JOIN xbrl_files xf ON comp.id = xf.company_id
        JOIN financial_facts ff ON xf.id = ff.xbrl_file_id
        JOIN financial_tags ft ON ff.tag_id = ft.id
        WHERE comp.cik = '0000320193' AND xf.fiscal_year = 2024
        GROUP BY comp.name, comp.cik, xf.fiscal_year
        """
        
        sample_result = extractor.conn.execute(sample_query).fetchone()
        if sample_result:
            print(f"   📈 Sample data (AAPL 2024): {sample_result[0]} - {sample_result[1]} - Year {sample_result[2]} - {sample_result[3]} metrics")
        
        extractor.disconnect()
        
    except Exception as e:
        print(f"   ❌ Database connection failed: {e}")


if __name__ == "__main__":
    test_database_connection()
    test_service()