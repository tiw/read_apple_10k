# XBRL Analysis Tool

This tool analyzes XBRL files to count GAAP facts per context.

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

- `main.py`: Main entry point
- `tools/`: Directory containing analysis tools
  - `context_analyzer.py`: Module for analyzing contexts and facts
- `venv/`: Virtual environment (created during setup)
- `requirements.txt`: Python package dependencies

## Analysis Results

The tool will display a table showing:
- Context ID: The identifier for each context in the XBRL file
- Fact Count: Number of GAAP facts associated with that context
- Period: Time period the context covers (instant for point-in-time or period for durations)
- Entity: The entity the context refers to (usually the company's CIK)

## Detailed Context Analysis

When using the `--context-id` option, the tool will list all facts associated with that specific context, including:
- Tag Name: The name of the XBRL tag
- Value: The value of the fact
- Period information for the context

## Implementation Details

The tool parses XBRL files and counts how many GAAP facts are associated with each context. This helps understand the data distribution in the financial filing. 

For example, you can see which contexts (time periods) have the most financial facts reported, and what time periods and entities they refer to.