"""
上下文分析器 - 分析XBRL文档中的上下文信息
"""

import re
from datetime import date, datetime
from typing import List, Optional, Dict, Any
from xml.etree.ElementTree import Element
from .models import ContextInfo


class ContextAnalyzer:
    """XBRL上下文分析器"""
    
    def __init__(self, reporting_year: int):
        """
        初始化上下文分析器
        
        Args:
            reporting_year: 报告年份，用于判断当年期间
        """
        self.reporting_year = reporting_year
        
        # XBRL命名空间定义
        self.namespaces = {
            'xbrli': 'http://www.xbrl.org/2003/instance',
            'xbrldi': 'http://xbrl.org/2006/xbrldi',
            'link': 'http://www.xbrl.org/2003/linkbase',
            'xlink': 'http://www.w3.org/1999/xlink'
        }
    
    def analyze_contexts(self, root: Element) -> List[ContextInfo]:
        """
        分析所有上下文
        
        Args:
            root: XML根元素
            
        Returns:
            上下文信息列表
        """
        contexts = []
        
        # 查找所有context元素
        for context_elem in root.findall('.//xbrli:context', self.namespaces):
            context_info = self._parse_context(context_elem)
            if context_info and self._is_current_year_context(context_info):
                contexts.append(context_info)
        
        return contexts
    
    def _parse_context(self, context_elem: Element) -> Optional[ContextInfo]:
        """
        解析单个上下文元素
        
        Args:
            context_elem: 上下文XML元素
            
        Returns:
            上下文信息对象
        """
        try:
            context_id = context_elem.get('id')
            if not context_id:
                return None
            
            # 获取实体信息
            entity_elem = context_elem.find('.//xbrli:entity', self.namespaces)
            if entity_elem is None:
                return None
            
            identifier_elem = entity_elem.find('.//xbrli:identifier', self.namespaces)
            if identifier_elem is None:
                return None
            
            entity_identifier = identifier_elem.text
            
            # 解析期间信息
            period_elem = context_elem.find('.//xbrli:period', self.namespaces)
            if period_elem is None:
                return None
            
            period_type, start_date, end_date, instant_date = self._parse_period(period_elem)
            
            # 解析维度信息
            dimensions = self._parse_dimensions(entity_elem)
            
            return ContextInfo(
                context_id=context_id,
                entity_identifier=entity_identifier,
                period_type=period_type,
                start_date=start_date,
                end_date=end_date,
                instant_date=instant_date,
                dimensions=dimensions
            )
            
        except Exception as e:
            print(f"解析上下文时发生错误: {e}")
            return None
    
    def _parse_period(self, period_elem: Element) -> tuple:
        """
        解析期间信息
        
        Args:
            period_elem: 期间XML元素
            
        Returns:
            (period_type, start_date, end_date, instant_date)
        """
        instant_elem = period_elem.find('.//xbrli:instant', self.namespaces)
        if instant_elem is not None:
            instant_date = self._parse_date(instant_elem.text)
            return 'instant', None, None, instant_date
        
        start_elem = period_elem.find('.//xbrli:startDate', self.namespaces)
        end_elem = period_elem.find('.//xbrli:endDate', self.namespaces)
        
        if start_elem is not None and end_elem is not None:
            start_date = self._parse_date(start_elem.text)
            end_date = self._parse_date(end_elem.text)
            return 'duration', start_date, end_date, None
        
        return 'unknown', None, None, None
    
    def _parse_dimensions(self, entity_elem: Element) -> List[Dict[str, str]]:
        """
        解析维度信息
        
        Args:
            entity_elem: 实体XML元素
            
        Returns:
            维度信息列表
        """
        dimensions = []
        
        segment_elem = entity_elem.find('.//xbrli:segment', self.namespaces)
        if segment_elem is not None:
            for member_elem in segment_elem.findall('.//xbrldi:explicitMember', self.namespaces):
                dimension_attr = member_elem.get('dimension')
                member_value = member_elem.text
                
                if dimension_attr and member_value:
                    dimensions.append({
                        'dimension': dimension_attr,
                        'member': member_value
                    })
        
        return dimensions
    
    def _parse_date(self, date_str: str) -> Optional[date]:
        """
        解析日期字符串
        
        Args:
            date_str: 日期字符串
            
        Returns:
            日期对象
        """
        if not date_str:
            return None
        
        try:
            # 处理YYYY-MM-DD格式
            return datetime.strptime(date_str.strip(), '%Y-%m-%d').date()
        except ValueError:
            try:
                # 处理其他可能的日期格式
                return datetime.strptime(date_str.strip(), '%Y-%m-%dT%H:%M:%S').date()
            except ValueError:
                print(f"无法解析日期: {date_str}")
                return None
    
    def _is_current_year_context(self, context: ContextInfo) -> bool:
        """
        判断是否为当年的上下文
        
        Args:
            context: 上下文信息
            
        Returns:
            是否为当年上下文
        """
        if context.period_type == 'instant':
            if context.instant_date:
                return context.instant_date.year == self.reporting_year
        
        elif context.period_type == 'duration':
            if context.end_date:
                # 如果结束日期是当年，认为是当年数据
                return context.end_date.year == self.reporting_year
            elif context.start_date:
                # 如果开始日期是当年，也可能是当年数据
                return context.start_date.year == self.reporting_year
        
        return False
    
    def get_annual_contexts(self, contexts: List[ContextInfo]) -> List[ContextInfo]:
        """
        获取年度上下文（非季度数据）
        
        Args:
            contexts: 所有上下文列表
            
        Returns:
            年度上下文列表
        """
        annual_contexts = []
        
        for context in contexts:
            if context.period_type == 'duration' and context.start_date and context.end_date:
                # 计算期间长度，年度数据通常超过300天
                duration = (context.end_date - context.start_date).days
                if duration > 300:  # 年度数据
                    annual_contexts.append(context)
            elif context.period_type == 'instant':
                # 即时数据通常是年末数据
                annual_contexts.append(context)
        
        return annual_contexts
