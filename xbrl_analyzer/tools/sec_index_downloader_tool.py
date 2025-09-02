#!/usr/bin/env python3
"""
基于SEC索引的10-K文件下载工具

这个工具通过下载SEC的master.idx索引文件来查找和下载10-K文件。
支持下载最多四个季度的master.idx文件，然后解析其中的10-K文件信息并下载相应的XBRL文件。
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from typing import List, Dict, Optional, Tuple

import requests


# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from xbrl_analyzer.tools.ticker_utils import get_cik_by_ticker


class SECIndexDownloader:
    """SEC索引下载器"""
    
    def __init__(self, output_dir: str = "./10k_xbrl"):
        self.output_dir = output_dir
        self.headers = {
            "User-Agent": "XBRL Analyzer (lingma@example.com)"
        }
        self.base_url = "https://www.sec.gov/Archives/edgar/full-index"
        
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
    
    def get_quarters_for_year(self, year: int) -> List[Tuple[int, int]]:
        """
        获取指定年份的四个季度
        
        Args:
            year: 年份
            
        Returns:
            季度列表，格式为[(年, 季度), ...]
        """
        return [(year, q) for q in range(1, 5)]
    
    def get_recent_quarters(self, max_quarters: int = 4) -> List[Tuple[int, int]]:
        """
        获取最近的几个季度
        
        Args:
            max_quarters: 最大季度数
            
        Returns:
            季度列表，格式为[(年, 季度), ...]
        """
        current_year = datetime.now().year
        current_month = datetime.now().month
        
        # 确定当前季度
        if current_month <= 3:
            current_quarter = 1
        elif current_month <= 6:
            current_quarter = 2
        elif current_month <= 9:
            current_quarter = 3
        else:
            current_quarter = 4
        
        quarters = []
        year = current_year
        quarter = current_quarter
        
        for _ in range(max_quarters):
            quarters.append((year, quarter))
            quarter -= 1
            if quarter == 0:
                quarter = 4
                year -= 1
        
        return quarters
    
    def download_master_idx(self, year: int, quarter: int) -> Optional[str]:
        """
        下载指定年份和季度的master.idx文件
        
        Args:
            year: 年份
            quarter: 季度
            
        Returns:
            下载的文件路径，如果失败返回None
        """
        # 构建URL
        url = f"{self.base_url}/{year}/QTR{quarter}/master.idx"
        
        # 构建输出文件路径
        filename = f"master_{year}_Q{quarter}.idx"
        output_path = os.path.join(self.output_dir, filename)
        
        print(f"正在下载 {url}")
        
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            
            with open(output_path, "wb") as f:
                f.write(response.content)
            
            print(f"已保存到 {output_path}")
            return output_path
            
        except requests.exceptions.RequestException as e:
            print(f"下载master.idx失败: {e}")
            return None
    
    def parse_master_idx(self, file_path: str, ticker: str, cik: str) -> List[Dict]:
        """
        解析master.idx文件，查找指定公司的10-K文件
        
        Args:
            file_path: master.idx文件路径
            ticker: 股票代码
            cik: CIK码
            
        Returns:
            10-K文件信息列表
        """
        filings = []
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            # 跳过前几行（通常是头部信息）
            data_lines = []
            for line in lines:
                line = line.strip()
                if line and not line.startswith('Company Name') and not line.startswith('CIK|'):
                    # 检查是否是数据行（包含CIK码和10-K）
                    if cik in line and '10-K' in line:
                        data_lines.append(line)
            
            print(f"在 {os.path.basename(file_path)} 中找到 {len(data_lines)} 个10-K文件")
            
            # 解析每一行
            for line in data_lines:
                parts = line.split('|')
                if len(parts) >= 5:
                    cik_str = parts[0].strip()
                    company_name = parts[1].strip()
                    form_type = parts[2].strip()
                    date_filed = parts[3].strip()
                    file_path_part = parts[4].strip()
                    
                    if cik_str == cik and form_type == '10-K':
                        filing_info = {
                            'company_name': company_name,
                            'form_type': form_type,
                            'cik': cik_str,
                            'date_filed': date_filed,
                            'file_path': file_path_part,
                            'source_file': os.path.basename(file_path)
                        }
                        filings.append(filing_info)
                        print(f"  找到10-K: {date_filed} - {file_path_part}")
        
        except Exception as e:
            print(f"解析master.idx文件失败: {e}")
        
        return filings
    
    def download_xbrl_files(self, filing_info: Dict) -> bool:
        """
        下载10-K文件的XBRL文件
        
        Args:
            filing_info: 文件信息字典
            
        Returns:
            是否下载成功
        """
        file_path = filing_info['file_path']
        if not file_path:
            print("文件路径为空，无法下载")
            return False
        
        # 构建基础URL
        # 从 edgar/data/320193/0000320193-23-000106.txt
        # 到 edgar/data/320193/000032019323000106/
        # 需要移除连字符并重新格式化accession number
        parts = file_path.split('/')
        if len(parts) >= 3:
            cik = parts[2]
            accession_with_dashes = parts[3].replace('.txt', '')
            # 移除连字符：0000320193-23-000106 -> 000032019323000106
            accession_clean = accession_with_dashes.replace('-', '')
            directory_path = f"edgar/data/{cik}/{accession_clean}/"
            directory_url = f"https://www.sec.gov/Archives/{directory_path}"
        else:
            print(f"无法解析文件路径: {file_path}")
            return False
        
        print(f"正在从目录获取文件列表: {directory_url}")
        
        try:
            # 获取目录内容
            response = requests.get(directory_url, headers=self.headers, timeout=30)
            response.raise_for_status()
            directory_content = response.text
            
            # 解析目录内容，查找XBRL文件
            files_to_download = self._extract_xbrl_files(directory_content, filing_info)
            
            if not files_to_download:
                print("未找到XBRL文件")
                return False
            
            # 创建子目录
            date_filed = filing_info['date_filed'].replace('-', '')
            sub_dir = os.path.join(self.output_dir, f"{date_filed}")
            os.makedirs(sub_dir, exist_ok=True)
            
            # 下载文件
            downloaded_files = []
            for filename in files_to_download:
                file_url = f"{directory_url}{filename}"
                output_path = os.path.join(sub_dir, filename)
                
                print(f"正在下载 {file_url}")
                try:
                    file_response = requests.get(file_url, headers=self.headers, timeout=30)
                    file_response.raise_for_status()
                    
                    with open(output_path, "wb") as f:
                        f.write(file_response.content)
                    
                    print(f"已保存到 {output_path}")
                    downloaded_files.append(filename)
                    
                    # 添加延迟以避免被限制
                    time.sleep(0.1)
                    
                except Exception as e:
                    print(f"下载 {filename} 失败: {e}")
            
            print(f"成功下载 {len(downloaded_files)} 个文件到 {sub_dir}")
            return len(downloaded_files) > 0
            
        except Exception as e:
            print(f"下载XBRL文件失败: {e}")
            return False
    
    def _extract_xbrl_files(self, directory_content: str, filing_info: Dict) -> List[str]:
        """
        从目录内容中提取XBRL文件列表
        
        Args:
            directory_content: 目录HTML内容
            filing_info: 文件信息
            
        Returns:
            XBRL文件名列表
        """
        files_to_download = []
        
        # 尝试使用MetaLinks.json获取文件列表
        try:
            # 构建MetaLinks.json URL
            file_path = filing_info['file_path']
            base_url = f"https://www.sec.gov/Archives/{file_path}"
            directory_url = base_url.rsplit('/', 1)[0] + "/"
            meta_links_url = f"{directory_url}MetaLinks.json"
            
            print(f"尝试获取MetaLinks.json: {meta_links_url}")
            meta_response = requests.get(meta_links_url, headers=self.headers, timeout=30)
            meta_response.raise_for_status()
            meta_data = meta_response.json()
            
            # 从MetaLinks.json中获取实例文档
            instance_files = meta_data.get('instance', {})
            for filename, instance_info in instance_files.items():
                # 将.htm文件转换为_htm.xml格式
                if filename.endswith('.htm'):
                    xml_filename = filename.replace('.htm', '_htm.xml')
                    files_to_download.append(xml_filename)
                else:
                    files_to_download.append(filename)
                
                # 从实例信息的dts部分获取各种链接库文件
                dts = instance_info.get('dts', {})
                
                # 获取各种链接库文件
                for link_type in ['calculationLink', 'definitionLink', 'labelLink', 'presentationLink', 'schema']:
                    link_files = dts.get(link_type, {}).get('local', [])
                    files_to_download.extend(link_files)
            
            print(f"从MetaLinks.json获取到 {len(files_to_download)} 个文件")
            
        except Exception as e:
            print(f"无法获取MetaLinks.json: {e}")
            print("尝试从HTML目录中解析文件...")
            
            # 从HTML目录中解析文件
            file_patterns = [
                r'href="([^"]*\.xsd)"',
                r'href="([^"]*_cal\.xml)"',
                r'href="([^"]*_def\.xml)"',
                r'href="([^"]*_lab\.xml)"',
                r'href="([^"]*_pre\.xml)"',
                r'href="([^"]*_htm\.xml)"',
                r'href="([^"]*\.xml)"',
            ]
            
            for pattern in file_patterns:
                matches = re.findall(pattern, directory_content, re.IGNORECASE)
                files_to_download.extend(matches)
            
            # 去重并清理文件路径
            files_to_download = list(set(files_to_download))
            # 只保留文件名，移除完整路径
            cleaned_files = []
            for file_path in files_to_download:
                # 如果包含完整URL路径，只取文件名部分
                if '/' in file_path:
                    filename = file_path.split('/')[-1]
                    cleaned_files.append(filename)
                else:
                    cleaned_files.append(file_path)
            
            files_to_download = cleaned_files
            print(f"从HTML目录中找到 {len(files_to_download)} 个文件")
        
        return files_to_download
    
    def download_10k_by_index(self, ticker: str, year: Optional[int] = None, max_quarters: int = 4) -> bool:
        """
        通过SEC索引下载10-K文件
        
        Args:
            ticker: 股票代码
            year: 指定年份（可选）
            max_quarters: 最大季度数
            
        Returns:
            是否下载成功
        """
        # 获取CIK码
        cik = get_cik_by_ticker(ticker)
        if not cik:
            print(f"无法找到股票代码 {ticker} 对应的CIK码")
            return False
        
        print(f"找到 {ticker} 的CIK码: {cik}")
        
        # 确定要下载的季度
        if year:
            quarters = self.get_quarters_for_year(year)
        else:
            quarters = self.get_recent_quarters(max_quarters)
        
        print(f"将下载以下季度的索引: {quarters}")
        
        all_filings = []
        
        # 下载master.idx文件并解析
        for year, quarter in quarters:
            print(f"\n处理 {year}年Q{quarter}...")
            
            # 下载master.idx
            master_file = self.download_master_idx(year, quarter)
            if not master_file:
                print(f"跳过 {year}年Q{quarter}，下载失败")
                continue
            
            # 解析master.idx
            filings = self.parse_master_idx(master_file, ticker, cik)
            all_filings.extend(filings)
            
            # 添加延迟
            time.sleep(1)
        
        if not all_filings:
            print(f"未找到 {ticker} 的10-K文件")
            return False
        
        print(f"\n总共找到 {len(all_filings)} 个10-K文件")
        
        # 按日期排序，最新的在前
        all_filings.sort(key=lambda x: x['date_filed'], reverse=True)
        
        # 下载XBRL文件
        success_count = 0
        for i, filing in enumerate(all_filings):
            print(f"\n下载第 {i+1} 个10-K文件 (日期: {filing['date_filed']})")
            if self.download_xbrl_files(filing):
                success_count += 1
            
            # 添加延迟
            time.sleep(2)
        
        print(f"\n成功下载 {success_count}/{len(all_filings)} 个10-K文件")
        return success_count > 0


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="基于SEC索引下载10-K XBRL文件")
    parser.add_argument("--ticker", required=True, help="公司股票代码 (例如: AAPL)")
    parser.add_argument("--year", type=int, help="指定年份 (可选，默认下载最近4个季度)")
    parser.add_argument("--max-quarters", type=int, default=4, 
                       help="最大季度数 (默认: 4)")
    parser.add_argument("--output-dir", default="./10k_xbrl", 
                       help="输出目录 (默认: ./10k_xbrl)")
    
    args = parser.parse_args()
    
    downloader = SECIndexDownloader(output_dir=args.output_dir)
    
    success = downloader.download_10k_by_index(
        ticker=args.ticker,
        year=args.year,
        max_quarters=args.max_quarters
    )
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()