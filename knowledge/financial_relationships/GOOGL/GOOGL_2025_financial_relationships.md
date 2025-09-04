# GOOGL 2025 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.google.com/role/CONSOLIDATEDSTATEMENTSOFINCOME

- us-gaap_IncomeStatementAbstract
  - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
  - us-gaap_CostsAndExpensesAbstract
    - us-gaap_CostOfRevenue
    - us-gaap_ResearchAndDevelopmentExpense
    - us-gaap_SellingAndMarketingExpense
    - us-gaap_GeneralAndAdministrativeExpense
    - us-gaap_CostsAndExpenses [totalLabel]
  - us-gaap_OperatingIncomeLoss [totalLabel]
  - us-gaap_NonoperatingIncomeExpense
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]
  - us-gaap_IncomeTaxExpenseBenefit
  - us-gaap_NetIncomeLoss [totalLabel]
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.google.com/role/CONSOLIDATEDSTATEMENTSOFCOMPREHENSIVEINCOME

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
    - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
    - us-gaap_OtherComprehensiveIncomeAvailableForSaleSecuritiesAdjustmentNetOfTaxPeriodIncreaseDecreaseAbstract
      - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesAdjustmentNetOfTax [totalLabel]
    - us-gaap_OtherComprehensiveIncomeDerivativesQualifyingAsHedgesNetOfTaxPeriodIncreaseDecreaseAbstract
      - us-gaap_OtherComprehensiveIncomeLossCashFlowHedgeGainLossBeforeReclassificationAfterTax
      - us-gaap_OtherComprehensiveIncomeLossCashFlowHedgeGainLossReclassificationAfterTax
      - us-gaap_OtherComprehensiveIncomeLossCashFlowHedgeGainLossAfterReclassificationAndTax [totalLabel]
    - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.google.com/role/CONSOLIDATEDSTATEMENTSOFCOMPREHENSIVEINCOMEParenthetical

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentTax
  - us-gaap_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesTax
  - us-gaap_OtherComprehensiveIncomeLossCashFlowHedgeGainLossAfterReclassificationTax

### http://www.google.com/role/CONSOLIDATEDSTATEMENTSOFCASHFLOWS

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_Depreciation
  - us-gaap_ShareBasedCompensation
  - us-gaap_DeferredIncomeTaxesAndTaxCredits
  - us-gaap_DebtAndEquitySecuritiesGainLoss
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.google.com/role/Revenues

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueFromContractWithCustomerTextBlock

### http://www.google.com/role/NetIncomePerShare

- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareTextBlock

### http://www.google.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.google.com/role/RevenuesTables

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_DisaggregationOfRevenueTableTextBlock
  - us-gaap_RevenueFromExternalCustomersByGeographicAreasTableTextBlock

### http://www.google.com/role/NetIncomePerShareTables

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock

### http://www.google.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfUnrecognizedTaxBenefitsRollForwardTableTextBlock

### http://www.google.com/role/RevenuesRevenuebySegmentDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_GainLossOnOilAndGasHedgingActivity

### http://www.google.com/role/RevenuesRevenuebyGeographicLocationDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_ConcentrationRiskByTypeAxis
      - us-gaap_ConcentrationRiskTypeDomain
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_ConcentrationRiskPercentage1
      - us-gaap_GainLossOnOilAndGasHedgingActivity

### http://www.google.com/role/RevenuesNarrativeDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionTable
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionLineItems
      - us-gaap_RevenueRemainingPerformanceObligation
      - us-gaap_RevenueRemainingPerformanceObligationPercentage
      - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionPeriod1
      - us-gaap_ContractWithCustomerLiability
      - us-gaap_ContractWithCustomerLiabilityRevenueRecognized

### http://www.google.com/role/FinancialInstrumentsMarketableSecuritiesDetails

- us-gaap_OtherComprehensiveIncomeLocationAxis
  - us-gaap_OtherComprehensiveIncomeLocationDomain
    - us-gaap_OtherComprehensiveIncomeMember
- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - goog_NetIncomeMember

### http://www.google.com/role/FinancialInstrumentsDerivativeNotionalAmountsDetails

- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
  - us-gaap_HedgingDesignationAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.google.com/role/FinancialInstrumentsEffectofDerivativeInstrumentsonIncomeandAccumulatedOtherComprehensiveIncomeDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_IncomeStatementLocationAxis
      - us-gaap_IncomeStatementLocationDomain
    - us-gaap_DerivativeInstrumentsGainLossLineItems
      - us-gaap_OtherComprehensiveIncomeDerivativesQualifyingAsHedgesBeforeTaxPeriodIncreaseDecreaseAbstract
      - us-gaap_OtherComprehensiveIncomeForeignCurrencyTransactionAndTranslationAdjustmentBeforeTaxPeriodIncreaseDecreaseAbstract
      - us-gaap_OtherComprehensiveIncomeLossBeforeTaxPortionAttributableToParent [totalLabel]
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_NonoperatingIncomeExpense
      - us-gaap_EffectOfCashFlowHedgesOnResultsOfOperationsAbstract
      - us-gaap_EffectOfFairValueHedgesOnResultsOfOperationsAbstract
      - us-gaap_EffectOfNetInvestmentHedgeOnResultsOfOperationsAbstract
      - goog_EffectofDerivativesNotDesignatedasCashFlowHedgesonResultsofOperationsAbstract
      - us-gaap_DerivativeGainLossOnDerivativeNet [totalLabel]
      - us-gaap_DerivativeGainLossStatementOfIncomeOrComprehensiveIncomeExtensibleEnumeration

### http://www.google.com/role/SupplementalFinancialStatementInformationComponentsofAccumulatedOtherComprehensiveIncomeDetails

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossTable
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_AccumulatedOtherComprehensiveIncomeLossLineItems
      - us-gaap_AOCIAttributableToParentNetOfTaxRollForward

### http://www.google.com/role/SupplementalFinancialStatementInformationReclassificationsOutofAccumulatedOtherComprehensiveIncomeLossDetails

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeTable
    - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeAxis
      - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeDomain
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ReclassificationAdjustmentOutOfAccumulatedOtherComprehensiveIncomeLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_NonoperatingIncomeExpense
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_NetIncomeLoss

### http://www.google.com/role/SupplementalFinancialStatementInformationComponentsofOtherIncomeExpenseNetDetails

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_InterestIncomeOther
  - us-gaap_InterestExpenseNonoperating
  - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
  - us-gaap_DebtSecuritiesRealizedGainLoss
  - us-gaap_EquitySecuritiesFvNiGainLoss
  - goog_InvestmentPerformanceFees
  - goog_IncomeLossFromEquityMethodInvestmentsAndOtherThanTemporaryImpairmentNet
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_NonoperatingIncomeExpense [totalLabel]
  - us-gaap_InterestCostsCapitalized

### http://www.google.com/role/NetIncomePerShareScheduleofEarningsPerShareDetails

- us-gaap_EarningsPerShareAbstract
  - goog_EarningsPerShareDisclosureTable
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - goog_EarningsPerShareDisclosureLineItems
      - us-gaap_EarningsPerShareBasicAbstract
      - us-gaap_EarningsPerShareDilutedAbstract

### http://www.google.com/role/IncomeTaxesIncomeFromContinuingOperationsBeforeIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]

### http://www.google.com/role/IncomeTaxesProvisionforIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxExpenseBenefitContinuingOperationsAbstract
    - us-gaap_CurrentIncomeTaxExpenseBenefitContinuingOperationsAbstract
      - us-gaap_CurrentFederalStateAndLocalTaxExpenseBenefit
      - us-gaap_CurrentForeignTaxExpenseBenefit
      - us-gaap_CurrentIncomeTaxExpenseBenefit [totalLabel]
    - us-gaap_DeferredIncomeTaxExpenseBenefitContinuingOperationsAbstract
      - us-gaap_DeferredFederalStateAndLocalTaxExpenseBenefit
      - us-gaap_DeferredForeignIncomeTaxExpenseBenefit
      - us-gaap_DeferredIncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.google.com/role/IncomeTaxesReconciliationofFederalStatutoryIncomeTaxRatetoEffectiveIncomeTaxRateDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_EffectiveIncomeTaxRateContinuingOperationsTaxRateReconciliationAbstract
    - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
    - us-gaap_EffectiveIncomeTaxRateReconciliationForeignIncomeTaxRateDifferential
    - us-gaap_EffectiveIncomeTaxRateReconciliationFdiiPercent
    - us-gaap_EffectiveIncomeTaxRateReconciliationNondeductibleExpenseShareBasedCompensationCost
    - us-gaap_EffectiveIncomeTaxRateReconciliationTaxCreditsResearch
    - us-gaap_EffectiveIncomeTaxRateReconciliationChangeInDeferredTaxAssetsValuationAllowance
    - us-gaap_EffectiveIncomeTaxRateReconciliationStateAndLocalIncomeTaxes
    - goog_EffectiveIncomeTaxRateReconciliationImpactOfTaxLawChangePercent
    - us-gaap_EffectiveIncomeTaxRateReconciliationOtherAdjustments
    - us-gaap_EffectiveIncomeTaxRateContinuingOperations [totalLabel]

### http://www.google.com/role/IncomeTaxesSignificantComponentsofDeferredTaxAssetsandLiabilitiesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
    - us-gaap_DeferredTaxAssetsNetAbstract
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsEmployeeBenefits
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccrualsOther
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsOther
      - us-gaap_DeferredTaxAssetsOperatingLossCarryforwards
      - goog_DeferredTaxAssetsOperatingLeaseRightOfUseAsset
      - us-gaap_DeferredTaxAssetsInProcessResearchAndDevelopment
      - us-gaap_DeferredTaxAssetsOther
      - us-gaap_DeferredTaxAssetsGross [totalLabel]
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_DeferredTaxAssetsNet [totalLabel]
    - us-gaap_DeferredTaxLiabilitiesAbstract
      - us-gaap_DeferredTaxLiabilitiesPropertyPlantAndEquipment
      - us-gaap_DeferredTaxLiabilitiesInvestments
      - goog_DeferredTaxLiabilitiesOperatingLeaseLiability
      - us-gaap_DeferredTaxLiabilitiesOther
      - us-gaap_DeferredIncomeTaxLiabilities
    - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]

### http://www.google.com/role/IncomeTaxesNarrativeDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - goog_IncomeTaxesTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_TaxCreditCarryforwardAxis
      - us-gaap_TaxCreditCarryforwardNameDomain
    - goog_IncomeTaxesLineItems
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_TaxCreditCarryforwardAmount
      - us-gaap_IncomeTaxesPaidNet
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - goog_NumberOfTaxJurisdictions

### http://www.google.com/role/IncomeTaxesSummaryofActivityRelatedtoGrossUnrecognizedTaxBenefitsDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ReconciliationOfUnrecognizedTaxBenefitsExcludingAmountsPertainingToExaminedTaxReturnsRollForward
    - us-gaap_UnrecognizedTaxBenefits
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefits

### http://www.google.com/role/InformationaboutSegmentsandGeographicAreasRevenueandOperatingIncomeLossbySegmentDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - srt_ConsolidationItemsAxis
      - srt_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_GainLossOnOilAndGasHedgingActivity
      - us-gaap_OperatingIncomeLoss
      - us-gaap_LaborAndRelatedExpense
      - us-gaap_OperatingExpenses
      - us-gaap_CostsAndExpenses [totalLabel]

