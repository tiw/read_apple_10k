import argparse
import json
import os
import re
import sys

import requests


# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from xbrl_analyzer.tools.ticker_utils import get_cik_by_ticker


def download_xbrl_files(ticker: str, year=None, output_dir: str = "./10k_xbrl"):
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
        print(f"找到{'最新的' if year is None else str(year) + '年的'}10-K文件: "
              f"{accession_number} (报告日期: {report_date})")
        
        # 构建文件URL
        formatted_accession = accession_number.replace("-", "")
        base_url = (f"https://www.sec.gov/Archives/edgar/data/"
                   f"{int(cik)}/{formatted_accession}")
        
        # 首先尝试使用MetaLinks.json获取确切的文件名
        files_to_download = []
        meta_links_url = f"{base_url}/MetaLinks.json"
        
        try:
            print(f"正在获取MetaLinks.json: {meta_links_url}")
            meta_response = requests.get(meta_links_url, headers=headers, timeout=30)
            meta_response.raise_for_status()
            meta_data = meta_response.json()
            
            # 从MetaLinks.json中获取实例文档
            instance_files = meta_data.get('instance', {})
            for filename in instance_files.keys():
                # 将.htm文件转换为_htm.xml格式
                if filename.endswith('.htm'):
                    xml_filename = filename.replace('.htm', '_htm.xml')
                    files_to_download.append(xml_filename)
                else:
                    files_to_download.append(filename)
            
            # 获取其他链接库文件
            presentation_files = meta_data.get('presentation', {}).keys()
            files_to_download.extend(presentation_files)
            
            calculation_files = meta_data.get('calculation', {}).keys()
            files_to_download.extend(calculation_files)
            
            definition_files = meta_data.get('definition', {}).keys()
            files_to_download.extend(definition_files)
            
            label_files = meta_data.get('label', {}).keys()
            files_to_download.extend(label_files)
            
            # 获取schema文件
            schema_files = meta_data.get('schema', {}).keys()
            files_to_download.extend(schema_files)
            
            print(f"从MetaLinks.json获取到 {len(files_to_download)} 个文件")
            
            # 检查是否获取到关键文件
            instance_files_count = len([f for f in files_to_download if '_htm.xml' in f])
            if instance_files_count == 0:
                print("警告: 未找到实例文档文件")
                
        except requests.exceptions.RequestException as e:
            print(f"网络错误，无法获取MetaLinks.json: {e}")
            print("尝试直接从目录中解析文件...")
            
            # 直接从目录中获取文件列表
            try:
                directory_url = f"{base_url}/"
                directory_response = requests.get(directory_url, headers=headers, timeout=30)
                directory_response.raise_for_status()
                directory_content = directory_response.text
                
                # 通过解析HTML目录内容获取文件链接
                import re
                # 匹配XBRL相关文件
                file_patterns = [
                    rf'({ticker.lower()}-\d{{8}}\.xsd)',
                    rf'({ticker.lower()}-\d{{8}}_cal\.xml)',
                    rf'({ticker.lower()}-\d{{8}}_def\.xml)',
                    rf'({ticker.lower()}-\d{{8}}_lab\.xml)',
                    rf'({ticker.lower()}-\d{{8}}_pre\.xml)',
                    rf'({ticker.lower()}-\d{{8}}\.xml)',  # 实例文档
                    rf'({ticker.lower()}_\d{{8}}\.xsd)',
                    rf'({ticker.lower()}_\d{{8}}_cal\.xml)',
                    rf'({ticker.lower()}_\d{{8}}_def\.xml)',
                    rf'({ticker.lower()}_\d{{8}}_lab\.xml)',
                    rf'({ticker.lower()}_\d{{8}}_pre\.xml)',
                    rf'({ticker.lower()}_\d{{8}}\.xml)',  # 实例文档
                ]
                
                files_found = []
                for pattern in file_patterns:
                    matches = re.findall(pattern, directory_content, re.IGNORECASE)
                    files_found.extend(matches)
                
                # 去重
                files_to_download = list(set(files_found))
                print(f"从目录中找到 {len(files_to_download)} 个文件")
                
            except Exception as dir_error:
                print(f"从目录中解析文件也失败了: {dir_error}")
                return False
                
        except json.JSONDecodeError as e:
            print(f"JSON解析错误，MetaLinks.json格式不正确: {e}")
            return False
        except Exception as e:
            print(f"处理MetaLinks.json时发生未知错误: {e}")
            return False
        
        # 下载文件
        downloaded_files = []
        for filename in files_to_download:
            file_url = f"{base_url}/{filename}"
            output_path = os.path.join(output_dir, filename)
            
            print(f"正在下载 {file_url}")
            try:
                file_response = requests.get(file_url, headers=headers, timeout=30)
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
    parser.add_argument("--output-dir", default="./10k_xbrl", 
                       help="输出目录 (默认: ./10k_xbrl)")
    
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