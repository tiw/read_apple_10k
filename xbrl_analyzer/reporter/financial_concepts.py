"""
财务概念定义模块

定义10-K年报中的财务概念、报表结构和计算指标
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum


class ReportSection(Enum):
    """报表部分枚举"""
    INCOME_STATEMENT = "income_statement"
    BALANCE_SHEET = "balance_sheet"
    CASH_FLOW = "cash_flow"
    EQUITY = "equity"
    FOOTNOTES = "footnotes"


class MetricCategory(Enum):
    """指标类别枚举"""
    PROFITABILITY = "profitability"
    LIQUIDITY = "liquidity"
    LEVERAGE = "leverage"
    EFFICIENCY = "efficiency"
    MARKET = "market"
    CASH_FLOW = "cash_flow"


@dataclass
class FinancialConcept:
    """财务概念定义"""
    concept_name: str
    chinese_name: str
    english_name: str
    section: ReportSection
    unit: str
    description: str
    is_calculated: bool = False
    formula: Optional[str] = None
    dependencies: Optional[List[str]] = None


@dataclass
class CalculatedMetric:
    """计算指标定义"""
    metric_name: str
    chinese_name: str
    category: MetricCategory
    formula: str
    description: str
    dependencies: List[str]
    unit: str = "ratio"
    is_percentage: bool = False


class FinancialConcepts:
    """财务概念定义类"""
    
    # 损益表概念
    INCOME_STATEMENT_CONCEPTS = {
        'RevenueFromContractWithCustomerExcludingAssessedTax': FinancialConcept(
            concept_name='RevenueFromContractWithCustomerExcludingAssessedTax',
            chinese_name='营业收入',
            english_name='Revenue from Contract with Customer',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD',
            description='客户合同收入，不包括评估税'
        ),
        'CostOfGoodsAndServicesSold': FinancialConcept(
            concept_name='CostOfGoodsAndServicesSold',
            chinese_name='营业成本',
            english_name='Cost of Goods and Services Sold',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD',
            description='销售商品和服务的成本'
        ),
        'GrossProfit': FinancialConcept(
            concept_name='GrossProfit',
            chinese_name='毛利润',
            english_name='Gross Profit',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD',
            description='毛利润'
        ),
        'OperatingExpenses': FinancialConcept(
            concept_name='OperatingExpenses',
            chinese_name='营业费用',
            english_name='Operating Expenses',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD',
            description='营业费用'
        ),
        'ResearchAndDevelopmentExpense': FinancialConcept(
            concept_name='ResearchAndDevelopmentExpense',
            chinese_name='研发费用',
            english_name='Research and Development Expense',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD',
            description='研发费用'
        ),
        'GeneralAndAdministrativeExpense': FinancialConcept(
            concept_name='GeneralAndAdministrativeExpense',
            chinese_name='一般及行政费用',
            english_name='General and Administrative Expense',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD',
            description='一般及行政费用'
        ),
        'OperatingIncomeLoss': FinancialConcept(
            concept_name='OperatingIncomeLoss',
            chinese_name='营业利润',
            english_name='Operating Income (Loss)',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD',
            description='营业利润（亏损）'
        ),
        'NonoperatingIncomeExpense': FinancialConcept(
            concept_name='NonoperatingIncomeExpense',
            chinese_name='非营业收支',
            english_name='Nonoperating Income (Expense)',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD',
            description='非营业收支'
        ),
        'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest': FinancialConcept(
            concept_name='IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',
            chinese_name='税前持续经营利润',
            english_name='Income from Continuing Operations Before Income Taxes',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD',
            description='税前持续经营利润'
        ),
        'IncomeTaxExpenseBenefit': FinancialConcept(
            concept_name='IncomeTaxExpenseBenefit',
            chinese_name='所得税费用',
            english_name='Income Tax Expense (Benefit)',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD',
            description='所得税费用（收益）'
        ),
        'NetIncomeLoss': FinancialConcept(
            concept_name='NetIncomeLoss',
            chinese_name='净利润',
            english_name='Net Income (Loss)',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD',
            description='净利润（亏损）'
        ),
        'EarningsPerShareBasic': FinancialConcept(
            concept_name='EarningsPerShareBasic',
            chinese_name='基本每股收益',
            english_name='Earnings Per Share Basic',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD/shares',
            description='基本每股收益'
        ),
        'EarningsPerShareDiluted': FinancialConcept(
            concept_name='EarningsPerShareDiluted',
            chinese_name='稀释每股收益',
            english_name='Earnings Per Share Diluted',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD/shares',
            description='稀释每股收益'
        ),
        'WeightedAverageNumberOfSharesOutstandingBasic': FinancialConcept(
            concept_name='WeightedAverageNumberOfSharesOutstandingBasic',
            chinese_name='加权平均流通股数（基本）',
            english_name='Weighted Average Number of Shares Outstanding Basic',
            section=ReportSection.INCOME_STATEMENT,
            unit='shares',
            description='加权平均流通股数（基本）'
        ),
        'WeightedAverageNumberOfDilutedSharesOutstanding': FinancialConcept(
            concept_name='WeightedAverageNumberOfDilutedSharesOutstanding',
            chinese_name='加权平均流通股数（稀释）',
            english_name='Weighted Average Number of Diluted Shares Outstanding',
            section=ReportSection.INCOME_STATEMENT,
            unit='shares',
            description='加权平均流通股数（稀释）'
        ),
        'DepreciationDepletionAndAmortization': FinancialConcept(
            concept_name='DepreciationDepletionAndAmortization',
            chinese_name='折旧、耗损和摊销',
            english_name='Depreciation, Depletion and Amortization',
            section=ReportSection.INCOME_STATEMENT,
            unit='USD',
            description='折旧、耗损和摊销'
        )
    }
    
    # 资产负债表概念
    BALANCE_SHEET_CONCEPTS = {
        'Assets': FinancialConcept(
            concept_name='Assets',
            chinese_name='总资产',
            english_name='Total Assets',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='总资产'
        ),
        'AssetsCurrent': FinancialConcept(
            concept_name='AssetsCurrent',
            chinese_name='流动资产',
            english_name='Current Assets',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='流动资产'
        ),
        'CashAndCashEquivalentsAtCarryingValue': FinancialConcept(
            concept_name='CashAndCashEquivalentsAtCarryingValue',
            chinese_name='现金及现金等价物',
            english_name='Cash and Cash Equivalents',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='现金及现金等价物'
        ),
        'MarketableSecuritiesCurrent': FinancialConcept(
            concept_name='MarketableSecuritiesCurrent',
            chinese_name='流动有价证券',
            english_name='Marketable Securities Current',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='流动有价证券'
        ),
        'AccountsReceivableNetCurrent': FinancialConcept(
            concept_name='AccountsReceivableNetCurrent',
            chinese_name='应收账款净额',
            english_name='Accounts Receivable Net Current',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='应收账款净额'
        ),
        'InventoryNet': FinancialConcept(
            concept_name='InventoryNet',
            chinese_name='存货净额',
            english_name='Inventory Net',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='存货净额'
        ),
        'AssetsNoncurrent': FinancialConcept(
            concept_name='AssetsNoncurrent',
            chinese_name='非流动资产',
            english_name='Noncurrent Assets',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='非流动资产'
        ),
        'MarketableSecuritiesNoncurrent': FinancialConcept(
            concept_name='MarketableSecuritiesNoncurrent',
            chinese_name='非流动有价证券',
            english_name='Marketable Securities Noncurrent',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='非流动有价证券'
        ),
        'PropertyPlantAndEquipmentNet': FinancialConcept(
            concept_name='PropertyPlantAndEquipmentNet',
            chinese_name='固定资产净额',
            english_name='Property, Plant and Equipment Net',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='固定资产净额'
        ),
        'OtherAssetsNoncurrent': FinancialConcept(
            concept_name='OtherAssetsNoncurrent',
            chinese_name='其他非流动资产',
            english_name='Other Assets Noncurrent',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='其他非流动资产'
        ),
        'Liabilities': FinancialConcept(
            concept_name='Liabilities',
            chinese_name='总负债',
            english_name='Total Liabilities',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='总负债'
        ),
        'LiabilitiesCurrent': FinancialConcept(
            concept_name='LiabilitiesCurrent',
            chinese_name='流动负债',
            english_name='Current Liabilities',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='流动负债'
        ),
        'AccountsPayableCurrent': FinancialConcept(
            concept_name='AccountsPayableCurrent',
            chinese_name='应付账款',
            english_name='Accounts Payable Current',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='应付账款'
        ),
        'CommercialPaper': FinancialConcept(
            concept_name='CommercialPaper',
            chinese_name='商业票据',
            english_name='Commercial Paper',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='商业票据'
        ),
        'LongTermDebtCurrent': FinancialConcept(
            concept_name='LongTermDebtCurrent',
            chinese_name='一年内到期的长期债务',
            english_name='Long Term Debt Current',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='一年内到期的长期债务'
        ),
        'LiabilitiesNoncurrent': FinancialConcept(
            concept_name='LiabilitiesNoncurrent',
            chinese_name='非流动负债',
            english_name='Noncurrent Liabilities',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='非流动负债'
        ),
        'LongTermDebtNoncurrent': FinancialConcept(
            concept_name='LongTermDebtNoncurrent',
            chinese_name='长期债务',
            english_name='Long Term Debt Noncurrent',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='长期债务'
        ),
        'OtherLiabilitiesNoncurrent': FinancialConcept(
            concept_name='OtherLiabilitiesNoncurrent',
            chinese_name='其他非流动负债',
            english_name='Other Liabilities Noncurrent',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='其他非流动负债'
        ),
        'StockholdersEquity': FinancialConcept(
            concept_name='StockholdersEquity',
            chinese_name='股东权益',
            english_name='Stockholders Equity',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='股东权益'
        ),
        'CommonStockSharesIssued': FinancialConcept(
            concept_name='CommonStockSharesIssued',
            chinese_name='发行的普通股股数',
            english_name='Common Stock Shares Issued',
            section=ReportSection.BALANCE_SHEET,
            unit='shares',
            description='发行的普通股股数'
        ),
        'RetainedEarningsAccumulatedDeficit': FinancialConcept(
            concept_name='RetainedEarningsAccumulatedDeficit',
            chinese_name='留存收益',
            english_name='Retained Earnings (Accumulated Deficit)',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='留存收益（累计亏损）'
        ),
        'AccumulatedOtherComprehensiveIncomeLossNetOfTax': FinancialConcept(
            concept_name='AccumulatedOtherComprehensiveIncomeLossNetOfTax',
            chinese_name='其他综合收益累计额',
            english_name='Accumulated Other Comprehensive Income (Loss) Net of Tax',
            section=ReportSection.BALANCE_SHEET,
            unit='USD',
            description='其他综合收益累计额（税后）'
        )
    }
    
    # 现金流量表概念
    CASH_FLOW_CONCEPTS = {
        'NetCashProvidedByUsedInOperatingActivities': FinancialConcept(
            concept_name='NetCashProvidedByUsedInOperatingActivities',
            chinese_name='经营活动现金流',
            english_name='Net Cash Provided by (Used in) Operating Activities',
            section=ReportSection.CASH_FLOW,
            unit='USD',
            description='经营活动产生的现金流量净额'
        ),
        'PaymentsToAcquirePropertyPlantAndEquipment': FinancialConcept(
            concept_name='PaymentsToAcquirePropertyPlantAndEquipment',
            chinese_name='购买固定资产支出',
            english_name='Payments to Acquire Property, Plant and Equipment',
            section=ReportSection.CASH_FLOW,
            unit='USD',
            description='购买固定资产支出'
        ),
        'PaymentsOfDividends': FinancialConcept(
            concept_name='PaymentsOfDividends',
            chinese_name='支付股息',
            english_name='Payments of Dividends',
            section=ReportSection.CASH_FLOW,
            unit='USD',
            description='支付股息'
        ),
        'PaymentsForRepurchaseOfCommonStock': FinancialConcept(
            concept_name='PaymentsForRepurchaseOfCommonStock',
            chinese_name='回购股票支出',
            english_name='Payments for Repurchase of Common Stock',
            section=ReportSection.CASH_FLOW,
            unit='USD',
            description='回购股票支出'
        )
    }
    
    @classmethod
    def get_all_concepts(cls) -> Dict[str, FinancialConcept]:
        """获取所有财务概念"""
        all_concepts = {}
        all_concepts.update(cls.INCOME_STATEMENT_CONCEPTS)
        all_concepts.update(cls.BALANCE_SHEET_CONCEPTS)
        all_concepts.update(cls.CASH_FLOW_CONCEPTS)
        return all_concepts
    
    @classmethod
    def get_concepts_by_section(cls, section: ReportSection) -> Dict[str, FinancialConcept]:
        """按报表部分获取财务概念"""
        all_concepts = cls.get_all_concepts()
        return {k: v for k, v in all_concepts.items() if v.section == section}


class CalculatedMetrics:
    """计算指标定义类"""
    
    # 盈利能力指标
    PROFITABILITY_METRICS = {
        'gross_margin': CalculatedMetric(
            metric_name='gross_margin',
            chinese_name='毛利率',
            category=MetricCategory.PROFITABILITY,
            formula='GrossProfit / RevenueFromContractWithCustomerExcludingAssessedTax',
            description='毛利润占营业收入的比例',
            dependencies=['GrossProfit', 'RevenueFromContractWithCustomerExcludingAssessedTax'],
            unit='ratio',
            is_percentage=True
        ),
        'operating_margin': CalculatedMetric(
            metric_name='operating_margin',
            chinese_name='营业利润率',
            category=MetricCategory.PROFITABILITY,
            formula='OperatingIncomeLoss / RevenueFromContractWithCustomerExcludingAssessedTax',
            description='营业利润占营业收入的比例',
            dependencies=['OperatingIncomeLoss', 'RevenueFromContractWithCustomerExcludingAssessedTax'],
            unit='ratio',
            is_percentage=True
        ),
        'net_profit_margin': CalculatedMetric(
            metric_name='net_profit_margin',
            chinese_name='净利润率',
            category=MetricCategory.PROFITABILITY,
            formula='NetIncomeLoss / RevenueFromContractWithCustomerExcludingAssessedTax',
            description='净利润占营业收入的比例',
            dependencies=['NetIncomeLoss', 'RevenueFromContractWithCustomerExcludingAssessedTax'],
            unit='ratio',
            is_percentage=True
        ),
        'effective_tax_rate': CalculatedMetric(
            metric_name='effective_tax_rate',
            chinese_name='实际税率',
            category=MetricCategory.PROFITABILITY,
            formula='IncomeTaxExpenseBenefit / IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',
            description='实际所得税税率',
            dependencies=['IncomeTaxExpenseBenefit', 'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'],
            unit='ratio',
            is_percentage=True
        ),
        'return_on_assets': CalculatedMetric(
            metric_name='return_on_assets',
            chinese_name='总资产收益率',
            category=MetricCategory.PROFITABILITY,
            formula='NetIncomeLoss / Assets',
            description='净利润占平均总资产的比例',
            dependencies=['NetIncomeLoss', 'Assets'],
            unit='ratio',
            is_percentage=True
        ),
        'return_on_equity': CalculatedMetric(
            metric_name='return_on_equity',
            chinese_name='股东权益收益率',
            category=MetricCategory.PROFITABILITY,
            formula='NetIncomeLoss / StockholdersEquity',
            description='净利润占股东权益的比例',
            dependencies=['NetIncomeLoss', 'StockholdersEquity'],
            unit='ratio',
            is_percentage=True
        )
    }
    
    # 流动性指标
    LIQUIDITY_METRICS = {
        'current_ratio': CalculatedMetric(
            metric_name='current_ratio',
            chinese_name='流动比率',
            category=MetricCategory.LIQUIDITY,
            formula='AssetsCurrent / LiabilitiesCurrent',
            description='流动资产与流动负债的比率',
            dependencies=['AssetsCurrent', 'LiabilitiesCurrent'],
            unit='ratio',
            is_percentage=False
        ),
        'quick_ratio': CalculatedMetric(
            metric_name='quick_ratio',
            chinese_name='速动比率',
            category=MetricCategory.LIQUIDITY,
            formula='(CashAndCashEquivalentsAtCarryingValue + MarketableSecuritiesCurrent + AccountsReceivableNetCurrent) / LiabilitiesCurrent',
            description='速动资产与流动负债的比率',
            dependencies=['CashAndCashEquivalentsAtCarryingValue', 'MarketableSecuritiesCurrent', 'AccountsReceivableNetCurrent', 'LiabilitiesCurrent'],
            unit='ratio',
            is_percentage=False
        )
    }
    
    # 杠杆比率
    LEVERAGE_METRICS = {
        'debt_to_asset_ratio': CalculatedMetric(
            metric_name='debt_to_asset_ratio',
            chinese_name='资产负债率',
            category=MetricCategory.LEVERAGE,
            formula='Liabilities / Assets',
            description='总负债与总资产的比率',
            dependencies=['Liabilities', 'Assets'],
            unit='ratio',
            is_percentage=True
        ),
        'equity_ratio': CalculatedMetric(
            metric_name='equity_ratio',
            chinese_name='股东权益比率',
            category=MetricCategory.LEVERAGE,
            formula='StockholdersEquity / Assets',
            description='股东权益与总资产的比率',
            dependencies=['StockholdersEquity', 'Assets'],
            unit='ratio',
            is_percentage=True
        ),
        'debt_to_equity_ratio': CalculatedMetric(
            metric_name='debt_to_equity_ratio',
            chinese_name='债务权益比率',
            category=MetricCategory.LEVERAGE,
            formula='Liabilities / StockholdersEquity',
            description='总负债与股东权益的比率',
            dependencies=['Liabilities', 'StockholdersEquity'],
            unit='ratio',
            is_percentage=False
        )
    }
    
    # 效率指标
    EFFICIENCY_METRICS = {
        'asset_turnover': CalculatedMetric(
            metric_name='asset_turnover',
            chinese_name='资产周转率',
            category=MetricCategory.EFFICIENCY,
            formula='RevenueFromContractWithCustomerExcludingAssessedTax / Assets',
            description='营业收入与平均总资产的比率',
            dependencies=['RevenueFromContractWithCustomerExcludingAssessedTax', 'Assets'],
            unit='ratio',
            is_percentage=False
        ),
        'inventory_turnover': CalculatedMetric(
            metric_name='inventory_turnover',
            chinese_name='存货周转率',
            category=MetricCategory.EFFICIENCY,
            formula='CostOfGoodsAndServicesSold / InventoryNet',
            description='营业成本与平均存货的比率',
            dependencies=['CostOfGoodsAndServicesSold', 'InventoryNet'],
            unit='ratio',
            is_percentage=False
        )
    }
    
    # 现金流指标
    CASH_FLOW_METRICS = {
        'free_cash_flow': CalculatedMetric(
            metric_name='free_cash_flow',
            chinese_name='自由现金流',
            category=MetricCategory.CASH_FLOW,
            formula='NetCashProvidedByUsedInOperatingActivities - PaymentsToAcquirePropertyPlantAndEquipment',
            description='经营活动现金流减去资本支出',
            dependencies=['NetCashProvidedByUsedInOperatingActivities', 'PaymentsToAcquirePropertyPlantAndEquipment'],
            unit='USD',
            is_percentage=False
        ),
        'dividend_payout_ratio': CalculatedMetric(
            metric_name='dividend_payout_ratio',
            chinese_name='股息支付率',
            category=MetricCategory.CASH_FLOW,
            formula='PaymentsOfDividends / NetIncomeLoss',
            description='股息支付占净利润的比例',
            dependencies=['PaymentsOfDividends', 'NetIncomeLoss'],
            unit='ratio',
            is_percentage=True
        ),
        'share_buyback_ratio': CalculatedMetric(
            metric_name='share_buyback_ratio',
            chinese_name='股票回购比例',
            category=MetricCategory.CASH_FLOW,
            formula='PaymentsForRepurchaseOfCommonStock / NetIncomeLoss',
            description='股票回购支出占净利润的比例',
            dependencies=['PaymentsForRepurchaseOfCommonStock', 'NetIncomeLoss'],
            unit='ratio',
            is_percentage=True
        )
    }
    
    # 每股指标
    PER_SHARE_METRICS = {
        'sales_per_share': CalculatedMetric(
            metric_name='sales_per_share',
            chinese_name='每股销售额',
            category=MetricCategory.MARKET,
            formula='RevenueFromContractWithCustomerExcludingAssessedTax / WeightedAverageNumberOfDilutedSharesOutstanding',
            description='每股销售额',
            dependencies=['RevenueFromContractWithCustomerExcludingAssessedTax', 'WeightedAverageNumberOfDilutedSharesOutstanding'],
            unit='USD',
            is_percentage=False
        ),
        'cash_flow_per_share': CalculatedMetric(
            metric_name='cash_flow_per_share',
            chinese_name='每股现金流',
            category=MetricCategory.CASH_FLOW,
            formula='NetCashProvidedByUsedInOperatingActivities / WeightedAverageNumberOfDilutedSharesOutstanding',
            description='每股经营活动现金流',
            dependencies=['NetCashProvidedByUsedInOperatingActivities', 'WeightedAverageNumberOfDilutedSharesOutstanding'],
            unit='USD',
            is_percentage=False
        ),
        'book_value_per_share': CalculatedMetric(
            metric_name='book_value_per_share',
            chinese_name='每股账面价值',
            category=MetricCategory.MARKET,
            formula='StockholdersEquity / WeightedAverageNumberOfDilutedSharesOutstanding',
            description='每股账面价值',
            dependencies=['StockholdersEquity', 'WeightedAverageNumberOfDilutedSharesOutstanding'],
            unit='USD',
            is_percentage=False
        ),
        'capital_spending_per_share': CalculatedMetric(
            metric_name='capital_spending_per_share',
            chinese_name='每股资本支出',
            category=MetricCategory.CASH_FLOW,
            formula='PaymentsToAcquirePropertyPlantAndEquipment / WeightedAverageNumberOfDilutedSharesOutstanding',
            description='每股资本支出',
            dependencies=['PaymentsToAcquirePropertyPlantAndEquipment', 'WeightedAverageNumberOfDilutedSharesOutstanding'],
            unit='USD',
            is_percentage=False
        )
    }
    
    @classmethod
    def get_all_metrics(cls) -> Dict[str, CalculatedMetric]:
        """获取所有计算指标"""
        all_metrics = {}
        all_metrics.update(cls.PROFITABILITY_METRICS)
        all_metrics.update(cls.LIQUIDITY_METRICS)
        all_metrics.update(cls.LEVERAGE_METRICS)
        all_metrics.update(cls.EFFICIENCY_METRICS)
        all_metrics.update(cls.CASH_FLOW_METRICS)
        all_metrics.update(cls.PER_SHARE_METRICS)
        return all_metrics
    
    @classmethod
    def get_metrics_by_category(cls, category: MetricCategory) -> Dict[str, CalculatedMetric]:
        """按类别获取计算指标"""
        all_metrics = cls.get_all_metrics()
        return {k: v for k, v in all_metrics.items() if v.category == category}