### http://www.google.com/role/InformationaboutSegmentsandGeographicAreasLongLivedAssetsbyGeographicAreaDetails

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - srt_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

## 资产负债表结构 (Balance Sheet Structure)

### http://www.google.com/role/CONSOLIDATEDBALANCESHEETS

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_AssetsAbstract
    - us-gaap_AssetsCurrentAbstract
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_MarketableSecuritiesCurrent
      - us-gaap_CashCashEquivalentsAndShortTermInvestments [totalLabel]
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_OtherAssetsCurrent
      - us-gaap_AssetsCurrent [totalLabel]
    - us-gaap_OtherLongTermInvestments
    - us-gaap_DeferredIncomeTaxAssetsNet
    - us-gaap_PropertyPlantAndEquipmentNet
    - us-gaap_OperatingLeaseRightOfUseAsset
    - us-gaap_Goodwill
    - us-gaap_OtherAssetsNoncurrent
    - us-gaap_Assets [totalLabel]
  - us-gaap_LiabilitiesAndStockholdersEquityAbstract
    - us-gaap_LiabilitiesCurrentAbstract
      - us-gaap_AccountsPayableCurrent
      - us-gaap_EmployeeRelatedLiabilitiesCurrent
      - us-gaap_AccruedLiabilitiesCurrent
      - goog_AccruedRevenueShare
      - us-gaap_ContractWithCustomerLiabilityCurrent
      - us-gaap_LiabilitiesCurrent [totalLabel]
    - us-gaap_LongTermDebtAndCapitalLeaseObligations
    - us-gaap_AccruedIncomeTaxesNoncurrent
    - us-gaap_OperatingLeaseLiabilityNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent
    - us-gaap_Liabilities [totalLabel]
    - us-gaap_CommitmentsAndContingencies
    - us-gaap_StockholdersEquityAbstract
      - us-gaap_ConvertiblePreferredStockNonredeemableOrRedeemableIssuerOptionValue
      - us-gaap_CommonStocksIncludingAdditionalPaidInCapital
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
      - us-gaap_RetainedEarningsAccumulatedDeficit
      - us-gaap_StockholdersEquity [totalLabel]
    - us-gaap_LiabilitiesAndStockholdersEquity [totalLabel]

### http://www.google.com/role/CONSOLIDATEDBALANCESHEETSParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_StatementLineItems
      - us-gaap_StockholdersEquityAbstract

### http://www.google.com/role/CONSOLIDATEDSTATEMENTSOFSTOCKHOLDERSEQUITY

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_SharesIssued
  - us-gaap_StockholdersEquity
  - us-gaap_StockIssuedDuringPeriodSharesNewIssues
  - us-gaap_StockIssuedDuringPeriodValueNewIssues
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
  - goog_TaxWithholdingRelatedToVestingOfRestrictedStockUnits
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalDividendsInExcessOfRetainedEarnings
  - us-gaap_NoncontrollingInterestIncreaseFromSaleOfParentEquityInterest
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent
  - us-gaap_SharesIssued
  - us-gaap_StockholdersEquity
- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockIncludingAdditionalPaidInCapitalMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
    - us-gaap_RetainedEarningsMember

### http://www.google.com/role/CONSOLIDATEDSTATEMENTSOFCASHFLOWS

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetIncomeLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
    - us-gaap_PaymentsToAcquireMarketableSecurities
    - us-gaap_ProceedsFromSaleAndMaturityOfMarketableSecurities
    - us-gaap_PaymentsToAcquireOtherInvestments
    - us-gaap_ProceedsFromSaleAndMaturityOfOtherInvestments
    - goog_AcquisitionsNetOfCashAcquiredAndPurchasesOfIntangibleAndOtherAssets
    - us-gaap_PaymentsForProceedsFromOtherInvestingActivities
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - goog_NetProceedsPaymentsRelatedToStockBasedAwardActivities
    - us-gaap_PaymentsForRepurchaseOfCommonStock
    - us-gaap_PaymentsOfDividends
    - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
    - us-gaap_RepaymentsOfDebtAndCapitalLeaseObligations
    - us-gaap_ProceedsFromMinorityShareholders
    - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
  - us-gaap_EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect [totalLabel]
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents

### http://www.google.com/role/CONSOLIDATEDSTATEMENTSOFSTOCKHOLDERSEQUITYParenthetical

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_CommonStockDividendsPerShareDeclared

### http://www.google.com/role/BusinessCombinations

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_BusinessCombinationDisclosureTextBlock

### http://www.google.com/role/Goodwill

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillDisclosureTextBlock

### http://www.google.com/role/StockholdersEquity

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.google.com/role/GoodwillTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTextBlock

### http://www.google.com/role/StockholdersEquityTables

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfTreasuryStockByClassTextBlock

### http://www.google.com/role/FinancialInstrumentsMarketableSecuritiesDetails

- us-gaap_ScheduleOfTradingSecuritiesAndOtherTradingAssetsTable
  - us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_FinancialInstrumentAxis
  - us-gaap_IncomeStatementLocationAxis
  - us-gaap_OtherComprehensiveIncomeLocationAxis
  - us-gaap_ScheduleOfTradingSecuritiesAndOtherTradingAssetsLineItems
    - us-gaap_AvailableForSaleSecuritiesFairValueToAmortizedCostBasisAbstract
    - us-gaap_MarketableSecuritiesNoncurrent

### http://www.google.com/role/FinancialInstrumentsGrossUnrealizedLossesandFairValuesforInvestmentsinUnrealizedLossPositionDetails

- us-gaap_FairValueDisclosuresAbstract
  - goog_InvestmentsUnrealizedLossPositionTable
    - us-gaap_FinancialInstrumentAxis
      - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
    - goog_InvestmentsUnrealizedLossPositionLineItems
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPositionLessThan12Months
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPositionLessThan12MonthsAccumulatedLoss
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPosition12MonthsOrLonger
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPosition12MonthsOrLongerAccumulatedLoss
      - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPosition [totalLabel]
      - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPositionAccumulatedLoss

### http://www.google.com/role/FinancialInstrumentsCarryingValuesforMarketableandNonMarketableEquitySecuritiesDetails

- us-gaap_EquitySecuritiesFvNiGainLossAbstract
  - goog_EquitySecuritiesFVNIAndWithoutReadilyDeterminableFairValueCost [totalLabel]
  - goog_EquitySecuritiesFVNIAndWithoutReadilyDeterminableFairValueAccumulatedGrossUnrealizedGainLossBeforeTax [totalLabel]
  - us-gaap_EquitySecuritiesFvNiAndWithoutReadilyDeterminableFairValue [totalLabel]
- goog_NonMarketableEquitySecuritiesAbstract
  - goog_EquitySecuritiesWithoutReadilyDeterminableFairValueCost
  - goog_EquitySecuritiesWithoutReadilyDeterminableFairValueAccumulatedGrossUnrealizedGainLossBeforeTax
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueAmount [totalLabel]

### http://www.google.com/role/FinancialInstrumentsGainsandLossesonMarketableandNonMarketableEquitySecuritiesDetails

- us-gaap_EquitySecuritiesFvNiGainLossAlternativeAbstract
  - us-gaap_EquitySecuritiesFvNiRealizedGainLoss
  - us-gaap_EquitySecuritiesFvNiUnrealizedGainLoss
  - goog_EquitySecuritiesWithoutReadilyDeterminableFairValueFVNIUnrealizedGainLoss
  - us-gaap_EquitySecuritiesFvNiGainLoss [totalLabel]

### http://www.google.com/role/FinancialInstrumentsFairValuesofOutstandingDerivativeInstrumentsDetails

- us-gaap_DerivativeAssetsAbstract
  - us-gaap_DerivativeAssets

### http://www.google.com/role/FinancialInstrumentsOffsettingofFinancialAssetsandFinancialLiabilitiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_DerivativeAssetsAbstract
    - us-gaap_DerivativeFairValueOfDerivativeAsset
    - us-gaap_DerivativeAssetFairValueGrossLiability
    - us-gaap_DerivativeAssets [totalLabel]
    - us-gaap_DerivativeAssetNotOffsetPolicyElectionDeduction
    - goog_DerivativeAssetSubjectToMasterNettingArrangementCollateralObligationToReturnCashAndSecurityNotOffset
    - us-gaap_DerivativeAssetFairValueOffsetAgainstCollateralNetOfNotSubjectToMasterNettingArrangementPolicyElection [totalLabel]
  - us-gaap_OffsettingDerivativeLiabilitiesAbstract
    - us-gaap_DerivativeFairValueOfDerivativeLiability
    - us-gaap_DerivativeLiabilityFairValueGrossAsset
    - us-gaap_DerivativeLiabilities [totalLabel]
    - us-gaap_DerivativeLiabilityNotOffsetPolicyElectionDeduction
    - goog_DerivativeLiabilitySubjectToMasterNettingArrangementCollateralRightToReclaimCashAndSecurityNotOffset
    - us-gaap_DerivativeLiabilityFairValueOffsetAgainstCollateralNetOfNotSubjectToMasterNettingArrangementPolicyElection [totalLabel]
  - us-gaap_DerivativeAssetStatementOfFinancialPositionExtensibleEnumeration
  - us-gaap_DerivativeLiabilityStatementOfFinancialPositionExtensibleEnumeration

### http://www.google.com/role/LeasesSupplementalBalanceSheetInformationDetails

- us-gaap_LeasesAbstract
  - goog_WeightedAverageRemainingLeaseTermAbstract
    - us-gaap_OperatingLeaseWeightedAverageRemainingLeaseTerm1
    - us-gaap_FinanceLeaseWeightedAverageRemainingLeaseTerm1
  - goog_LeasesWeightedAverageDiscountRateAbstract
    - us-gaap_OperatingLeaseWeightedAverageDiscountRatePercent
    - us-gaap_FinanceLeaseWeightedAverageDiscountRatePercent
  - us-gaap_LesseeOperatingLeaseDescriptionAbstract
    - us-gaap_OperatingLeaseRightOfUseAsset
    - us-gaap_OperatingLeaseLiabilityCurrent
    - us-gaap_OperatingLeaseLiabilityNoncurrent
    - us-gaap_OperatingLeaseLiability [totalLabel]
  - us-gaap_LesseeFinanceLeaseDescriptionAbstract
    - us-gaap_FinanceLeaseRightOfUseAssetBeforeAccumulatedAmortization
    - us-gaap_FinanceLeaseRightOfUseAssetAccumulatedAmortization
    - us-gaap_FinanceLeaseRightOfUseAsset [totalLabel]
    - us-gaap_FinanceLeaseLiabilityCurrent
    - us-gaap_FinanceLeaseLiabilityNoncurrent
    - us-gaap_FinanceLeaseLiability [totalLabel]
  - us-gaap_OperatingLeaseLiabilityCurrentStatementOfFinancialPositionExtensibleList
  - us-gaap_OperatingLeaseLiabilityNoncurrentStatementOfFinancialPositionExtensibleList
  - us-gaap_FinanceLeaseRightOfUseAssetStatementOfFinancialPositionExtensibleList
  - us-gaap_FinanceLeaseLiabilityCurrentStatementOfFinancialPositionExtensibleList
  - us-gaap_FinanceLeaseLiabilityNoncurrentStatementOfFinancialPositionExtensibleList

