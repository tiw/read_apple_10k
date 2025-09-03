"""
XBRL解析器主模块 - 高效解析10K报告文件
"""

import os
import re
from pathlib import Path
from datetime import date, datetime
from typing import Optional, List, Dict, Any
from xml.etree import ElementTree as ET

from .models import CompanyInfo, XBRLDocument
from .context_analyzer import ContextAnalyzer
from .fact_extractor import FactExtractor


class XBRLParser:
    """高效的XBRL 10K报告解析器"""
    
    def __init__(self):
        """初始化解析器"""
        # DEI命名空间定义（不同年份）
        self.dei_namespaces = [
            'http://xbrl.sec.gov/dei/2024',
            'http://xbrl.sec.gov/dei/2023',
            'http://xbrl.sec.gov/dei/2022',
            'http://xbrl.sec.gov/dei/2021',
            'http://xbrl.sec.gov/dei/2020',
            'http://xbrl.sec.gov/dei/2019',
            'http://xbrl.sec.gov/dei/2018',
            'http://xbrl.sec.gov/dei/2017',
            'http://xbrl.sec.gov/dei/2016',
            'http://xbrl.sec.gov/dei/2015',
            'http://xbrl.sec.gov/dei/2014-01-31'
        ]
        
        # XBRL实例命名空间
        self.xbrli_namespace = 'http://www.xbrl.org/2003/instance'
    
    def parse_file(self, file_path: str) -> Optional[XBRLDocument]:
        """
        解析XBRL文件
        
        Args:
            file_path: XBRL文件路径
            
        Returns:
            解析后的XBRL文档对象
        """
        try:
            print(f"开始解析文件: {file_path}")
            
            # 使用iterparse进行内存高效的解析
            root = self._parse_xml_efficiently(file_path)
            if root is None:
                return None
            
            # 提取公司基本信息
            company_info = self._extract_company_info(root)
            if not company_info:
                print("无法提取公司信息")
                return None
            
            # 提取报告年份
            reporting_year = self._extract_reporting_year(root, file_path)
            if not reporting_year:
                print("无法确定报告年份")
                return None
            
            print(f"公司: {company_info.name}, 报告年份: {reporting_year}")
            
            # 分析上下文
            context_analyzer = ContextAnalyzer(reporting_year)
            contexts = context_analyzer.analyze_contexts(root)
            
            print(f"找到 {len(contexts)} 个当年相关的上下文")
            
            # 提取事实数据
            fact_extractor = FactExtractor(contexts)
            facts = fact_extractor.extract_facts(root)
            
            print(f"提取了 {len(facts)} 条事实数据")
            
            # 获取期末日期和财政期间
            period_end_date, fiscal_period = self._extract_period_info(root)
            
            # 创建文档对象
            xbrl_doc = XBRLDocument(
                file_path=file_path,
                company=company_info,
                reporting_year=reporting_year,
                fiscal_period=fiscal_period,
                period_end_date=period_end_date,
                contexts=contexts,
                facts=facts
            )
            
            print(f"解析完成: {len(facts)} 条事实数据，{len(contexts)} 个上下文")
            return xbrl_doc
            
        except Exception as e:
            print(f"解析文件时发生错误: {e}")
            return None
    
    def _parse_xml_efficiently(self, file_path: str) -> Optional[ET.Element]:
        """
        高效解析XML文件
        
        Args:
            file_path: XML文件路径
            
        Returns:
            XML根元素
        """
        try:
            # 对于大文件，使用iterparse进行流式解析
            file_size = os.path.getsize(file_path)
            
            if file_size > 50 * 1024 * 1024:  # 50MB以上的大文件
                return self._parse_large_xml(file_path)
            else:
                # 小文件直接解析
                tree = ET.parse(file_path)
                return tree.getroot()
                
        except ET.ParseError as e:
            print(f"XML解析错误: {e}")
            return None
        except Exception as e:
            print(f"文件读取错误: {e}")
            return None
    
    def _parse_large_xml(self, file_path: str) -> Optional[ET.Element]:
        """
        解析大型XML文件
        
        Args:
            file_path: XML文件路径
            
        Returns:
            XML根元素
        """
        try:
            # 使用iterparse避免将整个文件加载到内存
            context = ET.iterparse(file_path, events=('start', 'end'))
            context = iter(context)
            event, root = next(context)
            
            # 处理大文件时清理已处理的元素以节省内存
            for event, elem in context:
                if event == 'end':
                    # 在某些情况下清理元素以节省内存
                    # 但保留我们需要的结构
                    pass
            
            return root
            
        except Exception as e:
            print(f"大文件解析错误: {e}")
            return None
    
    def _extract_company_info(self, root: ET.Element) -> Optional[CompanyInfo]:
        """
        提取公司基本信息
        
        Args:
            root: XML根元素
            
        Returns:
            公司信息对象
        """
        try:
            company_name = None
            cik = None
            ticker = None
            
            # 尝试从不同的DEI命名空间中提取信息
            for dei_ns in self.dei_namespaces:
                if company_name and cik:
                    break
                
                # 提取公司名称
                if not company_name:
                    name_elem = root.find(f'.//{{{dei_ns}}}EntityRegistrantName')
                    if name_elem is not None and name_elem.text:
                        company_name = name_elem.text.strip()
                
                # 提取CIK
                if not cik:
                    cik_elem = root.find(f'.//{{{dei_ns}}}EntityCentralIndexKey')
                    if cik_elem is not None and cik_elem.text:
                        cik = cik_elem.text.strip()
                
                # 提取股票代码
                if not ticker:
                    ticker_elem = root.find(f'.//{{{dei_ns}}}EntityTradingSymbol')
                    if ticker_elem is not None and ticker_elem.text:
                        ticker = ticker_elem.text.strip()
            
            # 如果从DEI中找不到，尝试从实体标识符中提取CIK
            if not cik:
                identifier_elem = root.find(f'.//{{{self.xbrli_namespace}}}identifier')
                if identifier_elem is not None and identifier_elem.text:
                    cik = identifier_elem.text.strip()
            
            if company_name or cik:
                return CompanyInfo(
                    name=company_name or "Unknown",
                    cik=cik or "Unknown",
                    ticker=ticker
                )
            
            return None
            
        except Exception as e:
            print(f"提取公司信息时发生错误: {e}")
            return None
    
    def _extract_reporting_year(self, root: ET.Element, file_path: str) -> Optional[int]:
        """
        提取报告年份
        
        Args:
            root: XML根元素
            file_path: 文件路径
            
        Returns:
            报告年份
        """
        try:
            # 首先尝试从文档中提取财政年份
            for dei_ns in self.dei_namespaces:
                fiscal_year_elem = root.find(f'.//{{{dei_ns}}}DocumentFiscalYearFocus')
                if fiscal_year_elem is not None and fiscal_year_elem.text:
                    try:
                        return int(fiscal_year_elem.text.strip())
                    except ValueError:
                        continue
            
            # 尝试从期末日期推断
            for dei_ns in self.dei_namespaces:
                period_end_elem = root.find(f'.//{{{dei_ns}}}DocumentPeriodEndDate')
                if period_end_elem is not None and period_end_elem.text:
                    try:
                        end_date = datetime.strptime(period_end_elem.text.strip(), '%Y-%m-%d')
                        return end_date.year
                    except ValueError:
                        continue
            
            # 从文件名中提取年份
            filename = os.path.basename(file_path)
            year_match = re.search(r'(\d{4})', filename)
            if year_match:
                return int(year_match.group(1))
            
            # 从文件路径中提取年份
            path_year_match = re.search(r'/(\d{4})\d{4}/', file_path)
            if path_year_match:
                year = int(path_year_match.group(1))
                # 验证年份合理性
                current_year = datetime.now().year
                if 2000 <= year <= current_year:
                    return year
            
            return None
            
        except Exception as e:
            print(f"提取报告年份时发生错误: {e}")
            return None
    
    def _extract_period_info(self, root: ET.Element) -> tuple:
        """
        提取期间信息
        
        Args:
            root: XML根元素
            
        Returns:
            (period_end_date, fiscal_period) 元组
        """
        period_end_date = None
        fiscal_period = None
        
        try:
            # 提取期末日期
            for dei_ns in self.dei_namespaces:
                period_end_elem = root.find(f'.//{{{dei_ns}}}DocumentPeriodEndDate')
                if period_end_elem is not None and period_end_elem.text:
                    try:
                        period_end_date = datetime.strptime(
                            period_end_elem.text.strip(), '%Y-%m-%d'
                        ).date()
                        break
                    except ValueError:
                        continue
            
            # 提取财政期间
            for dei_ns in self.dei_namespaces:
                fiscal_period_elem = root.find(f'.//{{{dei_ns}}}DocumentFiscalPeriodFocus')
                if fiscal_period_elem is not None and fiscal_period_elem.text:
                    fiscal_period = fiscal_period_elem.text.strip()
                    break
            
        except Exception as e:
            print(f"提取期间信息时发生错误: {e}")
        
        return period_end_date, fiscal_period
    
    def get_parser_stats(self, xbrl_doc: XBRLDocument) -> Dict[str, Any]:
        """
        获取解析统计信息
        
        Args:
            xbrl_doc: XBRL文档对象
            
        Returns:
            统计信息字典
        """
        if not xbrl_doc:
            return {}
        
        # 统计命名空间分布
        namespace_stats = {}
        for fact in xbrl_doc.facts:
            ns = fact.namespace or 'unknown'
            namespace_stats[ns] = namespace_stats.get(ns, 0) + 1
        
        # 统计上下文类型
        context_types = {}
        for context in xbrl_doc.contexts:
            context_types[context.period_type] = context_types.get(context.period_type, 0) + 1
        
        return {
            'company_name': xbrl_doc.company.name,
            'company_cik': xbrl_doc.company.cik,
            'reporting_year': xbrl_doc.reporting_year,
            'total_facts': len(xbrl_doc.facts),
            'total_contexts': len(xbrl_doc.contexts),
            'namespace_distribution': namespace_stats,
            'context_type_distribution': context_types,
            'has_annual_data': any(
                ctx.period_type == 'duration' and 
                ctx.start_date and ctx.end_date and 
                (ctx.end_date - ctx.start_date).days > 300 
                for ctx in xbrl_doc.contexts
            )
        }
