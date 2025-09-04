# AAPL 2019 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.apple.com/role/BenefitPlansSummaryOfShareBasedCompensationExpenseAndRelatedIncomeTaxBenefitDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_AllocatedShareBasedCompensationExpense
  - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense

### http://www.apple.com/role/ComprehensiveIncome

- us-gaap_EquityAbstract
  - us-gaap_ComprehensiveIncomeNoteTextBlock

### http://www.apple.com/role/ComprehensiveIncomeChangeInAociByComponentDetails

- us-gaap_EquityAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossTable
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_AccumulatedOtherComprehensiveIncomeLossLineItems
      - us-gaap_AOCIAttributableToParentNetOfTaxRollForward

### http://www.apple.com/role/ComprehensiveIncomePreTaxAmountsReclassifiedFromAociIntoConsolidatedStatementsOfOperationsDetails

- us-gaap_EquityAbstract
  - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeTable
    - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeAxis
      - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeDomain
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ReclassificationAdjustmentOutOfAccumulatedOtherComprehensiveIncomeLineItems
      - us-gaap_Revenues
      - us-gaap_CostOfGoodsAndServicesSold
      - us-gaap_NonoperatingIncomeExpense
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest

### http://www.apple.com/role/ComprehensiveIncomeTables

- us-gaap_EquityAbstract
  - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeTableTextBlock
  - us-gaap_ScheduleOfAccumulatedOtherComprehensiveIncomeLossTableTextBlock

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsOtherIncomeExpenseNetDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_InvestmentIncomeInterestAndDividend
  - us-gaap_InterestExpense
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_NonoperatingIncomeExpense [totalLabel]

### http://www.apple.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_DepreciationDepletionAndAmortization
  - us-gaap_ShareBasedCompensation
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.apple.com/role/ConsolidatedStatementsOfComprehensiveIncome

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_ComprehensiveIncomeNetOfTaxAbstract
    - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
    - us-gaap_OtherComprehensiveIncomeDerivativesQualifyingAsHedgesNetOfTaxPeriodIncreaseDecreaseAbstract
      - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIOnDerivativesNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossDerivativesQualifyingAsHedgesNetOfTax [totalLabel]
    - us-gaap_OtherComprehensiveIncomeAvailableForSaleSecuritiesAdjustmentNetOfTaxPeriodIncreaseDecreaseAbstract
      - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesAdjustmentNetOfTax [totalLabel]
    - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.apple.com/role/ConsolidatedStatementsOfOperations

- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
- us-gaap_OperatingExpensesAbstract
  - us-gaap_ResearchAndDevelopmentExpense
  - us-gaap_SellingGeneralAndAdministrativeExpense
  - us-gaap_OperatingExpenses [totalLabel]

### http://www.apple.com/role/FinancialInstrumentsPreTaxGainsAndLossesOfDerivativeAndNonDerivativeInstrumentsDesignatedAsHedgesDetails

- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.apple.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.apple.com/role/IncomeTaxesAdditionalInformationDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxContingencyTable
    - us-gaap_LossContingenciesByNatureOfContingencyAxis
      - us-gaap_LossContingencyNatureDomain
    - us-gaap_IncomeTaxContingencyLineItems
      - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
      - aapl_AdjustmentsToAdditionalPaidInCapitalTaxEffectFromShareBasedCompensationIncludingTransferPricing
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - us-gaap_DecreaseInUnrecognizedTaxBenefitsIsReasonablyPossible
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestExpense
      - aapl_IncomeTaxContingencyNumberOfSubsidiaries
      - us-gaap_LossContingencyEstimateOfPossibleLoss
      - aapl_LossContingencyEstimateofPossibleLossReductioninPeriod

### http://www.apple.com/role/IncomeTaxesAggregateChangesInGrossUnrecognizedTaxBenefitsExcludingInterestAndPenaltiesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ReconciliationOfUnrecognizedTaxBenefitsExcludingAmountsPertainingToExaminedTaxReturnsRollForward
    - us-gaap_UnrecognizedTaxBenefits
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
    - us-gaap_UnrecognizedTaxBenefitsReductionsResultingFromLapseOfApplicableStatuteOfLimitations
    - us-gaap_UnrecognizedTaxBenefits

### http://www.apple.com/role/IncomeTaxesProvisionForIncomeTaxesDetails

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