### http://www.google.com/role/LeasesSupplementalCashFlowInformationDetails

- goog_RightOfUseAssetObtainedInExchangeForLeaseLiabilityAbstract
  - us-gaap_RightOfUseAssetObtainedInExchangeForOperatingLeaseLiability
  - us-gaap_RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability
- goog_CashFlowLesseeAbstract
  - us-gaap_OperatingLeasePayments
  - us-gaap_FinanceLeaseInterestPaymentOnLiability
  - us-gaap_FinanceLeasePrincipalPayments

### http://www.google.com/role/BusinessCombinationsDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable

### http://www.google.com/role/GoodwillChangesinCarryingAmountofGoodwillDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTable

### http://www.google.com/role/StockholdersEquityNarrativeDetails

- us-gaap_EquityAbstract
  - goog_StockholdersEquityNoteTable
    - us-gaap_StatementClassOfStockAxis
    - srt_ShareRepurchaseProgramAxis
    - goog_StockholdersEquityNoteLineItems
      - goog_NumberOfClassesOfCommonStock
      - goog_CommonStockNumberOfVotes
      - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
      - srt_StockRepurchaseProgramAuthorizedAmount1
      - us-gaap_StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1
      - us-gaap_Dividends

### http://www.google.com/role/StockholdersEquityShareRepurchasesDetails

- us-gaap_EquityAbstract
  - goog_StockholdersEquityNoteTable
    - srt_ShareRepurchaseProgramAxis
    - us-gaap_StatementClassOfStockAxis
    - goog_StockholdersEquityNoteLineItems
      - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
      - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue

### http://www.google.com/role/CompensationPlansStockBasedAwardActivitiesDetails

- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue

### http://www.google.com/role/InformationaboutSegmentsandGeographicAreasLongLivedAssetsbyGeographicAreaDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - us-gaap_NonUsMember

## 现金流量表结构 (Cash Flow Structure)

### http://www.google.com/role/CONSOLIDATEDSTATEMENTSOFCASHFLOWS

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInIncomeTaxes
  - us-gaap_IncreaseDecreaseInOtherOperatingAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInAccruedLiabilities
  - goog_IncreaseDecreaseInAccruedRevenueShare
  - us-gaap_IncreaseDecreaseInContractWithCustomerLiability

### http://www.google.com/role/LeasesSupplementalCashFlowInformationDetails

- us-gaap_LeasesAbstract
  - goog_CashFlowLesseeAbstract
  - goog_RightOfUseAssetObtainedInExchangeForLeaseLiabilityAbstract

### http://www.google.com/role/LeasesFutureMinimumLeasePaymentsDetails

- us-gaap_OperatingLeaseLiabilitiesPaymentsDueAbstract
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueNextTwelveMonths
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearTwo
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearThree
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearFour
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearFive
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueAfterYearFive
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDue [totalLabel]
  - us-gaap_LesseeOperatingLeaseLiabilityUndiscountedExcessAmount
  - us-gaap_OperatingLeaseLiability

## 股东权益结构 (Equity Structure)

### http://www.google.com/role/CoverPage

- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - us-gaap_CommonClassAMember
    - goog_CapitalClassCMember
    - us-gaap_CommonClassBMember

### http://www.google.com/role/CONSOLIDATEDSTATEMENTSOFSTOCKHOLDERSEQUITY

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward

### http://www.google.com/role/CompensationPlans

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_CompensationAndEmployeeBenefitPlansTextBlock

### http://www.google.com/role/CompensationPlansTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationRestrictedStockUnitsAwardActivityTableTextBlock

### http://www.google.com/role/FinancialInstrumentsCarryingValuesforMarketableandNonMarketableEquitySecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_MarketableSecuritiesAbstract
    - us-gaap_EquitySecuritiesFvNiCost
    - goog_EquitySecuritiesFVNIAccumulatedGrossUnrealizedGainLossBeforeTax
    - us-gaap_EquitySecuritiesFvNi [totalLabel]
  - goog_NonMarketableEquitySecuritiesAbstract
  - us-gaap_EquitySecuritiesFvNiGainLossAbstract
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentCumulativeAmount
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueDownwardPriceAdjustmentCumulativeAmount

### http://www.google.com/role/FinancialInstrumentsGainsandLossesonMarketableandNonMarketableEquitySecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_EquitySecuritiesFvNiGainLossAlternativeAbstract
  - goog_NonMarketableSecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustment
  - goog_NonMarketableSecuritiesWithoutReadilyDeterminableFairValueDownwardPriceAdjustment

### http://www.google.com/role/FinancialInstrumentsCumulativeNetGainsLossesonEquitySecuritiesSoldDetails

- us-gaap_FairValueDisclosuresAbstract
  - goog_ProceedsFromSaleOfEquitySecuritiesFVNIHeldForInvestment
  - goog_EquitySecuritiesFVNICostBasisOfSecuritiesSold
  - goog_EquitySecuritiesFVNICumulativeGainLossNet

### http://www.google.com/role/StockholdersEquityNarrativeDetails

- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - us-gaap_CommonClassAMember
    - us-gaap_CommonClassBMember
    - goog_CapitalClassCMember
    - goog_CapitalClassAAndCMember
    - goog_CapitalClassAMember
    - goog_CapitalClassBMember
- srt_ShareRepurchaseProgramAxis
  - srt_ShareRepurchaseProgramDomain
    - goog_ShareRepurchaseProgramMember

### http://www.google.com/role/StockholdersEquityShareRepurchasesDetails

- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - goog_CapitalClassAMember
    - goog_CapitalClassCMember
- srt_ShareRepurchaseProgramAxis
  - srt_ShareRepurchaseProgramDomain
    - goog_ShareRepurchaseProgramMember

### http://www.google.com/role/CompensationPlansStockPlansDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_CommonStockCapitalSharesReservedForFutureIssuance

### http://www.google.com/role/CompensationPlansStockBasedCompensationDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_AllocatedShareBasedCompensationExpense
  - goog_SharebasedPaymentArrangementNoncashExpenseIncludingLiabilitiesSettled
  - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense
  - goog_TaxBenefitFromStockBasedAwardActivity

### http://www.google.com/role/CompensationPlansStockBasedAwardActivitiesDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]

### http://xbrl.sec.gov/ecd/role/AwardTimingDisclosure

- us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
  - us-gaap_EmployeeStockOptionMember
  - us-gaap_StockAppreciationRightsSARSMember

## 其他结构 (Other Structure)

### http://www.google.com/role/CoverPage

- dei_CoverAbstract
  - dei_EntitiesTable
    - us-gaap_StatementClassOfStockAxis
    - dei_DocumentInformationLineItems
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
      - dei_AmendmentFlag
      - dei_DocumentFiscalYearFocus
      - dei_DocumentFiscalPeriodFocus
      - dei_EntityCentralIndexKey

### http://www.google.com/role/AuditInformation

- goog_AuditInformationAbstract
  - dei_AuditorLocation
  - dei_AuditorName
  - dei_AuditorFirmId

### http://www.google.com/role/SummaryofSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BusinessDescriptionAndAccountingPoliciesTextBlock

### http://www.google.com/role/FinancialInstruments

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FinancialInstrumentsDisclosureTextBlock

### http://www.google.com/role/Leases

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeasesTextBlock
  - us-gaap_LesseeFinanceLeasesTextBlock

### http://www.google.com/role/VariableInterestEntities

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_VariableInterestEntityDisclosureTextBlock

### http://www.google.com/role/Debt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.google.com/role/SupplementalFinancialStatementInformation

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_SupplementalBalanceSheetDisclosuresTextBlock

### http://www.google.com/role/CommitmentsandContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.google.com/role/InformationaboutSegmentsandGeographicAreas

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.google.com/role/SubsequentEvent

- us-gaap_SubsequentEventsAbstract
  - us-gaap_SubsequentEventsTextBlock

### http://www.google.com/role/ScheduleIIValuationandQualifyingAccounts

- srt_ValuationAndQualifyingAccountsAbstract
  - srt_ScheduleOfValuationAndQualifyingAccountsDisclosureTextBlock

### http://www.google.com/role/SummaryofSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - goog_NatureOfOperationsPolicyPolicyTextBlock
  - us-gaap_ConsolidationPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_RevenueFromContractWithCustomerPolicyTextBlock
  - us-gaap_ResearchDevelopmentAndComputerSoftwarePolicyTextBlock
  - us-gaap_ShareBasedCompensationOptionAndIncentivePlansPolicy
  - us-gaap_AdvertisingCostsPolicyTextBlock
  - us-gaap_CompensationRelatedCostsPolicyTextBlock
  - us-gaap_FairValueOfFinancialInstrumentsPolicy
  - us-gaap_ConcentrationRiskCreditRisk
  - goog_CashAndCashEquivalentsAndMarketableSecuritiesPolicyPolicyTextBlock
  - goog_NonMarketableEquityInvestmentsPolicyPolicyTextBlock
  - us-gaap_ReceivablesPolicyTextBlock
  - us-gaap_FinanceLoansAndLeasesReceivablePolicy
  - goog_ImpairmentOfMarketableAndNonMarketableSecuritiesPolicyPolicyTextBlock
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_ConsolidationVariableInterestEntityPolicy
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_GoodwillAndIntangibleAssetsGoodwillPolicy
  - us-gaap_LesseeLeasesPolicyTextBlock
  - us-gaap_ImpairmentOrDisposalOfLongLivedAssetsPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_BusinessCombinationsPolicy
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock
  - us-gaap_PriorPeriodReclassificationAdjustmentDescription
  - us-gaap_SegmentReportingPolicyPolicyTextBlock

### http://www.google.com/role/FinancialInstrumentsTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_MarketableSecuritiesTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock
  - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPositionFairValueTableTextBlock
  - us-gaap_DebtSecuritiesAvailableForSaleTableTextBlock
  - goog_CarryingValueOfMarketableAndNonMarketableEquitySecuritiesTableTextBlock
  - us-gaap_GainLossOnInvestmentsTextBlock
  - goog_CumulativeNetGainLossOnEquitySecuritiesSoldTableTextBlock
  - us-gaap_ScheduleOfDerivativeInstrumentsTextBlock
  - us-gaap_ScheduleOfDerivativeInstrumentsInStatementOfFinancialPositionFairValueTextBlock
  - us-gaap_ScheduleOfDerivativeInstrumentsGainLossInStatementOfFinancialPerformanceTextBlock
  - us-gaap_OffsettingAssetsTableTextBlock
  - us-gaap_OffsettingLiabilitiesTableTextBlock

### http://www.google.com/role/LeasesTables

- us-gaap_LeasesAbstract
  - us-gaap_LeaseCostTableTextBlock
  - goog_AssetsAndLiabilitiesLesseeTableTextBlock
  - goog_SupplementalCashFlowInformationTableTextBlock
  - us-gaap_LesseeOperatingLeaseLiabilityMaturityTableTextBlock
  - us-gaap_FinanceLeaseLiabilityMaturityTableTextBlock

### http://www.google.com/role/DebtTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtInstrumentsTextBlock
  - us-gaap_ScheduleOfMaturitiesOfLongTermDebtTableTextBlock

