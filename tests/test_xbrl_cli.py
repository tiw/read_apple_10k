#!/usr/bin/env python3
"""
XBRL解析器测试CLI程序
用于测试magnificent_seven_10k_optimized目录下的文件
"""

import argparse
import os
import sys
import time
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from xbrl_analyzer.core.parser.xbrl_parser import XBRLParser
from xbrl_analyzer.core.parser.database_storage import DatabaseStorage


def list_available_files(base_dir):
    """列出可用的测试文件"""
    print("可用的测试文件:")
    print("=" * 50)
    
    companies = ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'NVDA', 'META', 'TSLA']
    
    for company in companies:
        company_dir = os.path.join(base_dir, company)
        if os.path.exists(company_dir):
            print(f"\n{company}:")
            
            # 查找主要的XBRL文件
            for root, dirs, files in os.walk(company_dir):
                for file in files:
                    if file.endswith('_htm.xml') or (file.endswith('.xml') and not any(x in file for x in ['_pre', '_lab', '_cal', '_def', 'FilingSummary'])):
                        year_match = file.split('-')[1][:4] if '-' in file else 'Unknown'
                        print(f"  - {year_match}: {os.path.join(root, file)}")


def test_single_file(file_path, db_path="test_results.duckdb"):
    """测试单个文件的解析"""
    print(f"测试文件: {file_path}")
    print("=" * 60)
    
    if not os.path.exists(file_path):
        print(f"错误: 文件不存在 - {file_path}")
        return False
    
    start_time = time.time()
    
    try:
        # 解析文件
        parser = XBRLParser()
        xbrl_doc = parser.parse_file(file_path)
        
        if not xbrl_doc:
            print("解析失败!")
            return False
        
        parse_time = time.time() - start_time
        
        # 显示解析结果
        print(f"✓ 解析成功 (耗时: {parse_time:.2f}秒)")
        print(f"  公司: {xbrl_doc.company.name}")
        print(f"  CIK: {xbrl_doc.company.cik}")
        print(f"  股票代码: {xbrl_doc.company.ticker}")
        print(f"  报告年份: {xbrl_doc.reporting_year}")
        print(f"  财政期间: {xbrl_doc.fiscal_period}")
        print(f"  期末日期: {xbrl_doc.period_end_date}")
        print(f"  上下文数量: {len(xbrl_doc.contexts)}")
        print(f"  事实数据数量: {len(xbrl_doc.facts)}")
        
        # 统计命名空间
        namespace_stats = {}
        for fact in xbrl_doc.facts:
            ns = fact.namespace or 'unknown'
            namespace_stats[ns] = namespace_stats.get(ns, 0) + 1
        
        print(f"  命名空间分布:")
        for ns, count in sorted(namespace_stats.items(), key=lambda x: x[1], reverse=True):
            print(f"    {ns}: {count} 个标签")
        
        # 存储到数据库
        print(f"\n正在存储到数据库: {db_path}")
        storage = DatabaseStorage(db_path)
        
        store_start = time.time()
        document_id = storage.store_document(xbrl_doc)
        store_time = time.time() - store_start
        
        if document_id:
            print(f"✓ 存储成功 (耗时: {store_time:.2f}秒)")
            print(f"  文档ID: {document_id}")
            
            # 查询一些示例数据
            print(f"\n查询示例 - US-GAAP收入相关数据:")
            facts = storage.query_company_facts(
                company_cik=xbrl_doc.company.cik,
                year=xbrl_doc.reporting_year,
                namespace="us-gaap"
            )
            
            revenue_facts = [f for f in facts if 'revenue' in f['tag_name'].lower() or 'sales' in f['tag_name'].lower()]
            
            for i, fact in enumerate(revenue_facts[:5]):
                print(f"  {i+1}. {fact['tag_name']}: {fact['value']}")
                if fact['unit']:
                    print(f"     单位: {fact['unit']}")
        else:
            print("存储失败!")
            return False
        
        total_time = time.time() - start_time
        print(f"\n总耗时: {total_time:.2f}秒")
        return True
        
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_multiple_files(base_dir, companies=None, limit_per_company=2):
    """测试多个文件"""
    print("批量测试多个文件")
    print("=" * 60)
    
    if companies is None:
        companies = ['AAPL', 'AMZN', 'GOOGL']
    
    db_path = "batch_test_results.duckdb"
    
    # 删除旧的数据库文件
    if os.path.exists(db_path):
        os.remove(db_path)
    
    results = []
    total_start = time.time()
    
    for company in companies:
        company_dir = os.path.join(base_dir, company)
        if not os.path.exists(company_dir):
            print(f"跳过 {company}: 目录不存在")
            continue
        
        print(f"\n处理 {company}:")
        print("-" * 30)
        
        # 查找文件
        files = []
        for root, dirs, files_list in os.walk(company_dir):
            for file in files_list:
                if file.endswith('_htm.xml') or (file.endswith('.xml') and not any(x in file for x in ['_pre', '_lab', '_cal', '_def', 'FilingSummary'])):
                    files.append(os.path.join(root, file))
        
        # 限制文件数量
        files = sorted(files)[:limit_per_company]
        
        for file_path in files:
            filename = os.path.basename(file_path)
            print(f"\n  测试: {filename}")
            
            success = test_single_file(file_path, db_path)
            results.append({
                'company': company,
                'file': filename,
                'success': success,
                'path': file_path
            })
    
    # 汇总结果
    total_time = time.time() - total_start
    successful = len([r for r in results if r['success']])
    total = len(results)
    
    print("\n" + "=" * 60)
    print("批量测试结果汇总")
    print("=" * 60)
    print(f"总文件数: {total}")
    print(f"成功: {successful}")
    print(f"失败: {total - successful}")
    print(f"成功率: {successful/total*100:.1f}%")
    print(f"总耗时: {total_time:.2f}秒")
    
    # 显示数据库摘要
    if os.path.exists(db_path):
        storage = DatabaseStorage(db_path)
        summary = storage.get_document_summary()
        
        print(f"\n数据库摘要 ({db_path}):")
        for doc in summary:
            print(f"  {doc['company_name']} {doc['reporting_year']}: {doc['fact_count']} 条数据")


