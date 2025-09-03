# XBRL 10K 报告解析器

这是一个高效的XBRL 10K报告解析器，专门用于从SEC 10K报告文件中结构化提取财务数据并存储到数据库中。

## 功能特点

1. **高效XML解析** - 支持大文件的流式解析，内存占用优化
2. **智能上下文分析** - 自动识别当年期间的上下文，过滤不相关数据
3. **全面事实提取** - 提取所有财务数据指标，包括值、单位、精度等信息
4. **多命名空间支持** - 支持us-gaap、dei、公司特定命名空间等
5. **数据库存储** - 结构化存储到DuckDB数据库，支持高效查询
6. **灵活查询接口** - 提供便捷的数据查询和分析功能

## 核心模块

### 1. XBRLParser (主解析器)
- 负责整体解析流程控制
- 提取公司基本信息和报告年份
- 协调各个子模块工作

### 2. ContextAnalyzer (上下文分析器)
- 解析XBRL上下文信息
- 判断当年期间逻辑
- 提取时间维度和业务维度信息

### 3. FactExtractor (事实提取器)
- 提取所有财务数据指标
- 解析命名空间和标签信息
- 处理数值、单位、精度等属性

### 4. DatabaseStorage (数据库存储)
- 将解析结果存储到DuckDB
- 提供数据查询接口
- 支持按公司、年份、命名空间查询

## 数据格式

解析后的数据包含以下信息：
- **公司信息**: 公司名称、CIK、股票代码
- **年份**: 报告年份
- **上下文ID**: XBRL上下文标识符
- **期间信息**: 上下文的时间期间（开始日期、结束日期或即时日期）
- **财务数据**: 标签名、值、命名空间（如us-gaap、dei、aapl等）
- **单位信息**: 数值单位、精度、小数位数

## 使用示例

### 基本使用

```python
from xbrl_analyzer.core.parser import XBRLParser, DatabaseStorage

# 创建解析器
parser = XBRLParser()

# 解析XBRL文件
xbrl_doc = parser.parse_file("path/to/10k-report.xml")

# 存储到数据库
storage = DatabaseStorage("financial_data.duckdb")
document_id = storage.store_document(xbrl_doc)

# 查询数据
facts = storage.query_company_facts(
    company_cik="0000320193",  # Apple
    year=2024,
    namespace="us-gaap"
)
```

### 命令行使用

```bash
# 解析并存储文件
python xbrl_analyzer/core/parser/example.py file.xml

# 分析命名空间分布
python xbrl_analyzer/core/parser/example.py file.xml analyze_namespaces
```

## 测试结果

解析器已在以下文件上测试成功：

1. **Apple 2024 10K** (aapl-20240928_htm.xml)
   - 583条事实数据，93个上下文
   - 命名空间：dei(62), us-gaap(452), aapl(50)

2. **Amazon 2015 10K** (amzn-20151231.xml)
   - 654条事实数据，130个上下文
   - 命名空间：amzn(81), dei(14), us-gaap(559)

## 支持的文件格式

- Apple格式: `company-YYYYMMDD_htm.xml`
- Amazon格式: `company-YYYYMMDD.xml`
- 其他标准XBRL实例文档

## 性能特点

- 支持大文件处理（50MB+）
- 内存优化的流式解析
- 自动过滤非当年数据，提高效率
- DuckDB存储，支持快速查询和分析

## 输入参数

**输入**: 报告文件的路径

**输出**: 结构化的财务数据，包含：
- 公司信息
- 年份信息
- 上下文详情
- 财务指标数据
- 命名空间分类