### http://www.google.com/role/SupplementalFinancialStatementInformationTables

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock
  - us-gaap_ScheduleOfAccruedLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfAccumulatedOtherComprehensiveIncomeLossTableTextBlock
  - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeTableTextBlock
  - us-gaap_ScheduleOfOtherNonoperatingIncomeExpenseTableTextBlock

### http://www.google.com/role/InformationaboutSegmentsandGeographicAreasTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
  - us-gaap_LongLivedAssetsByGeographicAreasTableTextBlock

### http://www.google.com/role/SummaryofSignificantAccountingPoliciesDetails

- us-gaap_AccountingPoliciesAbstract
  - goog_OrganizationAndSummaryOfSignificantAccountingPoliciesTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - goog_OrganizationAndSummaryOfSignificantAccountingPoliciesLineItems
      - us-gaap_MarketingAndAdvertisingExpense
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_GoodwillImpairmentLoss

### http://www.google.com/role/FinancialInstrumentsMarketableSecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_ScheduleOfTradingSecuritiesAndOtherTradingAssetsTable
- us-gaap_FinancialInstrumentAxis
  - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
    - us-gaap_BankTimeDepositsMember
    - us-gaap_MoneyMarketFundsMember
    - goog_MarketableEquitySecuritiesMember
    - us-gaap_MutualFundMember
    - goog_GovernmentBondsMember
    - us-gaap_CorporateDebtSecuritiesMember
    - goog_MortgageBackedandAssetBackedSecuritiesMember
- us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueInputsLevel2Member
    - us-gaap_FairValueInputsLevel1Member
- us-gaap_AvailableForSaleSecuritiesFairValueToAmortizedCostBasisAbstract
  - goog_CashCashEquivalentsAndAvailableForSaleDebtSecuritiesAmortizedCost [totalLabel]
  - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
  - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
  - goog_CashCashEquivalentsAndMarketableSecurities [totalLabel]
  - us-gaap_CashAndCashEquivalentsFairValueDisclosure
  - us-gaap_MarketableSecuritiesCurrent
  - us-gaap_Cash
  - us-gaap_CashAndCashEquivalentsAtCarryingValue

### http://www.google.com/role/FinancialInstrumentsNarrativeDetails

- us-gaap_FairValueDisclosuresAbstract
  - goog_FinancialInstrumentsAndFairValueTable
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ValuationTechniqueAxis
      - us-gaap_ValuationTechniqueDomain
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - goog_FinancialInstrumentsAndFairValueLineItems
      - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueAmount
      - us-gaap_EquityMethodInvestments
      - goog_InvestmentsInConvertibleNotesIncludingFinancingReceivablesAndAvailableForSaleDebtSecurities
      - us-gaap_DerivativeRemainingMaturity1
      - us-gaap_ForeignCurrencyCashFlowHedgeGainLossToBeReclassifiedDuringNext12Months

### http://www.google.com/role/FinancialInstrumentsContractualMaturityDateofMarketableDebtSecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterFiveThroughTenYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterTenYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtSecurities [totalLabel]

### http://www.google.com/role/FinancialInstrumentsSummaryofGainsandLossesforDebtSecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - goog_FairValueOptionDebtSecuritiesAvailableForSaleUnrealizedGainLoss
  - us-gaap_DebtSecuritiesAvailableForSaleRealizedGain
  - us-gaap_DebtSecuritiesAvailableForSaleRealizedLoss
  - us-gaap_DebtSecuritiesAvailableForSaleAllowanceForCreditLossPeriodIncreaseDecrease
  - us-gaap_DebtSecuritiesAvailableForSaleGainLoss [totalLabel]

### http://www.google.com/role/FinancialInstrumentsDerivativeNotionalAmountsDetails

- us-gaap_HedgingDesignationAxis
  - us-gaap_HedgingDesignationDomain
    - us-gaap_DesignatedAsHedgingInstrumentMember
    - us-gaap_NondesignatedMember
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ForeignExchangeContractMember
    - us-gaap_OtherContractMember
- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
  - us-gaap_HedgingRelationshipDomain
    - us-gaap_CashFlowHedgingMember
    - us-gaap_FairValueHedgingMember
    - us-gaap_NetInvestmentHedgingMember
- us-gaap_DerivativeInstrumentsGainLossLineItems
  - us-gaap_DerivativeNotionalAmount

### http://www.google.com/role/FinancialInstrumentsFairValuesofOutstandingDerivativeInstrumentsDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValuesDerivativesBalanceSheetLocationByDerivativeContractTypeByHedgingDesignationTable
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativesFairValueLineItems
      - us-gaap_DerivativeAssetsAbstract
      - us-gaap_DerivativeLiabilitiesAbstract

### http://www.google.com/role/LeasesComponentsofOperatingLeaseExpenseDetails

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeaseCost
  - goog_FinanceLeaseCostAbstract
    - us-gaap_FinanceLeaseRightOfUseAssetAmortization
    - us-gaap_FinanceLeaseInterestExpense
    - goog_FinanceLeaseCost [totalLabel]
  - us-gaap_VariableLeaseCost
  - us-gaap_LeaseCost [totalLabel]

### http://www.google.com/role/LeasesFutureMinimumLeasePaymentsDetails

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeaseLiabilitiesPaymentsDueAbstract
  - us-gaap_FinanceLeaseLiabilitiesPaymentsDueAbstract
    - us-gaap_FinanceLeaseLiabilityPaymentsDueNextTwelveMonths
    - us-gaap_FinanceLeaseLiabilityPaymentsDueYearTwo
    - us-gaap_FinanceLeaseLiabilityPaymentsDueYearThree
    - us-gaap_FinanceLeaseLiabilityPaymentsDueYearFour
    - us-gaap_FinanceLeaseLiabilityPaymentsDueYearFive
    - us-gaap_FinanceLeaseLiabilityPaymentsDueAfterYearFive
    - us-gaap_FinanceLeaseLiabilityPaymentsDue [totalLabel]
    - us-gaap_FinanceLeaseLiabilityUndiscountedExcessAmount
    - us-gaap_FinanceLeaseLiability

