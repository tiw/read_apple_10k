#!/usr/bin/env python3
"""
年报生成器使用示例

演示如何使用年报生成器生成10-K年报分析报告
"""

import os
import sys
import logging
from datetime import datetime

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from xbrl_analyzer.reporter import AnnualReportGenerator, DuckDBInterface, FinancialCalculator


def setup_logging():
    """设置日志"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def example_1_single_company_report():
    """示例1: 生成单个公司的年报"""
    print("=" * 60)
    print("示例1: 生成单个公司的年报")
    print("=" * 60)
    
    # 使用内存数据库进行演示
    with AnnualReportGenerator(output_dir="./example_reports") as generator:
        try:
            # 生成Apple公司的2024年年报
            results = generator.generate_ticker_report(
                ticker="AAPL",
                fiscal_year=2024,
                output_formats=['html', 'markdown', 'json']
            )
            
            print("✅ 年报生成成功!")
            print(f"📊 摘要信息:")
            summary = results['summary']
            print(f"  - 公司: {summary['company']['name']} ({summary['company']['ticker']})")
            print(f"  - 财政年度: {summary['fiscal_year']}")
            print(f"  - 财务事实: {summary['financial_facts']['total']} 个")
            print(f"  - 计算指标: {summary['calculated_metrics']['total_metrics']} 个")
            print(f"  - 成功率: {summary['calculated_metrics']['success_rate']:.1%}")
            
            print(f"\n📁 生成的文件:")
            for format_type, filepath in results.items():
                if format_type != 'summary':
                    print(f"  - {format_type.upper()}: {filepath}")
            
        except Exception as e:
            print(f"❌ 生成年报失败: {e}")


def example_2_batch_reports():
    """示例2: 批量生成多个公司的年报"""
    print("\n" + "=" * 60)
    print("示例2: 批量生成多个公司的年报")
    print("=" * 60)
    
    # 七朵金花公司列表
    magnificent_seven = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA"]
    
    with AnnualReportGenerator(output_dir="./example_reports") as generator:
        try:
            # 批量生成年报（只生成HTML和Markdown格式）
            results = generator.generate_batch_reports(
                tickers=magnificent_seven,
                fiscal_year=2024,
                output_formats=['html', 'markdown']
            )
            
            print("✅ 批量年报生成完成!")
            summary = results['summary']
            print(f"📊 批量生成摘要:")
            print(f"  - 总公司数: {summary['total_companies']}")
            print(f"  - 成功生成: {summary['successful']}")
            print(f"  - 生成失败: {summary['failed']}")
            print(f"  - 成功率: {summary['success_rate']:.1%}")
            
            print(f"\n📋 详细结果:")
            for ticker, result in results['results'].items():
                status = "✅" if result['status'] == 'success' else "❌"
                print(f"  {status} {ticker}: {result['status']}")
                if result['status'] == 'failed':
                    print(f"    错误: {result['error']}")
            
        except Exception as e:
            print(f"❌ 批量生成失败: {e}")


def example_3_data_export():
    """示例3: 导出财务数据"""
    print("\n" + "=" * 60)
    print("示例3: 导出财务数据")
    print("=" * 60)
    
    with AnnualReportGenerator(output_dir="./example_reports") as generator:
        try:
            # 导出Apple公司的财务数据
            csv_file = generator.export_financial_data(
                cik="0000320193",  # Apple的CIK
                fiscal_year=2024,
                output_format='csv'
            )
            
            print(f"✅ 财务数据导出成功!")
            print(f"📁 CSV文件: {csv_file}")
            
            # 也可以导出为Excel格式
            excel_file = generator.export_financial_data(
                cik="0000320193",
                fiscal_year=2024,
                output_format='excel'
            )
            
            print(f"📁 Excel文件: {excel_file}")
            
        except Exception as e:
            print(f"❌ 导出财务数据失败: {e}")


def example_4_database_operations():
    """示例4: 数据库操作示例"""
    print("\n" + "=" * 60)
    print("示例4: 数据库操作示例")
    print("=" * 60)
    
    with DuckDBInterface() as db:
        try:
            # 获取公司列表
            companies_df = db.get_companies_list()
            print(f"📊 数据库中的公司数量: {len(companies_df)}")
            
            if not companies_df.empty:
                print(f"📋 前5家公司:")
                for _, company in companies_df.head().iterrows():
                    print(f"  - {company['ticker']}: {company['name']} (CIK: {company['cik']})")
            
            # 获取Apple的可用财政年度
            apple_cik = "0000320193"
            fiscal_years = db.get_available_fiscal_years(apple_cik)
            print(f"\n📅 Apple的可用财政年度: {fiscal_years}")
            
            # 获取Apple的可用财务概念
            concepts = db.get_available_concepts(apple_cik, fiscal_year=2024)
            print(f"📊 Apple 2024年的财务概念数量: {len(concepts)}")
            
            if concepts:
                print(f"📋 前10个财务概念:")
                for concept in concepts[:10]:
                    print(f"  - {concept}")
            
        except Exception as e:
            print(f"❌ 数据库操作失败: {e}")


def example_5_financial_calculations():
    """示例5: 财务指标计算示例"""
    print("\n" + "=" * 60)
    print("示例5: 财务指标计算示例")
    print("=" * 60)
    
    # 模拟财务事实数据
    sample_facts = {
        'RevenueFromContractWithCustomerExcludingAssessedTax': {
            'value': 383285000000,  # 383.285B USD
            'unit': 'USD'
        },
        'CostOfGoodsAndServicesSold': {
            'value': 214137000000,  # 214.137B USD
            'unit': 'USD'
        },
        'GrossProfit': {
            'value': 169148000000,  # 169.148B USD
            'unit': 'USD'
        },
        'OperatingIncomeLoss': {
            'value': 123600000000,  # 123.6B USD
            'unit': 'USD'
        },
        'NetIncomeLoss': {
            'value': 97000000000,   # 97B USD
            'unit': 'USD'
        },
        'Assets': {
            'value': 352755000000,  # 352.755B USD
            'unit': 'USD'
        },
        'StockholdersEquity': {
            'value': 74146000000,   # 74.146B USD
            'unit': 'USD'
        }
    }
    
    calculator = FinancialCalculator()
    
    # 计算所有指标
    metrics = calculator.calculate_all_metrics(sample_facts)
    
    print("✅ 财务指标计算完成!")
    print(f"📊 计算了 {len(metrics)} 个财务指标")
    
    # 显示盈利能力指标
    profitability_metrics = {k: v for k, v in metrics.items() if v.get('category') == 'profitability'}
    print(f"\n💰 盈利能力指标:")
    for metric_name, metric in profitability_metrics.items():
        if metric.get('value') is not None:
            print(f"  - {metric['chinese_name']}: {metric['formatted_value']}")
    
    # 显示流动性指标
    liquidity_metrics = {k: v for k, v in metrics.items() if v.get('category') == 'liquidity'}
    if liquidity_metrics:
        print(f"\n💧 流动性指标:")
        for metric_name, metric in liquidity_metrics.items():
            if metric.get('value') is not None:
                print(f"  - {metric['chinese_name']}: {metric['formatted_value']}")
    
    # 显示杠杆比率
    leverage_metrics = {k: v for k, v in metrics.items() if v.get('category') == 'leverage'}
    if leverage_metrics:
        print(f"\n⚖️ 杠杆比率:")
        for metric_name, metric in leverage_metrics.items():
            if metric.get('value') is not None:
                print(f"  - {metric['chinese_name']}: {metric['formatted_value']}")


def main():
    """主函数"""
    setup_logging()
    
    print("🚀 XBRL年报生成器使用示例")
    print("=" * 60)
    print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # 运行所有示例
        example_1_single_company_report()
        example_2_batch_reports()
        example_3_data_export()
        example_4_database_operations()
        example_5_financial_calculations()
        
        print("\n" + "=" * 60)
        print("✅ 所有示例运行完成!")
        print("=" * 60)
        
    except KeyboardInterrupt:
        print("\n⚠️ 用户中断了示例运行")
    except Exception as e:
        print(f"\n❌ 示例运行出错: {e}")


if __name__ == "__main__":
    main()