### http://www.apple.com/role/IncomeTaxesReconciliationOfProvisionForIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
  - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
  - us-gaap_EffectiveIncomeTaxRateReconciliationTaxCutsAndJobsActOf2017Amount
  - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
  - us-gaap_IncomeTaxReconciliationTaxCreditsResearch
  - us-gaap_EffectiveIncomeTaxRateReconciliationShareBasedCompensationExcessTaxBenefitAmount
  - us-gaap_IncomeTaxReconciliationOtherAdjustments
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_EffectiveIncomeTaxRateContinuingOperations

### http://www.apple.com/role/IncomeTaxesSignificantComponentsOfDeferredTaxAssetsAndLiabilitiesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_DeferredTaxAssetsGrossAbstract
    - us-gaap_DeferredTaxAssetsGoodwillAndIntangibleAssets
    - us-gaap_DeferredTaxAssetsPropertyPlantAndEquipment
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccruals
    - us-gaap_DeferredTaxAssetsDeferredIncome
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
    - us-gaap_DeferredTaxAssetsUnrealizedLossesOnAvailableforSaleSecuritiesGross
    - us-gaap_DeferredTaxAssetsOther
    - us-gaap_DeferredTaxAssetsNet [totalLabel]
  - us-gaap_DeferredTaxLiabilitiesAbstract
    - aapl_DeferredTaxLiabilitiesMinimumTaxonForeignEarnings
    - us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings
    - us-gaap_DeferredTaxLiabilitiesOther
    - us-gaap_DeferredIncomeTaxLiabilities [totalLabel]
  - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]

### http://www.apple.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_SummaryOfPositionsForWhichSignificantChangeInUnrecognizedTaxBenefitsIsReasonablyPossibleTextBlock

### http://www.apple.com/role/RevenueRecognition

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueFromContractWithCustomerTextBlock

### http://www.apple.com/role/RevenueRecognitionAdditionalInformationDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - aapl_PerformanceObligationsinArrangements
  - us-gaap_ContractWithCustomerLiability

### http://www.apple.com/role/RevenueRecognitionDeferredRevenueExpectedTimingOfRealizationPercentageDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionTable
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionLineItems
      - us-gaap_RevenueRemainingPerformanceObligationPercentage

### http://www.apple.com/role/RevenueRecognitionDeferredRevenueExpectedTimingOfRealizationPeriodDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionTable
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionLineItems
      - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionPeriod1

### http://www.apple.com/role/RevenueRecognitionNetSalesDisaggregatedBySignificantProductsAndServicesDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_DisaggregationOfRevenueTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_DisaggregationOfRevenueLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_ContractWithCustomerLiabilityRevenueRecognized

### http://www.apple.com/role/RevenueRecognitionTables

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_DisaggregationOfRevenueTableTextBlock

### http://www.apple.com/role/SegmentInformationAndGeographicDataLongLivedAssetsDetails

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - srt_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

### http://www.apple.com/role/SegmentInformationAndGeographicDataNetSalesDetails

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - srt_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

### http://www.apple.com/role/SegmentInformationAndGeographicDataReconciliationOfSegmentOperatingIncomeToConsolidatedStatementsOfOperationsDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTable
    - srt_ConsolidationItemsAxis
      - srt_ConsolidationItemsDomain
    - us-gaap_SegmentReportingReconcilingItemForOperatingProfitLossFromSegmentToConsolidatedLineItems
      - us-gaap_OperatingIncomeLoss
      - us-gaap_ResearchAndDevelopmentExpense
      - us-gaap_OtherGeneralAndAdministrativeExpense

### http://www.apple.com/role/SummaryOfSignificantAccountingPoliciesComputationOfBasicAndDilutedEarningsPerShareDetails

- us-gaap_EarningsPerShareAbstract
  - us-gaap_NetIncomeLossAbstract
    - us-gaap_NetIncomeLoss
  - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
    - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
    - us-gaap_WeightedAverageNumberDilutedSharesOutstandingAdjustment
    - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding [totalLabel]
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

## 资产负债表结构 (Balance Sheet Structure)

### http://www.apple.com/role/BenefitPlansRestrictedStockUnitsActivityAndRelatedInformationDetails

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

