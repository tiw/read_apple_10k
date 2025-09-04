# GOOGL 2023 财务关系分析

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
    - us-gaap_OtherComprehensiveIncomeLossNetOfTax [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.google.com/role/CONSOLIDATEDSTATEMENTSOFCOMPREHENSIVEINCOMEParenthetical

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesTax
  - us-gaap_OtherComprehensiveIncomeLossCashFlowHedgeGainLossAfterReclassificationTax

### http://www.google.com/role/CONSOLIDATEDSTATEMENTSOFCASHFLOWS

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - goog_DepreciationAndImpairmentOnDispositionOfPropertyAndEquipment
  - goog_AmortizationAndImpairmentOfIntangibleAssets
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
  - us-gaap_SummaryOfIncomeTaxContingenciesTextBlock

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
  - us-gaap_RevenueRemainingPerformanceObligation
  - us-gaap_ContractWithCustomerLiability
  - us-gaap_ContractWithCustomerLiabilityRevenueRecognized
  - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionTable
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionLineItems
      - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionPeriod1
      - us-gaap_RevenueRemainingPerformanceObligationPercentage

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
  - us-gaap_InterestExpense
  - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
  - us-gaap_DebtSecuritiesRealizedGainLoss
  - us-gaap_EquitySecuritiesFvNiGainLoss
  - goog_InvestmentPerformanceFees
  - goog_IncomeLossFromEquityMethodInvestmentsAndOtherThanTemporaryImpairmentNet
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_NonoperatingIncomeExpense [totalLabel]
  - us-gaap_InterestCostsCapitalized

### http://www.google.com/role/GoodwillandOtherIntangibleAssetsExpectedAmortizationExpenseforAcquisitionRelatedIntangibleAssetsDetails

- us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.google.com/role/NetIncomePerShareScheduleofEarningsPerShareDetails

- us-gaap_EarningsPerShareAbstract
  - goog_EarningsPerShareDisclosureTable
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
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
    - goog_EffectiveIncomeTaxRateReconciliationTaxCutsAndJobsActForeignDerivedIntangibleIncomeDeductionPercent
    - us-gaap_EffectiveIncomeTaxRateReconciliationNondeductibleExpenseShareBasedCompensationCost
    - us-gaap_EffectiveIncomeTaxRateReconciliationTaxCreditsResearch
    - us-gaap_EffectiveIncomeTaxRateReconciliationChangeInDeferredTaxAssetsValuationAllowance
    - us-gaap_EffectiveIncomeTaxRateReconciliationStateAndLocalIncomeTaxes
    - us-gaap_EffectiveIncomeTaxRateReconciliationOtherAdjustments
    - us-gaap_EffectiveIncomeTaxRateContinuingOperations [totalLabel]

### http://www.google.com/role/IncomeTaxesNarrativeDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - goog_IncomeTaxesTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_TaxCreditCarryforwardAxis
      - us-gaap_TaxCreditCarryforwardNameDomain
    - goog_IncomeTaxesLineItems
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_TaxCreditCarryforwardAmount
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - goog_NumberOfTaxJurisdictions
      - us-gaap_DecreaseInUnrecognizedTaxBenefitsIsReasonablyPossible

### http://www.google.com/role/IncomeTaxesSignificantComponentsofDeferredTaxAssetsandLiabilitiesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
    - us-gaap_DeferredTaxAssetsNetAbstract
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
    - us-gaap_DeferredTaxLiabilities
    - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]

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
    - us-gaap_LossContingenciesByNatureOfContingencyAxis
      - us-gaap_LossContingencyNatureDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_GainLossOnOilAndGasHedgingActivity
      - us-gaap_OperatingIncomeLoss
      - us-gaap_LossContingencyLossInPeriod

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
      - us-gaap_InventoryNet
      - us-gaap_OtherAssetsCurrent
      - us-gaap_AssetsCurrent [totalLabel]
    - us-gaap_OtherLongTermInvestments
    - us-gaap_DeferredIncomeTaxAssetsNet
    - us-gaap_PropertyPlantAndEquipmentNet
    - us-gaap_OperatingLeaseRightOfUseAsset
    - us-gaap_IntangibleAssetsNetExcludingGoodwill
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
    - us-gaap_ContractWithCustomerLiabilityNoncurrent
    - us-gaap_AccruedIncomeTaxesNoncurrent
    - us-gaap_DeferredIncomeTaxLiabilitiesNet
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
  - us-gaap_CommonStockSharesAuthorized

