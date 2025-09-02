#!/usr/bin/env python3
"""
使用 sec-edgar-downloader 下载10-K文件的工具
"""

import argparse
import os
import sys
from sec_edgar_downloader import Downloader


def download_10k_filing(ticker: str, year: int, output_dir: str = "./10k_xbrl"):
    """
    使用 sec-edgar-downloader 下载特定公司和年份的10-K文件
    
    Args:
        ticker: 公司股票代码 (例如: AAPL)
        year: 报告年份
        output_dir: 输出目录路径
    """
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"下载 {ticker} {year}年10-K文件到: {output_dir}")
    
    # 初始化下载器
    dl = Downloader("XBRL Analyzer", "lingma@example.com", output_dir)
    
    try:
        # 设置日期范围
        after_date = f"{year}-01-01"
        before_date = f"{year}-12-31"
        
        # 下载10-K文件
        dl.get("10-K", ticker, after=after_date, before=before_date)
        print("下载完成!")
        
        # 列出下载的文件
        downloaded_files = []
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                if file.endswith(('.xml', '.xsd', '.htm', '.html')):
                    downloaded_files.append(os.path.join(root, file))
        
        print(f"\n下载的文件:")
        for file_path in downloaded_files:
            print(f"  - {file_path}")
        
        return True
        
    except Exception as e:
        print(f"下载10-K文件时出错: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="使用 sec-edgar-downloader 下载10-K文件")
    parser.add_argument("--ticker", required=True, help="公司股票代码 (例如: AAPL)")
    parser.add_argument("--year", type=int, required=True, help="报告年份")
    parser.add_argument("--output-dir", default="./10k_xbrl", 
                       help="输出目录 (默认: ./10k_xbrl)")
    
    args = parser.parse_args()
    
    success = download_10k_filing(
        ticker=args.ticker,
        year=args.year,
        output_dir=args.output_dir
    )
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()