### http://www.apple.com/role/ConsolidatedBalanceSheets

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_AssetsAbstract
    - us-gaap_AssetsCurrentAbstract
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_MarketableSecuritiesCurrent
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_InventoryNet
      - us-gaap_NontradeReceivablesCurrent
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
    - us-gaap_StockholdersEquityAbstract
      - us-gaap_CommonStocksIncludingAdditionalPaidInCapital
      - us-gaap_RetainedEarningsAccumulatedDeficit
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
      - us-gaap_StockholdersEquity [totalLabel]
    - us-gaap_LiabilitiesAndStockholdersEquity [totalLabel]

### http://www.apple.com/role/ConsolidatedBalanceSheetsParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_CommonStockParOrStatedValuePerShare
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_CommonStockSharesIssued
  - us-gaap_CommonStockSharesOutstanding

### http://www.apple.com/role/ConsolidatedStatementsOfCashFlows

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
    - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
    - us-gaap_PaymentsToAcquireOtherInvestments
    - us-gaap_ProceedsFromSaleAndMaturityOfOtherInvestments
    - us-gaap_PaymentsForProceedsFromOtherInvestingActivities
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperationsAbstract
    - us-gaap_ProceedsFromIssuanceOfCommonStock
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

### http://www.apple.com/role/ConsolidatedStatementsOfShareholdersEquity

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
  - aapl_AdjustmentsToAdditionalPaidInCapitalTaxEffectFromShareBasedCompensationIncludingTransferPricing
  - us-gaap_NetIncomeLoss
  - us-gaap_Dividends
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
  - us-gaap_CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent
  - us-gaap_StockholdersEquity
- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable

### http://www.apple.com/role/FinancialInstrumentsCashCashEquivalentsAndMarketableSecuritiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_ScheduleOfAvailableForSaleSecuritiesTable

### http://www.apple.com/role/FinancialInstrumentsDerivativeInstrumentsAtGrossFairValueDetails

- us-gaap_DerivativeAssetsAbstract
  - us-gaap_DerivativeFairValueOfDerivativeAsset

### http://www.apple.com/role/FinancialInstrumentsMarketableSecuritiesInContinuousUnrealizedLossPositionDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_AvailableForSaleSecuritiesAbstract
    - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPositionLessThan12Months
    - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPosition12MonthsOrLonger
    - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPosition [totalLabel]
  - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionAccumulatedLossAbstract
    - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPositionLessThan12MonthsAccumulatedLoss
    - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPosition12MonthsOrLongerAccumulatedLoss
    - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPositionAccumulatedLoss

### http://www.apple.com/role/FinancialInstrumentsRestrictedCashDetails

- us-gaap_SupplementalCashFlowElementsAbstract
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_RestrictedCashAndCashEquivalentsAtCarryingValue
  - us-gaap_RestrictedCashAndCashEquivalentsNoncurrent
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents [totalLabel]

### http://www.apple.com/role/SegmentInformationAndGeographicDataLongLivedAssetsDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - country_CN
    - aapl_OtherCountriesMember

### http://www.apple.com/role/ShareholdersEquity

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.apple.com/role/ShareholdersEquityAdditionalInformationDetails

- us-gaap_EquityClassOfTreasuryStockLineItems
  - us-gaap_StockRepurchaseProgramAuthorizedAmount1
  - aapl_AmountUtilizedUnderShareRepurchaseProgram
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
  - aapl_UpFrontPaymentUnderAcceleratedShareRepurchaseArrangement
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
- us-gaap_EquityAbstract
  - us-gaap_ClassOfTreasuryStockTable

### http://www.apple.com/role/ShareholdersEquitySharesOfCommonStockDetails

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

### http://www.apple.com/role/ShareholdersEquityTables

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfStockByClassTextBlock

### http://www.apple.com/role/SummaryOfSignificantAccountingPoliciesAdditionalInformationDetails

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_RetainedEarningsMember

## 现金流量表结构 (Cash Flow Structure)

### http://www.apple.com/role/CommitmentsAndContingenciesFutureMinimumLeasePaymentsUnderNoncancelableOperatingLeasesDetails

- us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueCurrent
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInTwoYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInThreeYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFourYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFiveYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueThereafter
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDue [totalLabel]

