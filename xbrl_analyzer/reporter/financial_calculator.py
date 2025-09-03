"""
财务指标计算器模块

提供财务指标计算功能，包括盈利能力、流动性、杠杆比率等指标
"""

from typing import Dict, List, Optional, Any, Tuple
import logging
import math

try:
    import pandas as pd
except ImportError:
    pd = None

from .financial_concepts import (
    CalculatedMetrics, MetricCategory, CalculatedMetric,
    FinancialConcepts, FinancialConcept
)


class FinancialCalculator:
    """财务指标计算器类"""
    
    def __init__(self):
        """初始化财务计算器"""
        self.logger = logging.getLogger(__name__)
        self.calculated_metrics = CalculatedMetrics.get_all_metrics()
    
    def format_financial_number(self, value: float, unit: str = 'USD') -> str:
        """
        格式化财务数字
        
        Args:
            value: 数值
            unit: 单位
            
        Returns:
            格式化后的字符串
        """
        if value is None or math.isnan(value) or math.isinf(value):
            return "N/A"
        
        if unit == 'USD':
            if abs(value) >= 1e12:
                return f"${value/1e12:.2f}T"
            elif abs(value) >= 1e9:
                return f"${value/1e9:.2f}B"
            elif abs(value) >= 1e6:
                return f"${value/1e6:.2f}M"
            elif abs(value) >= 1e3:
                return f"${value/1e3:.2f}K"
            else:
                return f"${value:.2f}"
        elif unit == 'shares':
            if abs(value) >= 1e9:
                return f"{value/1e9:.2f}B shares"
            elif abs(value) >= 1e6:
                return f"{value/1e6:.2f}M shares"
            elif abs(value) >= 1e3:
                return f"{value/1e3:.2f}K shares"
            else:
                return f"{value:.0f} shares"
        elif unit == 'USD/shares':
            return f"${value:.2f}/share"
        elif unit == 'ratio':
            return f"{value:.4f}"
        else:
            return f"{value:.2f} {unit}"
    
    def safe_divide(self, numerator: float, denominator: float, default: float = 0.0) -> float:
        """
        安全除法，避免除零错误
        
        Args:
            numerator: 分子
            denominator: 分母
            default: 默认值
            
        Returns:
            除法结果
        """
        if denominator == 0 or denominator is None or math.isnan(denominator):
            return default
        if numerator is None or math.isnan(numerator):
            return default
        return numerator / denominator
    
    def calculate_metric(self, metric_name: str, financial_facts: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        计算单个财务指标
        
        Args:
            metric_name: 指标名称
            financial_facts: 财务事实数据
            
        Returns:
            计算结果字典
        """
        if metric_name not in self.calculated_metrics:
            self.logger.warning(f"未知的财务指标: {metric_name}")
            return None
        
        metric = self.calculated_metrics[metric_name]
        
        try:
            # 检查依赖项是否都存在
            missing_deps = []
            for dep in metric.dependencies:
                if dep not in financial_facts:
                    missing_deps.append(dep)
            
            if missing_deps:
                self.logger.warning(f"计算{metric_name}缺少依赖项: {missing_deps}")
                return {
                    'metric_name': metric_name,
                    'chinese_name': metric.chinese_name,
                    'value': None,
                    'formatted_value': "N/A",
                    'formula': metric.formula,
                    'description': metric.description,
                    'category': metric.category.value,
                    'unit': metric.unit,
                    'is_percentage': metric.is_percentage,
                    'missing_dependencies': missing_deps
                }
            
            # 根据指标名称计算具体值
            value = self._calculate_specific_metric(metric_name, financial_facts)
            
            # 格式化结果
            if value is not None and not math.isnan(value) and not math.isinf(value):
                if metric.is_percentage:
                    formatted_value = f"{value:.1%}"
                else:
                    formatted_value = self.format_financial_number(value, metric.unit)
            else:
                formatted_value = "N/A"
            
            return {
                'metric_name': metric_name,
                'chinese_name': metric.chinese_name,
                'value': value,
                'formatted_value': formatted_value,
                'formula': metric.formula,
                'description': metric.description,
                'category': metric.category.value,
                'unit': metric.unit,
                'is_percentage': metric.is_percentage,
                'missing_dependencies': []
            }
            
        except Exception as e:
            self.logger.error(f"计算{metric_name}时出错: {e}")
            return {
                'metric_name': metric_name,
                'chinese_name': metric.chinese_name,
                'value': None,
                'formatted_value': "N/A",
                'formula': metric.formula,
                'description': metric.description,
                'category': metric.category.value,
                'unit': metric.unit,
                'is_percentage': metric.is_percentage,
                'error': str(e)
            }
    
    def _calculate_specific_metric(self, metric_name: str, financial_facts: Dict[str, Any]) -> Optional[float]:
        """
        计算特定指标的具体值
        
        Args:
            metric_name: 指标名称
            financial_facts: 财务事实数据
            
        Returns:
            计算结果
        """
        # 提取数值
        def get_value(concept: str) -> float:
            if concept in financial_facts:
                return financial_facts[concept]['value']
            return None
        
        # 盈利能力指标
        if metric_name == 'gross_margin':
            gross_profit = get_value('GrossProfit')
            revenue = get_value('RevenueFromContractWithCustomerExcludingAssessedTax')
            return self.safe_divide(gross_profit, revenue)
        
        elif metric_name == 'operating_margin':
            operating_income = get_value('OperatingIncomeLoss')
            revenue = get_value('RevenueFromContractWithCustomerExcludingAssessedTax')
            return self.safe_divide(operating_income, revenue)
        
        elif metric_name == 'net_profit_margin':
            net_income = get_value('NetIncomeLoss')
            revenue = get_value('RevenueFromContractWithCustomerExcludingAssessedTax')
            return self.safe_divide(net_income, revenue)
        
        elif metric_name == 'effective_tax_rate':
            tax_expense = get_value('IncomeTaxExpenseBenefit')
            pre_tax_income = get_value('IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest')
            return self.safe_divide(tax_expense, pre_tax_income)
        
        elif metric_name == 'return_on_assets':
            net_income = get_value('NetIncomeLoss')
            assets = get_value('Assets')
            return self.safe_divide(net_income, assets)
        
        elif metric_name == 'return_on_equity':
            net_income = get_value('NetIncomeLoss')
            equity = get_value('StockholdersEquity')
            return self.safe_divide(net_income, equity)
        
        # 流动性指标
        elif metric_name == 'current_ratio':
            current_assets = get_value('AssetsCurrent')
            current_liabilities = get_value('LiabilitiesCurrent')
            return self.safe_divide(current_assets, current_liabilities)
        
        elif metric_name == 'quick_ratio':
            cash = get_value('CashAndCashEquivalentsAtCarryingValue')
            securities = get_value('MarketableSecuritiesCurrent')
            receivables = get_value('AccountsReceivableNetCurrent')
            current_liabilities = get_value('LiabilitiesCurrent')
            
            quick_assets = (cash or 0) + (securities or 0) + (receivables or 0)
            return self.safe_divide(quick_assets, current_liabilities)
        
        # 杠杆比率
        elif metric_name == 'debt_to_asset_ratio':
            liabilities = get_value('Liabilities')
            assets = get_value('Assets')
            return self.safe_divide(liabilities, assets)
        
        elif metric_name == 'equity_ratio':
            equity = get_value('StockholdersEquity')
            assets = get_value('Assets')
            return self.safe_divide(equity, assets)
        
        elif metric_name == 'debt_to_equity_ratio':
            liabilities = get_value('Liabilities')
            equity = get_value('StockholdersEquity')
            return self.safe_divide(liabilities, equity)
        
        # 效率指标
        elif metric_name == 'asset_turnover':
            revenue = get_value('RevenueFromContractWithCustomerExcludingAssessedTax')
            assets = get_value('Assets')
            return self.safe_divide(revenue, assets)
        
        elif metric_name == 'inventory_turnover':
            cogs = get_value('CostOfGoodsAndServicesSold')
            inventory = get_value('InventoryNet')
            return self.safe_divide(cogs, inventory)
        
        # 现金流指标
        elif metric_name == 'free_cash_flow':
            operating_cash_flow = get_value('NetCashProvidedByUsedInOperatingActivities')
            capex = get_value('PaymentsToAcquirePropertyPlantAndEquipment')
            if operating_cash_flow is not None and capex is not None:
                return operating_cash_flow - capex
            return None
        
        elif metric_name == 'dividend_payout_ratio':
            dividends = get_value('PaymentsOfDividends')
            net_income = get_value('NetIncomeLoss')
            return self.safe_divide(dividends, net_income)
        
        elif metric_name == 'share_buyback_ratio':
            buybacks = get_value('PaymentsForRepurchaseOfCommonStock')
            net_income = get_value('NetIncomeLoss')
            return self.safe_divide(buybacks, net_income)
        
        # 每股指标
        elif metric_name == 'sales_per_share':
            revenue = get_value('RevenueFromContractWithCustomerExcludingAssessedTax')
            shares = get_value('WeightedAverageNumberOfDilutedSharesOutstanding')
            return self.safe_divide(revenue, shares)
        
        elif metric_name == 'cash_flow_per_share':
            operating_cash_flow = get_value('NetCashProvidedByUsedInOperatingActivities')
            shares = get_value('WeightedAverageNumberOfDilutedSharesOutstanding')
            return self.safe_divide(operating_cash_flow, shares)
        
        elif metric_name == 'book_value_per_share':
            equity = get_value('StockholdersEquity')
            shares = get_value('WeightedAverageNumberOfDilutedSharesOutstanding')
            return self.safe_divide(equity, shares)
        
        elif metric_name == 'capital_spending_per_share':
            capex = get_value('PaymentsToAcquirePropertyPlantAndEquipment')
            shares = get_value('WeightedAverageNumberOfDilutedSharesOutstanding')
            return self.safe_divide(capex, shares)
        
        else:
            self.logger.warning(f"未实现的指标计算: {metric_name}")
            return None
    
    def calculate_all_metrics(self, financial_facts: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """
        计算所有财务指标
        
        Args:
            financial_facts: 财务事实数据
            
        Returns:
            所有计算结果字典
        """
        results = {}
        
        for metric_name in self.calculated_metrics.keys():
            result = self.calculate_metric(metric_name, financial_facts)
            if result:
                results[metric_name] = result
        
        self.logger.info(f"计算完成: {len(results)} 个财务指标")
        return results
    
    def calculate_metrics_by_category(self, financial_facts: Dict[str, Any], 
                                    category: MetricCategory) -> Dict[str, Dict[str, Any]]:
        """
        按类别计算财务指标
        
        Args:
            financial_facts: 财务事实数据
            category: 指标类别
            
        Returns:
            该类别的计算结果字典
        """
        category_metrics = CalculatedMetrics.get_metrics_by_category(category)
        results = {}
        
        for metric_name in category_metrics.keys():
            result = self.calculate_metric(metric_name, financial_facts)
            if result:
                results[metric_name] = result
        
        self.logger.info(f"计算{category.value}类别指标: {len(results)} 个")
        return results
    
    def calculate_ebitda(self, financial_facts: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        计算EBITDA
        
        Args:
            financial_facts: 财务事实数据
            
        Returns:
            EBITDA计算结果
        """
        try:
            operating_income = financial_facts.get('OperatingIncomeLoss', {}).get('value')
            depreciation = financial_facts.get('DepreciationDepletionAndAmortization', {}).get('value')
            
            if operating_income is not None and depreciation is not None:
                ebitda = operating_income + depreciation
                return {
                    'metric_name': 'ebitda',
                    'chinese_name': 'EBITDA',
                    'value': ebitda,
                    'formatted_value': self.format_financial_number(ebitda),
                    'formula': 'OperatingIncomeLoss + DepreciationDepletionAndAmortization',
                    'description': '息税折旧摊销前利润',
                    'category': 'profitability',
                    'unit': 'USD',
                    'is_percentage': False
                }
            else:
                return {
                    'metric_name': 'ebitda',
                    'chinese_name': 'EBITDA',
                    'value': None,
                    'formatted_value': "N/A",
                    'formula': 'OperatingIncomeLoss + DepreciationDepletionAndAmortization',
                    'description': '息税折旧摊销前利润',
                    'category': 'profitability',
                    'unit': 'USD',
                    'is_percentage': False,
                    'missing_dependencies': ['OperatingIncomeLoss', 'DepreciationDepletionAndAmortization']
                }
        except Exception as e:
            self.logger.error(f"计算EBITDA时出错: {e}")
            return None
    
    def calculate_rotc(self, financial_facts: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        计算总资本回报率 (ROTC)
        
        Args:
            financial_facts: 财务事实数据
            
        Returns:
            ROTC计算结果
        """
        try:
            net_income = financial_facts.get('NetIncomeLoss', {}).get('value')
            long_term_debt = financial_facts.get('LongTermDebtNoncurrent', {}).get('value')
            equity = financial_facts.get('StockholdersEquity', {}).get('value')
            tax_expense = financial_facts.get('IncomeTaxExpenseBenefit', {}).get('value')
            pre_tax_income = financial_facts.get('IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest', {}).get('value')
            
            if all(v is not None for v in [net_income, long_term_debt, equity, tax_expense, pre_tax_income]):
                # 计算实际税率
                effective_tax_rate = self.safe_divide(tax_expense, pre_tax_income)
                
                # 估算利息费用 = 长期债务 × 4% × (1-实际税率)
                estimated_interest_expense = long_term_debt * 0.04 * (1 - effective_tax_rate)
                
                # 计算ROTC
                numerator = net_income + estimated_interest_expense
                denominator = long_term_debt + equity
                rotc = self.safe_divide(numerator, denominator)
                
                return {
                    'metric_name': 'rotc',
                    'chinese_name': '总资本回报率',
                    'value': rotc,
                    'formatted_value': f"{rotc:.1%}" if rotc is not None else "N/A",
                    'formula': '(NetIncomeLoss + EstimatedInterestExpense) / (LongTermDebtNoncurrent + StockholdersEquity)',
                    'description': '总资本回报率',
                    'category': 'profitability',
                    'unit': 'ratio',
                    'is_percentage': True,
                    'estimated_interest_expense': estimated_interest_expense,
                    'effective_tax_rate': effective_tax_rate
                }
            else:
                missing = []
                if net_income is None: missing.append('NetIncomeLoss')
                if long_term_debt is None: missing.append('LongTermDebtNoncurrent')
                if equity is None: missing.append('StockholdersEquity')
                if tax_expense is None: missing.append('IncomeTaxExpenseBenefit')
                if pre_tax_income is None: missing.append('IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest')
                
                return {
                    'metric_name': 'rotc',
                    'chinese_name': '总资本回报率',
                    'value': None,
                    'formatted_value': "N/A",
                    'formula': '(NetIncomeLoss + EstimatedInterestExpense) / (LongTermDebtNoncurrent + StockholdersEquity)',
                    'description': '总资本回报率',
                    'category': 'profitability',
                    'unit': 'ratio',
                    'is_percentage': True,
                    'missing_dependencies': missing
                }
        except Exception as e:
            self.logger.error(f"计算ROTC时出错: {e}")
            return None
    
    def get_metric_summary(self, calculated_metrics: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        获取指标计算摘要
        
        Args:
            calculated_metrics: 计算出的指标
            
        Returns:
            摘要信息
        """
        total_metrics = len(calculated_metrics)
        successful_metrics = sum(1 for m in calculated_metrics.values() if m.get('value') is not None)
        failed_metrics = total_metrics - successful_metrics
        
        # 按类别统计
        category_stats = {}
        for metric in calculated_metrics.values():
            category = metric.get('category', 'unknown')
            if category not in category_stats:
                category_stats[category] = {'total': 0, 'successful': 0}
            category_stats[category]['total'] += 1
            if metric.get('value') is not None:
                category_stats[category]['successful'] += 1
        
        return {
            'total_metrics': total_metrics,
            'successful_metrics': successful_metrics,
            'failed_metrics': failed_metrics,
            'success_rate': successful_metrics / total_metrics if total_metrics > 0 else 0,
            'category_stats': category_stats
        }
