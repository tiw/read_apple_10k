import xml.etree.ElementTree as ET
from collections import defaultdict
from .translation import FINANCIAL_TERMS

def list_all_contexts(xbrl_file_path):
    """
    List all contexts in the XBRL file.
    
    Args:
        xbrl_file_path (str): Path to the XBRL file
        
    Returns:
        list: List of context IDs
    """
    tree = ET.parse(xbrl_file_path)
    root = tree.getroot()
    
    namespaces = {
        'xbrli': 'http://www.xbrl.org/2003/instance'
    }
    
    contexts = []
    for context in root.findall('.//xbrli:context', namespaces):
        context_id = context.attrib.get('id')
        if context_id:
            contexts.append(context_id)
    
    return contexts

def get_context_info(xbrl_file_path, context_id):
    """
    Get detailed information about a specific context.
    
    Args:
        xbrl_file_path (str): Path to the XBRL file
        context_id (str): Context ID to get information for
        
    Returns:
        dict: Context information including period and dimensions
    """
    tree = ET.parse(xbrl_file_path)
    root = tree.getroot()
    
    namespaces = {
        'xbrli': 'http://www.xbrl.org/2003/instance',
        'dei': 'http://xbrl.sec.gov/dei/2024',
        'us-gaap': 'http://fasb.org/us-gaap/2024',
        'aapl': 'http://www.apple.com/20240928',
        'country': 'http://xbrl.sec.gov/country/2024',
        'ecd': 'http://xbrl.sec.gov/ecd/2024',
        'iso4217': 'http://www.xbrl.org/2003/iso4217',
        'srt': 'http://fasb.org/srt/2024',
        'xbrldi': 'http://xbrl.org/2006/xbrldi'
    }
    
    # Check if context exists
    context_found = False
    context_info = {
        'period_info': "No period info",
        'dimensions': []
    }
    
    for context_elem in root.findall('.//xbrli:context', namespaces):
        if context_elem.attrib.get('id') == context_id:
            context_found = True
            period_elem = context_elem.find('.//xbrli:period', namespaces)
            if period_elem is not None:
                instant = period_elem.find('.//xbrli:instant', namespaces)
                start_date = period_elem.find('.//xbrli:startDate', namespaces)
                end_date = period_elem.find('.//xbrli:endDate', namespaces)
                
                if instant is not None:
                    context_info['period_info'] = f"Instant: {instant.text}"
                elif start_date is not None and end_date is not None:
                    context_info['period_info'] = f"Period: {start_date.text} to {end_date.text}"
                elif start_date is not None:
                    context_info['period_info'] = f"Start date: {start_date.text}"
                elif end_date is not None:
                    context_info['period_info'] = f"End date: {end_date.text}"
            
            # Get dimension information
            explicit_members = context_elem.findall('.//xbrldi:explicitMember', namespaces)
            for member in explicit_members:
                dimension = member.attrib.get('dimension', '')
                member_value = member.text if member.text else ''
                context_info['dimensions'].append({
                    'dimension': dimension,
                    'member': member_value
                })
            break
    
    if not context_found:
        return None
    
    return context_info

