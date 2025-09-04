#!/usr/bin/env python3
"""
使用Apple 2024年真实10-K数据进行SEC API验证测试
从XBRL文件提取数据并与SEC API进行对比验证
"""

import sys
import os
import xml.etree.ElementTree as ET
from datetime import datetime
import re

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from xbrl_analyzer.validation.validation_orchestrator import ValidationOrchestrator
from xbrl_analyzer.validation.sec_cross_validator import SECCrossValidator


class RealSECAPIClient:
    """真实的SEC API客户端"""
    
    def __init__(self, user_agent="Ting Wang tting.wang@gmail.com"):
        self.user_agent = user_agent
        # 这里应该导入真实的SEC客户端
        # 为了演示，我们使用一个模拟的客户端
        try:
            from src import SECClient, XBRLFramesClient
            self.sec_client = SECClient(user_agent=user_agent)
            self.xbrl_client = XBRLFramesClient(self.sec_client)
            self.is_mock = False
        except ImportError:
            print("⚠️ 无法导入真实的SEC客户端，将使用模拟数据")
            self.is_mock = True
    
    def get_company_concept_data(self, cik: str, concept: str):
        """获取公司概念数据"""
        if self.is_mock:
            # 返回模拟数据
            return self._get_mock_data(concept)
        
        try:
            print(f"🔄 SEC API查询: CIK={cik}, Concept={concept}")
            return self.xbrl_client.get_company_concept_data(cik=cik, concept=concept)
        except Exception as e:
            print(f"❌ SEC API查询失败: {concept} - {e}")
            return None
    
    def _get_mock_data(self, concept: str):
        """获取模拟数据用于测试"""
        # 基于真实Apple 2024 10-K数据的模拟值
        mock_data = {
            'Revenues': {
                'units': {
                    'USD': [
                        {'val': 394328000000, 'fy': 2024, 'form': '10-K', 'end': '2024-09-28', 'filed': '2024-11-01'}
                    ]
                }
            },
            'NetIncomeLoss': {
                'units': {
                    'USD': [
                        {'val': 99980000000, 'fy': 2024, 'form': '10-K', 'end': '2024-09-28', 'filed': '2024-11-01'}
                    ]
                }
            },
            'Assets': {
                'units': {
                    'USD': [
                        {'val': 352583000000, 'fy': 2024, 'form': '10-K', 'end': '2024-09-28', 'filed': '2024-11-01'}
                    ]
                }
            },
            'Liabilities': {
                'units': {
                    'USD': [
                        {'val': 290437000000, 'fy': 2024, 'form': '10-K', 'end': '2024-09-28', 'filed': '2024-11-01'}
                    ]
                }
            },
            'StockholdersEquity': {
                'units': {
                    'USD': [
                        {'val': 62146000000, 'fy': 2024, 'form': '10-K', 'end': '2024-09-28', 'filed': '2024-11-01'}
                    ]
                }
            },
            'AssetsCurrent': {
                'units': {
                    'USD': [
                        {'val': 143566000000, 'fy': 2024, 'form': '10-K', 'end': '2024-09-28', 'filed': '2024-11-01'}
                    ]
                }
            },
            'LiabilitiesCurrent': {
                'units': {
                    'USD': [
                        {'val': 145308000000, 'fy': 2024, 'form': '10-K', 'end': '2024-09-28', 'filed': '2024-11-01'}
                    ]
                }
            }
        }
        
        # 模拟网络延迟
        import time
        time.sleep(0.1)
        
        return mock_data.get(concept)


def parse_xbrl_file(file_path: str) -> dict:
    """解析XBRL文件，提取财务数据"""
    print(f"📖 解析XBRL文件: {file_path}")
    
    try:
        # 读取XML文件
        with open(file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        # 使用XML解析器
        root = ET.fromstring(xml_content)
        
        # 定义要提取的财务指标
        target_metrics = [
            'Assets', 'Liabilities', 'StockholdersEquity', 
            'AssetsCurrent', 'LiabilitiesCurrent',
            'CashAndCashEquivalentsAtCarryingValue',
            'AccountsReceivableNetCurrent', 'InventoryNet',
            'PropertyPlantAndEquipmentNet',
            'RevenueFromContractWithCustomerExcludingAssessedTax',
            'NetIncomeLoss', 'OperatingIncomeLoss',
            'EarningsPerShareBasic', 'EarningsPerShareDiluted'
        ]
        
        # 命名空间映射
        namespaces = {
            'us-gaap': 'http://fasb.org/us-gaap/2024',
            'aapl': 'http://www.apple.com/20240928',
            'dei': 'http://xbrl.sec.gov/dei/2024',
            'xbrldi': 'http://xbrl.org/2006/xbrldi'
        }
        
        financial_data = {}
        
        for metric in target_metrics:
            # 尝试不同的命名空间前缀
            for ns_prefix, ns_uri in namespaces.items():
                elements = root.findall(f".//{ns_prefix}:{metric}", namespaces)
                if elements:
                    for element in elements:
                        # 获取contextRef来确定期间
                        context_ref = element.get('contextRef', '')
                        decimals = element.get('decimals', '0')
                        unit_ref = element.get('unitRef', 'USD')
                        
                        # 转换数值
                        try:
                            value = float(element.text)
                            
                            # 处理小数位
                            if decimals.startswith('-'):
                                multiplier = 10 ** int(decimals[1:])
                                value = value * multiplier
                            
                            financial_data[metric] = {
                                'value': value,
                                'context_ref': context_ref,
                                'decimals': decimals,
                                'unit': unit_ref,
                                'source': 'XBRL_File'
                            }
                            
                            print(f"✅ 找到 {metric}: {value:,.0f} {unit_ref}")
                            break
                        except (ValueError, TypeError) as e:
                            print(f"❌ 解析 {metric} 失败: {e}")
                
                if metric in financial_data:
                    break
        
        return financial_data
        
    except Exception as e:
        print(f"❌ 解析XBRL文件失败: {e}")
        return {}


def get_real_apple_2024_data():
    """从DuckDB数据库获取真实的Apple 2024年数据"""
    try:
        import duckdb
        
        # 连接到真实的DuckDB数据库
        conn = duckdb.connect('/Users/wangting/work/read_apple_10k/magnificent_seven_xbrl.duckdb')
        
        # 根据GAAP指标名称查询Apple 2024年的真实数据
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
        
        # 构建查询 - 使用特定的context优先级
        metrics_str = "', '".join(gaap_metrics)
        query = f'''
        SELECT ft.tag_name, ff.value, ff.unit, c.context_id, c.end_date, c.period_type, c.instant_date
        FROM financial_facts ff
        JOIN financial_tags ft ON ff.tag_id = ft.id
        JOIN contexts c ON ff.context_id = c.id
        JOIN xbrl_files xf ON ff.xbrl_file_id = xf.id
        JOIN companies comp ON xf.company_id = comp.id
        WHERE comp.cik = '0000320193' 
        AND xf.fiscal_year = 2024
        AND xf.filing_type = '10-K'
        AND ft.tag_name IN ('{metrics_str}')
        ORDER BY 
            CASE 
                WHEN c.context_id = 'c-21' THEN 1  -- 资产负债表数据优先
                WHEN c.context_id = 'c-1' THEN 2   -- 损益表数据优先
                WHEN c.context_id LIKE 'c-%' THEN 3
                ELSE 4
            END,
            ft.tag_name
        '''
        
        result = conn.execute(query).fetchall()
        
        # 转换为验证器需要的格式
        xbrl_data = {}
        for row in result:
            tag_name, value, unit, context_id, end_date, period_type, instant_date = row
            
            # 根据指标类型选择正确的context
            try:
                numeric_value = float(value)
                
                # 根据GAAP指标确定正确的context优先级
                balance_sheet_metrics = [
                    'Assets', 'Liabilities', 'StockholdersEquity',
                    'AssetsCurrent', 'LiabilitiesCurrent', 'AssetsNoncurrent', 'LiabilitiesNoncurrent',
                    'CashAndCashEquivalentsAtCarryingValue', 'MarketableSecuritiesCurrent',
                    'AccountsReceivableNetCurrent', 'InventoryNet',
                    'PropertyPlantAndEquipmentNet', 'OtherAssetsCurrent', 'OtherAssetsNoncurrent',
                    'AccountsPayableCurrent', 'OtherLiabilitiesCurrent', 'ContractWithCustomerLiabilityCurrent',
                    'CommercialPaper', 'LongTermDebtCurrent', 'LongTermDebtNoncurrent', 'OtherLiabilitiesNoncurrent',
                    'CommonStocksIncludingAdditionalPaidInCapital', 'RetainedEarningsAccumulatedDeficit',
                    'AccumulatedOtherComprehensiveIncomeLossNetOfTax'
                ]
                
                income_statement_metrics = [
                    'RevenueFromContractWithCustomerExcludingAssessedTax', 'CostOfGoodsAndServicesSold',
                    'GrossProfit', 'ResearchAndDevelopmentExpense', 'SellingGeneralAndAdministrativeExpense',
                    'OperatingIncomeLoss', 'NetIncomeLoss', 'OperatingExpenses'
                ]
                
                eps_metrics = ['EarningsPerShareBasic', 'EarningsPerShareDiluted']
                
                # 确定正确的context
                correct_context = None
                if tag_name in balance_sheet_metrics:
                    correct_context = 'c-21'  # 资产负债表使用instant context
                elif tag_name in income_statement_metrics:
                    correct_context = 'c-1'   # 损益表使用duration context
                elif tag_name in eps_metrics:
                    correct_context = 'c-21'  # EPS通常使用instant context
                
                # 只有当context匹配时才添加数据
                if context_id == correct_context:
                    xbrl_data[tag_name] = {
                        'value': numeric_value,
                        'context_ref': context_id,
                        'unit': unit,
                        'source': 'DuckDB_Database'
                    }
                    print(f"✅ 从数据库获取 {tag_name}: {numeric_value:,.0f} {unit} (Context: {context_id}, Type: {period_type})")
                elif tag_name not in xbrl_data:
                    # 如果没有找到正确的context，使用第一个可用的
                    xbrl_data[tag_name] = {
                        'value': numeric_value,
                        'context_ref': context_id,
                        'unit': unit,
                        'source': 'DuckDB_Database'
                    }
                    print(f"⚠️ 使用备用context获取 {tag_name}: {numeric_value:,.0f} {unit} (Context: {context_id}, Type: {period_type})")
                    
            except ValueError:
                print(f"❌ 转换数值失败: {tag_name} = {value}")
        
        conn.close()
        return xbrl_data
        
    except Exception as e:
        print(f"❌ 从数据库获取数据失败: {e}")
        return {}


def validate_apple_2024_data():
    """验证Apple 2024年真实数据"""
    
    print("🍎 Apple Inc. 2024年10-K数据SEC验证测试")
    print("="*70)
    
    # 从数据库获取真实数据
    xbrl_data = get_real_apple_2024_data()
    
    if not xbrl_data:
        print("❌ 未能从数据库中提取到数据")
        return
    
    print(f"\n📊 成功获取 {len(xbrl_data)} 个财务指标")
    
    # 公司信息
    company_info = {
        'name': 'Apple Inc.',
        'cik': '0000320193',
        'fiscal_year': 2024
    }
    
    # 创建SEC API客户端
    sec_api_client = RealSECAPIClient()
    
    # 创建验证协调器
    orchestrator = ValidationOrchestrator({
        'tolerance': 0.01,
        'user_agent': 'Apple SEC Validation (tting.wang@gmail.com)'
    })
    
    print(f"\n🔍 开始执行验证...")
    
    # 执行验证
    validation_result = orchestrator.validate_xbrl_document(
        xbrl_data=xbrl_data,
        company_info=company_info,
        sec_api_client=sec_api_client
    )
    
    # 显示结果
    print(f"\n📋 验证结果:")
    print(f"   验证状态: {validation_result['validation_status']}")
    print(f"   总体置信度: {validation_result['overall_confidence_score']:.1%}")
    print(f"   发现问题数: {len(validation_result['issues_found'])}")
    
    # 显示验证组件详情
    components = validation_result['validation_components']
    
    if 'internal_consistency' in components:
        internal = components['internal_consistency']
        print(f"   内部一致性: {'✅ 通过' if internal['passed'] else '❌ 失败'} "
              f"(置信度: {internal['confidence_score']:.1%})")
    
    if 'sec_api_external' in components:
        api_comp = components['sec_api_external']
        print(f"   SEC API验证: 🌐 匹配率 {api_comp['match_rate']:.1%}")
    
    # 显示问题
    if validation_result['issues_found']:
        print(f"\n❌ 发现的问题:")
        for i, issue in enumerate(validation_result['issues_found'][:5], 1):
            print(f"   {i}. {issue}")
    
    # 显示建议
    if validation_result['recommendations']:
        print(f"\n💡 建议:")
        for i, rec in enumerate(validation_result['recommendations'][:3], 1):
            print(f"   {i}. {rec}")
    
    # 生成报告
    report_path = orchestrator.generate_comprehensive_report(validation_result)
    print(f"\n📄 验证报告已保存至: {report_path}")
    
    # 显示数据详情
    print(f"\n📊 真实数据详情:")
    print("-" * 50)
    for metric, data in xbrl_data.items():
        print(f"{metric:45}: {data['value']:15,.0f} {data['unit']}")
    
    return validation_result


def test_balance_sheet_validation():
    """专门测试资产负债表平衡验证"""
    
    print(f"\n🏦 资产负债表平衡验证测试")
    print("="*50)
    
    # 从数据库获取真实数据
    xbrl_data = get_real_apple_2024_data()
    
    if not xbrl_data:
        print("❌ 未能提取到数据")
        return
    
    # 提取资产负债表关键数据
    assets = xbrl_data.get('Assets', {}).get('value', 0)
    liabilities = xbrl_data.get('Liabilities', {}).get('value', 0)
    equity = xbrl_data.get('StockholdersEquity', {}).get('value', 0)
    
    print(f"   资产总计: {assets:,.0f}")
    print(f"   负债总计: {liabilities:,.0f}")
    print(f"   股东权益: {equity:,.0f}")
    print(f"   负债+权益: {liabilities + equity:,.0f}")
    
    # 验证平衡
    difference = abs(assets - (liabilities + equity))
    relative_diff = difference / abs(assets) if assets != 0 else 0
    
    print(f"\n🔍 平衡检查:")
    print(f"   绝对差异: {difference:,.0f}")
    print(f"   相对差异: {relative_diff:.2%}")
    
    if relative_diff <= 0.001:  # 0.1%容差
        print("✅ 资产负债表平衡验证通过")
    else:
        print("❌ 资产负债表不平衡")
    
    # 使用验证器进行完整验证
    from xbrl_analyzer.validation.data_validator import XBRLDataValidator
    
    validator = XBRLDataValidator(tolerance=0.001)
    result = validator.validate_financial_data(xbrl_data)
    
    print(f"\n📊 完整验证结果:")
    print(f"   验证状态: {'✅ 通过' if result.is_valid else '❌ 失败'}")
    print(f"   置信度: {result.confidence_score:.1%}")
    print(f"   错误数: {len(result.errors)}")
    print(f"   警告数: {len(result.warnings)}")
    
    if result.errors:
        print(f"\n❌ 错误:")
        for error in result.errors:
            print(f"   - {error}")
    
    if result.warnings:
        print(f"\n⚠️ 警告:")
        for warning in result.warnings:
            print(f"   - {warning}")
    
    return result


def test_gaap_gross_profit_validation():
    """测试GAAP毛利计算验证（基于GAAP层次结构）"""
    
    print(f"\n📈 GAAP毛利计算验证测试")
    print("="*50)
    
    # 从数据库获取真实数据
    xbrl_data = get_real_apple_2024_data()
    
    if not xbrl_data:
        print("❌ 未能提取到数据")
        return
    
    # 根据GAAP层次结构验证毛利计算
    print("\n📊 毛利计算验证:")
    
    # 获取收入和成本数据
    revenue = xbrl_data.get('RevenueFromContractWithCustomerExcludingAssessedTax', {}).get('value', 0)
    cogs = xbrl_data.get('CostOfGoodsAndServicesSold', {}).get('value', 0)
    gross_profit_reported = xbrl_data.get('GrossProfit', {}).get('value', 0)
    
    # 计算毛利
    gross_profit_calculated = revenue - cogs
    
    print(f"   收入: {revenue:,.0f}")
    print(f"   销售成本: {cogs:,.0f}")
    print(f"   报告毛利: {gross_profit_reported:,.0f}")
    print(f"   计算毛利: {gross_profit_calculated:,.0f}")
    
    # 验证毛利计算
    if gross_profit_reported != 0:
        difference = abs(gross_profit_reported - gross_profit_calculated)
        relative_diff = difference / abs(gross_profit_reported)
        
        print(f"\n🔍 毛利验证:")
        print(f"   绝对差异: {difference:,.0f}")
        print(f"   相对差异: {relative_diff:.2%}")
        
        if relative_diff <= 0.01:  # 1%容差
            print("   ✅ 毛利计算验证通过")
        else:
            print("   ❌ 毛利计算验证失败")
            print(f"   💡 可能原因：缺少某些成本组件或计算方法不同")
    
    # 验证营业支出结构
    print("\n📊 营业支出结构验证:")
    
    # 获取营业支出组件
    rd_expense = xbrl_data.get('ResearchAndDevelopmentExpense', {}).get('value', 0)
    sg_expense = xbrl_data.get('SellingGeneralAndAdministrativeExpense', {}).get('value', 0)
    operating_expenses_reported = xbrl_data.get('OperatingExpenses', {}).get('value', 0)
    
    # 计算营业支出
    operating_expenses_calculated = rd_expense + sg_expense
    
    print(f"   研发费用: {rd_expense:,.0f}")
    print(f"   销售管理费用: {sg_expense:,.0f}")
    print(f"   报告营业支出: {operating_expenses_reported:,.0f}")
    print(f"   计算营业支出: {operating_expenses_calculated:,.0f}")
    
    if operating_expenses_reported != 0:
        op_diff = abs(operating_expenses_reported - operating_expenses_calculated)
        op_relative_diff = op_diff / abs(operating_expenses_reported)
        
        print(f"\n   营业支出差异: {op_relative_diff:.2%}")
        if op_relative_diff <= 0.01:
            print("   ✅ 营业支出结构验证通过")
        else:
            print("   ❌ 营业支出结构验证失败")
    
    # 验证营业利润计算
    print("\n📊 营业利润计算验证:")
    
    operating_income_reported = xbrl_data.get('OperatingIncomeLoss', {}).get('value', 0)
    operating_income_calculated = gross_profit_reported - operating_expenses_reported
    
    print(f"   报告营业利润: {operating_income_reported:,.0f}")
    print(f"   计算营业利润: {operating_income_calculated:,.0f}")
    
    if operating_income_reported != 0:
        op_income_diff = abs(operating_income_reported - operating_income_calculated)
        op_income_relative_diff = op_income_diff / abs(operating_income_reported)
        
        print(f"   营业利润差异: {op_income_relative_diff:.2%}")
        if op_income_relative_diff <= 0.01:
            print("   ✅ 营业利润计算验证通过")
        else:
            print("   ❌ 营业利润计算验证失败")
    
    return {
        'gross_profit_diff': relative_diff if gross_profit_reported != 0 else None,
        'operating_expenses_diff': op_relative_diff if operating_expenses_reported != 0 else None,
        'operating_income_diff': op_income_relative_diff if operating_income_reported != 0 else None
    }


def test_balance_sheet_structure_validation():
    """测试资产负债表结构验证（基于GAAP层次结构）"""
    
    print(f"\n🏗️ 资产负债表结构验证测试")
    print("="*50)
    
    # 从数据库获取真实数据
    xbrl_data = get_real_apple_2024_data()
    
    if not xbrl_data:
        print("❌ 未能提取到数据")
        return
    
    # 测试资产部分的结构
    print("\n📊 资产部分结构验证:")
    
    # 流动资产组成部分
    current_assets_components = [
        'CashAndCashEquivalentsAtCarryingValue',
        'MarketableSecuritiesCurrent', 
        'AccountsReceivableNetCurrent',
        'InventoryNet',
        'OtherAssetsCurrent'
    ]
    
    current_assets_sum = sum(xbrl_data.get(comp, {}).get('value', 0) for comp in current_assets_components)
    current_assets_total = xbrl_data.get('AssetsCurrent', {}).get('value', 0)
    
    print(f"   流动资产合计（计算值）: {current_assets_sum:,.0f}")
    print(f"   流动资产合计（直接值）: {current_assets_total:,.0f}")
    
    if current_assets_total != 0:
        current_diff = abs(current_assets_sum - current_assets_total) / current_assets_total
        print(f"   差异率: {current_diff:.2%}")
        if current_diff <= 0.01:  # 1%容差
            print("   ✅ 流动资产结构验证通过")
        else:
            print("   ❌ 流动资产结构验证失败")
    
    # 非流动资产组成部分
    noncurrent_assets_components = [
        'MarketableSecuritiesNoncurrent',
        'PropertyPlantAndEquipmentNet',
        'OtherAssetsNoncurrent'
    ]
    
    noncurrent_assets_sum = sum(xbrl_data.get(comp, {}).get('value', 0) for comp in noncurrent_assets_components)
    noncurrent_assets_total = xbrl_data.get('AssetsNoncurrent', {}).get('value', 0)
    
    print(f"\n   非流动资产合计（计算值）: {noncurrent_assets_sum:,.0f}")
    print(f"   非流动资产合计（直接值）: {noncurrent_assets_total:,.0f}")
    
    if noncurrent_assets_total != 0:
        noncurrent_diff = abs(noncurrent_assets_sum - noncurrent_assets_total) / noncurrent_assets_total
        print(f"   差异率: {noncurrent_diff:.2%}")
        if noncurrent_diff <= 0.01:
            print("   ✅ 非流动资产结构验证通过")
        else:
            print("   ❌ 非流动资产结构验证失败")
    
    # 测试资产总计
    assets_calculated = current_assets_sum + noncurrent_assets_sum
    assets_total = xbrl_data.get('Assets', {}).get('value', 0)
    
    print(f"\n   资产总计（计算值）: {assets_calculated:,.0f}")
    print(f"   资产总计（直接值）: {assets_total:,.0f}")
    
    if assets_total != 0:
        assets_diff = abs(assets_calculated - assets_total) / assets_total
        print(f"   差异率: {assets_diff:.2%}")
        if assets_diff <= 0.01:
            print("   ✅ 资产总计结构验证通过")
        else:
            print("   ❌ 资产总计结构验证失败")
    
    # 测试负债部分的结构
    print("\n📊 负债部分结构验证:")
    
    # 流动负债组成部分
    current_liabilities_components = [
        'AccountsPayableCurrent',
        'OtherLiabilitiesCurrent',
        'ContractWithCustomerLiabilityCurrent',
        'CommercialPaper',
        'LongTermDebtCurrent'
    ]
    
    current_liabilities_sum = sum(xbrl_data.get(comp, {}).get('value', 0) for comp in current_liabilities_components)
    current_liabilities_total = xbrl_data.get('LiabilitiesCurrent', {}).get('value', 0)
    
    print(f"   流动负债合计（计算值）: {current_liabilities_sum:,.0f}")
    print(f"   流动负债合计（直接值）: {current_liabilities_total:,.0f}")
    
    if current_liabilities_total != 0:
        current_liab_diff = abs(current_liabilities_sum - current_liabilities_total) / current_liabilities_total
        print(f"   差异率: {current_liab_diff:.2%}")
        if current_liab_diff <= 0.01:
            print("   ✅ 流动负债结构验证通过")
        else:
            print("   ❌ 流动负债结构验证失败")
    
    # 测试股东权益部分的结构
    print("\n📊 股东权益部分结构验证:")
    
    equity_components = [
        'CommonStocksIncludingAdditionalPaidInCapital',
        'RetainedEarningsAccumulatedDeficit',
        'AccumulatedOtherComprehensiveIncomeLossNetOfTax'
    ]
    
    equity_sum = sum(xbrl_data.get(comp, {}).get('value', 0) for comp in equity_components)
    equity_total = xbrl_data.get('StockholdersEquity', {}).get('value', 0)
    
    print(f"   股东权益合计（计算值）: {equity_sum:,.0f}")
    print(f"   股东权益合计（直接值）: {equity_total:,.0f}")
    
    if equity_total != 0:
        equity_diff = abs(equity_sum - equity_total) / equity_total
        print(f"   差异率: {equity_diff:.2%}")
        if equity_diff <= 0.01:
            print("   ✅ 股东权益结构验证通过")
        else:
            print("   ❌ 股东权益结构验证失败")
    
    return {
        'current_assets_diff': current_diff if current_assets_total != 0 else None,
        'noncurrent_assets_diff': noncurrent_diff if noncurrent_assets_total != 0 else None,
        'assets_diff': assets_diff if assets_total != 0 else None,
        'current_liabilities_diff': current_liab_diff if current_liabilities_total != 0 else None,
        'equity_diff': equity_diff if equity_total != 0 else None
    }


if __name__ == "__main__":
    try:
        print("🍎 Apple Inc. 2024年10-K数据综合验证测试")
        print("="*70)
        
        # 执行完整验证
        print("\n📋 1. 完整SEC验证测试")
        print("-" * 30)
        validation_result = validate_apple_2024_data()
        
        # 执行GAAP毛利验证
        print("\n📋 2. GAAP毛利计算验证测试")
        print("-" * 30)
        gross_profit_result = test_gaap_gross_profit_validation()
        
        # 执行资产负债表平衡验证
        print("\n📋 3. 资产负债表平衡验证测试")
        print("-" * 30)
        balance_result = test_balance_sheet_validation()
        
        # 执行资产负债表结构验证
        print("\n📋 4. 资产负债表结构验证测试")
        print("-" * 30)
        structure_result = test_balance_sheet_structure_validation()
        
        # 总结报告
        print("\n📋 5. 验证总结报告")
        print("-" * 30)
        print("验证测试完成！")
        print(f"• 完整验证状态: {validation_result['validation_status']}")
        print(f"• 总体置信度: {validation_result['overall_confidence_score']:.1%}")
        print(f"• 发现问题数: {len(validation_result['issues_found'])}")
        
        if gross_profit_result:
            gp_passed = gross_profit_result['gross_profit_diff'] <= 0.01 if gross_profit_result['gross_profit_diff'] is not None else False
            print(f"• GAAP毛利验证: {'✅ 通过' if gp_passed else '❌ 失败'}")
            if gross_profit_result['gross_profit_diff'] is not None:
                print(f"• 毛利差异: {gross_profit_result['gross_profit_diff']:.2%}")
        
        if balance_result:
            print(f"• 资产负债表验证: {'✅ 通过' if balance_result.is_valid else '❌ 失败'}")
            print(f"• 资产负债表置信度: {balance_result.confidence_score:.1%}")
        
        if structure_result:
            structure_passed = all(diff <= 0.01 for diff in structure_result.values() if diff is not None)
            print(f"• 资产负债表结构验证: {'✅ 通过' if structure_passed else '❌ 失败'}")
        
        print(f"\n🎉 验证测试完成!")
        
    except Exception as e:
        print(f"❌ 验证过程中出现错误: {e}")
        import traceback
        traceback.print_exc()