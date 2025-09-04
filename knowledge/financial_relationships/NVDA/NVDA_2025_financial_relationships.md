# NVDA 2025 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.nvidia.com/role/ConsolidatedStatementsofIncome

- us-gaap_IncomeStatementAbstract
  - us-gaap_Revenues
  - us-gaap_CostOfRevenue
  - us-gaap_GrossProfit [totalLabel]
  - us-gaap_OperatingExpensesAbstract
    - us-gaap_ResearchAndDevelopmentExpense
    - us-gaap_SellingGeneralAndAdministrativeExpense
    - nvda_BusinessCombinationAdvancedConsiderationWrittenOff
    - us-gaap_OperatingExpenses [totalLabel]
  - us-gaap_OperatingIncomeLoss [totalLabel]
  - us-gaap_InvestmentIncomeInterest
  - us-gaap_InterestExpenseNonoperating
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_NonoperatingIncomeExpense [totalLabel]
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]
  - us-gaap_IncomeTaxExpenseBenefit
  - us-gaap_NetIncomeLoss [totalLabel]
  - us-gaap_EarningsPerShareAbstract
    - us-gaap_EarningsPerShareBasic
    - us-gaap_EarningsPerShareDiluted
  - us-gaap_WeightedAverageNumberOfSharesOutstandingDilutedDisclosureItemsAbstract
    - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
    - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding

### http://www.nvidia.com/role/ConsolidatedStatementsofComprehensiveIncome

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
    - us-gaap_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesAdjustmentBeforeReclassificationAdjustmentsNetOfTaxAbstract
      - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesNetOfTax
      - us-gaap_OtherComprehensiveIncomeAvailableforsaleSecuritiesAdjustmentNetOfTaxPortionAttributableToParent [totalLabel]
  - us-gaap_OtherComprehensiveIncomeDerivativesQualifyingAsHedgesTaxPortionAttributableToParentAbstract
    - us-gaap_OtherComprehensiveIncomeLossCashFlowHedgeGainLossBeforeReclassificationAfterTax
    - us-gaap_OtherComprehensiveIncomeLossCashFlowHedgeGainLossReclassificationAfterTax
    - us-gaap_OtherComprehensiveIncomeLossCashFlowHedgeGainLossAfterReclassificationAndTax [totalLabel]
  - us-gaap_OtherComprehensiveIncomeLossNetOfTax [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.nvidia.com/role/ConsolidatedStatementsofCashFlows

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_ShareBasedCompensation
  - us-gaap_DepreciationDepletionAndAmortization
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_GainLossOnInvestments
  - nvda_BusinessCombinationAdvancedConsiderationWrittenOff
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.nvidia.com/role/NetIncomePerShare

- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareTextBlock

### http://www.nvidia.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.nvidia.com/role/NetIncomePerShareTables

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfWeightedAverageNumberOfSharesTableTextBlock

### http://www.nvidia.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfUnrecognizedTaxBenefitsRollForwardTableTextBlock

### http://www.nvidia.com/role/StockBasedCompensationScheduleofStockBasedCompensationExpenseDetails

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember
    - us-gaap_SellingGeneralAndAdministrativeExpensesMember

### http://www.nvidia.com/role/StockBasedCompensationSummaryofEquityAwardsDetails

- nvda_SummaryofunearnedSBCexpenseAbstract
  - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
  - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]

### http://www.nvidia.com/role/NetIncomePerShareDetails

- us-gaap_EarningsPerShareAbstract
  - nvda_NumeratorAbstract
    - us-gaap_NetIncomeLoss
  - nvda_DenominatorAbstract
    - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
    - us-gaap_WeightedAverageNumberDilutedSharesOutstandingAdjustment
    - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding [totalLabel]
  - nvda_NetIncomeLossPerShareAbstract
    - us-gaap_EarningsPerShareBasic
    - us-gaap_EarningsPerShareDiluted
  - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount

### http://www.nvidia.com/role/AmortizableIntangibleAssetsDetails

- us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.nvidia.com/role/BalanceSheetComponentsAccruedandOtherCurrentLiabilitiesDetails

- us-gaap_NatureOfExpenseAxis
  - us-gaap_InterimPeriodCostsNotAllocableDomain

### http://www.nvidia.com/role/BalanceSheetComponentsDeferredRevenueDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_MovementInDeferredRevenueRollForward
    - us-gaap_ContractWithCustomerLiability
    - nvda_ContractWithCustomerLiabilityAdditions
    - nvda_ContractWithCustomerLiabilityRevenueRecognizedOpeningBalanceAndCurrentPeriodAdditions
    - us-gaap_ContractWithCustomerLiability

### http://www.nvidia.com/role/BalanceSheetComponentsRevenueRemainingPerformanceObligationDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionTable
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionLineItems
      - us-gaap_ContractWithCustomerLiabilityRevenueRecognized
      - us-gaap_RevenueRemainingPerformanceObligation
      - nvda_RevenueRemainingPerformanceObligationContractWithCustomerLiabilityAmount
      - us-gaap_UnbilledContractsReceivable
      - us-gaap_RevenueRemainingPerformanceObligationPercentage
      - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionPeriod1

### http://www.nvidia.com/role/IncomeTaxesComponentsofIncomeTaxExpenseDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_CurrentIncomeTaxExpenseBenefitContinuingOperationsAbstract
    - us-gaap_CurrentFederalTaxExpenseBenefit
    - us-gaap_CurrentStateAndLocalTaxExpenseBenefit
    - us-gaap_CurrentForeignTaxExpenseBenefit
    - us-gaap_CurrentIncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_DeferredIncomeTaxExpenseBenefitContinuingOperationsAbstract
    - us-gaap_DeferredFederalIncomeTaxExpenseBenefit
    - us-gaap_DeferredStateAndLocalIncomeTaxExpenseBenefit
    - us-gaap_DeferredForeignIncomeTaxExpenseBenefit
    - us-gaap_DeferredIncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestmentsAbstract
    - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
    - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
    - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]

### http://www.nvidia.com/role/IncomeTaxesIncomeTaxReconciliationDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxExpenseBenefitContinuingOperationsIncomeTaxReconciliationAbstract
    - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
    - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
    - us-gaap_EffectiveIncomeTaxRateReconciliationFdiiAmount
    - us-gaap_IncomeTaxReconciliationNondeductibleExpenseShareBasedCompensationCost
    - us-gaap_IncomeTaxReconciliationTaxCreditsResearch
    - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
    - nvda_EffectiveIncomeTaxRateReconciliationAcquisitionTerminationCost
    - us-gaap_IncomeTaxReconciliationOtherAdjustments
    - us-gaap_IncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_EffectiveIncomeTaxRateContinuingOperationsTaxRateReconciliationAbstract
    - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
    - us-gaap_EffectiveIncomeTaxRateReconciliationStateAndLocalIncomeTaxes
    - us-gaap_EffectiveIncomeTaxRateReconciliationFdiiPercent
    - us-gaap_EffectiveIncomeTaxRateReconciliationNondeductibleExpenseShareBasedCompensationCost
    - us-gaap_EffectiveIncomeTaxRateReconciliationTaxCreditsResearch
    - us-gaap_EffectiveIncomeTaxRateReconciliationForeignIncomeTaxRateDifferential
    - nvda_EffectiveIncomeTaxRateReconciliationAcquisitionTerminationCostPercent
    - us-gaap_EffectiveIncomeTaxRateReconciliationOtherAdjustments
    - us-gaap_EffectiveIncomeTaxRateContinuingOperations [totalLabel]

### http://www.nvidia.com/role/IncomeTaxesDeferredTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxContingencyTable
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_IncomeTaxContingencyLineItems
      - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
      - us-gaap_ComponentsOfDeferredTaxLiabilitiesAbstract
      - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]

### http://www.nvidia.com/role/IncomeTaxesNarrativeDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxContingencyTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_TaxCreditCarryforwardAxis
      - us-gaap_TaxCreditCarryforwardNameDomain
    - us-gaap_IncomeTaxContingencyLineItems
      - us-gaap_DeferredTaxAssetsGross
      - us-gaap_DeferredIncomeTaxLiabilities
      - us-gaap_UndistributedEarningsOfForeignSubsidiaries
      - us-gaap_TaxCreditCarryforwardValuationAllowance
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsResearch
      - us-gaap_TaxCreditCarryforwardAmount
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestExpense
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued

### http://www.nvidia.com/role/IncomeTaxesUnrecognizedTaxBenefitsDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ReconciliationOfUnrecognizedTaxBenefitsExcludingAmountsPertainingToExaminedTaxReturnsRollForward
    - us-gaap_UnrecognizedTaxBenefits
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsReductionsResultingFromLapseOfApplicableStatuteOfLimitations
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
    - us-gaap_UnrecognizedTaxBenefits
  - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate

### http://www.nvidia.com/role/SegmentInformationRevenueandLonglivedAssetsbyRegionDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
      - us-gaap_Revenues
      - us-gaap_NoncurrentAssets

### http://www.nvidia.com/role/SegmentInformationRevenueandAccountsReceivablebyMajorCustomerDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfEntityWideRevenueByMajorCustomersByReportingSegmentsTable
    - srt_MajorCustomersAxis
      - srt_NameOfMajorCustomerDomain
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_ConcentrationRiskByTypeAxis
      - us-gaap_ConcentrationRiskTypeDomain
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_EntityWideRevenueMajorCustomerLineItems
      - us-gaap_ConcentrationRiskPercentage1

### http://www.nvidia.com/role/SegmentInformationScheduleofRevenuebyMarketDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_EntityWideInformationRevenueFromExternalCustomerLineItems
      - us-gaap_Revenues

## 资产负债表结构 (Balance Sheet Structure)

### http://www.nvidia.com/role/ConsolidatedBalanceSheets

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_AssetsAbstract
    - us-gaap_AssetsCurrentAbstract
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_MarketableSecuritiesCurrent
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_InventoryNet
      - us-gaap_PrepaidExpenseAndOtherAssetsCurrent
      - us-gaap_AssetsCurrent [totalLabel]
    - us-gaap_PropertyPlantAndEquipmentNet
    - us-gaap_OperatingLeaseRightOfUseAsset
    - us-gaap_Goodwill
    - us-gaap_IntangibleAssetsNetExcludingGoodwill
    - us-gaap_DeferredIncomeTaxAssetsNet
    - us-gaap_OtherAssetsNoncurrent
    - us-gaap_Assets [totalLabel]
  - us-gaap_LiabilitiesAndStockholdersEquityAbstract
    - us-gaap_LiabilitiesCurrentAbstract
      - us-gaap_AccountsPayableCurrent
      - us-gaap_AccruedLiabilitiesCurrent
      - us-gaap_DebtCurrent
      - us-gaap_LiabilitiesCurrent [totalLabel]
    - us-gaap_LongTermDebtNoncurrent
    - us-gaap_OperatingLeaseLiabilityNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent
    - us-gaap_Liabilities [totalLabel]
    - us-gaap_CommitmentsAndContingencies
    - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterestAbstract
      - us-gaap_PreferredStockValueOutstanding
      - us-gaap_CommonStockValue
      - us-gaap_AdditionalPaidInCapital
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
      - us-gaap_RetainedEarningsAccumulatedDeficit
      - us-gaap_StockholdersEquity [totalLabel]
    - us-gaap_LiabilitiesAndStockholdersEquity [totalLabel]

