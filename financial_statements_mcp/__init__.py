"""
MCP Service for Financial Statements

This package provides MCP server functionality for accessing financial statements data.
"""

from .financial_statements_service import FinancialStatementsService, FinancialStatements

__version__ = "1.0.0"
__all__ = ["FinancialStatementsService", "FinancialStatements"]

# Optional: Import MCP server only if needed
def get_server():
    """Get the MCP server instance"""
    from .financial_statements_mcp import server
    return server