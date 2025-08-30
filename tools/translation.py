"""
Financial term translations from English to Chinese
"""

# 财务术语中英文对照字典
FINANCIAL_TERMS = {
    # 基本公司信息
    "AmendmentFlag": "修订标志",
    "DocumentFiscalYearFocus": "文件财政年度焦点",
    "DocumentFiscalPeriodFocus": "文件财政期间焦点",
    "EntityCentralIndexKey": "实体中央索引键",
    "DocumentType": "文件类型",
    "DocumentAnnualReport": "年度报告文件",
    "DocumentPeriodEndDate": "文件期间结束日期",
    "CurrentFiscalYearEndDate": "当前财政年度结束日期",
    "DocumentTransitionReport": "过渡期报告",
    "EntityFileNumber": "实体文件编号",
    "EntityRegistrantName": "实体注册人名称",
    "EntityIncorporationStateCountryCode": "实体注册州/国家代码",
    "EntityTaxIdentificationNumber": "实体税务识别号",
    "EntityAddressAddressLine1": "实体地址第一行",
    "EntityAddressCityOrTown": "实体城市或城镇",
    "EntityAddressStateOrProvince": "实体州或省",
    "EntityAddressPostalZipCode": "实体邮政编码",
    "CityAreaCode": "城市区号",
    "LocalPhoneNumber": "本地电话号码",
    "EntityWellKnownSeasonedIssuer": "知名成熟发行人实体",
    "EntityVoluntaryFilers": "自愿申报实体",
    "EntityCurrentReportingStatus": "实体当前报告状态",
    "EntityInteractiveDataCurrent": "实体交互式数据当前状态",
    "EntityFilerCategory": "实体申报类别",
    "EntitySmallBusiness": "小企业实体",
    "EntityEmergingGrowthCompany": "新兴成长公司实体",
    "IcfrAuditorAttestationFlag": "ICFR审计师证明标志",
    "DocumentFinStmtErrorCorrectionFlag": "财务报表错误更正标志",
    "EntityShellCompany": "空壳公司实体",
    "DocumentsIncorporatedByReferenceTextBlock": "参考文献档文本块",
    
    # 收入和成本相关
    "RevenueFromContractWithCustomerExcludingAssessedTax": "来自与客户合同的收入（不含评估税）",
    "CostOfGoodsAndServicesSold": "已售商品和服务成本",
    "GrossProfit": "毛利润",
    "ResearchAndDevelopmentExpense": "研发费用",
    "SellingGeneralAndAdministrativeExpense": "销售、一般和行政费用",
    "OperatingExpenses": "营业费用",
    "OperatingIncomeLoss": "营业收入/亏损",
    "NonoperatingIncomeExpense": "非营业收入/费用",
    "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest": "持续经营业务税前收入/亏损（不含非常项目和非控股权益）",
    "IncomeTaxExpenseBenefit": "所得税费用/收益",
    "NetIncomeLoss": "净利润/亏损",
    
    # 每股收益
    "EarningsPerShareBasic": "基本每股收益",
    "EarningsPerShareDiluted": "稀释每股收益",
    "WeightedAverageNumberOfSharesOutstandingBasic": "基本流通股加权平均数",
    "WeightedAverageNumberOfDilutedSharesOutstanding": "稀释流通股加权平均数",
    "IncrementalCommonSharesAttributableToShareBasedPaymentArrangements": "归属于股份支付安排的增量普通股",
    
    # 综合收益
    "OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax": "外币交易和折算调整的其他综合收益/损失（税后）",
    "OtherComprehensiveIncomeLossDerivativeInstrumentGainLossbeforeReclassificationafterTax": "衍生工具收益/损失的其他综合收益/损失（税后重分类前）",
    "OtherComprehensiveIncomeLossDerivativeInstrumentGainLossReclassificationAfterTax": "衍生工具收益/损失重分类的其他综合收益/损失（税后）",
    "OtherComprehensiveIncomeLossDerivativeInstrumentGainLossafterReclassificationandTax": "衍生工具收益/损失的其他综合收益/损失（重分类和税后）",
    "OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodNetOfTax": "期间证券未实现持有收益/损失（税后）",
    "OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesNetOfTax": "证券出售的累计其他综合收益重分类调整（税后）",
    "OtherComprehensiveIncomeLossAvailableForSaleSecuritiesAdjustmentNetOfTax": "可供出售证券调整的其他综合收益/损失（税后）",
    "OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent": "归属于母公司股东的税后其他综合收益/损失",
    "ComprehensiveIncomeNetOfTax": "税后综合收益",
    
    # 分红
    "CommonStockDividendsPerShareDeclared": "普通股每股宣告股息",
    
    # 现金流量表项目
    "DepreciationDepletionAndAmortization": "折旧、耗减和摊销",
    "ShareBasedCompensation": "股份支付",
    "OtherNoncashIncomeExpense": "其他非现金收入/费用",
    "IncreaseDecreaseInAccountsReceivable": "应收账款增减",
    "IncreaseDecreaseInOtherReceivables": "其他应收款增减",
    "IncreaseDecreaseInInventories": "存货增减",
    "IncreaseDecreaseInOtherOperatingAssets": "其他经营资产增减",
    "IncreaseDecreaseInAccountsPayable": "应付账款增减",
    "IncreaseDecreaseInOtherOperatingLiabilities": "其他经营负债增减",
    "NetCashProvidedByUsedInOperatingActivities": "经营活动产生的现金流量净额",
    "PaymentsToAcquireAvailableForSaleSecuritiesDebt": "购买可供出售债务证券的支付",
    "ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities": "可供出售证券到期、预付和赎回的收入",
    "ProceedsFromSaleOfAvailableForSaleSecuritiesDebt": "出售可供出售债务证券的收入",
    "PaymentsToAcquirePropertyPlantAndEquipment": "购买财产、厂房和设备的支付",
    "PaymentsForProceedsFromOtherInvestingActivities": "其他投资活动的支付/收入",
    "NetCashProvidedByUsedInInvestingActivities": "投资活动产生的现金流量净额",
    "PaymentsRelatedToTaxWithholdingForShareBasedCompensation": "与股份支付相关的税款预扣",
    "PaymentsOfDividends": "股息支付",
    "PaymentsForRepurchaseOfCommonStock": "回购普通股的支付",
    "ProceedsFromIssuanceOfLongTermDebt": "长期债务发行收入",
    "RepaymentsOfLongTermDebt": "长期债务偿还",
    "ProceedsFromRepaymentsOfCommercialPaper": "商业票据收入/偿还",
    "ProceedsFromPaymentsForOtherFinancingActivities": "其他融资活动的收入/支付",
    "NetCashProvidedByUsedInFinancingActivities": "融资活动产生的现金流量净额",
    "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect": "现金、现金等价物、受限制现金和受限制现金等价物期间增减（含汇率影响）",
    "IncomeTaxesPaidNet": "所得税净支付",
    
    # 会计政策
    "BasisOfPresentationAndSignificantAccountingPoliciesTextBlock": "财务报表编制基础和重要会计政策文本块",
    "BasisOfAccountingPolicyPolicyTextBlock": "会计政策文本块",
    "FiscalPeriod": "财政期间",
    "RevenueRecognitionPolicyTextBlock": "收入确认政策文本块",
    "CompensationRelatedCostsPolicyTextBlock": "薪酬相关成本政策文本块",
    "CashAndCashEquivalentsPolicyTextBlock": "现金及现金等价物政策文本块",
    "MarketableSecuritiesPolicy": "有价证券政策",
    "InventoryPolicyTextBlock": "存货政策文本块",
    "PropertyPlantAndEquipmentPolicyTextBlock": "财产、厂房和设备政策文本块",
    "DerivativesPolicyTextBlock": "衍生工具政策文本块",
    "IncomeTaxPolicyTextBlock": "所得税政策文本块",
    "LesseeLeasesPolicyTextBlock": "承租人租赁政策文本块",
    
    # 收入分解
    "RevenueFromContractWithCustomerTextBlock": "来自与客户合同的收入文本块",
    "DisaggregationOfRevenueTableTextBlock": "收入分解表文本块",
    "ContractWithCustomerLiabilityRevenueRecognized": "与客户合同负债确认的收入",
    
    # 每股收益
    "EarningsPerShareTextBlock": "每股收益文本块",
    "ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock": "基本和稀释每股收益表文本块",
    
    # 金融工具
    "FinancialInstrumentsDisclosureTextBlock": "金融工具披露文本块",
    "ScheduleOfCashCashEquivalentsAndShortTermInvestmentsTableTextBlock": "现金、现金等价物和短期投资表文本块",
    "FairValueMeasurementPolicyPolicyTextBlock": "公允价值计量政策文本块",
    "ScheduleOfNotionalAmountsOfOutstandingDerivativePositionsTableTextBlock": "未平仓衍生品名义金额表文本块",
    "ScheduleOfFairValueHedgingInstrumentsStatementsOfFinancialPerformanceAndFinancialPositionLocationTableTextBlock": "公允价值套期保值工具财务业绩和财务状况表位置文本块",
    
    # 财产、厂房和设备
    "PropertyPlantAndEquipmentDisclosureTextBlock": "财产、厂房和设备披露文本块",
    "PropertyPlantAndEquipmentTextBlock": "财产、厂房和设备文本块",
    "Depreciation": "折旧",
    "AdditionalFinancialInformationDisclosureTextBlock": "额外财务信息披露文本块",
    
    # 资产和负债
    "ScheduleOfOtherAssetsNoncurrentTextBlock": "其他非流动资产表文本块",
    "OtherCurrentLiabilitiesTableTextBlock": "其他流动负债表文本块",
    "OtherNoncurrentLiabilitiesTableTextBlock": "其他非流动负债表文本块",
    
    # 所得税
    "IncomeTaxDisclosureTextBlock": "所得税披露文本块",
    "ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock": "所得税费用/收益组成部分表文本块",
    "CurrentFederalTaxExpenseBenefit": "当期联邦所得税费用/收益",
    "DeferredFederalIncomeTaxExpenseBenefit": "递延联邦所得税费用/收益",
    "FederalIncomeTaxExpenseBenefitContinuingOperations": "持续经营联邦所得税费用/收益",
    "CurrentStateAndLocalTaxExpenseBenefit": "当期州和地方所得税费用/收益",
    "DeferredStateAndLocalIncomeTaxExpenseBenefit": "递延州和地方所得税费用/收益",
    "StateAndLocalIncomeTaxExpenseBenefitContinuingOperations": "持续经营州和地方所得税费用/收益",
    "CurrentForeignTaxExpenseBenefit": "当期外国所得税费用/收益",
    "DeferredForeignIncomeTaxExpenseBenefit": "递延外国所得税费用/收益",
    "ForeignIncomeTaxExpenseBenefitContinuingOperations": "持续经营外国所得税费用/收益",
    "IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign": "持续经营业务税前收入/亏损（国外）",
    "ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock": "有效所得税率调节表文本块",
    "EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate": "按联邦法定所得税率的有效所得税率调节",
    "IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate": "按联邦法定所得税率的所得税费用/收益调节",
    "IncomeTaxReconciliationStateAndLocalIncomeTaxes": "州和地方所得税调节",
    "EffectiveIncomeTaxRateReconciliationImpactOfTheStateAidDecisionAmount": "州援助决定金额的有效所得税率调节影响",
    "IncomeTaxReconciliationForeignIncomeTaxRateDifferential": "外国所得税率差异调节",
    "IncomeTaxReconciliationTaxCreditsResearch": "研发税收抵免调节",
    "EffectiveIncomeTaxRateReconciliationShareBasedCompensationExcessTaxBenefitAmount": "股份支付超额税收收益金额的有效所得税率调节",
    "IncomeTaxReconciliationOtherAdjustments": "其他调整",
    "EffectiveIncomeTaxRateContinuingOperations": "持续经营有效所得税率",
    "ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock": "递延所得税资产和负债表文本块",
    "ScheduleOfUnrecognizedTaxBenefitsRollForwardTableTextBlock": "未确认所得税收益滚动表文本块",
    "UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions": "前期税务立场导致的未确认所得税收益增加",
    "UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions": "前期税务立场导致的未确认所得税收益减少",
    "UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions": "本期税务立场导致的未确认所得税收益增加",
    "UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities": "与税务机关结算导致的未确认所得税收益减少",
    "UnrecognizedTaxBenefitsReductionsResultingFromLapseOfApplicableStatuteOfLimitations": "适用诉讼时效届满导致的未确认所得税收益减少",
    
    # 租赁
    "LesseeOperatingLeasesTextBlock": "承租人经营租赁文本块",
    "LesseeFinanceLeasesTextBlock": "承租人融资租赁文本块",
    "LesseeOperatingandFinanceLeaseTermofContract": "承租人经营和融资租赁合同期限",
    "OperatingLeaseCost": "经营租赁费用",
    "VariableLeaseCost": "可变租赁费用",
    "OperatingLeasePayments": "经营租赁付款",
    "RightofUseAssetsObtainedinExchangeforOperatingandFinanceLeaseLiabilities": "为交换经营和融资租赁负债而获得的使用权资产",
    "OperatingandFinanceLeaseRightofUseAssetsandLeaseLiabilitiesTableTextBlock": "经营和融资租赁使用权资产和租赁负债表文本块",
    "LesseeOperatingLeaseLiabilityMaturityTableTextBlock": "承租人经营租赁负债到期表文本块",
    "FinanceLeaseLiabilityMaturityTableTextBlock": "融资租赁负债到期表文本块",
    "OperatingandFinanceLeaseWeightedAverageRemainingLeaseTerm": "经营和融资租赁剩余期限加权平均",
    
    # 债务
    "DebtDisclosureTextBlock": "债务披露文本块",
    "CommercialPaperCashFlowSummaryTableTextBlock": "商业票据现金流汇总表文本块",
    "ProceedsFromRepaymentsOfShortTermDebtMaturingInThreeMonthsOrLess": "三个月或更短期债务收入/偿还",
    "ProceedsFromShortTermDebtMaturingInMoreThanThreeMonths": "超过三个月到期的短期债务收入",
    "RepaymentsOfShortTermDebtMaturingInMoreThanThreeMonths": "超过三个月到期的短期债务偿还",
    "ProceedsFromRepaymentsOfShortTermDebtMaturingInMoreThanThreeMonths": "超过三个月到期的短期债务收入/偿还",
    "ScheduleOfDebtInstrumentsTextBlock": "债务工具表文本块",
    "ScheduleOfMaturitiesOfLongTermDebtTableTextBlock": "长期债务到期表文本块",
    
    # 股东权益
    "StockholdersEquityNoteDisclosureTextBlock": "股东权益说明披露文本块",
    "StockRepurchasedAndRetiredDuringPeriodShares": "期间回购并注销的股份数量",
    "StockRepurchasedAndRetiredDuringPeriodValue": "期间回购并注销的股份价值",
    "ScheduleOfCommonStockOutstandingRollForwardTableTextBlock": "流通普通股滚动表文本块",
    
    # 股份支付
    "DisclosureOfCompensationRelatedCostsShareBasedPaymentsTextBlock": "薪酬相关成本股份支付披露文本块",
    "ScheduleOfNonvestedRestrictedStockUnitsActivityTableTextBlock": "未归属限制性股票单位活动表文本块",
    "ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock": "员工服务股份支付已确认期间费用分配表文本块",
    "AllocatedShareBasedCompensationExpense": "分配的股份支付费用",
    "EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense": "员工服务股份支付费用的税收收益",
    
    # 承诺和或有事项
    "CommitmentsAndContingenciesDisclosureTextBlock": "承诺和或有事项披露文本块",
    "UnrecordedUnconditionalPurchaseObligationsDisclosureTextBlock": "未记录无条件购买义务披露文本块",
    
    # 分部报告
    "SegmentReportingDisclosureTextBlock": "分部报告披露文本块",
    "SegmentReportingPolicyPolicyTextBlock": "分部报告政策文本块",
    "ScheduleOfSegmentReportingInformationBySegmentTextBlock": "分部报告信息表文本块",
    "ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTextBlock": "分部营业利润/亏损与合并报表调节文本块",
    "ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsByGeographicalAreasTableTextBlock": "按地理区域划分的外部客户收入和长期资产表文本块",
    
    # 审计信息
    "AuditorName": "审计师名称",
    "AuditorLocation": "审计师所在地",
    "InsiderTrdPoliciesProcAdoptedFlag": "内幕交易政策程序采纳标志",
    "AuditorFirmId": "审计师事务所ID"
}