### http://www.apple.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInInventories
  - us-gaap_IncreaseDecreaseInOtherReceivables
  - us-gaap_IncreaseDecreaseInOtherOperatingAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInContractWithCustomerLiability
  - us-gaap_IncreaseDecreaseInOtherOperatingLiabilities

### http://www.apple.com/role/DebtSummaryOfCashFlowsAssociatedWithCommercialPaperDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInThreeMonthsOrLessAlternativeAbstract
    - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInThreeMonthsOrLess
  - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInMoreThanThreeMonthsAlternativeAbstract
    - us-gaap_ProceedsFromShortTermDebtMaturingInMoreThanThreeMonths
    - us-gaap_RepaymentsOfShortTermDebtMaturingInMoreThanThreeMonths
    - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInMoreThanThreeMonths [totalLabel]
  - us-gaap_ProceedsFromRepaymentsOfCommercialPaper [totalLabel]

### http://www.apple.com/role/FinancialInstrumentsCashCashEquivalentsAndMarketableSecuritiesDetails

- us-gaap_ScheduleOfAvailableForSaleSecuritiesTable
  - us-gaap_FinancialInstrumentAxis
    - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
      - us-gaap_CashMember
      - us-gaap_MoneyMarketFundsMember
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
  - us-gaap_ScheduleOfAvailableForSaleSecuritiesLineItems
    - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis [totalLabel]
    - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
    - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
    - us-gaap_AvailableForSaleSecuritiesDebtSecurities [totalLabel]
    - us-gaap_CashAndCashEquivalentsAtCarryingValue
    - us-gaap_MarketableSecuritiesCurrent
    - us-gaap_MarketableSecuritiesNoncurrent
    - us-gaap_RestrictedInvestments

## 股东权益结构 (Equity Structure)

### http://www.apple.com/role/BenefitPlans

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_CompensationAndEmployeeBenefitPlansTextBlock

### http://www.apple.com/role/BenefitPlansAdditionalInformationDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_PlanNameAxis
    - us-gaap_AwardTypeAxis
    - srt_RangeAxis
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - aapl_SharebasedCompensationArrangementbySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsNumberofSharesofCommonSharesAwardedUponSettlement
      - aapl_FactorByWhichEachRSUGrantedReducesAndEachRSUCanceledOrShareWithheldForTaxesIncreasesSharesAvailableForGrant
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAuthorized
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardPurchasePriceOfCommonStockPercent
      - aapl_ShareBasedCompensationArrangementByShareBasedPaymentAwardOfferingTerm
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardMaximumEmployeeSubscriptionRate
      - aapl_EmployeeStockPurchasePlanMaximumAnnualPurchasesPerEmployeeAmount
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant
      - us-gaap_DefinedContributionPlanMaximumAnnualContributionsPerEmployeeAmount
      - us-gaap_DefinedContributionPlanEmployerMatchingContributionPercentOfMatch
      - us-gaap_DefinedContributionPlanEmployerMatchingContributionPercent
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
      - us-gaap_SharesPaidForTaxWithholdingForShareBasedCompensation
      - us-gaap_PaymentsRelatedToTaxWithholdingForShareBasedCompensation
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
- us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
  - us-gaap_RestrictedStockUnitsRSUMember
  - us-gaap_EmployeeStockMember

### http://www.apple.com/role/BenefitPlansRestrictedStockUnitsActivityAndRelatedInformationDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsAggregateIntrinsicValueAbstract

### http://www.apple.com/role/BenefitPlansTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfNonvestedRestrictedStockUnitsActivityTableTextBlock
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock

### http://www.apple.com/role/ConsolidatedStatementsOfOperations

- us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding
- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.apple.com/role/ConsolidatedStatementsOfShareholdersEquity

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
    - us-gaap_CommonStockDividendsPerShareDeclared

### http://www.apple.com/role/CoverPage

- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - us-gaap_CommonStockMember
    - aapl_A1.000NotesDue2022Member
    - aapl_A1.375NotesDue2024Member
    - aapl_A0.875NotesDue2025Member
    - aapl_A1.625NotesDue2026Member
    - aapl_A2.000NotesDue2027Member
    - aapl_A1.375NotesDue2029Member
    - aapl_A3.050NotesDue2029Member
    - aapl_A3.600NotesDue2042Member

