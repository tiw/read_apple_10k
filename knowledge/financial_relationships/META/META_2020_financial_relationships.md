# META 2020 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.facebook.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_DepreciationDepletionAndAmortization
  - us-gaap_ShareBasedCompensation
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.facebook.com/role/ConsolidatedStatementsOfComprehensiveIncome

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
    - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
    - fb_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesAdjustmentAndOtherNetofTax
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.facebook.com/role/ConsolidatedStatementsOfIncome

- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
    - us-gaap_IncomeStatementLocationAxis
      - us-gaap_IncomeStatementLocationDomain
    - us-gaap_StatementLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
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
    - us-gaap_EarningsPerShareBasicLineItems
      - us-gaap_EarningsPerShareBasicAbstract
      - us-gaap_EarningsPerShareDilutedAbstract

### http://www.facebook.com/role/EarningsPerShareTables

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock

### http://www.facebook.com/role/GeographicalInformationScheduleOfPropertyAndEquipmentDetails

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - srt_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

### http://www.facebook.com/role/GoodwillAndIntangibleAssetsScheduleOfAmortizationExpenseDetails

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

### http://www.facebook.com/role/IncomeTaxesNarrativeDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - fb_IncomeTaxDisclosureTable
    - us-gaap_IncomeTaxAuthorityNameAxis
      - us-gaap_IncomeTaxAuthorityNameDomain
    - srt_LitigationCaseAxis
      - srt_LitigationCaseTypeDomain
    - us-gaap_TaxPeriodAxis
      - us-gaap_TaxPeriodDomain
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - srt_RangeAxis
      - srt_RangeMember
    - fb_IncomeTaxDisclosureLineItems
      - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_TaxCreditCarryforwardAmount
      - fb_EventCausingOwnershipChangeAndLossInNetOperatingLossAndTaxCreditCarryforwardCumulativeStockOwnershipChangeThreshhold
      - fb_EventCausingOwnershipChangeAndLossInNetOperatingLossAndTaxCreditCarryforwardChangeInOwnershipPercentageOverPeriod
      - us-gaap_IncomeTaxExaminationPenaltiesAndInterestAccrued
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_PaymentsForOtherTaxes
      - us-gaap_IncomeTaxExaminationEstimateOfPossibleLoss

### http://www.facebook.com/role/IncomeTaxesScheduleForIncomeBeforeIncomeTaxDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]

### http://www.facebook.com/role/IncomeTaxesScheduleOfDeferredTaxAssetsAndLiabilitiesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ComponentsOfDeferredTaxAssetsAndLiabilitiesAbstract
    - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
      - us-gaap_DeferredTaxAssetsOperatingLossCarryforwards
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwards
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccrualsAccruedLiabilities
      - fb_DeferredTaxAssetsLeaseLiabilities
      - us-gaap_DeferredTaxAssetsOther
      - us-gaap_DeferredTaxAssetsGross [totalLabel]
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_DeferredTaxAssetsNet [totalLabel]
    - us-gaap_ComponentsOfDeferredTaxLiabilitiesAbstract
      - us-gaap_DeferredTaxLiabilitiesPropertyPlantAndEquipment
      - us-gaap_DeferredTaxLiabilitiesLeasingArrangements
      - us-gaap_DeferredTaxLiabilitiesGoodwillAndIntangibleAssetsIntangibleAssets
      - us-gaap_DeferredIncomeTaxLiabilities
    - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]

### http://www.facebook.com/role/IncomeTaxesScheduleOfEffectiveIncomeTaxRateReconciliationDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_EffectiveIncomeTaxRateContinuingOperationsTaxRateReconciliationAbstract
    - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
    - us-gaap_EffectiveIncomeTaxRateReconciliationStateAndLocalIncomeTaxes
    - us-gaap_EffectiveIncomeTaxRateReconciliationTaxCreditsResearch
    - us-gaap_EffectiveIncomeTaxRateReconciliationNondeductibleExpenseShareBasedCompensationCost
    - fb_EffectiveTaxRateReconciliationShareBasedCompensationExcessTaxBenefitPercent
    - us-gaap_EffectiveIncomeTaxRateReconciliationForeignIncomeTaxRateDifferential
    - us-gaap_EffectiveIncomeTaxRateReconciliationTaxCutsAndJobsActOf2017Percent
    - fb_EffectiveTaxRateReconciliationNonDeductibleFederalTradeCommissionSettlementAccrualPercent
    - us-gaap_EffectiveIncomeTaxRateReconciliationOtherAdjustments
    - us-gaap_EffectiveIncomeTaxRateContinuingOperations [totalLabel]

