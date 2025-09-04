#!/usr/bin/env python3
"""
公司历年财务计算逻辑变化分析工具
Company Year-over-Year Financial Calculation Logic Change Analyzer

该工具分析单个公司历年来财务计算逻辑的变化，识别新增、删除和修改的计算关系。
"""

import os
import json
import pandas as pd
from pathlib import Path
from collections import defaultdict, Counter
import argparse
import re
from datetime import datetime

class CompanyCalculationChangeAnalyzer:
    def __init__(self, calculations_dir, company):
        self.calculations_dir = Path(calculations_dir)
        self.company = company
        self.data = self.load_company_calculations()
        
    def load_company_calculations(self):
        """加载指定公司的所有计算数据"""
        data = {}
        
        company_dir = self.calculations_dir / self.company
        if not company_dir.exists():
            print(f"Warning: Company directory {company_dir} not found")
            return {}
            
        for file_path in company_dir.glob(f"{self.company}_*_financial_calculations.md"):
            # Extract year from filename
            year_match = re.search(rf'{self.company}_(\d{{4}})_financial_calculations\.md', file_path.name)
            if year_match:
                year = year_match.group(1)
                calculations = self.parse_markdown_file(file_path)
                data[year] = calculations
        
        # Sort by year
        return dict(sorted(data.items()))
    
    def parse_markdown_file(self, file_path):
        """解析markdown文件提取计算关系"""
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
                elif line.startswith('- ') and ('+' in line or '-' in line):
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
    
    def analyze_year_over_year_changes(self):
        """分析逐年变化"""
        print(f"=== {self.company} 历年计算逻辑变化分析 ===\n")
        
        years = sorted(self.data.keys())
        if len(years) < 2:
            print("需要至少2年的数据才能进行变化分析")
            return {}
        
        changes = {}
        
        for i in range(len(years) - 1):
            year1 = years[i]
            year2 = years[i + 1]
            
            print(f"--- {year1} → {year2} 变化分析 ---")
            
            # Get calculations for both years
            calc1 = self.data[year1]
            calc2 = self.data[year2]
            
            # Convert to sets for comparison
            set1 = self.calculations_to_set(calc1)
            set2 = self.calculations_to_set(calc2)
            
            # Find changes
            added = set2 - set1
            removed = set1 - set2
            common = set1 & set2
            
            # Analyze by category
            category_changes = {}
            for category in calc1.keys():
                cat_set1 = self.category_calculations_to_set(calc1[category])
                cat_set2 = self.category_calculations_to_set(calc2[category])
                
                category_changes[category] = {
                    'added': list(cat_set2 - cat_set1),
                    'removed': list(cat_set1 - cat_set2),
                    'common': list(cat_set1 & cat_set2),
                    'count1': len(cat_set1),
                    'count2': len(cat_set2)
                }
            
            changes[f"{year1}_{year2}"] = {
                'added': list(added),
                'removed': list(removed),
                'common': list(common),
                'total_count1': len(set1),
                'total_count2': len(set2),
                'category_changes': category_changes
            }
            
            # Print summary
            print(f"总计: {len(set1)} → {len(set2)} 个计算关系")
            print(f"新增: {len(added)} 个")
            print(f"删除: {len(removed)} 个")
            print(f"保持: {len(common)} 个")
            
            # Print category breakdown
            print("\n按类别分析:")
            for category, cat_change in category_changes.items():
                if cat_change['count1'] > 0 or cat_change['count2'] > 0:
                    print(f"  {category}: {cat_change['count1']} → {cat_change['count2']} "
                          f"(新增{len(cat_change['added'])}, 删除{len(cat_change['removed'])})")
            
            # Print significant changes
            if added:
                print(f"\n新增的重要计算关系:")
                for calc in list(added)[:5]:  # Show top 5
                    print(f"  + {calc}")
                if len(added) > 5:
                    print(f"  ... 还有 {len(added) - 5} 个")
            
            if removed:
                print(f"\n删除的重要计算关系:")
                for calc in list(removed)[:5]:  # Show top 5
                    print(f"  - {calc}")
                if len(removed) > 5:
                    print(f"  ... 还有 {len(removed) - 5} 个")
            
            print()
        
        return changes
    
    def calculations_to_set(self, calculations):
        """将计算关系转换为集合用于比较"""
        calc_set = set()
        for category, calcs in calculations.items():
            for calc in calcs:
                key = f"{calc['from_concept']}_{calc['operator']}_{calc['to_concept']}"
                calc_set.add(key)
        return calc_set
    
    def category_calculations_to_set(self, calculations):
        """将特定类别的计算关系转换为集合"""
        calc_set = set()
        for calc in calculations:
            key = f"{calc['from_concept']}_{calc['operator']}_{calc['to_concept']}"
            calc_set.add(key)
        return calc_set
    
    def analyze_concept_evolution(self):
        """分析财务概念的演变"""
        print(f"=== {self.company} 财务概念演变分析 ===\n")
        
        years = sorted(self.data.keys())
        concept_timeline = defaultdict(list)
        
        # Build timeline for each concept
        for year in years:
            calculations = self.data[year]
            year_concepts = set()
            
            for category, calcs in calculations.items():
                for calc in calcs:
                    year_concepts.add(calc['from_concept'])
                    year_concepts.add(calc['to_concept'])
            
            for concept in year_concepts:
                concept_timeline[concept].append(year)
        
        # Analyze concept patterns
        always_present = []
        intermittent = []
        recent_additions = []
        discontinued = []
        
        for concept, timeline in concept_timeline.items():
            if len(timeline) == len(years):
                always_present.append(concept)
            elif timeline[0] == years[0]:
                if timeline[-1] == years[-1]:
                    intermittent.append((concept, timeline))
                else:
                    discontinued.append((concept, timeline))
            else:
                recent_additions.append((concept, timeline))
        
        print(f"持续存在的概念 ({len(always_present)} 个):")
        for concept in always_present[:10]:  # Show top 10
            print(f"  {concept}")
        if len(always_present) > 10:
            print(f"  ... 还有 {len(always_present) - 10} 个")
        
        print(f"\n间歇性出现的概念 ({len(intermittent)} 个):")
        for concept, timeline in intermittent[:5]:
            print(f"  {concept}: {timeline}")
        if len(intermittent) > 5:
            print(f"  ... 还有 {len(intermittent) - 5} 个")
        
        print(f"\n最近新增的概念 ({len(recent_additions)} 个):")
        for concept, timeline in sorted(recent_additions, key=lambda x: x[1][0])[:5]:
            print(f"  {concept}: {timeline[0]}年首次出现")
        if len(recent_additions) > 5:
            print(f"  ... 还有 {len(recent_additions) - 5} 个")
        
        print(f"\n停止使用的概念 ({len(discontinued)} 个):")
        for concept, timeline in sorted(discontinued, key=lambda x: x[1][-1])[:5]:
            print(f"  {concept}: 使用至{timeline[-1]}年")
        if len(discontinued) > 5:
            print(f"  ... 还有 {len(discontinued) - 5} 个")
        
        return {
            'always_present': always_present,
            'intermittent': intermittent,
            'recent_additions': recent_additions,
            'discontinued': discontinued
        }
    
    def analyze_complexity_trends(self):
        """分析计算复杂度趋势"""
        print(f"=== {self.company} 计算复杂度趋势分析 ===\n")
        
        years = sorted(self.data.keys())
        complexity_data = []
        
        for year in years:
            calculations = self.data[year]
            
            # Total calculations
            total_calcs = sum(len(calcs) for calcs in calculations.values())
            
            # By category
            category_counts = {}
            for category, calcs in calculations.items():
                category_counts[category] = len(calcs)
            
            # Unique concepts
            concepts = set()
            for category, calcs in calculations.items():
                for calc in calcs:
                    concepts.add(calc['from_concept'])
                    concepts.add(calc['to_concept'])
            
            complexity_data.append({
                'year': year,
                'total_calculations': total_calcs,
                'unique_concepts': len(concepts),
                'category_counts': category_counts
            })
        
        # Print trend analysis
        print("历年复杂度变化:")
        for i, data in enumerate(complexity_data):
            year = data['year']
            total = data['total_calculations']
            concepts = data['unique_concepts']
            
            if i > 0:
                prev_total = complexity_data[i-1]['total_calculations']
                prev_concepts = complexity_data[i-1]['unique_concepts']
                total_change = total - prev_total
                concepts_change = concepts - prev_concepts
                total_pct = (total_change / prev_total * 100) if prev_total > 0 else 0
                concepts_pct = (concepts_change / prev_concepts * 100) if prev_concepts > 0 else 0
                
                print(f"  {year}: {total} 个计算关系 ({total_change:+d}, {total_pct:+.1f}%), "
                      f"{concepts} 个概念 ({concepts_change:+d}, {concepts_pct:+.1f}%)")
            else:
                print(f"  {year}: {total} 个计算关系, {concepts} 个概念 (基准年)")
        
        # Category trends
        print(f"\n按类别的趋势分析:")
        categories = list(complexity_data[0]['category_counts'].keys())
        
        for category in categories:
            print(f"\n{category}:")
            for i, data in enumerate(complexity_data):
                count = data['category_counts'].get(category, 0)
                if i > 0:
                    prev_count = complexity_data[i-1]['category_counts'].get(category, 0)
                    change = count - prev_count
                    if change != 0:
                        print(f"  {data['year']}: {count} ({change:+d})")
                    else:
                        print(f"  {data['year']}: {count}")
                else:
                    print(f"  {data['year']}: {count} (基准)")
        
        return complexity_data
    
    def generate_timeline_report(self, output_file=None):
        """生成时间线变化报告"""
        print(f"=== 生成 {self.company} 时间线报告 ===\n")
        
        years = sorted(self.data.keys())
        if len(years) < 2:
            print("需要至少2年的数据才能生成时间线报告")
            return
        
        report_content = []
        report_content.append(f"# {self.company} 财务计算逻辑时间线分析报告\n")
        report_content.append(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_content.append(f"分析年份: {', '.join(years)}\n")
        
        # Year-over-year changes
        changes = self.analyze_year_over_year_changes()
        report_content.append("## 逐年变化分析\n")
        
        for period, change_data in changes.items():
            year1, year2 = period.split('_')
            report_content.append(f"### {year1} → {year2}\n")
            report_content.append(f"- 总计算关系: {change_data['total_count1']} → {change_data['total_count2']}")
            report_content.append(f"- 新增关系: {len(change_data['added'])} 个")
            report_content.append(f"- 删除关系: {len(change_data['removed'])} 个")
            report_content.append(f"- 保持关系: {len(change_data['common'])} 个\n")
            
            # Category breakdown
            report_content.append("#### 按类别变化:\n")
            for category, cat_change in change_data['category_changes'].items():
                if cat_change['count1'] > 0 or cat_change['count2'] > 0:
                    report_content.append(f"- {category}: {cat_change['count1']} → {cat_change['count2']} "
                                        f"(新增{len(cat_change['added'])}, 删除{len(cat_change['removed'])})")
            report_content.append("")
        
        # Concept evolution
        report_content.append("## 财务概念演变\n")
        concept_evo = self.analyze_concept_evolution()
        
        report_content.append("### 持续存在的概念\n")
        for concept in concept_evo['always_present'][:15]:  # Show top 15
            report_content.append(f"- {concept}")
        if len(concept_evo['always_present']) > 15:
            report_content.append(f"- ... 还有 {len(concept_evo['always_present']) - 15} 个")
        report_content.append("")
        
        report_content.append("### 最近新增的概念\n")
        for concept, timeline in sorted(concept_evo['recent_additions'], key=lambda x: x[1][0])[:10]:
            report_content.append(f"- {concept}: {timeline[0]}年首次出现")
        if len(concept_evo['recent_additions']) > 10:
            report_content.append(f"- ... 还有 {len(concept_evo['recent_additions']) - 10} 个")
        report_content.append("")
        
        # Complexity trends
        report_content.append("## 复杂度趋势\n")
        complexity_data = self.analyze_complexity_trends()
        
        report_content.append("### 历年复杂度变化\n")
        report_content.append("| 年份 | 计算关系数 | 概念数 | 同比变化 |")
        report_content.append("|------|------------|--------|----------|")
        
        for i, data in enumerate(complexity_data):
            year = data['year']
            total = data['total_calculations']
            concepts = data['unique_concepts']
            
            if i > 0:
                prev_total = complexity_data[i-1]['total_calculations']
                change = total - prev_total
                pct = (change / prev_total * 100) if prev_total > 0 else 0
                report_content.append(f"| {year} | {total} | {concepts} | {change:+d} ({pct:+.1f}%) |")
            else:
                report_content.append(f"| {year} | {total} | {concepts} | 基准 |")
        
        # Save report
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(report_content))
            print(f"\n时间线报告已保存到: {output_file}")
        
        return '\n'.join(report_content)