### http://www.google.com/role/CONSOLIDATEDBALANCESHEETSParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_StatementLineItems
      - us-gaap_PreferredStockParOrStatedValuePerShare
      - us-gaap_PreferredStockSharesAuthorized
      - us-gaap_PreferredStockSharesIssued
      - us-gaap_PreferredStockSharesOutstanding
      - us-gaap_CommonStockParOrStatedValuePerShare
      - us-gaap_CommonStockSharesAuthorized
      - us-gaap_CommonStockSharesIssued
      - us-gaap_CommonStockSharesOutstanding

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
  - us-gaap_NoncontrollingInterestIncreaseFromSaleOfParentEquityInterest
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTax
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
    - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
    - us-gaap_RepaymentsOfDebtAndCapitalLeaseObligations
    - us-gaap_ProceedsFromMinorityShareholders
    - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
  - us-gaap_EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect [totalLabel]
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
  - us-gaap_SupplementalCashFlowInformationAbstract
    - us-gaap_IncomeTaxesPaidNet

### http://www.google.com/role/Acquisitions

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_BusinessCombinationDisclosureTextBlock

### http://www.google.com/role/GoodwillandOtherIntangibleAssets

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillAndIntangibleAssetsDisclosureTextBlock

### http://www.google.com/role/StockholdersEquity

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.google.com/role/AcquisitionsTables

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfRecognizedIdentifiedAssetsAcquiredAndLiabilitiesAssumedTableTextBlock
  - us-gaap_FiniteLivedAndIndefiniteLivedIntangibleAssetsAcquiredAsPartOfBusinessCombinationTableTextBlock

### http://www.google.com/role/GoodwillandOtherIntangibleAssetsTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfIntangibleAssetsAndGoodwillTableTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

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

### http://www.google.com/role/FinancialInstrumentsGainsandLossesonEquitySecuritiesDetails

- us-gaap_EquitySecuritiesFvNiGainLossAlternativeAbstract
  - us-gaap_EquitySecuritiesFvNiRealizedGainLoss
  - us-gaap_EquitySecuritiesFvNiUnrealizedGainLoss
  - us-gaap_EquitySecuritiesFvNiGainLoss [totalLabel]

### http://www.google.com/role/FinancialInstrumentsCarryingAmountofEquitySecuritiesDetails

- us-gaap_EquitySecuritiesFvNiGainLossAbstract
  - goog_EquitySecuritiesFVNIAndWithoutReadilyDeterminableFairValueCost [totalLabel]
  - goog_EquitySecuritiesFVNIAndWithoutReadilyDeterminableFairValueAccumulatedGrossUnrealizedGainLossBeforeTax [totalLabel]
  - us-gaap_EquitySecuritiesFvNiAndWithoutReadilyDeterminableFairValue [totalLabel]
- goog_NonMarketableEquitySecuritiesAbstract
  - goog_EquitySecuritiesWithoutReadilyDeterminableFairValueCost
  - goog_EquitySecuritiesWithoutReadilyDeterminableFairValueAccumulatedGrossUnrealizedGainLossBeforeTax
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueAmount [totalLabel]

### http://www.google.com/role/FinancialInstrumentsMeasurementAlternativeInvestmentsDetails

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
  - us-gaap_DerivativeLiabilityStatementOfFinancialPositionExtensibleEnumeration
  - us-gaap_DerivativeAssetStatementOfFinancialPositionExtensibleEnumeration

### http://www.google.com/role/AcquisitionsNarrativeDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable

### http://www.google.com/role/AcquisitionsPurchasePriceAllocationDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable

### http://www.google.com/role/AcquisitionsIntangibleAssetsAcquiredDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.google.com/role/GoodwillandOtherIntangibleAssetsChangesinCarryingAmountofGoodwillDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_GoodwillLineItems
      - us-gaap_GoodwillRollForward

### http://www.google.com/role/GoodwillandOtherIntangibleAssetsAcquisitionRelatedIntangibleAssetsthatarebeingAmortizedDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetByMajorClassTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_AcquiredFiniteLivedIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]
      - us-gaap_IntangibleAssetsGrossExcludingGoodwill
      - us-gaap_IntangibleAssetsNetExcludingGoodwill [totalLabel]
  - us-gaap_IndefiniteLivedIntangibleAssetsExcludingGoodwill

