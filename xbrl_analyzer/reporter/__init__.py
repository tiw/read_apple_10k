"""
XBRL年报生成器模块

提供基于DuckDB数据的10-K年报生成功能，包括：
- 财务报表数据提取
- 财务指标计算
- 年报报告生成
"""

from .report_generator import AnnualReportGenerator
from .financial_calculator import FinancialCalculator
from .duckdb_interface import DuckDBInterface
from .report_templates import ReportTemplates
from .financial_concepts import FinancialConcepts, CalculatedMetrics

__all__ = [
    'AnnualReportGenerator',
    'FinancialCalculator', 
    'DuckDBInterface',
    'ReportTemplates',
    'FinancialConcepts',
    'CalculatedMetrics'
]

__version__ = '1.0.0'
