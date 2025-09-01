基于context_analyzer.py文件中的CLI工具功能，我来设计一个数据库结构，用于更好地管理这些XBRL数据。

## 数据库设计方案

### 1. 核心实体设计

#### 1.1 XBRL文件表 (xbrl_files)
存储XBRL文件的基本信息：
- id (主键)
- file_path (文件路径)
- company_name (公司名称)
- filing_type (文件类型，如10-K)
- fiscal_year (财政年度)
- fiscal_period (财政期间)
- period_end_date (期间结束日期)
- created_at (创建时间)

#### 1.2 上下文表 (contexts)
存储XBRL中的上下文信息：
- id (主键)
- xbrl_file_id (外键，关联XBRL文件)
- context_id (XBRL中的context ID)
- period_type (期间类型：instant, duration)
- start_date (开始日期，可为空)
- end_date (结束日期，可为空)
- instant_date (即时日期，可为空)

#### 1.3 维度表 (dimensions)
存储上下文中的维度信息：
- id (主键)
- context_id (外键，关联contexts表)
- dimension_name (维度名称，如ProductOrServiceAxis)
- member_name (成员名称，如IPhoneMember)

#### 1.4 财务标签表 (financial_tags)
存储财务标签信息：
- id (主键)
- tag_name (标签名称，如RevenueFromContractWithCustomerExcludingAssessedTax)
- chinese_name (中文名称)
- namespace (命名空间)
- description (描述)

#### 1.5 财务事实表 (financial_facts)
存储具体的财务数据：
- id (主键)
- xbrl_file_id (外键，关联XBRL文件)
- context_id (外键，关联contexts表)
- tag_id (外键，关联financial_tags表)
- value (数值)
- unit (单位)
- decimals (小数位数)

#### 1.6 计算规则表 (calculation_rules)
存储计算规则：
- id (主键)
- xbrl_file_id (外键，关联XBRL文件)
- role (角色)
- from_tag_id (起始标签ID)
- to_tag_id (目标标签ID)
- weight (权重)

### 2. 关系设计

1. 一个XBRL文件包含多个上下文 (1:N)
2. 一个上下文包含多个维度 (1:N)
3. 一个XBRL文件包含多个财务事实 (1:N)
4. 一个财务事实关联一个上下文和一个标签 (N:1)
5. 一个XBRL文件包含多个计算规则 (1:N)
6. 计算规则连接两个标签 (N:1)

### 3. 功能映射

#### 3.1 list_all_contexts功能
通过查询contexts表获取特定XBRL文件的所有context_id

#### 3.2 list_facts_for_context功能
通过关联查询contexts、financial_facts和financial_tags表，获取特定上下文的所有财务事实

#### 3.3 list_facts_by_presentation功能
通过presentation角色信息和标签关联，对财务事实进行分组展示

#### 3.4 calculate_formulas功能
通过calculation_rules表中的规则，对financial_facts表中的数值进行计算验证

### 4. 扩展性考虑

#### 4.1 多公司支持
通过xbrl_files表中的company_name字段支持多公司数据存储

#### 4.2 时间序列分析
通过contexts表中的时间信息支持跨年度数据分析

#### 4.3 维度分析
通过dimensions表支持按产品、地区等维度的数据切片

#### 4.4 多语言支持
通过financial_tags表中的chinese_name字段支持多语言标签

### 5. 性能优化建议

1. 在常用查询字段上建立索引（如context_id、tag_name等）
2. 对时间相关查询建立复合索引
3. 对大数据量表进行分区（如按年份对financial_facts表分区）
4. 使用视图简化复杂查询

### 6. 数据一致性保证

1. 使用外键约束保证数据完整性
2. 使用触发器自动维护汇总数据
3. 定期进行数据校验确保计算规则的一致性

这个数据库设计可以有效地支持当前CLI工具的所有功能，并为未来扩展提供良好的基础。