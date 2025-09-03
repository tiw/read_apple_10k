"""
XBRL数据验证模块
提供多层次的数据交叉验证功能
"""

from .data_validator import XBRLDataValidator, ValidationResult
from .sec_cross_validator import SECCrossValidator
from .historical_validator import HistoricalValidator, TrendAnalysis
from .validation_orchestrator import ValidationOrchestrator

__all__ = [
    'XBRLDataValidator',
    'ValidationResult', 
    'SECCrossValidator',
    'HistoricalValidator',
    'TrendAnalysis',
    'ValidationOrchestrator'
]

__version__ = "1.0.0"
__author__ = "XBRL Analyzer Team"
__description__ = "XBRL财务数据交叉验证框架"