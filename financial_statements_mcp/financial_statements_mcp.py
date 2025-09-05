"""
MCP Server for Financial Statements

This MCP server provides tools to access financial statements data for major companies.
"""

import asyncio
from typing import Dict, List, Optional, Any
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import json
import sys
import os

# Add the parent directory to the path to import from the mcp package
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from financial_statements_mcp.financial_statements_service import FinancialStatementsService

# Create the MCP server
server = Server("financial-statements")

# Initialize our service
service = FinancialStatementsService()


@server.list_tools()
async def list_tools() -> List[Tool]:
    """List available tools"""
    return [
        Tool(
            name="get_financial_statements",
            description="Get complete financial statements (balance sheet, income statement, cash flow) for a company",
            inputSchema={
                "type": "object",
                "properties": {
                    "company_symbol": {
                        "type": "string",
                        "description": "Company stock symbol (e.g., AAPL, MSFT, GOOGL, AMZN, META, TSLA, NVDA)"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Fiscal year (e.g., 2024)"
                    }
                },
                "required": ["company_symbol", "year"]
            }
        ),
        Tool(
            name="get_balance_sheet",
            description="Get balance sheet data for a company",
            inputSchema={
                "type": "object",
                "properties": {
                    "company_symbol": {
                        "type": "string",
                        "description": "Company stock symbol (e.g., AAPL, MSFT, GOOGL, AMZN, META, TSLA, NVDA)"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Fiscal year (e.g., 2024)"
                    }
                },
                "required": ["company_symbol", "year"]
            }
        ),
        Tool(
            name="get_income_statement",
            description="Get income statement data for a company",
            inputSchema={
                "type": "object",
                "properties": {
                    "company_symbol": {
                        "type": "string",
                        "description": "Company stock symbol (e.g., AAPL, MSFT, GOOGL, AMZN, META, TSLA, NVDA)"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Fiscal year (e.g., 2024)"
                    }
                },
                "required": ["company_symbol", "year"]
            }
        ),
        Tool(
            name="get_cash_flow_statement",
            description="Get cash flow statement data for a company",
            inputSchema={
                "type": "object",
                "properties": {
                    "company_symbol": {
                        "type": "string",
                        "description": "Company stock symbol (e.g., AAPL, MSFT, GOOGL, AMZN, META, TSLA, NVDA)"
                    },
                    "year": {
                        "type": "integer",
                        "description": "Fiscal year (e.g., 2024)"
                    }
                },
                "required": ["company_symbol", "year"]
            }
        ),
        Tool(
            name="get_supported_companies",
            description="Get list of supported company symbols",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_company_info",
            description="Get company information (name, CIK) for a symbol",
            inputSchema={
                "type": "object",
                "properties": {
                    "company_symbol": {
                        "type": "string",
                        "description": "Company stock symbol (e.g., AAPL, MSFT, GOOGL, AMZN, META, TSLA, NVDA)"
                    }
                },
                "required": ["company_symbol"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle tool calls"""
    
    try:
        if name == "get_financial_statements":
            company_symbol = arguments.get("company_symbol")
            year = arguments.get("year")
            
            if not company_symbol or not year:
                return [TextContent(type="text", text="Error: company_symbol and year are required")]
            
            statements = service.get_financial_statements(company_symbol, year)
            
            if not statements:
                return [TextContent(type="text", text=f"No data found for {company_symbol} in {year}")]
            
            # Convert to JSON-serializable format
            result = {
                "company_name": statements.company_name,
                "cik": statements.cik,
                "fiscal_year": statements.fiscal_year,
                "filing_date": statements.filing_date,
                "balance_sheet": statements.balance_sheet,
                "income_statement": statements.income_statement,
                "cash_flow_statement": statements.cash_flow_statement,
                "data_quality_score": statements.data_quality_score,
                "validation_errors": statements.validation_errors
            }
            
            return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
        
        elif name == "get_balance_sheet":
            company_symbol = arguments.get("company_symbol")
            year = arguments.get("year")
            
            if not company_symbol or not year:
                return [TextContent(type="text", text="Error: company_symbol and year are required")]
            
            balance_sheet = service.get_balance_sheet(company_symbol, year)
            
            if not balance_sheet:
                return [TextContent(type="text", text=f"No balance sheet data found for {company_symbol} in {year}")]
            
            return [TextContent(type="text", text=json.dumps(balance_sheet, indent=2, default=str))]
        
        elif name == "get_income_statement":
            company_symbol = arguments.get("company_symbol")
            year = arguments.get("year")
            
            if not company_symbol or not year:
                return [TextContent(type="text", text="Error: company_symbol and year are required")]
            
            income_statement = service.get_income_statement(company_symbol, year)
            
            if not income_statement:
                return [TextContent(type="text", text=f"No income statement data found for {company_symbol} in {year}")]
            
            return [TextContent(type="text", text=json.dumps(income_statement, indent=2, default=str))]
        
        elif name == "get_cash_flow_statement":
            company_symbol = arguments.get("company_symbol")
            year = arguments.get("year")
            
            if not company_symbol or not year:
                return [TextContent(type="text", text="Error: company_symbol and year are required")]
            
            cash_flow = service.get_cash_flow_statement(company_symbol, year)
            
            if not cash_flow:
                return [TextContent(type="text", text=f"No cash flow statement data found for {company_symbol} in {year}")]
            
            return [TextContent(type="text", text=json.dumps(cash_flow, indent=2, default=str))]
        
        elif name == "get_supported_companies":
            companies = service.get_supported_companies()
            return [TextContent(type="text", text=json.dumps(companies, indent=2))]
        
        elif name == "get_company_info":
            company_symbol = arguments.get("company_symbol")
            
            if not company_symbol:
                return [TextContent(type="text", text="Error: company_symbol is required")]
            
            company_info = service.get_company_info(company_symbol)
            
            if not company_info:
                return [TextContent(type="text", text=f"No information found for {company_symbol}")]
            
            return [TextContent(type="text", text=json.dumps(company_info, indent=2))]
        
        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]
    
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]


async def main():
    """Run the MCP server"""
    # Run the server using stdio
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())