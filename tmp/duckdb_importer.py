#!/usr/bin/env python3

import argparse
import os
import sys
import duckdb
from xml.etree import ElementTree as ET
import re

# 添加工具目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tools'))
from context_analyzer import list_all_contexts, get_context_info

def is_main_filing(filename):
    """
    判断是否为主要申报文件
    支持的格式：
    - aapl-20240928_htm.xml (Apple格式)
    - amzn-20151231.xml (Amazon格式)
    """
    # 排除明确的辅助文件
    if any(x in filename for x in ['_pre.', '_lab.', '_cal.', '_def.', 'FilingSummary']):
        return False
    
    # 匹配主文件模式
    patterns = [
        r'^[a-z]+-\d{8}_htm\.xml$',  # Apple格式
        r'^[a-z]+-\d{8}\.xml$'        # Amazon格式
    ]
    
    return any(re.match(pattern, filename) for pattern in patterns)

def get_xbrl_file_info(xbrl_file_path):
    """提取XBRL文件的基本信息"""
    tree = ET.parse(xbrl_file_path)
    root = tree.getroot()
    
    namespaces = {
        'dei': 'http://xbrl.sec.gov/dei/2024',
        'dei2023': 'http://xbrl.sec.gov/dei/2023',
        'dei2022': 'http://xbrl.sec.gov/dei/2022',
        'dei2021': 'http://xbrl.sec.gov/dei/2021',
        'dei2020': 'http://xbrl.sec.gov/dei/2020',
        'dei2019': 'http://xbrl.sec.gov/dei/2019',
        'dei2018': 'http://xbrl.sec.gov/dei/2018',
        'dei2014': 'http://xbrl.sec.gov/dei/2014-01-31',
        'xbrli': 'http://www.xbrl.org/2003/instance'
    }
    
    file_info = {
        'file_path': xbrl_file_path,
        'company_name': None,
        'filing_type': None,
        'fiscal_year': None,
        'fiscal_period': None,
        'period_end_date': None
    }
    
    # 提取公司名称
    for ns in namespaces:
        entity_name = root.find(f'.//{{{namespaces[ns]}}}EntityRegistrantName')
        if entity_name is not None and entity_name.text:
            file_info['company_name'] = entity_name.text.strip()
            break
    
    # 提取文件类型
    for ns in namespaces:
        doc_type = root.find(f'.//{{{namespaces[ns]}}}DocumentType')
        if doc_type is not None and doc_type.text:
            file_info['filing_type'] = doc_type.text.strip()
            break
    
    # 提取财年
    for ns in namespaces:
        fiscal_year = root.find(f'.//{{{namespaces[ns]}}}DocumentFiscalYearFocus')
        if fiscal_year is not None and fiscal_year.text:
            try:
                file_info['fiscal_year'] = int(fiscal_year.text.strip())
                break
            except ValueError:
                continue
    
    # 提取财期
    for ns in namespaces:
        fiscal_period = root.find(f'.//{{{namespaces[ns]}}}DocumentFiscalPeriodFocus')
        if fiscal_period is not None and fiscal_period.text:
            file_info['fiscal_period'] = fiscal_period.text.strip()
            break
    
    # 提取期末日期
    for ns in namespaces:
        period_end = root.find(f'.//{{{namespaces[ns]}}}DocumentPeriodEndDate')
        if period_end is not None and period_end.text:
            file_info['period_end_date'] = period_end.text.strip()
            break
    
    return file_info

def get_company_id_by_name(conn, company_name):
    """根据公司名称获取公司ID"""
    result = conn.execute("""
        SELECT id FROM companies 
        WHERE name ILIKE ?
    """, [f"%{company_name}%"]).fetchone()
    
    return result[0] if result else None

def insert_xbrl_file(conn, file_info, company_id):
    """将XBRL文件信息插入数据库"""
    # 确定文件类型
    file_type = 'htm' if '_htm.xml' in file_info['file_path'] else 'main'
    
    # 获取下一个可用的ID
    result = conn.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM xbrl_files").fetchone()
    next_id = result[0]
    
    result = conn.execute("""
        INSERT INTO xbrl_files 
        (id, company_id, file_path, file_type, filing_type, fiscal_year, fiscal_period, period_end_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        RETURNING id
    """, [
        next_id,
        company_id,
        file_info['file_path'],
        file_type,
        file_info['filing_type'],
        file_info['fiscal_year'],
        file_info['fiscal_period'],
        file_info['period_end_date']
    ]).fetchone()
    
    return result[0]

def insert_contexts(conn, xbrl_file_path, xbrl_file_id):
    """插入上下文信息"""
    context_ids = list_all_contexts(xbrl_file_path)
    context_mapping = {}
    
    # 获取下一个可用的context ID
    result = conn.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM contexts").fetchone()
    next_context_id = result[0]
    
    for context_id in context_ids:
        context_info = get_context_info(xbrl_file_path, context_id)
        if context_info is None:
            continue
            
        period_type = None
        start_date = None
        end_date = None
        instant_date = None
        
        period_info = context_info['period_info']
        if period_info.startswith('Instant: '):
            period_type = 'instant'
            instant_date = period_info[9:]
        elif period_info.startswith('Period: '):
            period_type = 'duration'
            period_part = period_info[8:]
            if ' to ' in period_part:
                start_date, end_date = period_part.split(' to ', 1)
        
        # 插入上下文
        result = conn.execute("""
            INSERT INTO contexts 
            (id, xbrl_file_id, context_id, period_type, start_date, end_date, instant_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            RETURNING id
        """, [next_context_id, xbrl_file_id, context_id, period_type, start_date, end_date, instant_date]).fetchone()
        
        context_db_id = result[0]
        context_mapping[context_id] = context_db_id
        next_context_id += 1
        
        # 获取下一个可用的dimension ID
        result = conn.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM dimensions").fetchone()
        next_dimension_id = result[0]
        
        # 插入维度
        for dimension in context_info['dimensions']:
            dimension_name = dimension['dimension'].split(':')[-1] if ':' in dimension['dimension'] else dimension['dimension']
            member_name = dimension['member'].split(':')[-1] if ':' in dimension['member'] else dimension['member']
            
            conn.execute("""
                INSERT INTO dimensions 
                (id, context_id, dimension_name, member_name)
                VALUES (?, ?, ?, ?)
            """, [next_dimension_id, context_db_id, dimension_name, member_name])
            
            next_dimension_id += 1
    
    return context_mapping

def insert_financial_facts(conn, xbrl_file_path, xbrl_file_id, context_mapping):
    """插入财务数据"""
    tree = ET.parse(xbrl_file_path)
    root = tree.getroot()
    
    # 获取下一个可用的fact ID
    result = conn.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM financial_facts").fetchone()
    next_fact_id = result[0]
    
    # 获取下一个可用的tag ID
    result = conn.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM financial_tags").fetchone()
    next_tag_id = result[0]
    
    # 缓存已存在的标签
    existing_tags = {}
    for row in conn.execute("SELECT id, tag_name FROM financial_tags").fetchall():
        existing_tags[row[1]] = row[0]
    
    facts_count = 0
    for elem in root.iter():
        if 'contextRef' in elem.attrib:
            context_ref = elem.attrib['contextRef']
            
            if context_ref not in context_mapping:
                continue
                
            context_db_id = context_mapping[context_ref]
            
            # 获取标签名
            tag_name = elem.tag
            if tag_name.startswith('{'):
                ns_uri, local_name = tag_name[1:].split('}', 1)
                tag_name = local_name
            
            # 获取或创建标签ID
            if tag_name in existing_tags:
                tag_id = existing_tags[tag_name]
            else:
                tag_id = next_tag_id
                conn.execute("""
                    INSERT INTO financial_tags (id, tag_name)
                    VALUES (?, ?)
                """, [tag_id, tag_name])
                existing_tags[tag_name] = tag_id
                next_tag_id += 1
            
            # 获取值和单位信息
            value = elem.text if elem.text else ""
            unit_ref = elem.attrib.get('unitRef', '')
            decimals = elem.attrib.get('decimals', '')
            
            try:
                decimals = int(decimals) if decimals else None
            except ValueError:
                decimals = None
            
            # 插入财务数据
            conn.execute("""
                INSERT INTO financial_facts 
                (id, xbrl_file_id, context_id, tag_id, value, unit, decimals)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, [next_fact_id, xbrl_file_id, context_db_id, tag_id, value, unit_ref, decimals])
            
            next_fact_id += 1
            facts_count += 1
    
    print(f"插入了 {facts_count} 条财务数据")

def import_xbrl_file(conn, xbrl_file_path):
    """导入XBRL文件到数据库"""
    print(f"正在导入XBRL文件: {xbrl_file_path}")
    
    # 获取文件信息
    file_info = get_xbrl_file_info(xbrl_file_path)
    print(f"文件信息: {file_info}")
    
    # 如果没有提取到公司名称，跳过
    if not file_info['company_name']:
        print("跳过：无法提取公司信息")
        return
    
    # 获取公司ID
    company_id = get_company_id_by_name(conn, file_info['company_name'])
    if not company_id:
        print(f"错误：找不到公司: {file_info['company_name']}")
        return
    
    # 插入文件信息
    file_id = insert_xbrl_file(conn, file_info, company_id)
    print(f"插入的XBRL文件ID: {file_id}")
    
    # 插入上下文
    context_mapping = insert_contexts(conn, xbrl_file_path, file_id)
    print(f"插入了 {len(context_mapping)} 个上下文")
    
    # 插入财务数据
    insert_financial_facts(conn, xbrl_file_path, file_id, context_mapping)
    
    print("导入完成")

def find_xbrl_files(directory):
    """查找所有XBRL主文件"""
    xbrl_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml') and is_main_filing(file):
                file_path = os.path.join(root, file)
                xbrl_files.append(file_path)
    
    return sorted(xbrl_files)  # 按文件名排序

def main():
    parser = argparse.ArgumentParser(description='将XBRL文件导入DuckDB数据库')
    parser.add_argument('--db', required=True, help='DuckDB数据库文件路径')
    parser.add_argument('--xbrl-file', help='单个XBRL文件路径')
    parser.add_argument('--xbrl-dir', help='包含XBRL文件的目录')
    
    args = parser.parse_args()
    
    # 连接数据库
    conn = duckdb.connect(args.db)
    
    try:
        if args.xbrl_file:
            # 导入单个文件
            if os.path.exists(args.xbrl_file):
                import_xbrl_file(conn, args.xbrl_file)
            else:
                print(f"错误：找不到文件: {args.xbrl_file}")
                sys.exit(1)
        
        elif args.xbrl_dir:
            # 导入目录中的所有文件
            if os.path.exists(args.xbrl_dir):
                xbrl_files = find_xbrl_files(args.xbrl_dir)
                print(f"找到 {len(xbrl_files)} 个XBRL主文件")
                
                for i, xbrl_file in enumerate(xbrl_files, 1):
                    print(f"\n[{i}/{len(xbrl_files)}] 正在导入: {xbrl_file}")
                    try:
                        import_xbrl_file(conn, xbrl_file)
                    except Exception as e:
                        print(f"导入 {xbrl_file} 时出错: {e}")
            else:
                print(f"错误：找不到目录: {args.xbrl_dir}")
                sys.exit(1)
        
        else:
            print("错误：必须指定 --xbrl-file 或 --xbrl-dir")
            sys.exit(1)
            
    finally:
        conn.close()

if __name__ == "__main__":
    main()