### http://www.google.com/role/GoodwillandOtherIntangibleAssetsNarrativeDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife
      - goog_IntangibleAssetsWriteOffDuringThePeriod
      - us-gaap_AmortizationOfIntangibleAssets

### http://www.google.com/role/GoodwillandOtherIntangibleAssetsExpectedAmortizationExpenseforAcquisitionRelatedIntangibleAssetsDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract

### http://www.google.com/role/StockholdersEquityNarrativeDetails

- us-gaap_EquityAbstract
  - goog_StockholdersEquityNoteTable
    - us-gaap_StatementClassOfStockAxis
    - us-gaap_ShareRepurchaseProgramAxis
    - goog_StockholdersEquityNoteLineItems
      - goog_NumberOfClassesOfCommonStock
      - goog_CommonStockNumberOfVotes
      - us-gaap_StockholdersEquityNoteStockSplitConversionRatio1
      - us-gaap_StockRepurchaseProgramAuthorizedAmount1
      - us-gaap_StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1

### http://www.google.com/role/StockholdersEquityShareRepurchasesDetails

- us-gaap_EquityAbstract
  - goog_StockholdersEquityNoteTable
    - us-gaap_ShareRepurchaseProgramAxis
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
  - us-gaap_OperatingLeasePayments
  - us-gaap_RightOfUseAssetObtainedInExchangeForOperatingLeaseLiability

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
    - us-gaap_CommonClassBMember
    - goog_CapitalClassCMember

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

### http://www.google.com/role/SummaryofSignificantAccountingPoliciesNarrativeDetails

- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - goog_CapitalClassAMember
    - goog_CapitalClassBMember
    - goog_CapitalClassCMember

### http://www.google.com/role/FinancialInstrumentsGainsandLossesonEquitySecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_EquitySecuritiesFvNiGainLossAlternativeAbstract

### http://www.google.com/role/FinancialInstrumentsCarryingAmountofEquitySecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - goog_ProceedsFromSaleOfEquitySecuritiesFVNIHeldForInvestment
  - goog_EquitySecuritiesFVNICostBasisOfSecuritiesSold
  - goog_EquitySecuritiesFVNICumulativeGainLossNet
  - us-gaap_MarketableSecuritiesAbstract
    - us-gaap_EquitySecuritiesFvNiCost
    - goog_EquitySecuritiesFVNIAccumulatedGrossUnrealizedGainLossBeforeTax
    - us-gaap_EquitySecuritiesFvNi [totalLabel]
  - goog_NonMarketableEquitySecuritiesAbstract
  - us-gaap_EquitySecuritiesFvNiGainLossAbstract
  - goog_EquitySecuritiesFVNICumulativeGainLossOfSecuritiesSold
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentCumulativeAmount
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueDownwardPriceAdjustmentCumulativeAmount
  - goog_NonMarketableSecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustment
  - goog_NonMarketableSecuritiesWithoutReadilyDeterminableFairValueDownwordPriceAdjustment

### http://www.google.com/role/StockholdersEquityNarrativeDetails

- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - us-gaap_CommonClassAMember
    - us-gaap_CommonClassBMember
    - goog_CapitalClassCMember
    - goog_CapitalClassAAndCMember
- us-gaap_ShareRepurchaseProgramAxis
  - us-gaap_ShareRepurchaseProgramDomain
    - goog_ShareRepurchaseProgramMember

### http://www.google.com/role/StockholdersEquityShareRepurchasesDetails

- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - goog_CapitalClassAMember
    - goog_CapitalClassCMember
- us-gaap_ShareRepurchaseProgramAxis
  - us-gaap_ShareRepurchaseProgramDomain
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

### http://www.google.com/role/VariableInterestEntities

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_VariableInterestEntityDisclosureTextBlock

### http://www.google.com/role/Debt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.google.com/role/SupplementalFinancialStatementInformation

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_SupplementalBalanceSheetDisclosuresTextBlock

