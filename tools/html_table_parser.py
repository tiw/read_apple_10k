import xml.etree.ElementTree as ET
from html import unescape
import re
from xml.etree.ElementTree import Element

def parse_html_table(html_content):
    """
    Parse HTML table content and extract structured data
    
    Args:
        html_content (str): HTML content containing tables
        
    Returns:
        list: List of parsed tables, each table is a dict with headers and rows
    """
    # 解析HTML内容
    try:
        # 移除XML声明（如果存在）
        if html_content.startswith('<?xml'):
            html_content = html_content.split('?>', 1)[1]
        
        # 创建根元素包装HTML内容
        wrapped_content = f"<root>{html_content}</root>"
        root = ET.fromstring(wrapped_content)
    except ET.ParseError as e:
        # 如果解析失败，尝试清理HTML内容
        # 移除HTML实体和特殊字符
        cleaned_content = re.sub(r'&[a-zA-Z]+;', '', html_content)
        cleaned_content = re.sub(r'&#[0-9]+;', '', cleaned_content)
        wrapped_content = f"<root>{cleaned_content}</root>"
        try:
            root = ET.fromstring(wrapped_content)
        except ET.ParseError:
            # 如果仍然失败，返回错误信息
            return [{"error": f"Failed to parse HTML content: {str(e)}"}]
    
    tables = []
    
    # 查找所有表格元素
    for table_elem in root.findall('.//table'):
        table_data = {
            "headers": [],
            "rows": [],
            "title": ""
        }
        
        # 查找表格标题（在表格前的文本）
        # 简单地查找任何包含文本的span元素作为标题
        span_elements = root.findall('.//span')
        for span in span_elements:
            if span.text and 'Lease liability maturities' in span.text:
                table_data["title"] = span.text.strip()
                break
        
        # 解析表头
        # 找到所有tr元素
        all_rows = table_elem.findall('.//tr')
        if all_rows:
            header_row = all_rows[0]  # 默认第一行是表头
            headers = []
            cells = header_row.findall('.//td') + header_row.findall('.//th')
            for cell in cells:
                # 提取单元格文本
                cell_text = ""
                spans = cell.findall('.//span')
                if spans:
                    # 合并所有span的文本
                    cell_text = " ".join([span.text.strip() for span in spans if span.text])
                elif cell.text:
                    cell_text = cell.text.strip()
                
                # 处理换行文本
                if '\n' in cell_text:
                    cell_text = ' '.join(cell_text.split())
                
                # 只添加非空的标题
                if cell_text.strip():
                    headers.append(cell_text)
            
            table_data["headers"] = headers
        
        # 解析数据行
        rows = all_rows[1:] if len(all_rows) > 1 else []  # 跳过表头行
            
        for row in rows:
            cells = row.findall('.//td') + row.findall('.//th')
            if cells:
                row_data = []
                for cell in cells:
                    # 提取单元格文本
                    cell_text = ""
                    spans = cell.findall('.//span')
                    if spans:
                        # 合并所有span的文本
                        cell_text = " ".join([span.text.strip() if span.text else "" for span in spans])
                    elif cell.text:
                        cell_text = cell.text.strip()
                    
                    # 清理文本
                    cell_text = re.sub(r'\s+', ' ', cell_text).strip()
                    # 移除特殊字符，如货币符号
                    cell_text = re.sub(r'[$£€]', '', cell_text).strip()
                    
                    row_data.append(cell_text)
                
                # 只添加非空行
                if any(cell.strip() for cell in row_data):
                    table_data["rows"].append(row_data)
        
        tables.append(table_data)
    
    return tables

def format_table_data(tables):
    """
    Format parsed table data into readable format
    
    Args:
        tables (list): List of parsed tables
        
    Returns:
        str: Formatted table data as string
    """
    result_lines = []
    
    for i, table in enumerate(tables):
        if "error" in table:
            result_lines.append(f"Error parsing table: {table['error']}")
            continue
            
        result_lines.append(f"Table {i+1}:")
        if table["title"]:
            result_lines.append(f"Title: {table['title']}")
        result_lines.append("")
        
        # 添加表头
        if table["headers"]:
            # 计算每列的最大宽度
            col_widths = []
            for j in range(len(table["headers"])):
                max_width = len(table["headers"][j])
                for row in table["rows"]:
                    if j < len(row):
                        max_width = max(max_width, len(row[j]))
                col_widths.append(max_width + 2)  # 添加一些填充
            
            # 格式化表头
            header_line = " | ".join(table["headers"][j].ljust(col_widths[j]) for j in range(len(table["headers"])))
            result_lines.append(header_line)
            result_lines.append("-" * len(header_line))
            
            # 格式化数据行
            for row in table["rows"]:
                row_line = " | ".join((row[j] if j < len(row) else "").ljust(col_widths[j]) for j in range(len(col_widths)))
                result_lines.append(row_line)
        else:
            # 没有表头的情况
            if table["rows"]:
                # 计算每列的最大宽度
                if table["rows"]:
                    col_count = max(len(row) for row in table["rows"])
                    col_widths = [0] * col_count
                    for row in table["rows"]:
                        for j in range(len(row)):
                            if j < col_count:
                                col_widths[j] = max(col_widths[j], len(row[j]) + 2)
                    
                    # 格式化数据行
                    for row in table["rows"]:
                        row_line = " | ".join((row[j] if j < len(row) else "").ljust(col_widths[j]) for j in range(len(col_widths)))
                        result_lines.append(row_line)
        
        result_lines.append("")  # 空行分隔
    
    return "\n".join(result_lines)

def extract_financial_data_from_html(html_content):
    """
    Extract and format financial data from HTML tables
    
    Args:
        html_content (str): HTML content containing financial tables
        
    Returns:
        str: Formatted financial data
    """
    tables = parse_html_table(html_content)
    return format_table_data(tables)