#!/usr/bin/env python3
"""
验证协调器
协调所有验证器执行完整的数据交叉验证流程
"""

import logging
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
import os

from .data_validator import XBRLDataValidator, ValidationResult
from .sec_cross_validator import SECCrossValidator
from .historical_validator import HistoricalValidator, TrendAnalysis

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ValidationOrchestrator:
    """验证协调器 - 统一管理所有验证流程"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        初始化验证协调器
        
        Args:
            config: 验证配置
        """
        self.config = config or {}
        
        # 初始化验证器
        self.data_validator = XBRLDataValidator(
            tolerance=self.config.get('tolerance', 0.01)
        )
        self.sec_validator = SECCrossValidator(
            user_agent=self.config.get('user_agent', 'XBRL Validator (analysis@example.com)')
        )
        self.historical_validator = HistoricalValidator(
            outlier_threshold=self.config.get('outlier_threshold', 2.5),
            min_historical_years=self.config.get('min_historical_years', 3)
        )
        
        # 验证结果存储
        self.validation_results = {}
        self.reports_generated = []
    
    def validate_xbrl_document(self, 
                              xbrl_data: Dict[str, Any],
                              company_info: Dict[str, Any],
                              historical_data: List[Dict[str, Any]] = None,
                              sec_accession_number: str = None,
                              sec_api_client = None) -> Dict[str, Any]:
        """
        执行完整的XBRL文档验证
        
        Args:
            xbrl_data: XBRL解析的财务数据
            company_info: 公司信息字典
            historical_data: 历史财务数据（可选）
            sec_accession_number: SEC文件编号（用于外部验证）
            
        Returns:
            完整的验证结果
        """
        company_name = company_info.get('name', 'Unknown Company')
        fiscal_year = company_info.get('fiscal_year', datetime.now().year)
        cik = company_info.get('cik')
        
        logger.info(f"开始验证 {company_name} {fiscal_year} 年度财务数据...")
        
        # 初始化验证结果
        validation_summary = {
            'company_name': company_name,
            'fiscal_year': fiscal_year,
            'cik': cik,
            'validation_timestamp': datetime.now().isoformat(),
            'overall_confidence_score': 0.0,
            'validation_status': 'UNKNOWN',
            'validation_components': {},
            'issues_found': [],
            'recommendations': []
        }
        
        try:
            # 1. 内部数据一致性验证
            logger.info("执行内部数据一致性验证...")
            internal_result = self.data_validator.validate_financial_data(xbrl_data)
            validation_summary['validation_components']['internal_consistency'] = {
                'passed': internal_result.is_valid,
                'confidence_score': internal_result.confidence_score,
                'errors': internal_result.errors,
                'warnings': internal_result.warnings
            }
            
            # 2. SEC外部数据验证（优先使用API，其次是文件数据）
            sec_validation_result = None
            sec_api_validation_result = None
            
            # 2a. SEC API验证（如果提供了API客户端）
            if sec_api_client and cik:
                logger.info("执行SEC API数据验证...")
                try:
                    api_comparison = self.sec_validator.validate_against_sec_api_data(
                        xbrl_data=xbrl_data,
                        sec_api_client=sec_api_client,
                        company_cik=cik,
                        fiscal_year=fiscal_year,
                        report_type='10-K'
                    )
                    
                    if api_comparison and api_comparison['api_match_rate'] > 0:
                        validation_summary['validation_components']['sec_api_external'] = {
                            'match_rate': api_comparison['api_match_rate'],
                            'matches': len(api_comparison['api_matches']),
                            'mismatches': len(api_comparison['api_mismatches']),
                            'missing_in_api': len(api_comparison['missing_in_api']),
                            'query_success_rate': sum(1 for q in api_comparison.get('api_query_details', []) if q.get('query_successful', False)) / len(api_comparison.get('api_query_details', [])) if api_comparison.get('api_query_details') else 0,
                            'comparison_details': api_comparison
                        }
                        sec_api_validation_result = api_comparison
                        logger.info(f"SEC API验证完成，匹配率: {api_comparison['api_match_rate']:.1%}")
                    else:
                        logger.warning("SEC API验证未返回有效数据")
                except Exception as e:
                    logger.error(f"SEC API验证失败: {e}")
            
            # 2b. SEC文件数据验证（如果提供了文件编号且API验证失败）
            if sec_accession_number and cik and not sec_api_validation_result:
                logger.info("执行SEC文件数据验证...")
                try:
                    sec_data = self.sec_validator.get_sec_filing_data(cik, sec_accession_number)
                    if sec_data:
                        sec_comparison = self.sec_validator.validate_against_sec_data(xbrl_data, sec_data)
                        validation_summary['validation_components']['sec_external'] = {
                            'match_rate': sec_comparison['overall_match_rate'],
                            'matches': len(sec_comparison['matches']),
                            'mismatches': len(sec_comparison['mismatches']),
                            'missing_in_sec': len(sec_comparison['missing_in_sec']),
                            'comparison_details': sec_comparison
                        }
                        sec_validation_result = sec_comparison
                    else:
                        logger.warning("无法获取SEC文件数据进行对比")
                except Exception as e:
                    logger.error(f"SEC文件验证失败: {e}")
            
            # 3. 历史趋势验证（如果有历史数据）
            historical_analysis = None
            if historical_data:
                logger.info("执行历史趋势验证...")
                try:
                    trend_analyses = self.historical_validator.validate_historical_trends(xbrl_data, historical_data)
                    if trend_analyses:
                        issues = self.historical_validator.validate_reasonableness(trend_analyses)
                        anomalies = self.historical_validator.detect_financial_anomalies(trend_analyses)
                        
                        validation_summary['validation_components']['historical_trends'] = {
                            'analyzed_concepts': len(trend_analyses),
                            'trend_issues': len(issues),
                            'anomalies_detected': sum(len(anomaly_list) for anomaly_list in anomalies.values()),
                            'issues': issues,
                            'anomalies': anomalies,
                            'trend_analyses': {k: v.__dict__ for k, v in trend_analyses.items()}
                        }
                        historical_analysis = {
                            'trend_analyses': trend_analyses,
                            'issues': issues,
                            'anomalies': anomalies
                        }
                except Exception as e:
                    logger.error(f"历史趋势验证失败: {e}")
            
            # 计算总体置信度分数
            overall_confidence = self._calculate_overall_confidence(validation_summary['validation_components'])
            validation_summary['overall_confidence_score'] = overall_confidence
            
            # 确定验证状态
            validation_summary['validation_status'] = self._determine_validation_status(
                validation_summary['validation_components'], overall_confidence
            )
            
            # 汇总所有问题
            validation_summary['issues_found'] = self._compile_all_issues(validation_summary['validation_components'])
            
            # 生成建议
            validation_summary['recommendations'] = self._generate_recommendations(validation_summary)
            
            logger.info(f"验证完成: {company_name} {fiscal_year} - "
                       f"状态={validation_summary['validation_status']}, "
                       f"置信度={overall_confidence:.1%}")
            
            return validation_summary
            
        except Exception as e:
            logger.error(f"验证过程发生错误: {e}")
            validation_summary['validation_status'] = 'ERROR'
            validation_summary['issues_found'].append(f"验证过程错误: {str(e)}")
            return validation_summary
    
    def _calculate_overall_confidence(self, components: Dict[str, Any]) -> float:
        """计算总体置信度分数"""
        confidence_scores = []
        weights = {
            'internal_consistency': 0.4,
            'sec_api_external': 0.3,
            'sec_external': 0.2,
            'historical_trends': 0.1
        }
        
        for component_name, weight in weights.items():
            if component_name in components:
                component = components[component_name]
                
                if component_name == 'internal_consistency':
                    confidence_scores.append(component['confidence_score'] * weight)
                elif component_name == 'sec_api_external':
                    # API验证的权重基于匹配率和查询成功率
                    match_rate = component['match_rate']
                    query_success_rate = component.get('query_success_rate', 1.0)
                    api_score = (match_rate * 0.7 + query_success_rate * 0.3) * weight
                    confidence_scores.append(api_score)
                elif component_name == 'sec_external':
                    confidence_scores.append(component['match_rate'] * weight)
                elif component_name == 'historical_trends':
                    # 基于趋势分析问题的数量计算分数
                    total_issues = component.get('trend_issues', 0) + component.get('anomalies_detected', 0)
                    trend_score = max(0, 1 - total_issues * 0.1)  # 每个问题扣0.1分
                    confidence_scores.append(trend_score * weight)
        
        return sum(confidence_scores) if confidence_scores else 0.0
    
    def _determine_validation_status(self, components: Dict[str, Any], confidence_score: float) -> str:
        """确定验证状态"""
        # 检查是否有严重错误
        for component_name, component in components.items():
            if component_name == 'internal_consistency' and not component['passed']:
                return 'FAILED'
        
        # 基于置信度分数确定状态
        if confidence_score >= 0.9:
            return 'EXCELLENT'
        elif confidence_score >= 0.8:
            return 'GOOD'
        elif confidence_score >= 0.6:
            return 'FAIR'
        else:
            return 'POOR'
    
    def _compile_all_issues(self, components: Dict[str, Any]) -> List[str]:
        """汇总所有问题"""
        all_issues = []
        
        for component_name, component in components.items():
            if component_name == 'internal_consistency':
                all_issues.extend([f"内部错误: {error}" for error in component.get('errors', [])])
                all_issues.extend([f"内部警告: {warning}" for warning in component.get('warnings', [])])
            elif component_name == 'sec_external':
                mismatches = component.get('comparison_details', {}).get('mismatches', [])
                for mismatch in mismatches:
                    all_issues.append(
                        f"SEC数据不匹配: {mismatch['concept']} "
                        f"(差异: {mismatch['relative_difference']:.1%})"
                    )
            elif component_name == 'historical_trends':
                all_issues.extend(component.get('issues', []))
                
                # 添加异常模式
                anomalies = component.get('anomalies', {})
                for anomaly_type, anomaly_list in anomalies.items():
                    for anomaly in anomaly_list:
                        all_issues.append(f"异常模式({anomaly_type}): {anomaly}")
        
        return all_issues
    
    def _generate_recommendations(self, validation_summary: Dict[str, Any]) -> List[str]:
        """生成改进建议"""
        recommendations = []
        status = validation_summary['validation_status']
        confidence = validation_summary['overall_confidence_score']
        
        if status == 'FAILED':
            recommendations.extend([
                "数据存在严重错误，建议重新解析XBRL文件",
                "检查原始SEC文件的完整性",
                "考虑手动核对关键财务数据"
            ])
        elif status == 'POOR':
            recommendations.extend([
                "数据质量较差，建议进行详细核查",
                "检查解析配置和参数设置",
                "考虑使用其他数据源进行交叉验证"
            ])
        elif status == 'FAIR':
            recommendations.extend([
                "数据基本可用但存在一些问题",
                "关注具体警告项并进行必要的人工核对",
                "建议在重要决策前进一步验证"
            ])
        elif status == 'GOOD':
            recommendations.extend([
                "数据质量良好，可以正常使用",
                "建议定期更新验证规则",
                "可以开始进行财务分析"
            ])
        elif status == 'EXCELLENT':
            recommendations.extend([
                "数据质量优秀，与外部数据高度一致",
                "可以放心用于财务分析和决策",
                "建议建立持续的数据质量监控"
            ])
        
        # 基于具体问题的建议
        components = validation_summary['validation_components']
        
        if 'internal_consistency' in components:
            internal = components['internal_consistency']
            if internal.get('errors'):
                recommendations.append("重点关注内部一致性问题，检查数据计算逻辑")
        
        if 'sec_api_external' in components:
            sec_api = components['sec_api_external']
            if sec_api.get('match_rate', 0) < 0.8:
                recommendations.append("SEC API数据匹配度较低，建议检查解析精度")
            elif sec_api.get('query_success_rate', 1.0) < 0.7:
                recommendations.append("SEC API查询成功率较低，可能影响验证准确性")
        elif 'sec_external' in components:
            sec = components['sec_external']
            if sec.get('match_rate', 0) < 0.8:
                recommendations.append("SEC数据匹配度较低，建议检查解析精度")
        
        if 'historical_trends' in components:
            historical = components['historical_trends']
            if historical.get('anomalies_detected', 0) > 0:
                recommendations.append("发现历史趋势异常，建议结合业务环境分析")
        
        return recommendations
    
    def generate_comprehensive_report(self, validation_summary: Dict[str, Any], 
                                    output_dir: str = "./validation_reports") -> str:
        """生成综合验证报告"""
        
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        
        company_name = validation_summary['company_name']
        fiscal_year = validation_summary['fiscal_year']
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # 生成报告文件名
        report_filename = f"{company_name.replace(' ', '_')}_{fiscal_year}_validation_report_{timestamp}.md"
        report_path = os.path.join(output_dir, report_filename)
        
        # 生成报告内容
        report_content = self._generate_report_content(validation_summary)
        
        # 保存报告
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        # 同时保存JSON格式的详细结果
        json_filename = f"{company_name.replace(' ', '_')}_{fiscal_year}_validation_data_{timestamp}.json"
        json_path = os.path.join(output_dir, json_filename)
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(validation_summary, f, indent=2, ensure_ascii=False, default=str)
        
        logger.info(f"验证报告已保存: {report_path}")
        self.reports_generated.append(report_path)
        
        return report_path
    
    def _generate_report_content(self, validation_summary: Dict[str, Any]) -> str:
        """生成报告内容"""
        report = []
        
        # 报告头部
        report.append(f"# {validation_summary['company_name']} {validation_summary['fiscal_year']}年度")
        report.append("# 财务数据交叉验证综合报告")
        report.append("")
        report.append(f"**生成时间**: {validation_summary['validation_timestamp']}")
        report.append(f"**公司CIK**: {validation_summary['cik']}")
        report.append(f"**验证状态**: {self._format_status(validation_summary['validation_status'])}")
        report.append(f"**总体置信度**: {validation_summary['overall_confidence_score']:.1%}")
        report.append("")
        
        # 执行摘要
        report.append("## 📊 执行摘要")
        report.append(self._generate_executive_summary(validation_summary))
        report.append("")
        
        # 验证结果详情
        components = validation_summary['validation_components']
        
        if 'internal_consistency' in components:
            report.append(self._generate_internal_section(components['internal_consistency']))
        
        if 'sec_api_external' in components:
            report.append(self._generate_sec_api_section(components['sec_api_external']))
        elif 'sec_external' in components:
            report.append(self._generate_sec_section(components['sec_external']))
        
        if 'historical_trends' in components:
            report.append(self._generate_historical_section(components['historical_trends']))
        
        # 问题汇总
        if validation_summary['issues_found']:
            report.append("## ❌ 问题汇总")
            for i, issue in enumerate(validation_summary['issues_found'], 1):
                report.append(f"{i}. {issue}")
            report.append("")
        
        # 建议和后续步骤
        if validation_summary['recommendations']:
            report.append("## 💡 改进建议")
            for i, recommendation in enumerate(validation_summary['recommendations'], 1):
                report.append(f"{i}. {recommendation}")
            report.append("")
        
        # 结论
        report.append("## 🎯 结论")
        report.append(self._generate_conclusion(validation_summary))
        
        return "\n".join(report)
    
    def _format_status(self, status: str) -> str:
        """格式化状态显示"""
        status_map = {
            'EXCELLENT': '✅ 优秀',
            'GOOD': '✅ 良好',
            'FAIR': '⚠️ 一般',
            'POOR': '❌ 较差',
            'FAILED': '❌ 失败',
            'ERROR': '❌ 错误'
        }
        return status_map.get(status, status)
    
    def _generate_executive_summary(self, validation_summary: Dict[str, Any]) -> str:
        """生成执行摘要"""
        status = validation_summary['validation_status']
        confidence = validation_summary['overall_confidence_score']
        issues_count = len(validation_summary['issues_found'])
        
        summary_parts = [
            f"数据验证状态为**{self._format_status(status)}**，",
            f"总体置信度分数为**{confidence:.1%}**。"
        ]
        
        if issues_count == 0:
            summary_parts.append("未发现明显问题，数据质量良好。")
        else:
            summary_parts.append(f"发现**{issues_count}个问题**需要关注。")
        
        return "".join(summary_parts)
    
    def _generate_internal_section(self, internal_data: Dict[str, Any]) -> str:
        """生成内部一致性验证部分"""
        section = ["## 🔍 内部一致性验证"]
        section.append("")
        
        status = "✅ 通过" if internal_data['passed'] else "❌ 失败"
        section.append(f"**验证状态**: {status}")
        section.append(f"**置信度分数**: {internal_data['confidence_score']:.1%}")
        section.append("")
        
        if internal_data.get('errors'):
            section.append("### 错误")
            for error in internal_data['errors']:
                section.append(f"- ❌ {error}")
            section.append("")
        
        if internal_data.get('warnings'):
            section.append("### 警告")
            for warning in internal_data['warnings']:
                section.append(f"- ⚠️ {warning}")
            section.append("")
        
        return "\n".join(section)
    
    def _generate_sec_api_section(self, sec_api_data: Dict[str, Any]) -> str:
        """生成SEC API验证部分"""
        section = ["## 🌐 SEC API数据验证"]
        section.append("")
        
        match_rate = sec_api_data['match_rate']
        query_success_rate = sec_api_data.get('query_success_rate', 1.0)
        matches = sec_api_data['matches']
        mismatches = sec_api_data['mismatches']
        
        section.append(f"**API数据匹配率**: {match_rate:.1%}")
        section.append(f"**API查询成功率**: {query_success_rate:.1%}")
        section.append(f"**匹配项数**: {matches}")
        section.append(f"**不匹配项数**: {mismatches}")
        section.append("")
        
        # API查询详情
        query_details = sec_api_data.get('comparison_details', {}).get('api_query_details', [])
        if query_details:
            successful_queries = sum(1 for q in query_details if q.get('query_successful', False))
            total_queries = len(query_details)
            
            section.append(f"### API查询统计")
            section.append(f"- 总查询次数: {total_queries}")
            section.append(f"- 成功查询: {successful_queries}")
            section.append(f"- 失败查询: {total_queries - successful_queries}")
            section.append("")
            
            # 失败查询
            failed_queries = [q for q in query_details if not q.get('query_successful', False)]
            if failed_queries:
                section.append("### API查询失败项")
                for query in failed_queries[:5]:  # 显示前5个
                    section.append(f"- {query['concept']} -> {query['api_concept']}: {query['reason']}")
                section.append("")
        
        # 不匹配项详情
        if mismatches > 0:
            section.append("### 主要不匹配项")
            comparison = sec_api_data['comparison_details']
            for mismatch in comparison['api_mismatches'][:5]:  # 显示前5个
                concept = mismatch['concept']
                diff_pct = mismatch['relative_difference'] * 100
                section.append(f"- {concept}: 差异 {diff_pct:.1f}%")
            section.append("")
        
        return "\n".join(section)
    
    def _generate_sec_section(self, sec_data: Dict[str, Any]) -> str:
        """生成SEC验证部分"""
        section = ["## 🌐 SEC官网数据验证"]
        section.append("")
        
        match_rate = sec_data['match_rate']
        section.append(f"**数据匹配率**: {match_rate:.1%}")
        section.append(f"**匹配项数**: {sec_data['matches']}")
        section.append(f"**不匹配项数**: {sec_data['mismatches']}")
        section.append("")
        
        if sec_data['mismatches'] > 0:
            section.append("### 主要不匹配项")
            comparison = sec_data['comparison_details']
            for mismatch in comparison['mismatches'][:5]:  # 显示前5个
                concept = mismatch['concept']
                diff_pct = mismatch['relative_difference'] * 100
                section.append(f"- {concept}: 差异 {diff_pct:.1f}%")
            section.append("")
        
        return "\n".join(section)
    
    def _generate_historical_section(self, historical_data: Dict[str, Any]) -> str:
        """生成历史趋势验证部分"""
        section = ["## 📈 历史趋势验证"]
        section.append("")
        
        analyzed_concepts = historical_data['analyzed_concepts']
        trend_issues = historical_data['trend_issues']
        anomalies_detected = historical_data['anomalies_detected']
        
        section.append(f"**分析指标数**: {analyzed_concepts}")
        section.append(f"**趋势问题**: {trend_issues}")
        section.append(f"**异常模式**: {anomalies_detected}")
        section.append("")
        
        if historical_data.get('anomalies'):
            section.append("### 检测到的异常模式")
            for anomaly_type, anomalies in historical_data['anomalies'].items():
                if anomalies:
                    section.append(f"#### {anomaly_type.replace('_', ' ').title()}")
                    for anomaly in anomalies[:3]:  # 显示前3个
                        section.append(f"- {anomaly}")
            section.append("")
        
        return "\n".join(section)
    
    def _generate_conclusion(self, validation_summary: Dict[str, Any]) -> str:
        """生成结论"""
        status = validation_summary['validation_status']
        confidence = validation_summary['overall_confidence_score']
        issues_count = len(validation_summary['issues_found'])
        
        if status == 'EXCELLENT':
            return "数据质量优秀，与各种验证标准高度一致，可以放心用于财务分析和决策。"
        elif status == 'GOOD':
            return "数据质量良好，存在少量不影响主要分析的差异，建议在重要决策前确认关键指标。"
        elif status == 'FAIR':
            return "数据基本可用但存在一些问题，建议重点关注警告项并在必要时进行人工核对。"
        elif status == 'POOR':
            return "数据质量存在明显问题，建议重新解析数据或使用其他数据源进行验证。"
        else:
            return "数据验证失败，存在严重错误，不建议使用当前数据进行重要分析。"