### http://www.nvidia.com/role/ConsolidatedBalanceSheetsParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_PreferredStockParOrStatedValuePerShare
  - us-gaap_PreferredStockSharesAuthorized
  - us-gaap_PreferredStockSharesIssued
  - us-gaap_CommonStockParOrStatedValuePerShare
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_CommonStockSharesIssued
  - us-gaap_CommonStockSharesOutstanding

### http://www.nvidia.com/role/ConsolidatedStatementsofShareholdersEquity

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTax
  - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockOwnershipPlan
  - us-gaap_StockIssuedDuringPeriodValueEmployeeStockOwnershipPlan
  - us-gaap_SharesPaidForTaxWithholdingForShareBasedCompensation
  - us-gaap_AdjustmentsRelatedToTaxWithholdingForShareBasedCompensation
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
  - us-gaap_DividendsCommonStockCash
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember
    - us-gaap_AdditionalPaidInCapitalMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
    - us-gaap_RetainedEarningsMember

### http://www.nvidia.com/role/ConsolidatedStatementsofShareholdersEquityParenthetical

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_CommonStockDividendsPerShareDeclared

### http://www.nvidia.com/role/ConsolidatedStatementsofCashFlows

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetIncomeLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities
    - us-gaap_ProceedsFromSaleOfAvailableForSaleSecuritiesDebt
    - us-gaap_ProceedsFromSaleOfEquitySecuritiesFvNi
    - us-gaap_PaymentsToAcquireAvailableForSaleSecuritiesDebt
    - us-gaap_PaymentsToAcquireProductiveAssets
    - us-gaap_PaymentsToAcquireEquitySecuritiesFvNi
    - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
    - us-gaap_PaymentsForProceedsFromOtherInvestingActivities
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_ProceedsFromStockPlans
    - us-gaap_PaymentsForRepurchaseOfCommonStock
    - us-gaap_PaymentsRelatedToTaxWithholdingForShareBasedCompensation
    - us-gaap_RepaymentsOfDebt
    - us-gaap_PaymentsOfDividends
    - nvda_PaymentsForFinancedPropertyPlantAndEquipmentAndIntangibleAssetsFinancingActivities
    - us-gaap_ProceedsFromPaymentsForOtherFinancingActivities
    - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect [totalLabel]
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
  - us-gaap_SupplementalCashFlowInformationAbstract
    - us-gaap_IncomeTaxesPaidNet
    - us-gaap_InterestPaidNet

### http://www.nvidia.com/role/BusinessCombination

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_BusinessCombinationDisclosureTextBlock

### http://www.nvidia.com/role/Goodwill

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillDisclosureTextBlock

### http://www.nvidia.com/role/AmortizableIntangibleAssets

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_IntangibleAssetsDisclosureTextBlock

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecurities

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_InvestmentsInDebtAndMarketableEquitySecuritiesAndCertainTradingAssetsDisclosureTextBlock

### http://www.nvidia.com/role/FairValueofFinancialAssetsandLiabilitiesandNonmarketableEquitySecurities

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueDisclosuresTextBlock

### http://www.nvidia.com/role/BalanceSheetComponents

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_SupplementalBalanceSheetDisclosuresTextBlock

### http://www.nvidia.com/role/ShareholdersEquity

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.nvidia.com/role/AmortizableIntangibleAssetsTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTableTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesTables

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_DebtSecuritiesAvailableForSaleTableTextBlock
  - us-gaap_GainLossOnInvestmentsTextBlock

### http://www.nvidia.com/role/FairValueofFinancialAssetsandLiabilitiesandNonmarketableEquitySecuritiesTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTableTextBlock
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueTableTextBlock

### http://www.nvidia.com/role/BalanceSheetComponentsTables

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_ScheduleOfInventoryCurrentTableTextBlock
  - us-gaap_PropertyPlantAndEquipmentTextBlock
  - us-gaap_ScheduleOfOtherAssetsNoncurrentTextBlock
  - us-gaap_ScheduleOfAccountsPayableAndAccruedLiabilitiesTableTextBlock
  - us-gaap_OtherNoncurrentLiabilitiesTableTextBlock
  - us-gaap_ContractWithCustomerAssetAndLiabilityTableTextBlock

### http://www.nvidia.com/role/BusinessCombinationDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable

### http://www.nvidia.com/role/StockBasedCompensationEquityIncentivePlansDetails

- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNonOptionEquityInstrumentsOutstandingRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNonOptionEquityInstrumentsOutstandingNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNonOptionEquityInstrumentsOutstandingNumber

### http://www.nvidia.com/role/GoodwillDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTable

### http://www.nvidia.com/role/AmortizableIntangibleAssetsDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]
      - us-gaap_AmortizationOfIntangibleAssets
      - us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesCashEquivalentsandMarketableSecuritiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_DebtSecuritiesAvailableForSaleTable

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesUnrealizedLossesAggregatedbyInvestmentCategoryDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_DebtSecuritiesAvailableForSaleTable

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesAmortizedCostandEstimatedFairValueofCashEquivalentsandMarketableSecuritiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAmortizedCostBasisRollingMaturityAbstract
  - us-gaap_FairValueDisclosuresAbstract

### http://www.nvidia.com/role/FairValueofFinancialAssetsandLiabilitiesandNonmarketableEquitySecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueByAssetClassAxis
      - us-gaap_FairValueAssetsMeasuredOnRecurringBasisUnobservableInputReconciliationByAssetClassDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_AssetsFairValueDisclosureAbstract
      - us-gaap_LiabilitiesFairValueDisclosureAbstract

