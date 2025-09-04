# AAPL 2021 财务关系分析

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
      - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodNetOfTax
      - aapl_OtherComprehensiveIncomeLossDerivativeInstrumentGainLossReclassificationAfterTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIOnDerivativesNetOfTax
      - aapl_OtherComprehensiveIncomeLossDerivativeInstrumentGainLossafterReclassificationandTax [totalLabel]
      - us-gaap_OtherComprehensiveIncomeLossDerivativesQualifyingAsHedgesNetOfTax [totalLabel]
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
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.apple.com/role/SummaryofSignificantAccountingPoliciesComputationofBasicandDilutedEarningsPerShareDetails

- us-gaap_EarningsPerShareAbstract
  - us-gaap_NetIncomeLossAbstract
    - us-gaap_NetIncomeLoss
  - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
    - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
    - us-gaap_WeightedAverageNumberDilutedSharesOutstandingAdjustment
    - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding [totalLabel]
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.apple.com/role/RevenueRecognition

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueFromContractWithCustomerTextBlock

### http://www.apple.com/role/RevenueRecognitionTables

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_DisaggregationOfRevenueTableTextBlock

### http://www.apple.com/role/RevenueRecognitionAdditionalInformationDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - aapl_PerformanceObligationsinArrangements
  - us-gaap_ContractWithCustomerLiability

### http://www.apple.com/role/RevenueRecognitionDeferredRevenueExpectedTimingofRealizationDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionTable
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionLineItems
      - us-gaap_RevenueRemainingPerformanceObligationPercentage
      - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionPeriod1

### http://www.apple.com/role/RevenueRecognitionNetSalesDisaggregatedbySignificantProductsandServicesDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_DisaggregationOfRevenueTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_DisaggregationOfRevenueLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_ContractWithCustomerLiabilityRevenueRecognized

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsOtherIncomeExpenseNetDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_InvestmentIncomeInterestAndDividend
  - us-gaap_InterestExpense
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_NonoperatingIncomeExpense [totalLabel]

### http://www.apple.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.apple.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfUnrecognizedTaxBenefitsRollForwardTableTextBlock

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
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestExpense
      - aapl_IncomeTaxContingencyNumberOfSubsidiaries
      - us-gaap_LossContingencyEstimateOfPossibleLoss

### http://www.apple.com/role/IncomeTaxesReconciliationoftheProvisionforIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
  - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
  - us-gaap_EffectiveIncomeTaxRateReconciliationTaxCutsAndJobsActOf2017Amount
  - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
  - aapl_EffectiveIncomeTaxRateReconciliationForeignDerivedIntangibleIncomeDeductionAmount
  - us-gaap_IncomeTaxReconciliationTaxCreditsResearch
  - us-gaap_EffectiveIncomeTaxRateReconciliationShareBasedCompensationExcessTaxBenefitAmount
  - us-gaap_IncomeTaxReconciliationOtherAdjustments
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_EffectiveIncomeTaxRateContinuingOperations

### http://www.apple.com/role/IncomeTaxesSignificantComponentsofDeferredTaxAssetsandLiabilitiesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_DeferredTaxAssetsGrossAbstract
    - us-gaap_DeferredTaxAssetsGoodwillAndIntangibleAssets
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccruals
    - aapl_DeferredTaxAssetsLeaseLiabilities
    - us-gaap_DeferredTaxAssetsDeferredIncome
    - us-gaap_DeferredTaxAssetsTaxCreditCarryforwards
    - us-gaap_DeferredTaxAssetsOther
    - us-gaap_DeferredTaxAssetsGross [totalLabel]
    - us-gaap_DeferredTaxAssetsValuationAllowance
    - us-gaap_DeferredTaxAssetsNet [totalLabel]
  - us-gaap_DeferredTaxLiabilitiesAbstract
    - aapl_DeferredTaxLiabilitiesMinimumTaxonForeignEarnings
    - us-gaap_DeferredTaxLiabilitiesLeasingArrangements
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

### http://www.apple.com/role/BenefitPlansSummaryofShareBasedCompensationExpenseandtheRelatedIncomeTaxBenefitDetails

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

