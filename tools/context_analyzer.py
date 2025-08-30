"""
Module for analyzing GAAP facts and their contexts in XBRL files
"""

import xml.etree.ElementTree as ET
from collections import defaultdict


def analyze_contexts(xbrl_file_path):
    """
    Analyze the XBRL file to count GAAP facts per context.
    
    Args:
        xbrl_file_path (str): Path to the XBRL file
        
    Returns:
        str: Formatted analysis results
    """
    # Parse the XML file
    tree = ET.parse(xbrl_file_path)
    root = tree.getroot()
    
    # Namespace definitions
    namespaces = {
        'xbrli': 'http://www.xbrl.org/2003/instance',
        'us-gaap': 'http://fasb.org/us-gaap/2024',
        'dei': 'http://xbrl.sec.gov/dei/2024',
        'xbrldi': 'http://xbrl.org/2006/xbrldi'
    }
    
    # Add namespaces from the root element if not already defined
    for elem in root.iter():
        if elem.tag.startswith('{'):
            ns_uri, local_name = elem.tag[1:].split('}', 1)
            if not any(ns_uri in ns for ns in namespaces.values()):
                # Extract prefix from tag if possible, otherwise use a generic name
                prefix = local_name.lower()[:4] if len(local_name) > 4 else local_name.lower()
                namespaces[prefix] = ns_uri
    
    # Count facts per context
    context_counts = defaultdict(int)
    
    # Find all facts (elements with contextRef)
    for elem in root.iter():
        if 'contextRef' in elem.attrib:
            context_ref = elem.attrib['contextRef']
            context_counts[context_ref] += 1
    
    # Extract context details
    context_details = {}
    for context_elem in root.findall('.//xbrli:context', namespaces):
        context_id = context_elem.attrib.get('id')
        if context_id in context_counts:
            # Get period information
            period_elem = context_elem.find('.//xbrli:period', namespaces)
            period_info = "No period info"
            if period_elem is not None:
                instant = period_elem.find('.//xbrli:instant', namespaces)
                start_date = period_elem.find('.//xbrli:startDate', namespaces)
                end_date = period_elem.find('.//xbrli:endDate', namespaces)
                
                if instant is not None:
                    period_info = f"Instant: {instant.text}"
                elif start_date is not None and end_date is not None:
                    period_info = f"Period: {start_date.text} to {end_date.text}"
                elif start_date is not None:
                    period_info = f"Start date: {start_date.text}"
                elif end_date is not None:
                    period_info = f"End date: {end_date.text}"
            
            # Get entity information
            entity_info = "No entity info"
            entity_elem = context_elem.find('.//xbrli:entity', namespaces)
            if entity_elem is not None:
                identifier_elem = entity_elem.find('.//xbrli:identifier', namespaces)
                if identifier_elem is not None:
                    entity_info = f"Entity: {identifier_elem.text} ({identifier_elem.attrib.get('scheme', 'no scheme')})"
            
            context_details[context_id] = {
                'period': period_info,
                'entity': entity_info
            }
    
    # Format results
    result_lines = ["GAAP Facts per Context Analysis:"]
    result_lines.append("=" * 80)
    result_lines.append(f"{'Context ID':<15} {'Fact Count':<10} {'Period':<30} {'Entity'}")
    result_lines.append("-" * 80)
    
    # Sort contexts by count (descending)
    sorted_contexts = sorted(context_counts.items(), key=lambda x: x[1], reverse=True)
    
    for context_id, count in sorted_contexts:
        period = context_details.get(context_id, {}).get('period', 'N/A') if context_id in context_details else 'N/A'
        entity = context_details.get(context_id, {}).get('entity', 'N/A') if context_id in context_details else 'N/A'
        result_lines.append(f"{context_id:<15} {count:<10} {period:<30} {entity}")
    
    result_lines.append("-" * 80)
    result_lines.append(f"Total Contexts: {len(context_counts)}")
    result_lines.append(f"Total GAAP Facts: {sum(context_counts.values())}")
    
    return "\n".join(result_lines)