def list_facts_for_context(xbrl_file_path, context_id):
    """
    List all facts for a specific context ID.
    
    Args:
        xbrl_file_path (str): Path to the XBRL file
        context_id (str): Context ID to list facts for
        
    Returns:
        str: Formatted list of facts
    """
    # Get context information
    context_info = get_context_info(xbrl_file_path, context_id)
    if context_info is None:
        return f"Context ID '{context_id}' not found in the XBRL file."
    
    tree = ET.parse(xbrl_file_path)
    root = tree.getroot()
    
    # Define namespaces
    namespaces = {
        'xbrli': 'http://www.xbrl.org/2003/instance',
        'dei': 'http://xbrl.sec.gov/dei/2024',
        'us-gaap': 'http://fasb.org/us-gaap/2024',
        'aapl': 'http://www.apple.com/20240928',
        'country': 'http://xbrl.sec.gov/country/2024',
        'ecd': 'http://xbrl.sec.gov/ecd/2024',
        'iso4217': 'http://www.xbrl.org/2003/iso4217',
        'srt': 'http://fasb.org/srt/2024',
        'xbrldi': 'http://xbrl.org/2006/xbrldi'
    }
    
    # Collect facts for the specified context
    facts = []
    for elem in root.iter():
        if 'contextRef' in elem.attrib and elem.attrib['contextRef'] == context_id:
            # Get the tag name
            tag_name = elem.tag
            if tag_name.startswith('{'):
                # Handle namespaced elements like {http://www.apple.com/20240928}TagName
                ns_uri, local_name = tag_name[1:].split('}', 1)
                tag_name = local_name
            
            # Get the value and unit (if available)
            value = elem.text if elem.text else ""
            unit_ref = elem.attrib.get('unitRef', '')
            
            # Format unit information
            unit_info = f" (Unit: {unit_ref})" if unit_ref else ""
            
            facts.append((tag_name, value, unit_info))
    
    # Format results
    result_lines = [f"Facts for Context ID: {context_id}"]
    
    # Add context information
    result_lines.append(f"Period: {context_info['period_info']}")
    
    # Add dimension information if available
    if context_info['dimensions']:
        result_lines.append("Dimensions:")
        for dim in context_info['dimensions']:
            # Make dimension and member names more readable
            dim_name = dim['dimension'].split(':')[-1] if ':' in dim['dimension'] else dim['dimension']
            member_name = dim['member'].split(':')[-1] if ':' in dim['member'] else dim['member']
            result_lines.append(f"  {dim_name}: {member_name}")
    
    result_lines.append("=" * 80)
    result_lines.append(f"{'Tag Name':<40} {'Chinese Name':<30} {'Value':<20}")
    result_lines.append("-" * 80)
    
    for tag_name, value, unit_info in facts:
        # Get Chinese translation
        chinese_name = FINANCIAL_TERMS.get(tag_name, "")
        result_lines.append(f"{tag_name:<40} {chinese_name:<30} {value:<20}")
    
    result_lines.append("=" * 80)
    result_lines.append(f"Total Facts: {len(facts)}")
    
    return "\n".join(result_lines)

