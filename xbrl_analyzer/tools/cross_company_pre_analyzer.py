#!/usr/bin/env python3
"""
跨公司pre文件财务关系结构对比分析工具
Cross-Company Financial Relationship Structure Comparison Analyzer (pre files)

该工具分析多个公司pre.xml文件中财务关系结构的差异，识别行业实践、公司特色和共同模式。
"""

import os
import json
import pandas as pd
from pathlib import Path
from collections import defaultdict, Counter
import argparse
import re
from datetime import datetime
import numpy as np

class CrossCompanyPreRelationshipAnalyzer:
    def __init__(self, relationships_dir):
        self.relationships_dir = Path(relationships_dir)
        self.companies = ['AAPL', 'AMZN', 'GOOGL', 'META', 'MSFT', 'NVDA', 'TSLA']
        self.data = self.load_all_companies_data()
        
    def load_all_companies_data(self):
        """加载所有公司的pre关系数据"""
        data = {}
        
        for company in self.companies:
            company_dir = self.relationships_dir / company
            if not company_dir.exists():
                print(f"Warning: Company directory {company_dir} not found")
                continue
                
            company_data = {}
            
            for file_path in company_dir.glob(f"{company}_*_financial_relationships.md"):
                # Extract year from filename
                year_match = re.search(rf'{company}_(\d{{4}})_financial_relationships\.md', file_path.name)
                if year_match:
                    year = year_match.group(1)
                    relationships = self.parse_markdown_file(file_path)
                    company_data[year] = relationships
            
            if company_data:
                data[company] = dict(sorted(company_data.items()))
        
        return data
    
    def parse_markdown_file(self, file_path):
        """解析markdown文件提取财务关系结构"""
        relationships = {
            'income_statement': {},
            'balance_sheet': {},
            'cash_flow': {},
            'comprehensive_income': {},
            'eps': {},
            'financial_instruments': {},
            'other': {}
        }
        
        current_category = None
        current_role = None
        hierarchy = {}
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                # Detect category
                if line.startswith('## 损益表结构'):
                    current_category = 'income_statement'
                    current_role = None
                    hierarchy = {}
                elif line.startswith('## 资产负债表结构'):
                    current_category = 'balance_sheet'
                    current_role = None
                    hierarchy = {}
                elif line.startswith('## 现金流量表结构'):
                    current_category = 'cash_flow'
                    current_role = None
                    hierarchy = {}
                elif line.startswith('## 全面收益结构'):
                    current_category = 'comprehensive_income'
                    current_role = None
                    hierarchy = {}
                elif line.startswith('## 每股收益结构'):
                    current_category = 'eps'
                    current_role = None
                    hierarchy = {}
                elif line.startswith('## 金融工具结构'):
                    current_category = 'financial_instruments'
                    current_role = None
                    hierarchy = {}
                elif line.startswith('## 其他结构'):
                    current_category = 'other'
                    current_role = None
                    hierarchy = {}
                
                # Detect role (subsection)
                elif line.startswith('### http'):
                    if current_role:
                        relationships[current_category][current_role] = hierarchy.copy()
                    current_role = line
                    hierarchy = {}
                
                # Parse hierarchy relationships
                elif line.startswith('- '):
                    # Parse indentation level
                    indent_level = len(line) - len(line.lstrip())
                    concept = line[2:].strip()
                    
                    # Remove [totalLabel] if present
                    is_total = '[totalLabel]' in concept
                    if is_total:
                        concept = concept.replace(' [totalLabel]', '').strip()
                    
                    # Find parent based on indentation
                    parent = self.find_parent_by_indentation(hierarchy, indent_level)
                    
                    # Add to hierarchy
                    if concept not in hierarchy:
                        hierarchy[concept] = {
                            'parent': parent,
                            'children': [],
                            'is_total': is_total,
                            'level': indent_level // 2
                        }
                    
                    if parent and parent in hierarchy:
                        if concept not in hierarchy[parent]['children']:
                            hierarchy[parent]['children'].append(concept)
            
            # Add the last role
            if current_role and current_category:
                relationships[current_category][current_role] = hierarchy.copy()
        
        return relationships
    
    def find_parent_by_indentation(self, hierarchy, indent_level):
        """根据缩进级别查找父概念"""
        if indent_level == 0:
            return None
        
        parent_level = (indent_level // 2) - 1
        for concept, data in hierarchy.items():
            if data['level'] == parent_level:
                return concept
        return None
    
    def analyze_cross_company_structure_differences(self):
        """分析跨公司结构差异"""
        print("=== 跨公司财务关系结构差异分析 ===\n")
        
        # 收集所有公司的最新年份数据
        latest_data = {}
        for company, years_data in self.data.items():
            if years_data:
                latest_year = max(years_data.keys())
                latest_data[company] = years_data[latest_year]
        
        if not latest_data:
            print("没有找到可用的数据")
            return {}
        
        # 分析角色使用差异
        print("1. 各公司财务角色使用情况:")
        role_usage = self.analyze_role_usage(latest_data)
        
        # 分析概念使用差异
        print("\n2. 各公司财务概念使用情况:")
        concept_usage = self.analyze_concept_usage(latest_data)
        
        # 分析结构复杂度差异
        print("\n3. 各公司结构复杂度对比:")
        complexity_analysis = self.analyze_complexity_differences(latest_data)
        
        # 分析行业共同模式
        print("\n4. 行业共同实践分析:")
        common_patterns = self.analyze_common_patterns(latest_data)
        
        # 分析公司特色实践
        print("\n5. 公司特色实践分析:")
        unique_practices = self.analyze_unique_practices(latest_data)
        
        return {
            'role_usage': role_usage,
            'concept_usage': concept_usage,
            'complexity_analysis': complexity_analysis,
            'common_patterns': common_patterns,
            'unique_practices': unique_practices,
            'latest_data': latest_data
        }
    
    def analyze_role_usage(self, data):
        """分析角色使用情况"""
        role_stats = defaultdict(lambda: defaultdict(int))
        role_companies = defaultdict(set)
        
        for company, relationships in data.items():
            for category, roles in relationships.items():
                for role in roles.keys():
                    role_stats[company][category] += 1
                    role_companies[category].add(company)
        
        # 打印统计
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
        
        print("各公司角色数量统计:")
        print("-" * 80)
        print(f"{'公司':<8} " + " ".join([f"{category_names[cat]:<8}" for cat in categories]))
        print("-" * 80)
        
        for company in sorted(data.keys()):
            row = [company]
            for category in categories:
                count = role_stats[company][category]
                row.append(f"{count}")
            print(" ".join([f"{item:<8}" for item in row]))
        
        # 分析普及率
        print(f"\n角色普及率分析:")
        for category in categories:
            companies_using = len(role_companies[category])
            total_companies = len(data)
            usage_rate = companies_using / total_companies * 100
            print(f"  {category_names[category]}: {companies_using}/{total_companies}家公司使用 ({usage_rate:.1f}%)")
        
        return role_stats
    
    def analyze_concept_usage(self, data):
        """分析概念使用情况"""
        concept_companies = defaultdict(set)
        concept_categories = defaultdict(lambda: defaultdict(set))
        company_concepts = defaultdict(set)
        
        for company, relationships in data.items():
            all_company_concepts = set()
            
            for category, roles in relationships.items():
                for role, hierarchy in roles.items():
                    concepts = self.extract_all_concepts(hierarchy)
                    all_company_concepts.update(concepts)
                    
                    for concept in concepts:
                        concept_companies[concept].add(company)
                        concept_categories[company][concept].add(category)
            
            company_concepts[company] = all_company_concepts
        
        # 分析高频概念
        print("最常用的财务概念 (Top 20):")
        concept_frequency = {concept: len(companies) for concept, companies in concept_companies.items()}
        sorted_concepts = sorted(concept_frequency.items(), key=lambda x: x[1], reverse=True)[:20]
        
        for i, (concept, count) in enumerate(sorted_concepts, 1):
            companies_using = concept_companies[concept]
            print(f"{i:2d}. {concept}")
            print(f"    使用公司: {', '.join(sorted(companies_using))} ({count}/{len(data)})")
        
        # 分析公司特有概念
        print(f"\n各公司特有概念:")
        for company in sorted(data.keys()):
            unique_concepts = []
            for concept in company_concepts[company]:
                if len(concept_companies[concept]) == 1 and list(concept_companies[concept])[0] == company:
                    unique_concepts.append(concept)
            
            if unique_concepts:
                print(f"  {company}: {len(unique_concepts)} 个特有概念")
                for concept in unique_concepts[:3]:  # 显示前3个
                    categories = concept_categories[company][concept]
                    print(f"    - {concept} (用于: {', '.join(categories)})")
                if len(unique_concepts) > 3:
                    print(f"    ... 还有 {len(unique_concepts) - 3} 个")
        
        return {
            'concept_frequency': concept_frequency,
            'company_concepts': company_concepts,
            'concept_companies': concept_companies
        }
    
    def extract_all_concepts(self, hierarchy):
        """提取层级结构中的所有概念"""
        concepts = set()
        for concept, data in hierarchy.items():
            concepts.add(concept)
            concepts.update(self.extract_all_concepts_recursive(data))
        return concepts
    
    def extract_all_concepts_recursive(self, node_data):
        """递归提取所有子概念"""
        concepts = set()
        for child in node_data.get('children', []):
            concepts.add(child)
        return concepts
    
    def analyze_complexity_differences(self, data):
        """分析复杂度差异"""
        complexity_stats = {}
        
        for company, relationships in data.items():
            total_concepts = 0
            total_roles = 0
            category_stats = {}
            
            for category, roles in relationships.items():
                role_count = len(roles)
                concept_count = sum(len(hierarchy) for hierarchy in roles.values())
                
                category_stats[category] = {
                    'roles': role_count,
                    'concepts': concept_count
                }
                
                total_roles += role_count
                total_concepts += concept_count
            
            complexity_stats[company] = {
                'total_concepts': total_concepts,
                'total_roles': total_roles,
                'avg_concepts_per_role': total_concepts / total_roles if total_roles > 0 else 0,
                'category_stats': category_stats
            }
        
        # 排名分析
        print("按总概念数排名:")
        by_concepts = sorted(complexity_stats.items(), key=lambda x: x[1]['total_concepts'], reverse=True)
        for i, (company, stats) in enumerate(by_concepts, 1):
            print(f"{i}. {company}: {stats['total_concepts']} 个概念, {stats['total_roles']} 个角色")
        
        print(f"\n按平均每个角色概念数排名:")
        by_avg = sorted(complexity_stats.items(), key=lambda x: x[1]['avg_concepts_per_role'], reverse=True)
        for i, (company, stats) in enumerate(by_avg, 1):
            print(f"{i}. {company}: 平均 {stats['avg_concepts_per_role']:.1f} 个概念/角色")
        
        return complexity_stats
    
    def analyze_common_patterns(self, data):
        """分析行业共同模式"""
        # 找出所有公司都使用的概念
        common_concepts = set()
        company_concept_sets = {}
        
        for company, relationships in data.items():
            company_concepts = set()
            for category, roles in relationships.items():
                for role, hierarchy in roles.items():
                    company_concepts.update(self.extract_all_concepts(hierarchy))
            
            company_concept_sets[company] = company_concepts
            
            if not common_concepts:
                common_concepts = company_concepts.copy()
            else:
                common_concepts &= company_concepts
        
        print(f"所有公司都使用的核心概念 ({len(common_concepts)} 个):")
        for concept in sorted(list(common_concepts))[:15]:  # 显示前15个
            print(f"  - {concept}")
        if len(common_concepts) > 15:
            print(f"  ... 还有 {len(common_concepts) - 15} 个")
        
        # 分析角色使用模式
        common_roles = defaultdict(int)
        for company, relationships in data.items():
            roles_used = set()
            for category, roles in relationships.items():
                for role in roles.keys():
                    # 只使用role的最后一部分作为模式识别
                    role_name = role.split('/')[-1] if '/' in role else role
                    roles_used.add(role_name)
            
            for role_name in roles_used:
                common_roles[role_name] += 1
        
        print(f"\n常用角色模式 (6/7家公司以上使用):")
        for role_name, count in sorted(common_roles.items(), key=lambda x: x[1], reverse=True):
            if count >= 6:
                print(f"  {role_name}: {count}/{len(data)} 家公司")
        
        return {
            'common_concepts': common_concepts,
            'common_role_patterns': common_roles
        }
    
    def analyze_unique_practices(self, data):
        """分析公司特色实践"""
        unique_practices = {}
        
        for company, relationships in data.items():
            company_practices = {
                'unique_roles': [],
                'unique_structures': [],
                'complexity_characteristics': ''
            }
            
            # 找出特有角色
            all_roles = set()
            for category, roles in relationships.items():
                for role in roles.keys():
                    all_roles.add(role)
            
            # 检查哪些角色是这家公司特有的
            for role in all_roles:
                other_companies_have_this_role = False
                for other_company, other_relationships in data.items():
                    if other_company == company:
                        continue
                    
                    for category, roles in other_relationships.items():
                        if role in roles:
                            other_companies_have_this_role = True
                            break
                    
                    if other_companies_have_this_role:
                        break
                
                if not other_companies_have_this_role:
                    company_practices['unique_roles'].append(role)
            
            # 分析复杂度特征
            total_concepts = sum(len(hierarchy) for roles in relationships.values() for hierarchy in roles.values())
            total_roles = sum(len(roles) for roles in relationships.values())
            avg_complexity = total_concepts / total_roles if total_roles > 0 else 0
            
            if avg_complexity > 8:
                company_practices['complexity_characteristics'] = '高复杂度'
            elif avg_complexity < 5:
                company_practices['complexity_characteristics'] = '低复杂度'
            else:
                company_practices['complexity_characteristics'] = '中等复杂度'
            
            unique_practices[company] = company_practices
        
        # 打印特色实践
        for company, practices in unique_practices.items():
            print(f"\n{company} 特色实践:")
            print(f"  复杂度特征: {practices['complexity_characteristics']}")
            
            if practices['unique_roles']:
                print(f"  特有角色 ({len(practices['unique_roles'])} 个):")
                for role in practices['unique_roles'][:3]:  # 显示前3个
                    role_short = role.split('/')[-1] if '/' in role else role
                    print(f"    - {role_short}")
                if len(practices['unique_roles']) > 3:
                    print(f"    ... 还有 {len(practices['unique_roles']) - 3} 个")
            else:
                print(f"  无特有角色，采用标准化实践")
        
        return unique_practices
    
    def analyze_temporal_trends_comparison(self):
        """分析跨公司时间趋势对比"""
        print("=== 跨公司时间趋势对比分析 ===\n")
        
        # 收集各公司的历年数据
        temporal_data = {}
        
        for company, years_data in self.data.items():
            company_trends = []
            
            for year in sorted(years_data.keys()):
                relationships = years_data[year]
                
                total_concepts = sum(len(hierarchy) for roles in relationships.values() for hierarchy in roles.values())
                total_roles = sum(len(roles) for roles in relationships.values())
                
                company_trends.append({
                    'year': year,
                    'total_concepts': total_concepts,
                    'total_roles': total_roles,
                    'complexity_ratio': total_concepts / total_roles if total_roles > 0 else 0
                })
            
            temporal_data[company] = company_trends
        
        # 分析趋势
        print("各公司复杂度趋势:")
        years = sorted(set(item['year'] for company_data in temporal_data.values() for item in company_data))
        
        print(f"{'年份':<6} " + " ".join([f"{company:<10}" for company in sorted(temporal_data.keys())]))
        print("-" * (6 + 10 * len(temporal_data)))
        
        for year in years:
            row = [f"{year}"]
            for company in sorted(temporal_data.keys()):
                year_data = next((item for item in temporal_data[company] if item['year'] == year), None)
                if year_data:
                    row.append(f"{year_data['total_concepts']:<10}")
                else:
                    row.append("N/A       ")
            print(" ".join(row))
        
        # 计算变化趋势
        print(f"\n复杂度变化趋势 (2020-2024):")
        for company, trends in temporal_data.items():
            # 找到2020年和2024年的数据
            data_2020 = next((item for item in trends if item['year'] == '2020'), None)
            data_2024 = next((item for item in trends if item['year'] == '2024'), None)
            
            if data_2020 and data_2024:
                change = data_2024['total_concepts'] - data_2020['total_concepts']
                pct_change = (change / data_2020['total_concepts'] * 100) if data_2020['total_concepts'] > 0 else 0
                print(f"  {company}: {data_2020['total_concepts']} → {data_2024['total_concepts']} ({change:+d}, {pct_change:+.1f}%)")
        
        return temporal_data
    
    def generate_comprehensive_report(self, output_file=None):
        """生成综合对比报告"""
        print("=== 生成跨公司pre文件综合对比报告 ===\n")
        
        # 执行所有分析
        structure_analysis = self.analyze_cross_company_structure_differences()
        temporal_analysis = self.analyze_temporal_trends_comparison()
        
        report_content = []
        report_content.append("# 跨公司财务关系结构对比分析报告 (pre文件)\n")
        report_content.append(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_content.append(f"涵盖公司: {', '.join(self.companies)}\n")
        
        # 结构差异分析
        report_content.append("## 跨公司结构差异分析\n")
        
        # 复杂度排名
        report_content.append("### 公司复杂度排名\n")
        complexity_data = structure_analysis['complexity_analysis']
        by_concepts = sorted(complexity_data.items(), key=lambda x: x[1]['total_concepts'], reverse=True)
        
        report_content.append("| 排名 | 公司 | 总概念数 | 总角色数 | 平均概念/角色 |")
        report_content.append("|------|------|----------|----------|---------------|")
        
        for i, (company, stats) in enumerate(by_concepts, 1):
            report_content.append(f"| {i} | {company} | {stats['total_concepts']} | {stats['total_roles']} | {stats['avg_concepts_per_role']:.1f} |")
        
        report_content.append("")
        
        # 共同模式
        report_content.append("### 行业共同实践\n")
        common_concepts = structure_analysis['common_patterns']['common_concepts']
        report_content.append(f"**所有公司都使用的核心概念 ({len(common_concepts)} 个):**\n")
        
        for concept in sorted(list(common_concepts))[:20]:  # 显示前20个
            report_content.append(f"- {concept}")
        
        if len(common_concepts) > 20:
            report_content.append(f"- ... 还有 {len(common_concepts) - 20} 个")
        
        report_content.append("")
        
        # 公司特色
        report_content.append("### 公司特色实践\n")
        unique_practices = structure_analysis['unique_practices']
        
        for company, practices in unique_practices.items():
            report_content.append(f"#### {company}\n")
            report_content.append(f"- **复杂度特征**: {practices['complexity_characteristics']}\n")
            
            if practices['unique_roles']:
                report_content.append(f"- **特有角色** ({len(practices['unique_roles'])} 个):\n")
                for role in practices['unique_roles'][:5]:  # 显示前5个
                    report_content.append(f"  - {role}")
                if len(practices['unique_roles']) > 5:
                    report_content.append(f"  - ... 还有 {len(practices['unique_roles']) - 5} 个")
            else:
                report_content.append("- **特有角色**: 无特有角色，采用标准化实践")
            
            report_content.append("")
        
        # 时间趋势分析
        report_content.append("## 时间趋势对比分析\n")
        
        # 生成趋势表格
        years = sorted(set(item['year'] for company_data in temporal_analysis.values() for item in company_data))
        
        report_content.append("### 各公司历年概念数量变化\n")
        report_content.append("| 年份 | " + " | ".join(sorted(temporal_analysis.keys())) + " |")
        report_content.append("|------|" + "|".join(["-" * len(company) for company in sorted(temporal_analysis.keys())]) + "|")
        
        for year in years:
            row = [f"| {year}"]
            for company in sorted(temporal_analysis.keys()):
                year_data = next((item for item in temporal_analysis[company] if item['year'] == year), None)
                if year_data:
                    row.append(f" {year_data['total_concepts']} ")
                else:
                    row.append(" N/A ")
            row.append("|")
            report_content.append("|".join(row))
        
        report_content.append("")
        
        # 2020-2024变化分析
        report_content.append("### 2020-2024年复杂度变化\n")
        report_content.append("| 公司 | 2020年概念数 | 2024年概念数 | 变化 | 变化率 |")
        report_content.append("|------|-------------|-------------|------|--------|")
        
        for company, trends in temporal_analysis.items():
            data_2020 = next((item for item in trends if item['year'] == '2020'), None)
            data_2024 = next((item for item in trends if item['year'] == '2024'), None)
            
            if data_2020 and data_2024:
                change = data_2024['total_concepts'] - data_2020['total_concepts']
                pct_change = (change / data_2020['total_concepts'] * 100) if data_2020['total_concepts'] > 0 else 0
                report_content.append(f"| {company} | {data_2020['total_concepts']} | {data_2024['total_concepts']} | {change:+d} | {pct_change:+.1f}% |")
        
        report_content.append("")
        
        # 保存报告
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(report_content))
            print(f"\n跨公司对比报告已保存到: {output_file}")
        
        return '\n'.join(report_content)

def main():
    parser = argparse.ArgumentParser(description='Cross-Company Financial Relationship Structure Comparison Analysis')
    parser.add_argument('--relationships-dir', default='/Users/wangting/work/read_apple_10k/knowledge/financial_relationships',
                       help='Directory containing financial relationship markdown files')
    parser.add_argument('--output-dir', default='/Users/wangting/work/read_apple_10k/cross_company_pre_analysis',
                       help='Output directory for analysis results')
    parser.add_argument('--analysis-type', choices=['all', 'structure', 'temporal', 'comparison'],
                       default='all', help='Type of analysis to perform')
    
    args = parser.parse_args()
    
    # Create analyzer
    analyzer = CrossCompanyPreRelationshipAnalyzer(args.relationships_dir)
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Execute analysis
    if args.analysis_type == 'all':
        analyzer.generate_comprehensive_report(output_dir / 'cross_company_pre_comparison_report.md')
    elif args.analysis_type == 'structure':
        analyzer.analyze_cross_company_structure_differences()
    elif args.analysis_type == 'temporal':
        analyzer.analyze_temporal_trends_comparison()
    elif args.analysis_type == 'comparison':
        analyzer.generate_comprehensive_report(output_dir / 'cross_company_pre_comparison_report.md')

if __name__ == "__main__":
    main()