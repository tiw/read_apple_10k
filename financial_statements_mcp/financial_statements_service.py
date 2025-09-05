"""
Financial Statements MCP Service

This service provides access to financial statements (income statement, balance sheet, cash flow statement)
for major companies based on their SEC XBRL filings.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime
import duckdb
import xml.etree.ElementTree as ET
import os
from pathlib import Path
import sys


@dataclass
class FinancialStatements:
    """Complete financial statements data"""
    company_name: str
    cik: str
    fiscal_year: int
    filing_date: str
    balance_sheet: Dict[str, Any]
    income_statement: Dict[str, Any]
    cash_flow_statement: Dict[str, Any]
    data_quality_score: float
    validation_errors: List[str]


@dataclass
class BalanceSheet:
    """Balance sheet data structure"""
    assets: Dict[str, float]
    liabilities: Dict[str, float]
    equity: Dict[str, float]
    total_assets: float
    total_liabilities: float
    total_equity: float


@dataclass
class IncomeStatement:
    """Income statement data structure"""
    revenue: float
    cost_of_goods_sold: float
    gross_profit: float
    operating_expenses: Dict[str, float]
    operating_income: float
    net_income: float
    eps_basic: float
    eps_diluted: float


@dataclass
class CashFlowStatement:
    """Cash flow statement data structure"""
    operating_activities: float
    investing_activities: float
    financing_activities: float
    net_cash_flow: float


class CompanyIdentifier:
    """Maps company symbols to CIK and other identifiers"""
    
    COMPANY_MAPPING = {
        'AAPL': {'name': 'Apple Inc.', 'cik': '0000320193'},
        'MSFT': {'name': 'Microsoft Corporation', 'cik': '0000789019'},
        'GOOGL': {'name': 'Alphabet Inc.', 'cik': '0001652044'},
        'AMZN': {'name': 'Amazon.com Inc.', 'cik': '0001018724'},
        'META': {'name': 'Meta Platforms Inc.', 'cik': '0001326801'},
        'TSLA': {'name': 'Tesla Inc.', 'cik': '0001318605'},
        'NVDA': {'name': 'NVIDIA Corporation', 'cik': '0001045810'}
    }
    
    @classmethod
    def get_company_info(cls, symbol: str) -> Optional[Dict[str, str]]:
        """Get company information by symbol"""
        return cls.COMPANY_MAPPING.get(symbol.upper())
    
    @classmethod
    def get_supported_companies(cls) -> List[str]:
        """Get list of supported company symbols"""
        return list(cls.COMPANY_MAPPING.keys())


class PreXMLAnalyzer:
    """Analyzes pre.xml files to extract financial statement structure and metrics"""
    
    def __init__(self, data_root: str = None):
        if data_root is None:
            current_dir = Path(__file__).parent
            project_root = current_dir.parent
            self.data_root = project_root / 'magnificent_seven_10k_optimized'
        else:
            self.data_root = Path(data_root)
        
        self.structure_cache = {}
    
    def get_financial_statement_structure(self, company_symbol: str, filing_date: str) -> Dict[str, Any]:
        """Extract financial statement structure from pre.xml"""
        cache_key = f"{company_symbol}_{filing_date}"
        if cache_key in self.structure_cache:
            return self.structure_cache[cache_key]
        
        # Find the filing directory
        company_dir = self.data_root / company_symbol
        if not company_dir.exists():
            return {}
        
        # Find the specific filing directory
        filing_dirs = [d for d in company_dir.iterdir() if d.is_dir()]
        target_dir = None
        
        # Try to match the filing date (convert 2023-06-30 to 20230630)
        filing_date_clean = filing_date.replace('-', '')
        
        # Look for exact match first
        for filing_dir in filing_dirs:
            if filing_date_clean in filing_dir.name:
                target_dir = filing_dir
                break
        
        # If not found, try to match year
        if not target_dir:
            year = filing_date.split('-')[0]  # Extract year from 2023-06-30
            for filing_dir in filing_dirs:
                if year in filing_dir.name:
                    target_dir = filing_dir
                    break
        
        # If still not found, use the most recent filing
        if not target_dir:
            filing_dirs.sort(key=lambda x: x.name, reverse=True)
            if filing_dirs:
                target_dir = filing_dirs[0]
            else:
                return {}
        
        # Look for pre.xml file
        pre_files = list(target_dir.glob("*_pre.xml"))
        if not pre_files:
            return {}
        
        # Parse the pre.xml file to extract structure
        structure = self._parse_pre_xml_structure(pre_files[0])
        self.structure_cache[cache_key] = structure
        return structure
    
    def _parse_pre_xml_structure(self, pre_file: Path) -> Dict[str, Any]:
        """Parse pre.xml file to extract financial statement structure"""
        try:
            tree = ET.parse(pre_file)
            root = tree.getroot()
            
            structure = {
                'income_statement': {'metrics': {}, 'hierarchy': {}, 'total_items': []},
                'balance_sheet': {'metrics': {}, 'hierarchy': {}, 'total_items': []},
                'cash_flow_statement': {'metrics': {}, 'hierarchy': {}, 'total_items': []}
            }
            
            # Find all presentation links
            ns = {
                'link': 'http://www.xbrl.org/2003/linkbase',
                'xlink': 'http://www.w3.org/1999/xlink',
                'xbrll': 'http://www.xbrl.org/2003/linkbase'
            }
            
            # Find comprehensive financial statements by analyzing content
            presentation_links = root.findall('.//link:presentationLink', ns)
            
            # First pass: Try role-based identification (works for AAPL, GOOGL, etc.)
            xlink_ns = 'http://www.w3.org/1999/xlink'
            
            for i, link in enumerate(presentation_links):
                role = link.get(f'{{{xlink_ns}}}role', '')
                
                # Role-based pattern matching
                statement_type = None
                role_upper = role.upper()
                
                if 'INCOMESTATEMENTS' in role_upper or 'INCOMESTATEMENT' in role_upper:
                    statement_type = 'income_statement'
                elif 'BALANCESHEETS' in role_upper or 'FINANCIALPOSITION' in role_upper:
                    statement_type = 'balance_sheet'
                elif 'CASHFLOWS' in role_upper or 'CASHFLOW' in role_upper:
                    statement_type = 'cash_flow_statement'
                
                if statement_type and not structure[statement_type]['metrics']:
                    # Extract metrics to confirm this is a comprehensive statement
                    locators = link.findall('.//link:loc', ns)
                    financial_metrics = []
                    for loc in locators:
                        href = loc.get(f'{{{xlink_ns}}}href', '')
                        if '#' in href:
                            metric_name = href.split('#')[-1]
                            if metric_name.startswith('us-gaap_'):
                                financial_metrics.append(metric_name)
                    
                    if len(financial_metrics) > 10:  # Reasonable threshold
                        print(f"Found {statement_type} via role pattern with {len(financial_metrics)} metrics in presentation link {i}")
                        self._extract_presentation_structure(link, structure[statement_type], ns)
            
            # Second pass: Content-based identification for companies with different patterns
            for i, link in enumerate(presentation_links):
                # Skip if we already processed this link
                role = link.get(f'{{{xlink_ns}}}role', '')
                if any(len(structure[stmt]['metrics']) > 0 for stmt in structure.keys()):
                    continue
                
                # Get all locators in this link
                locators = link.findall('.//link:loc', ns)
                
                # Extract all metric names
                financial_metrics = []
                for loc in locators:
                    href = loc.get(f'{{{xlink_ns}}}href', '')
                    if '#' in href:
                        metric_name = href.split('#')[-1]
                        # Filter for us-gaap metrics
                        if metric_name.startswith('us-gaap_'):
                            financial_metrics.append(metric_name)
                
                # Check if this looks like a comprehensive statement
                if len(financial_metrics) > 20:  # More than 20 metrics suggests a comprehensive statement
                    statement_type = None
                    
                    # More specific statement type identification
                    metrics_lower = [m.lower() for m in financial_metrics]
                    metrics_str = ' '.join(metrics_lower)
                    
                    # Check for specific patterns
                    if 'statementofcashflows' in metrics_str or ('cash' in metrics_str and 'flow' in metrics_str and 'operating' in metrics_str):
                        statement_type = 'cash_flow_statement'
                    elif 'statementoffinancialposition' in metrics_str or ('assets' in metrics_str and 'liabilities' in metrics_str):
                        statement_type = 'balance_sheet'
                    elif 'statementofincome' in metrics_str or ('revenue' in metrics_str and 'income' in metrics_str):
                        statement_type = 'income_statement'
                    else:
                        # Fallback to general pattern matching
                        if any('assets' in m or 'liabilities' in m or 'equity' in m for m in metrics_lower):
                            statement_type = 'balance_sheet'
                        elif any('revenue' in m or 'income' in m or 'expense' in m for m in metrics_lower):
                            statement_type = 'income_statement'
                        elif any('cash' in m or 'flow' in m for m in metrics_lower):
                            statement_type = 'cash_flow_statement'
                    
                    if statement_type and not structure[statement_type]['metrics']:  # Only use the first comprehensive statement of each type
                        print(f"Found {statement_type} with {len(financial_metrics)} metrics in presentation link {i}")
                        self._extract_presentation_structure(link, structure[statement_type], ns)
            
            return structure
            
        except Exception as e:
            print(f"Error parsing pre.xml: {e}")
            return {}
    
    def _extract_presentation_structure(self, presentation_link, statement_structure, ns):
        """Extract structure from a presentation link"""
        # Define namespace URIs
        xlink_ns = 'http://www.w3.org/1999/xlink'
        
        # Find all locators (metrics)
        locators = {}
        for loc in presentation_link.findall('.//link:loc', ns):
            label = loc.get(f'{{{xlink_ns}}}label', '')
            href = loc.get(f'{{{xlink_ns}}}href', '')
            # Extract metric name from href
            if '#' in href and label:
                metric_name = href.split('#')[-1]
                locators[label] = metric_name
        
        # Find all presentation arcs (hierarchy)
        for arc in presentation_link.findall('.//link:presentationArc', ns):
            from_label = arc.get(f'{{{xlink_ns}}}from', '')
            to_label = arc.get(f'{{{xlink_ns}}}to', '')
            order = arc.get('order', '0')
            preferred_label = arc.get(f'{{{xlink_ns}}}preferredLabel', '')
            
            if from_label in locators and to_label in locators:
                from_metric = locators[from_label]
                to_metric = locators[to_label]
                
                # Build hierarchy
                if from_metric not in statement_structure['hierarchy']:
                    statement_structure['hierarchy'][from_metric] = []
                statement_structure['hierarchy'][from_metric].append({
                    'metric': to_metric,
                    'order': int(order),
                    'preferred_label': preferred_label
                })
                
                # Add metric
                statement_structure['metrics'][to_metric] = {
                    'parent': from_metric,
                    'order': int(order),
                    'preferred_label': preferred_label
                }
                
                # Check if this is a total item
                if preferred_label == 'http://www.xbrl.org/2003/role/totalLabel':
                    statement_structure['total_items'].append(to_metric)


class ContextAnalyzer:
    """Analyzes XBRL context definitions from XML files"""
    
    def __init__(self, data_root: str = None):
        # If data_root is not provided, use the default path relative to the project root
        if data_root is None:
            # Get the current directory (mcp) and go up one level to project root
            current_dir = Path(__file__).parent
            project_root = current_dir.parent
            self.data_root = project_root / 'magnificent_seven_10k_optimized'
        else:
            self.data_root = Path(data_root)
        self.context_cache = {}
    
    def get_context_definitions(self, company_symbol: str, filing_date: str) -> Dict[str, Dict]:
        """Get context definitions from XBRL files"""
        cache_key = f"{company_symbol}_{filing_date}"
        
        if cache_key in self.context_cache:
            return self.context_cache[cache_key]
        
        # Find the filing directory
        company_dir = self.data_root / company_symbol
        if not company_dir.exists():
            return {}
        
        # Find the specific filing directory
        filing_dirs = [d for d in company_dir.iterdir() if d.is_dir()]
        target_dir = None
        
        # Try to match the filing date (convert 2023-06-30 to 20230630)
        filing_date_clean = filing_date.replace('-', '')
        
        # Look for exact match first
        for filing_dir in filing_dirs:
            if filing_date_clean in filing_dir.name:
                target_dir = filing_dir
                break
        
        # If not found, try to match year
        if not target_dir:
            year = filing_date.split('-')[0]  # Extract year from 2023-06-30
            for filing_dir in filing_dirs:
                if year in filing_dir.name:
                    target_dir = filing_dir
                    break
        
        # If still not found, use the most recent filing
        if not target_dir:
            filing_dirs.sort(key=lambda x: x.name, reverse=True)
            if filing_dirs:
                target_dir = filing_dirs[0]
            else:
                return {}
        
        # Look for the main XBRL file (try different patterns)
        xbrl_files = list(target_dir.glob("*_pre.xml"))  # Look for pre.xml files
        if not xbrl_files:
            xbrl_files = list(target_dir.glob(f"{company_symbol.lower()}-*.xml"))
        if not xbrl_files:
            xbrl_files = list(target_dir.glob("*.xml"))
        
        if not xbrl_files:
            return {}
        
        # Parse the XBRL file to extract contexts
        contexts = self._parse_xbrl_contexts(xbrl_files[0])
        self.context_cache[cache_key] = contexts
        return contexts
    
    def _parse_xbrl_contexts(self, xbrl_file: Path) -> Dict[str, Dict]:
        """Parse XBRL file to extract context definitions"""
        try:
            tree = ET.parse(xbrl_file)
            root = tree.getroot()
            
            # Find all context elements
            contexts = {}
            for context in root.findall(".//{http://www.xbrl.org/2003/instance}context"):
                context_id = context.get('id')
                if not context_id:
                    continue
                
                context_info = {'id': context_id}
                
                # Parse period
                period = context.find("{http://www.xbrl.org/2003/instance}period")
                if period is not None:
                    # Check for instant date
                    instant = period.find("{http://www.xbrl.org/2003/instance}instant")
                    if instant is not None:
                        context_info['type'] = 'instant'
                        context_info['date'] = instant.text
                    
                    # Check for start/end dates
                    else:
                        start_date = period.find("{http://www.xbrl.org/2003/instance}startDate")
                        end_date = period.find("{http://www.xbrl.org/2003/instance}endDate")
                        if start_date is not None and end_date is not None:
                            context_info['type'] = 'duration'
                            context_info['start_date'] = start_date.text
                            context_info['end_date'] = end_date.text
                
                contexts[context_id] = context_info
            
            return contexts
            
        except Exception as e:
            print(f"Error parsing XBRL file {xbrl_file}: {e}")
            return {}
    
    def find_best_context_for_metric(self, contexts: Dict[str, Dict], metric_type: str, target_year: int) -> Optional[str]:
        """Find the best context for a given metric type and year"""
        if not contexts:
            return None
        
        # Filter contexts by target year
        year_contexts = {}
        for context_id, context_info in contexts.items():
            if self._context_matches_year(context_info, target_year):
                year_contexts[context_id] = context_info
        
        if not year_contexts:
            return None
        
        if metric_type == 'balance_sheet':
            # For balance sheet: prefer instant contexts at year-end
            instant_contexts = {cid: info for cid, info in year_contexts.items() 
                               if info.get('type') == 'instant'}
            if instant_contexts:
                # Prefer contexts with year-end dates
                year_end_contexts = {cid: info for cid, info in instant_contexts.items()
                                   if self._is_year_end(info.get('date', ''))}
                if year_end_contexts:
                    return list(year_end_contexts.keys())[0]
                return list(instant_contexts.keys())[0]
        
        elif metric_type == 'income_statement':
            # For income statement: prefer duration contexts covering the fiscal year
            duration_contexts = {cid: info for cid, info in year_contexts.items() 
                               if info.get('type') == 'duration'}
            if duration_contexts:
                # Prefer contexts that cover the full fiscal year
                full_year_contexts = {cid: info for cid, info in duration_contexts.items()
                                    if self._is_full_fiscal_year(info, target_year)}
                if full_year_contexts:
                    return list(full_year_contexts.keys())[0]
                return list(duration_contexts.keys())[0]
        
        elif metric_type == 'eps':
            # For EPS: prefer instant contexts at year-end
            instant_contexts = {cid: info for cid, info in year_contexts.items() 
                               if info.get('type') == 'instant'}
            if instant_contexts:
                year_end_contexts = {cid: info for cid, info in instant_contexts.items()
                                   if self._is_year_end(info.get('date', ''))}
                if year_end_contexts:
                    return list(year_end_contexts.keys())[0]
                return list(instant_contexts.keys())[0]
        
        # Default: return first context that matches the year
        return list(year_contexts.keys())[0]
    
    def _context_matches_year(self, context_info: Dict, target_year: int) -> bool:
        """Check if context matches the target year"""
        if context_info.get('type') == 'instant':
            date_str = context_info.get('date', '')
            return str(target_year) in date_str
        
        elif context_info.get('type') == 'duration':
            end_date = context_info.get('end_date', '')
            return str(target_year) in end_date
        
        return False
    
    def _is_year_end(self, date_str: str) -> bool:
        """Check if date is a year-end date (September 30 for Apple)"""
        # This could be made more sophisticated based on company fiscal year
        return '09-30' in date_str or '12-31' in date_str
    
    def _is_full_fiscal_year(self, context_info: Dict, target_year: int) -> bool:
        """Check if duration context covers a full fiscal year"""
        start_date = context_info.get('start_date', '')
        end_date = context_info.get('end_date', '')
        
        # Simple check: if it covers most of the year
        return (str(target_year) in start_date and str(target_year) in end_date)


class DataExtractor:
    """Extracts financial data from DuckDB database"""
    
    def __init__(self, db_path: str = None, data_root: str = None):
        # If db_path is not provided, use the default path relative to the project root
        if db_path is None:
            current_dir = Path(__file__).parent
            project_root = current_dir.parent
            self.db_path = str(project_root / 'magnificent_seven_xbrl.duckdb')
        else:
            self.db_path = db_path
        
        self.conn = None
        self.context_analyzer = ContextAnalyzer(data_root)
        self.pre_xml_analyzer = PreXMLAnalyzer(data_root)
    
    def connect(self):
        """Connect to database"""
        if self.conn is None:
            self.conn = duckdb.connect(self.db_path)
    
    def disconnect(self):
        """Disconnect from database"""
        if self.conn:
            self.conn.close()
            self.conn = None
    
    def extract_financial_data(self, cik: str, fiscal_year: int, company_symbol: str = None) -> Dict[str, Any]:
        """Extract financial data for a company and year"""
        self.connect()
        
        try:
            # Get all available metrics for this company and year (dynamic approach)
            query = f'''
            SELECT ft.tag_name, ff.value, ff.unit, c.context_id, c.end_date, c.period_type, c.instant_date, xf.period_end_date
            FROM financial_facts ff
            JOIN financial_tags ft ON ff.tag_id = ft.id
            JOIN contexts c ON ff.context_id = c.id
            JOIN xbrl_files xf ON ff.xbrl_file_id = xf.id
            JOIN companies comp ON xf.company_id = comp.id
            WHERE comp.cik = '{cik}' 
            AND xf.fiscal_year = {fiscal_year}
            AND xf.filing_type = '10-K'
            ORDER BY ft.tag_name, c.context_id
            '''
            
            result = self.conn.execute(query).fetchall()
            
            # Get period end date for context analysis
            period_end_date = None
            if result:
                period_end_date = result[0][7]  # period_end_date is the 8th column
            
            # Get context definitions from XML files
            contexts = {}
            if company_symbol and period_end_date:
                contexts = self.context_analyzer.get_context_definitions(company_symbol, str(period_end_date))
            
            # Get pre.xml structure for dynamic metric classification
            pre_xml_structure = {}
            if company_symbol and period_end_date:
                pre_xml_structure = self.pre_xml_analyzer.get_financial_statement_structure(company_symbol, str(period_end_date))
            
            # Group data by metric
            metric_data = {}
            for row in result:
                tag_name, value, unit, context_id, end_date, period_type, instant_date, _ = row
                
                try:
                    numeric_value = float(value)
                    if tag_name not in metric_data:
                        metric_data[tag_name] = []
                    
                    metric_data[tag_name].append({
                        'value': numeric_value,
                        'context_ref': context_id,
                        'unit': unit,
                        'end_date': end_date,
                        'period_type': period_type,
                        'instant_date': instant_date
                    })
                except ValueError:
                    continue
            
            # Select the best value for each metric using context analysis and pre.xml structure
            financial_data = {}
            for metric, data_list in metric_data.items():
                best_value = self._select_best_value_with_pre_xml_analysis(
                    metric, data_list, contexts, pre_xml_structure, fiscal_year
                )
                if best_value:
                    financial_data[metric] = best_value
            
            return financial_data
            
        except Exception as e:
            print(f"Error extracting data: {e}")
            return {}
        finally:
            self.disconnect()
    
    def extract_financial_data_with_structure(self, cik: str, fiscal_year: int, company_symbol: str = None) -> Optional[Dict]:
        """Extract financial data with pre.xml structure information"""
        self.connect()
        
        try:
            # Get all available metrics for this company and year (dynamic approach)
            query = f'''
            SELECT ft.tag_name, ff.value, ff.unit, c.context_id, c.end_date, c.period_type, c.instant_date, xf.period_end_date
            FROM financial_facts ff
            JOIN financial_tags ft ON ff.tag_id = ft.id
            JOIN contexts c ON ff.context_id = c.id
            JOIN xbrl_files xf ON ff.xbrl_file_id = xf.id
            JOIN companies comp ON xf.company_id = comp.id
            WHERE comp.cik = '{cik}' 
            AND xf.fiscal_year = {fiscal_year}
            AND xf.filing_type = '10-K'
            ORDER BY ft.tag_name, c.context_id
            '''
            
            result = self.conn.execute(query).fetchall()
            
            # Get period end date for context analysis
            period_end_date = None
            if result:
                period_end_date = result[0][7]  # period_end_date is the 8th column
            
            # Get context definitions from XML files
            contexts = {}
            if company_symbol and period_end_date:
                contexts = self.context_analyzer.get_context_definitions(company_symbol, str(period_end_date))
            
            # Get pre.xml structure for dynamic metric classification
            pre_xml_structure = {}
            if company_symbol and period_end_date:
                pre_xml_structure = self.pre_xml_analyzer.get_financial_statement_structure(company_symbol, str(period_end_date))
            
            # Group data by metric
            metric_data = {}
            for row in result:
                tag_name, value, unit, context_id, end_date, period_type, instant_date, _ = row
                
                try:
                    numeric_value = float(value)
                    if tag_name not in metric_data:
                        metric_data[tag_name] = []
                    
                    metric_data[tag_name].append({
                        'value': numeric_value,
                        'context_ref': context_id,
                        'unit': unit,
                        'end_date': end_date,
                        'period_type': period_type,
                        'instant_date': instant_date
                    })
                except ValueError:
                    continue
            
            # Select the best value for each metric using context analysis and pre.xml structure
            financial_data = {}
            for metric, data_list in metric_data.items():
                best_value = self._select_best_value_with_pre_xml_analysis(
                    metric, data_list, contexts, pre_xml_structure, fiscal_year
                )
                if best_value:
                    financial_data[metric] = best_value
            
            return {
                'raw_data': financial_data,
                'pre_xml_structure': pre_xml_structure,
                'contexts': contexts
            }
            
        except Exception as e:
            print(f"Error extracting data: {e}")
            return {}
        finally:
            self.disconnect()
    
    def _select_best_value_with_pre_xml_analysis(self, metric: str, data_list: List[Dict], 
                                               contexts: Dict, pre_xml_structure: Dict, 
                                               fiscal_year: int) -> Optional[Dict]:
        """Select the best value using pre.xml structure and context analysis"""
        if not data_list:
            return None
        
        # Determine metric type using pre.xml structure
        metric_type = self._determine_metric_type_from_pre_xml(metric, pre_xml_structure)
        
        # Find the best context for this metric type and year
        best_context_id = None
        if contexts and metric_type:
            best_context_id = self.context_analyzer.find_best_context_for_metric(
                contexts, metric_type, fiscal_year
            )
        
        # Priority 1: Use best context if available
        if best_context_id:
            for data in data_list:
                if data['context_ref'] == best_context_id:
                    return data
        
        # Priority 2: Use pre.xml hierarchy to select most appropriate value
        if pre_xml_structure:
            best_data = self._select_value_using_pre_xml_hierarchy(metric, data_list, pre_xml_structure)
            if best_data:
                return best_data
        
        # Priority 3: Use context-based selection without XML analysis
        return self._fallback_context_selection(data_list, metric_type, fiscal_year)
    
    def _determine_metric_type_from_pre_xml(self, metric: str, pre_xml_structure: Dict) -> str:
        """Determine metric type based on pre.xml structure"""
        for statement_type, structure in pre_xml_structure.items():
            if metric in structure['metrics']:
                return statement_type
        
        # Fallback to traditional classification
        if metric in ['Assets', 'Liabilities', 'StockholdersEquity', 'AssetsCurrent', 'LiabilitiesCurrent', 
                      'AssetsNoncurrent', 'LiabilitiesNoncurrent', 'CashAndCashEquivalentsAtCarryingValue']:
            return 'balance_sheet'
        elif metric in ['RevenueFromContractWithCustomerExcludingAssessedTax', 'CostOfGoodsAndServicesSold', 
                       'OperatingIncomeLoss', 'NetIncomeLoss', 'EarningsPerShareBasic', 'EarningsPerShareDiluted']:
            return 'income_statement'
        elif 'Cash' in metric or 'Flow' in metric:
            return 'cash_flow_statement'
        
        return 'unknown'
    
    def _select_value_using_pre_xml_hierarchy(self, metric: str, data_list: List[Dict], pre_xml_structure: Dict) -> Optional[Dict]:
        """Select value using pre.xml hierarchy preferences"""
        # Priority: total items > regular items
        for statement_type, structure in pre_xml_structure.items():
            if metric in structure['total_items']:
                # This is a total item, give it priority
                # Find the value with the most complete context
                for data in sorted(data_list, key=lambda x: len(x.get('context_ref', '')), reverse=True):
                    return data
        
        # For regular items, prefer values that have complete hierarchy info
        if data_list:
            return data_list[0]
        
        return None
    
    def _fallback_context_selection(self, data_list: List[Dict], metric_type: str, fiscal_year: int) -> Optional[Dict]:
        """Fallback context-based selection"""
        if not data_list:
            return None
        
        # Simple heuristic based on metric type
        for data in data_list:
            context_ref = data.get('context_ref', '')
            end_date = data.get('end_date', '')
            
            # Prefer contexts that match the fiscal year
            if str(fiscal_year) in end_date:
                return data
        
        # Otherwise, return the first available value
        return data_list[0]


class FinancialStatementBuilder:
    """Builds structured financial statements from raw data"""
    
    def __init__(self):
        self.extractor = DataExtractor()
    
    def build_balance_sheet_with_structure(self, raw_data: Dict[str, Any], pre_xml_structure: Dict) -> BalanceSheet:
        """Build balance sheet from raw data"""
        
        assets = {
            'current_assets': raw_data.get('AssetsCurrent', {}).get('value', 0),
            'cash_and_equivalents': raw_data.get('CashAndCashEquivalentsAtCarryingValue', {}).get('value', 0),
            'marketable_securities_current': raw_data.get('MarketableSecuritiesCurrent', {}).get('value', 0),
            'accounts_receivable': raw_data.get('AccountsReceivableNetCurrent', {}).get('value', 0),
            'inventory': raw_data.get('InventoryNet', {}).get('value', 0),
            'other_current_assets': raw_data.get('OtherAssetsCurrent', {}).get('value', 0),
            'noncurrent_assets': raw_data.get('AssetsNoncurrent', {}).get('value', 0),
            'property_plant_equipment': raw_data.get('PropertyPlantAndEquipmentNet', {}).get('value', 0),
            'marketable_securities_noncurrent': raw_data.get('MarketableSecuritiesNoncurrent', {}).get('value', 0),
            'other_noncurrent_assets': raw_data.get('OtherAssetsNoncurrent', {}).get('value', 0)
        }
        
        liabilities = {
            'current_liabilities': raw_data.get('LiabilitiesCurrent', {}).get('value', 0),
            'accounts_payable': raw_data.get('AccountsPayableCurrent', {}).get('value', 0),
            'other_current_liabilities': raw_data.get('OtherLiabilitiesCurrent', {}).get('value', 0),
            'contract_liabilities': raw_data.get('ContractWithCustomerLiabilityCurrent', {}).get('value', 0),
            'commercial_paper': raw_data.get('CommercialPaper', {}).get('value', 0),
            'long_term_debt_current': raw_data.get('LongTermDebtCurrent', {}).get('value', 0),
            'noncurrent_liabilities': raw_data.get('LiabilitiesNoncurrent', {}).get('value', 0),
            'long_term_debt_noncurrent': raw_data.get('LongTermDebtNoncurrent', {}).get('value', 0),
            'other_noncurrent_liabilities': raw_data.get('OtherLiabilitiesNoncurrent', {}).get('value', 0)
        }
        
        equity = {
            'common_stock': raw_data.get('CommonStocksIncludingAdditionalPaidInCapital', {}).get('value', 0),
            'retained_earnings': raw_data.get('RetainedEarningsAccumulatedDeficit', {}).get('value', 0),
            'accumulated_other_comprehensive_income': raw_data.get('AccumulatedOtherComprehensiveIncomeLossNetOfTax', {}).get('value', 0)
        }
        
        total_assets = raw_data.get('Assets', {}).get('value', 0)
        total_liabilities = raw_data.get('Liabilities', {}).get('value', 0)
        total_equity = raw_data.get('StockholdersEquity', {}).get('value', 0)
        
        return BalanceSheet(
            assets=assets,
            liabilities=liabilities,
            equity=equity,
            total_assets=total_assets,
            total_liabilities=total_liabilities,
            total_equity=total_equity
        )
    
    def build_income_statement_with_structure(self, raw_data: Dict[str, Any], pre_xml_structure: Dict) -> IncomeStatement:
        """Build income statement from raw data"""
        
        revenue = raw_data.get('RevenueFromContractWithCustomerExcludingAssessedTax', {}).get('value', 0)
        cost_of_goods_sold = raw_data.get('CostOfGoodsAndServicesSold', {}).get('value', 0)
        gross_profit = raw_data.get('GrossProfit', {}).get('value', 0)
        
        operating_expenses = {
            'research_development': raw_data.get('ResearchAndDevelopmentExpense', {}).get('value', 0),
            'selling_general_administrative': raw_data.get('SellingGeneralAndAdministrativeExpense', {}).get('value', 0),
            'total_operating_expenses': raw_data.get('OperatingExpenses', {}).get('value', 0)
        }
        
        operating_income = raw_data.get('OperatingIncomeLoss', {}).get('value', 0)
        net_income = raw_data.get('NetIncomeLoss', {}).get('value', 0)
        eps_basic = raw_data.get('EarningsPerShareBasic', {}).get('value', 0)
        eps_diluted = raw_data.get('EarningsPerShareDiluted', {}).get('value', 0)
        
        return IncomeStatement(
            revenue=revenue,
            cost_of_goods_sold=cost_of_goods_sold,
            gross_profit=gross_profit,
            operating_expenses=operating_expenses,
            operating_income=operating_income,
            net_income=net_income,
            eps_basic=eps_basic,
            eps_diluted=eps_diluted
        )
    
    def build_cash_flow_statement_with_structure(self, raw_data: Dict[str, Any], pre_xml_structure: Dict) -> CashFlowStatement:
        """Build cash flow statement from raw data"""
        # Extract cash flow metrics from raw data
        operating_activities = 0
        investing_activities = 0
        financing_activities = 0
        net_cash_flow = 0
        
        # Look for common cash flow statement items
        cash_flow_mapping = {
            'NetCashProvidedByUsedInOperatingActivities': 'operating_activities',
            'CashFlowFromOperatingActivities': 'operating_activities',
            'NetCashProvidedByUsedInInvestingActivities': 'investing_activities',
            'CashFlowFromInvestingActivities': 'investing_activities',
            'NetCashProvidedByUsedInFinancingActivities': 'financing_activities',
            'CashFlowFromFinancingActivities': 'financing_activities',
            'NetCashFlow': 'net_cash_flow',
            'CashFlowFromContinuingOperations': 'operating_activities',
        }
        
        for metric, field in cash_flow_mapping.items():
            if metric in raw_data:
                value = raw_data[metric]
                # Handle case where value might be a dict
                if isinstance(value, dict):
                    value = value.get('value', 0)
                if field == 'operating_activities':
                    operating_activities = value
                elif field == 'investing_activities':
                    investing_activities = value
                elif field == 'financing_activities':
                    financing_activities = value
                elif field == 'net_cash_flow':
                    net_cash_flow = value
        
        # Calculate net cash flow if not directly available
        if net_cash_flow == 0:
            net_cash_flow = operating_activities + investing_activities + financing_activities
        
        return CashFlowStatement(
            operating_activities=operating_activities,
            investing_activities=investing_activities,
            financing_activities=financing_activities,
            net_cash_flow=net_cash_flow
        )
    
    def build_financial_statements(self, company_symbol: str, year: int) -> Optional[FinancialStatements]:
        """Build complete financial statements"""
        company_info = CompanyIdentifier.get_company_info(company_symbol)
        if not company_info:
            return None
        
        result = self.extractor.extract_financial_data_with_structure(company_info['cik'], year, company_symbol)
        if not result:
            return None
        
        raw_data = result['raw_data']
        pre_xml_structure = result['pre_xml_structure']
        
        balance_sheet = self.build_balance_sheet_with_structure(raw_data, pre_xml_structure)
        income_statement = self.build_income_statement_with_structure(raw_data, pre_xml_structure)
        cash_flow_statement = self.build_cash_flow_statement_with_structure(raw_data, pre_xml_structure)
        
        # Calculate data quality score
        data_quality_score = self._calculate_data_quality_score(raw_data)
        
        # Validate data
        validation_errors = self._validate_financial_data(balance_sheet, income_statement)
        
        return FinancialStatements(
            company_name=company_info['name'],
            cik=company_info['cik'],
            fiscal_year=year,
            filing_date=raw_data.get('Assets', {}).get('end_date', ''),
            balance_sheet=balance_sheet.__dict__,
            income_statement=income_statement.__dict__,
            cash_flow_statement=cash_flow_statement.__dict__,
            data_quality_score=data_quality_score,
            validation_errors=validation_errors
        )
    
    def _calculate_data_quality_score(self, raw_data: Dict[str, Any]) -> float:
        """Calculate data quality score based on completeness"""
        essential_metrics = [
            'Assets', 'Liabilities', 'StockholdersEquity',
            'RevenueFromContractWithCustomerExcludingAssessedTax', 'NetIncomeLoss'
        ]
        
        available_metrics = sum(1 for metric in essential_metrics if metric in raw_data)
        return available_metrics / len(essential_metrics)
    
    def _validate_financial_data(self, balance_sheet: BalanceSheet, income_statement: IncomeStatement) -> List[str]:
        """Validate financial data for consistency"""
        errors = []
        
        # Check balance sheet equation
        calculated_assets = balance_sheet.total_liabilities + balance_sheet.total_equity
        if abs(balance_sheet.total_assets - calculated_assets) > 0.01 * balance_sheet.total_assets:
            errors.append(f"Balance sheet doesn't balance: Assets={balance_sheet.total_assets}, Liabilities+Equity={calculated_assets}")
        
        # Check gross profit calculation
        calculated_gross_profit = income_statement.revenue - income_statement.cost_of_goods_sold
        if abs(income_statement.gross_profit - calculated_gross_profit) > 0.01 * abs(income_statement.gross_profit):
            errors.append(f"Gross profit calculation mismatch: Reported={income_statement.gross_profit}, Calculated={calculated_gross_profit}")
        
        return errors


class FinancialStatementsService:
    """Main service class for financial statements"""
    
    def __init__(self):
        self.builder = FinancialStatementBuilder()
    
    def get_financial_statements(self, company_symbol: str, year: int) -> Optional[FinancialStatements]:
        """Get complete financial statements for a company and year"""
        return self.builder.build_financial_statements(company_symbol, year)
    
    def get_balance_sheet(self, company_symbol: str, year: int) -> Optional[Dict[str, Any]]:
        """Get balance sheet only"""
        statements = self.get_financial_statements(company_symbol, year)
        return statements.balance_sheet if statements else None
    
    def get_income_statement(self, company_symbol: str, year: int) -> Optional[Dict[str, Any]]:
        """Get income statement only"""
        statements = self.get_financial_statements(company_symbol, year)
        return statements.income_statement if statements else None
    
    def get_cash_flow_statement(self, company_symbol: str, year: int) -> Optional[Dict[str, Any]]:
        """Get cash flow statement only"""
        statements = self.get_financial_statements(company_symbol, year)
        return statements.cash_flow_statement if statements else None
    
    def get_supported_companies(self) -> List[str]:
        """Get list of supported company symbols"""
        return CompanyIdentifier.get_supported_companies()
    
    def get_company_info(self, company_symbol: str) -> Optional[Dict[str, str]]:
        """Get company information"""
        return CompanyIdentifier.get_company_info(company_symbol)