### http://www.apple.com/role/SelectedQuarterlyFinancialInformationUnauditedSummaryOfQuarterlyFinancialInformationDetails

- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.apple.com/role/ShareholdersEquityAdditionalInformationDetails

- us-gaap_ClassOfTreasuryStockTable
  - us-gaap_ShareRepurchaseProgramAxis
    - us-gaap_ShareRepurchaseProgramDomain
      - aapl_AcceleratedShareRepurchaseArrangementFebruary2019Member
  - us-gaap_EquityClassOfTreasuryStockLineItems

### http://www.apple.com/role/ShareholdersEquitySharesOfCommonStockDetails

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward

## 其他结构 (Other Structure)

### http://www.apple.com/role/BenefitPlansAdditionalInformationDetails

- us-gaap_PlanNameAxis
  - us-gaap_PlanNameDomain
    - aapl_EmployeeStockPlan2014PlanMember
    - aapl_DirectorPlanMember
- us-gaap_AwardTypeAxis
  - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
- srt_RangeAxis
  - srt_RangeMember
    - srt_MinimumMember
    - srt_MaximumMember

### http://www.apple.com/role/CommitmentsAndContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.apple.com/role/CommitmentsAndContingenciesAdditionalInformationDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - aapl_CommitmentsAndContingenciesDisclosureTable
    - srt_LitigationCaseAxis
      - srt_LitigationCaseTypeDomain
    - us-gaap_LitigationStatusAxis
      - us-gaap_LitigationStatusDomain
    - aapl_CommitmentsAndContingenciesDisclosureLineItems
      - us-gaap_OperatingLeasesFutureMinimumPaymentsDue
      - us-gaap_LesseeOperatingLeaseTermOfContract
      - us-gaap_OperatingLeasesRentExpenseNet
      - us-gaap_LitigationSettlementAmountAwardedToOtherParty
      - aapl_LitigationSettlementAmountAwardedToOtherPartyRevisedAmountDeterminedinSubsequentProceedings

### http://www.apple.com/role/CommitmentsAndContingenciesChangesInAccruedWarrantiesAndRelatedCostsDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_MovementInStandardProductWarrantyAccrualRollForward
    - us-gaap_StandardProductWarrantyAccrual
    - us-gaap_StandardProductWarrantyAccrualPayments
    - us-gaap_StandardProductWarrantyAccrualWarrantiesIssued
    - us-gaap_StandardProductWarrantyAccrual

### http://www.apple.com/role/CommitmentsAndContingenciesFutureMinimumLeasePaymentsUnderNoncancelableOperatingLeasesDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract

### http://www.apple.com/role/CommitmentsAndContingenciesFuturePaymentsUnderUnconditionalPurchaseObligationsDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_UnrecordedUnconditionalPurchaseObligationAbstract
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnFirstAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnSecondAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnThirdAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnFourthAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnFifthAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationDueAfterFiveYears
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceSheetAmount [totalLabel]

### http://www.apple.com/role/CommitmentsAndContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_ScheduleOfProductWarrantyLiabilityTableTextBlock
  - us-gaap_ScheduleOfFutureMinimumRentalPaymentsForOperatingLeasesTableTextBlock
  - us-gaap_UnrecordedUnconditionalPurchaseObligationsDisclosureTextBlock

### http://www.apple.com/role/ConsolidatedFinancialStatementDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_AdditionalFinancialInformationDisclosureTextBlock

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsOtherNonCurrentLiabilitiesDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_AccruedIncomeTaxesNoncurrent
  - us-gaap_OtherAccruedLiabilitiesNoncurrent
  - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsPropertyPlantAndEquipmentNetDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsTables

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock
  - us-gaap_OtherNoncurrentLiabilitiesTableTextBlock
  - us-gaap_InterestAndOtherIncomeTableTextBlock

### http://www.apple.com/role/ConsolidatedStatementsOfOperations

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

### http://www.apple.com/role/CoverPage

