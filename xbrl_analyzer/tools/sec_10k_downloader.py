#!/usr/bin/env python3

import argparse
import os
import requests
import sys
from typing import Optional

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from xbrl_analyzer.tools.ticker_utils import get_cik_by_ticker

def download_xbrl_files(ticker: str, year: Optional[int] = None, output_dir: str = "./10k_xbrl"):
    """
    从SEC EDGAR下载特定公司和年份的10-K XBRL文件
    
    Args:
        ticker: 公司股票代码 (例如: AAPL)
        year: 报告年份 (可选)
        output_dir: 输出目录路径
    """
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取CIK码
    cik = get_cik_by_ticker(ticker)
    if not cik:
        print(f"无法找到股票代码 {ticker} 对应的CIK码")
        return False
    
    print(f"找到 {ticker} 的CIK码: {cik}")
    
    # 获取最新的10-K文件信息
    submissions_url = f"https://data.sec.gov/submissions/CIK{cik.zfill(10)}.json"
    headers = {
        "User-Agent": "XBRL Analyzer (lingma@example.com)"
    }
    
    try:
        response = requests.get(submissions_url, headers=headers)
        response.raise_for_status()
        submissions_data = response.json()
        
        # 查找最新的10-K文件
        filings = submissions_data.get("filings", {}).get("recent", {})
        form_types = filings.get("form", [])
        accession_numbers = filings.get("accessionNumber", [])
        report_dates = filings.get("reportDate", [])
        
        # 找到指定年份或最新的10-K文件
        target_index = None
        for i, (form, report_date) in enumerate(zip(form_types, report_dates)):
            if form == "10-K":
                report_year = int(report_date.split("-")[0])
                if year is None or report_year == year:
                    target_index = i
                    break
        
        if target_index is None:
            if year is None:
                print(f"未找到 {ticker} 的10-K文件")
            else:
                print(f"未找到 {ticker} 在 {year} 年的10-K文件")
            return False
            
        accession_number = accession_numbers[target_index]
        report_date = report_dates[target_index]
        print(f"找到{'最新的' if year is None else str(year) + '年的'}10-K文件: {accession_number} (报告日期: {report_date})")
        
        # 构建文件URL
        formatted_accession = accession_number.replace("-", "")
        base_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{formatted_accession}"
        
        # 获取目录列表以确定确切的文件名
        try:
            listing_response = requests.get(f"{base_url}/", headers=headers)
            listing_response.raise_for_status()
            listing_content = listing_response.text
            
            # 从目录中提取确切的文件名
            import re
            filename_patterns = [
                rf'({ticker.lower()}-\d{{8}}\.xsd)',
                rf'({ticker.lower()}-\d{{8}}_cal\.xml)',
                rf'({ticker.lower()}-\d{{8}}_def\.xml)',
                rf'({ticker.lower()}-\d{{8}}_lab\.xml)',
                rf'({ticker.lower()}-\d{{8}}_pre\.xml)',
                rf'({ticker.lower()}-\d{{8}}_htm\.xml)',
                rf'({ticker.lower()}_\d{{8}}\.xsd)',
                rf'({ticker.lower()}_\d{{8}}_cal\.xml)',
                rf'({ticker.lower()}_\d{{8}}_def\.xml)',
                rf'({ticker.lower()}_\d{{8}}_lab\.xml)',
                rf'({ticker.lower()}_\d{{8}}_pre\.xml)',
                rf'({ticker.lower()}_\d{{8}}_htm\.xml)',
            ]
            
            files_found = []
            for pattern in filename_patterns:
                matches = re.findall(pattern, listing_content)
                files_found.extend(matches)
            
            # 去重并过滤
            files_found = list(set(files_found))
            
            # 分类文件
            xsd_files = [f for f in files_found if f.endswith('.xsd')]
            xml_files = [f for f in files_found if f.endswith('.xml')]
            
            # 确保有正确的文件
            if not xsd_files:
                print("未找到XSD文件，使用默认命名")
                # 使用默认命名规则
                filing_date = report_dates[target_index].replace("-", "")
                files_to_download = [
                    f"{ticker.lower()}-{filing_date}.xsd",
                    f"{ticker.lower()}-{filing_date}_cal.xml",
                    f"{ticker.lower()}-{filing_date}_def.xml",
                    f"{ticker.lower()}-{filing_date}_lab.xml",
                    f"{ticker.lower()}-{filing_date}_pre.xml",
                    f"{ticker.lower()}-{filing_date}_htm.xml",
                ]
            else:
                # 只保留最多6个XML文件 (cal, def, lab, pre, htm等)
                xml_files = xml_files[:6] 
                files_to_download = xsd_files[:1] + xml_files  # 1个XSD + 最多6个XML
            
        except Exception as e:
            print(f"无法获取目录列表: {e}")
            # 使用默认命名规则
            filing_date = report_dates[target_index].replace("-", "")
            files_to_download = [
                f"{ticker.lower()}-{filing_date}.xsd",
                f"{ticker.lower()}-{filing_date}_cal.xml",
                f"{ticker.lower()}-{filing_date}_def.xml",
                f"{ticker.lower()}-{filing_date}_lab.xml",
                f"{ticker.lower()}-{filing_date}_pre.xml",
                f"{ticker.lower()}-{filing_date}_htm.xml",
            ]
        
        # 下载文件
        downloaded_files = []
        for filename in files_to_download:
            file_url = f"{base_url}/{filename}"
            output_path = os.path.join(output_dir, filename)
            
            print(f"正在下载 {file_url}")
            try:
                file_response = requests.get(file_url, headers=headers)
                file_response.raise_for_status()
                
                with open(output_path, "wb") as f:
                    f.write(file_response.content)
                
                print(f"已保存到 {output_path}")
                downloaded_files.append(filename)
                
            except Exception as e:
                print(f"下载 {filename} 失败: {e}")
        
        print(f"成功下载 {len(downloaded_files)} 个文件:")
        for file in downloaded_files:
            print(f"  - {file}")
            
        return True
        
    except Exception as e:
        print(f"获取提交信息时出错: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="从SEC EDGAR下载10-K XBRL文件")
    parser.add_argument("--ticker", required=True, help="公司股票代码 (例如: AAPL)")
    parser.add_argument("--year", type=int, help="报告年份 (可选)")
    parser.add_argument("--output-dir", default="./10k_xbrl", help="输出目录 (默认: ./10k_xbrl)")
    
    args = parser.parse_args()
    
    success = download_xbrl_files(
        ticker=args.ticker,
        year=args.year,
        output_dir=args.output_dir
    )
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()