### http://www.nvidia.com/role/FairValueofFinancialAssetsandLiabilitiesandNonmarketableEquitySecuritiesCarryingValueofNonmarketableEquitySecuritiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueAmount
  - nvda_EquitySecuritiesWithoutReadilyDeterminableFairValueNetAdditionsDisposals
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentAnnualAmount
  - nvda_EquitySecuritiesWithoutReadilyDeterminableFairValueImpairmentLossAndDownwardPriceAdjustmentAnnualAmount
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueAmount

### http://www.nvidia.com/role/FairValueofFinancialAssetsandLiabilitiesandNonmarketableEquitySecuritiesCumulativeGrossDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_OtherInvestmentNotReadilyMarketableTable
    - us-gaap_OtherInvestmentNotReadilyMarketableAxis
      - us-gaap_OtherInvestmentNotReadilyMarketableNameDomain
    - us-gaap_OtherInvestmentNotReadilyMarketableLineItems
      - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentCumulativeAmount
      - nvda_EquitySecuritiesWithoutReadilyDeterminableFairValueImpairmentLossAndDownwardPriceAdjustmentCumulativeAmount
      - us-gaap_UnrealizedGainLossOnInvestments

### http://www.nvidia.com/role/BalanceSheetComponentsNarrativeDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - srt_MajorCustomersAxis
      - srt_NameOfMajorCustomerDomain
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - us-gaap_ConcentrationRiskByTypeAxis
      - us-gaap_ConcentrationRiskTypeDomain
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_ConcentrationRiskPercentage1
      - us-gaap_Depreciation
      - us-gaap_FinanceLeaseRightOfUseAssetAccumulatedAmortization
      - us-gaap_CapitalExpendituresIncurredButNotYetPaid

### http://www.nvidia.com/role/BalanceSheetComponentsInventoriesDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_InventoryNetAbstract
    - us-gaap_InventoryRawMaterialsNetOfReserves
    - us-gaap_InventoryWorkInProcessNetOfReserves
    - us-gaap_InventoryFinishedGoodsNetOfReserves
    - us-gaap_InventoryNet [totalLabel]
    - us-gaap_InventoryWriteDown

### http://www.nvidia.com/role/BalanceSheetComponentsPropertyandEquipmentDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]
      - us-gaap_PropertyPlantAndEquipmentUsefulLife

### http://www.nvidia.com/role/BalanceSheetComponentsOtherAssetsDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_SupplyCommitmentTable
    - us-gaap_SupplyCommitmentAxis
      - us-gaap_SupplyCommitmentArrangementMember
    - us-gaap_SupplyCommitmentLineItems
      - us-gaap_EquitySecuritiesFVNINoncurrent
      - nvda_PrepaidSupplyAndCapacityAgreementsNoncurrent
      - us-gaap_IncomeTaxesReceivableNoncurrent
      - nvda_PrepaidRoyaltiesNoncurrent
      - us-gaap_OtherAssetsMiscellaneousNoncurrent
      - us-gaap_OtherAssetsNoncurrent [totalLabel]
      - us-gaap_PrepaidExpenseAndOtherAssetsCurrent

### http://www.nvidia.com/role/BalanceSheetComponentsAccruedandOtherCurrentLiabilitiesDetails

- us-gaap_InterimPeriodCostsNotAllocableDomain
  - nvda_InventoryPurchaseObligationsInExcessOfProjectionsMember
  - nvda_NatureOfExpenseCustomerAdvancesAndDeferralsMember
- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - nvda_AccrualsTable
    - us-gaap_NatureOfExpenseAxis
    - nvda_AccrualsLineItems
      - nvda_AccruedCustomerProgramsCurrent
      - nvda_ExcessInventoryPurchaseObligationsCurrent
      - nvda_ProductWarrantyAccrualsAndReturnProvisionsCurrent
      - us-gaap_TaxesPayableCurrent
      - us-gaap_EmployeeRelatedLiabilitiesCurrent
      - us-gaap_ContractWithCustomerLiabilityCurrent
      - us-gaap_OperatingLeaseLiabilityCurrent
      - nvda_AccruedLicensesAndRoyalties
      - nvda_AccruedShareRepurchaseLiabilityCurrent
      - us-gaap_OtherAccruedLiabilitiesCurrent
      - us-gaap_AccruedLiabilitiesCurrent [totalLabel]
      - us-gaap_OperatingLeaseLiabilityCurrentStatementOfFinancialPositionExtensibleList
      - us-gaap_CostOfRevenue

### http://www.nvidia.com/role/BalanceSheetComponentsOtherLongTermLiabilitiesDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_OtherLiabilitiesNoncurrentAbstract
    - us-gaap_AccruedIncomeTaxesNoncurrent
    - us-gaap_ContractWithCustomerLiabilityNoncurrent
    - us-gaap_DeferredIncomeTaxLiabilitiesNet
    - nvda_LicensesPayableNoncurrent
    - us-gaap_OtherSundryLiabilitiesNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]
  - nvda_ContractWithCustomerLiabilityAdditionsCustomerAdvances
  - nvda_ContractWithCustomerLiabilityRevenueRecognizedFromCustomerAdvances

### http://www.nvidia.com/role/ShareholdersEquityDetails

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_AdditionalPaidInCapitalMember
    - us-gaap_RetainedEarningsMember
- us-gaap_EquityClassOfTreasuryStockLineItems
  - nvda_StockRepurchaseProgramAdditionalNumberOfSharesAuthorizedForRepurchase
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
  - srt_StockRepurchaseProgramAuthorizedAmount1
  - us-gaap_PaymentsOfDividends
- us-gaap_EquityAbstract
  - us-gaap_ClassOfTreasuryStockTable

## 现金流量表结构 (Cash Flow Structure)

### http://www.nvidia.com/role/ConsolidatedStatementsofCashFlows

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInInventories
  - us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities
  - us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesCashEquivalentsandMarketableSecuritiesDetails

