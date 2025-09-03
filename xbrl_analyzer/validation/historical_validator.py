#!/usr/bin/env python3
"""
历史数据趋势验证器
通过历史数据趋势验证当前数据的合理性
"""

import logging
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass
import statistics
import math

logger = logging.getLogger(__name__)


@dataclass
class TrendAnalysis:
    """趋势分析结果"""
    concept: str
    current_value: float
    historical_values: List[float]
    growth_rate: float
    volatility: float
    z_score: float  # 当前值相对于历史分布的Z分数
    is_outlier: bool
    trend_direction: str  # 'increasing', 'decreasing', 'stable'
    confidence_level: float  # 对趋势判断的置信度


class HistoricalValidator:
    """历史数据趋势验证器"""
    
    def __init__(self, outlier_threshold: float = 2.5, min_historical_years: int = 3):
        """
        初始化历史验证器
        
        Args:
            outlier_threshold: 异常值检测阈值（标准差倍数）
            min_historical_years: 最少历史年数
        """
        self.outlier_threshold = outlier_threshold
        self.min_historical_years = min_historical_years
        
        # 定义合理的财务指标变化范围
        self.reasonable_changes = {
            'RevenueFromContractWithCustomerExcludingAssessedTax': {
                'max_growth': 0.50,    # 最大50%增长
                'max_decline': -0.30,  # 最大30%下降
                'volatility_threshold': 0.20  # 波动阈值
            },
            'NetIncomeLoss': {
                'max_growth': 1.00,    # 最大100%增长
                'max_decline': -0.50,  # 最大50%下降
                'volatility_threshold': 0.30
            },
            'Assets': {
                'max_growth': 0.30,    # 最大30%增长
                'max_decline': -0.10,  # 最大10%下降
                'volatility_threshold': 0.15
            },
            'Liabilities': {
                'max_growth': 0.40,    # 最大40%增长
                'max_decline': -0.20,  # 最大20%下降
                'volatility_threshold': 0.25
            },
            'StockholdersEquity': {
                'max_growth': 0.50,    # 最大50%增长
                'max_decline': -0.30,  # 最大30%下降
                'volatility_threshold': 0.25
            }
        }
    
    def validate_historical_trends(self, current_data: Dict[str, Any], 
                                  historical_data: List[Dict[str, Any]]) -> Dict[str, TrendAnalysis]:
        """
        验证历史趋势的合理性
        
        Args:
            current_data: 当前年度财务数据
            historical_data: 历史财务数据列表（按时间倒序）
            
        Returns:
            各指标的趋势分析结果
        """
        logger.info("开始历史趋势验证...")
        
        trend_analyses = {}
        
        # 确保有足够的历史数据
        if len(historical_data) < self.min_historical_years:
            logger.warning(f"历史数据不足，只有 {len(historical_data)} 年数据")
            return trend_analyses
        
        # 对每个关键指标进行趋势分析
        key_concepts = list(self.reasonable_changes.keys())
        
        for concept in key_concepts:
            try:
                # 获取当前值
                current_value = self._extract_value(current_data, concept)
                if current_value is None:
                    continue
                
                # 提取历史值
                historical_values = []
                for year_data in historical_data:
                    value = self._extract_value(year_data, concept)
                    if value is not None:
                        historical_values.append(value)
                
                if len(historical_values) < self.min_historical_years:
                    continue
                
                # 执行趋势分析
                analysis = self._analyze_trend(concept, current_value, historical_values)
                trend_analyses[concept] = analysis
                
                logger.info(f"{concept}: 当前值={current_value:,.0f}, 增长率={analysis.growth_rate:.1%}, "
                           f"Z分数={analysis.z_score:.2f}, 异常值={analysis.is_outlier}")
                
            except Exception as e:
                logger.error(f"分析 {concept} 趋势时出错: {e}")
                continue
        
        return trend_analyses
    
    def _analyze_trend(self, concept: str, current_value: float, 
                      historical_values: List[float]) -> TrendAnalysis:
        """分析单个指标的趋势"""
        # 计算增长率（与最近一年相比）
        previous_value = historical_values[0]
        growth_rate = (current_value - previous_value) / abs(previous_value) if previous_value != 0 else 0
        
        # 计算历史波动率
        if len(historical_values) >= 2:
            historical_growth_rates = []
            for i in range(len(historical_values) - 1):
                val1 = historical_values[i]
                val2 = historical_values[i + 1]
                if val2 != 0:
                    rate = (val1 - val2) / abs(val2)
                    historical_growth_rates.append(rate)
            
            volatility = statistics.stdev(historical_growth_rates) if len(historical_growth_rates) > 1 else 0
        else:
            volatility = 0
        
        # 计算Z分数
        if len(historical_values) >= 3:
            mean_val = statistics.mean(historical_values)
            stdev_val = statistics.stdev(historical_values) if len(historical_values) > 1 else 1
            
            if stdev_val > 0:
                z_score = (current_value - mean_val) / stdev_val
            else:
                z_score = 0
        else:
            z_score = 0
        
        # 判断是否为异常值
        is_outlier = abs(z_score) > self.outlier_threshold
        
        # 判断趋势方向
        trend_direction = self._determine_trend_direction(historical_values)
        
        # 计算置信度
        confidence_level = self._calculate_confidence_level(
            growth_rate, volatility, len(historical_values)
        )
        
        return TrendAnalysis(
            concept=concept,
            current_value=current_value,
            historical_values=historical_values,
            growth_rate=growth_rate,
            volatility=volatility,
            z_score=z_score,
            is_outlier=is_outlier,
            trend_direction=trend_direction,
            confidence_level=confidence_level
        )
    
    def _determine_trend_direction(self, values: List[float]) -> str:
        """判断趋势方向"""
        if len(values) < 2:
            return 'stable'
        
        # 计算简单线性回归斜率
        n = len(values)
        x = list(range(n))
        
        sum_x = sum(x)
        sum_y = sum(values)
        sum_xy = sum(xi * yi for xi, yi in zip(x, values))
        sum_x2 = sum(xi ** 2 for xi in x)
        
        if n * sum_x2 - sum_x ** 2 == 0:
            return 'stable'
        
        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        
        if slope > 0.01:
            return 'increasing'
        elif slope < -0.01:
            return 'decreasing'
        else:
            return 'stable'
    
    def _calculate_confidence_level(self, growth_rate: float, volatility: float, 
                                  data_points: int) -> float:
        """计算趋势判断的置信度"""
        # 基于波动率和数据点数量计算置信度
        volatility_penalty = min(volatility * 2, 0.5)  # 波动率惩罚
        data_bonus = min(data_points * 0.1, 0.3)      # 数据点奖励
        
        confidence = 0.5 + data_bonus - volatility_penalty
        return max(0.1, min(1.0, confidence))
    
    def validate_reasonableness(self, trend_analyses: Dict[str, TrendAnalysis]) -> List[str]:
        """验证趋势的合理性并返回问题列表"""
        issues = []
        
        for concept, analysis in trend_analyses.items():
            # 检查异常值
            if analysis.is_outlier:
                issues.append(
                    f"{concept} 当前值 ({analysis.current_value:,.0f}) "
                    f"偏离历史趋势 (Z分数: {analysis.z_score:.2f})"
                )
            
            # 检查增长率合理性
            if concept in self.reasonable_changes:
                rules = self.reasonable_changes[concept]
                
                if analysis.growth_rate > rules['max_growth']:
                    issues.append(
                        f"{concept} 增长率过高: {analysis.growth_rate:.1%} "
                        f"(合理范围: ≤{rules['max_growth']:.1%})"
                    )
                elif analysis.growth_rate < rules['max_decline']:
                    issues.append(
                        f"{concept} 下降过快: {analysis.growth_rate:.1%} "
                        f"(合理范围: ≥{rules['max_decline']:.1%})"
                    )
                
                # 检查波动率
                if analysis.volatility > rules['volatility_threshold']:
                    issues.append(
                        f"{concept} 历史波动率较高: {analysis.volatility:.1%} "
                        f"(阈值: ≤{rules['volatility_threshold']:.1%})"
                    )
        
        return issues
    
    def detect_financial_anomalies(self, trend_analyses: Dict[str, TrendAnalysis]) -> Dict[str, List[str]]:
        """检测财务异常模式"""
        anomalies = {
            'revenue_profit_mismatch': [],
            'asset_liability_imbalance': [],
            'cash_flow_concerns': [],
            'growth_rate_anomalies': []
        }
        
        # 收入与利润增长不匹配
        if ('RevenueFromContractWithCustomerExcludingAssessedTax' in trend_analyses and 
            'NetIncomeLoss' in trend_analyses):
            
            revenue_trend = trend_analyses['RevenueFromContractWithCustomerExcludingAssessedTax']
            profit_trend = trend_analyses['NetIncomeLoss']
            
            # 收入增长但利润下降
            if (revenue_trend.growth_rate > 0.1 and 
                profit_trend.growth_rate < -0.1):
                anomalies['revenue_profit_mismatch'].append(
                    f"收入增长{revenue_trend.growth_rate:.1%}但利润下降{profit_trend.growth_rate:.1%}"
                )
        
        # 资产负债增长异常
        if ('Assets' in trend_analyses and 'Liabilities' in trend_analyses):
            asset_trend = trend_analyses['Assets']
            liability_trend = trend_analyses['Liabilities']
            
            # 负债增长远快于资产增长
            if (liability_trend.growth_rate > asset_trend.growth_rate + 0.2):
                anomalies['asset_liability_imbalance'].append(
                    f"负债增长({liability_trend.growth_rate:.1%})远快于资产增长({asset_trend.growth_rate:.1%})"
                )
        
        # 增长率异常检测
        for concept, analysis in trend_analyses.items():
            if abs(analysis.growth_rate) > 0.5:  # 50%以上的变化
                anomalies['growth_rate_anomalies'].append(
                    f"{concept} 异常增长率: {analysis.growth_rate:.1%}"
                )
        
        return anomalies
    
    def _extract_value(self, data: Dict[str, Any], concept: str) -> Optional[float]:
        """从数据字典中提取数值"""
        if concept in data:
            value = data[concept]
            if isinstance(value, dict) and 'value' in value:
                return float(value['value'])
            elif isinstance(value, (int, float)):
                return float(value)
        return None
    
    def generate_historical_validation_report(self, trend_analyses: Dict[str, TrendAnalysis],
                                           issues: List[str],
                                           anomalies: Dict[str, List[str]],
                                           company_name: str, fiscal_year: int) -> str:
        """生成历史验证报告"""
        report = []
        report.append(f"# {company_name} {fiscal_year}年度历史趋势验证报告")
        report.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # 趋势分析摘要
        report.append("## 📈 趋势分析摘要")
        for concept, analysis in trend_analyses.items():
            trend_symbol = "📈" if analysis.growth_rate > 0 else "📉" if analysis.growth_rate < 0 else "➡️"
            outlier_symbol = "⚠️" if analysis.is_outlier else "✅"
            
            report.append(
                f"{trend_symbol} {concept}: {analysis.growth_rate:+.1%} "
                f"({outlier_symbol} Z分数: {analysis.z_score:.2f})"
            )
        report.append("")
        
        # 发现的问题
        if issues:
            report.append("## ❌ 发现的问题")
            for i, issue in enumerate(issues, 1):
                report.append(f"{i}. {issue}")
            report.append("")
        
        # 财务异常模式
        if any(anomalies.values()):
            report.append("## 🚨 财务异常模式")
            
            for anomaly_type, anomaly_list in anomalies.items():
                if anomaly_list:
                    report.append(f"### {anomaly_type.replace('_', ' ').title()}")
                    for anomaly in anomaly_list:
                        report.append(f"- {anomaly}")
            report.append("")
        
        # 详细分析
        report.append("## 🔍 详细趋势分析")
        for concept, analysis in trend_analyses.items():
            report.append(f"### {concept}")
            report.append(f"- **当前值**: {analysis.current_value:,.0f}")
            report.append(f"- **增长率**: {analysis.growth_rate:+.1%}")
            report.append(f"- **历史波动率**: {analysis.volatility:.1%}")
            report.append(f"- **Z分数**: {analysis.z_score:.2f}")
            report.append(f"- **趋势方向**: {analysis.trend_direction}")
            report.append(f"- **置信度**: {analysis.confidence_level:.1%}")
            
            if analysis.is_outlier:
                report.append("- **⚠️ 标记为异常值**")
            
            report.append("")
        
        # 总结和建议
        report.append("## 📋 总结和建议")
        
        if not issues and not any(anomalies.values()):
            report.append("✅ 财务数据趋势正常，未发现明显异常")
        else:
            report.append("⚠️ 发现一些需要关注的财务模式：")
            
            if issues:
                report.append(f"- 发现 {len(issues)} 个数据趋势问题")
            
            if any(anomalies.values()):
                total_anomalies = sum(len(anomaly_list) for anomaly_list in anomalies.values())
                report.append(f"- 检测到 {total_anomalies} 个财务异常模式")
            
            report.append("")
            report.append("建议：")
            report.append("- 重点关注异常波动的财务指标")
            report.append("- 结合业务环境分析变化原因")
            report.append("- 考虑与行业平均水平对比")
        
        return "\n".join(report)


