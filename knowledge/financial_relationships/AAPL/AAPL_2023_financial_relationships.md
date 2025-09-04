# AAPL 2023 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.apple.com/role/CONSOLIDATEDSTATEMENTSOFOPERATIONS

- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
- us-gaap_OperatingExpensesAbstract
  - us-gaap_ResearchAndDevelopmentExpense
  - us-gaap_SellingGeneralAndAdministrativeExpense
  - us-gaap_OperatingExpenses [totalLabel]

### http://www.apple.com/role/CONSOLIDATEDSTATEMENTSOFCOMPREHENSIVEINCOME

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_ComprehensiveIncomeNetOfTaxAbstract
    - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
    - us-gaap_OtherComprehensiveIncomeDerivativesQualifyingAsHedgesNetOfTaxPeriodIncreaseDecreaseAbstract
      - aapl_OtherComprehensiveIncomeLossDerivativeInstrumentGainLossbeforeReclassificationafterTax
      - aapl_OtherComprehensiveIncomeLossDerivativeInstrumentGainLossReclassificationAfterTax
      - aapl_OtherComprehensiveIncomeLossDerivativeInstrumentGainLossafterReclassificationandTax [totalLabel]
    - us-gaap_OtherComprehensiveIncomeAvailableForSaleSecuritiesAdjustmentNetOfTaxPeriodIncreaseDecreaseAbstract
      - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesAdjustmentNetOfTax [totalLabel]
    - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.apple.com/role/CONSOLIDATEDSTATEMENTSOFCASHFLOWS

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_DepreciationDepletionAndAmortization
  - us-gaap_ShareBasedCompensation
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.apple.com/role/Revenue

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueFromContractWithCustomerTextBlock

### http://www.apple.com/role/EarningsPerShare

- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareTextBlock

### http://www.apple.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.apple.com/role/RevenueTables

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_DisaggregationOfRevenueTableTextBlock

### http://www.apple.com/role/EarningsPerShareTables

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock

### http://www.apple.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfUnrecognizedTaxBenefitsRollForwardTableTextBlock

### http://www.apple.com/role/RevenueAdditionalInformationDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - aapl_PerformanceObligationsinArrangements
  - us-gaap_ContractWithCustomerLiabilityRevenueRecognized
  - us-gaap_ContractWithCustomerLiability

### http://www.apple.com/role/RevenueNetSalesDisaggregatedbySignificantProductsandServicesDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_DisaggregationOfRevenueTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_DisaggregationOfRevenueLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

### http://www.apple.com/role/RevenueDeferredRevenueExpectedTimingofRealizationDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionTable
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionLineItems
      - us-gaap_RevenueRemainingPerformanceObligationPercentage
      - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionPeriod1

### http://www.apple.com/role/EarningsPerShareComputationofBasicandDilutedEarningsPerShareDetails

- us-gaap_EarningsPerShareAbstract
  - us-gaap_NetIncomeLossAbstract
    - us-gaap_NetIncomeLoss
  - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
    - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
    - us-gaap_IncrementalCommonSharesAttributableToShareBasedPaymentArrangements
    - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding [totalLabel]
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.apple.com/role/EarningsPerShareAdditionalInformationDetails

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTable
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareByAntidilutiveSecuritiesAxis
      - us-gaap_AntidilutiveSecuritiesNameDomain
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareLineItems
      - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsOtherIncomeExpenseNetDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_InvestmentIncomeInterestAndDividend
  - us-gaap_InterestExpense
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_NonoperatingIncomeExpense [totalLabel]

