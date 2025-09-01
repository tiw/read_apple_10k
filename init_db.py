#!/usr/bin/env python3
"""
初始化XBRL数据库
"""

import sqlite3
import os
import sys

def init_database(db_path):
    """
    初始化XBRL数据库表结构
    
    Args:
        db_path (str): 数据库文件路径
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 创建XBRL文件表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS xbrl_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_path TEXT UNIQUE,
            company_name TEXT,
            filing_type TEXT,
            fiscal_year INTEGER,
            fiscal_period TEXT,
            period_end_date TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # 创建上下文表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contexts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            xbrl_file_id INTEGER,
            context_id TEXT,
            period_type TEXT,
            start_date TEXT,
            end_date TEXT,
            instant_date TEXT,
            FOREIGN KEY (xbrl_file_id) REFERENCES xbrl_files (id),
            UNIQUE(xbrl_file_id, context_id)
        )
    """)
    
    # 创建维度表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dimensions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            context_id INTEGER,
            dimension_name TEXT,
            member_name TEXT,
            FOREIGN KEY (context_id) REFERENCES contexts (id)
        )
    """)
    
    # 创建财务标签表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS financial_tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tag_name TEXT UNIQUE
        )
    """)
    
    # 创建财务事实表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS financial_facts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            xbrl_file_id INTEGER,
            context_id INTEGER,
            tag_id INTEGER,
            value TEXT,
            unit TEXT,
            decimals INTEGER,
            FOREIGN KEY (xbrl_file_id) REFERENCES xbrl_files (id),
            FOREIGN KEY (context_id) REFERENCES contexts (id),
            FOREIGN KEY (tag_id) REFERENCES financial_tags (id),
            UNIQUE(xbrl_file_id, context_id, tag_id)
        )
    """)
    
    conn.commit()
    conn.close()
    print(f"数据库 {db_path} 初始化完成")

def main():
    """
    主函数
    """
    db_path = "xbrl.db"
    if len(sys.argv) > 1:
        db_path = sys.argv[1]
    
    init_database(db_path)

if __name__ == "__main__":
    main()