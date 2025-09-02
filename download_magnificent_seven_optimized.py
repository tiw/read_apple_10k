#!/usr/bin/env python3
"""
优化版七朵金花近10年10-K数据下载工具

优化策略：
1. 先下载所有需要的季度索引文件（避免重复下载）
2. 然后一次性解析所有公司的10-K文件
3. 最后批量下载XBRL文件
"""

import os
import sys
import time
from datetime import datetime
from typing import List, Dict, Optional, Set, Tuple

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from xbrl_analyzer.tools.sec_index_downloader_tool import SECIndexDownloader
from xbrl_analyzer.tools.ticker_utils import get_cik_by_ticker


class OptimizedMagnificentSevenDownloader:
    """优化的七朵金花下载器"""
    
    def __init__(self, output_dir: str = "./magnificent_seven_10k_optimized"):
        self.output_dir = output_dir
        self.downloader = SECIndexDownloader(output_dir=output_dir)
        self.magnificent_seven = [
            "AAPL",  # Apple Inc.
            "MSFT",  # Microsoft Corp.
            "GOOGL", # Alphabet Inc.
            "AMZN",  # Amazon.com Inc.
            "META",  # Meta Platforms, Inc.
            "NVDA",  # NVIDIA Corp.
            "TSLA"   # Tesla, Inc.
        ]
        
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
    
    def get_quarters_to_download(self, max_quarters: int = 40) -> List[Tuple[int, int]]:
        """
        获取需要下载的季度列表
        
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
    
    def download_all_quarter_indexes(self, quarters: List[Tuple[int, int]]) -> Dict[Tuple[int, int], str]:
        """
        下载所有需要的季度索引文件
        
        Args:
            quarters: 季度列表
            
        Returns:
            季度到文件路径的映射
        """
        print("=" * 60)
        print("第一步：下载所有季度索引文件")
        print("=" * 60)
        
        quarter_files = {}
        total_quarters = len(quarters)
        
        for i, (year, quarter) in enumerate(quarters, 1):
            print(f"[{i}/{total_quarters}] 下载 {year}年Q{quarter} 索引...")
            
            file_path = self.downloader.download_master_idx(year, quarter)
            if file_path:
                quarter_files[(year, quarter)] = file_path
                print(f"✅ 成功下载 {year}年Q{quarter} 索引")
            else:
                print(f"❌ 下载 {year}年Q{quarter} 索引失败")
            
            # 添加延迟
            time.sleep(1)
        
        print(f"\n索引下载完成：成功 {len(quarter_files)}/{total_quarters} 个季度")
        return quarter_files
    
    def parse_all_companies_from_indexes(self, quarter_files: Dict[Tuple[int, int], str]) -> Dict[str, List[Dict]]:
        """
        从所有索引文件中解析所有公司的10-K文件
        
        Args:
            quarter_files: 季度到文件路径的映射
            
        Returns:
            公司到10-K文件列表的映射
        """
        print("\n" + "=" * 60)
        print("第二步：解析所有公司的10-K文件")
        print("=" * 60)
        
        # 获取所有公司的CIK码
        company_ciks = {}
        for ticker in self.magnificent_seven:
            cik = get_cik_by_ticker(ticker)
            if cik:
                company_ciks[ticker] = cik
                print(f"✅ {ticker}: CIK {cik}")
            else:
                print(f"❌ {ticker}: 无法获取CIK码")
        
        # 解析所有索引文件
        all_filings = {ticker: [] for ticker in self.magnificent_seven}
        
        for (year, quarter), file_path in quarter_files.items():
            print(f"\n解析 {year}年Q{quarter} 索引...")
            
            for ticker, cik in company_ciks.items():
                filings = self.downloader.parse_master_idx(file_path, ticker, cik)
                all_filings[ticker].extend(filings)
        
        # 统计结果
        print(f"\n解析结果统计：")
        for ticker, filings in all_filings.items():
            print(f"  {ticker}: {len(filings)} 个10-K文件")
        
        return all_filings
    
    def download_all_xbrl_files(self, all_filings: Dict[str, List[Dict]]) -> Dict[str, bool]:
        """
        下载所有公司的XBRL文件
        
        Args:
            all_filings: 公司到10-K文件列表的映射
            
        Returns:
            公司到下载结果的映射
        """
        print("\n" + "=" * 60)
        print("第三步：下载所有XBRL文件")
        print("=" * 60)
        
        results = {}
        total_companies = len(self.magnificent_seven)
        
        for i, ticker in enumerate(self.magnificent_seven, 1):
            print(f"\n[{i}/{total_companies}] 下载 {ticker} 的XBRL文件...")
            print("-" * 40)
            
            filings = all_filings.get(ticker, [])
            if not filings:
                print(f"❌ {ticker}: 没有找到10-K文件")
                results[ticker] = False
                continue
            
            # 按日期排序，最新的在前
            filings.sort(key=lambda x: x['date_filed'], reverse=True)
            
            # 为每个公司创建子目录
            company_output_dir = os.path.join(self.output_dir, ticker)
            os.makedirs(company_output_dir, exist_ok=True)
            
            # 下载XBRL文件
            success_count = 0
            for j, filing in enumerate(filings):
                print(f"  下载第 {j+1}/{len(filings)} 个10-K文件 (日期: {filing['date_filed']})")
                
                # 创建临时下载器实例用于下载XBRL文件
                temp_downloader = SECIndexDownloader(output_dir=company_output_dir)
                if temp_downloader.download_xbrl_files(filing):
                    success_count += 1
                
                # 添加延迟
                time.sleep(1)
            
            if success_count > 0:
                print(f"✅ {ticker}: 成功下载 {success_count}/{len(filings)} 个10-K文件")
                results[ticker] = True
            else:
                print(f"❌ {ticker}: 下载失败")
                results[ticker] = False
        
        return results
    
    def download_magnificent_seven_optimized(self, max_quarters: int = 40) -> Dict[str, bool]:
        """
        优化的七朵金花下载流程
        
        Args:
            max_quarters: 最大季度数
            
        Returns:
            公司到下载结果的映射
        """
        print("=" * 60)
        print("优化版七朵金花近10年10-K数据下载")
        print("=" * 60)
        print(f"目标公司: {', '.join(self.magnificent_seven)}")
        print(f"最大季度数: {max_quarters}")
        print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        # 第一步：获取需要下载的季度
        quarters = self.get_quarters_to_download(max_quarters)
        print(f"需要下载的季度: {len(quarters)} 个")
        
        # 第二步：下载所有季度索引文件
        quarter_files = self.download_all_quarter_indexes(quarters)
        
        if not quarter_files:
            print("❌ 没有成功下载任何索引文件，任务终止")
            return {ticker: False for ticker in self.magnificent_seven}
        
        # 第三步：解析所有公司的10-K文件
        all_filings = self.parse_all_companies_from_indexes(quarter_files)
        
        # 第四步：下载所有XBRL文件
        results = self.download_all_xbrl_files(all_filings)
        
        # 打印最终结果
        self.print_final_results(results)
        
        return results
    
    def print_final_results(self, results: Dict[str, bool]):
        """打印最终结果"""
        print("\n" + "=" * 60)
        print("下载任务完成！")
        print("=" * 60)
        print(f"完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        successful_count = sum(1 for success in results.values() if success)
        total_count = len(results)
        
        print(f"总公司数: {total_count}")
        print(f"成功下载: {successful_count}")
        print(f"下载失败: {total_count - successful_count}")
        print(f"成功率: {successful_count/total_count*100:.1f}%")
        
        print("\n详细结果:")
        for ticker, success in results.items():
            status_icon = "✅" if success else "❌"
            print(f"  {status_icon} {ticker}: {'成功' if success else '失败'}")
        
        print(f"\n数据保存位置: {os.path.abspath(self.output_dir)}")


def main():
    """主函数"""
    try:
        downloader = OptimizedMagnificentSevenDownloader()
        results = downloader.download_magnificent_seven_optimized(max_quarters=40)
        
        # 检查是否有成功的下载
        successful_count = sum(1 for success in results.values() if success)
        
        if successful_count > 0:
            print(f"\n🎉 成功下载了 {successful_count} 家公司的10-K数据！")
        else:
            print("\n😞 没有成功下载任何数据，请检查网络连接和配置。")
            
    except KeyboardInterrupt:
        print("\n\n用户中断了下载任务")
    except Exception as e:
        print(f"\n程序执行出错: {e}")


if __name__ == "__main__":
    main()