### http://www.apple.com/role/IncomeTaxesProvisionforIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_FederalIncomeTaxExpenseBenefitContinuingOperationsAbstract
    - us-gaap_CurrentFederalTaxExpenseBenefit
    - us-gaap_DeferredFederalIncomeTaxExpenseBenefit
    - us-gaap_FederalIncomeTaxExpenseBenefitContinuingOperations [totalLabel]
  - us-gaap_StateAndLocalIncomeTaxExpenseBenefitContinuingOperationsAbstract
    - us-gaap_CurrentStateAndLocalTaxExpenseBenefit
    - us-gaap_DeferredStateAndLocalIncomeTaxExpenseBenefit
    - us-gaap_StateAndLocalIncomeTaxExpenseBenefitContinuingOperations [totalLabel]
  - us-gaap_ForeignIncomeTaxExpenseBenefitContinuingOperationsAbstract
    - us-gaap_CurrentForeignTaxExpenseBenefit
    - us-gaap_DeferredForeignIncomeTaxExpenseBenefit
    - us-gaap_ForeignIncomeTaxExpenseBenefitContinuingOperations [totalLabel]
    - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.apple.com/role/IncomeTaxesAdditionalInformationDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxContingencyTable
    - us-gaap_LossContingenciesByNatureOfContingencyAxis
      - us-gaap_LossContingencyNatureDomain
    - us-gaap_IncomeTaxContingencyLineItems
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
      - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsForeign
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsResearch
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - us-gaap_DecreaseInUnrecognizedTaxBenefitsIsReasonablyPossible
      - aapl_IncomeTaxContingencyNumberOfSubsidiaries
      - us-gaap_LossContingencyEstimateOfPossibleLoss

### http://www.apple.com/role/IncomeTaxesReconciliationofProvisionforIncomeTaxestoAmountComputedbyApplyingtheStatutoryFederalIncomeTaxRatetoIncomeBeforeProvisionforIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
  - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
  - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
  - us-gaap_IncomeTaxReconciliationTaxCreditsResearch
  - us-gaap_EffectiveIncomeTaxRateReconciliationShareBasedCompensationExcessTaxBenefitAmount
  - us-gaap_EffectiveIncomeTaxRateReconciliationFdiiAmount
  - us-gaap_IncomeTaxReconciliationOtherAdjustments
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_EffectiveIncomeTaxRateContinuingOperations

### http://www.apple.com/role/IncomeTaxesSignificantComponentsofDeferredTaxAssetsandLiabilitiesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_DeferredTaxAssetsGrossAbstract
    - us-gaap_DeferredTaxAssetsTaxCreditCarryforwards
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccruals
    - aapl_DeferredTaxAssetsCapitalizedResearchAndDevelopment
    - us-gaap_DeferredTaxAssetsDeferredIncome
    - us-gaap_DeferredTaxAssetsOtherComprehensiveLoss
    - aapl_DeferredTaxAssetsLeaseLiabilities
    - us-gaap_DeferredTaxAssetsOther
    - us-gaap_DeferredTaxAssetsGross [totalLabel]
    - us-gaap_DeferredTaxAssetsValuationAllowance
    - us-gaap_DeferredTaxAssetsNet [totalLabel]
  - us-gaap_DeferredTaxLiabilitiesAbstract
    - us-gaap_DeferredTaxLiabilitiesLeasingArrangements
    - us-gaap_DeferredTaxLiabilitiesPropertyPlantAndEquipment
    - aapl_DeferredTaxLiabilitiesMinimumTaxonForeignEarnings
    - us-gaap_DeferredTaxLiabilitiesOtherComprehensiveIncome
    - us-gaap_DeferredTaxLiabilitiesOther
    - us-gaap_DeferredIncomeTaxLiabilities [totalLabel]
  - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]

### http://www.apple.com/role/IncomeTaxesAggregateChangesinGrossUnrecognizedTaxBenefitsDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ReconciliationOfUnrecognizedTaxBenefitsExcludingAmountsPertainingToExaminedTaxReturnsRollForward
    - us-gaap_UnrecognizedTaxBenefits
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
    - us-gaap_UnrecognizedTaxBenefitsReductionsResultingFromLapseOfApplicableStatuteOfLimitations
    - us-gaap_UnrecognizedTaxBenefits

### http://www.apple.com/role/ShareBasedCompensationSummaryofShareBasedCompensationExpenseandtheRelatedIncomeTaxBenefitDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_AllocatedShareBasedCompensationExpense
  - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense

### http://www.apple.com/role/SegmentInformationandGeographicDataReconciliationofSegmentOperatingIncometotheConsolidatedStatementsofOperationsDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTable
    - srt_ConsolidationItemsAxis
      - srt_ConsolidationItemsDomain
    - us-gaap_SegmentReportingReconcilingItemForOperatingProfitLossFromSegmentToConsolidatedLineItems
      - us-gaap_OperatingIncomeLoss
      - us-gaap_ResearchAndDevelopmentExpense
      - us-gaap_OtherGeneralAndAdministrativeExpense

