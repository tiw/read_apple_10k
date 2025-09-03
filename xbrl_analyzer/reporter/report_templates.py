"""
报表模板模块

定义年报生成的模板和格式
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import json


class ReportTemplates:
    """报表模板类"""
    
    @staticmethod
    def get_html_template() -> str:
        """获取HTML报表模板"""
        return """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{company_name} {fiscal_year}年10-K年报分析</title>
    <style>
        body {{
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            border-bottom: 3px solid #2c3e50;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        .header h1 {{
            color: #2c3e50;
            margin: 0;
            font-size: 2.5em;
        }}
        .header .subtitle {{
            color: #7f8c8d;
            font-size: 1.2em;
            margin-top: 10px;
        }}
        .section {{
            margin-bottom: 40px;
        }}
        .section h2 {{
            color: #34495e;
            border-left: 4px solid #3498db;
            padding-left: 15px;
            margin-bottom: 20px;
        }}
        .section h3 {{
            color: #2c3e50;
            margin-top: 25px;
            margin-bottom: 15px;
        }}
        .financial-table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            background-color: white;
        }}
        .financial-table th {{
            background-color: #34495e;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: bold;
        }}
        .financial-table td {{
            padding: 10px 12px;
            border-bottom: 1px solid #ecf0f1;
        }}
        .financial-table tr:nth-child(even) {{
            background-color: #f8f9fa;
        }}
        .financial-table tr:hover {{
            background-color: #e8f4f8;
        }}
        .metric-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .metric-card {{
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 20px;
        }}
        .metric-card h4 {{
            color: #2c3e50;
            margin: 0 0 10px 0;
            font-size: 1.1em;
        }}
        .metric-value {{
            font-size: 1.5em;
            font-weight: bold;
            color: #27ae60;
            margin-bottom: 5px;
        }}
        .metric-formula {{
            font-size: 0.9em;
            color: #7f8c8d;
            font-style: italic;
        }}
        .summary-stats {{
            background-color: #e8f5e8;
            border: 1px solid #27ae60;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 30px;
        }}
        .summary-stats h3 {{
            color: #27ae60;
            margin-top: 0;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }}
        .stat-item {{
            text-align: center;
        }}
        .stat-value {{
            font-size: 1.8em;
            font-weight: bold;
            color: #2c3e50;
        }}
        .stat-label {{
            color: #7f8c8d;
            font-size: 0.9em;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ecf0f1;
            color: #7f8c8d;
        }}
        .error {{
            color: #e74c3c;
            background-color: #fdf2f2;
            border: 1px solid #fecaca;
            border-radius: 4px;
            padding: 10px;
            margin: 10px 0;
        }}
        .warning {{
            color: #f39c12;
            background-color: #fef9e7;
            border: 1px solid #fde68a;
            border-radius: 4px;
            padding: 10px;
            margin: 10px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{company_name}</h1>
            <div class="subtitle">{fiscal_year}年10-K年报财务分析报告</div>
            <div class="subtitle">生成时间: {report_date}</div>
        </div>

        {content}

        <div class="footer">
            <p>本报告基于SEC EDGAR数据库的10-K年报数据生成</p>
            <p>数据来源: SEC EDGAR API | 生成工具: XBRL年报分析器</p>
        </div>
    </div>
</body>
</html>
        """
    
    @staticmethod
    def get_markdown_template() -> str:
        """获取Markdown报表模板"""
        return """
# {company_name} {fiscal_year}年10-K年报分析

**生成时间**: {report_date}  
**数据来源**: SEC EDGAR API

---

{content}

---

*本报告基于SEC EDGAR数据库的10-K年报数据生成*
        """
    
    @staticmethod
    def format_income_statement_section(facts: Dict[str, Any], concepts: Dict[str, Any]) -> str:
        """格式化损益表部分"""
        html = """
        <div class="section">
            <h2>💰 损益表 (Income Statement)</h2>
            <table class="financial-table">
                <thead>
                    <tr>
                        <th>项目</th>
                        <th>英文名称</th>
                        <th>数值</th>
                        <th>单位</th>
                        <th>财政年度</th>
                    </tr>
                </thead>
                <tbody>
        """
        
        income_concepts = [
            'RevenueFromContractWithCustomerExcludingAssessedTax',
            'CostOfGoodsAndServicesSold',
            'GrossProfit',
            'OperatingExpenses',
            'ResearchAndDevelopmentExpense',
            'GeneralAndAdministrativeExpense',
            'OperatingIncomeLoss',
            'NonoperatingIncomeExpense',
            'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',
            'IncomeTaxExpenseBenefit',
            'NetIncomeLoss',
            'EarningsPerShareBasic',
            'EarningsPerShareDiluted'
        ]
        
        for concept in income_concepts:
            if concept in facts:
                fact = facts[concept]
                concept_info = concepts.get(concept, {})
                html += f"""
                    <tr>
                        <td>{getattr(concept_info, 'chinese_name', concept)}</td>
                        <td>{getattr(concept_info, 'english_name', concept)}</td>
                        <td>{fact.get('formatted_value', 'N/A')}</td>
                        <td>{fact.get('unit', 'USD')}</td>
                        <td>FY{fact.get('fiscal_year', 'N/A')}</td>
                    </tr>
                """
        
        html += """
                </tbody>
            </table>
        </div>
        """
        return html
    
    @staticmethod
    def format_balance_sheet_section(facts: Dict[str, Any], concepts: Dict[str, Any]) -> str:
        """格式化资产负债表部分"""
        html = """
        <div class="section">
            <h2>🏦 资产负债表 (Balance Sheet)</h2>
            <table class="financial-table">
                <thead>
                    <tr>
                        <th>项目</th>
                        <th>英文名称</th>
                        <th>数值</th>
                        <th>单位</th>
                        <th>财政年度</th>
                    </tr>
                </thead>
                <tbody>
        """
        
        balance_concepts = [
            'Assets',
            'AssetsCurrent',
            'CashAndCashEquivalentsAtCarryingValue',
            'MarketableSecuritiesCurrent',
            'AccountsReceivableNetCurrent',
            'InventoryNet',
            'AssetsNoncurrent',
            'PropertyPlantAndEquipmentNet',
            'Liabilities',
            'LiabilitiesCurrent',
            'AccountsPayableCurrent',
            'LongTermDebtCurrent',
            'LiabilitiesNoncurrent',
            'LongTermDebtNoncurrent',
            'StockholdersEquity',
            'CommonStockSharesIssued',
            'RetainedEarningsAccumulatedDeficit'
        ]
        
        for concept in balance_concepts:
            if concept in facts:
                fact = facts[concept]
                concept_info = concepts.get(concept, {})
                html += f"""
                    <tr>
                        <td>{getattr(concept_info, 'chinese_name', concept)}</td>
                        <td>{getattr(concept_info, 'english_name', concept)}</td>
                        <td>{fact.get('formatted_value', 'N/A')}</td>
                        <td>{fact.get('unit', 'USD')}</td>
                        <td>FY{fact.get('fiscal_year', 'N/A')}</td>
                    </tr>
                """
        
        html += """
                </tbody>
            </table>
        </div>
        """
        return html
    
    @staticmethod
    def format_cash_flow_section(facts: Dict[str, Any], concepts: Dict[str, Any]) -> str:
        """格式化现金流量表部分"""
        html = """
        <div class="section">
            <h2>💸 现金流量表 (Cash Flow Statement)</h2>
            <table class="financial-table">
                <thead>
                    <tr>
                        <th>项目</th>
                        <th>英文名称</th>
                        <th>数值</th>
                        <th>单位</th>
                        <th>财政年度</th>
                    </tr>
                </thead>
                <tbody>
        """
        
        cash_flow_concepts = [
            'NetCashProvidedByUsedInOperatingActivities',
            'PaymentsToAcquirePropertyPlantAndEquipment',
            'PaymentsOfDividends',
            'PaymentsForRepurchaseOfCommonStock'
        ]
        
        for concept in cash_flow_concepts:
            if concept in facts:
                fact = facts[concept]
                concept_info = concepts.get(concept, {})
                html += f"""
                    <tr>
                        <td>{getattr(concept_info, 'chinese_name', concept)}</td>
                        <td>{getattr(concept_info, 'english_name', concept)}</td>
                        <td>{fact.get('formatted_value', 'N/A')}</td>
                        <td>{fact.get('unit', 'USD')}</td>
                        <td>FY{fact.get('fiscal_year', 'N/A')}</td>
                    </tr>
                """
        
        html += """
                </tbody>
            </table>
        </div>
        """
        return html
    
    @staticmethod
    def format_metrics_section(metrics: Dict[str, Any]) -> str:
        """格式化财务指标部分"""
        html = """
        <div class="section">
            <h2>📊 财务指标分析</h2>
        """
        
        # 按类别分组显示指标
        categories = {
            'profitability': '盈利能力指标',
            'liquidity': '流动性指标',
            'leverage': '杠杆比率',
            'efficiency': '效率指标',
            'cash_flow': '现金流指标',
            'market': '市场指标'
        }
        
        for category, category_name in categories.items():
            category_metrics = {k: v for k, v in metrics.items() if v.get('category') == category}
            
            if category_metrics:
                html += f"""
                <h3>{category_name}</h3>
                <div class="metric-grid">
                """
                
                for metric_name, metric in category_metrics.items():
                    if metric.get('value') is not None:
                        html += f"""
                        <div class="metric-card">
                            <h4>{metric.get('chinese_name', metric_name)}</h4>
                            <div class="metric-value">{metric.get('formatted_value', 'N/A')}</div>
                            <div class="metric-formula">{metric.get('formula', '')}</div>
                        </div>
                        """
                    else:
                        missing_deps = metric.get('missing_dependencies', [])
                        error_msg = f"缺少依赖项: {', '.join(missing_deps)}" if missing_deps else "计算失败"
                        html += f"""
                        <div class="metric-card">
                            <h4>{metric.get('chinese_name', metric_name)}</h4>
                            <div class="error">{error_msg}</div>
                        </div>
                        """
                
                html += """
                </div>
                """
        
        html += """
        </div>
        """
        return html
    
    @staticmethod
    def format_summary_section(summary: Dict[str, Any]) -> str:
        """格式化摘要部分"""
        html = f"""
        <div class="section">
            <h2>📋 数据摘要</h2>
            <div class="summary-stats">
                <h3>数据统计</h3>
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-value">{summary.get('total_facts', 0)}</div>
                        <div class="stat-label">财务事实</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">{summary.get('total_metrics', 0)}</div>
                        <div class="stat-label">计算指标</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">{summary.get('successful_metrics', 0)}</div>
                        <div class="stat-label">成功计算</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">{summary.get('success_rate', 0):.1%}</div>
                        <div class="stat-label">成功率</div>
                    </div>
                </div>
            </div>
        </div>
        """
        return html
    
    @staticmethod
    def format_company_info_section(company_info: Dict[str, Any]) -> str:
        """格式化公司信息部分"""
        html = f"""
        <div class="section">
            <h2>🏢 公司信息</h2>
            <table class="financial-table">
                <tbody>
                    <tr>
                        <td><strong>公司名称</strong></td>
                        <td>{company_info.get('name', 'N/A')}</td>
                    </tr>
                    <tr>
                        <td><strong>股票代码</strong></td>
                        <td>{company_info.get('ticker', 'N/A')}</td>
                    </tr>
                    <tr>
                        <td><strong>CIK码</strong></td>
                        <td>{company_info.get('cik', 'N/A')}</td>
                    </tr>
                    <tr>
                        <td><strong>SIC代码</strong></td>
                        <td>{company_info.get('sic_code', 'N/A')}</td>
                    </tr>
                    <tr>
                        <td><strong>SIC描述</strong></td>
                        <td>{company_info.get('sic_description', 'N/A')}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """
        return html
    
    @staticmethod
    def generate_html_report(company_info: Dict[str, Any], 
                           financial_facts: Dict[str, Any],
                           calculated_metrics: Dict[str, Any],
                           concepts: Dict[str, Any],
                           fiscal_year: int) -> str:
        """生成完整的HTML报告"""
        template = ReportTemplates.get_html_template()
        
        # 生成各部分内容
        content_parts = []
        
        # 公司信息
        content_parts.append(ReportTemplates.format_company_info_section(company_info))
        
        # 损益表
        content_parts.append(ReportTemplates.format_income_statement_section(financial_facts, concepts))
        
        # 资产负债表
        content_parts.append(ReportTemplates.format_balance_sheet_section(financial_facts, concepts))
        
        # 现金流量表
        content_parts.append(ReportTemplates.format_cash_flow_section(financial_facts, concepts))
        
        # 财务指标
        content_parts.append(ReportTemplates.format_metrics_section(calculated_metrics))
        
        # 摘要
        summary = {
            'total_facts': len(financial_facts),
            'total_metrics': len(calculated_metrics),
            'successful_metrics': sum(1 for m in calculated_metrics.values() if m.get('value') is not None),
            'success_rate': sum(1 for m in calculated_metrics.values() if m.get('value') is not None) / len(calculated_metrics) if calculated_metrics else 0
        }
        content_parts.append(ReportTemplates.format_summary_section(summary))
        
        # 合并内容
        content = '\n'.join(content_parts)
        
        # 填充模板
        html = template.format(
            company_name=company_info.get('name', 'Unknown Company'),
            fiscal_year=fiscal_year,
            report_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            content=content
        )
        
        return html
    
    @staticmethod
    def generate_markdown_report(company_info: Dict[str, Any], 
                               financial_facts: Dict[str, Any],
                               calculated_metrics: Dict[str, Any],
                               concepts: Dict[str, Any],
                               fiscal_year: int) -> str:
        """生成Markdown报告"""
        template = ReportTemplates.get_markdown_template()
        
        content_parts = []
        
        # 公司信息
        content_parts.append(f"""
## 🏢 公司信息

- **公司名称**: {company_info.get('name', 'N/A')}
- **股票代码**: {company_info.get('ticker', 'N/A')}
- **CIK码**: {company_info.get('cik', 'N/A')}
- **SIC代码**: {company_info.get('sic_code', 'N/A')}
- **SIC描述**: {company_info.get('sic_description', 'N/A')}
        """)
        
        # 损益表
        content_parts.append("""
## 💰 损益表 (Income Statement)

| 项目 | 英文名称 | 数值 | 单位 | 财政年度 |
|------|----------|------|------|----------|
        """)
        
        income_concepts = [
            'RevenueFromContractWithCustomerExcludingAssessedTax',
            'CostOfGoodsAndServicesSold',
            'GrossProfit',
            'OperatingIncomeLoss',
            'NetIncomeLoss'
        ]
        
        for concept in income_concepts:
            if concept in financial_facts:
                fact = financial_facts[concept]
                concept_info = concepts.get(concept, {})
                content_parts.append(f"| {getattr(concept_info, 'chinese_name', concept)} | {getattr(concept_info, 'english_name', concept)} | {fact.get('formatted_value', 'N/A')} | {fact.get('unit', 'USD')} | FY{fact.get('fiscal_year', 'N/A')} |")
        
        # 财务指标
        content_parts.append("""
## 📊 财务指标分析

### 盈利能力指标
        """)
        
        profitability_metrics = {k: v for k, v in calculated_metrics.items() if v.get('category') == 'profitability'}
        for metric_name, metric in profitability_metrics.items():
            if metric.get('value') is not None:
                content_parts.append(f"- **{metric.get('chinese_name', metric_name)}**: {metric.get('formatted_value', 'N/A')}")
        
        content_parts.append("""
### 流动性指标
        """)
        
        liquidity_metrics = {k: v for k, v in calculated_metrics.items() if v.get('category') == 'liquidity'}
        for metric_name, metric in liquidity_metrics.items():
            if metric.get('value') is not None:
                content_parts.append(f"- **{metric.get('chinese_name', metric_name)}**: {metric.get('formatted_value', 'N/A')}")
        
        # 合并内容
        content = '\n'.join(content_parts)
        
        # 填充模板
        markdown = template.format(
            company_name=company_info.get('name', 'Unknown Company'),
            fiscal_year=fiscal_year,
            report_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            content=content
        )
        
        return markdown
