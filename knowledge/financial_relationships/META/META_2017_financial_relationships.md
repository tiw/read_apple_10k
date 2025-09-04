# META 2017 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.facebook.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_DepreciationDepletionAndAmortization
  - us-gaap_ShareBasedCompensation
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - fb_TaxBenefitfromSharebasedCompensationOperatingActivities
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.facebook.com/role/ConsolidatedStatementsOfComprehensiveIncome

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
    - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
    - fb_OtherComprehensiveIncomeLossAvailableforsaleSecuritiesAdjustmentandOtherNetofTax
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.facebook.com/role/ConsolidatedStatementsOfIncome

- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
    - us-gaap_IncomeStatementLocationAxis
      - us-gaap_IncomeStatementLocationDomain
    - us-gaap_StatementLineItems
      - us-gaap_Revenues
      - us-gaap_CostsAndExpensesAbstract
      - us-gaap_OperatingIncomeLoss [totalLabel]
      - us-gaap_NonoperatingIncomeExpense
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_NetIncomeLoss [totalLabel]
      - us-gaap_UndistributedEarningsLossAllocatedToParticipatingSecuritiesBasic
      - us-gaap_NetIncomeLossAvailableToCommonStockholdersBasic [totalLabel]
      - us-gaap_EarningsPerShareAbstract
      - us-gaap_WeightedAverageNumberOfSharesOutstandingDilutedDisclosureItemsAbstract
      - us-gaap_IncomeStatementCompensationItemsAbstract

### http://www.facebook.com/role/EarningsPerShare

- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareTextBlock

### http://www.facebook.com/role/EarningsPerShareDetails

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfEarningsPerShareBasicByCommonClassTable
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_EarningsPerShareBasicLineItems
      - us-gaap_EarningsPerShareBasicAbstract
      - us-gaap_EarningsPerShareDilutedAbstract

### http://www.facebook.com/role/EarningsPerShareTables

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock

### http://www.facebook.com/role/GeographicalInformationPropertyAndEquipmentDetails

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - us-gaap_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_PropertyPlantAndEquipmentNet

### http://www.facebook.com/role/GeographicalInformationRevenueDetails

- us-gaap_SegmentsGeographicalAreasAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
    - us-gaap_StatementGeographicalAxis
      - us-gaap_SegmentGeographicalDomain
    - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
      - us-gaap_Revenues

### http://www.facebook.com/role/GoodwillAndIntangibleAssetsAmortizationExpenseDetails

- us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseCurrentAndFiveSucceedingFiscalYearsAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.facebook.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.facebook.com/role/IncomeTaxesDeferredTaxAssetsAndLiabilitiesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ComponentsOfDeferredTaxAssetsAndLiabilitiesAbstract
    - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
      - us-gaap_DeferredTaxAssetsOperatingLossCarryforwards
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwards
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccrualsAccruedLiabilities
      - us-gaap_DeferredTaxAssetsOther
      - us-gaap_DeferredTaxAssetsGross [totalLabel]
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_DeferredTaxAssetsNet [totalLabel]
    - us-gaap_ComponentsOfDeferredTaxLiabilitiesAbstract
      - us-gaap_DeferredTaxLiabilitiesPropertyPlantAndEquipment
      - us-gaap_DeferredTaxLiabilitiesGoodwillAndIntangibleAssetsIntangibleAssets
      - us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings
      - us-gaap_DeferredIncomeTaxLiabilities
    - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]

### http://www.facebook.com/role/IncomeTaxesEffectiveIncomeTaxRateReconciliationDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_EffectiveIncomeTaxRateContinuingOperationsTaxRateReconciliationAbstract
    - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
    - us-gaap_EffectiveIncomeTaxRateReconciliationStateAndLocalIncomeTaxes
    - us-gaap_EffectiveIncomeTaxRateReconciliationTaxCreditsResearch
    - us-gaap_EffectiveIncomeTaxRateReconciliationNondeductibleExpenseShareBasedCompensationCost
    - fb_EffectiveTaxRateReconciliationShareBasedCompensationExcessTaxBenefitPercent
    - us-gaap_EffectiveIncomeTaxRateReconciliationForeignIncomeTaxRateDifferential
    - us-gaap_EffectiveIncomeTaxRateReconciliationOtherAdjustments
    - us-gaap_EffectiveIncomeTaxRateContinuingOperations [totalLabel]