### http://www.apple.com/role/SegmentInformationandGeographicDataNetSalesDetails

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - srt_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

### http://www.apple.com/role/SegmentInformationandGeographicDataLongLivedAssetsDetails

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - srt_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

## 资产负债表结构 (Balance Sheet Structure)

### http://www.apple.com/role/CONSOLIDATEDBALANCESHEETS

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_AssetsAbstract
    - us-gaap_AssetsCurrentAbstract
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_MarketableSecuritiesCurrent
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_NontradeReceivablesCurrent
      - us-gaap_InventoryNet
      - us-gaap_OtherAssetsCurrent
      - us-gaap_AssetsCurrent [totalLabel]
    - us-gaap_AssetsNoncurrentAbstract
      - us-gaap_MarketableSecuritiesNoncurrent
      - us-gaap_PropertyPlantAndEquipmentNet
      - us-gaap_OtherAssetsNoncurrent
      - us-gaap_AssetsNoncurrent [totalLabel]
    - us-gaap_Assets [totalLabel]
  - us-gaap_LiabilitiesAndStockholdersEquityAbstract
    - us-gaap_LiabilitiesCurrentAbstract
      - us-gaap_AccountsPayableCurrent
      - us-gaap_OtherLiabilitiesCurrent
      - us-gaap_ContractWithCustomerLiabilityCurrent
      - us-gaap_CommercialPaper
      - us-gaap_LongTermDebtCurrent
      - us-gaap_LiabilitiesCurrent [totalLabel]
    - us-gaap_LiabilitiesNoncurrentAbstract
      - us-gaap_LongTermDebtNoncurrent
      - us-gaap_OtherLiabilitiesNoncurrent
      - us-gaap_LiabilitiesNoncurrent [totalLabel]
    - us-gaap_Liabilities [totalLabel]
    - us-gaap_CommitmentsAndContingencies
    - us-gaap_CommonStockSharesOutstanding
    - us-gaap_CommonStockSharesIssued
    - us-gaap_StockholdersEquityAbstract
      - us-gaap_CommonStocksIncludingAdditionalPaidInCapital
      - us-gaap_RetainedEarningsAccumulatedDeficit
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
      - us-gaap_StockholdersEquity [totalLabel]
    - us-gaap_LiabilitiesAndStockholdersEquity [totalLabel]

### http://www.apple.com/role/CONSOLIDATEDBALANCESHEETSParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_CommonStockParOrStatedValuePerShare
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_CommonStockSharesIssued
  - us-gaap_CommonStockSharesOutstanding

### http://www.apple.com/role/CONSOLIDATEDSTATEMENTSOFSHAREHOLDERSEQUITY

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockIncludingAdditionalPaidInCapitalMember
    - us-gaap_RetainedEarningsMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_StockholdersEquity
  - us-gaap_StockIssuedDuringPeriodValueNewIssues
  - us-gaap_AdjustmentsRelatedToTaxWithholdingForShareBasedCompensation
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
  - us-gaap_NetIncomeLoss
  - us-gaap_Dividends
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent
  - us-gaap_StockholdersEquity
- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable

### http://www.apple.com/role/CONSOLIDATEDSTATEMENTSOFCASHFLOWS

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperationsAbstract
    - us-gaap_NetIncomeLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperationsAbstract
    - us-gaap_PaymentsToAcquireAvailableForSaleSecuritiesDebt
    - us-gaap_ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities
    - us-gaap_ProceedsFromSaleOfAvailableForSaleSecuritiesDebt
    - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
    - us-gaap_PaymentsForProceedsFromOtherInvestingActivities
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperationsAbstract
    - us-gaap_PaymentsRelatedToTaxWithholdingForShareBasedCompensation
    - us-gaap_PaymentsOfDividends
    - us-gaap_PaymentsForRepurchaseOfCommonStock
    - us-gaap_ProceedsFromIssuanceOfLongTermDebt
    - us-gaap_RepaymentsOfLongTermDebt
    - us-gaap_ProceedsFromRepaymentsOfCommercialPaper
    - us-gaap_ProceedsFromPaymentsForOtherFinancingActivities
    - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect [totalLabel]
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
  - us-gaap_SupplementalCashFlowInformationAbstract
    - us-gaap_IncomeTaxesPaidNet
    - us-gaap_InterestPaidNet

