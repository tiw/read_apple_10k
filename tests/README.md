# XBRL解析器测试CLI

这是一个简单的命令行工具，用于测试XBRL解析器在magnificent_seven_10k_optimized目录下的文件。

## 安装要求

确保已安装所需的Python包：
```bash
pip install duckdb pandas
```

## 使用方法

### 1. 快速测试
测试Apple 2024年的10K报告：
```bash
python tests/test_xbrl_cli.py quick
```

### 2. 列出可用文件
查看所有可用的测试文件：
```bash
python tests/test_xbrl_cli.py list
```

### 3. 测试单个文件
测试特定的XBRL文件：
```bash
python tests/test_xbrl_cli.py test magnificent_seven_10k_optimized/AAPL/20241101/aapl-20240928_htm.xml
```

自定义数据库文件：
```bash
python tests/test_xbrl_cli.py test path/to/file.xml --db my_results.duckdb
```

### 4. 批量测试
测试多个公司的文件：
```bash
python tests/test_xbrl_cli.py batch --companies AAPL AMZN GOOGL --limit 2
```

只测试Apple和Amazon，每个公司限制1个文件：
```bash
python tests/test_xbrl_cli.py batch --companies AAPL AMZN --limit 1
```

## 命令选项

### 全局选项
- `--base-dir`: 指定测试文件的基础目录（默认: magnificent_seven_10k_optimized）

### 测试命令选项
- `--db`: 指定数据库文件路径（默认: test_results.duckdb）

### 批量测试选项
- `--companies`: 指定要测试的公司列表（默认: AAPL AMZN GOOGL）
- `--limit`: 每个公司测试的文件数量限制（默认: 2）

## 输出说明

对于每个测试的文件，CLI会显示：

1. **基本信息**：
   - 公司名称、CIK、股票代码
   - 报告年份和财政期间
   - 期末日期

2. **解析统计**：
   - 上下文数量
   - 事实数据数量
   - 命名空间分布

3. **性能指标**：
   - 解析耗时
   - 存储耗时
   - 总耗时

4. **数据示例**：
   - US-GAAP命名空间中的收入相关数据示例

## 支持的文件格式

CLI支持magnificent_seven目录下所有公司的XBRL文件：
- **AAPL** (Apple Inc.)
- **AMZN** (Amazon.com Inc.)
- **GOOGL** (Alphabet Inc.)
- **MSFT** (Microsoft Corporation)
- **NVDA** (NVIDIA Corporation)
- **META** (Meta Platforms Inc.)
- **TSLA** (Tesla Inc.)

## 数据库输出

测试结果会存储到DuckDB数据库中，包含以下表：
- `companies`: 公司信息
- `xbrl_documents`: 文档元数据
- `contexts`: 上下文信息
- `financial_facts`: 财务数据事实
- `context_dimensions`: 上下文维度

## 故障排除

### 常见问题

1. **文件不存在错误**
   - 确保指定的文件路径正确
   - 使用 `list` 命令查看可用文件

2. **解析失败**
   - 检查文件是否为有效的XBRL格式
   - 查看错误详细信息

3. **存储失败**
   - 确保有足够的磁盘空间
   - 检查数据库文件权限

### 性能考虑

- 大文件（>50MB）会使用流式解析以优化内存使用
- 批量测试会创建新的数据库文件以避免冲突
- 建议在SSD上运行以获得更好的I/O性能

## 示例输出

```
测试文件: magnificent_seven_10k_optimized/AAPL/20241101/aapl-20240928_htm.xml
============================================================
✓ 解析成功 (耗时: 0.02秒)
  公司: Apple Inc.
  CIK: 0000320193
  报告年份: 2024
  财政期间: FY
  上下文数量: 93
  事实数据数量: 583
  命名空间分布:
    us-gaap: 452 个标签
    dei: 62 个标签
    aapl: 50 个标签

✓ 存储成功 (耗时: 0.67秒)
总耗时: 0.79秒
```
