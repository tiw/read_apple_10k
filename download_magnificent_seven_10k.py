#!/usr/bin/env python3
"""
下载七朵金花近10年10-K数据

使用新实现的SEC索引下载工具批量下载Magnificent Seven的10-K数据
"""

import os
import sys
import time
from datetime import datetime

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from xbrl_analyzer.tools.sec_index_downloader_tool import SECIndexDownloader


def download_magnificent_seven_10k():
    """下载七朵金花近10年10-K数据"""
    
    # 七朵金花股票代码
    magnificent_seven = [
        "AAPL",  # Apple Inc.
        "MSFT",  # Microsoft Corp.
        "GOOGL", # Alphabet Inc.
        "AMZN",  # Amazon.com Inc.
        "META",  # Meta Platforms, Inc.
        "NVDA",  # NVIDIA Corp.
        "TSLA"   # Tesla, Inc.
    ]
    
    # 计算近10年的年份范围
    current_year = datetime.now().year
    start_year = current_year - 10
    
    print("=" * 60)
    print("七朵金花近10年10-K数据下载任务")
    print("=" * 60)
    print(f"下载年份范围: {start_year} - {current_year}")
    print(f"目标公司: {', '.join(magnificent_seven)}")
    print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # 创建主输出目录
    main_output_dir = "./magnificent_seven_10k_data"
    os.makedirs(main_output_dir, exist_ok=True)
    
    # 统计信息
    total_companies = len(magnificent_seven)
    successful_downloads = 0
    failed_downloads = 0
    results = {}
    
    for i, ticker in enumerate(magnificent_seven, 1):
        print(f"\n[{i}/{total_companies}] 正在处理 {ticker}...")
        print("-" * 40)
        
        # 为每个公司创建子目录
        company_output_dir = os.path.join(main_output_dir, ticker)
        
        try:
            # 创建下载器实例
            downloader = SECIndexDownloader(output_dir=company_output_dir)
            
            # 下载近10年的数据
            success = downloader.download_10k_by_index(
                ticker=ticker,
                year=None,  # 不指定年份，下载最近的数据
                max_quarters=40  # 10年 * 4季度 = 40个季度
            )
            
            if success:
                print(f"✅ {ticker} 下载成功！")
                successful_downloads += 1
                results[ticker] = "成功"
            else:
                print(f"❌ {ticker} 下载失败！")
                failed_downloads += 1
                results[ticker] = "失败"
                
        except Exception as e:
            print(f"❌ {ticker} 下载出错: {e}")
            failed_downloads += 1
            results[ticker] = f"错误: {str(e)}"
        
        # 添加延迟，避免请求过于频繁
        if i < total_companies:
            print("等待5秒后继续...")
            time.sleep(5)
    
    # 打印最终统计结果
    print("\n" + "=" * 60)
    print("下载任务完成！")
    print("=" * 60)
    print(f"完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"总公司数: {total_companies}")
    print(f"成功下载: {successful_downloads}")
    print(f"下载失败: {failed_downloads}")
    print(f"成功率: {successful_downloads/total_companies*100:.1f}%")
    
    print("\n详细结果:")
    for ticker, status in results.items():
        status_icon = "✅" if status == "成功" else "❌"
        print(f"  {status_icon} {ticker}: {status}")
    
    print(f"\n数据保存位置: {os.path.abspath(main_output_dir)}")
    
    return results


def main():
    """主函数"""
    try:
        results = download_magnificent_seven_10k()
        
        # 检查是否有成功的下载
        successful_count = sum(1 for status in results.values() if status == "成功")
        
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