### http://www.apple.com/role/ShareholdersEquity

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.apple.com/role/ShareholdersEquityTables

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfCommonStockOutstandingRollForwardTableTextBlock

### http://www.apple.com/role/FinancialInstrumentsCashCashEquivalentsandMarketableSecuritiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_MarketableSecuritiesTable

### http://www.apple.com/role/FinancialInstrumentsNonCurrentMarketableDebtSecuritiesbyContractualMaturityDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesSingleMaturityDateRollingMaturityAbstract

### http://www.apple.com/role/FinancialInstrumentsGrossFairValuesofDerivativeAssetsandLiabilitiesDetails

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_FairValuesDerivativesBalanceSheetLocationByDerivativeContractTypeByHedgingDesignationTable
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosuresLineItems
      - us-gaap_DerivativeAssetsAbstract
      - us-gaap_DerivativeLiabilitiesAbstract

### http://www.apple.com/role/FinancialInstrumentsDerivativeInstrumentsDesignatedasFairValueHedgesandRelatedHedgedItemsDetails

- us-gaap_HedgedAssetFairValueHedge
  - us-gaap_HedgedAssetStatementOfFinancialPositionExtensibleEnumeration
- us-gaap_HedgedLiabilityFairValueHedge
  - us-gaap_HedgedLiabilityStatementOfFinancialPositionExtensibleEnumeration

### http://www.apple.com/role/PropertyPlantandEquipmentGrossPropertyPlantandEquipmentbyMajorAssetClassandAccumulatedDepreciationDetails

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsOtherNonCurrentAssetsDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_DeferredIncomeTaxAssetsNet
  - us-gaap_OtherAssetsMiscellaneousNoncurrent
  - us-gaap_OtherAssetsNoncurrent [totalLabel]

### http://www.apple.com/role/LeasesROUAssetsandLeaseLiabilitiesDetails

- us-gaap_LeasesAbstract
  - us-gaap_AssetsAndLiabilitiesLesseeAbstract
    - us-gaap_OperatingLeaseRightOfUseAsset
      - us-gaap_OperatingLeaseRightOfUseAssetStatementOfFinancialPositionExtensibleList
    - us-gaap_FinanceLeaseRightOfUseAsset
      - us-gaap_FinanceLeaseRightOfUseAssetStatementOfFinancialPositionExtensibleList
    - aapl_OperatingandFinanceLeaseRightofUseAsset [totalLabel]
    - us-gaap_OperatingLeaseLiabilityCurrent
      - us-gaap_OperatingLeaseLiabilityCurrentStatementOfFinancialPositionExtensibleList
    - us-gaap_OperatingLeaseLiabilityNoncurrent
      - us-gaap_OperatingLeaseLiabilityNoncurrentStatementOfFinancialPositionExtensibleList
    - us-gaap_FinanceLeaseLiabilityCurrent
      - us-gaap_FinanceLeaseLiabilityCurrentStatementOfFinancialPositionExtensibleList
    - us-gaap_FinanceLeaseLiabilityNoncurrent
      - us-gaap_FinanceLeaseLiabilityNoncurrentStatementOfFinancialPositionExtensibleList
    - aapl_OperatingandFinanceLeaseLiability [totalLabel]

### http://www.apple.com/role/LeasesLeaseLiabilityMaturitiesDetails

- us-gaap_LeasesAbstract
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
  - aapl_LesseeOperatingandFinanceLeaseLiabilityPaymentDueAbstract
    - aapl_LesseeOperatingAndFinanceLeaseLiabilityToBePaidYearOne [totalLabel]
    - aapl_LesseeOperatingAndFinanceLeaseLiabilityToBePaidYearTwo [totalLabel]
    - aapl_LesseeOperatingAndFinanceLeaseLiabilityToBePaidYearThree [totalLabel]
    - aapl_LesseeOperatingAndFinanceLeaseLiabilityToBePaidYearFour [totalLabel]
    - aapl_LesseeOperatingAndFinanceLeaseLiabilityToBePaidYearFive [totalLabel]
    - aapl_LesseeOperatingAndFinanceLeaseLiabilityToBePaidAfterYearFive [totalLabel]
    - aapl_LesseeOperatingAndFinanceLeaseLiabilityToBePaid [totalLabel]
    - aapl_LesseeOperatingandFinanceLeaseLiabilityUndiscountedExcessAmount
    - aapl_OperatingandFinanceLeaseLiability [totalLabel]

