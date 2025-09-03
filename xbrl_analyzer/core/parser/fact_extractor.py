"""
事实数据提取器 - 从XBRL文档中提取财务数据
"""

import re
from typing import List, Set, Dict, Any
from xml.etree.ElementTree import Element
from .models import FactInfo, ContextInfo


class FactExtractor:
    """XBRL事实数据提取器"""
    
    def __init__(self, contexts: List[ContextInfo]):
        """
        初始化事实提取器
        
        Args:
            contexts: 有效的上下文列表
        """
        self.contexts = contexts
        self.context_ids = {ctx.context_id for ctx in contexts}
        
        # 常见的命名空间映射
        self.namespace_prefixes = {
            'us-gaap': 'http://fasb.org/us-gaap/',
            'dei': 'http://xbrl.sec.gov/dei/',
            'country': 'http://xbrl.sec.gov/country/',
            'currency': 'http://www.xbrl.org/2003/iso4217',
            'xbrli': 'http://www.xbrl.org/2003/instance'
        }
    
    def extract_facts(self, root: Element) -> List[FactInfo]:
        """
        从XML根元素中提取所有事实数据
        
        Args:
            root: XML根元素
            
        Returns:
            事实信息列表
        """
        facts = []
        
        # 遍历所有元素，查找包含contextRef属性的元素
        for elem in root.iter():
            if 'contextRef' in elem.attrib:
                fact_info = self._extract_fact_from_element(elem)
                if fact_info and fact_info.context_id in self.context_ids:
                    facts.append(fact_info)
        
        return facts
    
    def _extract_fact_from_element(self, elem: Element) -> FactInfo:
        """
        从XML元素中提取事实信息
        
        Args:
            elem: XML元素
            
        Returns:
            事实信息对象
        """
        try:
            # 获取上下文引用
            context_ref = elem.attrib.get('contextRef')
            if not context_ref:
                return None
            
            # 解析标签名和命名空间
            tag_name, namespace = self._parse_tag_name(elem.tag)
            if not tag_name:
                return None
            
            # 获取值
            value = elem.text if elem.text else ""
            
            # 获取其他属性
            unit = elem.attrib.get('unitRef', '')
            decimals = self._parse_int_attribute(elem.attrib.get('decimals'))
            precision = self._parse_int_attribute(elem.attrib.get('precision'))
            
            return FactInfo(
                tag_name=tag_name,
                namespace=namespace,
                context_id=context_ref,
                value=value,
                unit=unit,
                decimals=decimals,
                precision=precision
            )
            
        except Exception as e:
            print(f"提取事实数据时发生错误: {e}")
            return None
    
    def _parse_tag_name(self, full_tag: str) -> tuple:
        """
        解析完整标签名，提取标签名和命名空间
        
        Args:
            full_tag: 完整标签名
            
        Returns:
            (tag_name, namespace) 元组
        """
        if full_tag.startswith('{'):
            # 处理 {namespace}tagname 格式
            match = re.match(r'\{([^}]+)\}(.+)', full_tag)
            if match:
                namespace_uri, tag_name = match.groups()
                namespace = self._uri_to_prefix(namespace_uri)
                return tag_name, namespace
        elif ':' in full_tag:
            # 处理 prefix:tagname 格式
            parts = full_tag.split(':', 1)
            if len(parts) == 2:
                return parts[1], parts[0]
        
        # 如果没有命名空间，返回原标签名
        return full_tag, ''
    
    def _uri_to_prefix(self, namespace_uri: str) -> str:
        """
        将命名空间URI转换为前缀
        
        Args:
            namespace_uri: 命名空间URI
            
        Returns:
            命名空间前缀
        """
        # 检查已知的命名空间映射
        for prefix, uri_pattern in self.namespace_prefixes.items():
            if namespace_uri.startswith(uri_pattern):
                return prefix
        
        # 尝试从URI中提取有意义的前缀
        if 'fasb.org/us-gaap' in namespace_uri:
            return 'us-gaap'
        elif 'xbrl.sec.gov/dei' in namespace_uri:
            return 'dei'
        elif 'apple.com' in namespace_uri:
            return 'aapl'
        elif 'amazon.com' in namespace_uri:
            return 'amzn'
        elif 'microsoft.com' in namespace_uri:
            return 'msft'
        elif 'google.com' in namespace_uri or 'alphabet.com' in namespace_uri:
            return 'googl'
        elif 'meta.com' in namespace_uri or 'facebook.com' in namespace_uri:
            return 'meta'
        elif 'tesla.com' in namespace_uri:
            return 'tsla'
        elif 'nvidia.com' in namespace_uri:
            return 'nvda'
        
        # 如果无法识别，返回原URI的简化版本
        return namespace_uri.split('/')[-1] if '/' in namespace_uri else namespace_uri
    
    def _parse_int_attribute(self, attr_value: str) -> int:
        """
        解析整数属性值
        
        Args:
            attr_value: 属性值字符串
            
        Returns:
            整数值或None
        """
        if not attr_value:
            return None
        
        try:
            return int(attr_value)
        except ValueError:
            return None
    
    def filter_facts_by_namespace(self, facts: List[FactInfo], namespaces: List[str]) -> List[FactInfo]:
        """
        按命名空间过滤事实数据
        
        Args:
            facts: 事实数据列表
            namespaces: 要包含的命名空间列表
            
        Returns:
            过滤后的事实数据列表
        """
        return [fact for fact in facts if fact.namespace in namespaces]
    
    def filter_facts_by_tag_pattern(self, facts: List[FactInfo], pattern: str) -> List[FactInfo]:
        """
        按标签名模式过滤事实数据
        
        Args:
            facts: 事实数据列表
            pattern: 正则表达式模式
            
        Returns:
            过滤后的事实数据列表
        """
        compiled_pattern = re.compile(pattern, re.IGNORECASE)
        return [fact for fact in facts if compiled_pattern.search(fact.tag_name)]
    
    def get_fact_summary(self, facts: List[FactInfo]) -> Dict[str, Any]:
        """
        获取事实数据摘要统计
        
        Args:
            facts: 事实数据列表
            
        Returns:
            统计摘要字典
        """
        if not facts:
            return {}
        
        namespaces = {}
        contexts = set()
        tags = set()
        
        for fact in facts:
            # 统计命名空间
            if fact.namespace in namespaces:
                namespaces[fact.namespace] += 1
            else:
                namespaces[fact.namespace] = 1
            
            # 收集上下文和标签
            contexts.add(fact.context_id)
            tags.add(fact.tag_name)
        
        return {
            'total_facts': len(facts),
            'unique_contexts': len(contexts),
            'unique_tags': len(tags),
            'namespaces': namespaces,
            'context_ids': sorted(list(contexts)),
            'sample_tags': sorted(list(tags))[:20]  # 显示前20个标签作为示例
        }
