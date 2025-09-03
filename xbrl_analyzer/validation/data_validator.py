#!/usr/bin/env python3
"""
XBRL数据交叉验证器
提供多层次的数据准确性保障机制
"""

import logging
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from dataclasses import dataclass
import re
from decimal import Decimal

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class ValidationResult:
    """验证结果"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    confidence_score: float  # 0-1之间的置信度分数


@dataclass
class ValidationMetrics:
    """验证指标"""
    total_checks: int
    passed_checks: int
    failed_checks: int
    warning_checks: int
    accuracy_score: float


class XBRLDataValidator:
    """XBRL数据交叉验证器"""
    
    def __init__(self, tolerance: float = 0.01):
        """
        初始化验证器
        
        Args:
            tolerance: 数值比较的容差范围
        """
        self.tolerance = tolerance
        self.validation_results = []
        
        # 定义关键的财务计算关系
        self.financial_relationships = {
            # 资产负债表平衡
            'balance_sheet': {
                'Assets = Liabilities + StockholdersEquity': {
                    'left': ['Assets'],
                    'right': ['Liabilities', 'StockholdersEquity'],
                    'tolerance': 0.001  # 0.1%容差
                },
                'AssetsCurrent + AssetsNoncurrent = Assets': {
                    'left': ['AssetsCurrent', 'AssetsNoncurrent'],
                    'right': ['Assets'],
                    'tolerance': 0.001
                },
                'LiabilitiesCurrent + LiabilitiesNoncurrent = Liabilities': {
                    'left': ['LiabilitiesCurrent', 'LiabilitiesNoncurrent'],
                    'right': ['Liabilities'],
                    'tolerance': 0.001
                }
            },
            
            # 损益表关系
            'income_statement': {
                'GrossProfit = Revenue - CostOfGoodsSold': {
                    'left': ['GrossProfit'],
                    'right_expression': 'RevenueFromContractWithCustomerExcludingAssessedTax - CostOfGoodsAndServicesSold',
                    'tolerance': 0.001
                },
                'OperatingIncome = GrossProfit - OperatingExpenses': {
                    'left': ['OperatingIncomeLoss'],
                    'right_expression': 'GrossProfit - (ResearchAndDevelopmentExpense + GeneralAndAdministrativeExpense)',
                    'tolerance': 0.001
                }
            },
            
            # 现金流关系
            'cash_flow': {
                'FreeCashFlow = OperatingCashFlow - CapitalExpenditure': {
                    'left_expression': 'NetCashProvidedByUsedInOperatingActivities - PaymentsToAcquirePropertyPlantAndEquipment',
                    'right_expression': 'NetCashProvidedByUsedInOperatingActivities - PaymentsToAcquirePropertyPlantAndEquipment',
                    'tolerance': 0.001
                }
            }
        }
        
        # 定义数据合理性检查规则
        self.reasonableness_rules = {
            'revenue_growth': {
                'max_growth': 0.50,  # 最大50%增长率
                'min_growth': -0.30,  # 最小-30%增长率
                'severity': 'warning'
            },
            'profit_margin': {
                'min_margin': -0.20,  # 最小-20%利润率
                'max_margin': 0.50,   # 最大50%利润率
                'severity': 'warning'
            },
            'current_ratio': {
                'min_ratio': 0.5,     # 最小0.5流动比率
                'max_ratio': 10.0,   # 最大10.0流动比率
                'severity': 'error'
            }
        }
    
    def validate_financial_data(self, financial_facts: Dict[str, Any], 
                               historical_data: Dict[str, Any] = None,
                               sec_website_data: Dict[str, Any] = None) -> ValidationResult:
        """
        执行完整的财务数据验证
        
        Args:
            financial_facts: 当前财务事实数据
            historical_data: 历史财务数据（用于趋势验证）
            sec_website_data: SEC官网数据（用于外部验证）
            
        Returns:
            ValidationResult: 验证结果
        """
        errors = []
        warnings = []
        
        logger.info("开始财务数据交叉验证...")
        
        # 1. 内部一致性验证
        internal_result = self._validate_internal_consistency(financial_facts)
        errors.extend(internal_result.errors)
        warnings.extend(internal_result.warnings)
        
        # 2. 外部数据源验证
        if sec_website_data:
            external_result = self._validate_external_sources(financial_facts, sec_website_data)
            errors.extend(external_result.errors)
            warnings.extend(external_result.warnings)
        
        # 3. 趋势合理性验证
        if historical_data:
            trend_result = self._validate_trends(financial_facts, historical_data)
            errors.extend(trend_result.errors)
            warnings.extend(trend_result.warnings)
        
        # 4. 数据完整性验证
        completeness_result = self._validate_completeness(financial_facts)
        errors.extend(completeness_result.errors)
        warnings.extend(completeness_result.warnings)
        
        # 5. 业务逻辑验证
        business_result = self._validate_business_logic(financial_facts)
        errors.extend(business_result.errors)
        warnings.extend(business_result.warnings)
        
        # 计算置信度分数
        total_checks = len(errors) + len(warnings) + self._count_passed_checks(financial_facts)
        confidence_score = max(0, (total_checks - len(errors) * 2 - len(warnings)) / total_checks)
        
        logger.info(f"验证完成: 发现 {len(errors)} 个错误, {len(warnings)} 个警告, 置信度: {confidence_score:.2%}")
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            confidence_score=confidence_score
        )
    
    def _validate_internal_consistency(self, financial_facts: Dict[str, Any]) -> ValidationResult:
        """内部一致性验证"""
        errors = []
        warnings = []
        
        logger.info("执行内部一致性验证...")
        
        # 验证资产负债表平衡
        if self._check_balance_sheet_equation(financial_facts):
            logger.info("✓ 资产负债表平衡检查通过")
        else:
            errors.append("资产负债表不平衡: 资产 ≠ 负债 + 股东权益")
        
        # 验证损益表内部关系
        gross_profit = self._get_value(financial_facts, 'GrossProfit')
        revenue = self._get_value(financial_facts, 'RevenueFromContractWithCustomerExcludingAssessedTax')
        cogs = self._get_value(financial_facts, 'CostOfGoodsAndServicesSold')
        
        if all(val is not None for val in [gross_profit, revenue, cogs]):
            calculated_gp = revenue - cogs
            if abs(gross_profit - calculated_gp) / abs(revenue) > self.tolerance:
                errors.append(f"毛利润计算不一致: 报告值={gross_profit:,}, 计算值={calculated_gp:,}")
            else:
                logger.info("✓ 毛利润计算验证通过")
        
        # 验证现金流合理性
        operating_cf = self._get_value(financial_facts, 'NetCashProvidedByUsedInOperatingActivities')
        net_income = self._get_value(financial_facts, 'NetIncomeLoss')
        
        if operating_cf is not None and net_income is not None:
            if net_income > 0 and operating_cf < 0:
                warnings.append("净利润为正但经营活动现金流为负，需要关注")
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            confidence_score=0.9 if len(errors) == 0 else 0.5
        )
    
    def _validate_external_sources(self, financial_facts: Dict[str, Any], 
                                 sec_data: Dict[str, Any]) -> ValidationResult:
        """外部数据源验证"""
        errors = []
        warnings = []
        
        logger.info("执行外部数据源验证...")
        
        # 对比关键财务指标
        key_metrics = [
            'RevenueFromContractWithCustomerExcludingAssessedTax',
            'NetIncomeLoss',
            'Assets',
            'Liabilities'
        ]
        
        for metric in key_metrics:
            xbrl_value = self._get_value(financial_facts, metric)
            sec_value = sec_data.get(metric)
            
            if xbrl_value is not None and sec_value is not None:
                difference = abs(xbrl_value - sec_value)
                relative_diff = difference / abs(sec_value) if sec_value != 0 else 0
                
                if relative_diff > 0.05:  # 5%差异阈值
                    errors.append(f"{metric} 与SEC官网数据差异过大: XBRL={xbrl_value:,}, SEC={sec_value:,} ({relative_diff:.1%})")
                elif relative_diff > 0.01:  # 1%警告阈值
                    warnings.append(f"{metric} 与SEC官网数据存在小差异: XBRL={xbrl_value:,}, SEC={sec_value:,} ({relative_diff:.1%})")
                else:
                    logger.info(f"✓ {metric} 外部验证通过")
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            confidence_score=0.8 if len(errors) == 0 else 0.4
        )
    
    def _validate_trends(self, financial_facts: Dict[str, Any], 
                        historical_data: Dict[str, Any]) -> ValidationResult:
        """趋势合理性验证"""
        errors = []
        warnings = []
        
        logger.info("执行趋势合理性验证...")
        
        # 验证收入增长趋势
        current_revenue = self._get_value(financial_facts, 'RevenueFromContractWithCustomerExcludingAssessedTax')
        previous_revenue = self._get_value(historical_data, 'RevenueFromContractWithCustomerExcludingAssessedTax')
        
        if current_revenue is not None and previous_revenue is not None and previous_revenue > 0:
            growth_rate = (current_revenue - previous_revenue) / previous_revenue
            
            if abs(growth_rate) > 0.5:  # 50%以上的变化
                warnings.append(f"收入增长率异常: {growth_rate:.1%}")
            elif abs(growth_rate) > 1.0:  # 100%以上的变化
                errors.append(f"收入增长率极度异常: {growth_rate:.1%}")
        
        # 验证利润率稳定性
        net_income = self._get_value(financial_facts, 'NetIncomeLoss')
        if current_revenue is not None and net_income is not None and current_revenue > 0:
            profit_margin = net_income / current_revenue
            
            if profit_margin < -0.2:  # 亏损超过20%
                warnings.append(f"利润率较低: {profit_margin:.1%}")
            elif profit_margin > 0.4:  # 利润率超过40%
                warnings.append(f"利润率较高: {profit_margin:.1%}")
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            confidence_score=0.7 if len(errors) == 0 else 0.6
        )
    
    def _validate_completeness(self, financial_facts: Dict[str, Any]) -> ValidationResult:
        """数据完整性验证"""
        errors = []
        warnings = []
        
        logger.info("执行数据完整性验证...")
        
        # 检查必需的财务指标
        required_metrics = [
            'RevenueFromContractWithCustomerExcludingAssessedTax',
            'NetIncomeLoss',
            'Assets',
            'Liabilities',
            'StockholdersEquity'
        ]
        
        missing_metrics = []
        for metric in required_metrics:
            if self._get_value(financial_facts, metric) is None:
                missing_metrics.append(metric)
        
        if missing_metrics:
            errors.append(f"缺少关键财务指标: {', '.join(missing_metrics)}")
        else:
            logger.info("✓ 关键财务指标完整性检查通过")
        
        # 检查数据质量
        zero_values = []
        for metric, value in financial_facts.items():
            if isinstance(value, dict) and 'value' in value:
                val = value['value']
                if val == 0 and metric not in ['PreferredStockDividends', 'MinorityInterest']:
                    zero_values.append(metric)
        
        if len(zero_values) > 3:  # 超过3个零值
            warnings.append(f"发现较多零值指标: {', '.join(zero_values[:5])}")
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            confidence_score=0.8 if len(errors) == 0 else 0.5
        )
    
    def _validate_business_logic(self, financial_facts: Dict[str, Any]) -> ValidationResult:
        """业务逻辑验证"""
        errors = []
        warnings = []
        
        logger.info("执行业务逻辑验证...")
        
        # 验证流动比率合理性
        current_assets = self._get_value(financial_facts, 'AssetsCurrent')
        current_liabilities = self._get_value(financial_facts, 'LiabilitiesCurrent')
        
        if current_assets is not None and current_liabilities is not None and current_liabilities > 0:
            current_ratio = current_assets / current_liabilities
            
            if current_ratio < 0.5:
                errors.append(f"流动比率过低: {current_ratio:.2f}")
            elif current_ratio < 1.0:
                warnings.append(f"流动比率偏低: {current_ratio:.2f}")
            elif current_ratio > 10.0:
                warnings.append(f"流动比率过高: {current_ratio:.2f}")
        
        # 验证资产负债率
        total_assets = self._get_value(financial_facts, 'Assets')
        total_liabilities = self._get_value(financial_facts, 'Liabilities')
        
        if total_assets is not None and total_liabilities is not None and total_assets > 0:
            debt_ratio = total_liabilities / total_assets
            
            if debt_ratio > 0.9:
                errors.append(f"资产负债率过高: {debt_ratio:.1%}")
            elif debt_ratio > 0.7:
                warnings.append(f"资产负债率较高: {debt_ratio:.1%}")
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            confidence_score=0.85 if len(errors) == 0 else 0.6
        )
    
    def _check_balance_sheet_equation(self, financial_facts: Dict[str, Any]) -> bool:
        """检查资产负债表平衡方程"""
        assets = self._get_value(financial_facts, 'Assets')
        liabilities = self._get_value(financial_facts, 'Liabilities')
        equity = self._get_value(financial_facts, 'StockholdersEquity')
        
        if all(val is not None for val in [assets, liabilities, equity]):
            return abs(assets - (liabilities + equity)) / abs(assets) <= self.tolerance
        return False
    
    def _get_value(self, financial_facts: Dict[str, Any], metric_name: str) -> Optional[float]:
        """获取财务指标的值"""
        if metric_name in financial_facts:
            value = financial_facts[metric_name]
            if isinstance(value, dict) and 'value' in value:
                return float(value['value'])
            elif isinstance(value, (int, float, Decimal)):
                return float(value)
        return None
    
    def _count_passed_checks(self, financial_facts: Dict[str, Any]) -> int:
        """计算通过的检查数量"""
        passed = 0
        
        # 基本完整性检查
        if self._get_value(financial_facts, 'RevenueFromContractWithCustomerExcludingAssessedTax'):
            passed += 1
        if self._get_value(financial_facts, 'NetIncomeLoss'):
            passed += 1
        
        # 平衡检查
        if self._check_balance_sheet_equation(financial_facts):
            passed += 1
        
        return passed
    
    def generate_validation_report(self, validation_result: ValidationResult, 
                                 company_name: str, fiscal_year: int) -> str:
        """生成验证报告"""
        report = []
        report.append(f"# {company_name} {fiscal_year}年度财务数据验证报告")
        report.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # 总体评估
        status = "✅ 通过" if validation_result.is_valid else "❌ 失败"
        report.append(f"## 总体评估: {status}")
        report.append(f"**置信度分数**: {validation_result.confidence_score:.1%}")
        report.append("")
        
        # 错误信息
        if validation_result.errors:
            report.append("## ❌ 错误")
            for i, error in enumerate(validation_result.errors, 1):
                report.append(f"{i}. {error}")
            report.append("")
        
        # 警告信息
        if validation_result.warnings:
            report.append("## ⚠️ 警告")
            for i, warning in enumerate(validation_result.warnings, 1):
                report.append(f"{i}. {warning}")
            report.append("")
        
        # 建议
        report.append("## 📋 建议")
        if not validation_result.is_valid:
            report.append("- 请检查错误项并重新解析数据")
            report.append("- 建议与原始SEC文件进行人工核对")
        elif validation_result.confidence_score < 0.8:
            report.append("- 数据基本可用但存在一些警告")
            report.append("- 建议关注警告项的影响")
        else:
            report.append("- 数据质量良好，可以正常使用")
        
        return "\n".join(report)


def main():
    """示例使用"""
    # 示例数据
    sample_data = {
        'RevenueFromContractWithCustomerExcludingAssessedTax': {'value': 394328000000},
        'NetIncomeLoss': {'value': 99980000000},
        'Assets': {'value': 352583000000},
        'Liabilities': {'value': 290437000000},
        'StockholdersEquity': {'value': 62146000000},
        'AssetsCurrent': {'value': 143566000000},
        'LiabilitiesCurrent': {'value': 145308000000},
        'GrossProfit': {'value': 170312000000},
        'CostOfGoodsAndServicesSold': {'value': 224016000000}
    }
    
    # 创建验证器
    validator = XBRLDataValidator()
    
    # 执行验证
    result = validator.validate_financial_data(sample_data)
    
    # 生成报告
    report = validator.generate_validation_report(result, "Apple Inc.", 2024)
    print(report)


if __name__ == "__main__":
    main()