### http://www.apple.com/role/FinancialInstrumentsCashCashEquivalentsandMarketableSecuritiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_DebtSecuritiesAvailableForSaleTable

### http://www.apple.com/role/FinancialInstrumentsNonCurrentMarketableDebtSecuritiesbyContractualMaturityDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesSingleMaturityDateRollingMaturityAbstract

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
    - aapl_LesseeOperatingandFinanceLeaseLiabilityPaymentsDue [totalLabel]
    - aapl_LesseeOperatingandFinanceLeaseLiabilityUndiscountedExcessAmount
    - aapl_OperatingandFinanceLeaseLiability [totalLabel]

### http://www.apple.com/role/ShareholdersEquity

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.apple.com/role/ShareholdersEquityTables

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfStockByClassTextBlock

### http://www.apple.com/role/ShareholdersEquityAdditionalInformationDetails

- us-gaap_EquityClassOfTreasuryStockLineItems
  - us-gaap_StockRepurchaseProgramAuthorizedAmount1
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
  - aapl_UpFrontPaymentUnderAcceleratedShareRepurchaseAgreement
  - aapl_AmountUtilizedUnderShareRepurchaseProgram
- us-gaap_EquityAbstract
  - us-gaap_ClassOfTreasuryStockTable

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

### http://www.apple.com/role/BenefitPlansRestrictedStockUnitsActivityandRelatedInformationDetails

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
  - us-gaap_IncreaseDecreaseInInventories
  - us-gaap_IncreaseDecreaseInOtherReceivables
  - us-gaap_IncreaseDecreaseInOtherOperatingAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInContractWithCustomerLiability
  - us-gaap_IncreaseDecreaseInOtherOperatingLiabilities

### http://www.apple.com/role/FinancialInstrumentsCashCashEquivalentsandMarketableSecuritiesDetails

- us-gaap_DebtSecuritiesAvailableForSaleTable
  - us-gaap_FinancialInstrumentAxis
    - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
      - us-gaap_CashMember
      - us-gaap_MoneyMarketFundsMember
      - us-gaap_MutualFundMember
      - us-gaap_EquitySecuritiesMember
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
    - us-gaap_RestrictedInvestments

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
    - aapl_A1.000NotesDue2022Member
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
  - srt_CumulativeEffectPeriodOfAdoptionAxis
    - srt_CumulativeEffectPeriodOfAdoptionDomain
      - srt_CumulativeEffectPeriodOfAdoptionAdjustmentMember
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
    - us-gaap_CommonStockDividendsPerShareDeclared

### http://www.apple.com/role/ShareholdersEquityAdditionalInformationDetails

- us-gaap_ClassOfTreasuryStockTable
  - us-gaap_ShareRepurchaseProgramAxis
    - us-gaap_ShareRepurchaseProgramDomain
      - aapl_AcceleratedShareRepurchaseAgreementMay2021Member
  - us-gaap_EquityClassOfTreasuryStockLineItems

### http://www.apple.com/role/ShareholdersEquitySharesofCommonStockDetails

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward

### http://www.apple.com/role/BenefitPlans

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_CompensationAndEmployeeBenefitPlansTextBlock

### http://www.apple.com/role/BenefitPlansTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfNonvestedRestrictedStockUnitsActivityTableTextBlock
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock

### http://www.apple.com/role/BenefitPlansAdditionalInformationDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_PlanNameAxis
    - us-gaap_AwardTypeAxis
    - srt_RangeAxis
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - aapl_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNumberOfSharesOfCommonStockIssuedPerUnitUponVesting
      - aapl_FactorByWhichEachRSUGrantedReducesAndEachRSUCanceledOrShareWithheldForTaxesIncreasesSharesAvailableForGrant
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardPurchasePriceOfCommonStockPercent
      - aapl_ShareBasedCompensationArrangementByShareBasedPaymentAwardOfferingPeriod
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardMaximumEmployeeSubscriptionRate
      - aapl_EmployeeStockPurchasePlanMaximumAnnualPurchasesPerEmployeeAmount
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