### http://www.facebook.com/role/IncomeTaxesScheduleOfProvisionForIncomeTaxesDetails

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

### http://www.facebook.com/role/IncomeTaxesScheduleOfUnrecognizedTaxBenefitsDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ReconciliationOfUnrecognizedTaxBenefitsExcludingAmountsPertainingToExaminedTaxReturnsRollForward
    - us-gaap_UnrecognizedTaxBenefits
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
    - us-gaap_UnrecognizedTaxBenefits

### http://www.facebook.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfUnrecognizedTaxBenefitsRollForwardTableTextBlock

### http://www.facebook.com/role/InterestAndOtherIncomeNet

- us-gaap_NonoperatingIncomeExpenseAbstract
  - us-gaap_OtherNonoperatingIncomeAndExpenseTextBlock

### http://www.facebook.com/role/InterestAndOtherIncomeNetDetails

- us-gaap_NonoperatingIncomeExpenseAbstract
  - us-gaap_InvestmentIncomeInterest
  - us-gaap_InterestExpense
  - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_NonoperatingIncomeExpense [totalLabel]

### http://www.facebook.com/role/InterestAndOtherIncomeNetTables

- us-gaap_NonoperatingIncomeExpenseAbstract
  - us-gaap_ScheduleOfOtherNonoperatingIncomeExpenseTableTextBlock

### http://www.facebook.com/role/Revenue

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueFromContractWithCustomerTextBlock

### http://www.facebook.com/role/RevenueScheduleOfDeferredRevenueAndDepositsDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_ContractWithCustomerLiability
  - fb_ContractWithCustomerDepositsUnusedBalances
  - fb_ContractWithCustomerLiabilityAndUnusedDeposits [totalLabel]

### http://www.facebook.com/role/RevenueScheduleOfDisaggregationOfRevenueDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_DisaggregationOfRevenueTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_DisaggregationOfRevenueLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

### http://www.facebook.com/role/RevenueTables

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_DisaggregationOfRevenueTableTextBlock
  - us-gaap_ContractWithCustomerAssetAndLiabilityTableTextBlock

## 资产负债表结构 (Balance Sheet Structure)

### http://www.facebook.com/role/CashAndCashEquivalentsAndMarketableSecurities

- fb_CashandCashEquivalentsandMarketableSecuritiesAbstract
  - us-gaap_CashCashEquivalentsAndShortTermInvestmentsTextBlock

### http://www.facebook.com/role/CashAndCashEquivalentsAndMarketableSecuritiesNarrativeDetails

- fb_CashandCashEquivalentsandMarketableSecuritiesAbstract
  - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
  - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
  - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPosition12MonthsOrLongerAccumulatedLoss

### http://www.facebook.com/role/CashAndCashEquivalentsAndMarketableSecuritiesScheduleOfCashAndCashEquivalentsAndMarketableSecuritiesDetails

- fb_CashandCashEquivalentsandMarketableSecuritiesAbstract
  - fb_ScheduleOfCashCashEquivalentsAndMarketableSecuritiesTable
    - us-gaap_FinancialInstrumentAxis
    - us-gaap_CashAndCashEquivalentsAxis
      - us-gaap_RestrictedCashAndCashEquivalentsCashAndCashEquivalentsMember
    - fb_CashCashEquivalentsAndMarketableSecuritiesLineItems
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_AvailableForSaleSecuritiesDebtSecuritiesCurrent
      - fb_CashCashEquivalentsAndMarketableSecuritiesAtCarryingValue [totalLabel]

### http://www.facebook.com/role/CashAndCashEquivalentsAndMarketableSecuritiesScheduleOfContractualMaturitiesOfDebtSecuritiesDetails

- fb_CashandCashEquivalentsandMarketableSecuritiesAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtSecuritiesCurrent [totalLabel]

### http://www.facebook.com/role/CashAndCashEquivalentsAndMarketableSecuritiesTables

- fb_CashandCashEquivalentsandMarketableSecuritiesAbstract
  - us-gaap_ScheduleOfCashCashEquivalentsAndShortTermInvestmentsTableTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock

### http://www.facebook.com/role/ConsolidatedBalanceSheets

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_AssetsAbstract
    - us-gaap_AssetsCurrentAbstract
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_AvailableForSaleSecuritiesDebtSecuritiesCurrent
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_PrepaidExpenseAndOtherAssetsCurrent
      - us-gaap_AssetsCurrent [totalLabel]
    - fb_PropertyPlantAndEquipmentAndFinanceLeaseRightofUseAssetAfterAccumulatedDepreciationAndAmortization
    - us-gaap_PropertyPlantAndEquipmentNet
    - us-gaap_OperatingLeaseRightOfUseAsset
    - us-gaap_IntangibleAssetsNetExcludingGoodwill
    - us-gaap_Goodwill
    - us-gaap_OtherAssetsNoncurrent
    - us-gaap_Assets [totalLabel]
  - us-gaap_LiabilitiesAndStockholdersEquityAbstract
    - us-gaap_LiabilitiesCurrentAbstract
      - us-gaap_AccountsPayableCurrent
      - us-gaap_AccountsPayableTradeCurrent
      - us-gaap_OperatingLeaseLiabilityCurrent
      - us-gaap_AccruedLiabilitiesCurrent
      - us-gaap_ContractWithCustomerLiabilityCurrent
      - us-gaap_LiabilitiesCurrent [totalLabel]
    - us-gaap_OperatingLeaseLiabilityNoncurrent
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
  - us-gaap_StatementTable
- us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
  - us-gaap_PaymentsRelatedToTaxWithholdingForShareBasedCompensation
  - us-gaap_PaymentsForRepurchaseOfCommonStock
  - us-gaap_FinanceLeasePrincipalPayments
  - us-gaap_ProceedsFromRepaymentsOfBankOverdrafts
  - us-gaap_ProceedsFromPaymentsForOtherFinancingActivities
  - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
- us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
  - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
  - us-gaap_PaymentsToAcquireMarketableSecurities
  - us-gaap_ProceedsFromSaleOfAvailableForSaleSecuritiesDebt
  - us-gaap_ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities
  - fb_PaymentsToAcquireBusinessesNetOfCashAcquiredAndPurchasesOfIntangibleAndOtherAssets
  - us-gaap_PaymentsForProceedsFromOtherInvestingActivities
  - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
- us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
- us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffectAbstract
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_RestrictedCashAndCashEquivalents
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
- us-gaap_SupplementalCashFlowInformationAbstract
  - us-gaap_IncomeTaxesPaidNet
  - us-gaap_CashFlowNoncashInvestingAndFinancingActivitiesDisclosureAbstract
    - fb_IncreaseDecreaseInPrepaidsAndLiabilitiesRelatedToPropertyAndEquipmentAdditions
    - us-gaap_CapitalExpendituresIncurredButNotYetPaid

### http://www.facebook.com/role/ConsolidatedStatementsOfStockholdersEquity

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
  - us-gaap_StockIssuedDuringPeriodSharesAcquisitions
  - us-gaap_StockIssuedDuringPeriodValueAcquisitions
  - fb_NewAccountingPronouncementOrTaxCutsAndJobsActOf2017EffectOfAdoption
  - us-gaap_StockIssuedDuringPeriodSharesStockOptionsExercised
  - us-gaap_StockIssuedDuringPeriodValueStockOptionsExercised
  - fb_StockIssuedDuringPeriodSharesRestrictedStockUnitBeforeTaxSettlement
  - fb_StockIssuedDuringPeriodValueRestrictedStockUnitBeforeTaxSettlement
  - us-gaap_SharesPaidForTaxWithholdingForShareBasedCompensation
  - us-gaap_AdjustmentsRelatedToTaxWithholdingForShareBasedCompensation
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
  - us-gaap_StockRepurchasedDuringPeriodShares
  - us-gaap_StockRepurchasedDuringPeriodValue
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
  - us-gaap_FinancialInstrumentAxis
  - us-gaap_CashAndCashEquivalentsAxis
    - us-gaap_RestrictedCashAndCashEquivalentsCashAndCashEquivalentsMember
      - us-gaap_MoneyMarketFundsMember
      - us-gaap_USGovernmentDebtSecuritiesMember
      - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
      - us-gaap_BankTimeDepositsMember
      - us-gaap_CorporateDebtSecuritiesMember
  - us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_CashAndCashEquivalentsFairValueDisclosure
    - us-gaap_AvailableForSaleSecuritiesDebtSecuritiesCurrent
    - us-gaap_AssetsFairValueDisclosure [totalLabel]

### http://www.facebook.com/role/GoodwillAndIntangibleAssets

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillAndIntangibleAssetsDisclosureTextBlock

### http://www.facebook.com/role/GoodwillAndIntangibleAssetsScheduleOfAmortizationExpenseDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseCurrentAndFiveSucceedingFiscalYearsAbstract

### http://www.facebook.com/role/GoodwillAndIntangibleAssetsScheduleOfChangeInCarryingAmountDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillRollForward
    - us-gaap_Goodwill
    - us-gaap_GoodwillAcquiredDuringPeriod
    - us-gaap_GoodwillForeignCurrencyTranslationGainLoss
    - us-gaap_Goodwill

### http://www.facebook.com/role/GoodwillAndIntangibleAssetsScheduleOfIntangibleAssetsDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_AmortizationOfIntangibleAssets
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.facebook.com/role/GoodwillAndIntangibleAssetsTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTextBlock
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTableTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.facebook.com/role/LeasesScheduleOfSupplementalCashFlowDetails

- fb_CashFlowLesseeAbstract
  - us-gaap_OperatingLeasePayments
  - us-gaap_FinanceLeaseInterestPaymentOnLiability
  - us-gaap_FinanceLeasePrincipalPayments
- fb_RightOfUseAssetObtainedInExchangeForLeaseLiabilityAbstract
  - fb_OperatingLeaseLiabilityInExchangeForRightOfUseAssetObtained
  - fb_FinanceLeaseLiabilityInExchangeForRightOfUseAssetObtained

### http://www.facebook.com/role/PropertyAndEquipmentDetails

- fb_LongLivedTangibleAssetAxis
  - fb_LongLivedTangibleAssetAxisDomain
    - fb_FinanceLeaseRightOfUseAssetMember
    - us-gaap_LandMember
    - us-gaap_BuildingMember
    - us-gaap_LeaseholdImprovementsMember
    - us-gaap_ComputerEquipmentMember
    - fb_ComputerSoftwareOfficeEquipmentAndOtherMember
    - us-gaap_ConstructionInProgressMember

### http://www.facebook.com/role/StockholdersEquity

- us-gaap_EquityAbstract
  - us-gaap_ShareholdersEquityAndShareBasedPaymentsTextBlock

### http://www.facebook.com/role/StockholdersEquityAdditionalAwardDisclosuresDetails

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable

### http://www.facebook.com/role/StockholdersEquityCommonStockDetails

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfStockByClassTable

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

### http://www.facebook.com/role/StockholdersEquityShareBasedCompensationPlansDetails

- us-gaap_EquityAbstract
  - us-gaap_ShareBasedCompensationAbstract

### http://www.facebook.com/role/StockholdersEquityShareRepurchaseProgramDetails

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfStockByClassTable

### http://www.facebook.com/role/StockholdersEquityStockOptionAwardActivityDetails

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable

### http://www.facebook.com/role/StockholdersEquityTables

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationStockOptionsActivityTableTextBlock
  - us-gaap_ScheduleOfShareBasedCompensationRestrictedStockUnitsAwardActivityTableTextBlock

## 现金流量表结构 (Cash Flow Structure)

### http://www.facebook.com/role/CashAndCashEquivalentsAndMarketableSecuritiesScheduleOfCashAndCashEquivalentsAndMarketableSecuritiesDetails

- us-gaap_FinancialInstrumentAxis
  - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
    - us-gaap_USGovernmentDebtSecuritiesMember
    - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
    - us-gaap_CorporateDebtSecuritiesMember

### http://www.facebook.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_StatementTable
  - us-gaap_BalanceSheetLocationAxis
    - us-gaap_BalanceSheetLocationDomain
      - us-gaap_PrepaidExpensesAndOtherCurrentAssetsMember
      - us-gaap_OtherAssetsMember
  - us-gaap_StatementLineItems
    - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
    - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect [totalLabel]
    - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
    - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
    - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffectAbstract
    - us-gaap_SupplementalCashFlowInformationAbstract
- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets
  - us-gaap_IncreaseDecreaseInOtherOperatingAssets
  - us-gaap_IncreaseDecreaseInAccountsPayableTrade
  - us-gaap_IncreaseDecreaseInOtherAccountsPayable
  - us-gaap_IncreaseDecreaseInAccruedLiabilities
  - us-gaap_IncreaseDecreaseInContractWithCustomerLiability
  - us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities

### http://www.facebook.com/role/LeasesScheduleOfMaturitiesOfLeaseLiabilitiesDetails

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
  - us-gaap_OperatingLeaseLiabilityCurrent
  - us-gaap_OperatingLeaseLiabilityNoncurrent

### http://www.facebook.com/role/LeasesScheduleOfSupplementalCashFlowDetails

- us-gaap_LeasesAbstract
  - fb_CashFlowLesseeAbstract
  - fb_RightOfUseAssetObtainedInExchangeForLeaseLiabilityAbstract

## 股东权益结构 (Equity Structure)

### http://www.facebook.com/role/ConsolidatedStatementsOfStockholdersEquity

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward

### http://www.facebook.com/role/CoverPage

- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - us-gaap_CommonClassAMember
    - us-gaap_CommonClassBMember

### http://www.facebook.com/role/StockholdersEquityAdditionalAwardDisclosuresDetails

- us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_AwardTypeAxis
    - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
      - us-gaap_RestrictedStockUnitsRSUMember
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
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

### http://www.facebook.com/role/StockholdersEquityShareBasedCompensationPlansDetails

- us-gaap_ShareBasedCompensationAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - us-gaap_PlanNameAxis
      - us-gaap_PlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - fb_ShareBasedEmployeeCompensationPlansNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_CommonStockCapitalSharesReservedForFutureIssuance
      - fb_SharesReservedForIssuanceIncreasePercentage
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfAdditionalSharesAuthorized

### http://www.facebook.com/role/StockholdersEquityShareRepurchaseProgramDetails

- us-gaap_ScheduleOfStockByClassTable
  - us-gaap_SubsequentEventTypeAxis
    - us-gaap_SubsequentEventTypeDomain
      - us-gaap_SubsequentEventMember
  - us-gaap_ClassOfStockLineItems
    - us-gaap_StockRepurchaseProgramAuthorizedAmount1
    - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
    - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
    - us-gaap_StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1
    - fb_StockRepurchaseProgramIncreaseInAuthorizedAmount

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
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePriceRollforward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsExercisesInPeriodWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
    - fb_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsWeightedAverageRemainingContractualTermAbstract
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsOutstandingWeightedAverageRemainingContractualTerm2
    - fb_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsAggregateIntrinsicValueAbstract
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingIntrinsicValue
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodGross
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsForfeituresAndExpirationsInPeriod
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue [totalLabel]

## 其他结构 (Other Structure)

### http://www.facebook.com/role/CommitmentsAndContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.facebook.com/role/CommitmentsAndContingenciesDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - fb_CommitmentsAndContingenciesDisclosureTable
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - srt_LitigationCaseAxis
      - srt_LitigationCaseTypeDomain
    - fb_CommitmentsAndContingenciesDisclosureLineItems
      - us-gaap_ContractualObligation
      - us-gaap_LongtermPurchaseCommitmentPeriod
      - us-gaap_LossContingencyNewClaimsFiledNumber
      - us-gaap_LossContingencyAccrualAtCarryingValue

### http://www.facebook.com/role/CoverPage

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
      - dei_DocumentsIncorporatedByReferenceTextBlock
      - dei_AmendmentFlag
      - dei_DocumentFiscalYearFocus
      - dei_DocumentFiscalPeriodFocus
      - dei_EntityCentralIndexKey
      - dei_CurrentFiscalYearEndDate

### http://www.facebook.com/role/FairValueMeasurement

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueDisclosuresTextBlock

### http://www.facebook.com/role/FairValueMeasurementDetails

- us-gaap_FinancialInstrumentAxis
  - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
    - us-gaap_USGovernmentDebtSecuritiesMember
    - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
    - us-gaap_CorporateDebtSecuritiesMember
- us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueInputsLevel1Member
    - us-gaap_FairValueInputsLevel2Member
    - us-gaap_FairValueInputsLevel3Member
- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable

### http://www.facebook.com/role/FairValueMeasurementTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_ScheduleOfFairValueAssetsAndLiabilitiesMeasuredOnRecurringBasisTableTextBlock

### http://www.facebook.com/role/GeographicalInformation

- us-gaap_SegmentsGeographicalAreasAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.facebook.com/role/GeographicalInformationScheduleOfPropertyAndEquipmentDetails

- us-gaap_SegmentsGeographicalAreasAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - us-gaap_NonUsMember

### http://www.facebook.com/role/GeographicalInformationTables

- us-gaap_SegmentsGeographicalAreasAbstract
  - us-gaap_LongLivedAssetsByGeographicAreasTableTextBlock

### http://www.facebook.com/role/Leases

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeasesTextBlock
  - us-gaap_LesseeFinanceLeasesTextBlock

### http://www.facebook.com/role/LeasesNarrativeDetails

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_LesseeLeaseDescriptionLineItems
      - us-gaap_OperatingLeasesRentExpenseNet
      - fb_LesseeOperatingLeaseLeaseNotYetCommencedAmount
      - fb_LesseeFinanceLeaseLeaseNotYetCommencedAmount
      - fb_LesseeLeaseLeaseNotYetCommencedTermOfContract

### http://www.facebook.com/role/LeasesScheduleOfComponentsOfLeaseCostDetails

- us-gaap_LeasesAbstract
  - us-gaap_LeaseCostAbstract
    - us-gaap_FinanceLeaseRightOfUseAssetAmortization
    - us-gaap_FinanceLeaseInterestExpense
  - us-gaap_OperatingLeaseCost
  - us-gaap_VariableLeaseCost
  - us-gaap_LeaseCost [totalLabel]
  - fb_LesseeWeightedAverageRemainingLeaseTermAbstract
    - us-gaap_OperatingLeaseWeightedAverageRemainingLeaseTerm1
    - us-gaap_FinanceLeaseWeightedAverageRemainingLeaseTerm1
  - fb_LesseeWeightedAverageDiscountRateAbstract
    - us-gaap_OperatingLeaseWeightedAverageDiscountRatePercent
    - us-gaap_FinanceLeaseWeightedAverageDiscountRatePercent

### http://www.facebook.com/role/LeasesScheduleOfMaturitiesOfLeaseLiabilitiesDetails

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
    - us-gaap_FinanceLeaseLiabilityCurrent
    - us-gaap_FinanceLeaseLiabilityNoncurrent

### http://www.facebook.com/role/LeasesTables

- us-gaap_LeasesAbstract
  - us-gaap_LeaseCostTableTextBlock
  - us-gaap_FinanceLeaseLiabilityMaturityTableTextBlock
  - us-gaap_LesseeOperatingLeaseLiabilityMaturityTableTextBlock

### http://www.facebook.com/role/Liabilities

- us-gaap_AccountsPayableAndAccruedLiabilitiesCurrentAndNoncurrentAbstract
  - fb_AccountsPayableAccruedLiabilitiesandOtherLiabilitiesDisclosureCurrentandNoncurrentTextBlock

### http://www.facebook.com/role/LiabilitiesDetails

- us-gaap_AccountsPayableAndAccruedLiabilitiesCurrentAndNoncurrentAbstract
  - us-gaap_LossContingenciesTable
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - srt_LitigationCaseAxis
      - srt_LitigationCaseTypeDomain
    - us-gaap_LossContingenciesLineItems
      - us-gaap_LossContingencyAccrualAtCarryingValue
      - us-gaap_EmployeeRelatedLiabilitiesCurrent
      - fb_PropertyAndEquipmentAccruedLiabilities
      - us-gaap_TaxesPayableCurrent
      - fb_NotionalCashPoolOverdraftBalance
      - us-gaap_OtherAccruedLiabilitiesCurrent
      - us-gaap_AccruedLiabilitiesCurrent [totalLabel]
      - us-gaap_OtherLiabilitiesAbstract

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
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_LineOfCredit

### http://www.facebook.com/role/PropertyAndEquipment

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.facebook.com/role/PropertyAndEquipmentDetails

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - fb_LongLivedTangibleAssetAxis
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - fb_FinanceLeaseRightofUseAssetbeforeAccumulatedAmortization
      - fb_PropertyPlantAndEquipmentAndFinanceLeaseRightofUseAssetBeforeAccumulatedDepreciationAndAmortization [totalLabel]
      - fb_PropertyPlantAndEquipmentAndFinanceLeaseRightofUseAssetAccumulatedDepreciationAndAmortization
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - fb_PropertyPlantAndEquipmentAndFinanceLeaseRightofUseAssetAfterAccumulatedDepreciationAndAmortization
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]
      - us-gaap_Depreciation
  - us-gaap_InterestCostsCapitalized

### http://www.facebook.com/role/PropertyAndEquipmentTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.facebook.com/role/SummaryOfSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfPresentationAndSignificantAccountingPoliciesTextBlock

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesNarrativeDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - us-gaap_ConcentrationRiskByTypeAxis
      - us-gaap_ConcentrationRiskTypeDomain
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_AdvertisingExpense
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - fb_OperatingAndFinanceLeaseRightOfUseAsset
      - fb_OperatingAndFinanceLeaseLiability
      - us-gaap_FinanceLeaseRightOfUseAsset
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentNetOfTax
      - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
      - us-gaap_ConcentrationRiskPercentage1
      - us-gaap_NumberOfReportableSegments
      - us-gaap_NumberOfOperatingSegments

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfAccountingPolicyPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_RevenueFromContractWithCustomerPolicyTextBlock
  - us-gaap_ResearchDevelopmentAndComputerSoftwarePolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_AdvertisingCostsPolicyTextBlock
  - fb_CashAndCashEquivalentsAndMarketableSecuritiesPolicyTextBlock
  - us-gaap_FairValueOfFinancialInstrumentsPolicy
  - us-gaap_TradeAndOtherAccountsReceivablePolicy
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_LesseeLeasesPolicyTextBlock
  - us-gaap_CommitmentsAndContingenciesPolicyTextBlock
  - us-gaap_BusinessCombinationsPolicy
  - fb_LongLivedAssetsIncludingGoodwillAndIntangiblePolicyTextBlock
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_ConcentrationRiskCreditRisk
  - us-gaap_SegmentReportingPolicyPolicyTextBlock
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock
  - us-gaap_EarningsPerSharePolicyTextBlock

### http://www.facebook.com/role/SummaryOfSignificantAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - fb_PropertyPlantandEquipmentUsefulLifeTableTextBlock

