"""
数据库存储接口 - 将解析后的XBRL数据存储到数据库
"""

import duckdb
from typing import List, Optional, Dict, Any
from datetime import date
from .models import XBRLDocument, CompanyInfo, ContextInfo, FactInfo


class DatabaseStorage:
    """XBRL数据数据库存储器"""
    
    def __init__(self, db_path: str):
        """
        初始化数据库存储器
        
        Args:
            db_path: 数据库文件路径
        """
        self.db_path = db_path
        self._ensure_tables()
    
    def _ensure_tables(self):
        """确保数据库表存在"""
        conn = duckdb.connect(self.db_path)
        try:
            # 创建公司表
            conn.execute("""
                CREATE TABLE IF NOT EXISTS companies (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR,
                    cik VARCHAR UNIQUE,
                    ticker VARCHAR,
                    industry VARCHAR
                )
            """)
            
            # 创建XBRL文档表
            conn.execute("""
                CREATE TABLE IF NOT EXISTS xbrl_documents (
                    id INTEGER PRIMARY KEY,
                    file_path VARCHAR UNIQUE,
                    company_id INTEGER,
                    reporting_year INTEGER,
                    fiscal_period VARCHAR,
                    period_end_date DATE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # 创建上下文表
            conn.execute("""
                CREATE TABLE IF NOT EXISTS contexts (
                    id INTEGER PRIMARY KEY,
                    document_id INTEGER,
                    context_id VARCHAR,
                    entity_identifier VARCHAR,
                    period_type VARCHAR,
                    start_date DATE,
                    end_date DATE,
                    instant_date DATE
                )
            """)
            
            # 创建维度表
            conn.execute("""
                CREATE TABLE IF NOT EXISTS context_dimensions (
                    id INTEGER PRIMARY KEY,
                    context_table_id INTEGER,
                    dimension_name VARCHAR,
                    member_name VARCHAR
                )
            """)
            
            # 创建事实数据表
            conn.execute("""
                CREATE TABLE IF NOT EXISTS facts (
                    id INTEGER PRIMARY KEY,
                    document_id INTEGER,
                    context_table_id INTEGER,
                    tag_name VARCHAR,
                    namespace VARCHAR,
                    context_id VARCHAR,
                    value VARCHAR,
                    unit VARCHAR,
                    decimals INTEGER,
                    precision INTEGER
                )
            """)
            
            # 创建索引
            conn.execute("CREATE INDEX IF NOT EXISTS idx_companies_cik ON companies(cik)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_documents_company ON xbrl_documents(company_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_documents_year ON xbrl_documents(reporting_year)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_contexts_document ON contexts(document_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_facts_document ON facts(document_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_facts_namespace ON facts(namespace)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_facts_tag ON facts(tag_name)")
            
        finally:
            conn.close()
    
    def store_document(self, xbrl_doc: XBRLDocument) -> Optional[int]:
        """
        存储XBRL文档到数据库
        
        Args:
            xbrl_doc: XBRL文档对象
            
        Returns:
            文档ID
        """
        conn = duckdb.connect(self.db_path)
        try:
            # 存储或获取公司信息
            company_id = self._store_company(conn, xbrl_doc.company)
            if not company_id:
                print("无法存储公司信息")
                return None
            
            # 存储文档信息
            document_id = self._store_document_info(conn, xbrl_doc, company_id)
            if not document_id:
                print("无法存储文档信息")
                return None
            
            # 存储上下文
            context_mapping = self._store_contexts(conn, xbrl_doc.contexts, document_id)
            
            # 存储事实数据
            self._store_facts(conn, xbrl_doc.facts, document_id, context_mapping)
            
            print(f"成功存储文档，ID: {document_id}")
            return document_id
            
        except Exception as e:
            print(f"存储文档时发生错误: {e}")
            return None
        finally:
            conn.close()
    
    def _store_company(self, conn, company: CompanyInfo) -> Optional[int]:
        """存储公司信息"""
        try:
            # 检查公司是否已存在
            result = conn.execute("""
                SELECT id FROM companies WHERE cik = ?
            """, [company.cik]).fetchone()
            
            if result:
                return result[0]
            
            # 获取下一个可用的ID
            next_id_result = conn.execute("""
                SELECT COALESCE(MAX(id), 0) + 1 FROM companies
            """).fetchone()
            next_id = next_id_result[0]
            
            # 插入新公司
            result = conn.execute("""
                INSERT INTO companies (id, name, cik, ticker)
                VALUES (?, ?, ?, ?)
                RETURNING id
            """, [next_id, company.name, company.cik, company.ticker]).fetchone()
            
            return result[0] if result else None
            
        except Exception as e:
            print(f"存储公司信息时发生错误: {e}")
            return None
    
    def _store_document_info(self, conn, xbrl_doc: XBRLDocument, company_id: int) -> Optional[int]:
        """存储文档信息"""
        try:
            # 检查文档是否已存在
            result = conn.execute("""
                SELECT id FROM xbrl_documents WHERE file_path = ?
            """, [xbrl_doc.file_path]).fetchone()
            
            if result:
                print(f"文档已存在，ID: {result[0]}")
                return result[0]
            
            # 获取下一个可用的ID
            next_id_result = conn.execute("""
                SELECT COALESCE(MAX(id), 0) + 1 FROM xbrl_documents
            """).fetchone()
            next_id = next_id_result[0]
            
            # 插入新文档
            result = conn.execute("""
                INSERT INTO xbrl_documents 
                (id, file_path, company_id, reporting_year, fiscal_period, period_end_date)
                VALUES (?, ?, ?, ?, ?, ?)
                RETURNING id
            """, [
                next_id,
                xbrl_doc.file_path,
                company_id,
                xbrl_doc.reporting_year,
                xbrl_doc.fiscal_period,
                xbrl_doc.period_end_date
            ]).fetchone()
            
            return result[0] if result else None
            
        except Exception as e:
            print(f"存储文档信息时发生错误: {e}")
            return None
    
    def _store_contexts(self, conn, contexts: List[ContextInfo], document_id: int) -> Dict[str, int]:
        """存储上下文信息"""
        context_mapping = {}
        
        try:
            # 获取下一个可用的context ID
            next_context_id_result = conn.execute("""
                SELECT COALESCE(MAX(id), 0) + 1 FROM contexts
            """).fetchone()
            next_context_id = next_context_id_result[0]
            
            # 获取下一个可用的dimension ID
            next_dimension_id_result = conn.execute("""
                SELECT COALESCE(MAX(id), 0) + 1 FROM context_dimensions
            """).fetchone()
            next_dimension_id = next_dimension_id_result[0]
            
            for context in contexts:
                # 插入上下文
                result = conn.execute("""
                    INSERT INTO contexts 
                    (id, document_id, context_id, entity_identifier, period_type, 
                     start_date, end_date, instant_date)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    RETURNING id
                """, [
                    next_context_id,
                    document_id,
                    context.context_id,
                    context.entity_identifier,
                    context.period_type,
                    context.start_date,
                    context.end_date,
                    context.instant_date
                ]).fetchone()
                
                if result:
                    context_table_id = result[0]
                    context_mapping[context.context_id] = context_table_id
                    next_context_id += 1
                    
                    # 存储维度信息
                    for dimension in context.dimensions:
                        conn.execute("""
                            INSERT INTO context_dimensions 
                            (id, context_table_id, dimension_name, member_name)
                            VALUES (?, ?, ?, ?)
                        """, [
                            next_dimension_id,
                            context_table_id,
                            dimension['dimension'],
                            dimension['member']
                        ])
                        next_dimension_id += 1
            
            return context_mapping
            
        except Exception as e:
            print(f"存储上下文时发生错误: {e}")
            return {}
    
    def _store_facts(self, conn, facts: List[FactInfo], document_id: int, context_mapping: Dict[str, int]):
        """存储事实数据"""
        try:
            # 获取下一个可用的fact ID
            next_fact_id_result = conn.execute("""
                SELECT COALESCE(MAX(id), 0) + 1 FROM facts
            """).fetchone()
            next_fact_id = next_fact_id_result[0]
            
            for fact in facts:
                context_table_id = context_mapping.get(fact.context_id)
                
                conn.execute("""
                    INSERT INTO facts 
                    (id, document_id, context_table_id, tag_name, namespace, context_id, 
                     value, unit, decimals, precision)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, [
                    next_fact_id,
                    document_id,
                    context_table_id,
                    fact.tag_name,
                    fact.namespace,
                    fact.context_id,
                    fact.value,
                    fact.unit,
                    fact.decimals,
                    fact.precision
                ])
                next_fact_id += 1
            
        except Exception as e:
            print(f"存储事实数据时发生错误: {e}")
    
    def query_company_facts(self, company_cik: str, year: int, namespace: str = None) -> List[Dict[str, Any]]:
        """
        查询公司的事实数据
        
        Args:
            company_cik: 公司CIK
            year: 年份
            namespace: 命名空间过滤（可选）
            
        Returns:
            事实数据列表
        """
        conn = duckdb.connect(self.db_path)
        try:
            query = """
                SELECT 
                    c.name as company_name,
                    c.cik,
                    d.reporting_year,
                    f.tag_name,
                    f.namespace,
                    f.context_id,
                    f.value,
                    f.unit,
                    ctx.period_type,
                    ctx.start_date,
                    ctx.end_date,
                    ctx.instant_date
                FROM facts f
                JOIN xbrl_documents d ON f.document_id = d.id
                JOIN companies c ON d.company_id = c.id
                LEFT JOIN contexts ctx ON f.context_table_id = ctx.id
                WHERE c.cik = ? AND d.reporting_year = ?
            """
            
            params = [company_cik, year]
            
            if namespace:
                query += " AND f.namespace = ?"
                params.append(namespace)
            
            query += " ORDER BY f.tag_name"
            
            result = conn.execute(query, params).fetchall()
            
            # 转换为字典列表
            columns = ['company_name', 'cik', 'reporting_year', 'tag_name', 'namespace', 
                      'context_id', 'value', 'unit', 'period_type', 'start_date', 'end_date', 'instant_date']
            return [dict(zip(columns, row)) for row in result]
            
        except Exception as e:
            print(f"查询数据时发生错误: {e}")
            return []
        finally:
            conn.close()
    
    def get_document_summary(self, company_cik: str = None) -> List[Dict[str, Any]]:
        """
        获取文档摘要信息
        
        Args:
            company_cik: 公司CIK（可选）
            
        Returns:
            文档摘要列表
        """
        conn = duckdb.connect(self.db_path)
        try:
            query = """
                SELECT 
                    c.name as company_name,
                    c.cik,
                    c.ticker,
                    d.reporting_year,
                    d.fiscal_period,
                    d.period_end_date,
                    COUNT(f.id) as fact_count,
                    COUNT(DISTINCT ctx.id) as context_count,
                    d.created_at
                FROM xbrl_documents d
                JOIN companies c ON d.company_id = c.id
                LEFT JOIN facts f ON d.id = f.document_id
                LEFT JOIN contexts ctx ON d.id = ctx.document_id
            """
            
            params = []
            if company_cik:
                query += " WHERE c.cik = ?"
                params.append(company_cik)
            
            query += """
                GROUP BY c.name, c.cik, c.ticker, d.reporting_year, 
                         d.fiscal_period, d.period_end_date, d.created_at
                ORDER BY c.name, d.reporting_year DESC
            """
            
            result = conn.execute(query, params).fetchall()
            
            # 转换为字典列表
            columns = ['company_name', 'cik', 'ticker', 'reporting_year', 'fiscal_period', 
                      'period_end_date', 'fact_count', 'context_count', 'created_at']
            return [dict(zip(columns, row)) for row in result]
            
        except Exception as e:
            print(f"获取文档摘要时发生错误: {e}")
            return []
        finally:
            conn.close()