def main():
    parser = argparse.ArgumentParser(description='XBRL解析器测试CLI')
    parser.add_argument('--base-dir', 
                       default='magnificent_seven_10k_optimized',
                       help='测试文件基础目录 (默认: magnificent_seven_10k_optimized)')
    
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # 列出文件命令
    list_parser = subparsers.add_parser('list', help='列出可用的测试文件')
    
    # 测试单个文件命令
    test_parser = subparsers.add_parser('test', help='测试单个文件')
    test_parser.add_argument('file_path', help='XBRL文件路径')
    test_parser.add_argument('--db', default='test_results.duckdb', help='数据库文件路径')
    
    # 批量测试命令
    batch_parser = subparsers.add_parser('batch', help='批量测试多个文件')
    batch_parser.add_argument('--companies', nargs='+', 
                             default=['AAPL', 'AMZN', 'GOOGL'],
                             help='要测试的公司列表')
    batch_parser.add_argument('--limit', type=int, default=2,
                             help='每个公司测试的文件数量限制')
    
    # 快速测试命令
    quick_parser = subparsers.add_parser('quick', help='快速测试 (Apple 2024)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    base_dir = args.base_dir
    if not os.path.exists(base_dir):
        print(f"错误: 基础目录不存在 - {base_dir}")
        return
    
    if args.command == 'list':
        list_available_files(base_dir)
    
    elif args.command == 'test':
        test_single_file(args.file_path, args.db)
    
    elif args.command == 'batch':
        test_multiple_files(base_dir, args.companies, args.limit)
    
    elif args.command == 'quick':
        # 快速测试Apple 2024年的文件
        apple_2024_file = None
        apple_dir = os.path.join(base_dir, 'AAPL')
        
        for root, dirs, files in os.walk(apple_dir):
            for file in files:
                if '2024' in file and '_htm.xml' in file:
                    apple_2024_file = os.path.join(root, file)
                    break
            if apple_2024_file:
                break
        
        if apple_2024_file:
            print("快速测试 - Apple 2024年10K报告")
            test_single_file(apple_2024_file)
        else:
            print("未找到Apple 2024年的文件")


if __name__ == "__main__":
    main()