### http://www.facebook.com/role/IncomeTaxesNarrativeDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - fb_IncomeTaxDisclosureTable
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - fb_IncomeTaxDisclosureLineItems
      - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_OperatingLossCarryforwards
      - fb_OperatingLossCarryforwardsExpirationYear
      - us-gaap_TaxCreditCarryforwardAmount
      - fb_TaxCreditCarryforwardExpirationYear
      - fb_EventCausingOwnershipChangeAndLossInNetOperatingLossAndTaxCreditCarryforwardCumulativeStockOwnershipChangeThreshhold
      - fb_EventCausingOwnershipChangeAndLossInNetOperatingLossAndTaxCreditCarryforwardChangeInOwnershipPercentageOverPeriod
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
      - us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings
      - us-gaap_UndistributedEarningsOfForeignSubsidiaries
      - us-gaap_IncomeTaxExaminationPenaltiesAndInterestAccrued
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - us-gaap_IncomeTaxExaminationEstimateOfPossibleLoss

### http://www.facebook.com/role/IncomeTaxesProvisionForIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxExpenseBenefitContinuingOperationsAbstract
    - us-gaap_CurrentIncomeTaxExpenseBenefitContinuingOperationsAbstract
      - us-gaap_CurrentFederalTaxExpenseBenefit
      - us-gaap_CurrentStateAndLocalTaxExpenseBenefit
      - us-gaap_CurrentForeignTaxExpenseBenefit
      - us-gaap_CurrentIncomeTaxExpenseBenefit [totalLabel]
    - us-gaap_DeferredIncomeTaxExpenseBenefitContinuingOperationsAbstract
      - us-gaap_DeferredFederalIncomeTaxExpenseBenefit
      - us-gaap_DeferredStateAndLocalIncomeTaxExpenseBenefit
      - us-gaap_DeferredForeignIncomeTaxExpenseBenefit
      - fb_TotalDeferredIncomeTaxExpenseBenefit [totalLabel]
    - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.facebook.com/role/IncomeTaxesScheduleForIncomeBeforeIncomeTaxDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]

### http://www.facebook.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfUnrecognizedTaxBenefitsRollForwardTableTextBlock

### http://www.facebook.com/role/IncomeTaxesUnrecognizedTaxBenefitsDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ReconciliationOfUnrecognizedTaxBenefitsExcludingAmountsPertainingToExaminedTaxReturnsRollForward
    - us-gaap_UnrecognizedTaxBenefits
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
    - us-gaap_UnrecognizedTaxBenefits

### http://www.facebook.com/role/InterestAndOtherIncomeExpenseNet

- us-gaap_NonoperatingIncomeExpenseAbstract
  - us-gaap_OtherNonoperatingIncomeAndExpenseTextBlock

### http://www.facebook.com/role/InterestAndOtherIncomeExpenseNetDetails

- us-gaap_NonoperatingIncomeExpenseAbstract
  - us-gaap_InterestExpense
  - us-gaap_InvestmentIncomeInterest
  - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_NonoperatingIncomeExpense [totalLabel]

### http://www.facebook.com/role/InterestAndOtherIncomeExpenseNetTables

- us-gaap_NonoperatingIncomeExpenseAbstract
  - us-gaap_ScheduleOfOtherNonoperatingIncomeExpenseTableTextBlock

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesOtherPoliciesDetails

- fb_DeferredRevenueAndDepositsAbstract
  - fb_DeferredRevenueRateOfPayableCreatedUponSatisfactionOfRevenueRecognition
  - us-gaap_DeferredRevenueCurrent
  - us-gaap_OtherDeferredCreditsCurrent
  - us-gaap_DeferredRevenueAndCreditsCurrent [totalLabel]

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesRecentlyIssuedAndAdoptedAccountingPronouncementDetails

- us-gaap_IncomeStatementRelatedDisclosuresAbstract
  - us-gaap_AllocatedShareBasedCompensationExpense
  - us-gaap_CostsAndExpenses
  - us-gaap_IncomeTaxExpenseBenefit
  - us-gaap_NetIncomeLoss
  - us-gaap_EffectiveIncomeTaxRateContinuingOperations

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesRevenueRecognitionDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_AdvertisingRevenue
  - us-gaap_OtherSalesRevenueNet
  - us-gaap_Revenues [totalLabel]
  - fb_AdvertisingArrangementTerm

## 资产负债表结构 (Balance Sheet Structure)

