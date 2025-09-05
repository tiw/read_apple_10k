#!/usr/bin/env python3
"""
Startup script for Financial Statements MCP Service

This script makes it easy to run the MCP service from any directory.
"""

import sys
import os
import asyncio

# Add the project root to the path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Import and run the MCP service
from financial_statements_mcp.financial_statements_mcp import main

if __name__ == "__main__":
    asyncio.run(main())