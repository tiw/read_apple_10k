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

# 获取当前年份
CURRENT_YEAR = datetime.now().year

# 美股七朵金花股票代码和公司名称
MAGNIFICENT_SEVEN = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "GOOGL": "Alphabet",
    "AMZN": "Amazon",
    "TSLA": "Tesla",
    "NVDA": "NVIDIA",
    "META": "Meta"
}

# 根据各公司实际情况调整年份范围
COMPANY_YEAR_RANGES = {
    "AAPL": list(range(CURRENT_YEAR - 9, CURRENT_YEAR + 1)),
    "MSFT": list(range(CURRENT_YEAR - 9, CURRENT_YEAR + 1)), 
    "GOOGL": list(range(CURRENT_YEAR - 9, CURRENT_YEAR + 1)),
    "AMZN": list(range(CURRENT_YEAR - 9, CURRENT_YEAR + 1)),
    "TSLA": list(range(CURRENT_YEAR - 9, CURRENT_YEAR + 1)),
    "NVDA": list(range(CURRENT_YEAR - 9, CURRENT_YEAR + 1)),
    "META": list(range(CURRENT_YEAR - 9, CURRENT_YEAR + 1))
}

def move_sec_files_to_root(year_dir):
    """
    将SEC下载器创建的多层目录中的文件移动到年份目录的根目录
    """
    sec_filings_dir = os.path.join(year_dir, "sec-edgar-filings")
    if os.path.exists(sec_filings_dir):
        # 查找所有文件
        for root, dirs, files in os.walk(sec_filings_dir):
            for file in files:
                src_path = os.path.join(root, file)
                dst_path = os.path.join(year_dir, file)
                
                # 移动文件到年份目录根目录
                os.rename(src_path, dst_path)
                print(f"      移动文件: {file} -> {year_dir}")
        
        # 删除空的SEC目录结构
        import shutil
        shutil.rmtree(sec_filings_dir)
        print(f"      清理SEC目录结构")


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
    # 使用针对各公司的年份范围
    years = COMPANY_YEAR_RANGES.get(ticker, list(range(CURRENT_YEAR - 9, CURRENT_YEAR + 1)))
    
    for year in years:
        year_dir = os.path.join(company_dir, str(year))
        
        # 检查是否已经下载过该年份的文件
        if os.path.exists(year_dir) and os.listdir(year_dir):
            print(f"  {year} 年的文件已存在，跳过...")
            success_count += 1
            continue
            
        print(f"  正在下载 {year} 年的文件...")
        
        # 首先尝试使用 XBRL 下载器
        cmd_xbrl = [
            "python3", 
            "xbrl_analyzer/tools/sec_10k_downloader.py",
            "--ticker", ticker,
            "--year", str(year),
            "--output-dir", year_dir
        ]
        
        try:
            result = subprocess.run(cmd_xbrl, capture_output=True, text=True, cwd=".")
            if result.returncode == 0:
                print(f"    {year} 年文件下载成功")
                success_count += 1
            else:
                print(f"    XBRL下载器失败，尝试使用SEC下载器...")
                # 如果XBRL下载器失败，尝试使用SEC下载器
                cmd_sec = [
                    "python3",
                    "xbrl_analyzer/tools/sec_edgar_downloader_tool.py",
                    "--ticker", ticker,
                    "--year", str(year),
                    "--output-dir", year_dir
                ]
                result_sec = subprocess.run(cmd_sec, capture_output=True, text=True, cwd=".")
                if result_sec.returncode == 0:
                    print(f"    {year} 年文件下载成功 (使用SEC下载器)")
                    success_count += 1
                    # 移动SEC下载的文件到当前目录
                    move_sec_files_to_root(year_dir)
                else:
                    print(f"    SEC下载器也失败: {result_sec.stderr}")
        except Exception as e:
            print(f"    {year} 年文件下载出错: {e}")
    
    # 检查下载结果，如果目录仍然为空，使用SEC下载器重试
    for year in years:
        year_dir = os.path.join(company_dir, str(year))
        if os.path.exists(year_dir) and not os.listdir(year_dir):
            print(f"  {year} 年目录为空，使用SEC下载器重试...")
            cmd_sec = [
                "python3",
                "xbrl_analyzer/tools/sec_edgar_downloader_tool.py",
                "--ticker", ticker,
                "--year", str(year),
                "--output-dir", year_dir
            ]
            try:
                result_sec = subprocess.run(cmd_sec, capture_output=True, text=True, cwd=".")
                if result_sec.returncode == 0:
                    print(f"    {year} 年文件下载成功 (重试)")
                    success_count += 1
                    # 移动SEC下载的文件到当前目录
                    move_sec_files_to_root(year_dir)
                else:
                    print(f"    重试失败: {result_sec.stderr}")
            except Exception as e:
                print(f"    重试出错: {e}")
    
    print(f"  {company_name} 完成 {success_count}/{len(years)} 年的下载")
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
    print(f"年份范围: {COMPANY_YEAR_RANGES[ticker][0]} - {COMPANY_YEAR_RANGES[ticker][-1]}")
    print(f"总计成功下载: {total_success} 个文件")

if __name__ == "__main__":
    main()