def main():
    """示例使用"""
    # 模拟数据
    xbrl_data = {
        'RevenueFromContractWithCustomerExcludingAssessedTax': {'value': 394328000000},
        'NetIncomeLoss': {'value': 99980000000},
        'Assets': {'value': 352583000000},
        'Liabilities': {'value': 290437000000},
        'StockholdersEquity': {'value': 62146000000}
    }
    
    company_info = {
        'name': 'Apple Inc.',
        'cik': '0000320193',
        'fiscal_year': 2024
    }
    
    historical_data = [
        {'RevenueFromContractWithCustomerExcludingAssessedTax': {'value': 383285000000},
         'NetIncomeLoss': {'value': 96995000000},
         'Assets': {'value': 365725000000},
         'Liabilities': {'value': 302083000000}},
        {'RevenueFromContractWithCustomerExcludingAssessedTax': {'value': 365817000000},
         'NetIncomeLoss': {'value': 94680000000},
         'Assets': {'value': 352755000000},
         'Liabilities': {'value': 287912000000}}
    ]
    
    # 创建协调器并执行验证
    orchestrator = ValidationOrchestrator()
    result = orchestrator.validate_xbrl_document(
        xbrl_data=xbrl_data,
        company_info=company_info,
        historical_data=historical_data,
        sec_accession_number="0000320193-24-000123"  # 示例文件编号
    )
    
    # 生成报告
    report_path = orchestrator.generate_comprehensive_report(result)
    print(f"验证报告已生成: {report_path}")


if __name__ == "__main__":
    main()