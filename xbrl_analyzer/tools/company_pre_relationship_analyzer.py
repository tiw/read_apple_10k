#!/usr/bin/env python3
"""
公司历年pre文件财务关系变化分析工具
Company Year-over-Year Financial Relationship Change Analyzer (pre files)

该工具分析单个公司历年来pre.xml文件中财务关系结构的变化，识别新增、删除和修改的财务概念层级关系。
"""

import os
import json
import pandas as pd
from pathlib import Path
from collections import defaultdict, Counter
import argparse
import re
from datetime import datetime
import xml.etree.ElementTree as ET

class CompanyPreRelationshipAnalyzer:
    def __init__(self, relationships_dir, company):
        self.relationships_dir = Path(relationships_dir)
        self.company = company
        self.data = self.load_company_relationships()
        
    def load_company_relationships(self):
        """加载指定公司的所有pre关系数据"""
        data = {}
        
        company_dir = self.relationships_dir / self.company
        if not company_dir.exists():
            print(f"Warning: Company directory {company_dir} not found")
            return {}
            
        for file_path in company_dir.glob(f"{self.company}_*_financial_relationships.md"):
            # Extract year from filename
            year_match = re.search(rf'{self.company}_(\d{{4}})_financial_relationships\.md', file_path.name)
            if year_match:
                year = year_match.group(1)
                relationships = self.parse_markdown_file(file_path)
                data[year] = relationships
        
        # Sort by year
        return dict(sorted(data.items()))
    
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
                            'level': indent_level // 2  # Assuming 2 spaces per level
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
    
    def analyze_year_over_year_changes(self):
        """分析逐年变化"""
        print(f"=== {self.company} 历年财务关系结构变化分析 ===\n")
        
        years = sorted(self.data.keys())
        if len(years) < 2:
            print("需要至少2年的数据才能进行变化分析")
            return {}
        
        changes = {}
        
        for i in range(len(years) - 1):
            year1 = years[i]
            year2 = years[i + 1]
            
            print(f"--- {year1} → {year2} 变化分析 ---")
            
            # Get relationships for both years
            rel1 = self.data[year1]
            rel2 = self.data[year2]
            
            # Analyze changes
            year_changes = self.compare_relationship_structures(rel1, rel2, year1, year2)
            changes[f"{year1}_{year2}"] = year_changes
            
            # Print summary
            self.print_change_summary(year_changes, year1, year2)
        
        return changes
    
    def compare_relationship_structures(self, rel1, rel2, year1, year2):
        """比较两个年份的关系结构"""
        changes = {
            'category_changes': {},
            'role_changes': {},
            'concept_changes': {
                'added': [],
                'removed': [],
                'modified': []
            },
            'statistics': {
                'year1': self.calculate_statistics(rel1),
                'year2': self.calculate_statistics(rel2)
            }
        }
        
        # Compare each category
        all_categories = set(rel1.keys()) | set(rel2.keys())
        
        for category in all_categories:
            cat1 = rel1.get(category, {})
            cat2 = rel2.get(category, {})
            
            # Compare roles within category
            all_roles = set(cat1.keys()) | set(cat2.keys())
            
            for role in all_roles:
                if role in cat1 and role in cat2:
                    # Both years have this role - compare concepts
                    concepts1 = self.extract_all_concepts(cat1[role])
                    concepts2 = self.extract_all_concepts(cat2[role])
                    
                    added = concepts2 - concepts1
                    removed = concepts1 - concepts2
                    common = concepts1 & concepts2
                    
                    if added or removed:
                        if category not in changes['role_changes']:
                            changes['role_changes'][category] = {}
                        
                        changes['role_changes'][category][role] = {
                            'added_concepts': list(added),
                            'removed_concepts': list(removed),
                            'common_concepts': list(common),
                            'structure_change': self.compare_structure(cat1[role], cat2[role])
                        }
                        
                        changes['concept_changes']['added'].extend([(role, concept) for concept in added])
                        changes['concept_changes']['removed'].extend([(role, concept) for concept in removed])
                
                elif role in cat1:
                    # Role removed in year2
                    if category not in changes['role_changes']:
                        changes['role_changes'][category] = {}
                    changes['role_changes'][category][role] = {'status': 'removed'}
                    concepts = self.extract_all_concepts(cat1[role])
                    changes['concept_changes']['removed'].extend([(role, concept) for concept in concepts])
                
                else:
                    # Role added in year2
                    if category not in changes['role_changes']:
                        changes['role_changes'][category] = {}
                    changes['role_changes'][category][role] = {'status': 'added'}
                    concepts = self.extract_all_concepts(cat2[role])
                    changes['concept_changes']['added'].extend([(role, concept) for concept in concepts])
        
        # Analyze specific metric changes
        metric_changes = self.analyze_specific_metric_changes(rel1, rel2)
        changes['metric_changes'] = metric_changes
        
        return changes
    
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
    
    def compare_structure(self, hierarchy1, hierarchy2):
        """比较两个层级结构的差异"""
        differences = []
        
        for concept in hierarchy1:
            if concept in hierarchy2:
                # Compare parent relationships
                parent1 = hierarchy1[concept]['parent']
                parent2 = hierarchy2[concept]['parent']
                if parent1 != parent2:
                    differences.append(f"{concept}: parent {parent1} → {parent2}")
                
                # Compare children
                children1 = set(hierarchy1[concept]['children'])
                children2 = set(hierarchy2[concept]['children'])
                if children1 != children2:
                    added_children = children2 - children1
                    removed_children = children1 - children2
                    diff_desc = []
                    if added_children:
                        diff_desc.append(f"added {list(added_children)}")
                    if removed_children:
                        diff_desc.append(f"removed {list(removed_children)}")
                    differences.append(f"{concept}: children {', '.join(diff_desc)}")
            else:
                differences.append(f"{concept}: removed")
        
        for concept in hierarchy2:
            if concept not in hierarchy1:
                differences.append(f"{concept}: added")
        
        return differences
    
    def analyze_specific_metric_changes(self, rel1, rel2):
        """分析具体财务指标的变化"""
        # Extract all unique concepts from both years
        concepts1 = set()
        concepts2 = set()
        
        for category, roles in rel1.items():
            for role, hierarchy in roles.items():
                concepts1.update(self.extract_all_concepts(hierarchy))
        
        for category, roles in rel2.items():
            for role, hierarchy in roles.items():
                concepts2.update(self.extract_all_concepts(hierarchy))
        
        # Find new and removed metrics
        new_metrics = concepts2 - concepts1
        removed_metrics = concepts1 - concepts2
        
        # Find metrics with changed hierarchy structure
        hierarchy_changes = []
        
        # Build hierarchy mappings for both years
        hierarchy_map1 = self.build_hierarchy_map(rel1)
        hierarchy_map2 = self.build_hierarchy_map(rel2)
        
        # Check for hierarchy changes in common metrics
        common_metrics = concepts1 & concepts2
        for metric in common_metrics:
            if metric in hierarchy_map1 and metric in hierarchy_map2:
                hierarchy1 = hierarchy_map1[metric]
                hierarchy2 = hierarchy_map2[metric]
                
                if hierarchy1 != hierarchy2:
                    # Find what changed
                    changes = []
                    
                    # Check for parent changes
                    parent1 = hierarchy1.get('parent')
                    parent2 = hierarchy2.get('parent')
                    if parent1 != parent2:
                        changes.append(f"父概念变化: {parent1} → {parent2}")
                    
                    # Check for role changes
                    role1 = hierarchy1.get('role')
                    role2 = hierarchy2.get('role')
                    if role1 != role2:
                        role_name1 = role1.split('/')[-1] if '/' in role1 else role1
                        role_name2 = role2.split('/')[-1] if '/' in role2 else role2
                        changes.append(f"角色变化: {role_name1} → {role_name2}")
                    
                    # Check for level changes
                    level1 = hierarchy1.get('level', 0)
                    level2 = hierarchy2.get('level', 0)
                    if level1 != level2:
                        changes.append(f"层级变化: {level1} → {level2}")
                    
                    # Check for total label changes
                    is_total1 = hierarchy1.get('is_total', False)
                    is_total2 = hierarchy2.get('is_total', False)
                    if is_total1 != is_total2:
                        changes.append(f"总计标签变化: {'是' if is_total1 else '否'} → {'是' if is_total2 else '否'}")
                    
                    if changes:
                        hierarchy_changes.append((metric, changes))
        
        return {
            'new_metrics': list(new_metrics),
            'removed_metrics': list(removed_metrics),
            'hierarchy_changes': hierarchy_changes
        }
    
    def build_hierarchy_map(self, relationships):
        """构建指标到层级结构的映射"""
        hierarchy_map = {}
        
        for category, roles in relationships.items():
            for role, hierarchy in roles.items():
                for concept, data in hierarchy.items():
                    hierarchy_map[concept] = {
                        'parent': data.get('parent'),
                        'role': role,
                        'level': data.get('level', 0),
                        'is_total': data.get('is_total', False),
                        'category': category
                    }
        
        return hierarchy_map
    
    def calculate_statistics(self, relationships):
        """计算关系统计信息"""
        stats = {
            'total_roles': 0,
            'total_concepts': 0,
            'categories': {}
        }
        
        for category, roles in relationships.items():
            category_stats = {
                'roles': len(roles),
                'concepts': 0
            }
            
            for role, hierarchy in roles.items():
                category_stats['concepts'] += len(hierarchy)
            
            stats['categories'][category] = category_stats
            stats['total_roles'] += category_stats['roles']
            stats['total_concepts'] += category_stats['concepts']
        
        return stats
    
    def print_change_summary(self, changes, year1, year2):
        """打印变化摘要"""
        stats1 = changes['statistics']['year1']
        stats2 = changes['statistics']['year2']
        
        print(f"总计: {stats1['total_concepts']} → {stats2['total_concepts']} 个概念")
        print(f"      {stats1['total_roles']} → {stats2['total_roles']} 个角色")
        
        added_concepts = len(changes['concept_changes']['added'])
        removed_concepts = len(changes['concept_changes']['removed'])
        
        print(f"新增概念: {added_concepts} 个")
        print(f"删除概念: {removed_concepts} 个")
        
        # Category breakdown
        print("\n按类别分析:")
        for category in stats1['categories'].keys():
            cat1 = stats1['categories'].get(category, {'roles': 0, 'concepts': 0})
            cat2 = stats2['categories'].get(category, {'roles': 0, 'concepts': 0})
            
            if cat1['concepts'] > 0 or cat2['concepts'] > 0:
                roles_change = cat2['roles'] - cat1['roles']
                concepts_change = cat2['concepts'] - cat1['concepts']
                print(f"  {category}: {cat1['concepts']} → {cat2['concepts']} 个概念 "
                      f"({concepts_change:+d}), {cat1['roles']} → {cat2['roles']} 个角色 ({roles_change:+d})")
        
        # Show significant changes
        if changes['role_changes']:
            print(f"\n重要结构变化:")
            for category, role_changes in changes['role_changes'].items():
                for role, change_data in role_changes.items():
                    if isinstance(change_data, dict) and 'added_concepts' in change_data:
                        if change_data['added_concepts'] or change_data['removed_concepts']:
                            role_name = role.split('/')[-1] if '/' in role else role
                            print(f"  {category}/{role_name}: "
                                  f"新增{len(change_data['added_concepts'])}, "
                                  f"删除{len(change_data['removed_concepts'])} 个概念")
                    elif change_data.get('status') == 'added':
                        role_name = role.split('/')[-1] if '/' in role else role
                        print(f"  {category}/{role_name}: 新增角色")
                    elif change_data.get('status') == 'removed':
                        role_name = role.split('/')[-1] if '/' in role else role
                        print(f"  {category}/{role_name}: 删除角色")
        
        # Print specific metric changes
        metric_changes = changes.get('metric_changes', {})
        if metric_changes.get('new_metrics'):
            print(f"\n新增的财务指标:")
            for metric in metric_changes['new_metrics'][:5]:
                print(f"  + {metric}")
            if len(metric_changes['new_metrics']) > 5:
                print(f"  ... 还有 {len(metric_changes['new_metrics']) - 5} 个")
        
        if metric_changes.get('removed_metrics'):
            print(f"\n删除的财务指标:")
            for metric in metric_changes['removed_metrics'][:5]:
                print(f"  - {metric}")
            if len(metric_changes['removed_metrics']) > 5:
                print(f"  ... 还有 {len(metric_changes['removed_metrics']) - 5} 个")
        
        if metric_changes.get('hierarchy_changes'):
            print(f"\n层级结构变化的指标:")
            for metric, changes in metric_changes['hierarchy_changes'][:5]:
                print(f"  ~ {metric}:")
                for change in changes:
                    print(f"    {change}")
            if len(metric_changes['hierarchy_changes']) > 5:
                print(f"  ... 还有 {len(metric_changes['hierarchy_changes']) - 5} 个")
        
        print()
    
    def analyze_concept_evolution(self):
        """分析财务概念的演变"""
        print(f"=== {self.company} 财务概念演变分析 (pre文件) ===\n")
        
        years = sorted(self.data.keys())
        concept_timeline = defaultdict(list)
        
        # Build timeline for each concept
        for year in years:
            relationships = self.data[year]
            year_concepts = set()
            
            for category, roles in relationships.items():
                for role, hierarchy in roles.items():
                    year_concepts.update(self.extract_all_concepts(hierarchy))
            
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
    
    def analyze_structure_complexity(self):
        """分析结构复杂度趋势"""
        print(f"=== {self.company} 财务关系结构复杂度趋势分析 ===\n")
        
        years = sorted(self.data.keys())
        complexity_data = []
        
        for year in years:
            relationships = self.data[year]
            
            # Calculate complexity metrics
            total_concepts = 0
            total_roles = 0
            max_depth = 0
            avg_children = 0
            
            category_stats = {}
            
            for category, roles in relationships.items():
                category_concepts = 0
                category_roles = len(roles)
                
                for role, hierarchy in roles.items():
                    category_concepts += len(hierarchy)
                    depth, children_count = self.analyze_hierarchy_depth(hierarchy)
                    max_depth = max(max_depth, depth)
                
                category_stats[category] = {
                    'concepts': category_concepts,
                    'roles': category_roles
                }
                
                total_concepts += category_concepts
                total_roles += category_roles
            
            if total_roles > 0:
                avg_children = total_concepts / total_roles
            
            complexity_data.append({
                'year': year,
                'total_concepts': total_concepts,
                'total_roles': total_roles,
                'max_depth': max_depth,
                'avg_children_per_role': avg_children,
                'category_stats': category_stats
            })
        
        # Print trend analysis
        print("历年结构复杂度变化:")
        for i, data in enumerate(complexity_data):
            year = data['year']
            concepts = data['total_concepts']
            roles = data['total_roles']
            depth = data['max_depth']
            avg_children = data['avg_children_per_role']
            
            if i > 0:
                prev_concepts = complexity_data[i-1]['total_concepts']
                prev_roles = complexity_data[i-1]['total_roles']
                concepts_change = concepts - prev_concepts
                roles_change = roles - prev_roles
                concepts_pct = (concepts_change / prev_concepts * 100) if prev_concepts > 0 else 0
                
                print(f"  {year}: {concepts} 个概念 ({concepts_change:+d}, {concepts_pct:+.1f}%), "
                      f"{roles} 个角色 ({roles_change:+d}), 最大深度 {depth}, 平均每个角色 {avg_children:.1f} 个概念")
            else:
                print(f"  {year}: {concepts} 个概念, {roles} 个角色, 最大深度 {depth}, 平均每个角色 {avg_children:.1f} 个概念 (基准年)")
        
        return complexity_data
    
    def analyze_hierarchy_depth(self, hierarchy, current_depth=0):
        """分析层级深度"""
        if not hierarchy:
            return current_depth, 0
        
        max_depth = current_depth
        total_children = len(hierarchy)
        
        for concept, data in hierarchy.items():
            child_depth, child_count = self.analyze_hierarchy_depth_recursive(data, current_depth + 1)
            max_depth = max(max_depth, child_depth)
            total_children += child_count
        
        return max_depth, total_children
    
    def analyze_hierarchy_depth_recursive(self, node_data, current_depth):
        """递归分析层级深度"""
        children = node_data.get('children', [])
        if not children:
            return current_depth, 0
        
        max_depth = current_depth
        total_children = len(children)
        
        # Build child hierarchy for recursion
        child_hierarchy = {}
        for child in children:
            child_hierarchy[child] = {
                'parent': node_data.get('parent'),
                'children': [],
                'is_total': False,
                'level': node_data.get('level', 0) + 1
            }
        
        for child, child_data in child_hierarchy.items():
            child_depth, child_count = self.analyze_hierarchy_depth_recursive(child_data, current_depth + 1)
            max_depth = max(max_depth, child_depth)
            total_children += child_count
        
        return max_depth, total_children
    
    def generate_timeline_report(self, output_file=None):
        """生成时间线变化报告"""
        print(f"=== 生成 {self.company} pre文件时间线报告 ===\n")
        
        years = sorted(self.data.keys())
        if len(years) < 2:
            print("需要至少2年的数据才能生成时间线报告")
            return
        
        report_content = []
        report_content.append(f"# {self.company} 财务关系结构时间线分析报告 (pre文件)\n")
        report_content.append(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_content.append(f"分析年份: {', '.join(years)}\n")
        
        # Year-over-year changes
        changes = self.analyze_year_over_year_changes()
        report_content.append("## 逐年变化分析\n")
        
        for period, change_data in changes.items():
            year1, year2 = period.split('_')
            stats1 = change_data['statistics']['year1']
            stats2 = change_data['statistics']['year2']
            
            report_content.append(f"### {year1} → {year2}\n")
            report_content.append(f"- 总概念数: {stats1['total_concepts']} → {stats2['total_concepts']}")
            report_content.append(f"- 总角色数: {stats1['total_roles']} → {stats2['total_roles']}")
            report_content.append(f"- 新增概念: {len(change_data['concept_changes']['added'])} 个")
            report_content.append(f"- 删除概念: {len(change_data['concept_changes']['removed'])} 个\n")
            
            # Category breakdown
            report_content.append("#### 按类别变化:\n")
            for category in stats1['categories'].keys():
                cat1 = stats1['categories'].get(category, {'roles': 0, 'concepts': 0})
                cat2 = stats2['categories'].get(category, {'roles': 0, 'concepts': 0})
                
                if cat1['concepts'] > 0 or cat2['concepts'] > 0:
                    roles_change = cat2['roles'] - cat1['roles']
                    concepts_change = cat2['concepts'] - cat1['concepts']
                    report_content.append(f"- {category}: {cat1['concepts']} → {cat2['concepts']} 个概念 "
                                        f"({concepts_change:+d}), {cat1['roles']} → {cat2['roles']} 个角色 ({roles_change:+d})")
            report_content.append("")
            
            # Add detailed metric changes to report
            metric_changes = change_data.get('metric_changes', {})
            if metric_changes.get('new_metrics'):
                report_content.append("#### 新增的财务指标\n")
                for metric in metric_changes['new_metrics'][:10]:
                    report_content.append(f"- {metric}")
                if len(metric_changes['new_metrics']) > 10:
                    report_content.append(f"- ... 还有 {len(metric_changes['new_metrics']) - 10} 个")
                report_content.append("")
            
            if metric_changes.get('removed_metrics'):
                report_content.append("#### 删除的财务指标\n")
                for metric in metric_changes['removed_metrics'][:10]:
                    report_content.append(f"- {metric}")
                if len(metric_changes['removed_metrics']) > 10:
                    report_content.append(f"- ... 还有 {len(metric_changes['removed_metrics']) - 10} 个")
                report_content.append("")
            
            if metric_changes.get('hierarchy_changes'):
                report_content.append("#### 层级结构变化的指标\n")
                for metric, changes in metric_changes['hierarchy_changes'][:10]:
                    report_content.append(f"- {metric}:")
                    for change in changes:
                        report_content.append(f"  - {change}")
                if len(metric_changes['hierarchy_changes']) > 10:
                    report_content.append(f"- ... 还有 {len(metric_changes['hierarchy_changes']) - 10} 个")
                report_content.append("")
        
        # Concept evolution
        report_content.append("## 财务概念演变\n")
        concept_evo = self.analyze_concept_evolution()
        
        report_content.append("### 持续存在的核心概念\n")
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
        
        # Structure complexity
        report_content.append("## 结构复杂度趋势\n")
        complexity_data = self.analyze_structure_complexity()
        
        report_content.append("### 历年复杂度变化\n")
        report_content.append("| 年份 | 概念数 | 角色数 | 最大深度 | 平均每个角色概念数 | 同比变化 |")
        report_content.append("|------|--------|--------|----------|-------------------|----------|")
        
        for i, data in enumerate(complexity_data):
            year = data['year']
            concepts = data['total_concepts']
            roles = data['total_roles']
            depth = data['max_depth']
            avg_children = data['avg_children_per_role']
            
            if i > 0:
                prev_concepts = complexity_data[i-1]['total_concepts']
                change = concepts - prev_concepts
                pct = (change / prev_concepts * 100) if prev_concepts > 0 else 0
                report_content.append(f"| {year} | {concepts} | {roles} | {depth} | {avg_children:.1f} | {change:+d} ({pct:+.1f}%) |")
            else:
                report_content.append(f"| {year} | {concepts} | {roles} | {depth} | {avg_children:.1f} | 基准 |")
        
        # Save report
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(report_content))
            print(f"\npre文件时间线报告已保存到: {output_file}")
        
        return '\n'.join(report_content)