### http://www.facebook.com/role/CashAndCashEquivalentsAndMarketableSecurities

- fb_CashAndCashEquivalentsAndMarketableSecuritiesAbstract
  - us-gaap_CashCashEquivalentsAndShortTermInvestmentsTextBlock

### http://www.facebook.com/role/CashAndCashEquivalentsAndMarketableSecuritiesContractualMaturitiesOfDebtSecuritiesDetails

- fb_CashAndCashEquivalentsAndMarketableSecuritiesAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsFairValue
  - us-gaap_MarketableSecuritiesCurrent [totalLabel]

### http://www.facebook.com/role/CashAndCashEquivalentsAndMarketableSecuritiesDetails

- fb_CashAndCashEquivalentsAndMarketableSecuritiesAbstract
  - fb_ScheduleOfCashCashEquivalentsAndMarketableSecuritiesTable
    - us-gaap_CashAndCashEquivalentsAxis
      - us-gaap_RestrictedCashAndCashEquivalentsCashAndCashEquivalentsMember
    - invest_InvestmentAxis
    - fb_CashCashEquivalentsAndMarketableSecuritiesLineItems
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_MarketableSecuritiesCurrent
      - fb_CashCashEquivalentsAndMarketableSecuritiesAtCarryingValue [totalLabel]

### http://www.facebook.com/role/CashAndCashEquivalentsAndMarketableSecuritiesTables

- fb_CashAndCashEquivalentsAndMarketableSecuritiesAbstract
  - us-gaap_ScheduleOfCashCashEquivalentsAndShortTermInvestmentsTableTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock

### http://www.facebook.com/role/ConsolidatedBalanceSheets

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_AssetsAbstract
    - us-gaap_AssetsCurrentAbstract
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_MarketableSecuritiesCurrent
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_PrepaidExpenseAndOtherAssetsCurrent
      - us-gaap_AssetsCurrent [totalLabel]
    - us-gaap_PropertyPlantAndEquipmentNet
    - us-gaap_IntangibleAssetsNetExcludingGoodwill
    - us-gaap_Goodwill
    - us-gaap_OtherAssetsNoncurrent
    - us-gaap_Assets [totalLabel]
  - us-gaap_LiabilitiesAndStockholdersEquityAbstract
    - us-gaap_LiabilitiesCurrentAbstract
      - us-gaap_AccountsPayableCurrent
      - us-gaap_AccountsPayableOtherCurrent
      - us-gaap_AccruedLiabilitiesCurrent
      - us-gaap_DeferredRevenueAndCreditsCurrent
      - us-gaap_CapitalLeaseObligationsCurrent
      - us-gaap_LiabilitiesCurrent [totalLabel]
    - us-gaap_CapitalLeaseObligationsNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent
    - us-gaap_Liabilities [totalLabel]
    - us-gaap_CommitmentsAndContingencies
    - us-gaap_StockholdersEquityAbstract
      - us-gaap_CommonStockValue
      - us-gaap_AdditionalPaidInCapital
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
      - us-gaap_RetainedEarningsAccumulatedDeficit
      - us-gaap_StockholdersEquity [totalLabel]
    - us-gaap_LiabilitiesAndStockholdersEquity [totalLabel]

### http://www.facebook.com/role/ConsolidatedBalanceSheetsParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_StatementLineItems
      - us-gaap_AssetsCurrentAbstract
      - us-gaap_StockholdersEquityAbstract

### http://www.facebook.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetIncomeLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
    - us-gaap_PaymentsToAcquireMarketableSecurities
    - us-gaap_ProceedsFromSaleOfAvailableForSaleSecurities
    - us-gaap_ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities
    - fb_PaymentsToAcquireBusinessesNetOfCashAcquiredAndPurchasesOfIntangibleAndOtherAssets
    - fb_IncreaseDecreaseInRestrictedCashAndDeposits
    - us-gaap_PaymentsForProceedsFromOtherInvestingActivities
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - fb_RepaymentsOfCapitalLeaseAndOtherFinancingObligations
    - us-gaap_ProceedsFromPaymentsForOtherFinancingActivities
    - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
  - us-gaap_EffectOfExchangeRateOnCashAndCashEquivalents
  - us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease [totalLabel]
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_SupplementalCashFlowInformationAbstract
    - fb_CashPaidDuringPeriodForAbstract
      - us-gaap_InterestPaid
      - us-gaap_IncomeTaxesPaidNet
    - us-gaap_CashFlowNoncashInvestingAndFinancingActivitiesDisclosureAbstract
      - us-gaap_CapitalExpendituresIncurredButNotYetPaid
      - us-gaap_OtherSignificantNoncashTransactionValueOfConsiderationGiven1
      - us-gaap_NotesIssued1
      - fb_SettlementOfContingentConsiderationLiability

### http://www.facebook.com/role/ConsolidatedStatementsOfStockholdersEquity

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
  - us-gaap_CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption
  - us-gaap_StockIssuedDuringPeriodSharesStockOptionsExercised
  - us-gaap_StockIssuedDuringPeriodValueStockOptionsExercised
  - us-gaap_StockIssuedDuringPeriodSharesAcquisitions
  - us-gaap_StockIssuedDuringPeriodValueAcquisitions
  - fb_StockIssuedDuringPeriodSharesRestrictedStockUnitBeforeTaxSettlement
  - fb_StockIssuedDuringPeriodValueRestrictedStockUnitBeforeTaxSettlement
  - us-gaap_SharesPaidForTaxWithholdingForShareBasedCompensation
  - us-gaap_AdjustmentsRelatedToTaxWithholdingForShareBasedCompensation
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalTaxEffectFromShareBasedCompensation
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent
  - us-gaap_NetIncomeLoss
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember
    - us-gaap_AdditionalPaidInCapitalMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
    - us-gaap_RetainedEarningsMember

### http://www.facebook.com/role/FairValueMeasurementDetails

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_FairValueByMeasurementFrequencyAxis
  - us-gaap_CashAndCashEquivalentsAxis
    - us-gaap_RestrictedCashAndCashEquivalentsCashAndCashEquivalentsMember
      - us-gaap_MoneyMarketFundsMember
      - us-gaap_USGovernmentDebtSecuritiesMember
      - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
      - us-gaap_CorporateDebtSecuritiesMember
  - invest_InvestmentAxis
  - us-gaap_FairValueByLiabilityClassAxis
    - us-gaap_FairValueLiabilitiesMeasuredOnRecurringBasisUnobservableInputReconciliationByLiabilityClassDomain
      - us-gaap_OtherCurrentLiabilitiesMember
      - us-gaap_OtherNoncurrentLiabilitiesMember
  - us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_CashAndCashEquivalentsFairValueDisclosure
    - us-gaap_MarketableSecuritiesCurrent
    - us-gaap_AssetsFairValueDisclosure [totalLabel]
    - us-gaap_BusinessCombinationContingentConsiderationLiabilityCurrent
    - us-gaap_BusinessCombinationContingentConsiderationLiability
    - us-gaap_BusinessCombinationContingentConsiderationArrangementsChangeInAmountOfContingentConsiderationLiability1

### http://www.facebook.com/role/GoodwillAndIntangibleAssets

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillAndIntangibleAssetsDisclosureTextBlock

### http://www.facebook.com/role/GoodwillAndIntangibleAssetsAmortizationExpenseDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseCurrentAndFiveSucceedingFiscalYearsAbstract

### http://www.facebook.com/role/GoodwillAndIntangibleAssetsChangeInCarryingAmountDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillRollForward
    - us-gaap_Goodwill
    - us-gaap_GoodwillAcquiredDuringPeriod
    - us-gaap_GoodwillForeignCurrencyTranslationGainLoss
    - us-gaap_Goodwill

### http://www.facebook.com/role/GoodwillAndIntangibleAssetsIntangibleAssetsDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_IntangibleAssetsGrossExcludingGoodwill [totalLabel]
  - us-gaap_IntangibleAssetsNetExcludingGoodwill [totalLabel]
  - us-gaap_AmortizationOfIntangibleAssets
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]
  - us-gaap_ScheduleOfIndefiniteLivedIntangibleAssetsTable
    - us-gaap_IndefiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_IndefiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_IndefiniteLivedIntangibleAssetsByMajorClassLineItems
      - us-gaap_IndefiniteLivedIntangibleAssetsExcludingGoodwill

### http://www.facebook.com/role/GoodwillAndIntangibleAssetsTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTextBlock
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTableTextBlock
  - us-gaap_ScheduleOfIndefiniteLivedIntangibleAssetsTableTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.facebook.com/role/StockholdersEquity

- us-gaap_EquityAbstract
  - us-gaap_ShareholdersEquityAndShareBasedPaymentsTextBlock

### http://www.facebook.com/role/StockholdersEquityAdditionalAwardDisclosuresDetails

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable

### http://www.facebook.com/role/StockholdersEquityCommonStockDetails

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfStockByClassTable

### http://www.facebook.com/role/StockholdersEquityReclassificationsDetails

- us-gaap_EquityAbstract
  - fb_StockDividendSharesofCapitalStockIssuedforEachShareofCommonStock

### http://www.facebook.com/role/StockholdersEquityRsuAwardActivityDetails

- fb_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsWeightedAverageGrantDateFairValueAbstract
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
- fb_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsRollforwardAbstract
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber

### http://www.facebook.com/role/StockholdersEquityShareBasedCompensationPlansDetail

- us-gaap_EquityAbstract
  - us-gaap_ShareBasedCompensationAbstract

### http://www.facebook.com/role/StockholdersEquityShareRepurchaseProgramDetails

- us-gaap_EquityAbstract
  - us-gaap_StockRepurchaseProgramAuthorizedAmount1

### http://www.facebook.com/role/StockholdersEquityStockOptionAwardActivityDetails

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable

### http://www.facebook.com/role/StockholdersEquityStockOptionsAdditionalDisclosuresDetails

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationSharesAuthorizedUnderStockOptionPlansByExercisePriceRangeTable

### http://www.facebook.com/role/StockholdersEquityTables

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationStockOptionsActivityTableTextBlock
  - us-gaap_ScheduleOfShareBasedCompensationSharesAuthorizedUnderStockOptionPlansByExercisePriceRangeTextBlock
  - us-gaap_ScheduleOfShareBasedCompensationRestrictedStockUnitsAwardActivityTableTextBlock

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesIntangibleAssetsDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_GoodwillAndIntangibleAssetImpairment

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesRecentlyIssuedAndAdoptedAccountingPronouncementDetails

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_RetainedEarningsMember
- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivities
  - us-gaap_NetCashProvidedByUsedInFinancingActivities

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesShareBasedCompensationDetails

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_AdditionalPaidInCapitalMember

## 现金流量表结构 (Cash Flow Structure)

### http://www.facebook.com/role/CashAndCashEquivalentsAndMarketableSecuritiesDetails

- invest_InvestmentAxis
  - invest_InvestmentDomain
    - us-gaap_USGovernmentDebtSecuritiesMember
    - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
    - us-gaap_CorporateDebtSecuritiesMember

### http://www.facebook.com/role/CommitmentsAndContingenciesDetails

- us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueCurrent
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInTwoYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInThreeYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFourYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFiveYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueThereafter
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDue [totalLabel]
- fb_FinancingObligationFutureMinimumPaymentsDueAbstract
  - fb_FinancingObligationBuildingInProgressLeasedFacilityFutureMinimumPaymentsDueCurrent
  - fb_FinancingObligationBuildingInProgressLeasedFacilityFutureMinimumPaymentsDueInTwoYears
  - fb_FinancingObligationBuildingInProgressLeasedFacilityFutureMinimumPaymentsDueInThreeYears
  - fb_FinancingObligationBuildingInProgressLeasedFacilityFutureMinimumPaymentsDueInFourYears
  - fb_FinancingObligationBuildingInProgressLeasedFacilityFutureMinimumPaymentsDueInFiveYears
  - fb_FinancingObligationBuildingInProgressLeasedFacilityFutureMinimumPaymentsDueThereafter
  - fb_FinancingObligationBuildingInProgressLeasedFacilityFutureMinimumPaymentsDue [totalLabel]

### http://www.facebook.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets
  - us-gaap_IncreaseDecreaseInOtherOperatingAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInOtherAccountsPayable
  - us-gaap_IncreaseDecreaseInAccruedLiabilities
  - us-gaap_IncreaseDecreaseInDeferredRevenueAndCustomerAdvancesAndDeposits
  - us-gaap_IncreaseDecreaseInOtherOperatingLiabilities

## 股东权益结构 (Equity Structure)

### http://www.facebook.com/role/ConsolidatedStatementsOfStockholdersEquity

- us-gaap_StatementTable
  - us-gaap_NewAccountingPronouncementEarlyAdoptionAxis
    - us-gaap_NewAccountingPrinciplesEarlyAdoptionMember
      - us-gaap_NewAccountingPronouncementEarlyAdoptionEffectMember
  - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
    - us-gaap_TypeOfAdoptionMember
      - fb_AccountingStandardsUpdate201609ExcessIncomeTaxBenefitComponentMember
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward

### http://www.facebook.com/role/DocumentAndEntityInformation

- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - us-gaap_CommonClassAMember
    - us-gaap_CommonClassBMember

### http://www.facebook.com/role/StockholdersEquityAdditionalAwardDisclosuresDetails

- us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_AwardTypeAxis
    - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
      - us-gaap_RestrictedStockUnitsRSUMember
      - fb_OtherAwardsMember
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
    - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
    - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]

### http://www.facebook.com/role/StockholdersEquityCommonStockDetails

- us-gaap_ScheduleOfStockByClassTable
  - us-gaap_StatementClassOfStockAxis
    - us-gaap_ClassOfStockDomain
      - us-gaap_CommonClassAMember
      - us-gaap_CommonClassBMember
  - us-gaap_ClassOfStockLineItems
    - us-gaap_CommonStockSharesAuthorized
    - us-gaap_CommonStockParOrStatedValuePerShare
    - fb_CommonStockNumberOfVotesByClass
    - us-gaap_CommonStockSharesIssued
    - us-gaap_CommonStockSharesOutstanding

### http://www.facebook.com/role/StockholdersEquityRsuAwardActivityDetails

- us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_AwardTypeAxis
    - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
      - us-gaap_RestrictedStockUnitsRSUMember
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
    - fb_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsRollforwardAbstract
    - fb_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsWeightedAverageGrantDateFairValueAbstract
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]

### http://www.facebook.com/role/StockholdersEquityShareBasedCompensationPlansDetail

- us-gaap_ShareBasedCompensationAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_PlanNameAxis
      - us-gaap_PlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - fb_ShareBasedEmployeeCompensationPlansNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAuthorized
      - fb_SharesReservedForIssuanceIncreaseDate
      - fb_SharesReservedForIssuanceIncreasePercentage
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
      - us-gaap_DeferredCompensationArrangementWithIndividualRequisiteServicePeriod1

### http://www.facebook.com/role/StockholdersEquityStockOptionAwardActivityDetails

- us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_StatementClassOfStockAxis
    - us-gaap_ClassOfStockDomain
      - us-gaap_CommonClassAMember
  - us-gaap_AwardTypeAxis
    - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
      - us-gaap_EmployeeStockOptionMember
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
      - us-gaap_StockIssuedDuringPeriodSharesStockOptionsExercised
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisableNumber
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePriceRollforward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsExercisesInPeriodWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisableWeightedAverageExercisePrice
    - fb_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsWeightedAverageRemainingContractualTermAbstract
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsOutstandingWeightedAverageRemainingContractualTerm2
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsExercisableWeightedAverageRemainingContractualTerm1
    - fb_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsAggregateIntrinsicValueAbstract
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingIntrinsicValue
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsExercisableIntrinsicValue1
    - us-gaap_SharePrice
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodGross
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsForfeituresAndExpirationsInPeriod
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue [totalLabel]
    - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsVestedInPeriodFairValue1

### http://www.facebook.com/role/StockholdersEquityStockOptionsAdditionalDisclosuresDetails

- us-gaap_ScheduleOfShareBasedCompensationSharesAuthorizedUnderStockOptionPlansByExercisePriceRangeTable
  - us-gaap_ShareBasedCompensationSharesAuthorizedUnderStockOptionPlansByExercisePriceRangeAxis
    - us-gaap_ShareBasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeDomain
      - fb_ExercisePriceRange029033Member
      - fb_ExercisePriceRange185Member
      - fb_ExercisePriceRange295Member
      - fb_ExercisePriceRange1039Member
      - fb_ExercisePriceRange1500Member
  - us-gaap_ShareBasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeLineItems
    - us-gaap_ShareBasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeLowerRangeLimit
    - us-gaap_ShareBasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeUpperRangeLimit
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
    - us-gaap_SharebasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeOutstandingOptionsWeightedAverageRemainingContractualTerm2
    - us-gaap_SharebasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeOutstandingOptionsWeightedAverageExercisePriceBeginningBalance1
    - us-gaap_ShareBasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeNumberOfExercisableOptions
    - us-gaap_SharebasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeExercisableOptionsWeightedAverageExercisePrice1

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesRecentlyIssuedAndAdoptedAccountingPronouncementDetails

- us-gaap_WeightedAverageNumberOfSharesOutstandingDilutedDisclosureItemsAbstract
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding
- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesShareBasedCompensationDetails

- us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardRequisiteServicePeriod1

## 其他结构 (Other Structure)

### http://www.facebook.com/role/CommitmentsAndContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.facebook.com/role/CommitmentsAndContingenciesDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - fb_CommitmentsAndContingenciesDisclosureTable
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - us-gaap_LossContingenciesByNatureOfContingencyAxis
      - us-gaap_LossContingencyNatureDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - fb_CommitmentsAndContingenciesDisclosureLineItems
      - us-gaap_LeasesAbstract
      - fb_FinancingObligationBuildingInProgressLeasedFacility
      - us-gaap_OperatingLeasesRentExpenseNet
      - fb_ContractualObligationAbstract
      - us-gaap_LossContingencyInformationAboutLitigationMattersAbstract

### http://www.facebook.com/role/CommitmentsAndContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_ScheduleOfFutureMinimumRentalPaymentsForOperatingLeasesTableTextBlock

### http://www.facebook.com/role/DocumentAndEntityInformation

- fb_DocumentandEntityInformationAbstract
  - dei_EntitiesTable
    - us-gaap_StatementClassOfStockAxis
    - dei_EntityInformationLineItems
      - dei_DocumentType
      - dei_AmendmentFlag
      - dei_DocumentPeriodEndDate
      - dei_DocumentFiscalYearFocus
      - dei_DocumentFiscalPeriodFocus
      - dei_TradingSymbol
      - dei_EntityRegistrantName
      - dei_EntityCentralIndexKey
      - dei_CurrentFiscalYearEndDate
      - dei_EntityFilerCategory
      - dei_EntityCommonStockSharesOutstanding
      - dei_EntityPublicFloat
      - dei_EntityWellKnownSeasonedIssuer
      - dei_EntityVoluntaryFilers
      - dei_EntityCurrentReportingStatus

### http://www.facebook.com/role/FairValueMeasurement

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueDisclosuresTextBlock

### http://www.facebook.com/role/FairValueMeasurementDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueInputsLevel1Member
    - us-gaap_FairValueInputsLevel2Member
    - us-gaap_FairValueInputsLevel3Member
- invest_InvestmentAxis
  - invest_InvestmentDomain
    - us-gaap_USGovernmentDebtSecuritiesMember
    - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
    - us-gaap_CorporateDebtSecuritiesMember
- us-gaap_FairValueByMeasurementFrequencyAxis
  - us-gaap_FairValueMeasurementFrequencyDomain
    - us-gaap_FairValueMeasurementsRecurringMember

### http://www.facebook.com/role/FairValueMeasurementTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_ScheduleOfFairValueAssetsAndLiabilitiesMeasuredOnRecurringBasisTableTextBlock

### http://www.facebook.com/role/GeographicalInformation

- us-gaap_SegmentsGeographicalAreasAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.facebook.com/role/GeographicalInformationPropertyAndEquipmentDetails

- us-gaap_SegmentsGeographicalAreasAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- us-gaap_StatementGeographicalAxis
  - us-gaap_SegmentGeographicalDomain
    - country_US
    - fb_RestOfWorldMember
    - country_SE

### http://www.facebook.com/role/GeographicalInformationTables

- us-gaap_SegmentsGeographicalAreasAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsByGeographicalAreasTableTextBlock

### http://www.facebook.com/role/Liabilities

- us-gaap_AccountsPayableAndAccruedLiabilitiesCurrentAndNoncurrentAbstract
  - fb_AccountsPayableAccruedLiabilitiesandOtherLiabilitiesDisclosureCurrentandNoncurrentTextBlock

### http://www.facebook.com/role/LiabilitiesDetails

- us-gaap_AccountsPayableAndAccruedLiabilitiesCurrentAndNoncurrentAbstract
  - us-gaap_AccruedLiabilitiesAndOtherLiabilitiesAbstract
    - us-gaap_EmployeeRelatedLiabilitiesCurrent
    - fb_PropertyandEquipmentAccruedLiabilities
    - us-gaap_NotesPayableCurrent
    - us-gaap_BusinessCombinationContingentConsiderationLiabilityCurrent
    - us-gaap_OtherAccruedLiabilitiesCurrent
    - us-gaap_AccruedLiabilitiesCurrent [totalLabel]
  - us-gaap_OtherLiabilitiesAbstract
    - us-gaap_LiabilityForUncertainTaxPositionsNoncurrent
    - us-gaap_BusinessCombinationContingentConsiderationLiabilityNoncurrent
    - us-gaap_OtherSundryLiabilitiesNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.facebook.com/role/LiabilitiesTables

- us-gaap_AccountsPayableAndAccruedLiabilitiesCurrentAndNoncurrentAbstract
  - us-gaap_ScheduleOfAccruedLiabilitiesTableTextBlock
  - us-gaap_OtherLiabilitiesTableTextBlock

### http://www.facebook.com/role/LongTermDebt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_LongTermDebtTextBlock

### http://www.facebook.com/role/LongTermDebtBorrowingsDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentTerm
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_LineOfCredit

### http://www.facebook.com/role/PropertyAndEquipment

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.facebook.com/role/PropertyAndEquipmentDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]
  - us-gaap_Depreciation
  - us-gaap_CapitalLeasedAssetsGross
  - us-gaap_CapitalLeasesLesseeBalanceSheetAssetsByMajorClassAccumulatedDeprecation
  - us-gaap_InterestCostsCapitalized

### http://www.facebook.com/role/PropertyAndEquipmentTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.facebook.com/role/SubsequentEvent

- us-gaap_SubsequentEventsAbstract
  - us-gaap_SubsequentEventsTextBlock

### http://www.facebook.com/role/SummaryOfSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfPresentationAndSignificantAccountingPoliciesTextBlock

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesCreditRiskAndConcentrationDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ConcentrationRiskTable
    - us-gaap_ConcentrationRiskByTypeAxis
      - us-gaap_ConcentrationRiskTypeDomain
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - us-gaap_StatementGeographicalAxis
      - us-gaap_SegmentGeographicalDomain
    - us-gaap_ConcentrationRiskLineItems
      - us-gaap_ConcentrationRiskPercentage1
      - us-gaap_ProvisionForDoubtfulAccounts

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesForeignCurrencyDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentNetOfTax
  - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesOtherPoliciesDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_AdvertisingExpense
  - fb_DeferredRevenueAndDepositsAbstract

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfAccountingPolicyPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - us-gaap_CostOfSalesPolicyTextBlock
  - us-gaap_ShareBasedCompensationOptionAndIncentivePlansPolicy
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_AdvertisingCostPolicyExpensedAdvertisingCost
  - fb_CashAndCashEquivalentsAndMarketableSecuritiesPolicyTextBlock
  - us-gaap_FairValueOfFinancialInstrumentsPolicy
  - us-gaap_TradeAndOtherAccountsReceivablePolicy
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_LeasePolicyTextBlock
  - us-gaap_CommitmentsAndContingenciesPolicyTextBlock
  - us-gaap_BusinessCombinationsPolicy
  - fb_LongLivedAssetsIncludingGoodwillAndIntangiblePolicyTextBlock
  - us-gaap_RevenueRecognitionDeferredRevenue
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_ConcentrationRiskCreditRisk
  - us-gaap_SegmentReportingPolicyPolicyTextBlock
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesPropertyEquipmentDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesRecentlyIssuedAndAdoptedAccountingPronouncementDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NewAccountingPronouncementEarlyAdoptionTable
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_NewAccountingPronouncementEarlyAdoptionAxis
      - us-gaap_NewAccountingPrinciplesEarlyAdoptionMember
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_NewAccountingPronouncementEarlyAdoptionLineItems
      - us-gaap_CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption
      - us-gaap_ExcessTaxBenefitFromShareBasedCompensationFinancingActivities
      - us-gaap_ExcessTaxBenefitFromShareBasedCompensationOperatingActivities
      - fb_AccountingStandardsUpdateASU201609IncomeTaxExpenseBenefit
      - us-gaap_BalanceSheetRelatedDisclosuresAbstract
      - us-gaap_IncomeStatementRelatedDisclosuresAbstract
      - us-gaap_EarningsPerShareAbstract
      - us-gaap_WeightedAverageNumberOfSharesOutstandingDilutedDisclosureItemsAbstract
      - us-gaap_StatementOfCashFlowsAbstract

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesShareBasedCompensationDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTextBlock
  - fb_PropertyPlantAndEqiupmentUsefulLifeTableTextBlock
  - fb_DeferredRevenueAndDepositsTableTextBlock
  - us-gaap_NewAccountingPronouncementEarlyAdoptionTableTextBlock

