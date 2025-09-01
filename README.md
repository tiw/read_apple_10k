# Apple 10-K XBRL Parser

This tool helps parse and analyze XBRL files from Apple's 10-K filings, extracting financial data and presenting it in a more readable format.

## Features

1. Context Analysis
   - List all available contexts in an XBRL instance document
   - View facts associated with a specific context
   - View facts organized by presentation structure

2. Financial Statement Generation
   - Generate financial statements by combining XSD schema, definition linkbase, and instance document
   - Organize facts by statement type (Balance Sheet, Income Statement, Cash Flow Statement)
   - Filter facts by context ID

3. Calculation Validation
   - Validate calculations defined in calculation linkbases
   - Filter out zero-value calculations for cleaner output

4. HTML Table Parsing
   - Parse HTML tables from SEC filings
   - Extract structured data from complex HTML tables
   - Format data for better readability

5. Revenue Analysis by Product
   - Analyze revenue breakdown by product lines
   - Extract revenue data for iPhone, Mac, iPad, Wearables, and Services
   - Show revenue structure from definition linkbase

## Installation

1. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Context Analysis

List all contexts in an XBRL instance document:
```
python main.py --file 10k/aapl-20240928_htm.xml --list-contexts
```

List all facts for a specific context:
```
python main.py --file 10k/aapl-20240928_htm.xml --context-id c-1
```

List facts organized by presentation structure:
```
python main.py --file 10k/aapl-20240928_htm.xml --context-id c-1 --presentation 10k/aapl-20240928_pre.xml
```

### Financial Statement Generation

Generate financial statements from XBRL files:
```
python main.py --file 10k/aapl-20240928_htm.xml --generate-statements --xsd 10k/aapl-20240928.xsd --definition 10k/aapl-20240928_def.xml
```

Generate financial statements for a specific context:
```
python main.py --file 10k/aapl-20240928_htm.xml --generate-statements --xsd 10k/aapl-20240928.xsd --definition 10k/aapl-20240928_def.xml --context-id c-1
```

### Calculation Validation

Validate calculations in XBRL files:
```
python main.py --file 10k/aapl-20240928_htm.xml --context-id c-1 --calculation 10k/aapl-20240928_cal.xml
```

Validate calculations and filter out zero-value results:
```
python main.py --file 10k/aapl-20240928_htm.xml --context-id c-1 --calculation 10k/aapl-20240928_cal.xml --calculation-filter-zero
```

### HTML Table Parsing

Parse HTML tables from files:
```
python main.py --parse-html-table tools/test.html
```

### Revenue Analysis by Product

Analyze revenue breakdown by product lines:
```
python main.py --file 10k/aapl-20240928_htm.xml --analyze-revenue --xsd 10k/aapl-20240928.xsd --definition 10k/aapl-20240928_def.xml
```
## XBRL File Types

- `.xsd`: Schema files that define the structure and elements
- `.xml`: Instance documents that contain the actual financial data
- `_pre.xml`: Presentation linkbase files that define the display structure
- `_cal.xml`: Calculation linkbase files that define calculation relationships
- `_def.xml`: Definition linkbase files that define dimensional relationships

## Examples

### Viewing Financial Statements

To view financial statements for Apple's 2024 fiscal year:
```
python main.py --file 10k/aapl-20240928_htm.xml --generate-statements --xsd 10k/aapl-20240928.xsd --definition 10k/aapl-20240928_def.xml --context-id c-1
```

This will generate a formatted output showing:
- Dimensional structure information
- Assets, liabilities, and equity items
- Income statement items
- Cash flow items
- Other financial facts

### Validating Calculations

To validate calculations in the financial statements:
```
python main.py --file 10k/aapl-20240928_htm.xml --context-id c-1 --calculation 10k/aapl-20240928_cal.xml --calculation-filter-zero
```

This will show calculations where the actual result differs from the expected result, helping to identify potential data inconsistencies.

### Parsing HTML Tables

To extract data from HTML tables in SEC filings:
```
python main.py --parse-html-table tools/test.html
```

This will parse the HTML content and extract tabular data in a structured, readable format.

### Analyzing Revenue by Product

To analyze Apple's revenue by product lines:
```
python main.py --file 10k/aapl-20240928_htm.xml --analyze-revenue --xsd 10k/aapl-20240928.xsd --definition 10k/aapl-20240928_def.xml
```

This will show:
- Product members defined in the XSD schema
- Revenue structure from the definition linkbase
- Revenue breakdown by product (iPhone, Mac, iPad, Wearables, Services)
- Total revenue across all products