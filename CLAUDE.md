# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an XBRL analysis tool for parsing and analyzing SEC 10-K filings, specifically focused on Apple and other major tech companies ("Magnificent Seven"). The tool can download, parse, and analyze XBRL financial data from SEC filings.

## Key Components

- **XBRL Parser**: Core parsing functionality in `tools/context_analyzer.py` and `tools/financial_statements.py`
- **SEC Downloaders**: Multiple downloader implementations for fetching 10-K filings
- **Database Integration**: SQLite database for storing and querying financial data
- **CLI Interface**: Command-line tools in `xbrl_analyzer/cli/`

## Development Commands

### Setup and Installation
```bash
# Create virtual environment
python venv_setup.py

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .
```

### Running the Main CLI Tool
```bash
# List all contexts in an XBRL file
xbrl-analyzer --file path/to/file.xml --list-contexts

# Show facts for specific context
xbrl-analyzer --file path/to/file.xml --context-id c-1

# Generate financial statements
xbrl-analyzer --file path/to/file.xml --generate-statements --xsd path/to/schema.xsd --definition path/to/def.xml
```

### Database Operations
```bash
# Import XBRL data into database
xbrl-db-import --file path/to/file.xml --company AAPL --year 2024

# Query database
xbrl-db-query --company AAPL --year 2024
```

### SEC Downloaders
```bash
# Download single company data
python xbrl_analyzer/tools/sec_index_downloader_tool.py --ticker AAPL

# Download Magnificent Seven data (optimized)
python download_magnificent_seven_optimized.py
```

## Architecture

### File Types
- `.xsd`: XBRL schema files
- `*_htm.xml`: Instance documents with financial data
- `*_cal.xml`: Calculation linkbase files
- `*_def.xml`: Definition linkbase files
- `*_pre.xml`: Presentation linkbase files

### Data Flow
1. **Download**: SEC filings via index-based or API-based downloaders
2. **Parse**: XBRL files using lxml and custom parsers
3. **Store**: Financial facts in SQLite database
4. **Analyze**: Generate reports and financial statements

### Database Schema
Financial data is stored in SQLite with tables for:
- Companies (ticker, CIK, name)
- Filings (company, filing_date, period)
- Facts (filing_id, concept, value, context, decimals)
- Contexts (context_id, period_type, dimensions)

## Key Files and Directories

- `xbrl_analyzer/`: Main package with CLI tools
- `tools/`: Core parsing and analysis utilities
- `db/`: SQLite database files
- `magnificent_seven_10k_optimized/`: Downloaded 10-K data
- `company_tickers.json`: SEC company ticker to CIK mapping

## Performance Considerations

- Use optimized downloader (`download_magnificent_seven_optimized.py`) for bulk downloads
- Index-based downloaders are more efficient than API-based for historical data
- Database queries should use appropriate indexes for large datasets

## Testing

Run individual test scripts:
```bash
python test_xbrl_parsing.py
python check_msft.py
python check_schema.py
```

## Common Development Tasks

- Adding new financial statement templates
- Enhancing XBRL parsing for specific elements
- Optimizing database queries for large datasets
- Adding support for additional SEC filing types
- Improving error handling in downloaders