### http://www.apple.com/role/BenefitPlansRestrictedStockUnitsActivityandRelatedInformationDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsAggregateIntrinsicValueAbstract

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
      - dei_EntityShellCompany
      - dei_EntityPublicFloat
      - dei_EntityCommonStockSharesOutstanding
      - dei_AmendmentFlag
      - dei_DocumentFiscalYearFocus
      - dei_DocumentFiscalPeriodFocus
      - dei_EntityCentralIndexKey

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

### http://www.apple.com/role/SummaryofSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfAccountingPolicyPolicyTextBlock
  - us-gaap_FiscalPeriod
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock
  - us-gaap_AdvertisingCostsPolicyTextBlock
  - us-gaap_CompensationRelatedCostsPolicyTextBlock
  - us-gaap_EarningsPerSharePolicyTextBlock
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_MarketableSecuritiesPolicy
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - aapl_RestrictedCashandRestrictedMarketableSecuritiesPolicyTextBlock
  - us-gaap_DerivativesPolicyTextBlock
  - us-gaap_FairValueMeasurementPolicyPolicyTextBlock
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_LesseeLeasesPolicyTextBlock
  - us-gaap_SegmentReportingPolicyPolicyTextBlock

### http://www.apple.com/role/SummaryofSignificantAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock

### http://www.apple.com/role/SummaryofSignificantAccountingPoliciesAdditionalInformationDetails

- us-gaap_AccountingPoliciesAbstract
  - aapl_SignificantAccountingPoliciesTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - aapl_SignificantAccountingPoliciesLineItems
      - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_Depreciation
      - aapl_NonCashActivitiesInvolvingPropertyPlantandEquipmentNetIncreaseDecreasetoAccountsPayableandOtherCurrentLiabilities

### http://www.apple.com/role/FinancialInstruments

- us-gaap_InvestmentsAllOtherInvestmentsAbstract
  - us-gaap_FinancialInstrumentsDisclosureTextBlock

### http://www.apple.com/role/FinancialInstrumentsTables

- us-gaap_InvestmentsAllOtherInvestmentsAbstract
  - us-gaap_ScheduleOfCashCashEquivalentsAndShortTermInvestmentsTableTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock
  - us-gaap_ScheduleOfNotionalAmountsOfOutstandingDerivativePositionsTableTextBlock
  - us-gaap_ScheduleOfFairValueHedgingInstrumentsStatementsOfFinancialPerformanceAndFinancialPositionLocationTableTextBlock

### http://www.apple.com/role/FinancialInstrumentsNonCurrentMarketableDebtSecuritiesbyContractualMaturityDetails

- us-gaap_AvailableForSaleSecuritiesDebtMaturitiesSingleMaturityDateRollingMaturityAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearTwoThroughFiveFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearSixThroughTenFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingAfterYearTenFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesSingleMaturityDate [totalLabel]

### http://www.apple.com/role/FinancialInstrumentsAdditionalInformationDetails

- us-gaap_FairValueDisclosuresAbstract
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
      - aapl_NumberOfCustomersWithSignificantAccountsReceivableBalance
      - us-gaap_ConcentrationRiskPercentage1
      - aapl_NumberOfSignificantVendors

### http://www.apple.com/role/FinancialInstrumentsNotionalAmountsofDerivativeInstrumentsDetails

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeTable
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativeLineItems
      - us-gaap_DerivativeNotionalAmount

### http://www.apple.com/role/FinancialInstrumentsDerivativeInstrumentsDesignatedasFairValueHedgesandRelatedHedgedItemsDetails

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosuresTable
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosuresLineItems
      - us-gaap_HedgedAssetFairValueHedge
      - us-gaap_HedgedLiabilityFairValueHedge

### http://www.apple.com/role/ConsolidatedFinancialStatementDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_AdditionalFinancialInformationDisclosureTextBlock

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsTables

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock
  - us-gaap_OtherNoncurrentLiabilitiesTableTextBlock
  - us-gaap_InterestAndOtherIncomeTableTextBlock

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsPropertyPlantandEquipmentNetDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]

### http://www.apple.com/role/ConsolidatedFinancialStatementDetailsOtherNonCurrentLiabilitiesDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_AccruedIncomeTaxesNoncurrent
  - us-gaap_OtherAccruedLiabilitiesNoncurrent
  - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.apple.com/role/Leases

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeasesTextBlock
  - us-gaap_LesseeFinanceLeasesTextBlock

