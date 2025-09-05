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
        
        for filing_dir in filing_dirs:
            # Try to match the filing date
            if filing_date in filing_dir.name:
                target_dir = filing_dir
                break
        
        if not target_dir:
            # Use the most recent filing
            filing_dirs.sort(key=lambda x: x.name, reverse=True)
            if filing_dirs:
                target_dir = filing_dirs[0]
            else:
                return {}
        
        # Look for the main XBRL file
        xbrl_files = list(target_dir.glob(f"{company_symbol.lower()}-*.xml"))
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
            # Define GAAP metrics to extract
            gaap_metrics = [
                'Assets', 'Liabilities', 'StockholdersEquity', 
                'AssetsCurrent', 'LiabilitiesCurrent', 'AssetsNoncurrent', 'LiabilitiesNoncurrent',
                'CashAndCashEquivalentsAtCarryingValue', 'MarketableSecuritiesCurrent',
                'AccountsReceivableNetCurrent', 'InventoryNet',
                'PropertyPlantAndEquipmentNet', 'OtherAssetsCurrent', 'OtherAssetsNoncurrent',
                'AccountsPayableCurrent', 'OtherLiabilitiesCurrent', 'ContractWithCustomerLiabilityCurrent',
                'CommercialPaper', 'LongTermDebtCurrent', 'LongTermDebtNoncurrent', 'OtherLiabilitiesNoncurrent',
                'CommonStocksIncludingAdditionalPaidInCapital', 'RetainedEarningsAccumulatedDeficit',
                'AccumulatedOtherComprehensiveIncomeLossNetOfTax',
                'RevenueFromContractWithCustomerExcludingAssessedTax', 'CostOfGoodsAndServicesSold',
                'GrossProfit', 'ResearchAndDevelopmentExpense', 'SellingGeneralAndAdministrativeExpense',
                'OperatingIncomeLoss', 'NetIncomeLoss',
                'EarningsPerShareBasic', 'EarningsPerShareDiluted',
                'OperatingExpenses', 'MarketableSecuritiesNoncurrent'
            ]
            
            metrics_str = "', '".join(gaap_metrics)
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
            AND ft.tag_name IN ('{metrics_str}')
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
            
            # Define metric categories
            balance_sheet_metrics = {
                'Assets', 'Liabilities', 'StockholdersEquity',
                'AssetsCurrent', 'LiabilitiesCurrent', 'AssetsNoncurrent', 'LiabilitiesNoncurrent',
                'CashAndCashEquivalentsAtCarryingValue', 'MarketableSecuritiesCurrent',
                'AccountsReceivableNetCurrent', 'InventoryNet',
                'PropertyPlantAndEquipmentNet', 'OtherAssetsCurrent', 'OtherAssetsNoncurrent',
                'AccountsPayableCurrent', 'OtherLiabilitiesCurrent', 'ContractWithCustomerLiabilityCurrent',
                'CommercialPaper', 'LongTermDebtCurrent', 'LongTermDebtNoncurrent', 'OtherLiabilitiesNoncurrent',
                'CommonStocksIncludingAdditionalPaidInCapital', 'RetainedEarningsAccumulatedDeficit',
                'AccumulatedOtherComprehensiveIncomeLossNetOfTax'
            }
            
            income_statement_metrics = {
                'RevenueFromContractWithCustomerExcludingAssessedTax', 'CostOfGoodsAndServicesSold',
                'GrossProfit', 'ResearchAndDevelopmentExpense', 'SellingGeneralAndAdministrativeExpense',
                'OperatingIncomeLoss', 'NetIncomeLoss', 'OperatingExpenses'
            }
            
            eps_metrics = {'EarningsPerShareBasic', 'EarningsPerShareDiluted'}
            
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
            
            # Select the best value for each metric using context analysis
            financial_data = {}
            for metric, data_list in metric_data.items():
                best_value = self._select_best_value_with_context_analysis(
                    metric, data_list, contexts, balance_sheet_metrics, 
                    income_statement_metrics, eps_metrics, fiscal_year
                )
                if best_value:
                    financial_data[metric] = best_value
            
            return financial_data
            
        except Exception as e:
            print(f"Error extracting data: {e}")
            return {}
        finally:
            self.disconnect()
    
    def _select_best_value_with_context_analysis(self, metric: str, data_list: List[Dict], 
                                               contexts: Dict, balance_sheet_metrics: set, 
                                               income_statement_metrics: set, eps_metrics: set, 
                                               fiscal_year: int) -> Optional[Dict]:
        """Select the best value using context analysis"""
        if not data_list:
            return None
        
        # Determine metric type
        if metric in balance_sheet_metrics:
            metric_type = 'balance_sheet'
        elif metric in income_statement_metrics:
            metric_type = 'income_statement'
        elif metric in eps_metrics:
            metric_type = 'eps'
        else:
            # Default: use the first value
            return data_list[0]
        
        # Find the best context for this metric type and year
        best_context_id = self.context_analyzer.find_best_context_for_metric(
            contexts, metric_type, fiscal_year
        )
        
        if best_context_id:
            # Look for data with the best context
            for data in data_list:
                if data['context_ref'] == best_context_id:
                    return data
        
        # Fallback: use context-based selection without XML analysis
        return self._select_best_value_fallback(metric, data_list, balance_sheet_metrics, 
                                                income_statement_metrics, eps_metrics)
    
    def _select_best_value_fallback(self, metric: str, data_list: List[Dict], balance_sheet_metrics: set, 
                                   income_statement_metrics: set, eps_metrics: set) -> Optional[Dict]:
        """Fallback method for selecting best value"""
        if not data_list:
            return None
        
        # Determine metric category
        if metric in balance_sheet_metrics:
            # For balance sheet: prefer instant contexts
            instant_data = [d for d in data_list if d['period_type'] == 'instant']
            if instant_data:
                return instant_data[0]
        
        elif metric in income_statement_metrics:
            # For income statement: prefer duration contexts
            duration_data = [d for d in data_list if d['period_type'] == 'duration']
            if duration_data:
                return duration_data[0]
        
        elif metric in eps_metrics:
            # For EPS: prefer instant contexts
            instant_data = [d for d in data_list if d['period_type'] == 'instant']
            if instant_data:
                return instant_data[0]
        
        # Default: return first value
        return data_list[0]


class FinancialStatementBuilder:
    """Builds structured financial statements from raw data"""
    
    def __init__(self):
        self.extractor = DataExtractor()
    
    def build_balance_sheet(self, raw_data: Dict[str, Any]) -> BalanceSheet:
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
    
    def build_income_statement(self, raw_data: Dict[str, Any]) -> IncomeStatement:
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
    
    def build_cash_flow_statement(self, raw_data: Dict[str, Any]) -> CashFlowStatement:
        """Build cash flow statement from raw data"""
        # Note: This is a simplified version - in practice, you'd need more specific cash flow metrics
        return CashFlowStatement(
            operating_activities=0,  # Placeholder
            investing_activities=0,   # Placeholder
            financing_activities=0,  # Placeholder
            net_cash_flow=0           # Placeholder
        )
    
    def build_financial_statements(self, company_symbol: str, year: int) -> Optional[FinancialStatements]:
        """Build complete financial statements"""
        company_info = CompanyIdentifier.get_company_info(company_symbol)
        if not company_info:
            return None
        
        raw_data = self.extractor.extract_financial_data(company_info['cik'], year, company_symbol)
        if not raw_data:
            return None
        
        balance_sheet = self.build_balance_sheet(raw_data)
        income_statement = self.build_income_statement(raw_data)
        cash_flow_statement = self.build_cash_flow_statement(raw_data)
        
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