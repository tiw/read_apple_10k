# Apple 2024年10-K财务概念分析

## 📊 财务事实字段梳理

### 1. 损益表概念 (Income Statement)

| 中文名称 | GAAP概念名称 | 说明 |
|---------|-------------|------|
| 客户合同收入 | RevenueFromContractWithCustomerExcludingAssessedTax | 主要营业收入 |
| 服务和商品成本 | CostOfGoodsAndServicesSold | 营业成本 |
| 毛利润 | GrossProfit | 营业收入减去营业成本 |
| 营业费用 | OperatingExpenses | 总营业费用 |
| 研发费用 | ResearchAndDevelopmentExpense | 研发投入 |
| 一般及行政费用 | GeneralAndAdministrativeExpense | 管理费用 |
| 营业利润 | OperatingIncomeLoss | 营业利润/亏损 |
| 非营业收支 | NonoperatingIncomeExpense | 非经常性收支 |
| 税前持续经营利润 | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 税前利润 |
| 所得税费用 | IncomeTaxExpenseBenefit | 所得税费用/收益 |
| 净利润 | NetIncomeLoss | 净利润/亏损 |
| 基本每股收益 | EarningsPerShareBasic | 基本每股收益 |
| 稀释每股收益 | EarningsPerShareDiluted | 稀释每股收益 |
| 加权平均流通股数（基本） | WeightedAverageNumberOfSharesOutstandingBasic | 基本股数 |
| 加权平均流通股数（稀释） | WeightedAverageNumberOfDilutedSharesOutstanding | 稀释股数 |
| 折旧、耗损和摊销 | DepreciationDepletionAndAmortization | 折旧摊销费用 |

### 2. 资产负债表概念 (Balance Sheet)

| 中文名称 | GAAP概念名称 | 说明 |
|---------|-------------|------|
| 总资产 | Assets | 总资产 |
| 流动资产 | AssetsCurrent | 流动资产 |
| 现金及现金等价物 | CashAndCashEquivalentsAtCarryingValue | 现金及等价物 |
| 流动有价证券 | MarketableSecuritiesCurrent | 短期投资 |
| 应收账款净额 | AccountsReceivableNetCurrent | 应收账款 |
| 存货净额 | InventoryNet | 存货 |
| 非流动资产 | AssetsNoncurrent | 非流动资产 |
| 非流动有价证券 | MarketableSecuritiesNoncurrent | 长期投资 |
| 固定资产净额 | PropertyPlantAndEquipmentNet | 固定资产 |
| 其他非流动资产 | OtherAssetsNoncurrent | 其他长期资产 |
| 总负债 | Liabilities | 总负债 |
| 流动负债 | LiabilitiesCurrent | 流动负债 |
| 应付账款 | AccountsPayableCurrent | 应付账款 |
| 商业票据 | CommercialPaper | 短期借款 |
| 一年内到期的长期债务 | LongTermDebtCurrent | 短期债务 |
| 非流动负债 | LiabilitiesNoncurrent | 非流动负债 |
| 长期债务 | LongTermDebtNoncurrent | 长期债务 |
| 其他非流动负债 | OtherLiabilitiesNoncurrent | 其他长期负债 |
| 股东权益 | StockholdersEquity | 股东权益 |
| 发行的普通股股数 | CommonStockSharesIssued | 发行股数 |
| 留存收益 | RetainedEarningsAccumulatedDeficit | 留存收益/累计亏损 |
| 其他综合收益累计额 | AccumulatedOtherComprehensiveIncomeLossNetOfTax | 其他综合收益 |

### 3. 现金流量表概念 (Cash Flow Statement)

| 中文名称 | GAAP概念名称 | 说明 |
|---------|-------------|------|
| 经营活动现金流 | NetCashProvidedByUsedInOperatingActivities | 经营现金流 |
| 购买固定资产支出 | PaymentsToAcquirePropertyPlantAndEquipment | 资本支出 |
| 支付股息 | PaymentsOfDividends | 股息支付 |
| 回购股票支出 | PaymentsForRepurchaseOfCommonStock | 股票回购 |

## 📈 计算指标梳理

### 1. 盈利能力指标 (Profitability Ratios)

