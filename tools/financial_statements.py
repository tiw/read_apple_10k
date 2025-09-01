import xml.etree.ElementTree as ET
from collections import defaultdict
import translation

FINANCIAL_TERMS = translation.FINANCIAL_TERMS

def parse_xsd(xsd_file_path):
    """
    Parse XSD file to extract element definitions
    
    Args:
        xsd_file_path (str): Path to XSD file
        
    Returns:
        dict: Dictionary of element definitions
    """
    tree = ET.parse(xsd_file_path)
    root = tree.getroot()
    
    # Define namespaces
    namespaces = {
        'xs': 'http://www.w3.org/2001/XMLSchema',
        'xbrli': 'http://www.xbrl.org/2003/instance',
        'link': 'http://www.xbrl.org/2003/linkbase',
        'xbrldt': 'http://xbrl.org/2005/xbrldt',
        'dtr-types': 'http://www.xbrl.org/dtr/type/2020-01-21',
        'dtr-types1': 'http://www.xbrl.org/dtr/type/2020-01-21'
    }
    
    elements = {}
    
    # Extract element definitions
    for elem in root.findall('.//xs:element', namespaces):
        element_id = elem.get('id')
        element_name = elem.get('name')
        element_type = elem.get('type')
        period_type = elem.get('{http://www.xbrl.org/2003/instance}periodType')
        balance = elem.get('{http://www.xbrl.org/2003/instance}balance')
        abstract = elem.get('abstract')
        
        if element_id and element_name:
            elements[element_name] = {
                'id': element_id,
                'type': element_type,
                'periodType': period_type,
                'balance': balance,
                'abstract': abstract
            }
    
    # Extract role types
    roles = {}
    for role_type in root.findall('.//link:roleType', namespaces):
        role_uri = role_type.get('roleURI')
        role_id = role_type.get('id')
        
        definition_elem = role_type.find('.//link:definition', namespaces)
        definition = definition_elem.text if definition_elem is not None else ""
        
        if role_uri and role_id:
            roles[role_id] = {
                'uri': role_uri,
                'definition': definition
            }
    
    return elements, roles

def parse_definition_linkbase(def_file_path):
    """
    Parse definition linkbase to extract dimensional structure
    
    Args:
        def_file_path (str): Path to definition linkbase file
        
    Returns:
        dict: Dimensional structure information
    """
    tree = ET.parse(def_file_path)
    root = tree.getroot()
    
    # Define namespaces
    namespaces = {
        'link': 'http://www.xbrl.org/2003/linkbase',
        'xlink': 'http://www.w3.org/1999/xlink',
        'xbrldt': 'http://xbrl.org/2005/xbrldt'
    }
    
    # Extract dimensional relationships
    dimensions = defaultdict(list)
    hypercubes = defaultdict(list)
    domain_members = defaultdict(list)
    
    # Extract locators first
    locators = {}
    for loc in root.findall('.//link:loc', namespaces):
        label = loc.get('{http://www.w3.org/1999/xlink}label')
        href = loc.get('{http://www.w3.org/1999/xlink}href')
        if href and '#' in href:
            element_name = href.split('#')[-1]
            # Remove namespace prefix if present
            if '_' in element_name and not element_name.startswith('_'):
                element_name = '_'.join(element_name.split('_')[1:])
            locators[label] = element_name
    
    # Process definitionArc elements
    for arc in root.findall('.//link:definitionArc', namespaces):
        arcrole = arc.get('{http://www.w3.org/1999/xlink}arcrole')
        from_label = arc.get('{http://www.w3.org/1999/xlink}from')
        to_label = arc.get('{http://www.w3.org/1999/xlink}to')
        
        from_element = locators.get(from_label)
        to_element = locators.get(to_label)
        
        if from_element and to_element:
            if 'hypercube-dimension' in arcrole:
                dimensions[from_element].append(to_element)
            elif 'domain-member' in arcrole:
                domain_members[from_element].append(to_element)
            elif 'dimension-domain' in arcrole:
                if from_element not in dimensions:
                    dimensions[from_element] = []
                dimensions[from_element].append(to_element)
            elif 'all' in arcrole:
                # This is a hypercube relationship
                hypercubes[from_element] = hypercubes.get(from_element, []) + [to_element]
    
    return {
        'dimensions': dict(dimensions),
        'hypercubes': dict(hypercubes),
        'domain_members': dict(domain_members)
    }