### http://www.google.com/role/LeasesNarrativeDetails

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_LesseeLeaseDescriptionLineItems
      - goog_LesseeLeaseNotYetCommencedCurrentAmount
      - goog_LesseeLeaseNotYetCommencedNoncurrentAmount
      - us-gaap_LesseeFinanceLeaseLeaseNotYetCommencedTermOfContract1
      - us-gaap_LesseeOperatingLeaseLeaseNotYetCommencedTermOfContract1

### http://www.google.com/role/VariableInterestEntitiesDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTable
    - srt_ConsolidatedEntitiesAxis
      - srt_ConsolidatedEntitiesDomain
    - us-gaap_PledgedStatusAxis
      - us-gaap_PledgedStatusDomain
    - us-gaap_RecourseStatusAxis
      - us-gaap_RecourseStatusDomain
    - srt_CounterpartyNameAxis
      - srt_RepurchaseAgreementCounterpartyNameDomain
    - us-gaap_VariableInterestEntityLineItems
      - us-gaap_Assets
      - us-gaap_Liabilities
      - us-gaap_InvestmentsInAndAdvancesToAffiliatesAtFairValueGrossAdditions
      - us-gaap_NoncontrollingInterestInVariableInterestEntity
      - goog_RedeemableNoncontrollingInterestInVariableInterestEntity
      - goog_UnconsolidatedVariableInterestEntityFutureFundingCommitments

### http://www.google.com/role/DebtNarrativeDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_ShortTermDebtTypeAxis
      - us-gaap_ShortTermDebtTypeDomain
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - goog_ShortTermDebtMaximumBorrowingCapacity
      - us-gaap_CommercialPaper
      - us-gaap_DebtWeightedAverageInterestRate
      - us-gaap_LongTermDebtFairValue
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_LinesOfCreditCurrent

### http://www.google.com/role/DebtLongTermDebtDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LongTermDebtNoncurrentAbstract

### http://www.google.com/role/DebtFuturePrincipalPaymentsforBorrowingsDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_LongTermDebtByMaturityAbstract
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive
    - us-gaap_LongTermDebt [totalLabel]

### http://www.google.com/role/SupplementalFinancialStatementInformationNarrativeDetails

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_AllowanceForDoubtfulAccountsReceivable

### http://www.google.com/role/SupplementalFinancialStatementInformationPropertyandEquipmentNetDetails

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_ConstructionInProgressGross
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]

### http://www.google.com/role/SupplementalFinancialStatementInformationAccruedExpensesandOtherCurrentLiabilitiesDetails

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_LossContingencyAccrualCarryingValueCurrent
  - goog_AccruedPurchasesOfPropertyAndEquipmentCurrent
  - goog_AccruedCustomerLiabilitiesCurrent
  - us-gaap_OperatingLeaseLiabilityCurrent
  - us-gaap_AccruedIncomeTaxesCurrent
  - us-gaap_OtherAccruedLiabilitiesCurrent
  - us-gaap_AccruedLiabilitiesCurrent [totalLabel]
  - us-gaap_OperatingLeaseLiabilityCurrentStatementOfFinancialPositionExtensibleList
  - us-gaap_LossContingencyAccrualPayments
  - us-gaap_CapitalExpendituresIncurredButNotYetPaid

### http://www.google.com/role/BusinessCombinationsDetails

- us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
  - us-gaap_BusinessAcquisitionAxis
    - us-gaap_BusinessAcquisitionAcquireeDomain
      - goog_Character.aiMember
  - us-gaap_BusinessAcquisitionLineItems
    - us-gaap_Goodwill
    - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles
    - us-gaap_BusinessCombinationConsiderationTransferred1

### http://www.google.com/role/GoodwillChangesinCarryingAmountofGoodwillDetails

- us-gaap_ScheduleOfGoodwillTable
  - us-gaap_StatementBusinessSegmentsAxis
    - us-gaap_SegmentDomain
      - goog_GoogleServicesMember
      - goog_GoogleCloudMember
      - us-gaap_AllOtherSegmentsMember
  - us-gaap_GoodwillLineItems
    - us-gaap_GoodwillRollForward
      - us-gaap_Goodwill
      - us-gaap_GoodwillAcquiredDuringPeriod
      - us-gaap_GoodwillTranslationAndPurchaseAccountingAdjustments
      - us-gaap_Goodwill

### http://www.google.com/role/CommitmentsandContingenciesNarrativeDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_LossContingenciesTable
    - us-gaap_LossContingenciesByNatureOfContingencyAxis
      - us-gaap_LossContingencyNatureDomain
    - us-gaap_LossContingenciesLineItems
      - us-gaap_PurchaseObligation
      - us-gaap_LossContingencyLossInPeriod
      - us-gaap_LossContingencyAccrualPayments
      - goog_LossContingencyLossInPeriodAdjustment
      - goog_LossContingencyLossInPeriodValueAnnulled
      - goog_NumberOfOpenInvestigations

### http://www.google.com/role/SubsequentEventDetails

- us-gaap_SubsequentEventsAbstract
  - us-gaap_SubsequentEventTable
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - us-gaap_SubsequentEventLineItems
      - us-gaap_EquitySecuritiesFvNiAndWithoutReadilyDeterminableFairValue
      - goog_EquitySecuritiesWithoutReadilyDeterminableFairValueFVNIUnrealizedGainLoss

### http://www.google.com/role/ScheduleIIValuationandQualifyingAccountsDetails

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