### http://www.apple.com/role/ShareholdersEquityAdditionalInformationDetails

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteAbstract
    - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
    - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue

### http://www.apple.com/role/ShareholdersEquitySharesofCommonStockDetails

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
  - aapl_StockIssuedDuringPeriodSharesSharebasedPaymentArrangementNetofSharesWithheldforTaxes
  - us-gaap_CommonStockSharesOutstanding
- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable

### http://www.apple.com/role/ShareBasedCompensationRestrictedStockUnitActivityandRelatedInformationDetails

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
- us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsAggregateIntrinsicValueAbstract
  - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsAggregateIntrinsicValueNonvested

### http://www.apple.com/role/SegmentInformationandGeographicDataLongLivedAssetsDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - country_CN
    - aapl_OtherCountriesMember

## 现金流量表结构 (Cash Flow Structure)

### http://www.apple.com/role/CONSOLIDATEDSTATEMENTSOFCASHFLOWS

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInOtherReceivables
  - us-gaap_IncreaseDecreaseInInventories
  - us-gaap_IncreaseDecreaseInOtherOperatingAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInOtherOperatingLiabilities

### http://www.apple.com/role/FinancialInstrumentsCashCashEquivalentsandMarketableSecuritiesDetails

- us-gaap_MarketableSecuritiesTable
  - us-gaap_FinancialInstrumentAxis
    - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
      - us-gaap_CashMember
      - us-gaap_MoneyMarketFundsMember
      - us-gaap_EquitySecuritiesMember
      - us-gaap_MutualFundMember
      - us-gaap_USTreasurySecuritiesMember
      - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
      - us-gaap_ForeignGovernmentDebtSecuritiesMember
      - us-gaap_BankTimeDepositsMember
      - us-gaap_CommercialPaperMember
      - us-gaap_CorporateDebtSecuritiesMember
      - us-gaap_USStatesAndPoliticalSubdivisionsMember
      - us-gaap_AssetBackedSecuritiesMember
  - us-gaap_FairValueByFairValueHierarchyLevelAxis
    - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
      - us-gaap_FairValueInputsLevel1Member
      - us-gaap_FairValueInputsLevel2Member
  - us-gaap_MarketableSecuritiesLineItems
    - us-gaap_Cash
    - us-gaap_EquitySecuritiesFvNiCost [totalLabel]
    - aapl_EquitySecuritiesFVNIAccumulatedGrossUnrealizedGainBeforeTax
    - aapl_EquitySecuritiesFVNIAccumulatedGrossUnrealizedLossBeforeTax
    - us-gaap_EquitySecuritiesFvNiCurrentAndNoncurrent [totalLabel]
    - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis [totalLabel]
    - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
    - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
    - us-gaap_AvailableForSaleSecuritiesDebtSecurities [totalLabel]
    - aapl_CashCashEquivalentsAndMarketableSecuritiesCost [totalLabel]
    - aapl_CashEquivalentsAndMarketableSecuritiesAccumulatedGrossUnrealizedGainBeforeTax [totalLabel]
    - aapl_CashEquivalentsAndMarketableSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
    - aapl_CashCashEquivalentsAndMarketableSecurities [totalLabel]
    - us-gaap_CashAndCashEquivalentsAtCarryingValue
    - us-gaap_MarketableSecuritiesCurrent
    - us-gaap_MarketableSecuritiesNoncurrent
    - us-gaap_DebtSecuritiesAvailableForSaleRestricted

### http://www.apple.com/role/DebtSummaryofCashFlowsAssociatedwithCommercialPaperDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInThreeMonthsOrLessAlternativeAbstract
    - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInThreeMonthsOrLess
  - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInMoreThanThreeMonthsAlternativeAbstract
    - us-gaap_ProceedsFromShortTermDebtMaturingInMoreThanThreeMonths
    - us-gaap_RepaymentsOfShortTermDebtMaturingInMoreThanThreeMonths
    - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInMoreThanThreeMonths [totalLabel]
  - us-gaap_ProceedsFromRepaymentsOfCommercialPaper [totalLabel]

## 股东权益结构 (Equity Structure)

### http://www.apple.com/role/CoverPage

- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - us-gaap_CommonStockMember
    - aapl_A1.375NotesDue2024Member
    - aapl_A0.000Notesdue2025Member
    - aapl_A0.875NotesDue2025Member
    - aapl_A1.625NotesDue2026Member
    - aapl_A2.000NotesDue2027Member
    - aapl_A1.375NotesDue2029Member
    - aapl_A3.050NotesDue2029Member
    - aapl_A0.500Notesdue2031Member
    - aapl_A3.600NotesDue2042Member

### http://www.apple.com/role/CONSOLIDATEDSTATEMENTSOFOPERATIONS

- us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding
- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.apple.com/role/CONSOLIDATEDSTATEMENTSOFSHAREHOLDERSEQUITY

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
    - us-gaap_CommonStockDividendsPerShareDeclared

### http://www.apple.com/role/ShareBasedCompensation

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_DisclosureOfCompensationRelatedCostsShareBasedPaymentsTextBlock

### http://www.apple.com/role/ShareBasedCompensationTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfNonvestedRestrictedStockUnitsActivityTableTextBlock
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock

### http://www.apple.com/role/ShareholdersEquitySharesofCommonStockDetails

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward

### http://www.apple.com/role/ShareBasedCompensationAdditionalInformationDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_PlanNameAxis
    - us-gaap_AwardTypeAxis
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - aapl_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNumberOfSharesOfCommonStockIssuedPerUnitUponVesting
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAuthorized
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
      - us-gaap_SharesPaidForTaxWithholdingForShareBasedCompensation
      - us-gaap_PaymentsRelatedToTaxWithholdingForShareBasedCompensation
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
- us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
  - us-gaap_RestrictedStockUnitsRSUMember

### http://www.apple.com/role/ShareBasedCompensationRestrictedStockUnitActivityandRelatedInformationDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsAggregateIntrinsicValueAbstract

### http://xbrl.sec.gov/ecd/role/AwardTimingDisclosure

- us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
  - us-gaap_EmployeeStockOptionMember
  - us-gaap_StockAppreciationRightsSARSMember
  - us-gaap_RestrictedStockUnitsRSUMember

## 其他结构 (Other Structure)

### http://www.apple.com/role/CoverPage

- dei_CoverAbstract
  - dei_EntitiesTable
    - us-gaap_StatementClassOfStockAxis
    - dei_EntityInformationLineItems
      - dei_DocumentType
      - dei_DocumentAnnualReport
      - dei_CurrentFiscalYearEndDate
      - dei_DocumentPeriodEndDate
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
      - dei_NoTradingSymbolFlag
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

### http://www.apple.com/role/AuditorInformation

- aapl_AuditorInformationAbstract
  - dei_AuditorName
  - dei_AuditorLocation
  - dei_AuditorFirmId

### http://www.apple.com/role/CONSOLIDATEDSTATEMENTSOFOPERATIONS

- us-gaap_StatementTable
  - srt_ProductOrServiceAxis
    - srt_ProductsAndServicesDomain
      - us-gaap_ProductMember
      - us-gaap_ServiceMember
  - us-gaap_StatementLineItems
    - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
    - us-gaap_CostOfGoodsAndServicesSold
    - us-gaap_GrossProfit [totalLabel]
    - us-gaap_OperatingExpensesAbstract
    - us-gaap_OperatingIncomeLoss [totalLabel]
    - us-gaap_NonoperatingIncomeExpense
    - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]
    - us-gaap_IncomeTaxExpenseBenefit
    - us-gaap_NetIncomeLoss [totalLabel]
    - us-gaap_EarningsPerShareAbstract
    - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract

### http://www.apple.com/role/SummaryofSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfPresentationAndSignificantAccountingPoliciesTextBlock

### http://www.apple.com/role/FinancialInstruments

- aapl_FinancialInstrumentsAbstract
  - us-gaap_FinancialInstrumentsDisclosureTextBlock

### http://www.apple.com/role/PropertyPlantandEquipment

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.apple.com/role/ConsolidatedFinancialStatementDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_AdditionalFinancialInformationDisclosureTextBlock

### http://www.apple.com/role/Leases

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeasesTextBlock
  - us-gaap_LesseeFinanceLeasesTextBlock