def main():
    parser = argparse.ArgumentParser(description='Company Financial Relationship Structure Change Analysis (pre files)')
    parser.add_argument('--relationships-dir', default='/Users/wangting/work/read_apple_10k/knowledge/financial_relationships',
                       help='Directory containing financial relationship markdown files')
    parser.add_argument('--company', required=True, 
                       help='Company symbol to analyze (e.g., AAPL, AMZN, GOOGL)')
    parser.add_argument('--output-dir', default='/Users/wangting/work/read_apple_10k/pre_timeline_analysis',
                       help='Output directory for analysis results')
    parser.add_argument('--analysis-type', choices=['all', 'changes', 'concepts', 'complexity', 'timeline'],
                       default='all', help='Type of analysis to perform')
    
    args = parser.parse_args()
    
    # Create analyzer
    analyzer = CompanyPreRelationshipAnalyzer(args.relationships_dir, args.company)
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Execute analysis
    if args.analysis_type == 'all':
        analyzer.generate_timeline_report(output_dir / f'{args.company}_pre_timeline_analysis.md')
    elif args.analysis_type == 'changes':
        analyzer.analyze_year_over_year_changes()
    elif args.analysis_type == 'concepts':
        analyzer.analyze_concept_evolution()
    elif args.analysis_type == 'complexity':
        analyzer.analyze_structure_complexity()
    elif args.analysis_type == 'timeline':
        analyzer.generate_timeline_report(output_dir / f'{args.company}_pre_timeline_analysis.md')

if __name__ == "__main__":
    main()