def main():
    parser = argparse.ArgumentParser(description='Company Financial Calculation Logic Change Analysis')
    parser.add_argument('--calculations-dir', default='/Users/wangting/work/read_apple_10k/knowledge/financial_calculations',
                       help='Directory containing financial calculation markdown files')
    parser.add_argument('--company', required=True, 
                       help='Company symbol to analyze (e.g., AAPL, AMZN, GOOGL)')
    parser.add_argument('--output-dir', default='/Users/wangting/work/read_apple_10k/timeline_analysis',
                       help='Output directory for analysis results')
    parser.add_argument('--analysis-type', choices=['all', 'changes', 'concepts', 'complexity', 'timeline'],
                       default='all', help='Type of analysis to perform')
    
    args = parser.parse_args()
    
    # Create analyzer
    analyzer = CompanyCalculationChangeAnalyzer(args.calculations_dir, args.company)
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Execute analysis
    if args.analysis_type == 'all':
        analyzer.generate_timeline_report(output_dir / f'{args.company}_timeline_analysis.md')
    elif args.analysis_type == 'changes':
        analyzer.analyze_year_over_year_changes()
    elif args.analysis_type == 'concepts':
        analyzer.analyze_concept_evolution()
    elif args.analysis_type == 'complexity':
        analyzer.analyze_complexity_trends()
    elif args.analysis_type == 'timeline':
        analyzer.generate_timeline_report(output_dir / f'{args.company}_timeline_analysis.md')

if __name__ == "__main__":
    main()