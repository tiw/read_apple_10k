#!/usr/bin/env python3
"""
下载美股七朵金花（Magnificent Seven）近十年的10-K文档
包括：Apple (AAPL), Microsoft (MSFT), Alphabet (GOOGL), Amazon (AMZN), 
      Tesla (TSLA), NVIDIA (NVDA), Meta (META)
"""

import os
import subprocess
import sys
from datetime import datetime

# 美股七朵金花股票代码
MAGNIFICENT_SEVEN = {
    "AAPL": "Apple",
    "MSFT": "Microsoft", 
    "GOOGL": "Alphabet",
    "AMZN": "Amazon",
    "TSLA": "Tesla",
    "NVDA": "NVIDIA",
    "META": "Meta"
}

# 近十年
CURRENT_YEAR = datetime.now().year
YEARS = list(range(CURRENT_YEAR - 9, CURRENT_YEAR + 1))  # 近十年

def download_company_files(ticker, company_name):
    """
    下载单个公司的近十年10-K文件
    
    Args:
        ticker: 股票代码
        company_name: 公司名称
    """
    print(f"\n开始下载 {company_name} ({ticker}) 的10-K文件...")
    
    company_dir = os.path.join("magnificent_seven_data", ticker)
    os.makedirs(company_dir, exist_ok=True)
    
    success_count = 0
    for year in YEARS:
        year_dir = os.path.join(company_dir, str(year))
        
        # 检查是否已经下载过该年份的文件
        if os.path.exists(year_dir) and os.listdir(year_dir):
            print(f"  {year} 年的文件已存在，跳过...")
            success_count += 1
            continue
            
        print(f"  正在下载 {year} 年的文件...")
        
        # 调用现有的下载器脚本
        cmd = [
            "python3", 
            "xbrl_analyzer/tools/sec_10k_downloader.py",
            "--ticker", ticker,
            "--year", str(year),
            "--output-dir", year_dir
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
            if result.returncode == 0:
                print(f"    {year} 年文件下载成功")
                success_count += 1
            else:
                print(f"    {year} 年文件下载失败: {result.stderr}")
        except Exception as e:
            print(f"    {year} 年文件下载出错: {e}")
    
    print(f"  {company_name} 完成 {success_count}/{len(YEARS)} 年的下载")
    return success_count

def main():
    """
    主函数：下载所有七朵金花公司的近十年10-K文件
    """
    print("开始下载美股七朵金花近十年的10-K文档")
    print("=" * 50)
    
    # 确保主数据目录存在
    os.makedirs("magnificent_seven_data", exist_ok=True)
    
    # 记录总体统计
    total_companies = len(MAGNIFICENT_SEVEN)
    total_years = len(YEARS)
    total_possible = total_companies * total_years
    total_success = 0
    
    # 逐个下载每个公司的文件
    for ticker, company_name in MAGNIFICENT_SEVEN.items():
        try:
            success_count = download_company_files(ticker, company_name)
            total_success += success_count
        except Exception as e:
            print(f"下载 {company_name} 文件时出错: {e}")
    
    # 输出总结
    print("\n" + "=" * 50)
    print("下载完成总结:")
    print(f"公司数量: {total_companies}")
    print(f"年份范围: {YEARS[0]} - {YEARS[-1]}")
    print(f"总计尝试下载: {total_possible} 个文件")
    print(f"成功下载: {total_success} 个文件")
    print(f"成功率: {total_success/total_possible*100:.1f}%")

if __name__ == "__main__":
    main()