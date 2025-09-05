# Financial Statements MCP Service

一个基于FastMCP的财务报表服务，提供七大科技巨头（苹果、微软、谷歌、亚马逊、Meta、特斯拉、英伟达）的财务报表数据访问。

## 功能特性

- **三大财务报表**：资产负债表、损益表、现金流量表
- **智能数据提取**：基于XBRL context定义自动选择正确的财务数据
- **数据验证**：内置会计等式验证和数据质量评分
- **多公司支持**：支持7家主要科技公司的财务数据
- **多年度数据**：支持历史财务年度数据查询

## 支持的公司

| 股票代码 | 公司名称 | CIK |
|---------|---------|-----|
| AAPL | Apple Inc. | 0000320193 |
| MSFT | Microsoft Corporation | 0000789019 |
| GOOGL | Alphabet Inc. | 0001652044 |
| AMZN | Amazon.com Inc. | 0001018724 |
| META | Meta Platforms Inc. | 0001326801 |
| TSLA | Tesla Inc. | 0001318605 |
| NVDA | NVIDIA Corporation | 0001045810 |

## 安装和使用

### 1. 激活虚拟环境

```bash
source venv/bin/activate
```

### 2. 运行MCP服务

```bash
python financial_statements_mcp.py
```

### 3. 使用Python API

```python
from financial_statements_service import FinancialStatementsService

# 初始化服务
service = FinancialStatementsService()

# 获取完整财务报表
statements = service.get_financial_statements("AAPL", 2024)

# 获取单个报表
balance_sheet = service.get_balance_sheet("AAPL", 2024)
income_statement = service.get_income_statement("AAPL", 2024)
cash_flow = service.get_cash_flow_statement("AAPL", 2024)

# 获取支持的公司列表
companies = service.get_supported_companies()

# 获取公司信息
company_info = service.get_company_info("AAPL")
```

## MCP工具接口

### get_financial_statements
获取完整的财务报表数据

**参数：**
- `company_symbol`: 公司股票代码（如 "AAPL"）
- `year`: 财政年度（如 2024）

**返回：** 完整的财务报表数据，包括资产负债表、损益表、现金流量表

### get_balance_sheet
获取资产负债表数据

**参数：**
- `company_symbol`: 公司股票代码
- `year`: 财政年度

**返回：** 资产负债表数据

### get_income_statement
获取损益表数据

**参数：**
- `company_symbol`: 公司股票代码
- `year`: 财政年度

**返回：** 损益表数据

### get_cash_flow_statement
获取现金流量表数据

**参数：**
- `company_symbol`: 公司股票代码
- `year`: 财政年度

**返回：** 现金流量表数据

### get_supported_companies
获取支持的公司列表

**返回：** 支持的公司股票代码列表

### get_company_info
获取公司信息

**参数：**
- `company_symbol`: 公司股票代码

**返回：** 公司名称和CIK信息

## 数据结构

### 资产负债表 (Balance Sheet)
```python
{
    "assets": {
        "current_assets": float,
        "cash_and_equivalents": float,
        "marketable_securities_current": float,
        "accounts_receivable": float,
        "inventory": float,
        "other_current_assets": float,
        "noncurrent_assets": float,
        "property_plant_equipment": float,
        "marketable_securities_noncurrent": float,
        "other_noncurrent_assets": float
    },
    "liabilities": {
        "current_liabilities": float,
        "accounts_payable": float,
        "other_current_liabilities": float,
        "contract_liabilities": float,
        "commercial_paper": float,
        "long_term_debt_current": float,
        "noncurrent_liabilities": float,
        "long_term_debt_noncurrent": float,
        "other_noncurrent_liabilities": float
    },
    "equity": {
        "common_stock": float,
        "retained_earnings": float,
        "accumulated_other_comprehensive_income": float
    },
    "total_assets": float,
    "total_liabilities": float,
    "total_equity": float
}
```

### 损益表 (Income Statement)
```python
{
    "revenue": float,
    "cost_of_goods_sold": float,
    "gross_profit": float,
    "operating_expenses": {
        "research_development": float,
        "selling_general_administrative": float,
        "total_operating_expenses": float
    },
    "operating_income": float,
    "net_income": float,
    "eps_basic": float,
    "eps_diluted": float
}
```

### 现金流量表 (Cash Flow Statement)
```python
{
    "operating_activities": float,
    "investing_activities": float,
    "financing_activities": float,
    "net_cash_flow": float
}
```

## 技术特点

### 智能Context分析
- 自动解析XBRL文件中的context定义
- 根据财务指标类型选择合适的context
- 资产负债表：选择instant类型的year-end context
- 损益表：选择duration类型的fiscal year context
- EPS：选择instant类型的year-end context

### 数据验证
- 会计等式验证：资产 = 负债 + 权益
- 毛利计算验证：毛利 = 收入 - 销售成本
- 数据完整性检查
- 数据质量评分

### 性能优化
- 数据库查询优化
- Context缓存机制
- 并行数据处理

## 运行示例

```bash
# 运行测试脚本
python test_financial_service.py

# 运行使用示例
python usage_example.py
```

## 数据源

- **主要数据源**：DuckDB数据库 (`magnificent_seven_xbrl.duckdb`)
- **XBRL文件**：`magnificent_seven_10k_optimized/` 目录下的SEC XBRL文件
- **公司信息**：SEC公司标识映射

## 错误处理

服务包含完整的错误处理机制：
- 无效公司代码处理
- 无效年度处理
- 数据缺失处理
- 数据库连接错误处理
- XML解析错误处理

## 扩展性

服务设计具有良好的扩展性：
- 可以轻松添加新的公司支持
- 支持新的财务指标
- 可扩展的数据验证规则
- 灵活的context选择策略

## 许可证

内部使用，请遵循公司数据使用政策。