### http://www.apple.com/role/Debt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.apple.com/role/CommitmentsContingenciesandSupplyConcentrations

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.apple.com/role/SegmentInformationandGeographicData

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.apple.com/role/SummaryofSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfAccountingPolicyPolicyTextBlock
  - us-gaap_FiscalPeriod
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - us-gaap_CompensationRelatedCostsPolicyTextBlock
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_MarketableSecuritiesPolicy
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_DerivativesPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_LesseeLeasesPolicyTextBlock
  - us-gaap_FairValueMeasurementPolicyPolicyTextBlock
  - us-gaap_SegmentReportingPolicyPolicyTextBlock

### http://www.apple.com/role/FinancialInstrumentsTables

- aapl_FinancialInstrumentsAbstract
  - us-gaap_ScheduleOfCashCashEquivalentsAndShortTermInvestmentsTableTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock
  - us-gaap_ScheduleOfNotionalAmountsOfOutstandingDerivativePositionsTableTextBlock
  - us-gaap_ScheduleOfDerivativeInstrumentsInStatementOfFinancialPositionFairValueTextBlock
  - us-gaap_ScheduleOfFairValueHedgingInstrumentsStatementsOfFinancialPerformanceAndFinancialPositionLocationTableTextBlock

### http://www.apple.com/role/PropertyPlantandEquipmentTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsTables

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_ScheduleOfOtherAssetsNoncurrentTextBlock
  - us-gaap_OtherCurrentLiabilitiesTableTextBlock
  - us-gaap_OtherNoncurrentLiabilitiesTableTextBlock
  - us-gaap_InterestAndOtherIncomeTableTextBlock

### http://www.apple.com/role/LeasesTables

- us-gaap_LeasesAbstract
  - aapl_OperatingandFinanceLeaseRightofUseAssetsandLeaseLiabilitiesTableTextBlock
  - us-gaap_LesseeOperatingLeaseLiabilityMaturityTableTextBlock
  - us-gaap_FinanceLeaseLiabilityMaturityTableTextBlock

### http://www.apple.com/role/DebtTables

- us-gaap_DebtDisclosureAbstract
  - aapl_CommercialPaperCashFlowSummaryTableTextBlock
  - us-gaap_ScheduleOfDebtInstrumentsTextBlock
  - us-gaap_ScheduleOfMaturitiesOfLongTermDebtTableTextBlock

### http://www.apple.com/role/CommitmentsContingenciesandSupplyConcentrationsTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_UnrecordedUnconditionalPurchaseObligationsDisclosureTextBlock

### http://www.apple.com/role/SegmentInformationandGeographicDataTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
  - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTextBlock
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsByGeographicalAreasTableTextBlock

### http://www.apple.com/role/FinancialInstrumentsNonCurrentMarketableDebtSecuritiesbyContractualMaturityDetails

- us-gaap_AvailableForSaleSecuritiesDebtMaturitiesSingleMaturityDateRollingMaturityAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearTwoThroughFiveFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearSixThroughTenFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingAfterYearTenFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesSingleMaturityDate [totalLabel]

### http://www.apple.com/role/FinancialInstrumentsAdditionalInformationDetails

- aapl_FinancialInstrumentsAbstract
  - aapl_FinancialInstrumentsTable
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - us-gaap_ConcentrationRiskByTypeAxis
      - us-gaap_ConcentrationRiskTypeDomain
    - srt_MajorCustomersAxis
      - srt_NameOfMajorCustomerDomain
    - aapl_FinancialInstrumentsLineItems
      - us-gaap_MaximumLengthOfTimeForeignCurrencyCashFlowHedge
      - us-gaap_FairValueConcentrationOfRiskDerivativeFinancialInstrumentsAssets
      - aapl_DerivativeAssetsReductionForMasterNettingArrangementsIncludingTheEffectsOfCollateral
      - aapl_DerivativeLiabilitiesReductionForMasterNettingArrangementsIncludingTheEffectsOfCollateral
      - us-gaap_DerivativeFairValueOfDerivativeNet
      - aapl_NumberOfCustomersWithSignificantAccountsReceivableBalance
      - us-gaap_ConcentrationRiskPercentage1
      - aapl_NumberOfSignificantVendors