def extract_facts_from_instance(instance_file_path, context_id=None):
    """
    Extract facts from XBRL instance document
    
    Args:
        instance_file_path (str): Path to XBRL instance file
        context_id (str): Optional context ID to filter facts
        
    Returns:
        dict: Dictionary of facts
    """
    tree = ET.parse(instance_file_path)
    root = tree.getroot()
    
    # Define namespaces
    namespaces = {
        'xbrli': 'http://www.xbrl.org/2003/instance',
        'us-gaap': 'http://fasb.org/us-gaap/2024',
        'aapl': 'http://www.apple.com/20240928',
        'dei': 'http://xbrl.sec.gov/dei/2024'
    }
    
    facts = {}
    
    # Extract all facts
    for elem in root.iter():
        # Skip non-fact elements
        if elem.tag in ['{http://www.xbrl.org/2003/instance}context', 
                        '{http://www.xbrl.org/2003/instance}unit']:
            continue
            
        # Check if it's a fact element (has text content and possibly contextRef)
        if elem.text and elem.text.strip():
            # Get the tag name
            tag_name = elem.tag
            if tag_name.startswith('{'):
                # Handle namespaced elements
                ns_uri, local_name = tag_name[1:].split('}', 1)
                tag_name = local_name
            
            context_ref = elem.get('contextRef')
            
            # If context_id is specified, only include facts with that context
            if context_id and context_ref != context_id:
                continue
                
            unit_ref = elem.get('unitRef')
            decimals = elem.get('decimals')
            
            # Create a unique key for the fact
            fact_key = tag_name
            if context_ref:
                fact_key = f"{tag_name}[context={context_ref}]"
                
            facts[fact_key] = {
                'name': tag_name,
                'value': elem.text.strip(),
                'contextRef': context_ref,
                'unitRef': unit_ref,
                'decimals': decimals
            }
    
    return facts

def format_value(value):
    """
    Format numeric values for better readability
    
    Args:
        value (str): Value to format
        
    Returns:
        str: Formatted value
    """
    try:
        # Try to convert to float
        num_value = float(value)
        # Format large numbers with commas
        if abs(num_value) >= 1000:
            return f"{num_value:,.2f}"
        else:
            return str(num_value)
    except ValueError:
        # If it's not a number, return as is
        return value

def organize_facts_by_statement_type(facts, structure, roles):
    """
    Organize facts by statement type based on structure and roles
    
    Args:
        facts (dict): Dictionary of facts
        structure (dict): Structure information from definition linkbase
        roles (dict): Role information from XSD
        
    Returns:
        dict: Facts organized by statement type
    """
    organized_facts = defaultdict(list)
    
    # Try to identify key financial statements from roles
    balance_sheet_roles = [role_id for role_id in roles if 'BALANCE SHEET' in roles[role_id]['definition'].upper()]
    income_statement_roles = [role_id for role_id in roles if 'OPERATIONS' in roles[role_id]['definition'].upper() or 'INCOME' in roles[role_id]['definition'].upper()]
    cash_flow_roles = [role_id for role_id in roles if 'CASH FLOW' in roles[role_id]['definition'].upper()]
    
    # Categorize facts based on their names
    for fact_key, fact_info in facts.items():
        fact_name = fact_info['name']
        
        # Skip text blocks
        if 'textblock' in fact_name.lower() or 'disclosure' in fact_name.lower():
            continue
            
        # Balance sheet items (assets, liabilities, equity)
        if any(asset_term in fact_name.lower() for asset_term in 
               ['asset', 'cash', 'receivable', 'inventory', 'securities', 'property', 'plant', 'equipment']):
            organized_facts['Assets'].append(fact_info)
        elif any(liab_term in fact_name.lower() for liab_term in 
                 ['liability', 'payable', 'debt', 'loan', 'borrowing', 'longtermdebt', 'shorttermdebt']):
            organized_facts['Liabilities'].append(fact_info)
        elif any(equity_term in fact_name.lower() for equity_term in 
                 ['equity', 'capital', 'retained', 'stock', 'shareholder']):
            organized_facts['Equity'].append(fact_info)
        # Income statement items (revenue, expenses)
        elif any(income_term in fact_name.lower() for income_term in 
                 ['revenue', 'income', 'expense', 'cost', 'profit', 'earnings']):
            organized_facts['Income_Statement'].append(fact_info)
        # Cash flow items
        elif any(cash_term in fact_name.lower() for cash_term in 
                 ['cash', 'flow']):
            organized_facts['Cash_Flow'].append(fact_info)
        else:
            organized_facts['Other'].append(fact_info)
    
    return organized_facts

def generate_financial_statements(instance_file_path, xsd_file_path, def_file_path, context_id=None):
    """
    Generate financial statements by combining XSD definitions, definition linkbase structure, and instance facts
    
    Args:
        instance_file_path (str): Path to XBRL instance file
        xsd_file_path (str): Path to XSD schema file
        def_file_path (str): Path to definition linkbase file
        context_id (str): Optional context ID to filter facts
        
    Returns:
        str: Formatted financial statements
    """
    # Parse XSD for element definitions
    elements, roles = parse_xsd(xsd_file_path)
    
    # Parse definition linkbase for structure
    structure = parse_definition_linkbase(def_file_path)
    
    # Extract facts from instance document
    facts = extract_facts_from_instance(instance_file_path, context_id)
    
    # Organize facts by statement type
    organized_facts = organize_facts_by_statement_type(facts, structure, roles)
    
    # Generate output
    result_lines = []
    result_lines.append("Financial Statements Generated from XBRL Data")
    result_lines.append("=" * 80)
    
    # Add information about the context if specified
    if context_id:
        result_lines.append(f"Context: {context_id}")
    
    # Try to get context information
    context_info = "No specific context"
    for fact_key, fact_info in facts.items():
        if fact_info.get('contextRef') == context_id:
            context_info = f"Context {context_id}"
            break
    
    result_lines.append(f"Context Information: {context_info}")
    result_lines.append("")
    
    # Display dimensional structure information
    result_lines.append("Dimensional Structure:")
    result_lines.append("-" * 40)
    if structure['dimensions']:
        result_lines.append("Dimensions (Hypercube -> Dimensions):")
        for hypercube, dimensions in list(structure['dimensions'].items())[:5]:
            result_lines.append(f"  {hypercube}:")
            for dim in dimensions[:3]:  # Limit to first 3 for brevity
                result_lines.append(f"    - {dim}")
    
    if structure['domain_members']:
        result_lines.append("")
        result_lines.append("Domain Members (Domain -> Members):")
        count = 0
        for domain, members in structure['domain_members'].items():
            if count >= 5:  # Limit to first 5 domains
                break
            result_lines.append(f"  {domain}:")
            for member in members[:3]:  # Limit to first 3 members
                result_lines.append(f"    - {member}")
            count += 1
    
    result_lines.append("")
    
    # Display organized financial statements
    result_lines.append("Organized Financial Statements:")
    result_lines.append("=" * 80)
    
    # Display Balance Sheet items
    if organized_facts['Assets'] or organized_facts['Liabilities'] or organized_facts['Equity']:
        result_lines.append("\nBALANCE SHEET")
        result_lines.append("-" * 50)
        
        # Assets
        if organized_facts['Assets']:
            result_lines.append("ASSETS:")
            for fact in organized_facts['Assets'][:10]:  # Limit to first 10
                fact_name = fact['name']
                chinese_name = FINANCIAL_TERMS.get(fact_name, "")
                value = format_value(fact.get('value', 'N/A'))
                context = fact.get('contextRef', 'N/A')
                result_lines.append(f"  {fact_name} ({chinese_name}): {value}")
        
        # Liabilities
        if organized_facts['Liabilities']:
            result_lines.append("\nLIABILITIES:")
            for fact in organized_facts['Liabilities'][:10]:  # Limit to first 10
                fact_name = fact['name']
                chinese_name = FINANCIAL_TERMS.get(fact_name, "")
                value = format_value(fact.get('value', 'N/A'))
                result_lines.append(f"  {fact_name} ({chinese_name}): {value}")
        
        # Equity
        if organized_facts['Equity']:
            result_lines.append("\nEQUITY:")
            for fact in organized_facts['Equity'][:10]:  # Limit to first 10
                fact_name = fact['name']
                chinese_name = FINANCIAL_TERMS.get(fact_name, "")
                value = format_value(fact.get('value', 'N/A'))
                result_lines.append(f"  {fact_name} ({chinese_name}): {value}")
    
    # Display Income Statement items
    if organized_facts['Income_Statement']:
        result_lines.append("\n\nINCOME STATEMENT")
        result_lines.append("-" * 50)
        for fact in organized_facts['Income_Statement'][:15]:  # Limit to first 15
            fact_name = fact['name']
            chinese_name = FINANCIAL_TERMS.get(fact_name, "")
            value = format_value(fact.get('value', 'N/A'))
            result_lines.append(f"  {fact_name} ({chinese_name}): {value}")
    
    # Display Cash Flow items
    if organized_facts['Cash_Flow']:
        result_lines.append("\n\nCASH FLOW STATEMENT")
        result_lines.append("-" * 50)
        for fact in organized_facts['Cash_Flow'][:10]:  # Limit to first 10
            fact_name = fact['name']
            chinese_name = FINANCIAL_TERMS.get(fact_name, "")
            value = format_value(fact.get('value', 'N/A'))
            result_lines.append(f"  {fact_name} ({chinese_name}): {value}")
    
    # Display other items
    if organized_facts['Other']:
        result_lines.append("\n\nOTHER FINANCIAL FACTS")
        result_lines.append("-" * 50)
        for fact in organized_facts['Other'][:10]:  # Limit to first 10
            fact_name = fact['name']
            chinese_name = FINANCIAL_TERMS.get(fact_name, "")
            value = format_value(fact.get('value', 'N/A'))
            context = fact.get('contextRef', 'N/A')
            result_lines.append(f"  {fact_name} ({chinese_name}): {value} (Context: {context})")
    
    result_lines.append("")
    result_lines.append(f"Total facts extracted: {len(facts)}")
    result_lines.append("=" * 80)
    
    return "\n".join(result_lines)