- dei_CoverAbstract
  - dei_EntitiesTable
    - us-gaap_StatementClassOfStockAxis
    - dei_EntityInformationLineItems
      - dei_DocumentType
      - dei_DocumentAnnualReport
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
      - dei_SecurityExchangeName
      - dei_EntityWellKnownSeasonedIssuer
      - dei_EntityVoluntaryFilers
      - dei_EntityCurrentReportingStatus
      - dei_EntityInteractiveDataCurrent
      - dei_EntityFilerCategory
      - dei_EntitySmallBusiness
      - dei_EntityEmergingGrowthCompany
      - dei_EntityShellCompany
      - dei_EntityPublicFloat
      - dei_EntityCommonStockSharesOutstanding
      - dei_AmendmentFlag
      - dei_DocumentFiscalYearFocus
      - dei_DocumentFiscalPeriodFocus
      - dei_EntityCentralIndexKey
      - dei_CurrentFiscalYearEndDate

### http://www.apple.com/role/Debt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.apple.com/role/DebtAdditionalInformationDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_CommercialPaper
      - us-gaap_DebtInstrumentTerm
      - us-gaap_ShortTermDebtWeightedAverageInterestRate
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_SeniorNotes
      - us-gaap_InterestCostsIncurred
      - us-gaap_LongTermDebtFairValue

### http://www.apple.com/role/DebtFuturePrincipalPaymentsForTermDebtDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive
  - us-gaap_DebtInstrumentCarryingAmount [totalLabel]

### http://www.apple.com/role/DebtSummaryOfTermDebtDetails

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
      - us-gaap_LongTermDebtCurrent
      - us-gaap_LongTermDebtNoncurrent
      - aapl_DebtInstrumentMaturityYearRangeStart
      - aapl_DebtInstrumentMaturityYearRangeEnd
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage

### http://www.apple.com/role/DebtTables

- us-gaap_DebtDisclosureAbstract
  - aapl_CommercialPaperCashFlowSummaryTableTextBlock
  - us-gaap_ScheduleOfDebtInstrumentsTextBlock
  - us-gaap_ScheduleOfMaturitiesOfLongTermDebtTableTextBlock

### http://www.apple.com/role/FinancialInstruments

- us-gaap_InvestmentsAllOtherInvestmentsAbstract
  - us-gaap_FinancialInstrumentsDisclosureTextBlock

### http://www.apple.com/role/FinancialInstrumentsAdditionalInformationDetails

- us-gaap_FairValueDisclosuresAbstract
  - aapl_FinancialInstrumentsTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - us-gaap_ConcentrationRiskByTypeAxis
      - us-gaap_ConcentrationRiskTypeDomain
    - srt_MajorCustomersAxis
      - srt_NameOfMajorCustomerDomain
    - aapl_FinancialInstrumentsLineItems
      - aapl_LongTermMarketableSecuritiesMaturitiesTerm
      - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueAmount
      - us-gaap_MaximumLengthOfTimeForeignCurrencyCashFlowHedge
      - us-gaap_MaximumLengthOfTimeHedgedInInterestRateCashFlowHedge1
      - us-gaap_GainLossFromComponentsExcludedFromAssessmentOfFairValueHedgeEffectivenessNet
      - aapl_CollateralAlreadyReceivedAggregateFairValue
      - us-gaap_CollateralAlreadyPostedAggregateFairValue
      - aapl_DerivativeAssetsReductionforMasterNettingArrangements
      - aapl_DerivativeLiabilitiesReductionforMasterNettingArrangements
      - us-gaap_DerivativeFairValueOfDerivativeNet
      - aapl_NumberOfCustomersWithSignificantAccountsReceivableBalance
      - us-gaap_ConcentrationRiskPercentage1
      - aapl_NumberOfSignificantVendors

### http://www.apple.com/role/FinancialInstrumentsDerivativeInstrumentsAtGrossFairValueDetails

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_FairValuesDerivativesBalanceSheetLocationByDerivativeContractTypeByHedgingDesignationTable
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_DerivativesFairValueLineItems
      - us-gaap_DerivativeAssetsAbstract
      - us-gaap_DerivativeLiabilitiesAbstract

### http://www.apple.com/role/FinancialInstrumentsNotionalAmountsAndCreditRiskAmountsAssociatedWithDerivativeInstrumentsDetails

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeTable
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativeLineItems
      - us-gaap_DerivativeNotionalAmount
      - aapl_DerivativeCounterpartyCreditRiskExposure

