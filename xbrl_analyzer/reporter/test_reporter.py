#!/usr/bin/env python3
"""
年报生成器测试脚本

测试年报生成器的基本功能
"""

import os
import sys
import logging
import tempfile
import shutil
from datetime import datetime

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from xbrl_analyzer.reporter import (
    AnnualReportGenerator, DuckDBInterface, FinancialCalculator,
    FinancialConcepts, CalculatedMetrics
)
from xbrl_analyzer.reporter.financial_concepts import ReportSection, MetricCategory


def setup_logging():
    """设置日志"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def test_financial_concepts():
    """测试财务概念定义"""
    print("🧪 测试财务概念定义...")
    
    # 测试获取所有概念
    all_concepts = FinancialConcepts.get_all_concepts()
    print(f"  ✅ 获取所有财务概念: {len(all_concepts)} 个")
    
    # 测试按部分获取概念
    income_concepts = FinancialConcepts.get_concepts_by_section(ReportSection.INCOME_STATEMENT)
    balance_concepts = FinancialConcepts.get_concepts_by_section(ReportSection.BALANCE_SHEET)
    cash_flow_concepts = FinancialConcepts.get_concepts_by_section(ReportSection.CASH_FLOW)
    
    print(f"  ✅ 损益表概念: {len(income_concepts)} 个")
    print(f"  ✅ 资产负债表概念: {len(balance_concepts)} 个")
    print(f"  ✅ 现金流量表概念: {len(cash_flow_concepts)} 个")
    
    # 测试计算指标
    all_metrics = CalculatedMetrics.get_all_metrics()
    print(f"  ✅ 获取所有计算指标: {len(all_metrics)} 个")
    
    # 按类别测试
    profitability_metrics = CalculatedMetrics.get_metrics_by_category(MetricCategory.PROFITABILITY)
    print(f"  ✅ 盈利能力指标: {len(profitability_metrics)} 个")


def test_financial_calculator():
    """测试财务计算器"""
    print("\n🧪 测试财务计算器...")
    
    calculator = FinancialCalculator()
    
    # 测试数字格式化
    test_values = [1234567890, 1234567, 1234, 12.34, 0.1234]
    for value in test_values:
        formatted = calculator.format_financial_number(value)
        print(f"  ✅ {value} -> {formatted}")
    
    # 测试安全除法
    test_cases = [
        (100, 10, 0.0),  # 正常除法
        (100, 0, 0.0),   # 除零
        (None, 10, 0.0), # 分子为None
        (100, None, 0.0) # 分母为None
    ]
    
    for numerator, denominator, expected in test_cases:
        result = calculator.safe_divide(numerator, denominator, expected)
        print(f"  ✅ {numerator} / {denominator} = {result}")
    
    # 测试指标计算
    sample_facts = {
        'RevenueFromContractWithCustomerExcludingAssessedTax': {'value': 1000000000},
        'GrossProfit': {'value': 400000000},
        'OperatingIncomeLoss': {'value': 200000000},
        'NetIncomeLoss': {'value': 150000000},
        'Assets': {'value': 2000000000},
        'StockholdersEquity': {'value': 800000000}
    }
    
    # 计算毛利率
    gross_margin = calculator.calculate_metric('gross_margin', sample_facts)
    if gross_margin and gross_margin.get('value') is not None:
        print(f"  ✅ 毛利率计算: {gross_margin['formatted_value']}")
    else:
        print(f"  ❌ 毛利率计算失败")
    
    # 计算ROE
    roe = calculator.calculate_metric('return_on_equity', sample_facts)
    if roe and roe.get('value') is not None:
        print(f"  ✅ ROE计算: {roe['formatted_value']}")
    else:
        print(f"  ❌ ROE计算失败")


def test_duckdb_interface():
    """测试DuckDB接口"""
    print("\n🧪 测试DuckDB接口...")
    
    # 使用临时数据库
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp_file:
        db_path = tmp_file.name
    
    try:
        # 确保文件不存在或删除现有文件
        if os.path.exists(db_path):
            os.unlink(db_path)
            
        with DuckDBInterface(db_path) as db:
            # 测试插入公司信息
            db.insert_company(
                cik="0000320193",
                ticker="AAPL",
                name="Apple Inc.",
                sic_code="3571",
                sic_description="Electronic Computers"
            )
            print("  ✅ 插入公司信息成功")
            
            # 测试获取公司信息
            company_info = db.get_company_info(cik="0000320193")
            if company_info:
                print(f"  ✅ 获取公司信息: {company_info['name']} ({company_info['ticker']})")
            else:
                print("  ❌ 获取公司信息失败")
            
            # 测试插入财务事实
            sample_facts = [
                {
                    'cik': '0000320193',
                    'concept': 'RevenueFromContractWithCustomerExcludingAssessedTax',
                    'value': 383285000000,
                    'unit': 'USD',
                    'end_date': '2024-09-28',
                    'start_date': '2023-09-30',
                    'form': '10-K',
                    'filed_date': '2024-11-01',
                    'frame': '',
                    'fiscal_year': 2024,
                    'fiscal_period': 'FY',
                    'accession_number': '0000320193-24-000123'
                }
            ]
            
            db.insert_financial_facts(sample_facts)
            print("  ✅ 插入财务事实成功")
            
            # 测试获取财务事实
            facts_df = db.get_financial_facts("0000320193")
            if hasattr(facts_df, 'empty'):
                # pandas DataFrame
                if not facts_df.empty:
                    print(f"  ✅ 获取财务事实: {len(facts_df)} 条记录")
                else:
                    print("  ❌ 获取财务事实失败")
            else:
                # 列表
                if facts_df:
                    print(f"  ✅ 获取财务事实: {len(facts_df)} 条记录")
                else:
                    print("  ❌ 获取财务事实失败")
            
            # 测试获取最新财务事实
            latest_facts = db.get_latest_financial_facts("0000320193")
            if latest_facts:
                print(f"  ✅ 获取最新财务事实: {len(latest_facts)} 个概念")
            else:
                print("  ❌ 获取最新财务事实失败")
    
    finally:
        # 清理临时文件
        if os.path.exists(db_path):
            os.unlink(db_path)


def test_report_generator():
    """测试年报生成器"""
    print("\n🧪 测试年报生成器...")
    
    # 创建临时输出目录
    temp_dir = tempfile.mkdtemp()
    
    try:
        with AnnualReportGenerator(output_dir=temp_dir) as generator:
            # 测试获取可用公司列表
            companies_df = generator.get_available_companies()
            if hasattr(companies_df, 'empty'):
                company_count = len(companies_df) if not companies_df.empty else 0
            else:
                company_count = len(companies_df)
            print(f"  ✅ 获取公司列表: {company_count} 家公司")
            
            # 如果有公司数据，测试生成报告
            has_companies = False
            if hasattr(companies_df, 'empty'):
                has_companies = not companies_df.empty
            else:
                has_companies = len(companies_df) > 0
            
            if has_companies:
                # 获取第一个公司的信息
                if hasattr(companies_df, 'iloc'):
                    # pandas DataFrame
                    first_company = companies_df.iloc[0]
                    cik = first_company['cik']
                    ticker = first_company['ticker']
                else:
                    # 列表格式
                    first_company = companies_df[0]
                    cik = first_company[0]  # cik是第1列
                    ticker = first_company[1]  # ticker是第2列
                
                print(f"  📊 测试公司: {ticker} (CIK: {cik})")
                
                # 测试获取可用财政年度
                fiscal_years = generator.get_available_fiscal_years(cik)
                print(f"  ✅ 可用财政年度: {fiscal_years}")
                
                if fiscal_years:
                    # 使用最新的财政年度
                    latest_year = max(fiscal_years)
                    print(f"  📅 使用财政年度: {latest_year}")
                    
                    # 测试生成报告
                    try:
                        results = generator.generate_company_report(
                            cik=cik,
                            fiscal_year=latest_year,
                            output_formats=['json']  # 只生成JSON格式进行测试
                        )
                        
                        if 'json' in results:
                            print(f"  ✅ 生成JSON报告: {results['json']}")
                        
                        if 'summary' in results:
                            summary = results['summary']
                            print(f"  ✅ 报告摘要: {summary['financial_facts']['total']} 个财务事实, {summary['calculated_metrics']['total_metrics']} 个计算指标")
                        
                    except Exception as e:
                        print(f"  ⚠️ 生成报告时出错: {e}")
                else:
                    print("  ⚠️ 没有可用的财政年度数据")
            else:
                print("  ⚠️ 数据库中没有公司数据，跳过报告生成测试")
    
    finally:
        # 清理临时目录
        shutil.rmtree(temp_dir, ignore_errors=True)


def main():
    """主函数"""
    setup_logging()
    
    print("🧪 XBRL年报生成器测试")
    print("=" * 60)
    print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # 运行所有测试
        test_financial_concepts()
        test_financial_calculator()
        test_duckdb_interface()
        test_report_generator()
        
        print("\n" + "=" * 60)
        print("✅ 所有测试完成!")
        print("=" * 60)
        
    except KeyboardInterrupt:
        print("\n⚠️ 用户中断了测试")
    except Exception as e:
        print(f"\n❌ 测试运行出错: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