- us-gaap_DebtSecuritiesAvailableForSaleTable
  - us-gaap_FinancialInstrumentAxis
    - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
      - us-gaap_CorporateDebtSecuritiesMember
      - us-gaap_USTreasurySecuritiesMember
      - us-gaap_MoneyMarketFundsMember
      - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
      - us-gaap_ForeignGovernmentDebtSecuritiesMember
      - us-gaap_CertificatesOfDepositMember
      - nvda_MarketableSecuritiesWithFairValueAdjustmentsRecordedInOtherComprehensiveIncomeMember
      - nvda_PubliclyHeldEquitySecuritiesMember
  - us-gaap_FairValueByFairValueHierarchyLevelAxis
    - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
      - us-gaap_FairValueInputsLevel1Member
  - us-gaap_ScheduleOfAvailableForSaleSecuritiesLineItems
    - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis [totalLabel]
    - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
    - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
    - us-gaap_AvailableForSaleSecuritiesDebtSecurities [totalLabel]
    - us-gaap_CashEquivalentsAtCarryingValue
    - us-gaap_MarketableSecurities
    - us-gaap_EquitySecuritiesFvNiCurrentAndNoncurrent
    - nvda_DebtSecuritiesAvailableForSaleAndEquitySecuritiesFVNI [totalLabel]
    - nvda_MarketableSecuritiesAndEquitySecuritiesFVNI [totalLabel]
    - us-gaap_EquitySecuritiesFvNiUnrealizedGainLoss
    - us-gaap_EquitySecuritiesFvNiRealizedGainLoss

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesUnrealizedLossesAggregatedbyInvestmentCategoryDetails

- us-gaap_DebtSecuritiesAvailableForSaleTable
  - us-gaap_FinancialInstrumentAxis
    - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
      - us-gaap_USTreasurySecuritiesMember
      - us-gaap_CorporateDebtSecuritiesMember
      - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
  - us-gaap_ScheduleOfAvailableForSaleSecuritiesLineItems
    - us-gaap_DebtSecuritiesAvailableforSaleUnrealizedLossPositionAbstract
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPositionLessThan12Months
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPosition12MonthsOrLonger
      - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPosition [totalLabel]
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionAccumulatedLossAbstract
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPositionLessThan12MonthsAccumulatedLoss
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPosition12MonthsOrLongerAccumulatedLoss
      - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPositionAccumulatedLoss

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesAmortizedCostandEstimatedFairValueofCashEquivalentsandMarketableSecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtSecurities [totalLabel]
- us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAmortizedCostBasisRollingMaturityAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearAmortizedCost
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsAmortizedCost
  - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis [totalLabel]

## 股东权益结构 (Equity Structure)

### http://www.nvidia.com/role/ConsolidatedStatementsofShareholdersEquity

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward

### http://www.nvidia.com/role/StockBasedCompensation

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_DisclosureOfCompensationRelatedCostsShareBasedPaymentsTextBlock

### http://www.nvidia.com/role/StockBasedCompensationTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock
  - us-gaap_DisclosureOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTextBlock
  - us-gaap_ScheduleOfShareBasedPaymentAwardStockOptionsValuationAssumptionsTableTextBlock
  - us-gaap_ScheduleOfShareBasedCompensationActivityTableTextBlock

### http://www.nvidia.com/role/StockBasedCompensationScheduleofStockBasedCompensationExpenseDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
      - us-gaap_AllocatedShareBasedCompensationExpense

### http://www.nvidia.com/role/StockBasedCompensationSummaryofEquityAwardsDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
      - nvda_ShareBasedCompensationArrangementByShareBasedPaymentAwardGrantsInPeriodGrantDateTotalFairValue [totalLabel]
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardPerShareWeightedAveragePriceOfSharesPurchased
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - nvda_SummaryofunearnedSBCexpenseAbstract
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsAndMethodologyAbstract

### http://www.nvidia.com/role/StockBasedCompensationNarrativeDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - srt_StatementScenarioAxis
      - srt_ScenarioUnspecifiedDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
      - nvda_NumberOfSharesMayBeIssuedUnderRestated2007Plan
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardMaximumEmployeeSubscriptionRate
      - nvda_EmployeeStockPurchasePlanOfferingPeriodDuration
      - nvda_EmployeeStockPurchasePlanNumberOfPurchasePeriodsInOfferingPeriod
      - nvda_EmployeeStockPurchasePlanPurchasePeriodDuration
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardPurchasePriceOfCommonStockPercent
      - us-gaap_CommonStockCapitalSharesReservedForFutureIssuance
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]

### http://www.nvidia.com/role/StockBasedCompensationEquityIncentivePlansDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNonOptionEquityInstrumentsOutstandingRollForward
  - nvda_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedAndExpectedToVest
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
  - nvda_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedAndExpectedToVestOutstandingWeightedAverageExercisePrice

### http://www.nvidia.com/role/ShareholdersEquityDetails

- us-gaap_ClassOfTreasuryStockTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_SubsequentEventTypeAxis
    - us-gaap_SubsequentEventTypeDomain
      - us-gaap_SubsequentEventMember
  - us-gaap_EquityClassOfTreasuryStockLineItems

### http://xbrl.sec.gov/ecd/role/AwardTimingDisclosure

- us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
  - us-gaap_EmployeeStockOptionMember
  - us-gaap_StockAppreciationRightsSARSMember

## 其他结构 (Other Structure)

### http://www.nvidia.com/role/CoverPage

