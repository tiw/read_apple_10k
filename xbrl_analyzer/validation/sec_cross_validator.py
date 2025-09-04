#!/usr/bin/env python3
"""
SEC官网数据交叉验证器
从SEC官网获取原始数据进行对比验证
"""

import requests
import json
import re
import logging
from typing import Dict, Any, Optional, List, Tuple
from datetime import datetime
from dataclasses import dataclass
from urllib.parse import urljoin
import time

logger = logging.getLogger(__name__)


class SECCrossValidator:
    """SEC官网数据交叉验证器"""
    
    def __init__(self, user_agent: str = "XBRL Analyzer (financial-analysis@example.com)"):
        self.user_agent = user_agent
        self.base_url = "https://www.sec.gov"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        })
        
        # 请求限速设置
        self.last_request_time = 0
        self.min_request_interval = 0.5  # 500ms间隔
    
    def _rate_limit_request(self, url: str) -> requests.Response:
        """带限速的请求"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.min_request_interval:
            time.sleep(self.min_request_interval - time_since_last)
        
        try:
            response = self.session.get(url, timeout=30)
            self.last_request_time = time.time()
            return response
        except Exception as e:
            logger.error(f"请求失败: {url}, 错误: {e}")
            raise
    
    def get_sec_filing_data(self, cik: str, accession_number: str) -> Dict[str, Any]:
        """
        从SEC官网获取文件数据
        
        Args:
            cik: 公司CIK码
            accession_number: 文件编号
            
        Returns:
            SEC文件数据字典
        """
        try:
            # 构建文件URL
            formatted_accession = accession_number.replace('-', '')
            filing_url = f"{self.base_url}/Archives/edgar/data/{int(cik)}/{formatted_accession}/"
            
            logger.info(f"获取SEC文件数据: {filing_url}")
            
            # 获取 filing-summary.xml
            summary_url = urljoin(filing_url, "FilingSummary.xml")
            response = self._rate_limit_request(summary_url)
            
            if response.status_code == 200:
                return self._parse_filing_summary(response.text)
            else:
                logger.warning(f"无法获取FilingSummary.xml，状态码: {response.status_code}")
                return {}
                
        except Exception as e:
            logger.error(f"获取SEC文件数据失败: {e}")
            return {}
    
    def _parse_filing_summary(self, xml_content: str) -> Dict[str, Any]:
        """解析FilingSummary.xml"""
        try:
            import xml.etree.ElementTree as ET
            
            root = ET.fromstring(xml_content)
            
            # 提取关键财务数据
            financial_data = {}
            
            # 查找所有报表
            reports = root.findall('.//Report')
            for report in reports:
                report_name = report.get('Name', '')
                
                # 查找财务数据
                for my_co in report.findall('.//MyCo'):
                    concept = my_co.get('concept', '')
                    value = my_co.get('value', '')
                    units = my_co.get('units', '')
                    
                    if concept and value and units:
                        try:
                            # 转换数值
                            numeric_value = float(value.replace(',', '').replace('$', ''))
                            
                            # 根据单位调整
                            if units == 'USD':
                                pass  # 已经是美元
                            elif units == 'USDmillions':
                                numeric_value *= 1000000
                            elif units == 'USDbillions':
                                numeric_value *= 1000000000
                            
                            financial_data[concept] = {
                                'value': numeric_value,
                                'units': units,
                                'source': 'SEC_FilingSummary'
                            }
                            
                        except ValueError:
                            continue
            
            return financial_data
            
        except Exception as e:
            logger.error(f"解析FilingSummary失败: {e}")
            return {}
    
    def get_sec_html_data(self, cik: str, accession_number: str) -> Dict[str, Any]:
        """
        从HTML文件中提取财务数据
        
        Args:
            cik: 公司CIK码
            accession_number: 文件编号
            
        Returns:
            HTML财务数据字典
        """
        try:
            # 构建文件URL
            formatted_accession = accession_number.replace('-', '')
            filing_url = f"{self.base_url}/Archives/edgar/data/{int(cik)}/{formatted_accession}/"
            
            # 查找HTML文件
            html_url = None
            response = self._rate_limit_request(filing_url)
            
            if response.status_code == 200:
                # 从目录页面查找HTML文件
                html_files = re.findall(r'href="([^"]*\.html)"', response.text)
                if html_files:
                    html_url = urljoin(filing_url, html_files[0])
            
            if not html_url:
                logger.warning("未找到HTML文件")
                return {}
            
            logger.info(f"解析HTML文件: {html_url}")
            response = self._rate_limit_request(html_url)
            
            if response.status_code == 200:
                return self._parse_html_financial_data(response.text)
            else:
                logger.warning(f"无法获取HTML文件，状态码: {response.status_code}")
                return {}
                
        except Exception as e:
            logger.error(f"获取HTML数据失败: {e}")
            return {}
    
    def _parse_html_financial_data(self, html_content: str) -> Dict[str, Any]:
        """从HTML中提取财务数据"""
        financial_data = {}
        
        try:
            # 使用正则表达式提取关键财务数据
            patterns = {
                'RevenueFromContractWithCustomerExcludingAssessedTax': [
                    r'Net sales?\s*\$?([\d,]+)\s*million',
                    r'Revenue\s*\$?([\d,]+)\s*million',
                    r'Total net sales?\s*\$?([\d,]+)\s*million'
                ],
                'NetIncomeLoss': [
                    r'Net income\s*\$?([\d,]+)\s*million',
                    r'Net earnings?\s*\$?([\d,]+)\s*million'
                ],
                'Assets': [
                    r'Total assets?\s*\$?([\d,]+)\s*million',
                    r'Total assets?\s*\$?([\d,]+)'
                ],
                'Liabilities': [
                    r'Total liabilities?\s*\$?([\d,]+)\s*million'
                ]
            }
            
            for concept, pattern_list in patterns.items():
                for pattern in pattern_list:
                    matches = re.findall(pattern, html_content, re.IGNORECASE)
                    if matches:
                        try:
                            # 取最后一个匹配（通常是最新数据）
                            value = matches[-1].replace(',', '')
                            numeric_value = float(value)
                            
                            # 如果是millions，转换为实际数值
                            if 'million' in pattern.lower():
                                numeric_value *= 1000000
                            
                            financial_data[concept] = {
                                'value': numeric_value,
                                'source': 'SEC_HTML'
                            }
                            break
                            
                        except ValueError:
                            continue
            
            return financial_data
            
        except Exception as e:
            logger.error(f"解析HTML财务数据失败: {e}")
            return {}
    
    def validate_against_sec_api_data(self, xbrl_data: Dict[str, Any], 
                                  sec_api_client, 
                                  company_cik: str, 
                                  fiscal_year: int,
                                  report_type: str = '10-K') -> Dict[str, Any]:
        """
        使用SEC API直接获取数据进行对比验证
        
        Args:
            xbrl_data: XBRL解析的数据
            sec_api_client: SEC API客户端实例
            company_cik: 公司CIK码
            fiscal_year: 财政年度
            report_type: 报告类型 (10-K, 10-Q等)
            
        Returns:
            API验证结果字典
        """
        validation_results = {
            'api_matches': [],
            'api_mismatches': [],
            'missing_in_api': [],
            'missing_in_xbrl': [],
            'api_match_rate': 0.0,
            'api_data_source': 'SEC_API',
            'api_query_details': []
        }
        
        # 获取XBRL数据的值
        xbrl_values = {}
        for key, value in xbrl_data.items():
            if isinstance(value, dict) and 'value' in value:
                xbrl_values[key] = value['value']
            elif isinstance(value, (int, float)):
                xbrl_values[key] = value
        
        # 定义关键的财务指标映射
        key_metrics_mapping = [
            ('RevenueFromContractWithCustomerExcludingAssessedTax', 'Revenues'),
            ('NetIncomeLoss', 'NetIncomeLoss'),
            ('Assets', 'Assets'),
            ('Liabilities', 'Liabilities'),
            ('AssetsCurrent', 'AssetsCurrent'),
            ('LiabilitiesCurrent', 'LiabilitiesCurrent'),
            ('StockholdersEquity', 'StockholdersEquity'),
            ('CashAndCashEquivalentsAtCarryingValue', 'CashAndCashEquivalentsAtCarryingValue'),
            ('AccountsReceivableNetCurrent', 'AccountsReceivableNetCurrent'),
            ('InventoryNet', 'InventoryNet'),
            ('PropertyPlantAndEquipmentNet', 'PropertyPlantAndEquipmentNet'),
            ('GrossProfit', 'GrossProfit'),
            ('OperatingIncomeLoss', 'OperatingIncomeLoss'),
            ('ResearchAndDevelopmentExpense', 'ResearchAndDevelopmentExpense'),
            ('GeneralAndAdministrativeExpense', 'GeneralAndAdministrativeExpense'),
            ('NetCashProvidedByUsedInOperatingActivities', 'NetCashProvidedByUsedInOperatingActivities'),
            ('PaymentsToAcquirePropertyPlantAndEquipment', 'PaymentsToAcquirePropertyPlantAndEquipment'),
            ('EarningsPerShareBasic', 'EarningsPerShareBasic'),
            ('EarningsPerShareDiluted', 'EarningsPerShareDiluted')
        ]
        
        # SEC API数据收集
        sec_api_data = {}
        api_query_details = []
        
        for xbrl_concept, api_concept in key_metrics_mapping:
            try:
                # 使用SEC API获取数据
                concept_data = sec_api_client.get_company_concept_data(
                    cik=company_cik,
                    concept=api_concept
                )
                
                if concept_data and 'units' in concept_data:
                    # 确定合适的单位
                    unit_key, unit_data = self._determine_best_unit_for_concept(
                        concept_data['units'], api_concept
                    )
                    
                    if unit_data:
                        # 筛选特定年度和报表类型的数据
                        matching_data = []
                        for item in unit_data:
                            item_year = item.get('fy', 0)
                            item_form = item.get('form', '').upper()
                            
                            if item_year == fiscal_year and item_form == report_type.upper():
                                matching_data.append(item)
                        
                        if matching_data:
                            # 取最新的数据
                            latest_data = sorted(matching_data, key=lambda x: x.get('end', ''), reverse=True)[0]
                            
                            sec_api_data[xbrl_concept] = {
                                'value': latest_data.get('val', 0),
                                'end_date': latest_data.get('end', ''),
                                'form': latest_data.get('form', ''),
                                'fiscal_year': latest_data.get('fy', ''),
                                'unit': unit_key,
                                'source': 'SEC_API',
                                'api_concept': api_concept
                            }
                            
                            api_query_details.append({
                                'concept': xbrl_concept,
                                'api_concept': api_concept,
                                'query_successful': True,
                                'value_found': latest_data.get('val', 0),
                                'unit': unit_key
                            })
                            logger.info(f"API查询成功: {xbrl_concept} -> {api_concept} = {latest_data.get('val', 0):,}")
                        else:
                            api_query_details.append({
                                'concept': xbrl_concept,
                                'api_concept': api_concept,
                                'query_successful': False,
                                'reason': f'未找到{fiscal_year}年{report_type}数据'
                            })
                            logger.warning(f"API查询失败: {xbrl_concept} -> {api_concept}, 未找到{fiscal_year}年{report_type}数据")
                    else:
                        api_query_details.append({
                            'concept': xbrl_concept,
                            'api_concept': api_concept,
                            'query_successful': False,
                            'reason': '未找到合适的单位数据'
                        })
                        logger.warning(f"API查询失败: {xbrl_concept} -> {api_concept}, 未找到合适的单位数据")
                else:
                    api_query_details.append({
                        'concept': xbrl_concept,
                        'api_concept': api_concept,
                        'query_successful': False,
                        'reason': 'API返回空数据'
                    })
                    logger.warning(f"API查询失败: {xbrl_concept} -> {api_concept}, API返回空数据")
                    
            except Exception as e:
                api_query_details.append({
                    'concept': xbrl_concept,
                    'api_concept': api_concept,
                    'query_successful': False,
                    'reason': f'API查询异常: {str(e)}'
                })
                logger.error(f"API查询异常: {xbrl_concept} -> {api_concept}, 错误: {e}")
        
        validation_results['api_query_details'] = api_query_details
        
        # 对比数据
        total_comparisons = 0
        successful_comparisons = 0
        
        for concept in xbrl_values.keys():
            if concept in sec_api_data:
                total_comparisons += 1
                
                xbrl_value = xbrl_values[concept]
                api_value = sec_api_data[concept]['value']
                
                if api_value == 0:
                    continue
                
                # 计算差异百分比
                difference = abs(xbrl_value - api_value)
                relative_diff = difference / abs(api_value)
                
                comparison_result = {
                    'concept': concept,
                    'xbrl_value': xbrl_value,
                    'api_value': api_value,
                    'difference': difference,
                    'relative_difference': relative_diff,
                    'match_status': 'MATCH' if relative_diff <= 0.01 else 'MISMATCH',
                    'api_details': sec_api_data[concept]
                }
                
                if relative_diff <= 0.01:  # 1%以内认为匹配
                    validation_results['api_matches'].append(comparison_result)
                    successful_comparisons += 1
                    logger.info(f"API数据匹配: {concept}, XBRL={xbrl_value:,}, API={api_value:,} ({relative_diff:.1%})")
                else:
                    validation_results['api_mismatches'].append(comparison_result)
                    logger.warning(f"API数据不匹配: {concept}, XBRL={xbrl_value:,}, API={api_value:,} ({relative_diff:.1%})")
            else:
                validation_results['missing_in_api'].append(concept)
        
        # 检查API中有但XBRL中没有的数据
        for concept in sec_api_data.keys():
            if concept not in xbrl_values:
                validation_results['missing_in_xbrl'].append(concept)
        
        # 计算总体匹配率
        if total_comparisons > 0:
            validation_results['api_match_rate'] = successful_comparisons / total_comparisons
        
        return validation_results
    
    def _determine_best_unit_for_concept(self, units: Dict[str, List], concept: str) -> tuple:
        """为特定概念确定最佳单位"""
        # 每股收益相关概念
        if concept in ['EarningsPerShareBasic', 'EarningsPerShareDiluted']:
            preferred_units = ['USD/shares', 'USD per share', 'per share']
        # 股份数量相关概念
        elif concept in ['WeightedAverageNumberOfSharesOutstandingBasic', 'WeightedAverageNumberOfDilutedSharesOutstanding', 'CommonStockSharesIssued']:
            preferred_units = ['shares', 'share']
        # 默认使用USD
        else:
            preferred_units = ['USD', 'USDmillions', 'USDbillions']
        
        # 按优先级查找单位
        for preferred in preferred_units:
            if preferred in units:
                return preferred, units[preferred]
        
        # 如果没有找到首选单位，返回第一个可用单位
        if units:
            first_unit = next(iter(units))
            return first_unit, units[first_unit]
        
        return None, None
    
    def validate_against_sec_data(self, xbrl_data: Dict[str, Any], 
                                 sec_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        将XBRL数据与SEC数据进行对比验证
        
        Args:
            xbrl_data: XBRL解析的数据
            sec_data: SEC官网数据
            
        Returns:
            验证结果字典
        """
        validation_results = {
            'matches': [],
            'mismatches': [],
            'missing_in_sec': [],
            'missing_in_xbrl': [],
            'overall_match_rate': 0.0
        }
        
        # 获取XBRL数据的值
        xbrl_values = {}
        for key, value in xbrl_data.items():
            if isinstance(value, dict) and 'value' in value:
                xbrl_values[key] = value['value']
            elif isinstance(value, (int, float)):
                xbrl_values[key] = value
        
        # 对比每个关键指标
        total_comparisons = 0
        successful_comparisons = 0
        
        for concept in xbrl_values.keys():
            if concept in sec_data:
                total_comparisons += 1
                
                xbrl_value = xbrl_values[concept]
                sec_value = sec_data[concept]['value'] if isinstance(sec_data[concept], dict) else sec_data[concept]
                
                if sec_value == 0:
                    continue
                
                # 计算差异百分比
                difference = abs(xbrl_value - sec_value)
                relative_diff = difference / abs(sec_value)
                
                comparison_result = {
                    'concept': concept,
                    'xbrl_value': xbrl_value,
                    'sec_value': sec_value,
                    'difference': difference,
                    'relative_difference': relative_diff,
                    'match_status': 'MATCH' if relative_diff <= 0.01 else 'MISMATCH'
                }
                
                if relative_diff <= 0.01:  # 1%以内认为匹配
                    validation_results['matches'].append(comparison_result)
                    successful_comparisons += 1
                else:
                    validation_results['mismatches'].append(comparison_result)
                    logger.warning(f"数据不匹配: {concept}, XBRL={xbrl_value:,}, SEC={sec_value:,} ({relative_diff:.1%})")
            else:
                validation_results['missing_in_sec'].append(concept)
        
        # 检查SEC中有但XBRL中没有的数据
        for concept in sec_data.keys():
            if concept not in xbrl_values:
                validation_results['missing_in_xbrl'].append(concept)
        
        # 计算总体匹配率
        if total_comparisons > 0:
            validation_results['overall_match_rate'] = successful_comparisons / total_comparisons
        
        return validation_results
    
    def generate_sec_api_validation_report(self, validation_results: Dict[str, Any], 
                                        company_name: str, fiscal_year: int) -> str:
        """生成SEC API验证报告"""
        report = []
        report.append(f"# {company_name} {fiscal_year}年度SEC API数据交叉验证报告")
        report.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"数据来源: SEC EDGAR API")
        report.append("")
        
        # API查询概览
        query_details = validation_results.get('api_query_details', [])
        successful_queries = sum(1 for q in query_details if q.get('query_successful', False))
        total_queries = len(query_details)
        
        report.append(f"## API查询概览")
        report.append(f"- 总查询次数: {total_queries}")
        report.append(f"- 成功查询: {successful_queries}")
        report.append(f"- 失败查询: {total_queries - successful_queries}")
        report.append(f"- 查询成功率: {successful_queries/total_queries:.1%}" if total_queries > 0 else "- 查询成功率: 0%")
        report.append("")
        
        # 失败查询详情
        failed_queries = [q for q in query_details if not q.get('query_successful', False)]
        if failed_queries:
            report.append(f"## API查询失败详情")
            for query in failed_queries:
                report.append(f"- {query['concept']} -> {query['api_concept']}: {query['reason']}")
            report.append("")
        
        # 总体匹配情况
        match_rate = validation_results['api_match_rate']
        report.append(f"## 总体匹配率: {match_rate:.1%}")
        report.append("")
        
        # 匹配的数据
        if validation_results['api_matches']:
            report.append("## ✅ API匹配的数据项")
            for match in validation_results['api_matches']:
                concept = match['concept']
                xbrl_val = match['xbrl_value']
                api_val = match['api_value']
                diff_pct = match['relative_difference'] * 100
                api_details = match['api_details']
                
                report.append(f"- {concept}:")
                report.append(f"  - XBRL值: {xbrl_val:,.0f}")
                report.append(f"  - API值: {api_val:,.0f}")
                report.append(f"  - 差异: {diff_pct:.2f}%")
                report.append(f"  - API来源: {api_details['api_concept']} ({api_details['unit']})")
                report.append(f"  - 报告期: {api_details.get('fiscal_year', 'N/A')} {api_details.get('form', 'N/A')}")
            report.append("")
        
        # 不匹配的数据
        if validation_results['api_mismatches']:
            report.append("## ❌ API不匹配的数据项")
            for mismatch in validation_results['api_mismatches']:
                concept = mismatch['concept']
                xbrl_val = mismatch['xbrl_value']
                api_val = mismatch['api_value']
                diff_pct = mismatch['relative_difference'] * 100
                api_details = mismatch['api_details']
                
                report.append(f"- {concept}:")
                report.append(f"  - XBRL值: {xbrl_val:,.0f}")
                report.append(f"  - API值: {api_val:,.0f}")
                report.append(f"  - 差异: {diff_pct:.2f}%")
                report.append(f"  - API来源: {api_details['api_concept']} ({api_details['unit']})")
                report.append(f"  - 报告期: {api_details.get('fiscal_year', 'N/A')} {api_details.get('form', 'N/A')}")
            report.append("")
        
        # 缺失数据
        if validation_results['missing_in_api']:
            report.append("## ⚠️ API数据中缺失的项目")
            for item in validation_results['missing_in_api']:
                report.append(f"- {item}")
            report.append("")
        
        if validation_results['missing_in_xbrl']:
            report.append("## ℹ️ XBRL数据中缺失的项目")
            for item in validation_results['missing_in_xbrl']:
                report.append(f"- {item}")
            report.append("")
        
        # 总结和建议
        report.append("## 📋 总结和建议")
        if match_rate >= 0.9:
            report.append("✅ 数据质量优秀，与SEC API数据高度一致")
        elif match_rate >= 0.7:
            report.append("⚠️ 数据质量良好，但存在少量差异，建议关注")
        else:
            report.append("❌ 数据质量存在问题，建议重新解析或人工核对")
        
        # API查询质量评估
        if successful_queries / total_queries >= 0.8 if total_queries > 0 else 0:
            report.append("✅ API查询质量良好，大部分数据成功获取")
        else:
            report.append("⚠️ API查询存在较多失败，可能影响验证准确性")
        
        return "\n".join(report)
    
    def generate_sec_validation_report(self, validation_results: Dict[str, Any], 
                                      company_name: str, fiscal_year: int) -> str:
        """生成SEC验证报告"""
        report = []
        report.append(f"# {company_name} {fiscal_year}年度SEC数据交叉验证报告")
        report.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # 总体匹配情况
        match_rate = validation_results['overall_match_rate']
        report.append(f"## 总体匹配率: {match_rate:.1%}")
        report.append("")
        
        # 匹配的数据
        if validation_results['matches']:
            report.append("## ✅ 匹配的数据项")
            for match in validation_results['matches']:
                concept = match['concept']
                xbrl_val = match['xbrl_value']
                sec_val = match['sec_value']
                diff_pct = match['relative_difference'] * 100
                
                report.append(f"- {concept}: XBRL={xbrl_val:,.0f}, SEC={sec_val:,.0f} (差异: {diff_pct:.2f}%)")
            report.append("")
        
        # 不匹配的数据
        if validation_results['mismatches']:
            report.append("## ❌ 不匹配的数据项")
            for mismatch in validation_results['mismatches']:
                concept = mismatch['concept']
                xbrl_val = mismatch['xbrl_value']
                sec_val = mismatch['sec_value']
                diff_pct = mismatch['relative_difference'] * 100
                
                report.append(f"- {concept}: XBRL={xbrl_val:,.0f}, SEC={sec_val:,.0f} (差异: {diff_pct:.2f}%)")
            report.append("")
        
        # 缺失数据
        if validation_results['missing_in_sec']:
            report.append("## ⚠️ SEC数据中缺失的项目")
            for item in validation_results['missing_in_sec']:
                report.append(f"- {item}")
            report.append("")
        
        if validation_results['missing_in_xbrl']:
            report.append("## ℹ️ XBRL数据中缺失的项目")
            for item in validation_results['missing_in_xbrl']:
                report.append(f"- {item}")
            report.append("")
        
        # 总结和建议
        report.append("## 📋 总结和建议")
        if match_rate >= 0.9:
            report.append("✅ 数据质量优秀，与SEC官网数据高度一致")
        elif match_rate >= 0.7:
            report.append("⚠️ 数据质量良好，但存在少量差异，建议关注")
        else:
            report.append("❌ 数据质量存在问题，建议重新解析或人工核对")
        
        return "\n".join(report)