| 指标名称 | 计算公式 | 依赖字段 |
|---------|---------|---------|
| 毛利率 (Gross Margin) | GrossProfit / RevenueFromContractWithCustomerExcludingAssessedTax | GrossProfit, RevenueFromContractWithCustomerExcludingAssessedTax |
| EBITDA | OperatingIncomeLoss + DepreciationDepletionAndAmortization | OperatingIncomeLoss, DepreciationDepletionAndAmortization |
| 营业利润率 (Operating Margin) | EBITDA / RevenueFromContractWithCustomerExcludingAssessedTax | EBITDA, RevenueFromContractWithCustomerExcludingAssessedTax |
| 净利润率 (Net Profit Margin) | NetIncomeLoss / RevenueFromContractWithCustomerExcludingAssessedTax | NetIncomeLoss, RevenueFromContractWithCustomerExcludingAssessedTax |
| 实际税率 (Effective Tax Rate) | IncomeTaxExpenseBenefit / IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | IncomeTaxExpenseBenefit, IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest |
| 基本每股收益 (Basic EPS) | EarningsPerShareBasic | EarningsPerShareBasic |
| 稀释每股收益 (Diluted EPS) | EarningsPerShareDiluted | EarningsPerShareDiluted |

### 2. 流动性指标 (Liquidity Ratios)

| 指标名称 | 计算公式 | 依赖字段 |
|---------|---------|---------|
| 流动比率 (Current Ratio) | AssetsCurrent / LiabilitiesCurrent | AssetsCurrent, LiabilitiesCurrent |
| 速动比率 (Quick Ratio) | (CashAndCashEquivalentsAtCarryingValue + MarketableSecuritiesCurrent + AccountsReceivableNetCurrent) / LiabilitiesCurrent | CashAndCashEquivalentsAtCarryingValue, MarketableSecuritiesCurrent, AccountsReceivableNetCurrent, LiabilitiesCurrent |

### 3. 杠杆比率 (Leverage Ratios)

| 指标名称 | 计算公式 | 依赖字段 |
|---------|---------|---------|
| 资产负债率 (Debt-to-Asset Ratio) | Liabilities / Assets | Liabilities, Assets |
| 股东权益比率 (Equity Ratio) | StockholdersEquity / Assets | StockholdersEquity, Assets |

### 4. 现金流指标 (Cash Flow Metrics)

| 指标名称 | 计算公式 | 依赖字段 |
|---------|---------|---------|
| 自由现金流 (Free Cash Flow) | NetCashProvidedByUsedInOperatingActivities - PaymentsToAcquirePropertyPlantAndEquipment | NetCashProvidedByUsedInOperatingActivities, PaymentsToAcquirePropertyPlantAndEquipment |
| Value Line自由现金流 | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | NetCashProvidedByUsedInOperatingActivities, PaymentsToAcquirePropertyPlantAndEquipment |
| 股息支付率 (Dividend Payout Ratio) | PaymentsOfDividends / NetIncomeLoss | PaymentsOfDividends, NetIncomeLoss |
| 股票回购比例 (Share Buyback Ratio) | PaymentsForRepurchaseOfCommonStock / NetIncomeLoss | PaymentsForRepurchaseOfCommonStock, NetIncomeLoss |

### 5. 回报率指标 (Return Metrics)

| 指标名称 | 计算公式 | 依赖字段 |
|---------|---------|---------|
| 净资产收益率 (ROE) | NetIncomeLoss / StockholdersEquity | NetIncomeLoss, StockholdersEquity |
| 总资本回报率 (ROTC) | (NetIncomeLoss + EstimatedInterestExpense) / (LongTermDebtNoncurrent + StockholdersEquity) | NetIncomeLoss, LongTermDebtNoncurrent, StockholdersEquity, IncomeTaxExpenseBenefit, IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest |
| 留存收益比率 (Retained Earnings Ratio) | (NetIncomeLoss - PaymentsOfDividends) / StockholdersEquity | NetIncomeLoss, PaymentsOfDividends, StockholdersEquity |

### 6. 每股指标 (Per-Share Metrics)

