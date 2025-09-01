-- 创建XBRL文件表
CREATE TABLE xbrl_files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT NOT NULL UNIQUE,
    company_name TEXT,
    filing_type TEXT,
    fiscal_year INTEGER,
    fiscal_period TEXT,
    period_end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建上下文表
CREATE TABLE contexts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    xbrl_file_id INTEGER NOT NULL,
    context_id TEXT NOT NULL,
    period_type TEXT CHECK(period_type IN ('instant', 'duration')),
    start_date DATE,
    end_date DATE,
    instant_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (xbrl_file_id) REFERENCES xbrl_files(id) ON DELETE CASCADE,
    UNIQUE(xbrl_file_id, context_id)
);

-- 创建维度表
CREATE TABLE dimensions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    context_id INTEGER NOT NULL,
    dimension_name TEXT NOT NULL,
    member_name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (context_id) REFERENCES contexts(id) ON DELETE CASCADE
);

-- 创建财务标签表
CREATE TABLE financial_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag_name TEXT NOT NULL UNIQUE,
    chinese_name TEXT,
    namespace TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建财务事实表
CREATE TABLE financial_facts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    xbrl_file_id INTEGER NOT NULL,
    context_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    value DECIMAL(15,2),
    unit TEXT,
    decimals INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (xbrl_file_id) REFERENCES xbrl_files(id) ON DELETE CASCADE,
    FOREIGN KEY (context_id) REFERENCES contexts(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES financial_tags(id) ON DELETE CASCADE,
    UNIQUE(xbrl_file_id, context_id, tag_id)
);

-- 创建计算规则表
CREATE TABLE calculation_rules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    xbrl_file_id INTEGER NOT NULL,
    role TEXT,
    from_tag_id INTEGER NOT NULL,
    to_tag_id INTEGER NOT NULL,
    weight DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (xbrl_file_id) REFERENCES xbrl_files(id) ON DELETE CASCADE,
    FOREIGN KEY (from_tag_id) REFERENCES financial_tags(id) ON DELETE CASCADE,
    FOREIGN KEY (to_tag_id) REFERENCES financial_tags(id) ON DELETE CASCADE
);

-- 创建索引以提高查询性能
CREATE INDEX idx_contexts_xbrl_file_id ON contexts(xbrl_file_id);
CREATE INDEX idx_contexts_context_id ON contexts(context_id);
CREATE INDEX idx_dimensions_context_id ON dimensions(context_id);
CREATE INDEX idx_dimensions_dimension_name ON dimensions(dimension_name);
CREATE INDEX idx_financial_facts_context_id ON financial_facts(context_id);
CREATE INDEX idx_financial_facts_tag_id ON financial_facts(tag_id);
CREATE INDEX idx_financial_facts_xbrl_file_id ON financial_facts(xbrl_file_id);
CREATE INDEX idx_calculation_rules_xbrl_file_id ON calculation_rules(xbrl_file_id);
CREATE INDEX idx_calculation_rules_from_tag_id ON calculation_rules(from_tag_id);