### http://www.google.com/role/Commitmentsandcontingencies

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
  - goog_ImpairmentOfMarketableAndNonMarketableSecuritiesPolicyPolicyTextBlock
  - us-gaap_ReceivablesPolicyTextBlock
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_ConsolidationVariableInterestEntityPolicy
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_LesseeLeasesPolicyTextBlock
  - goog_LongLivedAssetsPolicyPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_BusinessCombinationsPolicy
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_PriorPeriodReclassificationAdjustmentDescription

### http://www.google.com/role/FinancialInstrumentsTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_MarketableSecuritiesTextBlock
  - us-gaap_DebtSecuritiesAvailableForSaleTableTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock
  - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPositionFairValueTableTextBlock
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
  - goog_SupplementalCashFlowInformationTableTextBlock
  - us-gaap_LesseeOperatingLeaseLiabilityMaturityTableTextBlock

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

### http://www.google.com/role/SummaryofSignificantAccountingPoliciesNarrativeDetails

- us-gaap_AccountingPoliciesAbstract
  - goog_OrganizationAndSummaryOfSignificantAccountingPoliciesTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_StatementClassOfStockAxis
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - goog_OrganizationAndSummaryOfSignificantAccountingPoliciesLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_StockholdersEquityNoteStockSplitConversionRatio1
      - us-gaap_CommonStockParOrStatedValuePerShare
      - us-gaap_NetIncomeLoss
      - us-gaap_EarningsPerShareBasic
      - us-gaap_EarningsPerShareDiluted
      - us-gaap_MarketingAndAdvertisingExpense
      - us-gaap_AllowanceForDoubtfulAccountsReceivable
      - us-gaap_GoodwillImpairmentLoss
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife

### http://www.google.com/role/FinancialInstrumentsNarrativeDetails

- us-gaap_FairValueDisclosuresAbstract
  - goog_FinancialInstrumentsAndFairValueTable
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_ValuationTechniqueAxis
      - us-gaap_ValuationTechniqueDomain
    - goog_FinancialInstrumentsAndFairValueLineItems
      - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueAmount
      - us-gaap_DebtSecuritiesAvailableForSaleRealizedGain
      - us-gaap_DebtSecuritiesAvailableForSaleRealizedLoss
      - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentCumulativeAmount
      - us-gaap_EquityMethodInvestments
      - us-gaap_DerivativeNotionalAmount
      - us-gaap_DerivativeRemainingMaturity1
      - us-gaap_ForeignCurrencyCashFlowHedgeGainLossToBeReclassifiedDuringNext12Months

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

### http://www.google.com/role/FinancialInstrumentsContractualMaturityDateofMarketableDebtSecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterFiveThroughTenYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterTenYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtSecurities [totalLabel]

### http://www.google.com/role/FinancialInstrumentsMeasurementAlternativeInvestmentsDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_EquitySecuritiesFvNiGainLossAlternativeAbstract

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

### http://www.google.com/role/FinancialInstrumentsSummaryofgainsandlossesforDebtSecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - goog_FairValueOptionDebtSecuritiesAvailableForSaleUnrealizedGainLoss
  - us-gaap_DebtSecuritiesAvailableForSaleRealizedGain
  - us-gaap_DebtSecuritiesAvailableForSaleRealizedLoss
  - us-gaap_DebtSecuritiesAvailableForSaleAllowanceForCreditLossPeriodIncreaseDecrease
  - us-gaap_DebtSecuritiesAvailableForSaleGainLoss [totalLabel]
  - goog_FairValueOptionDebtSecuritiesAvailableForSaleAccumulatedUnrealizedGainLoss

### http://www.google.com/role/LeasesComponentsofOperatingLeaseExpenseDetails

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeaseCost
  - us-gaap_VariableLeaseCost
  - us-gaap_LeaseCost [totalLabel]

### http://www.google.com/role/LeasesNarrativeDetails

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_LesseeLeaseDescriptionLineItems
      - us-gaap_OperatingLeaseWeightedAverageRemainingLeaseTerm1
      - us-gaap_OperatingLeaseWeightedAverageDiscountRatePercent
      - goog_LesseeLeaseNotYetCommencedCurrentAmount
      - goog_LesseeLeaseNotYetCommencedNoncurrentAmount
      - us-gaap_LesseeOperatingLeaseLeaseNotYetCommencedTermOfContract1
      - us-gaap_LesseeFinanceLeaseLeaseNotYetCommencedTermOfContract1

### http://www.google.com/role/LeasesFutureMinimumLeasePaymentsDetails

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeaseLiabilitiesPaymentsDueAbstract

