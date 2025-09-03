"""
XBRL解析器使用示例
"""

import os
import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from xbrl_analyzer.core.parser.xbrl_parser import XBRLParser
from xbrl_analyzer.core.parser.database_storage import DatabaseStorage


def parse_and_store_file(file_path: str, db_path: str = "xbrl_parsed_data.duckdb"):
    """
    解析XBRL文件并存储到数据库
    
    Args:
        file_path: XBRL文件路径
        db_path: 数据库路径
    """
    print(f"开始处理文件: {file_path}")
    
    # 创建解析器
    parser = XBRLParser()
    
    # 解析文件
    xbrl_doc = parser.parse_file(file_path)
    
    if not xbrl_doc:
        print("解析失败")
        return
    
    # 显示解析统计信息
    stats = parser.get_parser_stats(xbrl_doc)
    print("\n解析统计信息:")
    print(f"公司: {stats['company_name']} (CIK: {stats['company_cik']})")
    print(f"报告年份: {stats['reporting_year']}")
    print(f"事实数据总数: {stats['total_facts']}")
    print(f"上下文总数: {stats['total_contexts']}")
    print(f"命名空间分布: {stats['namespace_distribution']}")
    print(f"包含年度数据: {stats['has_annual_data']}")
    
    # 存储到数据库
    print(f"\n开始存储到数据库: {db_path}")
    storage = DatabaseStorage(db_path)
    document_id = storage.store_document(xbrl_doc)
    
    if document_id:
        print(f"成功存储，文档ID: {document_id}")
        
        # 查询示例
        print("\n查询示例 - US-GAAP命名空间的前10条数据:")
        facts = storage.query_company_facts(
            company_cik=xbrl_doc.company.cik,
            year=xbrl_doc.reporting_year,
            namespace="us-gaap"
        )
        
        for i, fact in enumerate(facts[:10]):
            print(f"{i+1}. {fact['tag_name']}: {fact['value']}")
            if fact['unit']:
                print(f"   单位: {fact['unit']}")
            print(f"   上下文: {fact['context_id']}")
            print()
    
    else:
        print("存储失败")


def analyze_namespace_distribution(file_path: str):
    """
    分析文件中的命名空间分布
    
    Args:
        file_path: XBRL文件路径
    """
    print(f"分析文件命名空间分布: {file_path}")
    
    parser = XBRLParser()
    xbrl_doc = parser.parse_file(file_path)
    
    if not xbrl_doc:
        print("解析失败")
        return
    
    # 统计命名空间
    namespace_stats = {}
    for fact in xbrl_doc.facts:
        ns = fact.namespace or 'unknown'
        if ns not in namespace_stats:
            namespace_stats[ns] = []
        namespace_stats[ns].append(fact.tag_name)
    
    print("\n命名空间分析:")
    for ns, tags in namespace_stats.items():
        print(f"\n{ns}: {len(tags)} 个标签")
        # 显示前5个标签作为示例
        for tag in sorted(set(tags))[:5]:
            print(f"  - {tag}")
        if len(set(tags)) > 5:
            print(f"  ... 还有 {len(set(tags)) - 5} 个标签")


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python example.py <xbrl_file_path> [action]")
        print("Actions:")
        print("  parse_and_store (默认) - 解析并存储到数据库")
        print("  analyze_namespaces - 分析命名空间分布")
        return
    
    file_path = sys.argv[1]
    action = sys.argv[2] if len(sys.argv) > 2 else "parse_and_store"
    
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return
    
    if action == "parse_and_store":
        parse_and_store_file(file_path)
    elif action == "analyze_namespaces":
        analyze_namespace_distribution(file_path)
    else:
        print(f"未知操作: {action}")


if __name__ == "__main__":
    main()
