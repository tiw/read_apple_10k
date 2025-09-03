"""
数据模型定义
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from datetime import date


@dataclass
class CompanyInfo:
    """公司信息"""
    name: str
    cik: str
    ticker: Optional[str] = None
    industry: Optional[str] = None


@dataclass
class ContextInfo:
    """上下文信息"""
    context_id: str
    entity_identifier: str
    period_type: str  # 'instant' or 'duration'
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    instant_date: Optional[date] = None
    dimensions: List[Dict[str, str]] = None
    
    def __post_init__(self):
        if self.dimensions is None:
            self.dimensions = []


@dataclass
class FactInfo:
    """事实数据信息"""
    tag_name: str
    namespace: str
    context_id: str
    value: str
    unit: Optional[str] = None
    decimals: Optional[int] = None
    precision: Optional[int] = None
    
    @property
    def qualified_name(self) -> str:
        """获取完全限定名"""
        return f"{self.namespace}:{self.tag_name}" if self.namespace else self.tag_name


@dataclass
class XBRLDocument:
    """XBRL文档信息"""
    file_path: str
    company: CompanyInfo
    reporting_year: int
    fiscal_period: Optional[str] = None
    period_end_date: Optional[date] = None
    contexts: List[ContextInfo] = None
    facts: List[FactInfo] = None
    
    def __post_init__(self):
        if self.contexts is None:
            self.contexts = []
        if self.facts is None:
            self.facts = []