| 指标名称 | 计算公式 | 依赖字段 |
|---------|---------|---------|
| 每股销售额 (Sales per Share) | RevenueFromContractWithCustomerExcludingAssessedTax / WeightedAverageNumberOfDilutedSharesOutstanding | RevenueFromContractWithCustomerExcludingAssessedTax, WeightedAverageNumberOfDilutedSharesOutstanding |
| 每股销售额 (使用发行股数) | RevenueFromContractWithCustomerExcludingAssessedTax / CommonStockSharesIssued | RevenueFromContractWithCustomerExcludingAssessedTax, CommonStockSharesIssued |
| 每股现金流 (Cash Flow per Share) | NetCashProvidedByUsedInOperatingActivities / WeightedAverageNumberOfDilutedSharesOutstanding | NetCashProvidedByUsedInOperatingActivities, WeightedAverageNumberOfDilutedSharesOutstanding |
| 每股现金流 (使用净利润+折旧摊销) | (DepreciationDepletionAndAmortization + NetIncomeLoss) / CommonStockSharesIssued | DepreciationDepletionAndAmortization, NetIncomeLoss, CommonStockSharesIssued |
| 每股账面价值 (Book Value per Share) | StockholdersEquity / WeightedAverageNumberOfDilutedSharesOutstanding | StockholdersEquity, WeightedAverageNumberOfDilutedSharesOutstanding |
| 每股账面价值 (使用发行股数) | StockholdersEquity / CommonStockSharesIssued | StockholdersEquity, CommonStockSharesIssued |
| 每股资本支出 (Capital Spending per Share) | PaymentsToAcquirePropertyPlantAndEquipment / WeightedAverageNumberOfDilutedSharesOutstanding | PaymentsToAcquirePropertyPlantAndEquipment, WeightedAverageNumberOfDilutedSharesOutstanding |
| 每股资本支出 (使用发行股数) | PaymentsToAcquirePropertyPlantAndEquipment / CommonStockSharesIssued | PaymentsToAcquirePropertyPlantAndEquipment, CommonStockSharesIssued |
| 在外流通普通股总数 | CommonStockSharesIssued | CommonStockSharesIssued |

## 📋 报表组合表达

### 1. 损益表 (Income Statement)

**包含指标：**
- 客户合同收入
- 服务和商品成本
- 毛利润
- 营业费用
- 研发费用
- 一般及行政费用
- 营业利润
- 非营业收支
- 税前持续经营利润
- 所得税费用
- 净利润
- 基本每股收益
- 稀释每股收益
- 加权平均流通股数（基本）
- 加权平均流通股数（稀释）
- 折旧、耗损和摊销

### 2. 资产负债表 (Balance Sheet)

**包含指标：**
- 总资产
- 流动资产
  - 现金及现金等价物
  - 流动有价证券
  - 应收账款净额
  - 存货净额
- 非流动资产
  - 非流动有价证券
  - 固定资产净额
  - 其他非流动资产
- 总负债
- 流动负债
  - 应付账款
  - 商业票据
  - 一年内到期的长期债务
- 非流动负债
  - 长期债务
  - 其他非流动负债
- 股东权益
  - 发行的普通股股数
  - 留存收益
  - 其他综合收益累计额

### 3. 现金流量表 (Cash Flow Statement)

**包含指标：**
- 经营活动现金流
- 购买固定资产支出
- 支付股息
- 回购股票支出

### 4. 财务比率分析表

**盈利能力指标：**
- 毛利率
- EBITDA
- 营业利润率
- 净利润率
- 实际税率
- 基本每股收益
- 稀释每股收益

**流动性指标：**
- 流动比率
- 速动比率

**杠杆比率：**
- 资产负债率
- 股东权益比率

**现金流指标：**
- 自由现金流
- Value Line自由现金流
- 股息支付率
- 股票回购比例

**回报率指标：**
- 净资产收益率 (ROE)
- 总资本回报率 (ROTC)
- 留存收益比率

**每股指标：**
- 每股销售额
- 每股现金流
- 每股账面价值
- 每股资本支出
- 在外流通普通股总数

## 📝 注意事项

1. **缺失数据：**
   - 市盈率 (P/E) 和股息收益率需要股价数据支持
   - 某些财务概念可能在不同年份有不同的GAAP名称

2. **负留存收益：**
   - 留存收益为负可能因历史亏损或大额分红/回购

3. **利息费用假设：**
   - ROTC中的利息费用采用公式：EstimatedInterestExpense = LongTermDebtNoncurrent × 4% × (1-实际税率)

4. **数据来源：**
   - 所有数据来源于SEC EDGAR API
   - 基于10-K年度报告数据
   - 财政年度通常为2024年

---

*本分析基于Apple Inc. 2024年10-K年度报告数据整理*
