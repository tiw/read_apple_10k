#!/usr/bin/env python3
"""
Utility functions for working with stock tickers and CIK numbers.
"""

import os
import json
from typing import Optional


def get_cik_by_ticker(ticker: str) -> Optional[str]:
    """
    Get CIK by ticker symbol from company_tickers.json
    
    Args:
        ticker: Company ticker symbol (e.g., AAPL)
        
    Returns:
        CIK number as string or None if not found
    """
    # Load company tickers data
    tickers_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 
                               'company_tickers.json')
    
    if not os.path.exists(tickers_file):
        print(f"Error: company_tickers.json not found at {tickers_file}")
        return None
    
    with open(tickers_file, 'r') as f:
        tickers_data = json.load(f)
    
    # Search for ticker
    for entry in tickers_data.values():
        if entry['ticker'] == ticker:
            return str(entry['cik_str'])
    
    return None