def list_facts_by_presentation(xbrl_file_path, context_id, presentation_file_path):
    """
    List facts for a specific context ID grouped by presentation categories.
    
    Args:
        xbrl_file_path (str): Path to the XBRL file
        context_id (str): Context ID to list facts for
        presentation_file_path (str): Path to the presentation XML file
        
    Returns:
        str: Formatted list of facts grouped by presentation categories
    """
    # Parse the XBRL file
    xbrl_tree = ET.parse(xbrl_file_path)
    xbrl_root = xbrl_tree.getroot()
    
    # Parse the presentation file
    pres_tree = ET.parse(presentation_file_path)
    pres_root = pres_tree.getroot()
    
    # Define namespaces for both files
    xbrl_namespaces = {
        'xbrli': 'http://www.xbrl.org/2003/instance',
        'dei': 'http://xbrl.sec.gov/dei/2024',
        'us-gaap': 'http://fasb.org/us-gaap/2024',
        'aapl': 'http://www.apple.com/20240928',
        'country': 'http://xbrl.sec.gov/country/2024',
        'ecd': 'http://xbrl.sec.gov/ecd/2024',
        'iso4217': 'http://www.xbrl.org/2003/iso4217',
        'srt': 'http://fasb.org/srt/2024',
        'xbrldi': 'http://xbrl.org/2006/xbrldi'
    }
    
    pres_namespaces = {
        'link': 'http://www.xbrl.org/2003/linkbase',
        'xlink': 'http://www.w3.org/1999/xlink'
    }
    
    # Collect facts for the specified context from XBRL file
    facts = {}
    for elem in xbrl_root.iter():
        if 'contextRef' in elem.attrib and elem.attrib['contextRef'] == context_id:
            # Get the tag name
            tag_name = elem.tag
            if tag_name.startswith('{'):
                # Handle namespaced elements like {http://www.apple.com/20240928}TagName
                ns_uri, local_name = tag_name[1:].split('}', 1)
                tag_name = local_name
            
            # Get the value and unit (if available)
            value = elem.text if elem.text else ""
            unit_ref = elem.attrib.get('unitRef', '')
            
            # Format unit information
            unit_info = f" (Unit: {unit_ref})" if unit_ref else ""
            
            facts[tag_name] = {
                'namespace': next((k for k, v in xbrl_namespaces.items() if v == ns_uri), ns_uri.split('/')[-1]) if tag_name.startswith('{') else "",
                'value': value,
                'unit': unit_info
            }
    
    # Check if context exists
    context_found = False
    period_info = "No period info"
    
    # Find context using explicit namespace handling
    for context_elem in xbrl_root.findall('.//xbrli:context', xbrl_namespaces):
        if context_elem.attrib.get('id') == context_id:
            context_found = True
            period_elem = context_elem.find('.//xbrli:period', xbrl_namespaces)
            if period_elem is not None:
                instant = period_elem.find('.//xbrli:instant', xbrl_namespaces)
                start_date = period_elem.find('.//xbrli:startDate', xbrl_namespaces)
                end_date = period_elem.find('.//xbrli:endDate', xbrl_namespaces)
                
                if instant is not None:
                    period_info = f"Instant: {instant.text}"
                elif start_date is not None and end_date is not None:
                    period_info = f"Period: {start_date.text} to {end_date.text}"
                elif start_date is not None:
                    period_info = f"Start date: {start_date.text}"
                elif end_date is not None:
                    period_info = f"End date: {end_date.text}"
            break
    
    if not context_found:
        return f"Context ID '{context_id}' not found in the XBRL file."
    
    # Extract presentation structure
    presentation_groups = defaultdict(list)
    
    # Process each presentationLink in the presentation file
    for pres_link in pres_root.findall('.//link:presentationLink', pres_namespaces):
        role = pres_link.attrib.get('{http://www.w3.org/1999/xlink}role', '')
        # Extract a readable name from the role URI
        group_name = role.split('/')[-1] if '/' in role else role
        
        # Find all locators in this presentation link
        locators = {}
        for loc in pres_link.findall('.//link:loc', pres_namespaces):
            label = loc.attrib.get('{http://www.w3.org/1999/xlink}label', '')
            href = loc.attrib.get('{http://www.w3.org/1999/xlink}href', '')
            # Extract element name from href (format: "file.xsd#element_name")
            if '#' in href:
                element_name = href.split('#')[-1]
                # Remove namespace prefix if present (e.g., "us-gaap_" or "aapl_")
                if '_' in element_name:
                    element_name = '_'.join(element_name.split('_')[1:])
                locators[label] = element_name
        
        # Find facts that match the elements in this presentation group
        for label, element_name in locators.items():
            # Check if the element name exists in our facts
            if element_name in facts:
                presentation_groups[group_name].append({
                    'tag': element_name,
                    'namespace': facts[element_name]['namespace'],
                    'value': facts[element_name]['value'],
                    'unit': facts[element_name]['unit']
                })
    
    # Format results
    result_lines = [f"Facts for Context ID: {context_id} (Grouped by Presentation)"]
    result_lines.append(f"Period: {period_info}")
    result_lines.append("=" * 120)
    
    # Display facts grouped by presentation
    for group_name, group_facts in presentation_groups.items():
        if group_facts:  # Only show groups that have facts for this context
            # Make the group name more readable by removing prefixes like "http://www.apple.com/role/"
            readable_group_name = group_name.replace("http://www.apple.com/role/", "")
            result_lines.append(f"\n{readable_group_name}:")
            result_lines.append("-" * 80)
            result_lines.append(f"{'Namespace':<15} {'Tag Name':<35} {'Chinese Name':<40} {'Value':<30}")
            result_lines.append("-" * 80)
            
            for fact in group_facts:
                # Get Chinese translation
                chinese_name = FINANCIAL_TERMS.get(fact['tag'], "")
                
                # Truncate long values
                value_display = fact['value'][:27] + "..." if len(fact['value']) > 30 else fact['value']
                result_lines.append(f"{fact['namespace']:<15} {fact['tag']:<35} {chinese_name:<40} {value_display:<30}")
    
    result_lines.append("=" * 120)
    total_facts = sum(len(group_facts) for group_facts in presentation_groups.values())
    result_lines.append(f"Total Facts: {total_facts}")
    
    return "\n".join(result_lines)

