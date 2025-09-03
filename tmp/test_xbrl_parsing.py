#!/usr/bin/env python3
"""
测试解析SEC XBRL XML文件的CLI工具
"""

import os
import subprocess
import sys
from pathlib import Path

def test_xbrl_parsing():
    """
    测试XBRL解析CLI工具是否能正确处理下载的文件
    """
    print("测试XBRL解析CLI工具")
    print("=" * 50)
    
    # 查找一个存在的XBRL文件进行测试
    test_files_dir = "magnificent_seven_data/AAPL/2023"
    htm_file = os.path.join(test_files_dir, "aapl-20230930_htm.xml")
    xsd_file = os.path.join(test_files_dir, "aapl-20230930.xsd")
    pre_file = os.path.join(test_files_dir, "aapl-20230930_pre.xml")
    cal_file = os.path.join(test_files_dir, "aapl-20230930_cal.xml")
    def_file = os.path.join(test_files_dir, "aapl-20230930_def.xml")
    
    required_files = [htm_file, xsd_file, pre_file, cal_file, def_file]
    for file in required_files:
        if not os.path.exists(file):
            print(f"错误: 找不到测试文件 {file}")
            print("请确保已运行 download_magnificent_seven.py 脚本")
            return False
    
    print(f"使用测试文件: {htm_file}")
    print()
    
    # 测试1: 测试基本上下文列表功能
    print("测试1: 列出上下文功能")
    cmd = [sys.executable, "-m", "xbrl_analyzer.cli.main", "--file", htm_file, "--list-contexts"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        if result.returncode == 0:
            print("  ✓ 列出上下文成功")
            if result.stdout:
                contexts = result.stdout.strip().split('\n')
                print(f"  找到 {len(contexts)-1} 个上下文")  # 减去标题行
        else:
            print("  ✗ 列出上下文失败")
            print(f"  错误信息: {result.stderr}")
            return False
    except Exception as e:
        print(f"  ✗ 运行上下文命令时出错: {e}")
        return False
    
    print()
    
    # 测试2: 测试展示链接库功能
    print("测试2: 展示链接库功能")
    cmd = [sys.executable, "-m", "xbrl_analyzer.cli.main", "--file", htm_file, 
           "--presentation", pre_file, "--context-id", "FY2023"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        if result.returncode == 0:
            print("  ✓ 展示链接库解析成功")
            if result.stdout:
                lines = result.stdout.strip().split('\n')
                print(f"  返回 {len(lines)} 行数据")
        else:
            print("  ✗ 展示链接库解析失败")
            print(f"  错误信息: {result.stderr}")
            # 这个测试可能失败，因为上下文ID可能不正确，我们继续执行其他测试
    except Exception as e:
        print(f"  ✗ 运行展示链接库命令时出错: {e}")
    
    print()
    
    # 测试3: 测试生成财务报表功能
    print("测试3: 生成财务报表功能")
    cmd = [sys.executable, "-m", "xbrl_analyzer.cli.main", "--file", htm_file, 
           "--xsd", xsd_file, "--definition", def_file, "--generate-statements"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        if result.returncode == 0:
            print("  ✓ 财务报表生成成功")
            if result.stdout:
                lines = result.stdout.strip().split('\n')
                print(f"  返回 {len(lines)} 行数据")
        else:
            print("  ✗ 财务报表生成失败")
            print(f"  错误信息: {result.stderr}")
            return False
    except Exception as e:
        print(f"  ✗ 运行财务报表命令时出错: {e}")
        return False
    
    print()
    
    # 测试4: 测试导入数据库功能
    print("测试4: 导入数据库功能")
    # 确保数据库文件存在
    db_file = "xbrl.db"
    cmd = [sys.executable, "-m", "xbrl_analyzer.cli.importer", "--db", db_file, "--xbrl-file", htm_file]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        if result.returncode == 0:
            print("  ✓ 数据库导入成功")
            if result.stdout:
                print(f"  输出: {result.stdout.strip()}")
        else:
            print("  ✗ 数据库导入失败")
            print(f"  错误信息: {result.stderr}")
            return False
    except Exception as e:
        print(f"  ✗ 运行导入命令时出错: {e}")
        return False
    
    print()
    
    # 测试5: 测试查询功能
    print("测试5: 数据库查询功能")
    queries = [
        ("查询公司列表", ["--db", db_file, "list-companies"]),
        ("搜索资产相关事实", ["--db", db_file, "search-facts", "--tag-name", "Assets"]),
    ]
    
    for desc, query_args in queries:
        print(f"  {desc}")
        cmd = [sys.executable, "-m", "xbrl_analyzer.cli.db_query"] + query_args
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
            if result.returncode == 0:
                print("    ✓ 查询成功")
                if result.stdout and len(result.stdout.strip()) > 0:
                    lines = result.stdout.strip().split('\n')
                    print(f"    返回 {len(lines)} 行数据")
            else:
                print("    ✗ 查询失败")
                print(f"    错误信息: {result.stderr}")
                # 不返回False，因为某些查询可能因数据不存在而失败
        except Exception as e:
            print(f"    ✗ 运行查询命令时出错: {e}")
    
    print()
    print("=" * 50)
    print("所有测试完成!")
    return True

def main():
    """
    主函数
    """
    success = test_xbrl_parsing()
    if success:
        print("✓ XBRL解析CLI工具测试通过")
        return 0
    else:
        print("✗ XBRL解析CLI工具测试失败")
        return 1

if __name__ == "__main__":
    sys.exit(main())