def main():
    """示例使用"""
    # 创建验证器
    validator = SECCrossValidator()
    
    # 示例数据
    xbrl_data = {
        'RevenueFromContractWithCustomerExcludingAssessedTax': {'value': 394328000000},
        'NetIncomeLoss': {'value': 99980000000},
        'Assets': {'value': 352583000000},
        'Liabilities': {'value': 290437000000}
    }
    
    sec_data = {
        'RevenueFromContractWithCustomerExcludingAssessedTax': {'value': 394328000000},
        'NetIncomeLoss': {'value': 99980000000},
        'Assets': {'value': 352583000000},
        'Liabilities': {'value': 290437000000}
    }
    
    # 执行验证
    results = validator.validate_against_sec_data(xbrl_data, sec_data)
    
    # 生成报告
    report = validator.generate_sec_validation_report(results, "Apple Inc.", 2024)
    print(report)


def test_sec_api_validation():
    """测试SEC API验证功能"""
    # 模拟XBRL数据
    xbrl_data = {
        'RevenueFromContractWithCustomerExcludingAssessedTax': {'value': 394328000000},
        'NetIncomeLoss': {'value': 99980000000},
        'Assets': {'value': 352583000000},
        'Liabilities': {'value': 290437000000},
        'StockholdersEquity': {'value': 62146000000},
        'AssetsCurrent': {'value': 143566000000},
        'LiabilitiesCurrent': {'value': 145308000000},
        'EarningsPerShareBasic': {'value': 6.15}
    }
    
    # 模拟SEC API客户端
    class MockSECClient:
        def get_company_concept_data(self, cik, concept):
            # 模拟API返回数据
            mock_data = {
                'Revenues': {
                    'units': {
                        'USD': [
                            {'val': 394328000000, 'fy': 2024, 'form': '10-K', 'end': '2024-09-28'}
                        ]
                    }
                },
                'NetIncomeLoss': {
                    'units': {
                        'USD': [
                            {'val': 99980000000, 'fy': 2024, 'form': '10-K', 'end': '2024-09-28'}
                        ]
                    }
                },
                'Assets': {
                    'units': {
                        'USD': [
                            {'val': 352583000000, 'fy': 2024, 'form': '10-K', 'end': '2024-09-28'}
                        ]
                    }
                },
                'Liabilities': {
                    'units': {
                        'USD': [
                            {'val': 290437000000, 'fy': 2024, 'form': '10-K', 'end': '2024-09-28'}
                        ]
                    }
                },
                'EarningsPerShareBasic': {
                    'units': {
                        'USD/shares': [
                            {'val': 6.15, 'fy': 2024, 'form': '10-K', 'end': '2024-09-28'}
                        ]
                    }
                }
            }
            return mock_data.get(concept)
    
    # 创建验证器
    validator = SECCrossValidator()
    mock_client = MockSECClient()
    
    # 执行验证
    results = validator.validate_against_sec_api_data(
        xbrl_data=xbrl_data,
        sec_api_client=mock_client,
        company_cik='0000320193',
        fiscal_year=2024,
        report_type='10-K'
    )
    
    # 生成报告
    report = validator.generate_sec_api_validation_report(results, "Apple Inc.", 2024)
    print(report)
    
    return results


if __name__ == "__main__":
    main()