### http://www.apple.com/role/LeasesTables

- us-gaap_LeasesAbstract
  - aapl_OperatingandFinanceLeaseRightofUseAssetsandLeaseLiabilitiesTableTextBlock
  - us-gaap_LesseeOperatingLeaseLiabilityMaturityTableTextBlock
  - us-gaap_FinanceLeaseLiabilityMaturityTableTextBlock

### http://www.apple.com/role/LeasesAdditionalInformationDetails

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_LesseeLeaseDescriptionLineItems
      - aapl_LesseeOperatingandFinanceLeaseTermofContract
      - us-gaap_OperatingLeaseCost
      - us-gaap_VariableLeaseCost
      - us-gaap_OperatingLeasesRentExpenseNet
      - us-gaap_OperatingLeasePayments
      - aapl_RightofUseAssetsObtainedinExchangeforOperatingandFinanceLeaseLiabilities
      - aapl_OperatingandFinanceLeaseWeightedAverageRemainingLeaseTerm
      - aapl_OperatingandFinanceLeaseWeightedAverageDiscountRatePercent
      - aapl_LesseeOperatingAndFinanceLeaseLeaseNotYetCommencedPaymentsDue
      - aapl_LesseeOperatingAndFinanceLeaseLeaseNotYetCommencedTermOfContract

### http://www.apple.com/role/Debt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.apple.com/role/DebtTables

- us-gaap_DebtDisclosureAbstract
  - aapl_CommercialPaperCashFlowSummaryTableTextBlock
  - us-gaap_ScheduleOfDebtInstrumentsTextBlock
  - us-gaap_ScheduleOfMaturitiesOfLongTermDebtTableTextBlock

### http://www.apple.com/role/DebtAdditionalInformationDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_ShortTermDebtTypeAxis
      - us-gaap_ShortTermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_CommercialPaper
      - us-gaap_DebtInstrumentTerm
      - us-gaap_ShortTermDebtWeightedAverageInterestRate
      - us-gaap_ProceedsFromOtherShortTermDebt
      - us-gaap_RepaymentsOfOtherShortTermDebt
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_InterestExpenseDebt
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
      - aapl_HedgeAccountingAdjustmentsRelatedToTermDebt
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

### http://www.apple.com/role/CommitmentsandContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.apple.com/role/CommitmentsandContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_ScheduleOfProductWarrantyLiabilityTableTextBlock
  - us-gaap_UnrecordedUnconditionalPurchaseObligationsDisclosureTextBlock

### http://www.apple.com/role/CommitmentsandContingenciesChangesinAccruedWarrantiesandRelatedCostsDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_MovementInStandardProductWarrantyAccrualRollForward
    - us-gaap_StandardProductWarrantyAccrual
    - us-gaap_StandardProductWarrantyAccrualPayments
    - us-gaap_StandardProductWarrantyAccrualWarrantiesIssued
    - us-gaap_StandardProductWarrantyAccrual

### http://www.apple.com/role/CommitmentsandContingenciesFuturePaymentsUnderUnconditionalPurchaseObligationsDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_UnrecordedUnconditionalPurchaseObligationAbstract
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnFirstAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnSecondAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnThirdAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnFourthAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnFifthAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationDueAfterFiveYears
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceSheetAmount [totalLabel]

### http://www.apple.com/role/CommitmentsandContingenciesAdditionalInformationDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - aapl_CommitmentsAndContingenciesDisclosureTable
    - srt_LitigationCaseAxis
      - srt_LitigationCaseTypeDomain
    - us-gaap_LitigationStatusAxis
      - us-gaap_LitigationStatusDomain
    - aapl_CommitmentsAndContingenciesDisclosureLineItems
      - us-gaap_LitigationSettlementAmountAwardedToOtherParty

### http://www.apple.com/role/SegmentInformationandGeographicData

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.apple.com/role/SegmentInformationandGeographicDataTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
  - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTextBlock
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsByGeographicalAreasTableTextBlock

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