- dei_CoverAbstract
  - dei_DocumentType
  - dei_DocumentAnnualReport
  - dei_DocumentPeriodEndDate
  - dei_CurrentFiscalYearEndDate
  - dei_DocumentTransitionReport
  - dei_EntityFileNumber
  - dei_EntityRegistrantName
  - dei_EntityIncorporationStateCountryCode
  - dei_EntityTaxIdentificationNumber
  - dei_EntityAddressAddressLine1
  - dei_EntityAddressCityOrTown
  - dei_EntityAddressStateOrProvince
  - dei_EntityAddressPostalZipCode
  - dei_CityAreaCode
  - dei_LocalPhoneNumber
  - dei_Security12bTitle
  - dei_TradingSymbol
  - dei_SecurityExchangeName
  - dei_EntityWellKnownSeasonedIssuer
  - dei_EntityVoluntaryFilers
  - dei_EntityCurrentReportingStatus
  - dei_EntityInteractiveDataCurrent
  - dei_EntityFilerCategory
  - dei_EntitySmallBusiness
  - dei_EntityEmergingGrowthCompany
  - dei_IcfrAuditorAttestationFlag
  - dei_DocumentFinStmtErrorCorrectionFlag
  - dei_EntityShellCompany
  - dei_EntityPublicFloat
  - dei_EntityCommonStockSharesOutstanding
  - dei_DocumentsIncorporatedByReferenceTextBlock
  - dei_EntityCentralIndexKey
  - dei_DocumentFiscalYearFocus
  - dei_DocumentFiscalPeriodFocus
  - dei_AmendmentFlag

### http://www.nvidia.com/role/AuditInformation

- nvda_AuditInformationAbstract
  - dei_AuditorFirmId
  - dei_AuditorName
  - dei_AuditorLocation

### http://www.nvidia.com/role/OrganizationandSummaryofSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_SignificantAccountingPoliciesTextBlock

### http://www.nvidia.com/role/DerivativeFinancialInstruments

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureTextBlock

### http://www.nvidia.com/role/Debt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.nvidia.com/role/CommitmentsandContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.nvidia.com/role/EmployeeRetirementPlans

- us-gaap_CompensationAndRetirementDisclosureAbstract
  - us-gaap_PensionAndOtherPostretirementBenefitsDisclosureTextBlock

### http://www.nvidia.com/role/SegmentInformation

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.nvidia.com/role/Leases

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeasesTextBlock

### http://www.nvidia.com/role/ScheduleIIValuationandQualifyingAccounts

- srt_ValuationAndQualifyingAccountsAbstract
  - srt_ScheduleOfValuationAndQualifyingAccountsDisclosureTextBlock

### http://www.nvidia.com/role/OrganizationandSummaryofSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - nvda_NatureOfOperationsPolicyTextBlock
  - us-gaap_FiscalPeriod
  - us-gaap_ConsolidationPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_RevenueFromContractWithCustomerPolicyTextBlock
  - us-gaap_CommitmentsAndContingenciesPolicyTextBlock
  - us-gaap_CompensationRelatedCostsPolicyTextBlock
  - us-gaap_LegalCostsPolicyTextBlock
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_EarningsPerSharePolicyTextBlock
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_MarketableSecuritiesPolicy
  - us-gaap_InvestmentPolicyTextBlock
  - us-gaap_ConcentrationRiskCreditRisk
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_LesseeLeasesPolicyTextBlock
  - us-gaap_GoodwillAndIntangibleAssetsPolicyTextBlock
  - us-gaap_IntangibleAssetsFiniteLivedPolicy
  - us-gaap_BusinessCombinationsPolicy
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValuePolicyTextBlock
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock

### http://www.nvidia.com/role/DerivativeFinancialInstrumentsTables

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_ScheduleOfNotionalAmountsOfOutstandingDerivativePositionsTableTextBlock

### http://www.nvidia.com/role/DebtTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtInstrumentsTextBlock

### http://www.nvidia.com/role/CommitmentsandContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - srt_ContractualObligationFiscalYearMaturityScheduleTableTextBlock
  - us-gaap_ScheduleOfProductWarrantyLiabilityTableTextBlock

### http://www.nvidia.com/role/SegmentInformationTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsByGeographicalAreasTableTextBlock
  - us-gaap_ScheduleOfRevenueByMajorCustomersByReportingSegmentsTableTextBlock
  - us-gaap_LongLivedAssetsByGeographicAreasTableTextBlock

### http://www.nvidia.com/role/LeasesTables

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeaseLiabilityMaturityTableTextBlock
  - nvda_LesseeOperatingLeasesOtherInformationRelatedToLeasesTableTextBlock

### http://www.nvidia.com/role/OrganizationandSummaryofSignificantAccountingPoliciesDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_TaxCreditCarryforwardAxis
      - us-gaap_TaxCreditCarryforwardNameDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_CostOfRevenue
      - us-gaap_OperatingExpenses
      - us-gaap_NetIncomeLoss
      - us-gaap_EarningsPerShareBasic
      - us-gaap_EarningsPerShareDiluted
      - us-gaap_OperatingIncomeLoss
      - nvda_WarrantyLiabilityTermOfWarranties
      - us-gaap_TaxCreditCarryforwardValuationAllowance
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife

### http://www.nvidia.com/role/BusinessCombinationDetails

- us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
  - us-gaap_BusinessAcquisitionAxis
    - us-gaap_BusinessAcquisitionAcquireeDomain
      - nvda_ArmLimitedMember
  - us-gaap_BusinessAcquisitionLineItems
    - us-gaap_BusinessCombinationAcquisitionRelatedCosts

### http://www.nvidia.com/role/GoodwillDetails

- us-gaap_ScheduleOfGoodwillTable
  - us-gaap_StatementBusinessSegmentsAxis
    - us-gaap_SegmentDomain
      - nvda_ComputeAndNetworkingSegmentMember
      - nvda_GraphicsSegmentMember
  - us-gaap_GoodwillLineItems
    - us-gaap_Goodwill
    - us-gaap_GoodwillAcquiredDuringPeriod
    - us-gaap_GoodwillImpairmentLoss

### http://www.nvidia.com/role/DerivativeFinancialInstrumentsNotionalValueofOurForeignCurrencyForwardContractsOutstandingDetails

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosuresTable
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosuresLineItems
      - us-gaap_DerivativeNotionalAmount

### http://www.nvidia.com/role/DerivativeFinancialInstrumentsNarrativeDetails

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeTable
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativeLineItems
      - us-gaap_MaximumRemainingMaturityOfForeignCurrencyDerivatives1

### http://www.nvidia.com/role/DebtNarrativeDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_RepaymentsOfDebt
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_CommercialPaper

### http://www.nvidia.com/role/DebtScheduleofDebtDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentTerm
      - us-gaap_DebtInstrumentInterestRateDuringPeriod
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_DebtInstrumentUnamortizedDiscountPremiumAndDebtIssuanceCostsNet
      - us-gaap_LongTermDebt [totalLabel]
      - us-gaap_LongTermDebtCurrent
      - us-gaap_LongTermDebtNoncurrent

### http://www.nvidia.com/role/CommitmentsandContingenciesNarrativeDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_SupplyCommitmentTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_LossContingenciesByNatureOfContingencyAxis
      - us-gaap_LossContingencyNatureDomain
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - us-gaap_SupplyCommitmentLineItems
      - nvda_PurchaseObligationInventoryPurchaseAndSupplyAgreements
      - us-gaap_OtherCommitment
      - us-gaap_ProductWarrantyAccrual
      - nvda_LossContingencyMotionToExtendStayAwardedDuration

### http://www.nvidia.com/role/CommitmentsandContingenciesSummaryofFutureCommitmentsDuebyYearDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_PurchaseObligationFiscalYearMaturityAbstract
    - us-gaap_PurchaseObligationDueInNextTwelveMonths
    - us-gaap_PurchaseObligationDueInSecondYear
    - us-gaap_PurchaseObligationDueInThirdYear
    - us-gaap_PurchaseObligationDueInFourthYear
    - us-gaap_PurchaseObligationDueInFifthYear
    - us-gaap_PurchaseObligationDueAfterFifthYear
    - us-gaap_PurchaseObligation [totalLabel]

### http://www.nvidia.com/role/CommitmentsandContingenciesScheduleofProductWarrantyLiabilitiesDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_MovementInStandardAndExtendedProductWarrantyIncreaseDecreaseRollForward
    - us-gaap_ProductWarrantyAccrual
    - us-gaap_ProductWarrantyAccrualWarrantiesIssued
    - us-gaap_ProductWarrantyAccrualPayments
    - us-gaap_ProductWarrantyAccrual

### http://www.nvidia.com/role/EmployeeRetirementPlansDetails

- us-gaap_CompensationAndRetirementDisclosureAbstract
  - us-gaap_DefinedContributionPlanCostRecognized

### http://www.nvidia.com/role/SegmentInformationNarrativeDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - us-gaap_ConcentrationRiskByTypeAxis
      - us-gaap_ConcentrationRiskTypeDomain
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - srt_MajorCustomersAxis
      - srt_NameOfMajorCustomerDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_NumberOfReportableSegments
      - us-gaap_DepreciationDepletionAndAmortization
      - us-gaap_ConcentrationRiskPercentage1

### http://www.nvidia.com/role/SegmentInformationReportableSegmentsDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - srt_ConsolidationItemsAxis
      - srt_ConsolidationItemsDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_Revenues
      - us-gaap_SegmentReportingOtherItemAmount
      - us-gaap_OperatingIncomeLoss

### http://www.nvidia.com/role/SegmentInformationReconcilingItemsDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - srt_ConsolidationItemsAxis
      - srt_ConsolidationItemsDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_ShareBasedCompensation
      - nvda_UnallocatedCorporateOperatingExpendituresAndOtherExpenses
      - nvda_AcquisitionRelatedAndOtherCosts
      - nvda_AcquisitionTerminationCost
      - us-gaap_OtherOperatingIncome
      - us-gaap_OperatingIncomeLoss [totalLabel]

### http://www.nvidia.com/role/LeasesScheduleofFutureMinimumLeasePaymentsDetails

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueNextTwelveMonths
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearTwo
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearThree
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearFour
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearFive
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueAfterYearFive
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDue [totalLabel]
  - us-gaap_LesseeOperatingLeaseLiabilityUndiscountedExcessAmount
  - us-gaap_OperatingLeaseLiability [totalLabel]
  - us-gaap_OperatingLeaseLiabilityCurrentStatementOfFinancialPositionExtensibleList
  - us-gaap_OperatingLeaseLiabilityCurrent
  - us-gaap_OperatingLeaseLiabilityNoncurrent

### http://www.nvidia.com/role/LeasesNarrativeDetails

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_LesseeLeaseDescriptionLineItems
      - us-gaap_LesseeOperatingLeaseLeaseNotYetCommencedTermOfContract1
      - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceSheetAmount
      - us-gaap_OperatingLeaseCost
      - us-gaap_OperatingLeaseWeightedAverageRemainingLeaseTerm1
      - us-gaap_OperatingLeaseWeightedAverageDiscountRatePercent

### http://www.nvidia.com/role/LeasesScheduleofotherleaseinformationDetails

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeasePayments
  - us-gaap_RightOfUseAssetObtainedInExchangeForOperatingLeaseLiability

### http://www.nvidia.com/role/ScheduleIIValuationandQualifyingAccountsDetails

- srt_ValuationAndQualifyingAccountsAbstract
  - srt_ValuationAndQualifyingAccountsDisclosureTable
    - us-gaap_ValuationAllowancesAndReservesTypeAxis
      - us-gaap_ValuationAllowancesAndReservesDomain
    - srt_ValuationAndQualifyingAccountsDisclosureLineItems
      - us-gaap_MovementInValuationAllowancesAndReservesRollForward

### http://xbrl.sec.gov/ecd/role/AwardTimingDisclosure

- ecd_AwardTmgDiscLineItems
  - ecd_AwardTmgMnpiDiscTextBlock
  - ecd_AwardTmgMethodTextBlock
  - ecd_AwardTmgPredtrmndFlag
  - ecd_AwardTmgMnpiCnsdrdFlag
  - ecd_AwardTmgHowMnpiCnsdrdTextBlock
  - ecd_MnpiDiscTimedForCompValFlag
  - ecd_AwardsCloseToMnpiDiscTableTextBlock
  - ecd_AwardsCloseToMnpiDiscTable
    - ecd_IndividualAxis
      - ecd_AllIndividualsMember
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
  - ecd_AwardsCloseToMnpiDiscIndName
  - ecd_AwardUndrlygSecuritiesAmt
  - ecd_AwardExrcPrice
  - ecd_AwardGrantDateFairValue
  - ecd_UndrlygSecurityMktPriceChngPct

### http://xbrl.sec.gov/ecd/role/ErrCompDisclosure

- ecd_RecoveryOfErrCompDisclosureLineItems
  - ecd_ErrCompRecoveryTable
    - ecd_RestatementDateAxis
    - ecd_IndividualAxis
      - ecd_AllIndividualsMember
  - ecd_RestatementDeterminationDate
  - ecd_AggtErrCompAmt
  - ecd_ErrCompAnalysisTextBlock
  - ecd_StkPrcOrTsrEstimationMethodTextBlock
  - ecd_OutstandingAggtErrCompAmt
  - ecd_AggtErrCompNotYetDeterminedTextBlock
  - ecd_ForgoneRecoveryIndName
  - ecd_ForgoneRecoveryDueToExpenseOfEnforcementAmt
  - ecd_ForgoneRecoveryDueToViolationOfHomeCountryLawAmt
  - ecd_ForgoneRecoveryDueToDisqualificationOfTaxBenefitsAmt
  - ecd_ForgoneRecoveryExplanationOfImpracticabilityTextBlock
  - ecd_OutstandingRecoveryIndName
  - ecd_OutstandingRecoveryCompAmt
  - ecd_RestatementDoesNotRequireRecoveryTextBlock

### http://xbrl.sec.gov/ecd/role/PvpDisclosure

- ecd_PayVsPerformanceDisclosureLineItems
  - ecd_PvpTable
    - ecd_ExecutiveCategoryAxis
      - ecd_AllExecutiveCategoriesMember
    - ecd_IndividualAxis
      - ecd_AllIndividualsMember
    - ecd_AdjToCompAxis
      - ecd_AllAdjToCompMember
    - ecd_MeasureAxis
  - ecd_PvpTableTextBlock
  - ecd_CoSelectedMeasureName
  - ecd_NamedExecutiveOfficersFnTextBlock
  - ecd_PeerGroupIssuersFnTextBlock
  - ecd_ChangedPeerGroupFnTextBlock
  - ecd_PeoTotalCompAmt [totalLabel]
  - ecd_PeoActuallyPaidCompAmt
  - ecd_AdjToPeoCompFnTextBlock
  - ecd_NonPeoNeoAvgTotalCompAmt [totalLabel]
  - ecd_NonPeoNeoAvgCompActuallyPaidAmt
  - ecd_AdjToNonPeoNeoCompFnTextBlock
  - ecd_EquityValuationAssumptionDifferenceFnTextBlock
  - ecd_CompActuallyPaidVsTotalShareholderRtnTextBlock [totalLabel]
  - ecd_CompActuallyPaidVsNetIncomeTextBlock
  - ecd_CompActuallyPaidVsCoSelectedMeasureTextBlock
  - ecd_TotalShareholderRtnVsPeerGroupTextBlock [totalLabel]
  - ecd_CompActuallyPaidVsOtherMeasureTextBlock
  - ecd_TabularListTableTextBlock
  - ecd_TotalShareholderRtnAmt [totalLabel]
  - ecd_PeerGroupTotalShareholderRtnAmt [totalLabel]
  - us-gaap_NetIncomeLoss
  - ecd_CoSelectedMeasureAmt
  - ecd_OtherPerfMeasureAmt
  - ecd_AdjToCompAmt
  - ecd_PeoName
  - ecd_MeasureName
  - ecd_NonGaapMeasureDescriptionTextBlock
  - ecd_Additional402vDisclosureTextBlock
  - ecd_PnsnBnftsAdjFnTextBlock
  - ecd_EqtyAwrdsAdjFnTextBlock

### http://xbrl.sec.gov/ecd/role/InsiderTradingArrangements

- ecd_InsiderTradingArrLineItems
  - ecd_TradingArrByIndTable
    - ecd_TradingArrAxis
      - ecd_AllTradingArrangementsMember
    - ecd_IndividualAxis
      - ecd_AllIndividualsMember
  - ecd_MtrlTermsOfTrdArrTextBlock
  - ecd_TrdArrIndName
  - ecd_TrdArrIndTitle
  - ecd_Rule10b51ArrAdoptedFlag
  - ecd_NonRule10b51ArrAdoptedFlag
  - ecd_TrdArrAdoptionDate
  - ecd_Rule10b51ArrTrmntdFlag
  - ecd_NonRule10b51ArrTrmntdFlag
  - ecd_TrdArrTerminationDate
  - ecd_TrdArrExpirationDate
  - ecd_TrdArrDuration
  - ecd_TrdArrSecuritiesAggAvailAmt

### http://xbrl.sec.gov/ecd/role/InsiderTradingPoliciesProc

- ecd_InsiderTradingPoliciesProcLineItems
  - ecd_InsiderTrdPoliciesProcAdoptedFlag
  - ecd_InsiderTrdPoliciesProcNotAdoptedTextBlock

