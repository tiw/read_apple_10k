#!/usr/bin/env python3
"""
Cross-Company Financial Calculator Analysis Tool
自动跨公司财务计算逻辑对比分析工具

This tool analyzes financial calculation logic across different companies and years,
providing automated comparison capabilities.
"""

import os
import json
import pandas as pd
from pathlib import Path
from collections import defaultdict, Counter
import argparse
import re

class CrossCompanyCalculatorAnalyzer:
    def __init__(self, calculations_dir):
        self.calculations_dir = Path(calculations_dir)
        self.companies = ['AAPL', 'AMZN', 'GOOGL', 'META', 'MSFT', 'NVDA', 'TSLA']
        self.data = self.load_all_calculations()
    
    def load_all_calculations(self):
        """Load all calculation data from markdown files."""
        data = defaultdict(lambda: defaultdict(list))
        
        for company in self.companies:
            company_dir = self.calculations_dir / company
            if not company_dir.exists():
                continue
                
            for file_path in company_dir.glob("*_financial_calculations.md"):
                # Extract year from filename
                year_match = re.search(r'(\d{4})_financial_calculations\.md', file_path.name)
                if year_match:
                    year = year_match.group(1)
                    calculations = self.parse_markdown_file(file_path)
                    data[company][year] = calculations
        
        return data
    
    def parse_markdown_file(self, file_path):
        """Parse a markdown file to extract calculation relationships."""
        calculations = {
            'income_statement': [],
            'balance_sheet': [],
            'cash_flow': [],
            'comprehensive_income': [],
            'eps': [],
            'financial_instruments': [],
            'other': []
        }
        
        current_category = None
        current_role = None
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                # Detect category
                if line.startswith('## 损益表计算逻辑'):
                    current_category = 'income_statement'
                elif line.startswith('## 资产负债表计算逻辑'):
                    current_category = 'balance_sheet'
                elif line.startswith('## 现金流量表计算逻辑'):
                    current_category = 'cash_flow'
                elif line.startswith('## 全面收益计算逻辑'):
                    current_category = 'comprehensive_income'
                elif line.startswith('## 每股收益计算逻辑'):
                    current_category = 'eps'
                elif line.startswith('## 金融工具计算逻辑'):
                    current_category = 'financial_instruments'
                elif line.startswith('## 其他计算逻辑'):
                    current_category = 'other'
                
                # Detect role (subsection)
                elif line.startswith('### '):
                    current_role = line[3:].strip()
                
                # Extract calculation relationships
                elif line.startswith('- ') and '+' in line or '-' in line:
                    if current_category and current_role:
                        # Parse calculation formula
                        formula = line[2:]  # Remove '- ' prefix
                        calc_parts = formula.split(' ')
                        if len(calc_parts) >= 3:
                            from_concept = calc_parts[0]
                            operator = calc_parts[1]
                            to_concept = calc_parts[2]
                            
                            calculations[current_category].append({
                                'from_concept': from_concept,
                                'to_concept': to_concept,
                                'operator': operator,
                                'role': current_role,
                                'formula': formula
                            })
        
        return calculations
    
    def analyze_calculation_differences(self):
        """分析不同公司在相同计算逻辑上的差异"""
        print("=== 跨公司计算逻辑差异分析 ===\n")
        
        # 收集所有计算关系
        all_calculations = defaultdict(list)
        company_usage = defaultdict(lambda: defaultdict(set))
        
        for company, years_data in self.data.items():
            for year, calc_data in years_data.items():
                for category, calcs in calc_data.items():
                    for calc in calcs:
                        key = f"{calc['from_concept']}_{calc['operator']}_{calc['to_concept']}"
                        all_calculations[key].append({
                            'company': company,
                            'year': year,
                            'category': category,
                            'role': calc['role']
                        })
                        company_usage[company][category].add(key)
        
        # 分析常见计算逻辑
        print("1. 最常用的财务计算逻辑 (Top 20):")
        sorted_calcs = sorted(all_calculations.items(), key=lambda x: len(x[1]), reverse=True)[:20]
        for i, (calc_key, usages) in enumerate(sorted_calcs, 1):
            companies_using = set(usage['company'] for usage in usages)
            print(f"{i:2d}. {calc_key}")
            print(f"    使用公司: {', '.join(companies_using)} ({len(companies_using)}/7)")
            print(f"    使用次数: {len(usages)}")
            print()
        
        # 分析公司独特计算逻辑
        print("\n2. 各公司独特的计算逻辑:")
        for company in self.companies:
            if company not in company_usage:
                continue
                
            all_company_calcs = set()
            for category_calcs in company_usage[company].values():
                all_company_calcs.update(category_calcs)
            
            # 找出只有这家公司使用的计算逻辑
            unique_calcs = []
            for calc_key in all_company_calcs:
                other_companies = set()
                for other_company in self.companies:
                    if other_company != company and other_company in company_usage:
                        for category_calcs in company_usage[other_company].values():
                            if calc_key in category_calcs:
                                other_companies.add(other_company)
                                break
                
                if not other_companies:
                    unique_calcs.append(calc_key)
            
            if unique_calcs:
                print(f"\n{company} 独有的计算逻辑 ({len(unique_calcs)} 个):")
                for calc in unique_calcs[:5]:  # 只显示前5个
                    print(f"  - {calc}")
                if len(unique_calcs) > 5:
                    print(f"  ... 还有 {len(unique_calcs) - 5} 个")
    
    def analyze_financial_concepts_usage(self):
        """分析财务概念的使用情况"""
        print("\n=== 财务概念使用分析 ===\n")
        
        concept_usage = defaultdict(lambda: defaultdict(int))
        concept_categories = defaultdict(lambda: defaultdict(set))
        
        for company, years_data in self.data.items():
            for year, calc_data in years_data.items():
                for category, calcs in calc_data.items():
                    for calc in calcs:
                        concept_usage[company][calc['from_concept']] += 1
                        concept_usage[company][calc['to_concept']] += 1
                        concept_categories[company][calc['from_concept']].add(category)
                        concept_categories[company][calc['to_concept']].add(category)
        
        # 分析高频财务概念
        print("1. 最常用的财务概念 (Top 15):")
        all_concepts = Counter()
        for company in concept_usage:
            for concept, count in concept_usage[company].items():
                all_concepts[concept] += count
        
        top_concepts = all_concepts.most_common(15)
        for i, (concept, total_count) in enumerate(top_concepts, 1):
            using_companies = [company for company in concept_usage if concept in concept_usage[company]]
            print(f"{i:2d}. {concept}")
            print(f"    总使用次数: {total_count}")
            print(f"    使用公司: {', '.join(using_companies)} ({len(using_companies)}/7)")
            print()
        
        # 分析公司特有概念
        print("\n2. 各公司特有的财务概念:")
        all_company_concepts = defaultdict(set)
        for company in concept_usage:
            all_company_concepts[company] = set(concept_usage[company].keys())
        
        for company in self.companies:
            if company not in all_company_concepts:
                continue
                
            unique_concepts = []
            for concept in all_company_concepts[company]:
                is_unique = True
                for other_company in self.companies:
                    if other_company != company and other_company in all_company_concepts:
                        if concept in all_company_concepts[other_company]:
                            is_unique = False
                            break
                
                if is_unique:
                    unique_concepts.append(concept)
            
            if unique_concepts:
                print(f"\n{company} 特有概念 ({len(unique_concepts)} 个):")
                for concept in unique_concepts:
                    categories = concept_categories[company][concept]
                    print(f"  - {concept} (用于: {', '.join(categories)})")
    
    def analyze_calculation_complexity(self):
        """分析计算复杂度"""
        print("\n=== 计算复杂度分析 ===\n")
        
        company_complexity = defaultdict(lambda: defaultdict(int))
        
        for company, years_data in self.data.items():
            for year, calc_data in years_data.items():
                total_calculations = sum(len(calcs) for calcs in calc_data.values())
                company_complexity[company][year] = total_calculations
        
        # 计算平均复杂度
        print("1. 各公司平均计算复杂度:")
        complexity_ranking = []
        for company in self.companies:
            if company in company_complexity:
                complexities = list(company_complexity[company].values())
                avg_complexity = sum(complexities) / len(complexities) if complexities else 0
                complexity_ranking.append((company, avg_complexity, len(complexities)))
        
        complexity_ranking.sort(key=lambda x: x[1], reverse=True)
        
        for i, (company, avg_complexity, years_count) in enumerate(complexity_ranking, 1):
            print(f"{i}. {company}: 平均 {avg_complexity:.1f} 个计算公式/年 ({years_count} 年数据)")
        
        # 分析最复杂的年份
        print("\n2. 最复杂的财务报告年份:")
        all_years_data = []
        for company, years_data in company_complexity.items():
            for year, complexity in years_data.items():
                all_years_data.append((company, year, complexity))
        
        all_years_data.sort(key=lambda x: x[2], reverse=True)
        
        for i, (company, year, complexity) in enumerate(all_years_data[:10], 1):
            print(f"{i}. {company} {year}: {complexity} 个计算公式")
    
    def analyze_category_preferences(self):
        """分析各公司对不同计算类别的偏好"""
        print("\n=== 计算类别偏好分析 ===\n")
        
        category_usage = defaultdict(lambda: defaultdict(int))
        
        for company, years_data in self.data.items():
            for year, calc_data in years_data.items():
                for category, calcs in calc_data.items():
                    category_usage[company][category] += len(calcs)
        
        # 创建偏好矩阵
        categories = ['income_statement', 'balance_sheet', 'cash_flow', 'comprehensive_income', 'eps', 'financial_instruments', 'other']
        category_names = {
            'income_statement': '损益表',
            'balance_sheet': '资产负债表',
            'cash_flow': '现金流量表',
            'comprehensive_income': '全面收益',
            'eps': '每股收益',
            'financial_instruments': '金融工具',
            'other': '其他'
        }
        
        print("各公司计算类别使用情况:")
        print("-" * 80)
        print(f"{'公司':<8} {'损益表':<8} {'资产负债表':<10} {'现金流量表':<10} {'全面收益':<8} {'每股收益':<8} {'金融工具':<8} {'其他':<6}")
        print("-" * 80)
        
        for company in self.companies:
            if company in category_usage:
                row = [company]
                for category in categories:
                    count = category_usage[company].get(category, 0)
                    row.append(f"{count}")
                
                print(f"{row[0]:<8} {row[1]:<8} {row[2]:<10} {row[3]:<10} {row[4]:<8} {row[5]:<8} {row[6]:<8} {row[7]:<6}")
        
        # 分析类别偏好
        print("\n各公司最关注的计算类别:")
        for company in self.companies:
            if company in category_usage:
                categories_sorted = sorted(category_usage[company].items(), key=lambda x: x[1], reverse=True)
                top_category = categories_sorted[0]
                category_name = category_names.get(top_category[0], top_category[0])
                print(f"{company}: {category_name} ({top_category[1]} 个计算公式)")
    
    def analyze_temporal_changes(self):
        """分析时间序列变化"""
        print("\n=== 时间序列变化分析 ===\n")
        
        # 分析计算逻辑的增减变化
        concept_trends = defaultdict(lambda: defaultdict(list))
        
        for company, years_data in self.data.items():
            years = sorted(years_data.keys())
            for year in years:
                calc_data = years_data[year]
                all_concepts = set()
                for category, calcs in calc_data.items():
                    for calc in calcs:
                        all_concepts.add(calc['from_concept'])
                        all_concepts.add(calc['to_concept'])
                
                concept_trends[company][year] = len(all_concepts)
        
        # 分析趋势
        print("各公司财务概念数量变化趋势:")
        for company in self.companies:
            if company in concept_trends:
                years = sorted(concept_trends[company].keys())
                if len(years) > 1:
                    start_count = concept_trends[company][years[0]]
                    end_count = concept_trends[company][years[-1]]
                    change = end_count - start_count
                    change_pct = (change / start_count * 100) if start_count > 0 else 0
                    
                    print(f"\n{company}:")
                    print(f"  {years[0]}: {start_count} 个概念")
                    print(f"  {years[-1]}: {end_count} 个概念")
                    print(f"  变化: {change:+d} ({change_pct:+.1f}%)")
    
    def generate_comparison_report(self, output_file=None):
        """生成综合对比报告"""
        print("=== 生成综合跨公司对比报告 ===\n")
        
        report_content = []
        report_content.append("# 跨公司财务计算逻辑对比分析报告\n")
        report_content.append(f"分析时间: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_content.append(f"涵盖公司: {', '.join(self.companies)}\n")
        
        # 执行所有分析
        analyses = [
            ("计算逻辑差异", self.analyze_calculation_differences),
            ("财务概念使用", self.analyze_financial_concepts_usage),
            ("计算复杂度", self.analyze_calculation_complexity),
            ("计算类别偏好", self.analyze_category_preferences),
            ("时间序列变化", self.analyze_temporal_changes)
        ]
        
        for title, analysis_func in analyses:
            report_content.append(f"## {title}\n")
            # 这里可以捕获print输出并添加到报告中
            # 为了简化，我们直接调用分析函数
            analysis_func()
            report_content.append("---\n")
        
        # 保存报告
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(report_content))
            print(f"\n完整报告已保存到: {output_file}")
    
    def export_to_csv(self, output_dir):
        """导出数据到CSV文件以便进一步分析"""
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)
        
        # 导出计算逻辑统计
        calc_stats = []
        for company, years_data in self.data.items():
            for year, calc_data in years_data.items():
                for category, calcs in calc_data.items():
                    calc_stats.append({
                        'company': company,
                        'year': year,
                        'category': category,
                        'calculation_count': len(calcs)
                    })
        
        df_calc = pd.DataFrame(calc_stats)
        df_calc.to_csv(output_dir / 'calculation_statistics.csv', index=False)
        
        # 导出概念使用统计
        concept_stats = []
        for company, years_data in self.data.items():
            for year, calc_data in years_data.items():
                for category, calcs in calc_data.items():
                    for calc in calcs:
                        concept_stats.append({
                            'company': company,
                            'year': year,
                            'category': category,
                            'from_concept': calc['from_concept'],
                            'to_concept': calc['to_concept'],
                            'operator': calc['operator'],
                            'role': calc['role']
                        })
        
        df_concept = pd.DataFrame(concept_stats)
        df_concept.to_csv(output_dir / 'concept_usage.csv', index=False)
        
        print(f"数据已导出到: {output_dir}")
        print(f"- calculation_statistics.csv: 计算逻辑统计")
        print(f"- concept_usage.csv: 概念使用统计")