def main():
    """示例使用"""
    # 创建验证器
    validator = HistoricalValidator()
    
    # 模拟数据
    current_data = {
        'RevenueFromContractWithCustomerExcludingAssessedTax': {'value': 394328000000},
        'NetIncomeLoss': {'value': 99980000000},
        'Assets': {'value': 352583000000},
        'Liabilities': {'value': 290437000000}
    }
    
    historical_data = [
        {'RevenueFromContractWithCustomerExcludingAssessedTax': {'value': 383285000000},
         'NetIncomeLoss': {'value': 96995000000},
         'Assets': {'value': 365725000000},
         'Liabilities': {'value': 302083000000}},
        {'RevenueFromContractWithCustomerExcludingAssessedTax': {'value': 365817000000},
         'NetIncomeLoss': {'value': 94680000000},
         'Assets': {'value': 352755000000},
         'Liabilities': {'value': 287912000000}},
        {'RevenueFromContractWithCustomerExcludingAssessedTax': {'value': 394328000000},
         'NetIncomeLoss': {'value': 99980000000},
         'Assets': {'value': 352583000000},
         'Liabilities': {'value': 290437000000}}
    ]
    
    # 执行验证
    trend_analyses = validator.validate_historical_trends(current_data, historical_data)
    issues = validator.validate_reasonableness(trend_analyses)
    anomalies = validator.detect_financial_anomalies(trend_analyses)
    
    # 生成报告
    report = validator.generate_historical_validation_report(
        trend_analyses, issues, anomalies, "Apple Inc.", 2024
    )
    print(report)


if __name__ == "__main__":
    main()