### http://www.google.com/role/VariableInterestEntitiesNarrativeDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTable
    - srt_ConsolidatedEntitiesAxis
      - srt_ConsolidatedEntitiesDomain
    - us-gaap_PledgedStatusAxis
      - us-gaap_PledgedStatusDomain
    - us-gaap_RecourseStatusAxis
      - us-gaap_RecourseStatusDomain
    - us-gaap_VariableInterestEntityLineItems
      - us-gaap_Assets
      - us-gaap_Liabilities
      - us-gaap_NoncontrollingInterestInVariableInterestEntity
      - goog_RedeemableNoncontrollingInterestInVariableInterestEntity
      - goog_UnconsolidatedVariableInterestEntityCarryingValue
      - us-gaap_VariableInterestEntityEntityMaximumLossExposureAmount

### http://www.google.com/role/DebtNarrativeDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_ShortTermDebtTypeAxis
      - us-gaap_ShortTermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - goog_ShortTermDebtMaximumBorrowingCapacity
      - us-gaap_CommercialPaper
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
      - us-gaap_FinanceLeaseLiabilityStatementOfFinancialPositionExtensibleList

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

### http://www.google.com/role/SupplementalFinancialStatementInformationPropertyandEquipmentDetails

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentNetAbstract

### http://www.google.com/role/SupplementalFinancialStatementInformationAccruedExpensesandOtherCurrentLiabilitiesDetails

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_LossContingencyAccrualCarryingValueCurrent
  - goog_AccruedCustomerLiabilitiesCurrent
  - goog_AccruedPurchasesOfPropertyAndEquipmentCurrent
  - us-gaap_OperatingLeaseLiabilityCurrent
  - us-gaap_OtherAccruedLiabilitiesCurrent
  - us-gaap_AccruedLiabilitiesCurrent [totalLabel]
  - us-gaap_OperatingLeaseLiabilityCurrentStatementOfFinancialPositionExtensibleList

### http://www.google.com/role/AcquisitionsNarrativeDetails

- us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
  - us-gaap_BusinessAcquisitionAxis
    - us-gaap_BusinessAcquisitionAcquireeDomain
      - goog_MandiantMember
  - us-gaap_BusinessAcquisitionLineItems
    - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredGoodwillAndLiabilitiesAssumedNet

### http://www.google.com/role/AcquisitionsPurchasePriceAllocationDetails

- us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
  - us-gaap_BusinessAcquisitionAxis
    - us-gaap_BusinessAcquisitionAcquireeDomain
      - goog_MandiantMember
  - us-gaap_BusinessAcquisitionLineItems
    - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles
    - us-gaap_Goodwill
    - goog_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedOtherAssets
    - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredGoodwillAndLiabilitiesAssumedNet [totalLabel]
    - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCashAndEquivalents

### http://www.google.com/role/CommitmentsandcontingenciesNarrativeDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_LossContingenciesTable
    - us-gaap_LossContingenciesByNatureOfContingencyAxis
      - us-gaap_LossContingencyNatureDomain
    - us-gaap_LossContingenciesLineItems
      - us-gaap_PurchaseObligation
      - us-gaap_LossContingencyLossInPeriod
      - goog_LossContingencyLossInPeriodAdjustment

### http://www.google.com/role/SubsequentEventDetails

- us-gaap_SubsequentEventsAbstract
  - us-gaap_SubsequentEventTable
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - srt_StatementScenarioAxis
      - srt_ScenarioUnspecifiedDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_RestructuringCostAndReserveAxis
      - us-gaap_TypeOfRestructuringDomain
    - us-gaap_SubsequentEventLineItems
      - us-gaap_RestructuringAndRelatedCostNumberOfPositionsEliminated
      - us-gaap_RestructuringAndRelatedCostExpectedCost1

### http://www.google.com/role/ScheduleIIValuationandQualifyingAccountsDetails

- srt_ValuationAndQualifyingAccountsAbstract
  - srt_ValuationAndQualifyingAccountsDisclosureTable
    - us-gaap_ValuationAllowancesAndReservesTypeAxis
      - us-gaap_ValuationAllowancesAndReservesDomain
    - srt_ValuationAndQualifyingAccountsDisclosureLineItems
      - us-gaap_MovementInValuationAllowancesAndReservesRollForward