def main():
    parser = argparse.ArgumentParser(description='Cross-Company Financial Calculator Analysis')
    parser.add_argument('--calculations-dir', default='/Users/wangting/work/read_apple_10k/knowledge/financial_calculations',
                       help='Directory containing financial calculation markdown files')
    parser.add_argument('--output-dir', default='/Users/wangting/work/read_apple_10k/cross_company_analysis',
                       help='Output directory for analysis results')
    parser.add_argument('--analysis-type', choices=['all', 'differences', 'concepts', 'complexity', 'categories', 'temporal'],
                       default='all', help='Type of analysis to perform')
    
    args = parser.parse_args()
    
    # 创建分析器
    analyzer = CrossCompanyCalculatorAnalyzer(args.calculations_dir)
    
    # 创建输出目录
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # 执行分析
    if args.analysis_type == 'all':
        analyzer.generate_comparison_report(output_dir / 'cross_company_analysis_report.md')
        analyzer.export_to_csv(output_dir)
    elif args.analysis_type == 'differences':
        analyzer.analyze_calculation_differences()
    elif args.analysis_type == 'concepts':
        analyzer.analyze_financial_concepts_usage()
    elif args.analysis_type == 'complexity':
        analyzer.analyze_calculation_complexity()
    elif args.analysis_type == 'categories':
        analyzer.analyze_category_preferences()
    elif args.analysis_type == 'temporal':
        analyzer.analyze_temporal_changes()

if __name__ == "__main__":
    main()