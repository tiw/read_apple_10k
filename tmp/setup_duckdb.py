import duckdb
import os

def setup_database(db_path):
    """
    设置DuckDB数据库结构
    """
    # 连接到数据库（如果不存在则创建）
    conn = duckdb.connect(db_path)
    
    try:
        # 创建公司信息表
        conn.execute("""
            CREATE TABLE IF NOT EXISTS companies (
                id INTEGER PRIMARY KEY,
                ticker VARCHAR,
                name VARCHAR,
                cik VARCHAR
            )
        """)
        
        # 创建文件信息表
        conn.execute("""
            CREATE TABLE IF NOT EXISTS xbrl_files (
                id INTEGER PRIMARY KEY,
                company_id INTEGER,
                file_path VARCHAR,
                file_type VARCHAR,  -- 'htm', 'pre', 'lab' 等
                filing_type VARCHAR,
                fiscal_year INTEGER,
                fiscal_period VARCHAR,
                period_end_date DATE
            )
        """)
        
        # 创建上下文表
        conn.execute("""
            CREATE TABLE IF NOT EXISTS contexts (
                id INTEGER PRIMARY KEY,
                xbrl_file_id INTEGER,
                context_id VARCHAR,
                period_type VARCHAR,  -- 'instant' 或 'duration'
                start_date DATE,
                end_date DATE,
                instant_date DATE
            )
        """)
        
        # 创建维度表
        conn.execute("""
            CREATE TABLE IF NOT EXISTS dimensions (
                id INTEGER PRIMARY KEY,
                context_id INTEGER,
                dimension_name VARCHAR,
                member_name VARCHAR
            )
        """)
        
        # 创建财务标签表
        conn.execute("""
            CREATE TABLE IF NOT EXISTS financial_tags (
                id INTEGER PRIMARY KEY,
                tag_name VARCHAR UNIQUE
            )
        """)
        
        # 创建财务数据表
        conn.execute("""
            CREATE TABLE IF NOT EXISTS financial_facts (
                id INTEGER PRIMARY KEY,
                xbrl_file_id INTEGER,
                context_id INTEGER,
                tag_id INTEGER,
                value VARCHAR,  -- 保持为VARCHAR以保留原始数据格式
                unit VARCHAR,
                decimals INTEGER
            )
        """)
        
        # 创建索引以提高查询性能
        conn.execute("CREATE INDEX IF NOT EXISTS idx_companies_ticker ON companies(ticker)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_xbrl_files_company ON xbrl_files(company_id)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_contexts_file ON contexts(xbrl_file_id)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_financial_facts_context ON financial_facts(context_id)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_financial_facts_tag ON financial_facts(tag_id)")
        
        # 初始化一些基本的公司数据
        conn.execute("""
            INSERT INTO companies (id, ticker, name, cik)
            VALUES 
                (1, 'AAPL', 'Apple Inc.', '0000320193'),
                (2, 'MSFT', 'Microsoft Corporation', '0000789019'),
                (3, 'GOOGL', 'Alphabet Inc.', '0001652044'),
                (4, 'AMZN', 'Amazon.com, Inc.', '0001018724'),
                (5, 'NVDA', 'NVIDIA Corporation', '0001045810'),
                (6, 'META', 'Meta Platforms, Inc.', '0001326801'),
                (7, 'TSLA', 'Tesla, Inc.', '0001318605')
            ON CONFLICT (id) DO NOTHING
        """)
        
        print("数据库结构创建成功！")
        
    finally:
        conn.close()

if __name__ == "__main__":
    db_path = "magnificent_seven_xbrl.duckdb"
    setup_database(db_path)