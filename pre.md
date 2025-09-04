GAAP 毛利相关指标和关系

  损益表结构 (Income Statement Structure)

  StatementLineItems
  ├── RevenueFromContractWithCustomerExcludingAssessedTax (order=1)
  ├── CostOfGoodsAndServicesSold (order=2)
  └── GrossProfit (order=3) [totalLabel]

  毛利计算逻辑

  - 毛利 = 收入 - 销售成本
  - GrossProfit = RevenueFromContractWithCustomerExcludingAssessedTax - CostOfGoodsAndServicesSold

  营业支出结构

  OperatingExpensesAbstract
  ├── ResearchAndDevelopmentExpense (order=1)
  ├── SellingGeneralAndAdministrativeExpense (order=2)
  └── OperatingExpenses (order=3) [totalLabel]

  营业利润计算

  - 营业利润 = 毛利 - 营业支出
  - OperatingIncomeLoss = GrossProfit - OperatingExpenses

  GAAP 资产结构相关指标和关系

  资产负债表结构 (Balance Sheet Structure)

  StatementOfFinancialPositionAbstract
  ├── AssetsAbstract (order=1)
  │   ├── AssetsCurrentAbstract (order=1)
  │   │   ├── CashAndCashEquivalentsAtCarryingValue (order=1)
  │   │   ├── MarketableSecuritiesCurrent (order=2)
  │   │   ├── AccountsReceivableNetCurrent (order=3)
  │   │   ├── NontradeReceivablesCurrent (order=4)
  │   │   ├── InventoryNet (order=5)
  │   │   ├── OtherAssetsCurrent (order=6)
  │   │   └── AssetsCurrent (order=7) [totalLabel]
  │   ├── AssetsNoncurrentAbstract (order=2)
  │   │   ├── MarketableSecuritiesNoncurrent (order=1)
  │   │   ├── PropertyPlantAndEquipmentNet (order=2)
  │   │   ├── OtherAssetsNoncurrent (order=3)
  │   │   └── AssetsNoncurrent (order=4) [totalLabel]
  │   └── Assets (order=3) [totalLabel]

  负债和股东权益结构

  LiabilitiesAndStockholdersEquityAbstract (order=2)
  ├── LiabilitiesCurrentAbstract (order=1)
  │   ├── AccountsPayableCurrent (order=1)
  │   ├── OtherLiabilitiesCurrent (order=2)
  │   ├── ContractWithCustomerLiabilityCurrent (order=3)
  │   ├── CommercialPaper (order=4)
  │   ├── LongTermDebtCurrent (order=5)
  │   └── LiabilitiesCurrent (order=6) [totalLabel]
  ├── LiabilitiesNoncurrentAbstract (order=2)
  │   ├── LongTermDebtNoncurrent (order=1)
  │   ├── OtherLiabilitiesNoncurrent (order=2)
  │   └── LiabilitiesNoncurrent (order=3) [totalLabel]
  ├── Liabilities (order=3) [totalLabel]
  └── StockholdersEquityAbstract (order=7)
      ├── CommonStocksIncludingAdditionalPaidInCapital (order=1)
      ├── RetainedEarningsAccumulatedDeficit (order=2)
      ├── AccumulatedOtherComprehensiveIncomeLossNetOfTax (order=3)
      └── StockholdersEquity (order=4) [totalLabel]