def calculate_formulas(xbrl_file_path, context_id, calculation_file_path, filter_zero=False):
    """
    Calculate formulas based on calculation definitions and XBRL facts.
    
    Args:
        xbrl_file_path (str): Path to the XBRL file
        context_id (str): Context ID to calculate formulas for
        calculation_file_path (str): Path to the calculation XML file
        filter_zero (bool): Whether to filter out calculations where all factors are zero
        
    Returns:
        str: Formatted list of calculated formulas
    """
    # Parse the XBRL file
    xbrl_tree = ET.parse(xbrl_file_path)
    xbrl_root = xbrl_tree.getroot()
    
    # Parse the calculation file
    calc_tree = ET.parse(calculation_file_path)
    calc_root = calc_tree.getroot()
    
    # Define namespaces
    xbrl_namespaces = {
        'xbrli': 'http://www.xbrl.org/2003/instance',
        'dei': 'http://xbrl.sec.gov/dei/2024',
        'us-gaap': 'http://fasb.org/us-gaap/2024',
        'aapl': 'http://www.apple.com/20240928',
        'country': 'http://xbrl.sec.gov/country/2024',
        'ecd': 'http://xbrl.sec.gov/ecd/2024',
        'iso4217': 'http://www.xbrl.org/2003/iso4217',
        'srt': 'http://fasb.org/srt/2024',
        'xbrldi': 'http://xbrl.org/2006/xbrldi'
    }
    
    calc_namespaces = {
        'link': 'http://www.xbrl.org/2003/linkbase',
        'xlink': 'http://www.w3.org/1999/xlink'
    }
    
    # Collect facts for the specified context from XBRL file
    facts = {}
    for elem in xbrl_root.iter():
        if 'contextRef' in elem.attrib and elem.attrib['contextRef'] == context_id:
            # Get the tag name
            tag_name = elem.tag
            if tag_name.startswith('{'):
                # Handle namespaced elements like {http://www.apple.com/20240928}TagName
                ns_uri, local_name = tag_name[1:].split('}', 1)
                tag_name = local_name
            
            # Get the value and unit (if available)
            value = elem.text if elem.text else "0"
            # Convert to float for calculations
            try:
                facts[tag_name] = float(value)
            except ValueError:
                facts[tag_name] = 0.0
    
    # Check if context exists
    context_found = False
    period_info = "No period info"
    
    # Find context using explicit namespace handling
    for context_elem in xbrl_root.findall('.//xbrli:context', xbrl_namespaces):
        if context_elem.attrib.get('id') == context_id:
            context_found = True
            period_elem = context_elem.find('.//xbrli:period', xbrl_namespaces)
            if period_elem is not None:
                instant = period_elem.find('.//xbrli:instant', xbrl_namespaces)
                start_date = period_elem.find('.//xbrli:startDate', xbrl_namespaces)
                end_date = period_elem.find('.//xbrli:endDate', xbrl_namespaces)
                
                if instant is not None:
                    period_info = f"Instant: {instant.text}"
                elif start_date is not None and end_date is not None:
                    period_info = f"Period: {start_date.text} to {end_date.text}"
                elif start_date is not None:
                    period_info = f"Start date: {start_date.text}"
                elif end_date is not None:
                    period_info = f"End date: {end_date.text}"
            break
    
    if not context_found:
        return f"Context ID '{context_id}' not found in the XBRL file."
    
    # Extract calculation structure
    calculation_groups = defaultdict(list)
    
    # Process each calculationLink in the calculation file
    for calc_link in calc_root.findall('.//link:calculationLink', calc_namespaces):
        role = calc_link.attrib.get('{http://www.w3.org/1999/xlink}role', '')
        # Extract a readable name from the role URI
        group_name = role.split('/')[-1] if '/' in role else role
        
        # Find all locators in this calculation link
        locators = {}
        for loc in calc_link.findall('.//link:loc', calc_namespaces):
            label = loc.attrib.get('{http://www.w3.org/1999/xlink}label', '')
            href = loc.attrib.get('{http://www.w3.org/1999/xlink}href', '')
            # Extract element name from href (format: "file.xsd#element_name")
            if '#' in href:
                element_name = href.split('#')[-1]
                # Remove namespace prefix if present (e.g., "us-gaap_" or "aapl_")
                if '_' in element_name:
                    element_name = '_'.join(element_name.split('_')[1:])
                locators[label] = element_name
        
        # Find calculation arcs
        calculations = []
        for arc in calc_link.findall('.//link:calculationArc', calc_namespaces):
            from_label = arc.attrib.get('{http://www.w3.org/1999/xlink}from', '')
            to_label = arc.attrib.get('{http://www.w3.org/1999/xlink}to', '')
            weight = float(arc.attrib.get('weight', '1.0'))
            
            from_element = locators.get(from_label)
            to_element = locators.get(to_label)
            
            if from_element and to_element:
                calculations.append({
                    'from': from_element,
                    'to': to_element,
                    'weight': weight
                })
        
        if calculations:
            calculation_groups[group_name].extend(calculations)
    
    # Perform calculations and format results
    result_lines = [f"Formula Calculations for Context ID: {context_id}"]
    result_lines.append(f"Period: {period_info}")
    if filter_zero:
        result_lines.append("Filtering out calculations where all factors are zero")
    result_lines.append("=" * 100)
    
    # Display calculations grouped by role
    for group_name, calculations in calculation_groups.items():
        if calculations:  # Only show groups that have calculations
            # Make the group name more readable
            readable_group_name = group_name.replace("http://www.apple.com/role/", "")
            
            # Group calculations by 'from' element
            calc_by_from = defaultdict(list)
            for calc in calculations:
                calc_by_from[calc['from']].append(calc)
            
            # Check if this group has any calculations
            group_content_lines = []
            
            for from_element, calc_items in calc_by_from.items():
                from_value = facts.get(from_element, 0.0)
                calculated_sum = 0.0
                
                # Calculate the sum
                for calc in calc_items:
                    to_element = calc['to']
                    weight = calc['weight']
                    to_value = facts.get(to_element, 0.0)
                    weighted_value = to_value * weight
                    calculated_sum += weighted_value
                
                # Skip if filter_zero is True and the result is zero
                if filter_zero and from_value == 0.0:
                    continue
                chinese_name_from = FINANCIAL_TERMS.get(from_element, "")
                group_content_lines.append(f"\n{from_element} ({chinese_name_from}): {from_value:,.2f}")
                
                for calc in calc_items:
                    to_element = calc['to']
                    weight = calc['weight']
                    to_value = facts.get(to_element, 0.0)
                    weighted_value = to_value * weight
                    
                    chinese_name_to = FINANCIAL_TERMS.get(to_element, "")
                    sign = "+" if weight >= 0 else "-"
                    group_content_lines.append(f"  {sign} {abs(weight):.1f} * {to_element} ({chinese_name_to}): {to_value:,.2f} = {weighted_value:,.2f}")
                
                # Check if calculation is correct
                if abs(from_value - calculated_sum) < 0.01:  # Allow for small rounding differences
                    group_content_lines.append(f"  ✓ Calculation verified: {from_value:,.2f} ≈ {calculated_sum:,.2f}")
                else:
                    group_content_lines.append(f"  ✗ Calculation mismatch: {from_value:,.2f} ≠ {calculated_sum:,.2f}")
            
            # Only add group if it has content when filtering
            if group_content_lines or not filter_zero:
                result_lines.append(f"\n{readable_group_name}:")
                result_lines.append("-" * 80)
                result_lines.extend(group_content_lines)
    
    result_lines.append("=" * 100)
    return "\n".join(result_lines)