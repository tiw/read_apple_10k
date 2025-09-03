"""
DuckDB数据接口模块

提供与DuckDB数据库的交互功能，用于查询10-K财务数据
"""

import duckdb
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
import os
import logging

try:
    import pandas as pd
except ImportError:
    pd = None

from .financial_concepts import FinancialConcepts, ReportSection, FinancialConcept


class DuckDBInterface:
    """DuckDB数据接口类"""
    
    def __init__(self, db_path: str = None):
        """
        初始化DuckDB接口
        
        Args:
            db_path: 数据库文件路径，如果为None则使用内存数据库
        """
        self.db_path = db_path
        self.conn = None
        self.logger = logging.getLogger(__name__)
        
        # 初始化连接
        self._connect()
        
        # 创建必要的表结构
        self._create_tables()
    
    def _connect(self):
        """建立数据库连接"""
        try:
            if self.db_path:
                self.conn = duckdb.connect(self.db_path)
                self.logger.info(f"连接到DuckDB数据库: {self.db_path}")
            else:
                self.conn = duckdb.connect(':memory:')
                self.logger.info("连接到内存DuckDB数据库")
        except Exception as e:
            self.logger.error(f"连接数据库失败: {e}")
            raise
    
    def _create_tables(self):
        """创建必要的表结构"""
        try:
            # 创建公司信息表
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS companies (
                    cik VARCHAR PRIMARY KEY,
                    ticker VARCHAR,
                    name VARCHAR,
                    sic_code VARCHAR,
                    sic_description VARCHAR,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # 创建财务事实表
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS financial_facts (
                    id BIGINT PRIMARY KEY,
                    cik VARCHAR,
                    concept VARCHAR,
                    value DECIMAL(20,2),
                    unit VARCHAR,
                    end_date DATE,
                    start_date DATE,
                    form VARCHAR,
                    filed_date DATE,
                    frame VARCHAR,
                    fiscal_year INTEGER,
                    fiscal_period VARCHAR,
                    accession_number VARCHAR,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (cik) REFERENCES companies(cik)
                )
            """)
            
            # 创建索引
            self.conn.execute("CREATE INDEX IF NOT EXISTS idx_facts_cik ON financial_facts(cik)")
            self.conn.execute("CREATE INDEX IF NOT EXISTS idx_facts_concept ON financial_facts(concept)")
            self.conn.execute("CREATE INDEX IF NOT EXISTS idx_facts_fiscal_year ON financial_facts(fiscal_year)")
            self.conn.execute("CREATE INDEX IF NOT EXISTS idx_facts_form ON financial_facts(form)")
            
            self.logger.info("数据库表结构创建完成")
            
        except Exception as e:
            self.logger.error(f"创建表结构失败: {e}")
            raise
    
    def insert_company(self, cik: str, ticker: str, name: str, 
                      sic_code: str = None, sic_description: str = None):
        """
        插入公司信息
        
        Args:
            cik: 公司CIK码
            ticker: 股票代码
            name: 公司名称
            sic_code: SIC代码
            sic_description: SIC描述
        """
        try:
            self.conn.execute("""
                INSERT OR REPLACE INTO companies (cik, ticker, name, sic_code, sic_description)
                VALUES (?, ?, ?, ?, ?)
            """, [cik, ticker, name, sic_code, sic_description])
            
            self.logger.info(f"插入公司信息: {ticker} ({cik})")
            
        except Exception as e:
            self.logger.error(f"插入公司信息失败: {e}")
            raise
    
    def insert_financial_facts(self, facts_data: List[Dict[str, Any]]):
        """
        批量插入财务事实数据
        
        Args:
            facts_data: 财务事实数据列表
        """
        try:
            if not facts_data:
                return
            
            # 获取下一个ID
            result = self.conn.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM financial_facts").fetchone()
            next_id = result[0] if result else 1
            
            # 准备数据
            data_tuples = []
            for i, fact in enumerate(facts_data):
                data_tuples.append((
                    next_id + i,  # 手动分配ID
                    fact.get('cik'),
                    fact.get('concept'),
                    fact.get('value'),
                    fact.get('unit'),
                    fact.get('end_date'),
                    fact.get('start_date'),
                    fact.get('form'),
                    fact.get('filed_date'),
                    fact.get('frame'),
                    fact.get('fiscal_year'),
                    fact.get('fiscal_period'),
                    fact.get('accession_number')
                ))
            
            # 批量插入
            self.conn.executemany("""
                INSERT INTO financial_facts (
                    id, cik, concept, value, unit, end_date, start_date, 
                    form, filed_date, frame, fiscal_year, fiscal_period, accession_number
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, data_tuples)
            
            self.logger.info(f"批量插入 {len(facts_data)} 条财务事实数据")
            
        except Exception as e:
            self.logger.error(f"插入财务事实数据失败: {e}")
            raise
    
    def get_company_info(self, cik: str = None, ticker: str = None) -> Optional[Dict[str, Any]]:
        """
        获取公司信息
        
        Args:
            cik: 公司CIK码
            ticker: 股票代码
            
        Returns:
            公司信息字典
        """
        try:
            if cik:
                query = "SELECT * FROM companies WHERE cik = ?"
                params = [cik]
            elif ticker:
                query = "SELECT * FROM companies WHERE ticker = ?"
                params = [ticker]
            else:
                return None
            
            result = self.conn.execute(query, params).fetchone()
            
            if result:
                # 根据实际数据库结构映射字段
                # 数据库结构: (id, name, cik, ticker, industry)
                return {
                    'id': result[0],
                    'name': result[1],
                    'cik': result[2],
                    'ticker': result[3],
                    'industry': result[4]
                }
            return None
            
        except Exception as e:
            self.logger.error(f"获取公司信息失败: {e}")
            return None
    
    def get_financial_facts(self, cik: str, concept: str = None, 
                           fiscal_year: int = None, form: str = '10-K'):
        """
        获取财务事实数据
        
        Args:
            cik: 公司CIK码
            concept: 财务概念名称
            fiscal_year: 财政年度
            form: 报告类型
            
        Returns:
            财务事实数据DataFrame或空列表
        """
        try:
            query = """
                SELECT * FROM financial_facts 
                WHERE cik = ? AND form = ?
            """
            params = [cik, form]
            
            if concept:
                query += " AND concept = ?"
                params.append(concept)
            
            if fiscal_year:
                query += " AND fiscal_year = ?"
                params.append(fiscal_year)
            
            query += " ORDER BY fiscal_year DESC, end_date DESC"
            
            if pd is not None:
                result = self.conn.execute(query, params).fetchdf()
                self.logger.info(f"获取财务事实数据: {len(result)} 条记录")
                return result
            else:
                result = self.conn.execute(query, params).fetchall()
                self.logger.info(f"获取财务事实数据: {len(result)} 条记录")
                return result
            
        except Exception as e:
            self.logger.error(f"获取财务事实数据失败: {e}")
            return [] if pd is None else pd.DataFrame()
    
    def get_latest_financial_facts(self, cik: str, fiscal_year: int = None) -> Dict[str, Any]:
        """
        获取最新的财务事实数据
        
        Args:
            cik: 公司CIK码
            fiscal_year: 财政年度，如果为None则获取最新年度
            
        Returns:
            财务事实数据字典
        """
        try:
            # 如果没有指定财政年度，获取最新的财政年度
            if fiscal_year is None:
                year_query = """
                    SELECT MAX(fiscal_year) FROM financial_facts 
                    WHERE cik = ? AND form = '10-K'
                """
                result = self.conn.execute(year_query, [cik]).fetchone()
                if result and result[0]:
                    fiscal_year = result[0]
                else:
                    return {}
            
            # 获取指定财政年度的所有财务事实
            facts_df = self.get_financial_facts(cik, fiscal_year=fiscal_year)
            
            # 检查是否为空
            is_empty = False
            if hasattr(facts_df, 'empty'):
                is_empty = facts_df.empty
            else:
                is_empty = len(facts_df) == 0
            
            if is_empty:
                return {}
            
            # 转换为字典格式
            facts_dict = {}
            if hasattr(facts_df, 'iterrows'):
                # pandas DataFrame
                for _, row in facts_df.iterrows():
                    concept = row['concept']
                    facts_dict[concept] = {
                        'value': row['value'],
                        'unit': row['unit'],
                        'end_date': row['end_date'],
                        'start_date': row['start_date'],
                        'form': row['form'],
                        'filed_date': row['filed_date'],
                        'frame': row['frame'],
                        'fiscal_year': row['fiscal_year'],
                        'fiscal_period': row['fiscal_period']
                    }
            else:
                # 列表格式
                for row in facts_df:
                    concept = row[2]  # concept是第3列
                    facts_dict[concept] = {
                        'value': row[3],  # value是第4列
                        'unit': row[4],   # unit是第5列
                        'end_date': row[5],
                        'start_date': row[6],
                        'form': row[7],
                        'filed_date': row[8],
                        'frame': row[9],
                        'fiscal_year': row[10],
                        'fiscal_period': row[11]
                    }
            
            self.logger.info(f"获取最新财务事实数据: {len(facts_dict)} 个概念")
            return facts_dict
            
        except Exception as e:
            self.logger.error(f"获取最新财务事实数据失败: {e}")
            return {}
    
    def get_financial_facts_by_section(self, cik: str, section: ReportSection, 
                                     fiscal_year: int = None) -> Dict[str, Any]:
        """
        按报表部分获取财务事实数据
        
        Args:
            cik: 公司CIK码
            section: 报表部分
            fiscal_year: 财政年度
            
        Returns:
            财务事实数据字典
        """
        try:
            # 获取该部分的所有概念
            concepts = FinancialConcepts.get_concepts_by_section(section)
            concept_names = list(concepts.keys())
            
            if not concept_names:
                return {}
            
            # 获取财务事实数据
            facts_df = self.get_financial_facts(cik, fiscal_year=fiscal_year)
            
            if facts_df.empty:
                return {}
            
            # 过滤出该部分的概念
            section_facts = facts_df[facts_df['concept'].isin(concept_names)]
            
            # 转换为字典格式
            facts_dict = {}
            for _, row in section_facts.iterrows():
                concept = row['concept']
                facts_dict[concept] = {
                    'value': row['value'],
                    'unit': row['unit'],
                    'end_date': row['end_date'],
                    'start_date': row['start_date'],
                    'form': row['form'],
                    'filed_date': row['filed_date'],
                    'frame': row['frame'],
                    'fiscal_year': row['fiscal_year'],
                    'fiscal_period': row['fiscal_period']
                }
            
            self.logger.info(f"获取{section.value}部分财务事实数据: {len(facts_dict)} 个概念")
            return facts_dict
            
        except Exception as e:
            self.logger.error(f"获取{section.value}部分财务事实数据失败: {e}")
            return {}
    
    def get_historical_financial_facts(self, cik: str, concept: str, 
                                     years: int = 5):
        """
        获取历史财务事实数据
        
        Args:
            cik: 公司CIK码
            concept: 财务概念名称
            years: 获取的年数
            
        Returns:
            历史财务事实数据DataFrame或列表
        """
        try:
            query = """
                SELECT * FROM financial_facts 
                WHERE cik = ? AND concept = ? AND form = '10-K'
                ORDER BY fiscal_year DESC
                LIMIT ?
            """
            
            if pd is not None:
                result = self.conn.execute(query, [cik, concept, years]).fetchdf()
                self.logger.info(f"获取历史财务事实数据: {concept}, {len(result)} 条记录")
                return result
            else:
                result = self.conn.execute(query, [cik, concept, years]).fetchall()
                self.logger.info(f"获取历史财务事实数据: {concept}, {len(result)} 条记录")
                return result
            
        except Exception as e:
            self.logger.error(f"获取历史财务事实数据失败: {e}")
            return [] if pd is None else pd.DataFrame()
    
    def get_companies_list(self):
        """
        获取所有公司列表
        
        Returns:
            公司列表DataFrame或列表
        """
        try:
            query = "SELECT * FROM companies ORDER BY ticker"
            if pd is not None:
                result = self.conn.execute(query).fetchdf()
                self.logger.info(f"获取公司列表: {len(result)} 家公司")
                return result
            else:
                result = self.conn.execute(query).fetchall()
                self.logger.info(f"获取公司列表: {len(result)} 家公司")
                return result
            
        except Exception as e:
            self.logger.error(f"获取公司列表失败: {e}")
            return [] if pd is None else pd.DataFrame()
    
    def get_available_fiscal_years(self, cik: str) -> List[int]:
        """
        获取可用的财政年度列表
        
        Args:
            cik: 公司CIK码
            
        Returns:
            财政年度列表
        """
        try:
            query = """
                SELECT DISTINCT fiscal_year FROM financial_facts 
                WHERE cik = ? AND form = '10-K'
                ORDER BY fiscal_year DESC
            """
            
            result = self.conn.execute(query, [cik]).fetchall()
            years = [row[0] for row in result if row[0]]
            
            self.logger.info(f"获取可用财政年度: {cik}, {len(years)} 个年度")
            return years
            
        except Exception as e:
            self.logger.error(f"获取可用财政年度失败: {e}")
            return []
    
    def get_available_concepts(self, cik: str, fiscal_year: int = None) -> List[str]:
        """
        获取可用的财务概念列表
        
        Args:
            cik: 公司CIK码
            fiscal_year: 财政年度
            
        Returns:
            财务概念列表
        """
        try:
            query = "SELECT DISTINCT concept FROM financial_facts WHERE cik = ?"
            params = [cik]
            
            if fiscal_year:
                query += " AND fiscal_year = ?"
                params.append(fiscal_year)
            
            query += " ORDER BY concept"
            
            result = self.conn.execute(query, params).fetchall()
            concepts = [row[0] for row in result]
            
            self.logger.info(f"获取可用财务概念: {cik}, {len(concepts)} 个概念")
            return concepts
            
        except Exception as e:
            self.logger.error(f"获取可用财务概念失败: {e}")
            return []
    
    def execute_custom_query(self, query: str, params: List[Any] = None):
        """
        执行自定义查询
        
        Args:
            query: SQL查询语句
            params: 查询参数
            
        Returns:
            查询结果DataFrame或列表
        """
        try:
            if pd is not None:
                if params:
                    result = self.conn.execute(query, params).fetchdf()
                else:
                    result = self.conn.execute(query).fetchdf()
                self.logger.info(f"执行自定义查询: {len(result)} 条记录")
                return result
            else:
                if params:
                    result = self.conn.execute(query, params).fetchall()
                else:
                    result = self.conn.execute(query).fetchall()
                self.logger.info(f"执行自定义查询: {len(result)} 条记录")
                return result
            
        except Exception as e:
            self.logger.error(f"执行自定义查询失败: {e}")
            return [] if pd is None else pd.DataFrame()
    
    def close(self):
        """关闭数据库连接"""
        if self.conn:
            self.conn.close()
            self.logger.info("数据库连接已关闭")
    
    def __enter__(self):
        """上下文管理器入口"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器出口"""
        self.close()
