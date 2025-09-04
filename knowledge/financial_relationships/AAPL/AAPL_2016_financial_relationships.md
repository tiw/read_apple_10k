# AAPL 2016 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.apple.com/role/AcquiredIntangibleAssetsExpectedAnnualAmortizationExpenseRelatedToAcquiredIntangibleAssetsDetail

- us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.apple.com/role/BenefitPlansSummaryOfShareBasedCompensationExpenseDetail

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember
    - us-gaap_SellingGeneralAndAdministrativeExpensesMember

### http://www.apple.com/role/CommitmentsAndContingenciesAdditionalInformationDetail

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_SalesRevenueNetMember

### http://www.apple.com/role/ComprehensiveIncome

- us-gaap_EquityAbstract
  - us-gaap_ComprehensiveIncomeNoteTextBlock

### http://www.apple.com/role/ComprehensiveIncomeChangeInAccumulatedOtherComprehensiveIncomeByComponentDetail

- us-gaap_EquityAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossTable
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_AccumulatedOtherComprehensiveIncomeLossLineItems
      - us-gaap_AOCIAttributableToParentNetOfTaxRollForward

### http://www.apple.com/role/ComprehensiveIncomePreTaxAmountsReclassifiedFromAociIntoConsolidatedStatementsOfOperationsDetail

- us-gaap_EquityAbstract
  - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeTable
    - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeAxis
      - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeDomain
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ReclassificationAdjustmentOutOfAccumulatedOtherComprehensiveIncomeLineItems
      - us-gaap_SalesRevenueNet
      - us-gaap_CostOfGoodsAndServicesSold
      - us-gaap_NonoperatingIncomeExpense
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest

### http://www.apple.com/role/ComprehensiveIncomeTables

- us-gaap_EquityAbstract
  - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeTableTextBlock
  - us-gaap_ScheduleOfAccumulatedOtherComprehensiveIncomeLossTableTextBlock

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsOtherIncomeExpenseNetDetail

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_OtherIncomeAndExpensesAbstract
    - us-gaap_InvestmentIncomeInterestAndDividend
    - us-gaap_InterestExpense
    - us-gaap_OtherNonoperatingIncomeExpense
    - us-gaap_NonoperatingIncomeExpense [totalLabel]

### http://www.apple.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_DepreciationAmortizationAndAccretionNet
  - us-gaap_ShareBasedCompensation
  - us-gaap_DeferredIncomeTaxExpenseBenefit
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
    - us-gaap_OtherComprehensiveIncomeLossNetOfTax [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.apple.com/role/ConsolidatedStatementsOfComprehensiveIncomeParenthetical

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentTax
      - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIOnDerivativesTax
      - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesTax

### http://www.apple.com/role/ConsolidatedStatementsOfOperations

- us-gaap_IncomeStatementAbstract
  - us-gaap_SalesRevenueNet
  - us-gaap_CostOfGoodsAndServicesSold
  - us-gaap_GrossProfit [totalLabel]
  - us-gaap_OperatingExpensesAbstract
    - us-gaap_ResearchAndDevelopmentExpense
    - us-gaap_SellingGeneralAndAdministrativeExpense
    - us-gaap_OperatingExpenses [totalLabel]
  - us-gaap_OperatingIncomeLoss [totalLabel]
  - us-gaap_NonoperatingIncomeExpense
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]
  - us-gaap_IncomeTaxExpenseBenefit
  - us-gaap_NetIncomeLoss [totalLabel]
  - us-gaap_EarningsPerShareAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
  - us-gaap_CommonStockDividendsPerShareDeclared

### http://www.apple.com/role/FinancialInstrumentsPreTaxGainsAndLossesOfDerivativeAndNonDerivativeInstrumentsDesignatedAsCashFlowNetInvestmentAndFairValueHedgesDetail

- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.apple.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.apple.com/role/IncomeTaxesAdditionalInformationDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_EffectiveIncomeTaxRateReconciliationForeignIncomeTaxRateDifferential
  - us-gaap_UndistributedEarningsOfForeignSubsidiaries
  - us-gaap_DeferredTaxLiabilityNotRecognizedAmountOfUnrecognizedDeferredTaxLiabilityUndistributedEarningsOfForeignSubsidiaries
  - aapl_CashCashEquivalentsAndMarketableSecuritiesHeldByForeignSubsidiaries
  - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
  - aapl_ShareBasedCompensationTaxExpenseBenefit
  - aapl_PercentageOfIncomeTaxExaminationMinimumLikelihoodOfTaxBenefitsBeingRealizedUponSettlement
  - us-gaap_UnrecognizedTaxBenefits
  - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
  - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
  - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestExpense
  - us-gaap_DecreaseInUnrecognizedTaxBenefitsIsReasonablyPossible
  - us-gaap_LossContingenciesTable
    - us-gaap_LossContingenciesByNatureOfContingencyAxis
      - us-gaap_LossContingencyNatureDomain
    - us-gaap_LossContingenciesLineItems
      - aapl_LossContingencySubsidiariesImpactedNumber
      - us-gaap_LossContingencyRangeOfPossibleLossMaximum

### http://www.apple.com/role/IncomeTaxesAggregateChangesInGrossUnrecognizedTaxBenefitsExcludingInterestAndPenaltiesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ReconciliationOfUnrecognizedTaxBenefitsExcludingAmountsPertainingToExaminedTaxReturnsRollForward
    - us-gaap_UnrecognizedTaxBenefits
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
    - us-gaap_UnrecognizedTaxBenefitsReductionsResultingFromLapseOfApplicableStatuteOfLimitations
    - us-gaap_UnrecognizedTaxBenefits

### http://www.apple.com/role/IncomeTaxesReconciliationOfProvisionForIncomeTaxesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
  - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
  - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
  - us-gaap_IncomeTaxReconciliationDeductionsQualifiedProductionActivities
  - us-gaap_IncomeTaxReconciliationTaxCreditsResearch
  - us-gaap_IncomeTaxReconciliationOtherAdjustments
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_EffectiveIncomeTaxRateContinuingOperations

### http://www.apple.com/role/IncomeTaxesSignificantComponentsOfCompanysDeferredTaxAssetsAndLiabilitiesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_DeferredTaxAssetsGrossAbstract
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccruals
    - us-gaap_DeferredTaxAssetsPropertyPlantAndEquipment
    - us-gaap_DeferredTaxAssetsDeferredIncome
    - aapl_DeferredTaxAssetsDeferredCostSharing
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
    - aapl_DeferredTaxAssetsUnrealizedLosses
    - us-gaap_DeferredTaxAssetsOther
    - us-gaap_DeferredTaxAssetsNet [totalLabel]
  - us-gaap_DeferredTaxLiabilitiesAbstract
    - us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings
    - us-gaap_DeferredTaxLiabilitiesOther
    - us-gaap_DeferredIncomeTaxLiabilities [totalLabel]
  - us-gaap_DeferredIncomeTaxLiabilitiesNet
  - us-gaap_DeferredTaxAssetsValuationAllowance

### http://www.apple.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_SummaryOfPositionsForWhichSignificantChangeInUnrecognizedTaxBenefitsIsReasonablyPossibleTextBlock

### http://www.apple.com/role/ProvisionForIncomeTaxesDetail

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

### http://www.apple.com/role/SegmentInformationAndGeographicDataLongLivedAssetsDetail

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - us-gaap_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

### http://www.apple.com/role/SegmentInformationAndGeographicDataNetSalesDetail

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - us-gaap_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_SalesRevenueNet

### http://www.apple.com/role/SegmentInformationAndGeographicDataReconciliationOfSegmentOperatingIncomeToConsolidatedStatementsOfOperationsDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTable
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_SegmentReportingReconcilingItemForOperatingProfitLossFromSegmentToConsolidatedLineItems
      - us-gaap_OperatingIncomeLoss
      - us-gaap_ResearchAndDevelopmentExpense
      - us-gaap_OtherOperatingIncomeExpenseNet
      - us-gaap_OperatingIncomeLoss [totalLabel]

### http://www.apple.com/role/SummaryOfSignificantAccountingPoliciesComputationOfBasicAndDilutedEarningsPerShareDetail

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

### http://www.apple.com/role/AcquiredIntangibleAssets

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_IntangibleAssetsDisclosureTextBlock

### http://www.apple.com/role/AcquiredIntangibleAssetsAdditionalInformationDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_AmortizationOfIntangibleAssets
  - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.apple.com/role/AcquiredIntangibleAssetsComponentsOfGrossAndNetIntangibleAssetBalancesDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_FiniteLivedIntangibleAssetsGross
  - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]
  - us-gaap_IndefiniteLivedIntangibleAssetsExcludingGoodwill
  - us-gaap_IntangibleAssetsGrossExcludingGoodwill [totalLabel]
  - us-gaap_IntangibleAssetsNetExcludingGoodwill [totalLabel]

### http://www.apple.com/role/AcquiredIntangibleAssetsExpectedAnnualAmortizationExpenseRelatedToAcquiredIntangibleAssetsDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract

### http://www.apple.com/role/AcquiredIntangibleAssetsTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTableTextBlock
  - us-gaap_ScheduleOfIndefiniteLivedIntangibleAssetsTableTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.apple.com/role/BenefitPlansRestrictedStockUnitsActivityAndRelatedInformationDetail

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
      - us-gaap_AvailableForSaleSecuritiesCurrent
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_InventoryNet
      - us-gaap_NontradeReceivablesCurrent
      - us-gaap_OtherAssetsCurrent
      - us-gaap_AssetsCurrent [totalLabel]
    - us-gaap_AvailableForSaleSecuritiesNoncurrent
    - us-gaap_PropertyPlantAndEquipmentNet
    - us-gaap_Goodwill
    - us-gaap_IntangibleAssetsNetExcludingGoodwill
    - us-gaap_OtherAssetsNoncurrent
    - us-gaap_Assets [totalLabel]
  - us-gaap_LiabilitiesAndStockholdersEquityAbstract
    - us-gaap_LiabilitiesCurrentAbstract
      - us-gaap_AccountsPayableCurrent
      - us-gaap_AccruedLiabilitiesCurrent
      - us-gaap_DeferredRevenueCurrent
      - us-gaap_CommercialPaper
      - us-gaap_LongTermDebtCurrent
      - us-gaap_LiabilitiesCurrent [totalLabel]
    - us-gaap_DeferredRevenueNoncurrent
    - us-gaap_LongTermDebtNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent
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
  - us-gaap_AllowanceForDoubtfulAccountsReceivableCurrent
  - us-gaap_CommonStockParOrStatedValuePerShare
  - us-gaap_CommonStockSharesIssued
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_CommonStockSharesAuthorized

### http://www.apple.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperationsAbstract
    - us-gaap_NetIncomeLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperations [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperationsAbstract
    - us-gaap_PaymentsToAcquireAvailableForSaleSecurities
    - us-gaap_ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities
    - us-gaap_ProceedsFromSaleOfAvailableForSaleSecurities
    - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
    - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
    - us-gaap_PaymentsToAcquireIntangibleAssets
    - us-gaap_PaymentsToAcquireOtherInvestments
    - us-gaap_PaymentsForProceedsFromOtherInvestingActivities
    - us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperations [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperationsAbstract
    - us-gaap_ProceedsFromIssuanceOfCommonStock
    - us-gaap_ExcessTaxBenefitFromShareBasedCompensationFinancingActivities
    - us-gaap_PaymentsRelatedToTaxWithholdingForShareBasedCompensation
    - aapl_PaymentsOfDividendsAndDividendEquivalentsOnCommonStockAndRestrictedStockUnits
    - us-gaap_PaymentsForRepurchaseOfCommonStock
    - us-gaap_ProceedsFromIssuanceOfLongTermDebt
    - us-gaap_RepaymentsOfLongTermDebt
    - us-gaap_ProceedsFromRepaymentsOfCommercialPaper
    - us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperations [totalLabel]
  - us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease [totalLabel]
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_SupplementalCashFlowInformationAbstract
    - us-gaap_IncomeTaxesPaidNet
    - us-gaap_InterestPaid

### http://www.apple.com/role/ConsolidatedStatementsOfShareholdersEquity

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTax
  - aapl_DividendsAndDividendEquivalentsDeclaredOnCommonStockAndRestrictedStockUnits
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
  - aapl_SharesOfStockIssuedDuringPeriodShareBasedCompensationNetOfSharesWithheldForTaxes
  - aapl_StockIssuedDuringPeriodValueShareBasedCompensationNetOfSharesWithheldForTaxes
  - aapl_AdjustmentsToAdditionalPaidInCapitalTaxEffectFromShareBasedCompensationIncludingTransferPricing
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockIncludingAdditionalPaidInCapitalMember
    - us-gaap_RetainedEarningsMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember

### http://www.apple.com/role/FinancialInstrumentsCashAndAvailableForSaleSecuritiesAdjustedCostGrossUnrealizedGainsGrossUnrealizedLossesAndFairValueRecordedAsCashAndCashEquivalentsOrShortTermOrLongTermMarketableSecuritiesDetail

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_ScheduleOfAvailableForSaleSecuritiesTable

### http://www.apple.com/role/FinancialInstrumentsDerivativeInstrumentsAtGrossFairValueDetail

- us-gaap_DerivativeAssetsAbstract
  - us-gaap_DerivativeFairValueOfDerivativeAsset

### http://www.apple.com/role/SegmentInformationAndGeographicDataLongLivedAssetsDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- us-gaap_StatementGeographicalAxis
  - us-gaap_SegmentGeographicalDomain
    - country_US
    - country_CN
    - aapl_OtherCountriesMember

### http://www.apple.com/role/ShareholdersEquity

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.apple.com/role/ShareholdersEquityAcceleratedShareRepurchaseActivityAndRelatedInformationDetail

- us-gaap_EquityAbstract
  - us-gaap_AcceleratedShareRepurchasesTable

### http://www.apple.com/role/ShareholdersEquityAdditionalInformationDetail

- us-gaap_EquityAbstract
  - us-gaap_StockRepurchaseProgramAuthorizedAmount1
  - aapl_AmountUtilizedUnderShareRepurchaseProgram

### http://www.apple.com/role/ShareholdersEquityRepurchasesOfCommonSharesInOpenMarketDetail

- us-gaap_EquityAbstract
  - aapl_ScheduleOfStockRepurchaseProgramTable

### http://www.apple.com/role/ShareholdersEquitySummaryOfDividendsDeclaredAndPaidDetail

- us-gaap_EquityAbstract
  - us-gaap_CommonStockDividendsPerShareDeclared
  - us-gaap_PaymentsOfDividends

### http://www.apple.com/role/ShareholdersEquityTables

- us-gaap_EquityAbstract
  - us-gaap_DividendsDeclaredTableTextBlock
  - us-gaap_AcceleratedShareRepurchasesTextBlock
  - aapl_ScheduleOfCommonStockRepurchasedTableTextBlock

## 现金流量表结构 (Cash Flow Structure)

### http://www.apple.com/role/CommitmentsAndContingenciesFutureMinimumLeasePaymentsUnderNoncancelableOperatingLeasesDetail

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
  - us-gaap_IncreaseDecreaseInDeferredRevenue
  - us-gaap_IncreaseDecreaseInOtherOperatingLiabilities

### http://www.apple.com/role/DebtSummaryOfCashFlowsAssociatedWithIssuanceAndMaturitiesOfCommercialPaperDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInThreeMonthsOrLessAlternativeAbstract
    - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInThreeMonthsOrLess
  - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInMoreThanThreeMonthsAlternativeAbstract
    - us-gaap_ProceedsFromShortTermDebtMaturingInMoreThanThreeMonths
    - us-gaap_RepaymentsOfShortTermDebtMaturingInMoreThanThreeMonths
    - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInMoreThanThreeMonths [totalLabel]
  - us-gaap_ProceedsFromRepaymentsOfCommercialPaper [totalLabel]

### http://www.apple.com/role/FinancialInstrumentsCashAndAvailableForSaleSecuritiesAdjustedCostGrossUnrealizedGainsGrossUnrealizedLossesAndFairValueRecordedAsCashAndCashEquivalentsOrShortTermOrLongTermMarketableSecuritiesDetail

- us-gaap_ScheduleOfAvailableForSaleSecuritiesTable
  - us-gaap_FairValueByFairValueHierarchyLevelAxis
    - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
      - us-gaap_FairValueInputsLevel1Member
      - us-gaap_FairValueInputsLevel2Member
  - us-gaap_InvestmentTypeAxis
    - us-gaap_InvestmentTypeCategorizationMember
      - us-gaap_CashMember
      - us-gaap_MoneyMarketFundsMember
      - us-gaap_EquitySecuritiesMember
      - us-gaap_USTreasurySecuritiesMember
      - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
      - us-gaap_ForeignGovernmentDebtSecuritiesMember
      - us-gaap_BankTimeDepositsMember
      - us-gaap_CommercialPaperMember
      - us-gaap_CorporateDebtSecuritiesMember
      - us-gaap_USStatesAndPoliticalSubdivisionsMember
      - us-gaap_AssetBackedSecuritiesMember
  - us-gaap_ScheduleOfAvailableForSaleSecuritiesLineItems
    - us-gaap_AvailableForSaleSecuritiesAmortizedCost [totalLabel]
    - us-gaap_AvailableForSaleSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
    - us-gaap_AvailableForSaleSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
    - us-gaap_AvailableForSaleSecurities
    - us-gaap_CashAndCashEquivalentsAtCarryingValue
    - us-gaap_AvailableForSaleSecuritiesCurrent
    - us-gaap_AvailableForSaleSecuritiesNoncurrent

### http://www.apple.com/role/FinancialInstrumentsPreTaxGainsAndLossesOfDerivativeAndNonDerivativeInstrumentsDesignatedAsCashFlowNetInvestmentAndFairValueHedgesDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
- us-gaap_DerivativeInstrumentsGainLossLineItems
  - us-gaap_DerivativeInstrumentsGainLossRecognizedInOtherComprehensiveIncomeEffectivePortionNet
  - us-gaap_DerivativeInstrumentsGainLossReclassifiedFromAccumulatedOCIIntoIncomeEffectivePortionNet
  - us-gaap_DerivativeGainLossOnDerivativeNet
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

## 股东权益结构 (Equity Structure)

### http://www.apple.com/role/BenefitPlans

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_CompensationAndEmployeeBenefitPlansTextBlock

### http://www.apple.com/role/BenefitPlansAdditionalInformationDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_PlanNameAxis
    - us-gaap_RangeAxis
    - us-gaap_AwardTypeAxis
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - aapl_SharebasedCompensationArrangementbySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsNumberofSharesofCommonSharesAwardedUponSettlement
      - aapl_SharebasedCompensationArrangementbySharebasedPaymentAwardEquityInstrumentsOtherthanOptionsReductioninNumberofSharesAvailableforGrantPerShareGranted
      - aapl_SharebasedCompensationArrangementbySharebasedPaymentAwardEquityInstrumentsOtherthanOptionsIncreaseinNumberofSharesAvailableforGrantPerShareCancelledorWithheld
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAuthorized
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardExpirationPeriod
      - aapl_ShareBasedCompensationArrangementByShareBasedPaymentAwardPeriodOfTimeOptionsBecomeExercisable
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardExpirationDate
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardPurchasePriceOfCommonStockPercent
      - aapl_ShareBasedCompensationArrangementByShareBasedPaymentAwardOfferingTerm
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardMaximumEmployeeSubscriptionRate
      - aapl_EmployeeStockPurchaseProgramAuthorizedAmount
      - us-gaap_DefinedContributionPlanMaximumAnnualContributionsPerEmployeeAmount
      - us-gaap_DefinedContributionPlanEmployerMatchingContributionPercent
      - aapl_DefinedContributionPlanContributionRatesAsPercentageOfEmployeesEarnings
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
      - us-gaap_SharesPaidForTaxWithholdingForShareBasedCompensation
      - us-gaap_EmployeeServiceShareBasedCompensationCashFlowEffectCashUsedToSettleAwards
      - us-gaap_IncomeTaxReconciliationNondeductibleExpenseShareBasedCompensationCost
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
- us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
  - us-gaap_RestrictedStockUnitsRSUMember
  - us-gaap_EmployeeStockOptionMember
  - aapl_EmployeeStockPurchasePlanMember

### http://www.apple.com/role/BenefitPlansRestrictedStockUnitsActivityAndRelatedInformationDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsAggregateIntrinsicValueAbstract

### http://www.apple.com/role/BenefitPlansSummaryOfShareBasedCompensationExpenseDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
    - dei_LegalEntityAxis
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
      - us-gaap_AllocatedShareBasedCompensationExpense

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

### http://www.apple.com/role/SelectedQuarterlyFinancialInformationSummaryOfQuarterlyFinancialInformationDetail

- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.apple.com/role/ShareholdersEquityAcceleratedShareRepurchaseActivityAndRelatedInformationDetail

- us-gaap_AcceleratedShareRepurchasesTable
  - us-gaap_ShareRepurchaseProgramAxis
    - us-gaap_ShareRepurchaseProgramDomain
      - aapl_AcceleratedShareRepurchaseAgreementAugust2016Member
      - aapl_AcceleratedShareRepurchaseAgreementMay2016Member
      - aapl_AcceleratedShareRepurchaseAgreementNovember2015Member
      - aapl_AcceleratedShareRepurchaseAgreementMayTwentyFifteenMember
      - aapl_AcceleratedShareRepurchaseAgreementAugustTwentyFourteenMember
      - aapl_AcceleratedShareRepurchaseAgreementJanuaryTwentyFourteenMember
  - us-gaap_AcceleratedShareRepurchasesLineItems
    - aapl_StockRepurchaseProgramCompletionDate
    - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
    - us-gaap_AcceleratedShareRepurchasesFinalPricePaidPerShare
    - aapl_UpfrontPaymentUnderAcceleratedShareRepurchaseProgram

### http://www.apple.com/role/ShareholdersEquityRepurchasesOfCommonSharesInOpenMarketDetail

- aapl_ScheduleOfStockRepurchaseProgramTable
  - us-gaap_ShareRepurchaseProgramAxis
    - us-gaap_ShareRepurchaseProgramDomain
      - aapl_OpenMarketRepurchasesMember
  - aapl_StockRepurchaseProgramLineItems
    - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
    - aapl_StockRepurchasedAndRetiredDuringPeriodWeightedAveragePrice
    - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue

## 其他结构 (Other Structure)

### http://www.apple.com/role/BenefitPlansAdditionalInformationDetail

- us-gaap_PlanNameAxis
  - us-gaap_PlanNameDomain
    - aapl_EmployeeStockPlan2014PlanMember
    - aapl_EmployeeStockPlanTwentyZeroThreePlanMember
    - aapl_DirectorsPlanMember
- us-gaap_AwardTypeAxis
  - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
- us-gaap_RangeAxis
  - us-gaap_RangeMember
    - us-gaap_MinimumMember
    - us-gaap_MaximumMember

### http://www.apple.com/role/BenefitPlansSummaryOfShareBasedCompensationExpenseDetail

- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.apple.com/role/CommitmentsAndContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.apple.com/role/CommitmentsAndContingenciesAdditionalInformationDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - aapl_CommitmentsAndContingenciesDisclosureTable
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_LeaseArrangementTypeAxis
      - us-gaap_LeaseArrangementTypeDomain
    - us-gaap_LitigationCaseAxis
      - us-gaap_LitigationCaseTypeDomain
    - us-gaap_IncomeStatementLocationAxis
    - aapl_CommitmentsAndContingenciesDisclosureLineItems
      - us-gaap_LongtermPurchaseCommitmentPeriod
      - us-gaap_OperatingLeasesFutureMinimumPaymentsDue
      - us-gaap_LesseeLeasingArrangementsOperatingLeasesTermOfContract
      - us-gaap_OperatingLeasesRentExpenseNet
      - aapl_ResultOfLegalProceedings
      - us-gaap_GainContingencyUnrecordedAmount
      - us-gaap_ProceedsFromLegalSettlements

### http://www.apple.com/role/CommitmentsAndContingenciesChangesInAccruedWarrantiesAndRelatedCostsDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_MovementInStandardProductWarrantyAccrualRollForward
    - us-gaap_StandardProductWarrantyAccrual
    - us-gaap_StandardProductWarrantyAccrualPayments
    - us-gaap_StandardProductWarrantyAccrualWarrantiesIssued
    - us-gaap_StandardProductWarrantyAccrual

### http://www.apple.com/role/CommitmentsAndContingenciesFutureMinimumLeasePaymentsUnderNoncancelableOperatingLeasesDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract

### http://www.apple.com/role/CommitmentsAndContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_ScheduleOfProductWarrantyLiabilityTableTextBlock
  - us-gaap_ScheduleOfFutureMinimumRentalPaymentsForOperatingLeasesTableTextBlock

### http://www.apple.com/role/ConsolidatedFinancialStatementDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_AdditionalFinancialInformationDisclosureTextBlock

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsOtherNonCurrentLiabilitiesDetail

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_OtherLiabilitiesDisclosureAbstract
    - us-gaap_DeferredTaxLiabilitiesNoncurrent
    - us-gaap_OtherAccruedLiabilitiesNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsPropertyPlantAndEquipmentNetDetail

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_PropertyPlantAndEquipmentAbstract
    - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
      - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentLineItems

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsTables

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock
  - us-gaap_OtherNoncurrentLiabilitiesTableTextBlock
  - us-gaap_InterestAndOtherIncomeTableTextBlock

### http://www.apple.com/role/Debt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.apple.com/role/DebtAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_ShortTermDebtTypeAxis
      - us-gaap_ShortTermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_CommercialPaper
      - us-gaap_DebtInstrumentTerm
      - us-gaap_ShortTermDebtWeightedAverageInterestRate
      - us-gaap_DebtInstrumentCarryingAmount
      - invest_DerivativeNotionalAmount
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_SeniorNotes
      - us-gaap_InterestExpenseDebt
      - us-gaap_LongTermDebtFairValue

### http://www.apple.com/role/DebtDebtInstrumentFuturePrincipalPaymentsDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive
  - us-gaap_DebtInstrumentCarryingAmount [totalLabel]

### http://www.apple.com/role/DebtSummaryOfTermDebtDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - aapl_DebtInstrumentMaturityYear
      - us-gaap_SeniorNotes
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_DebtInstrumentUnamortizedDiscountPremiumNet
      - aapl_HedgeAccountingAdjustmentsRelatedToLongTermDebt
      - us-gaap_LongTermDebtCurrent
      - us-gaap_LongTermDebtNoncurrent
      - us-gaap_DebtInstrumentFaceAmount
      - aapl_DebtInstrumentMaturityYearRangeStart
      - aapl_DebtInstrumentMaturityYearRangeEnd
      - us-gaap_DebtInstrumentInterestRateEffectivePercentageRateRangeMinimum
      - us-gaap_DebtInstrumentInterestRateEffectivePercentageRateRangeMaximum
      - us-gaap_DebtInstrumentInterestRateStatedPercentageRateRangeMinimum
      - us-gaap_DebtInstrumentInterestRateStatedPercentageRateRangeMaximum
      - us-gaap_DebtInstrumentInterestRateStatedPercentage

### http://www.apple.com/role/DebtTables

- us-gaap_DebtDisclosureAbstract
  - aapl_CommercialPaperCashFlowSummaryTableTextBlock
  - us-gaap_ScheduleOfDebtInstrumentsTextBlock
  - us-gaap_ScheduleOfMaturitiesOfLongTermDebtTableTextBlock

### http://www.apple.com/role/DocumentAndEntityInformation

- aapl_DocumentAndEntityInformationAbstract
  - dei_DocumentType
  - dei_AmendmentFlag
  - dei_DocumentPeriodEndDate
  - dei_DocumentFiscalYearFocus
  - dei_DocumentFiscalPeriodFocus
  - dei_TradingSymbol
  - dei_EntityRegistrantName
  - dei_EntityCentralIndexKey
  - dei_CurrentFiscalYearEndDate
  - dei_EntityWellKnownSeasonedIssuer
  - dei_EntityCurrentReportingStatus
  - dei_EntityVoluntaryFilers
  - dei_EntityFilerCategory
  - dei_EntityCommonStockSharesOutstanding
  - dei_EntityPublicFloat

### http://www.apple.com/role/FinancialInstruments

- us-gaap_InvestmentsAllOtherInvestmentsAbstract
  - us-gaap_FinancialInstrumentsDisclosureTextBlock

### http://www.apple.com/role/FinancialInstrumentsAdditionalInformationDetail

- us-gaap_FairValueDisclosuresAbstract
  - aapl_FinancialInstrumentsTable
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - us-gaap_ConcentrationRiskByTypeAxis
      - us-gaap_ConcentrationRiskTypeDomain
    - us-gaap_MajorCustomersAxis
      - us-gaap_NameOfMajorCustomerDomain
    - aapl_FinancialInstrumentsLineItems
      - aapl_LongTermMarketableSecuritiesMaturitiesTermMinimum
      - aapl_LongTermMarketableSecuritiesMaturitiesTermMaximum
      - us-gaap_MaximumLengthOfTimeForeignCurrencyCashFlowHedge
      - us-gaap_MaximumLengthOfTimeHedgedInInterestRateCashFlowHedge1
      - aapl_CollateralAlreadyReceivedAggregateFairValue
      - aapl_DerivativeAssetsReducedForMasterNettingArrangements
      - aapl_DerivativeLiabilitiesReducedForMasterNettingArrangements
      - us-gaap_DerivativeFairValueOfDerivativeNet
      - aapl_NumberOfCustomersWithSignificantAccountsReceivableBalance
      - us-gaap_ConcentrationRiskPercentage1
      - aapl_NumberOfSignificantVendors

### http://www.apple.com/role/FinancialInstrumentsDerivativeInstrumentsAtGrossFairValueDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_FairValuesDerivativesBalanceSheetLocationByDerivativeContractTypeByHedgingDesignationTable
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_DerivativesFairValueLineItems
      - us-gaap_DerivativeAssetsAbstract
      - us-gaap_DerivativeLiabilitiesAbstract

### http://www.apple.com/role/FinancialInstrumentsNotionalAmountsOfOutstandingDerivativeInstrumentsAndCreditRiskAmountsAssociatedWithOutstandingOrUnsettledDerivativeInstrumentsDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeTable
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativeLineItems
      - invest_DerivativeNotionalAmount
      - aapl_CreditRiskAmountOfForeignCurrencyDerivativeInstrumentsDesignatedAsHedgingInstruments
      - aapl_CreditRiskAmountOfInterestRateDerivativeInstrumentsDesignatedAsHedgingInstruments
      - aapl_CreditRiskAmountOfForeignCurrencyDerivativeInstrumentsNotDesignatedAsHedgingInstruments

### http://www.apple.com/role/FinancialInstrumentsTables

- us-gaap_InvestmentsAllOtherInvestmentsAbstract
  - us-gaap_AvailableForSaleSecuritiesTextBlock
  - us-gaap_ScheduleOfCashAndCashEquivalentsTableTextBlock
  - us-gaap_ScheduleOfDerivativeInstrumentsInStatementOfFinancialPositionFairValueTextBlock
  - us-gaap_ScheduleOfDerivativeInstrumentsGainLossInStatementOfFinancialPerformanceTextBlock
  - aapl_NotionalAndCreditRiskAmountsOfOutstandingDerivativePositionsDisclosureTextBlock

### http://www.apple.com/role/SegmentInformationAndGeographicData

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.apple.com/role/SegmentInformationAndGeographicDataAdditionalInformationDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_EntityWideDisclosureOnGeographicAreasDescriptionOfRevenueFromExternalCustomers
  - us-gaap_SegmentReportingDisclosureOfMajorCustomers

### http://www.apple.com/role/SegmentInformationAndGeographicDataNetSalesByProductDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_ProductOrServiceAxis
      - us-gaap_ProductsAndServicesDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_SalesRevenueNet

### http://www.apple.com/role/SegmentInformationAndGeographicDataNetSalesDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- us-gaap_StatementGeographicalAxis
  - us-gaap_SegmentGeographicalDomain
    - country_US
    - country_CN
    - aapl_OtherCountriesMember

### http://www.apple.com/role/SegmentInformationAndGeographicDataSummaryInformationByOperatingSegmentDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_SalesRevenueNet
      - us-gaap_OperatingIncomeLoss

### http://www.apple.com/role/SegmentInformationAndGeographicDataTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
  - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTextBlock
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsByGeographicalAreasTableTextBlock
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTextBlock

### http://www.apple.com/role/SelectedQuarterlyFinancialInformationSummaryOfQuarterlyFinancialInformationDetail

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_SelectedQuarterlyFinancialInformationAbstract
    - us-gaap_SalesRevenueNet
    - us-gaap_GrossProfit
    - us-gaap_NetIncomeLoss
    - us-gaap_EarningsPerShareAbstract

### http://www.apple.com/role/SelectedQuarterlyFinancialInformationUnaudited

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_QuarterlyFinancialInformationTextBlock

### http://www.apple.com/role/SelectedQuarterlyFinancialInformationUnauditedTables

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_ScheduleOfQuarterlyFinancialInformationTableTextBlock

### http://www.apple.com/role/SummaryOfSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfPresentationAndSignificantAccountingPoliciesTextBlock

### http://www.apple.com/role/SummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_AccountingPoliciesAbstract
  - aapl_SignificantAccountingPoliciesTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - aapl_SignificantAccountingPoliciesLineItems
      - aapl_DeliverablesInArrangement
      - aapl_PercentageOfIncomeTaxExaminationMinimumLikelihoodOfTaxBenefitsBeingRealizedUponSettlement
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_DepreciationAndAmortization
      - us-gaap_GoodwillImpairmentLoss
      - us-gaap_ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife

### http://www.apple.com/role/SummaryOfSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfAccountingPolicyPolicyTextBlock
  - us-gaap_FiscalPeriod
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - us-gaap_ShippingAndHandlingCostPolicyTextBlock
  - us-gaap_StandardProductWarrantyPolicy
  - us-gaap_ResearchDevelopmentAndComputerSoftwarePolicyTextBlock
  - us-gaap_AdvertisingCostsPolicyTextBlock
  - us-gaap_CompensationRelatedCostsPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_EarningsPerSharePolicyTextBlock
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_DerivativesPolicyTextBlock
  - us-gaap_ReceivablesTradeAndOtherAccountsReceivableAllowanceForDoubtfulAccountsPolicy
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_GoodwillAndIntangibleAssetsPolicyTextBlock
  - us-gaap_FairValueMeasurementPolicyPolicyTextBlock
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock

### http://www.apple.com/role/SummaryOfSignificantAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock

