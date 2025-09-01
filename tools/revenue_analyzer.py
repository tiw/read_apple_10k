import xml.etree.ElementTree as ET
from collections import defaultdict, OrderedDict
from datetime import datetime

def parse_xsd_for_products(xsd_file_path):
    """
    Parse XSD file to extract product members
    
    Args:
        xsd_file_path (str): Path to XSD file
        
    Returns:
        list: List of product member names
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
    
    product_members = []
    
    # Extract product member elements
    for elem in root.findall('.//xs:element', namespaces):
        element_name = elem.get('name')
        if element_name and 'Member' in element_name and (
                'IPhone' in element_name or 
                'IPad' in element_name or 
                'Mac' in element_name or 
                'Wearables' in element_name):
            product_members.append(element_name)
    
    return product_members

def parse_definition_linkbase_for_revenue_structure(def_file_path):
    """
    Parse definition linkbase to extract revenue structure for significant products and services
    
    Args:
        def_file_path (str): Path to definition linkbase file
        
    Returns:
        dict: Revenue structure information
    """
    tree = ET.parse(def_file_path)
    root = tree.getroot()
    
    # Define namespaces
    namespaces = {
        'link': 'http://www.xbrl.org/2003/linkbase',
        'xlink': 'http://www.w3.org/1999/xlink',
        'xbrldt': 'http://xbrl.org/2005/xbrldt'
    }
    
    # Find all definitionLink elements
    definition_links = root.findall('.//link:definitionLink', namespaces)
    
    # Look for the specific role we're interested in
    target_role_link = None
    for definition_link in definition_links:
        role = definition_link.get('{http://www.w3.org/1999/xlink}role')
        if role and 'RevenueNetSalesDisaggregatedbySignificantProductsandServicesDetails' in role:
            target_role_link = definition_link
            break
    
    if not target_role_link:
        return {}
    
    # Extract locators first
    locators = {}
    for loc in target_role_link.findall('.//link:loc', namespaces):
        label = loc.get('{http://www.w3.org/1999/xlink}label')
        href = loc.get('{http://www.w3.org/1999/xlink}href')
        if href and '#' in href:
            element_name = href.split('#')[-1]
            # Remove namespace prefix if present
            if ':' in element_name:
                element_name = element_name.split(':')[-1]
            locators[label] = element_name
    
    # Process definitionArc elements to build structure
    structure = defaultdict(list)
    for arc in target_role_link.findall('.//link:definitionArc', namespaces):
        from_label = arc.get('{http://www.w3.org/1999/xlink}from')
        to_label = arc.get('{http://www.w3.org/1999/xlink}to')
        order = arc.get('order')
        
        from_element = locators.get(from_label)
        to_element = locators.get(to_label)
        
        if from_element and to_element:
            structure[from_element].append((to_element, order))
    
    return dict(structure)

def extract_product_revenue_from_instance(instance_file_path, context_id=None):
    """
    Extract product revenue facts from XBRL instance document
    
    Args:
        instance_file_path (str): Path to XBRL instance file
        context_id (str): Optional context ID to filter facts
        
    Returns:
        dict: Dictionary of product revenue facts
    """
    tree = ET.parse(instance_file_path)
    root = tree.getroot()
    
    # Define namespaces
    namespaces = {
        'xbrli': 'http://www.xbrl.org/2003/instance',
        'us-gaap': 'http://fasb.org/us-gaap/2024',
        'aapl': 'http://www.apple.com/20240928',
        'dei': 'http://xbrl.sec.gov/dei/2024',
        'xbrldi': 'http://xbrl.org/2006/xbrldi'
    }
    
    product_revenue = {}
    
    # Extract revenue facts
    revenue_elements = root.findall('.//us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax', namespaces)
    
    for elem in revenue_elements:
        context_ref = elem.get('contextRef')
        if context_id and context_ref != context_id:
            continue
            
        # Get the value
        value = elem.text.strip() if elem.text else "0"
        
        # Find the context to determine which product this is for
        context_elem = root.find(f'.//xbrli:context[@id="{context_ref}"]', namespaces)
        if context_elem is not None:
            # Look for explicit member that indicates the product
            explicit_members = context_elem.findall('.//xbrldi:explicitMember', namespaces)
            for member in explicit_members:
                dimension = member.get('dimension')
                member_value = member.text
                if dimension and 'ProductOrServiceAxis' in dimension:
                    # Extract just the member name (e.g., aapl:IPhoneMember -> IPhoneMember)
                    if ':' in member_value:
                        member_name = member_value.split(':')[-1]
                    else:
                        member_name = member_value
                    
                    # Get the period information for this context
                    period_info = {}
                    period_elem = context_elem.find('.//xbrli:period', namespaces)
                    if period_elem is not None:
                        start_date = period_elem.find('.//xbrli:startDate', namespaces)
                        end_date = period_elem.find('.//xbrli:endDate', namespaces)
                        instant = period_elem.find('.//xbrli:instant', namespaces)
                        
                        if start_date is not None and end_date is not None:
                            period_info = {
                                'start_date': start_date.text,
                                'end_date': end_date.text
                            }
                        elif instant is not None:
                            period_info = {
                                'instant': instant.text
                            }
                    
                    # Create revenue entry with period information
                    revenue_entry = {
                        'value': value,
                        'contextRef': context_ref,
                        'period': period_info
                    }
                    
                    # If we already have an entry for this product, check if this one is more recent
                    if member_name in product_revenue:
                        # Compare periods to keep the most recent data
                        existing_entry = product_revenue[member_name]
                        if is_more_recent_period(period_info, existing_entry.get('period', {})):
                            product_revenue[member_name] = revenue_entry
                    else:
                        product_revenue[member_name] = revenue_entry
    
    return product_revenue

def is_more_recent_period(new_period, existing_period):
    """
    Determine if the new period is more recent than the existing period
    
    Args:
        new_period (dict): New period information
        existing_period (dict): Existing period information
        
    Returns:
        bool: True if new period is more recent, False otherwise
    """
    try:
        # Extract end dates for comparison
        new_end_date = None
        existing_end_date = None
        
        if 'end_date' in new_period:
            new_end_date = datetime.strptime(new_period['end_date'], '%Y-%m-%d')
        elif 'instant' in new_period:
            new_end_date = datetime.strptime(new_period['instant'], '%Y-%m-%d')
            
        if 'end_date' in existing_period:
            existing_end_date = datetime.strptime(existing_period['end_date'], '%Y-%m-%d')
        elif 'instant' in existing_period:
            existing_end_date = datetime.strptime(existing_period['instant'], '%Y-%m-%d')
        
        # If we have dates for both, compare them
        if new_end_date and existing_end_date:
            return new_end_date > existing_end_date
        elif new_end_date:
            return True
        else:
            return False
    except (ValueError, KeyError):
        # If we can't parse the dates, default to keeping the existing entry
        return False

def format_revenue_value(value):
    """
    Format revenue value for better readability
    
    Args:
        value (str): Value to format
        
    Returns:
        str: Formatted value
    """
    try:
        # Try to convert to float
        num_value = float(value)
        # Format large numbers with commas and in millions
        return f"${num_value / 1_000_000:,.1f}M"
    except ValueError:
        # If it's not a number, return as is
        return value

def analyze_revenue_by_product(instance_file_path, xsd_file_path, def_file_path, context_id=None):
    """
    Analyze revenue by product by combining XSD definitions, definition linkbase structure, and instance facts
    
    Args:
        instance_file_path (str): Path to XBRL instance file
        xsd_file_path (str): Path to XSD schema file
        def_file_path (str): Path to definition linkbase file
        context_id (str): Optional context ID to filter facts
        
    Returns:
        str: Formatted revenue analysis by product
    """
    # Parse XSD for product members
    product_members = parse_xsd_for_products(xsd_file_path)
    
    # Parse definition linkbase for revenue structure
    structure = parse_definition_linkbase_for_revenue_structure(def_file_path)
    
    # Extract product revenue from instance document
    product_revenue = extract_product_revenue_from_instance(instance_file_path, context_id)
    
    # Generate output
    result_lines = []
    result_lines.append("Apple Revenue Analysis by Product")
    result_lines.append("=" * 80)
    
    # Add information about the context if specified
    if context_id:
        result_lines.append(f"Context: {context_id}")
    
    # Display product members found in XSD
    result_lines.append("\nProduct Members from XSD:")
    result_lines.append("-" * 40)
    for member in product_members:
        result_lines.append(f"  - {member}")
    
    # Display structure from definition linkbase
    result_lines.append("\nRevenue Structure from Definition Linkbase:")
    result_lines.append("-" * 40)
    for parent, children in structure.items():
        result_lines.append(f"  {parent}:")
        for child, order in children:
            result_lines.append(f"    - {child}")
    
    # Display revenue by product
    result_lines.append("\nRevenue by Product:")
    result_lines.append("-" * 40)
    
    total_revenue = 0
    product_total = 0
    service_total = 0
    
    # Calculate totals based on specific product categories
    for product, info in product_revenue.items():
        value = info.get('value', 'N/A')
        
        try:
            revenue_value = float(value)
            
            # Categorize revenue based on product type
            if product in ['IPhoneMember', 'MacMember', 'IPadMember', 'WearablesHomeandAccessoriesMember']:
                product_total += revenue_value
            elif product in ['ServiceMember']:
                service_total += revenue_value
            elif product in ['ProductMember']:
                # This is the total of all products, so we don't add it to product_total
                # to avoid double counting
                pass
                
            total_revenue += revenue_value
            
        except ValueError:
            pass
    
    # Display individual product revenues
    for product, info in product_revenue.items():
        value = info.get('value', 'N/A')
        context_ref = info.get('contextRef', 'N/A')
        period = info.get('period', {})
        
        try:
            formatted_value = format_revenue_value(value)
            
            # Add period information to the output
            period_str = ""
            if 'end_date' in period:
                period_str = f" (Period: {period.get('start_date', '')} to {period['end_date']})"
            elif 'instant' in period:
                period_str = f" (Instant: {period['instant']})"
            
            result_lines.append(f"  {product}: {formatted_value}{period_str} [{context_ref}]")
        except ValueError:
            result_lines.append(f"  {product}: {value}")
    
    # Add totals
    result_lines.append("-" * 40)
    result_lines.append(f"  Product Total (IPhone+Mac+IPad+Wearables): {format_revenue_value(str(product_total))}")
    result_lines.append(f"  Service Total: {format_revenue_value(str(service_total))}")
    result_lines.append(f"  Grand Total: {format_revenue_value(str(product_total + service_total))}")
    
    result_lines.append("")
    result_lines.append(f"Total product revenue items: {len(product_revenue)}")
    result_lines.append("=" * 80)
    
    return "\n".join(result_lines)
