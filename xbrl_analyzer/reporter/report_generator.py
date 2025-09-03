"""
年报生成器主模块

提供完整的10-K年报生成功能
"""

import os
import json
import logging
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime

try:
    import pandas as pd
except ImportError:
    pd = None

from .duckdb_interface import DuckDBInterface
from .financial_calculator import FinancialCalculator
from .report_templates import ReportTemplates
from .financial_concepts import FinancialConcepts, ReportSection


class AnnualReportGenerator:
    """年报生成器主类"""
    
    def __init__(self, db_path: str = None, output_dir: str = "./reports"):
        """
        初始化年报生成器
        
        Args:
            db_path: DuckDB数据库路径
            output_dir: 报告输出目录
        """
        self.db_path = db_path
        self.output_dir = output_dir
        self.logger = logging.getLogger(__name__)
        
        # 初始化组件
        self.db_interface = DuckDBInterface(db_path)
        self.calculator = FinancialCalculator()
        self.templates = ReportTemplates()
        
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        
        # 获取财务概念定义（基于Apple 2024年10-K分析文档）
        self.concepts = self._get_comprehensive_financial_concepts()
        
        self.logger.info(f"年报生成器初始化完成，输出目录: {output_dir}")
    
    def _get_comprehensive_financial_concepts(self) -> Dict[str, Any]:
        """
        获取全面的财务概念定义（基于Apple 2024年10-K分析文档）
        
        Returns:
            财务概念定义字典
        """
        return {
            # 损益表概念 (Income Statement)
            'income_statement': {
                'RevenueFromContractWithCustomerExcludingAssessedTax': {
                    'chinese_name': '客户合同收入',
                    'description': '主要营业收入',
                    'category': 'income_statement',
                    'unit': 'USD'
                },
                'CostOfGoodsAndServicesSold': {
                    'chinese_name': '服务和商品成本',
                    'description': '营业成本',
                    'category': 'income_statement',
                    'unit': 'USD'
                },
                'GrossProfit': {
                    'chinese_name': '毛利润',
                    'description': '营业收入减去营业成本',
                    'category': 'income_statement',
                    'unit': 'USD'
                },
                'OperatingExpenses': {
                    'chinese_name': '营业费用',
                    'description': '总营业费用',
                    'category': 'income_statement',
                    'unit': 'USD'
                },
                'ResearchAndDevelopmentExpense': {
                    'chinese_name': '研发费用',
                    'description': '研发投入',
                    'category': 'income_statement',
                    'unit': 'USD'
                },
                'GeneralAndAdministrativeExpense': {
                    'chinese_name': '一般及行政费用',
                    'description': '管理费用',
                    'category': 'income_statement',
                    'unit': 'USD'
                },
                'OperatingIncomeLoss': {
                    'chinese_name': '营业利润',
                    'description': '营业利润/亏损',
                    'category': 'income_statement',
                    'unit': 'USD'
                },
                'NonoperatingIncomeExpense': {
                    'chinese_name': '非营业收支',
                    'description': '非经常性收支',
                    'category': 'income_statement',
                    'unit': 'USD'
                },
                'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest': {
                    'chinese_name': '税前持续经营利润',
                    'description': '税前利润',
                    'category': 'income_statement',
                    'unit': 'USD'
                },
                'IncomeTaxExpenseBenefit': {
                    'chinese_name': '所得税费用',
                    'description': '所得税费用/收益',
                    'category': 'income_statement',
                    'unit': 'USD'
                },
                'NetIncomeLoss': {
                    'chinese_name': '净利润',
                    'description': '净利润/亏损',
                    'category': 'income_statement',
                    'unit': 'USD'
                },
                'EarningsPerShareBasic': {
                    'chinese_name': '基本每股收益',
                    'description': '基本每股收益',
                    'category': 'income_statement',
                    'unit': 'USD/shares'
                },
                'EarningsPerShareDiluted': {
                    'chinese_name': '稀释每股收益',
                    'description': '稀释每股收益',
                    'category': 'income_statement',
                    'unit': 'USD/shares'
                },
                'WeightedAverageNumberOfSharesOutstandingBasic': {
                    'chinese_name': '加权平均流通股数（基本）',
                    'description': '基本股数',
                    'category': 'income_statement',
                    'unit': 'shares'
                },
                'WeightedAverageNumberOfDilutedSharesOutstanding': {
                    'chinese_name': '加权平均流通股数（稀释）',
                    'description': '稀释股数',
                    'category': 'income_statement',
                    'unit': 'shares'
                },
                'DepreciationDepletionAndAmortization': {
                    'chinese_name': '折旧、耗损和摊销',
                    'description': '折旧摊销费用',
                    'category': 'income_statement',
                    'unit': 'USD'
                }
            },
            
            # 资产负债表概念 (Balance Sheet)
            'balance_sheet': {
                'Assets': {
                    'chinese_name': '总资产',
                    'description': '总资产',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'AssetsCurrent': {
                    'chinese_name': '流动资产',
                    'description': '流动资产',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'CashAndCashEquivalentsAtCarryingValue': {
                    'chinese_name': '现金及现金等价物',
                    'description': '现金及等价物',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'MarketableSecuritiesCurrent': {
                    'chinese_name': '流动有价证券',
                    'description': '短期投资',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'AccountsReceivableNetCurrent': {
                    'chinese_name': '应收账款净额',
                    'description': '应收账款',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'InventoryNet': {
                    'chinese_name': '存货净额',
                    'description': '存货',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'AssetsNoncurrent': {
                    'chinese_name': '非流动资产',
                    'description': '非流动资产',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'MarketableSecuritiesNoncurrent': {
                    'chinese_name': '非流动有价证券',
                    'description': '长期投资',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'PropertyPlantAndEquipmentNet': {
                    'chinese_name': '固定资产净额',
                    'description': '固定资产',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'OtherAssetsNoncurrent': {
                    'chinese_name': '其他非流动资产',
                    'description': '其他长期资产',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'Liabilities': {
                    'chinese_name': '总负债',
                    'description': '总负债',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'LiabilitiesCurrent': {
                    'chinese_name': '流动负债',
                    'description': '流动负债',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'AccountsPayableCurrent': {
                    'chinese_name': '应付账款',
                    'description': '应付账款',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'CommercialPaper': {
                    'chinese_name': '商业票据',
                    'description': '短期借款',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'LongTermDebtCurrent': {
                    'chinese_name': '一年内到期的长期债务',
                    'description': '短期债务',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'LiabilitiesNoncurrent': {
                    'chinese_name': '非流动负债',
                    'description': '非流动负债',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'LongTermDebtNoncurrent': {
                    'chinese_name': '长期债务',
                    'description': '长期债务',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'OtherLiabilitiesNoncurrent': {
                    'chinese_name': '其他非流动负债',
                    'description': '其他长期负债',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'StockholdersEquity': {
                    'chinese_name': '股东权益',
                    'description': '股东权益',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'CommonStockSharesIssued': {
                    'chinese_name': '发行的普通股股数',
                    'description': '发行股数',
                    'category': 'balance_sheet',
                    'unit': 'shares'
                },
                'RetainedEarningsAccumulatedDeficit': {
                    'chinese_name': '留存收益',
                    'description': '留存收益/累计亏损',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                },
                'AccumulatedOtherComprehensiveIncomeLossNetOfTax': {
                    'chinese_name': '其他综合收益累计额',
                    'description': '其他综合收益',
                    'category': 'balance_sheet',
                    'unit': 'USD'
                }
            },
            
            # 现金流量表概念 (Cash Flow Statement)
            'cash_flow': {
                'NetCashProvidedByUsedInOperatingActivities': {
                    'chinese_name': '经营活动现金流',
                    'description': '经营现金流',
                    'category': 'cash_flow',
                    'unit': 'USD'
                },
                'PaymentsToAcquirePropertyPlantAndEquipment': {
                    'chinese_name': '购买固定资产支出',
                    'description': '资本支出',
                    'category': 'cash_flow',
                    'unit': 'USD'
                },
                'PaymentsOfDividends': {
                    'chinese_name': '支付股息',
                    'description': '股息支付',
                    'category': 'cash_flow',
                    'unit': 'USD'
                },
                'PaymentsForRepurchaseOfCommonStock': {
                    'chinese_name': '回购股票支出',
                    'description': '股票回购',
                    'category': 'cash_flow',
                    'unit': 'USD'
                }
            }
        }
    
    def generate_company_report(self, cik: str, fiscal_year: int = None, 
                              output_formats: List[str] = ['html', 'markdown', 'json']) -> Dict[str, Any]:
        """
        生成公司年报
        
        Args:
            cik: 公司CIK码
            fiscal_year: 财政年度，如果为None则使用最新年度
            output_formats: 输出格式列表
            
        Returns:
            生成结果字典
        """
        try:
            self.logger.info(f"开始生成公司年报: CIK={cik}, 财政年度={fiscal_year}")
            
            # 获取公司信息
            company_info = self.db_interface.get_company_info(cik=cik)
            if not company_info:
                raise ValueError(f"未找到CIK为{cik}的公司信息")
            
            # 获取财务事实数据
            financial_facts = self.db_interface.get_latest_financial_facts(cik, fiscal_year)
            if not financial_facts:
                raise ValueError(f"未找到CIK为{cik}的财务事实数据")
            
            # 确定实际使用的财政年度
            if fiscal_year is None:
                fiscal_year = max(fact.get('fiscal_year', 0) for fact in financial_facts.values())
            
            self.logger.info(f"使用财政年度: {fiscal_year}")
            
            # 计算所有财务指标（基于Apple 2024年10-K分析文档）
            calculated_metrics = self._calculate_comprehensive_metrics(financial_facts)
            
            # 生成报告
            results = {}
            
            for format_type in output_formats:
                if format_type == 'html':
                    html_content = self.templates.generate_html_report(
                        company_info, financial_facts, calculated_metrics, 
                        self.concepts, fiscal_year
                    )
                    html_file = self._save_html_report(html_content, company_info, fiscal_year)
                    results['html'] = html_file
                
                elif format_type == 'markdown':
                    markdown_content = self.templates.generate_markdown_report(
                        company_info, financial_facts, calculated_metrics,
                        self.concepts, fiscal_year
                    )
                    md_file = self._save_markdown_report(markdown_content, company_info, fiscal_year)
                    results['markdown'] = md_file
                
                elif format_type == 'json':
                    json_data = self._generate_json_report(
                        company_info, financial_facts, calculated_metrics, fiscal_year
                    )
                    json_file = self._save_json_report(json_data, company_info, fiscal_year)
                    results['json'] = json_file
            
            # 生成摘要信息
            summary = self._generate_summary(company_info, financial_facts, calculated_metrics, fiscal_year)
            results['summary'] = summary
            
            self.logger.info(f"公司年报生成完成: {company_info.get('ticker', cik)}")
            return results
            
        except Exception as e:
            self.logger.error(f"生成公司年报失败: {e}")
            raise
    
    def generate_ticker_report(self, ticker: str, fiscal_year: int = None,
                             output_formats: List[str] = ['html', 'markdown', 'json']) -> Dict[str, Any]:
        """
        根据股票代码生成年报
        
        Args:
            ticker: 股票代码
            fiscal_year: 财政年度
            output_formats: 输出格式列表
            
        Returns:
            生成结果字典
        """
        try:
            # 根据股票代码获取CIK
            company_info = self.db_interface.get_company_info(ticker=ticker)
            if not company_info:
                raise ValueError(f"未找到股票代码为{ticker}的公司信息")
            
            cik = company_info['cik']
            return self.generate_company_report(cik, fiscal_year, output_formats)
            
        except Exception as e:
            self.logger.error(f"根据股票代码生成年报失败: {e}")
            raise
    
    def generate_batch_reports(self, tickers: List[str], fiscal_year: int = None,
                             output_formats: List[str] = ['html', 'markdown']) -> Dict[str, Any]:
        """
        批量生成多个公司的年报
        
        Args:
            tickers: 股票代码列表
            fiscal_year: 财政年度
            output_formats: 输出格式列表
            
        Returns:
            批量生成结果字典
        """
        results = {}
        successful = 0
        failed = 0
        
        for ticker in tickers:
            try:
                self.logger.info(f"生成 {ticker} 的年报...")
                result = self.generate_ticker_report(ticker, fiscal_year, output_formats)
                results[ticker] = {
                    'status': 'success',
                    'result': result
                }
                successful += 1
                
            except Exception as e:
                self.logger.error(f"生成 {ticker} 年报失败: {e}")
                results[ticker] = {
                    'status': 'failed',
                    'error': str(e)
                }
                failed += 1
        
        # 生成批量报告摘要
        batch_summary = {
            'total_companies': len(tickers),
            'successful': successful,
            'failed': failed,
            'success_rate': successful / len(tickers) if tickers else 0,
            'generated_at': datetime.now().isoformat()
        }
        
        self.logger.info(f"批量生成完成: {successful}/{len(tickers)} 成功")
        return {
            'summary': batch_summary,
            'results': results
        }
    
    def _save_html_report(self, html_content: str, company_info: Dict[str, Any], 
                         fiscal_year: int) -> str:
        """保存HTML报告"""
        filename = f"{company_info.get('ticker', 'UNKNOWN')}_{fiscal_year}_annual_report.html"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        self.logger.info(f"HTML报告已保存: {filepath}")
        return filepath
    
    def _save_markdown_report(self, markdown_content: str, company_info: Dict[str, Any],
                             fiscal_year: int) -> str:
        """保存Markdown报告"""
        filename = f"{company_info.get('ticker', 'UNKNOWN')}_{fiscal_year}_annual_report.md"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        self.logger.info(f"Markdown报告已保存: {filepath}")
        return filepath
    
    def _save_json_report(self, json_data: Dict[str, Any], company_info: Dict[str, Any],
                         fiscal_year: int) -> str:
        """保存JSON报告"""
        filename = f"{company_info.get('ticker', 'UNKNOWN')}_{fiscal_year}_annual_report.json"
        filepath = os.path.join(self.output_dir, filename)
        
        # 转换Decimal和date为可序列化类型
        def convert_decimal(obj):
            if hasattr(obj, '__iter__') and not isinstance(obj, str):
                if isinstance(obj, dict):
                    return {k: convert_decimal(v) for k, v in obj.items()}
                else:
                    return [convert_decimal(item) for item in obj]
            elif hasattr(obj, 'to_eng_string'):  # Decimal对象
                return float(obj)
            elif hasattr(obj, 'isoformat'):  # date/datetime对象
                return obj.isoformat()
            else:
                return obj
        
        json_data_converted = convert_decimal(json_data)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(json_data_converted, f, ensure_ascii=False, indent=2)
        
        self.logger.info(f"JSON报告已保存: {filepath}")
        return filepath
    
    def _generate_json_report(self, company_info: Dict[str, Any],
                            financial_facts: Dict[str, Any],
                            calculated_metrics: Dict[str, Any],
                            fiscal_year: int) -> Dict[str, Any]:
        """生成JSON格式报告"""
        return {
            'report_info': {
                'company': company_info,
                'fiscal_year': fiscal_year,
                'generated_at': datetime.now().isoformat(),
                'data_source': 'SEC EDGAR API'
            },
            'financial_facts': financial_facts,
            'calculated_metrics': calculated_metrics,
            'summary': self._generate_summary(company_info, financial_facts, calculated_metrics, fiscal_year)
        }
    
    def _calculate_comprehensive_metrics(self, financial_facts: Dict[str, Any]) -> Dict[str, Any]:
        """
        计算全面的财务指标（基于Apple 2024年10-K分析文档）
        
        Args:
            financial_facts: 财务事实数据
            
        Returns:
            计算指标字典
        """
        # 转换所有数值为float以避免Decimal运算问题
        for concept, data in financial_facts.items():
            if 'value' in data and data['value'] is not None:
                try:
                    data['value'] = float(data['value'])
                except (ValueError, TypeError):
                    pass
        
        metrics = {}
        
        # 1. 盈利能力指标 (Profitability Ratios)
        metrics.update(self._calculate_profitability_metrics(financial_facts))
        
        # 2. 流动性指标 (Liquidity Ratios)
        metrics.update(self._calculate_liquidity_metrics(financial_facts))
        
        # 3. 杠杆比率 (Leverage Ratios)
        metrics.update(self._calculate_leverage_metrics(financial_facts))
        
        # 4. 现金流指标 (Cash Flow Metrics)
        metrics.update(self._calculate_cash_flow_metrics(financial_facts))
        
        # 5. 回报率指标 (Return Metrics)
        metrics.update(self._calculate_return_metrics(financial_facts))
        
        # 6. 每股指标 (Per-Share Metrics)
        metrics.update(self._calculate_per_share_metrics(financial_facts))
        
        return metrics
    
    def _calculate_profitability_metrics(self, financial_facts: Dict[str, Any]) -> Dict[str, Any]:
        """计算盈利能力指标"""
        metrics = {}
        
        # 毛利率
        if 'GrossProfit' in financial_facts and 'RevenueFromContractWithCustomerExcludingAssessedTax' in financial_facts:
            gross_profit = float(financial_facts['GrossProfit']['value'])
            revenue = float(financial_facts['RevenueFromContractWithCustomerExcludingAssessedTax']['value'])
            if revenue != 0:
                margin = gross_profit / revenue
                metrics['gross_margin'] = {
                    'value': margin,
                    'formatted_value': f"{margin:.1%}",
                    'formula': 'GrossProfit / RevenueFromContractWithCustomerExcludingAssessedTax',
                    'category': 'profitability',
                    'chinese_name': '毛利率'
                }
        
        # EBITDA
        if 'OperatingIncomeLoss' in financial_facts and 'DepreciationDepletionAndAmortization' in financial_facts:
            operating_income = financial_facts['OperatingIncomeLoss']['value']
            depreciation = financial_facts['DepreciationDepletionAndAmortization']['value']
            ebitda = operating_income + depreciation
            metrics['ebitda'] = {
                'value': ebitda,
                'formatted_value': f"{ebitda:,.0f}",
                'formula': 'OperatingIncomeLoss + DepreciationDepletionAndAmortization',
                'category': 'profitability',
                'chinese_name': 'EBITDA'
            }
            
            # 营业利润率（基于EBITDA）
            if 'RevenueFromContractWithCustomerExcludingAssessedTax' in financial_facts:
                revenue = financial_facts['RevenueFromContractWithCustomerExcludingAssessedTax']['value']
                if revenue != 0:
                    metrics['operating_margin'] = {
                        'value': ebitda / revenue,
                        'formatted_value': f"{(ebitda / revenue):.1%}",
                        'formula': 'EBITDA / RevenueFromContractWithCustomerExcludingAssessedTax',
                        'category': 'profitability',
                        'chinese_name': '营业利润率'
                    }
        
        # 净利润率
        if 'NetIncomeLoss' in financial_facts and 'RevenueFromContractWithCustomerExcludingAssessedTax' in financial_facts:
            net_income = financial_facts['NetIncomeLoss']['value']
            revenue = financial_facts['RevenueFromContractWithCustomerExcludingAssessedTax']['value']
            if revenue != 0:
                metrics['net_profit_margin'] = {
                    'value': net_income / revenue,
                    'formatted_value': f"{(net_income / revenue):.1%}",
                    'formula': 'NetIncomeLoss / RevenueFromContractWithCustomerExcludingAssessedTax',
                    'category': 'profitability',
                    'chinese_name': '净利润率'
                }
        
        # 实际税率
        if ('IncomeTaxExpenseBenefit' in financial_facts and 
            'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest' in financial_facts):
            tax_expense = financial_facts['IncomeTaxExpenseBenefit']['value']
            pre_tax_income = financial_facts['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest']['value']
            if pre_tax_income != 0:
                metrics['effective_tax_rate'] = {
                    'value': tax_expense / pre_tax_income,
                    'formatted_value': f"{(tax_expense / pre_tax_income):.1%}",
                    'formula': 'IncomeTaxExpenseBenefit / IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',
                    'category': 'profitability',
                    'chinese_name': '实际税率'
                }
        
        # 每股收益
        if 'EarningsPerShareBasic' in financial_facts:
            metrics['basic_eps'] = {
                'value': financial_facts['EarningsPerShareBasic']['value'],
                'formatted_value': f"{financial_facts['EarningsPerShareBasic']['value']:.2f}",
                'formula': 'EarningsPerShareBasic',
                'category': 'profitability',
                'chinese_name': '基本每股收益'
            }
        
        if 'EarningsPerShareDiluted' in financial_facts:
            metrics['diluted_eps'] = {
                'value': financial_facts['EarningsPerShareDiluted']['value'],
                'formatted_value': f"{financial_facts['EarningsPerShareDiluted']['value']:.2f}",
                'formula': 'EarningsPerShareDiluted',
                'category': 'profitability',
                'chinese_name': '稀释每股收益'
            }
        
        return metrics
    
    def _calculate_liquidity_metrics(self, financial_facts: Dict[str, Any]) -> Dict[str, Any]:
        """计算流动性指标"""
        metrics = {}
        
        # 流动比率
        if 'AssetsCurrent' in financial_facts and 'LiabilitiesCurrent' in financial_facts:
            current_assets = financial_facts['AssetsCurrent']['value']
            current_liabilities = financial_facts['LiabilitiesCurrent']['value']
            if current_liabilities != 0:
                metrics['current_ratio'] = {
                    'value': current_assets / current_liabilities,
                    'formatted_value': f"{(current_assets / current_liabilities):.2f}",
                    'formula': 'AssetsCurrent / LiabilitiesCurrent',
                    'category': 'liquidity',
                    'chinese_name': '流动比率'
                }
        
        # 速动比率
        if (all(k in financial_facts for k in ['CashAndCashEquivalentsAtCarryingValue', 
                                               'MarketableSecuritiesCurrent', 
                                               'AccountsReceivableNetCurrent', 
                                               'LiabilitiesCurrent'])):
            cash = financial_facts['CashAndCashEquivalentsAtCarryingValue']['value']
            securities = financial_facts['MarketableSecuritiesCurrent']['value']
            receivables = financial_facts['AccountsReceivableNetCurrent']['value']
            current_liabilities = financial_facts['LiabilitiesCurrent']['value']
            
            quick_assets = cash + securities + receivables
            if current_liabilities != 0:
                metrics['quick_ratio'] = {
                    'value': quick_assets / current_liabilities,
                    'formatted_value': f"{(quick_assets / current_liabilities):.2f}",
                    'formula': '(CashAndCashEquivalentsAtCarryingValue + MarketableSecuritiesCurrent + AccountsReceivableNetCurrent) / LiabilitiesCurrent',
                    'category': 'liquidity',
                    'chinese_name': '速动比率'
                }
        
        return metrics
    
    def _calculate_leverage_metrics(self, financial_facts: Dict[str, Any]) -> Dict[str, Any]:
        """计算杠杆比率"""
        metrics = {}
        
        # 资产负债率
        if 'Liabilities' in financial_facts and 'Assets' in financial_facts:
            liabilities = financial_facts['Liabilities']['value']
            assets = financial_facts['Assets']['value']
            if assets != 0:
                metrics['debt_to_asset_ratio'] = {
                    'value': liabilities / assets,
                    'formatted_value': f"{(liabilities / assets):.1%}",
                    'formula': 'Liabilities / Assets',
                    'category': 'leverage',
                    'chinese_name': '资产负债率'
                }
        
        # 股东权益比率
        if 'StockholdersEquity' in financial_facts and 'Assets' in financial_facts:
            equity = financial_facts['StockholdersEquity']['value']
            assets = financial_facts['Assets']['value']
            if assets != 0:
                metrics['equity_ratio'] = {
                    'value': equity / assets,
                    'formatted_value': f"{(equity / assets):.1%}",
                    'formula': 'StockholdersEquity / Assets',
                    'category': 'leverage',
                    'chinese_name': '股东权益比率'
                }
        
        return metrics
    
    def _calculate_cash_flow_metrics(self, financial_facts: Dict[str, Any]) -> Dict[str, Any]:
        """计算现金流指标"""
        metrics = {}
        
        # 自由现金流
        if ('NetCashProvidedByUsedInOperatingActivities' in financial_facts and 
            'PaymentsToAcquirePropertyPlantAndEquipment' in financial_facts):
            operating_cash_flow = financial_facts['NetCashProvidedByUsedInOperatingActivities']['value']
            capex = financial_facts['PaymentsToAcquirePropertyPlantAndEquipment']['value']
            free_cash_flow = operating_cash_flow - capex
            
            metrics['free_cash_flow'] = {
                'value': free_cash_flow,
                'formatted_value': f"{free_cash_flow:,.0f}",
                'formula': 'NetCashProvidedByUsedInOperatingActivities - PaymentsToAcquirePropertyPlantAndEquipment',
                'category': 'cash_flow',
                'chinese_name': '自由现金流'
            }
            
            # Value Line自由现金流
            value_line_fcf = operating_cash_flow + capex
            metrics['value_line_free_cash_flow'] = {
                'value': value_line_fcf,
                'formatted_value': f"{value_line_fcf:,.0f}",
                'formula': 'NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment',
                'category': 'cash_flow',
                'chinese_name': 'Value Line自由现金流'
            }
        
        # 股息支付率
        if 'PaymentsOfDividends' in financial_facts and 'NetIncomeLoss' in financial_facts:
            dividends = financial_facts['PaymentsOfDividends']['value']
            net_income = financial_facts['NetIncomeLoss']['value']
            if net_income != 0:
                metrics['dividend_payout_ratio'] = {
                    'value': dividends / net_income,
                    'formatted_value': f"{(dividends / net_income):.1%}",
                    'formula': 'PaymentsOfDividends / NetIncomeLoss',
                    'category': 'cash_flow',
                    'chinese_name': '股息支付率'
                }
        
        # 股票回购比例
        if 'PaymentsForRepurchaseOfCommonStock' in financial_facts and 'NetIncomeLoss' in financial_facts:
            buybacks = financial_facts['PaymentsForRepurchaseOfCommonStock']['value']
            net_income = financial_facts['NetIncomeLoss']['value']
            if net_income != 0:
                metrics['share_buyback_ratio'] = {
                    'value': buybacks / net_income,
                    'formatted_value': f"{(buybacks / net_income):.1%}",
                    'formula': 'PaymentsForRepurchaseOfCommonStock / NetIncomeLoss',
                    'category': 'cash_flow',
                    'chinese_name': '股票回购比例'
                }
        
        return metrics
    
    def _calculate_return_metrics(self, financial_facts: Dict[str, Any]) -> Dict[str, Any]:
        """计算回报率指标"""
        metrics = {}
        
        # 净资产收益率 (ROE)
        if 'NetIncomeLoss' in financial_facts and 'StockholdersEquity' in financial_facts:
            net_income = financial_facts['NetIncomeLoss']['value']
            equity = financial_facts['StockholdersEquity']['value']
            if equity != 0:
                metrics['roe'] = {
                    'value': net_income / equity,
                    'formatted_value': f"{(net_income / equity):.1%}",
                    'formula': 'NetIncomeLoss / StockholdersEquity',
                    'category': 'return',
                    'chinese_name': '净资产收益率 (ROE)'
                }
        
        # 总资产收益率 (ROA)
        if 'NetIncomeLoss' in financial_facts and 'Assets' in financial_facts:
            net_income = financial_facts['NetIncomeLoss']['value']
            assets = financial_facts['Assets']['value']
            if assets != 0:
                metrics['roa'] = {
                    'value': net_income / assets,
                    'formatted_value': f"{(net_income / assets):.1%}",
                    'formula': 'NetIncomeLoss / Assets',
                    'category': 'return',
                    'chinese_name': '总资产收益率 (ROA)'
                }
        
        # 总资本回报率 (ROTC)
        if (all(k in financial_facts for k in ['NetIncomeLoss', 'LongTermDebtNoncurrent', 
                                               'StockholdersEquity', 'IncomeTaxExpenseBenefit',
                                               'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'])):
            net_income = financial_facts['NetIncomeLoss']['value']
            long_term_debt = financial_facts['LongTermDebtNoncurrent']['value']
            equity = financial_facts['StockholdersEquity']['value']
            tax_expense = financial_facts['IncomeTaxExpenseBenefit']['value']
            pre_tax_income = financial_facts['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest']['value']
            
            if pre_tax_income != 0:
                effective_tax_rate = float(tax_expense) / float(pre_tax_income)
                estimated_interest_expense = float(long_term_debt) * 0.04 * (1 - effective_tax_rate)
                total_capital = float(long_term_debt) + float(equity)
                
                if total_capital != 0:
                    rotc = (net_income + estimated_interest_expense) / total_capital
                    metrics['rotc'] = {
                        'value': rotc,
                        'formatted_value': f"{rotc:.1%}",
                        'formula': '(NetIncomeLoss + EstimatedInterestExpense) / (LongTermDebtNoncurrent + StockholdersEquity)',
                        'category': 'return',
                        'chinese_name': '总资本回报率 (ROTC)',
                        'note': f'EstimatedInterestExpense = LongTermDebtNoncurrent × 4% × (1-{effective_tax_rate:.1%})'
                    }
        
        # 留存收益比率
        if ('NetIncomeLoss' in financial_facts and 'PaymentsOfDividends' in financial_facts and 
            'StockholdersEquity' in financial_facts):
            net_income = financial_facts['NetIncomeLoss']['value']
            dividends = financial_facts['PaymentsOfDividends']['value']
            equity = financial_facts['StockholdersEquity']['value']
            
            retained_earnings = net_income - dividends
            if equity != 0:
                metrics['retained_earnings_ratio'] = {
                    'value': retained_earnings / equity,
                    'formatted_value': f"{(retained_earnings / equity):.1%}",
                    'formula': '(NetIncomeLoss - PaymentsOfDividends) / StockholdersEquity',
                    'category': 'return',
                    'chinese_name': '留存收益比率'
                }
        
        return metrics
    
    def _calculate_per_share_metrics(self, financial_facts: Dict[str, Any]) -> Dict[str, Any]:
        """计算每股指标"""
        metrics = {}
        
        # 每股销售额
        if 'RevenueFromContractWithCustomerExcludingAssessedTax' in financial_facts:
            revenue = financial_facts['RevenueFromContractWithCustomerExcludingAssessedTax']['value']
            
            # 使用稀释股数
            if 'WeightedAverageNumberOfDilutedSharesOutstanding' in financial_facts:
                diluted_shares = financial_facts['WeightedAverageNumberOfDilutedSharesOutstanding']['value']
                if diluted_shares != 0:
                    metrics['sales_per_share'] = {
                        'value': revenue / diluted_shares,
                        'formatted_value': f"{(revenue / diluted_shares):.2f}",
                        'formula': 'RevenueFromContractWithCustomerExcludingAssessedTax / WeightedAverageNumberOfDilutedSharesOutstanding',
                        'category': 'per_share',
                        'chinese_name': '每股销售额'
                    }
            
            # 使用发行股数
            if 'CommonStockSharesIssued' in financial_facts:
                issued_shares = financial_facts['CommonStockSharesIssued']['value']
                if issued_shares != 0:
                    metrics['sales_per_share_issued'] = {
                        'value': revenue / issued_shares,
                        'formatted_value': f"{(revenue / issued_shares):.2f}",
                        'formula': 'RevenueFromContractWithCustomerExcludingAssessedTax / CommonStockSharesIssued',
                        'category': 'per_share',
                        'chinese_name': '每股销售额 (使用发行股数)'
                    }
        
        # 每股现金流
        if 'NetCashProvidedByUsedInOperatingActivities' in financial_facts:
            operating_cash_flow = financial_facts['NetCashProvidedByUsedInOperatingActivities']['value']
            
            # 使用稀释股数
            if 'WeightedAverageNumberOfDilutedSharesOutstanding' in financial_facts:
                diluted_shares = financial_facts['WeightedAverageNumberOfDilutedSharesOutstanding']['value']
                if diluted_shares != 0:
                    metrics['cash_flow_per_share'] = {
                        'value': operating_cash_flow / diluted_shares,
                        'formatted_value': f"{(operating_cash_flow / diluted_shares):.2f}",
                        'formula': 'NetCashProvidedByUsedInOperatingActivities / WeightedAverageNumberOfDilutedSharesOutstanding',
                        'category': 'per_share',
                        'chinese_name': '每股现金流'
                    }
            
            # 使用净利润+折旧摊销
            if ('DepreciationDepletionAndAmortization' in financial_facts and 
                'NetIncomeLoss' in financial_facts and 'CommonStockSharesIssued' in financial_facts):
                depreciation = financial_facts['DepreciationDepletionAndAmortization']['value']
                net_income = financial_facts['NetIncomeLoss']['value']
                issued_shares = financial_facts['CommonStockSharesIssued']['value']
                
                cash_flow_estimate = depreciation + net_income
                if issued_shares != 0:
                    metrics['cash_flow_per_share_estimate'] = {
                        'value': cash_flow_estimate / issued_shares,
                        'formatted_value': f"{(cash_flow_estimate / issued_shares):.2f}",
                        'formula': '(DepreciationDepletionAndAmortization + NetIncomeLoss) / CommonStockSharesIssued',
                        'category': 'per_share',
                        'chinese_name': '每股现金流 (使用净利润+折旧摊销)'
                    }
        
        # 每股账面价值
        if 'StockholdersEquity' in financial_facts:
            equity = financial_facts['StockholdersEquity']['value']
            
            # 使用稀释股数
            if 'WeightedAverageNumberOfDilutedSharesOutstanding' in financial_facts:
                diluted_shares = financial_facts['WeightedAverageNumberOfDilutedSharesOutstanding']['value']
                if diluted_shares != 0:
                    metrics['book_value_per_share'] = {
                        'value': equity / diluted_shares,
                        'formatted_value': f"{(equity / diluted_shares):.2f}",
                        'formula': 'StockholdersEquity / WeightedAverageNumberOfDilutedSharesOutstanding',
                        'category': 'per_share',
                        'chinese_name': '每股账面价值'
                    }
            
            # 使用发行股数
            if 'CommonStockSharesIssued' in financial_facts:
                issued_shares = financial_facts['CommonStockSharesIssued']['value']
                if issued_shares != 0:
                    metrics['book_value_per_share_issued'] = {
                        'value': equity / issued_shares,
                        'formatted_value': f"{(equity / issued_shares):.2f}",
                        'formula': 'StockholdersEquity / CommonStockSharesIssued',
                        'category': 'per_share',
                        'chinese_name': '每股账面价值 (使用发行股数)'
                    }
        
        # 每股资本支出
        if 'PaymentsToAcquirePropertyPlantAndEquipment' in financial_facts:
            capex = financial_facts['PaymentsToAcquirePropertyPlantAndEquipment']['value']
            
            # 使用稀释股数
            if 'WeightedAverageNumberOfDilutedSharesOutstanding' in financial_facts:
                diluted_shares = financial_facts['WeightedAverageNumberOfDilutedSharesOutstanding']['value']
                if diluted_shares != 0:
                    metrics['capital_spending_per_share'] = {
                        'value': capex / diluted_shares,
                        'formatted_value': f"{(capex / diluted_shares):.2f}",
                        'formula': 'PaymentsToAcquirePropertyPlantAndEquipment / WeightedAverageNumberOfDilutedSharesOutstanding',
                        'category': 'per_share',
                        'chinese_name': '每股资本支出'
                    }
            
            # 使用发行股数
            if 'CommonStockSharesIssued' in financial_facts:
                issued_shares = financial_facts['CommonStockSharesIssued']['value']
                if issued_shares != 0:
                    metrics['capital_spending_per_share_issued'] = {
                        'value': capex / issued_shares,
                        'formatted_value': f"{(capex / issued_shares):.2f}",
                        'formula': 'PaymentsToAcquirePropertyPlantAndEquipment / CommonStockSharesIssued',
                        'category': 'per_share',
                        'chinese_name': '每股资本支出 (使用发行股数)'
                    }
        
        # 在外流通普通股总数
        if 'CommonStockSharesIssued' in financial_facts:
            issued_shares = financial_facts['CommonStockSharesIssued']['value']
            metrics['common_shares_outstanding'] = {
                'value': issued_shares,
                'formatted_value': f"{issued_shares:,.0f}",
                'formula': 'CommonStockSharesIssued',
                'category': 'per_share',
                'chinese_name': '在外流通普通股总数'
            }
        
        return metrics

    def _generate_summary(self, company_info: Dict[str, Any],
                         financial_facts: Dict[str, Any],
                         calculated_metrics: Dict[str, Any],
                         fiscal_year: int) -> Dict[str, Any]:
        """生成报告摘要"""
        # 计算指标摘要
        metric_summary = self._get_metric_summary(calculated_metrics)
        
        # 按报表部分统计财务事实
        section_stats = {}
        for category, concepts in self.concepts.items():
            section_facts = {k: v for k, v in financial_facts.items() if k in concepts}
            section_stats[category] = len(section_facts)
        
        return {
            'company': {
                'name': company_info.get('name'),
                'ticker': company_info.get('ticker'),
                'cik': company_info.get('cik')
            },
            'fiscal_year': fiscal_year,
            'financial_facts': {
                'total': len(financial_facts),
                'by_section': section_stats
            },
            'calculated_metrics': metric_summary,
            'generated_at': datetime.now().isoformat()
        }
    
    def _get_metric_summary(self, calculated_metrics: Dict[str, Any]) -> Dict[str, Any]:
        """获取指标摘要"""
        categories = {}
        successful_metrics = 0
        
        for metric_name, metric_data in calculated_metrics.items():
            category = metric_data.get('category', 'other')
            if category not in categories:
                categories[category] = 0
            categories[category] += 1
            
            if metric_data.get('value') is not None:
                successful_metrics += 1
        
        return {
            'total_metrics': len(calculated_metrics),
            'successful_metrics': successful_metrics,
            'success_rate': successful_metrics / len(calculated_metrics) if calculated_metrics else 0,
            'by_category': categories
        }
    
    def get_available_companies(self):
        """获取可用的公司列表"""
        return self.db_interface.get_companies_list()
    
    def get_available_fiscal_years(self, cik: str) -> List[int]:
        """获取可用的财政年度"""
        return self.db_interface.get_available_fiscal_years(cik)
    
    def get_available_concepts(self, cik: str, fiscal_year: int = None) -> List[str]:
        """获取可用的财务概念"""
        return self.db_interface.get_available_concepts(cik, fiscal_year)
    
    def get_all_financial_concepts(self) -> List[str]:
        """获取所有财务概念列表"""
        all_concepts = []
        for category, concepts in self.concepts.items():
            all_concepts.extend(concepts.keys())
        return all_concepts
    
    def get_concepts_by_category(self, category: str) -> List[str]:
        """根据类别获取财务概念列表"""
        return list(self.concepts.get(category, {}).keys())
    
    def export_financial_data(self, cik: str, fiscal_year: int = None, 
                            output_format: str = 'csv') -> str:
        """
        导出财务数据
        
        Args:
            cik: 公司CIK码
            fiscal_year: 财政年度
            output_format: 输出格式 ('csv', 'excel', 'json')
            
        Returns:
            导出文件路径
        """
        try:
            # 获取财务事实数据
            facts_df = self.db_interface.get_financial_facts(cik, fiscal_year=fiscal_year)
            
            if facts_df.empty:
                raise ValueError(f"未找到CIK为{cik}的财务数据")
            
            # 获取公司信息
            company_info = self.db_interface.get_company_info(cik=cik)
            ticker = company_info.get('ticker', 'UNKNOWN') if company_info else 'UNKNOWN'
            
            # 确定文件名
            year_suffix = f"_{fiscal_year}" if fiscal_year else ""
            base_filename = f"{ticker}{year_suffix}_financial_data"
            
            if output_format == 'csv':
                filename = f"{base_filename}.csv"
                filepath = os.path.join(self.output_dir, filename)
                facts_df.to_csv(filepath, index=False, encoding='utf-8')
            
            elif output_format == 'excel':
                filename = f"{base_filename}.xlsx"
                filepath = os.path.join(self.output_dir, filename)
                facts_df.to_excel(filepath, index=False)
            
            elif output_format == 'json':
                filename = f"{base_filename}.json"
                filepath = os.path.join(self.output_dir, filename)
                facts_df.to_json(filepath, orient='records', indent=2, force_ascii=False)
            
            else:
                raise ValueError(f"不支持的输出格式: {output_format}")
            
            self.logger.info(f"财务数据已导出: {filepath}")
            return filepath
            
        except Exception as e:
            self.logger.error(f"导出财务数据失败: {e}")
            raise
    
    def close(self):
        """关闭数据库连接"""
        if self.db_interface:
            self.db_interface.close()
    
    def __enter__(self):
        """上下文管理器入口"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器出口"""
        self.close()