### http://www.apple.com/role/FinancialInstrumentsNotionalAmountsAssociatedwithDerivativeInstrumentsDetails

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_FairValuesDerivativesBalanceSheetLocationByDerivativeContractTypeByHedgingDesignationTable
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativesFairValueLineItems
      - us-gaap_DerivativeNotionalAmount

### http://www.apple.com/role/FinancialInstrumentsDerivativeInstrumentsDesignatedasFairValueHedgesandRelatedHedgedItemsDetails

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_HedgedAssetFairValueHedge
  - us-gaap_HedgedLiabilityFairValueHedge

### http://www.apple.com/role/PropertyPlantandEquipmentAdditionalInformationDetails

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_Depreciation

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsOtherCurrentLiabilitiesDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_AccruedIncomeTaxesCurrent
  - us-gaap_OtherAccruedLiabilitiesCurrent
  - us-gaap_OtherLiabilitiesCurrent [totalLabel]

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsOtherNonCurrentLiabilitiesDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_AccruedIncomeTaxesNoncurrent
  - us-gaap_OtherAccruedLiabilitiesNoncurrent
  - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.apple.com/role/LeasesAdditionalInformationDetails

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_LesseeLeaseDescriptionLineItems
      - aapl_LesseeOperatingandFinanceLeaseTermofContract
      - us-gaap_OperatingLeaseCost
      - us-gaap_VariableLeaseCost
      - us-gaap_OperatingLeasePayments
      - aapl_RightofUseAssetsObtainedinExchangeforOperatingandFinanceLeaseLiabilities
      - aapl_OperatingandFinanceLeaseWeightedAverageRemainingLeaseTerm
      - aapl_OperatingandFinanceLeaseWeightedAverageDiscountRatePercent
      - aapl_LesseeOperatingAndFinanceLeaseLeaseNotYetCommencedPaymentsDue
      - aapl_LesseeOperatingAndFinanceLeaseLeaseNotYetCommencedTermOfContract

### http://www.apple.com/role/DebtAdditionalInformationDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_ShortTermDebtTypeAxis
      - us-gaap_ShortTermDebtTypeDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_CommercialPaper
      - us-gaap_DebtInstrumentTerm
      - us-gaap_ShortTermDebtWeightedAverageInterestRate
      - us-gaap_InterestCostsIncurred
      - us-gaap_LongTermDebtFairValue

### http://www.apple.com/role/DebtSummaryofTermDebtDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_DebtInstrumentUnamortizedDiscountPremiumAndDebtIssuanceCostsNet
      - aapl_HedgeAccountingAdjustmentsRelatedToLongTermDebt
      - us-gaap_LongTermDebt [totalLabel]
      - us-gaap_LongTermDebtCurrent
      - us-gaap_LongTermDebtNoncurrent
      - aapl_DebtInstrumentMaturityYearRangeStart
      - aapl_DebtInstrumentMaturityYearRangeEnd
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage

### http://www.apple.com/role/DebtFuturePrincipalPaymentsforTermDebtDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive
  - us-gaap_DebtInstrumentCarryingAmount [totalLabel]

### http://www.apple.com/role/ShareBasedCompensationAdditionalInformationDetails

- us-gaap_PlanNameAxis
  - us-gaap_PlanNameDomain
    - aapl_EmployeeStockPlan2022PlanMember
- us-gaap_AwardTypeAxis
  - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain

### http://www.apple.com/role/CommitmentsContingenciesandSupplyConcentrationsFuturePaymentsUnderUnconditionalPurchaseObligationsDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_UnrecordedUnconditionalPurchaseObligationAbstract
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnFirstAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnSecondAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnThirdAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnFourthAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnFifthAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationDueAfterFiveYears
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceSheetAmount [totalLabel]

### http://www.apple.com/role/SegmentInformationandGeographicDataInformationbyReportableSegmentDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_OperatingIncomeLoss

### http://www.apple.com/role/SegmentInformationandGeographicDataNetSalesDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - country_CN
    - aapl_OtherCountriesMember

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
  - ecd_TrdArrDuration
  - ecd_TrdArrSecuritiesAggAvailAmt

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

### http://xbrl.sec.gov/ecd/role/InsiderTradingPoliciesProc

- ecd_InsiderTradingPoliciesProcLineItems
  - ecd_InsiderTrdPoliciesProcAdoptedFlag
  - ecd_InsiderTrdPoliciesProcNotAdoptedTextBlock

