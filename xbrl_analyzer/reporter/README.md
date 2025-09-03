# XBRL年报生成器

基于DuckDB数据的10-K年报分析报告生成工具，提供完整的财务报表分析和财务指标计算功能。

## 功能特性

### 📊 财务报表分析

- **损益表 (Income Statement)**: 营业收入、营业成本、毛利润、营业利润、净利润等
- **资产负债表 (Balance Sheet)**: 总资产、流动资产、负债、股东权益等
- **现金流量表 (Cash Flow Statement)**: 经营活动现金流、资本支出、股息支付等

### 📈 财务指标计算

- **盈利能力指标**: 毛利率、营业利润率、净利润率、ROA、ROE等
- **流动性指标**: 流动比率、速动比率等
- **杠杆比率**: 资产负债率、股东权益比率、债务权益比率等
- **效率指标**: 资产周转率、存货周转率等
- **现金流指标**: 自由现金流、股息支付率、股票回购比例等
- **每股指标**: 每股销售额、每股现金流、每股账面价值等

### 📋 报告生成

- **HTML报告**: 美观的网页格式报告，支持响应式设计
- **Markdown报告**: 简洁的Markdown格式报告
- **JSON报告**: 结构化的JSON数据报告
- **数据导出**: 支持CSV、Excel、JSON格式的数据导出

## 安装要求

```bash
pip install duckdb pandas lxml requests
```

## 快速开始

### 1. 基本使用

```python
from xbrl_analyzer.reporter import AnnualReportGenerator

# 创建年报生成器
with AnnualReportGenerator(output_dir="./reports") as generator:
    # 生成Apple公司的2024年年报
    results = generator.generate_ticker_report(
        ticker="AAPL",
        fiscal_year=2024,
        output_formats=['html', 'markdown', 'json']
    )
    
    print("报告生成完成!")
    print(f"HTML报告: {results['html']}")
    print(f"Markdown报告: {results['markdown']}")
    print(f"JSON报告: {results['json']}")
```

### 2. 批量生成报告

```python
# 七朵金花公司列表
magnificent_seven = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA"]

with AnnualReportGenerator(output_dir="./reports") as generator:
    # 批量生成年报
    results = generator.generate_batch_reports(
        tickers=magnificent_seven,
        fiscal_year=2024,
        output_formats=['html', 'markdown']
    )
    
    print(f"批量生成完成: {results['summary']['successful']}/{results['summary']['total_companies']} 成功")
```

### 3. 数据导出

```python
with AnnualReportGenerator(output_dir="./reports") as generator:
    # 导出财务数据为CSV
    csv_file = generator.export_financial_data(
        cik="0000320193",  # Apple的CIK
        fiscal_year=2024,
        output_format='csv'
    )
    
    print(f"财务数据已导出: {csv_file}")
```

## 核心组件

### 1. DuckDBInterface

数据库接口，提供财务数据的存储和查询功能。

```python
from xbrl_analyzer.reporter import DuckDBInterface

with DuckDBInterface() as db:
    # 插入公司信息
    db.insert_company(
        cik="0000320193",
        ticker="AAPL", 
        name="Apple Inc."
    )
    
    # 获取财务事实
    facts = db.get_latest_financial_facts("0000320193")
```

### 2. FinancialCalculator

财务指标计算器，提供各种财务比率的计算。

```python
from xbrl_analyzer.reporter import FinancialCalculator

calculator = FinancialCalculator()

# 计算单个指标
gross_margin = calculator.calculate_metric('gross_margin', financial_facts)

# 计算所有指标
all_metrics = calculator.calculate_all_metrics(financial_facts)
```

### 3. ReportTemplates

报表模板，提供HTML、Markdown等格式的报告生成。

```python
from xbrl_analyzer.reporter import ReportTemplates

templates = ReportTemplates()

# 生成HTML报告
html_content = templates.generate_html_report(
    company_info, financial_facts, calculated_metrics, concepts, fiscal_year
)
```

## 财务概念定义

### 损益表概念

- `RevenueFromContractWithCustomerExcludingAssessedTax`: 营业收入
- `CostOfGoodsAndServicesSold`: 营业成本
- `GrossProfit`: 毛利润
- `OperatingIncomeLoss`: 营业利润
- `NetIncomeLoss`: 净利润
- `EarningsPerShareBasic`: 基本每股收益
- `EarningsPerShareDiluted`: 稀释每股收益

### 资产负债表概念

- `Assets`: 总资产
- `AssetsCurrent`: 流动资产
- `CashAndCashEquivalentsAtCarryingValue`: 现金及现金等价物
- `Liabilities`: 总负债
- `StockholdersEquity`: 股东权益
- `CommonStockSharesIssued`: 发行的普通股股数

### 现金流量表概念

- `NetCashProvidedByUsedInOperatingActivities`: 经营活动现金流
- `PaymentsToAcquirePropertyPlantAndEquipment`: 购买固定资产支出
- `PaymentsOfDividends`: 支付股息
- `PaymentsForRepurchaseOfCommonStock`: 回购股票支出

## 计算指标

### 盈利能力指标

- **毛利率**: `GrossProfit / RevenueFromContractWithCustomerExcludingAssessedTax`
- **营业利润率**: `OperatingIncomeLoss / RevenueFromContractWithCustomerExcludingAssessedTax`
- **净利润率**: `NetIncomeLoss / RevenueFromContractWithCustomerExcludingAssessedTax`
- **总资产收益率 (ROA)**: `NetIncomeLoss / Assets`
- **股东权益收益率 (ROE)**: `NetIncomeLoss / StockholdersEquity`

### 流动性指标

- **流动比率**: `AssetsCurrent / LiabilitiesCurrent`
- **速动比率**: `(Cash + MarketableSecurities + Receivables) / LiabilitiesCurrent`

### 杠杆比率

- **资产负债率**: `Liabilities / Assets`
- **股东权益比率**: `StockholdersEquity / Assets`
- **债务权益比率**: `Liabilities / StockholdersEquity`

### 现金流指标

- **自由现金流**: `OperatingCashFlow - CapitalExpenditure`
- **股息支付率**: `DividendPayments / NetIncome`
- **股票回购比例**: `ShareBuybacks / NetIncome`

## 示例报告

生成的HTML报告包含以下部分：

1. **公司信息**: 公司名称、股票代码、CIK码等基本信息
2. **损益表**: 完整的损益表数据展示
3. **资产负债表**: 资产、负债、股东权益数据
4. **现金流量表**: 现金流相关数据
5. **财务指标分析**: 按类别分组的财务指标
6. **数据摘要**: 统计信息和成功率

## 运行示例

```bash
# 运行使用示例
python xbrl_analyzer/reporter/example_usage.py

# 运行测试
python xbrl_analyzer/reporter/test_reporter.py
```

## 注意事项

1. **数据依赖**: 需要先有财务数据才能生成报告
2. **概念匹配**: 不同公司的财务概念可能略有差异
3. **计算精度**: 财务指标计算可能存在舍入误差
4. **数据完整性**: 缺少必要数据时，相关指标将显示为"N/A"

## 扩展功能

### 自定义指标

可以通过继承`FinancialCalculator`类来添加自定义的财务指标计算。

### 自定义模板

可以通过修改`ReportTemplates`类来定制报告格式和样式。

### 数据库集成

支持与现有的DuckDB数据库集成，也可以使用内存数据库进行快速测试。

## 许可证

本项目采用MIT许可证。
