# SEC索引下载工具使用说明

## 概述

`sec_index_downloader_tool.py` 是一个基于SEC索引的10-K文件下载工具。与之前的 `sec_10k_downloader.py` 不同，这个工具通过下载SEC的 `master.idx` 索引文件来查找和下载10-K文件，支持批量下载多个季度的数据。

## 主要特性

1. **基于索引下载**: 通过下载SEC的 `master.idx` 文件来查找10-K文件
2. **多季度支持**: 可以下载最多4个季度的数据
3. **自动文件解析**: 自动解析 `MetaLinks.json` 或HTML目录来获取XBRL文件列表
4. **智能文件组织**: 按日期创建子目录组织下载的文件
5. **错误处理**: 完善的错误处理和重试机制

## 使用方法

### 基本用法

```bash
# 下载AAPL最近4个季度的10-K文件
python xbrl_analyzer/tools/sec_index_downloader_tool.py --ticker AAPL

# 下载指定年份的10-K文件
python xbrl_analyzer/tools/sec_index_downloader_tool.py --ticker AAPL --year 2024

# 指定输出目录
python xbrl_analyzer/tools/sec_index_downloader_tool.py --ticker AAPL --output-dir ./my_data

# 限制下载季度数
python xbrl_analyzer/tools/sec_index_downloader_tool.py --ticker AAPL --max-quarters 2
```

### 参数说明

- `--ticker`: 公司股票代码（必需），例如 AAPL、MSFT、GOOGL
- `--year`: 指定年份（可选），如果不指定则下载最近几个季度
- `--max-quarters`: 最大季度数（默认4），最多下载4个季度的数据
- `--output-dir`: 输出目录（默认 ./10k_xbrl）

## 工作流程

1. **获取CIK码**: 根据股票代码从 `company_tickers.json` 获取CIK码
2. **确定季度**: 根据参数确定要下载的季度列表
3. **下载索引**: 下载指定季度的 `master.idx` 文件
4. **解析索引**: 解析索引文件，查找指定公司的10-K文件
5. **下载XBRL**: 下载找到的10-K文件的XBRL相关文件

## 文件结构

下载的文件会按以下结构组织：

```
output_dir/
├── master_2024_Q4.idx          # 下载的索引文件
├── master_2024_Q3.idx
├── 20240928/                   # 按日期组织的10-K文件
│   ├── aapl-20240928.xsd
│   ├── aapl-20240928_cal.xml
│   ├── aapl-20240928_def.xml
│   ├── aapl-20240928_lab.xml
│   ├── aapl-20240928_pre.xml
│   └── aapl-20240928_htm.xml
└── 20230930/
    └── ...
```

## 下载的文件类型

工具会下载以下类型的XBRL文件：

- **实例文档**: `*_htm.xml` (主要的财务数据文件)
- **模式文件**: `*.xsd` (XBRL模式定义)
- **计算链接**: `*_cal.xml` (计算关系)
- **定义链接**: `*_def.xml` (定义关系)
- **标签链接**: `*_lab.xml` (标签信息)
- **展示链接**: `*_pre.xml` (展示关系)

## 与旧工具的区别

| 特性 | sec_10k_downloader.py | sec_index_downloader_tool.py |
|------|----------------------|------------------------------|
| 数据源 | SEC API submissions | SEC master.idx 索引 |
| 批量下载 | 单次下载 | 支持多季度批量下载 |
| 文件组织 | 平铺结构 | 按日期分目录 |
| 索引文件 | 不保存 | 保存master.idx文件 |
| 适用场景 | 单次下载最新文件 | 批量下载历史数据 |

## 注意事项

1. **网络延迟**: 工具会在请求之间添加延迟以避免被SEC限制
2. **文件大小**: master.idx文件可能很大，下载需要时间
3. **错误处理**: 如果某个季度下载失败，会跳过继续处理其他季度
4. **依赖文件**: 需要 `company_tickers.json` 文件来获取CIK码

## 测试

运行测试脚本：

```bash
python test_sec_index_downloader.py
```

## 示例输出

```
找到 AAPL 的CIK码: 320193
将下载以下季度的索引: [(2024, 4), (2024, 3), (2024, 2), (2024, 1)]

处理 2024年Q4...
正在下载 https://www.sec.gov/Archives/edgar/full-index/2024/QTR4/master.idx
已保存到 ./10k_xbrl/master_2024_Q4.idx
在 master_2024_Q4.idx 中找到 1 个10-K文件
  找到10-K: 2024-09-28 - edgar/data/320193/0000320193-24-000096/0000320193-24-000096.txt

总共找到 1 个10-K文件

下载第 1 个10-K文件 (日期: 2024-09-28)
正在从目录获取文件列表: https://www.sec.gov/Archives/edgar/data/320193/0000320193-24-000096/
尝试获取MetaLinks.json: https://www.sec.gov/Archives/edgar/data/320193/0000320193-24-000096/MetaLinks.json
从MetaLinks.json获取到 6 个文件
正在下载 https://www.sec.gov/Archives/edgar/data/320193/0000320193-24-000096/aapl-20240928.xsd
已保存到 ./10k_xbrl/20240928/aapl-20240928.xsd
...

成功下载 1/1 个10-K文件
```