### http://www.apple.com/role/FinancialInstrumentsPreTaxGainsAndLossesOfDerivativeAndNonDerivativeInstrumentsDesignatedAsHedgesDetails

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
- us-gaap_DerivativeInstrumentsGainLossLineItems
  - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodBeforeTax
  - us-gaap_DerivativeInstrumentsGainLossReclassifiedFromAccumulatedOCIIntoIncomeEffectivePortionNet
  - us-gaap_ChangeInUnrealizedGainLossOnFairValueHedgingInstruments1
  - us-gaap_ChangeInUnrealizedGainLossOnHedgedItemInFairValueHedge1
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ForeignExchangeContractMember
    - us-gaap_InterestRateContractMember
    - aapl_ForeignCurrencyDebtMember
- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
  - us-gaap_HedgingRelationshipDomain
    - us-gaap_CashFlowHedgingMember
    - us-gaap_NetInvestmentHedgingMember
    - us-gaap_FairValueHedgingMember

### http://www.apple.com/role/FinancialInstrumentsTables

- us-gaap_InvestmentsAllOtherInvestmentsAbstract
  - aapl_CashCashEquivalentsandAvailableforSaleSecuritiesTableTextBlock
  - us-gaap_ScheduleOfUnrealizedLossOnInvestmentsTableTextBlock
  - us-gaap_ScheduleOfRestrictedCashAndCashEquivalentsTextBlock
  - us-gaap_ScheduleOfDerivativeInstrumentsInStatementOfFinancialPositionFairValueTextBlock
  - us-gaap_ScheduleOfDerivativeInstrumentsGainLossInStatementOfFinancialPerformanceTextBlock
  - aapl_NotionalAndCreditRiskAmountsOfOutstandingDerivativePositionsDisclosureTableTextBlock

### http://www.apple.com/role/SegmentInformationAndGeographicData

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.apple.com/role/SegmentInformationAndGeographicDataNetSalesDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - country_CN
    - aapl_OtherCountriesMember

### http://www.apple.com/role/SegmentInformationAndGeographicDataSummaryInformationByReportableSegmentDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_OperatingIncomeLoss

### http://www.apple.com/role/SegmentInformationAndGeographicDataTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
  - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTextBlock
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsByGeographicalAreasTableTextBlock

### http://www.apple.com/role/SelectedQuarterlyFinancialInformationUnaudited

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_QuarterlyFinancialInformationTextBlock

### http://www.apple.com/role/SelectedQuarterlyFinancialInformationUnauditedSummaryOfQuarterlyFinancialInformationDetails

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_SelectedQuarterlyFinancialInformationAbstract
    - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
    - us-gaap_GrossProfit
    - us-gaap_NetIncomeLoss
    - us-gaap_EarningsPerShareAbstract

### http://www.apple.com/role/SelectedQuarterlyFinancialInformationUnauditedTables

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_ScheduleOfQuarterlyFinancialInformationTableTextBlock

### http://www.apple.com/role/SummaryOfSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfPresentationAndSignificantAccountingPoliciesTextBlock

### http://www.apple.com/role/SummaryOfSignificantAccountingPoliciesAdditionalInformationDetails

- us-gaap_AccountingPoliciesAbstract
  - aapl_SignificantAccountingPoliciesTable
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - aapl_SignificantAccountingPoliciesLineItems
      - us-gaap_DeferredTaxAssetsLiabilitiesNet
      - us-gaap_OtherAssetsNoncurrent
      - us-gaap_CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption
      - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_Depreciation
      - aapl_NonCashActivitiesInvolvingPropertyPlantandEquipmentNetIncreaseDecreasetoAccountsPayableandOtherCurrentLiabilities

### http://www.apple.com/role/SummaryOfSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfAccountingPolicyPolicyTextBlock
  - us-gaap_FiscalPeriod
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock
  - us-gaap_AdvertisingCostsPolicyTextBlock
  - us-gaap_CompensationRelatedCostsPolicyTextBlock
  - us-gaap_EarningsPerSharePolicyTextBlock
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValuePolicyTextBlock
  - aapl_RestrictedCashandRestrictedMarketableSecuritiesPolicyTextBlock
  - us-gaap_FairValueMeasurementPolicyPolicyTextBlock
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - us-gaap_DerivativesPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_SegmentReportingPolicyPolicyTextBlock

### http://www.apple.com/role/SummaryOfSignificantAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock

