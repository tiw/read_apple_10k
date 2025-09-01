# Apple 10-K XBRL Parser

This tool helps parse and analyze XBRL files from Apple's 10-K filings, extracting financial data and presenting it in a more readable format.

## Setup

1. Run the virtual environment setup script:
   ```bash
   python venv_setup.py
   ```

2. Activate the virtual environment:
   ```bash
   # On Unix/Linux/macOS:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

## Usage

```bash
python main.py --file <path_to_xbrl_file> [--output <output_file>] [--context-id <context_id>]
```

Examples:
```bash
# Analyze all contexts and show fact counts
python main.py --file 10k/aapl-20240928_htm.xml

# List all facts for a specific context
python main.py --file 10k/aapl-20240928_htm.xml --context-id c-1

# Save output to a file
python main.py --file 10k/aapl-20240928_htm.xml --output results.txt
```

## Project Structure

- `main.py`: Entry point for the application
- `tools/`: Contains various parsing and analysis tools
  - `context_analyzer.py`: Context and fact analysis tools
  - `financial_statements.py`: Financial statement generation tools
  - `html_table_parser.py`: HTML table parsing tools
  - `translation.py`: Financial term translation dictionary
- `10k/`: Contains Apple's 10-K XBRL files
- `tools/test.html`: Sample HTML file for testing table parsing

## Analysis Results

The tool will display a table showing:
- Context ID: The identifier for each context in the XBRL file
- Fact Count: Number of GAAP facts associated with that context
- Period: Time period the context covers (instant for point-in-time or period for durations)
- Entity: The entity the context refers to (usually the company's CIK)
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