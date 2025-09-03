#!/usr/bin/env python3
"""
将七朵金花十年的XBRL数据导入数据库
"""

import os
import subprocess
import sys
from pathlib import Path

def import_company_data(db_path, company_ticker):
    """
    导入单个公司的所有年份数据到数据库
    
    Args:
        db_path (str): 数据库路径
        company_ticker (str): 公司股票代码
    """
    company_dir = os.path.join("magnificent_seven_data", company_ticker)
    if not os.path.exists(company_dir):
        print(f"警告: 公司目录 {company_dir} 不存在，跳过...")
        return 0
    
    years = os.listdir(company_dir)
    years = [y for y in years if y.isdigit() and os.path.isdir(os.path.join(company_dir, y))]
    years.sort()
    
    success_count = 0
    for year in years:
        year_dir = os.path.join(company_dir, year)
        htm_file = None
        
        # 查找XBRL HTM文件
        for file_name in os.listdir(year_dir):
            if file_name.endswith('_htm.xml'):
                htm_file = os.path.join(year_dir, file_name)
                break
        
        if not htm_file:
            print(f"  警告: {company_ticker} {year} 年找不到XBRL HTM文件，跳过...")
            continue
        
        print(f"  正在导入 {company_ticker} {year} 年数据...")
        
        # 调用导入工具
        cmd = [
            sys.executable, 
            "-m", 
            "xbrl_analyzer.cli.importer", 
            "--db", 
            db_path, 
            "--xbrl-file", 
            htm_file
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
            if result.returncode == 0:
                print(f"    ✓ {company_ticker} {year} 年数据导入成功")
                success_count += 1
            else:
                print(f"    ✗ {company_ticker} {year} 年数据导入失败: {result.stderr}")
        except Exception as e:
            print(f"    ✗ 运行导入命令时出错: {e}")
    
    return success_count

def main():
    """
    主函数：导入所有七朵金花十年的数据到数据库
    """
    print("开始导入七朵金花十年的XBRL数据到数据库")
    print("=" * 50)
    
    # 数据库路径
    db_path = "xbrl.db"
    
    # 确保数据库存在
    if not os.path.exists(db_path):
        print(f"错误: 数据库文件 {db_path} 不存在")
        print("请先运行 init_db.py 初始化数据库")
        return 1
    
    # 七朵金花股票代码
    magnificent_seven = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "META"]
    
    total_companies = len(magnificent_seven)
    total_success = 0
    
    # 逐个导入每个公司的数据
    for ticker in magnificent_seven:
        print(f"\n正在处理 {ticker} 的数据...")
        success_count = import_company_data(db_path, ticker)
        total_success += success_count
        print(f"  {ticker} 完成 {success_count} 年的导入")
    
    # 输出总结
    print("\n" + "=" * 50)
    print("数据导入完成总结:")
    print(f"公司数量: {total_companies}")
    print(f"成功导入: {total_success} 个年份的数据")
    print("数据导入完成!")

if __name__ == "__main__":
    sys.exit(main())