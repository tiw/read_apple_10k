# AMZN 2018 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.amazon.com/role/AccumulatedOtherComprehensiveLossDetails

- us-gaap_AccumulatedOtherComprehensiveIncomeLossTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossLineItems
    - us-gaap_AOCIAttributableToParentNetOfTaxRollForward

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsExpectedFutureAmortizationExpenseOfAcquiredIntangibleAssetsDetails

- us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.amazon.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_DepreciationDepletionAndAmortization
  - us-gaap_ShareBasedCompensation
  - us-gaap_OtherOperatingActivitiesCashFlowStatement
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.amazon.com/role/ConsolidatedStatementsOfComprehensiveIncome

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
    - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
    - us-gaap_OtherComprehensiveIncomeAvailableForSaleSecuritiesAdjustmentNetOfTaxPeriodIncreaseDecreaseAbstract
      - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesAdjustmentNetOfTax [totalLabel]
    - us-gaap_OtherComprehensiveIncomeLossNetOfTax [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.amazon.com/role/ConsolidatedStatementsOfComprehensiveIncomeParenthetical

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentTax
  - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodTax
  - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesTax

### http://www.amazon.com/role/ConsolidatedStatementsOfOperations

- us-gaap_IncomeStatementAbstract
  - us-gaap_SalesRevenueGoodsNet
  - us-gaap_SalesRevenueServicesNet
  - us-gaap_SalesRevenueNet [totalLabel]
  - us-gaap_CostsAndExpensesAbstract
    - us-gaap_CostOfGoodsAndServicesSold
    - amzn_FulfillmentExpense
    - us-gaap_MarketingExpense
    - amzn_TechnologyAndContentExpense
    - us-gaap_GeneralAndAdministrativeExpense
    - us-gaap_OtherCostAndExpenseOperating
    - us-gaap_CostsAndExpenses [totalLabel]
  - us-gaap_OperatingIncomeLoss [totalLabel]
  - us-gaap_InvestmentIncomeInterest
  - us-gaap_InterestExpense
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_NonoperatingIncomeExpense [totalLabel]
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments [totalLabel]
  - us-gaap_IncomeTaxExpenseBenefit
  - us-gaap_IncomeLossFromEquityMethodInvestments
  - us-gaap_NetIncomeLoss [totalLabel]
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted
  - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesOtherIncomeExpenseNetDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
  - us-gaap_MarketableSecuritiesRealizedGainLoss
  - us-gaap_DerivativeTable
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativeLineItems
      - us-gaap_DerivativeGainLossOnDerivativeNet

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesRevenueDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ValuationAllowanceTable
    - us-gaap_ValuationAllowancesAndReservesTypeAxis
      - us-gaap_ValuationAllowancesAndReservesDomain
    - us-gaap_ValuationAllowanceLineItems
      - us-gaap_ValuationAllowancesAndReservesBalance
      - us-gaap_ValuationAllowancesAndReservesChargedToCostAndExpense
      - us-gaap_ValuationAllowancesAndReservesDeductions

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesUnearnedRevenueDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_DeferredRevenueNoncurrent
  - us-gaap_DeferredRevenueRevenueRecognized1

### http://www.amazon.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.amazon.com/role/IncomeTaxesAdditionalInformationDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxExpenseBenefit
  - us-gaap_IncomeTaxesPaidNet
  - amzn_TaxCutsAndJobsActOf2017IncompleteAccountingProvisionalIncomeTaxExpenseBenefit
  - amzn_IncomeTaxesTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_TaxCreditCarryforwardAxis
      - us-gaap_TaxCreditCarryforwardNameDomain
    - us-gaap_IncomeTaxAuthorityNameAxis
      - us-gaap_IncomeTaxAuthorityNameDomain
    - amzn_IncomeTaxesLineItems
      - us-gaap_ValuationAllowanceDeferredTaxAssetChangeInAmount
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_TaxCreditCarryforwardAmount
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestExpense
      - us-gaap_IncomeTaxExaminationEstimateOfPossibleLoss

### http://www.amazon.com/role/IncomeTaxesComponentsOfProvisionForIncomeTaxesNetDetails

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

### http://www.amazon.com/role/IncomeTaxesDeferredIncomeTaxAssetsAndLiabilitiesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - amzn_ScheduleOfDeferredIncomeTaxAssetsAndLiabilitiesTable
    - us-gaap_TaxCreditCarryforwardAxis
      - us-gaap_TaxCreditCarryforwardNameDomain
    - amzn_ScheduleOfDeferredIncomeTaxAssetsAndLiabilitiesLineItems
      - us-gaap_DeferredTaxAssetsNetAbstract
      - us-gaap_DeferredTaxLiabilitiesAbstract
      - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]
      - us-gaap_DeferredTaxLiabilities

### http://www.amazon.com/role/IncomeTaxesItemsAccountingForDifferencesBetweenIncomeTaxesComputedAtFederalStatutoryRateAndProvisionRecordedForIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
  - amzn_EffectiveIncomeTaxRateReconciliationOtherReconcilingItemsAbstract
    - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
    - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
    - us-gaap_IncomeTaxReconciliationTaxCredits
    - us-gaap_IncomeTaxReconciliationNondeductibleExpenseShareBasedCompensationCost
    - us-gaap_IncomeTaxReconciliationDeductionsQualifiedProductionActivities
    - amzn_EffectiveIncomeTaxRateReconciliationTaxCutsandJobsActof2017Amount
    - us-gaap_IncomeTaxReconciliationOtherAdjustments
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]
  - amzn_EffectiveIncomeTaxRateReconciliationSharebasedCompensationExcessTaxBenefitAmount

### http://www.amazon.com/role/IncomeTaxesReconciliationOfTaxContingenciesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ReconciliationOfUnrecognizedTaxBenefitsExcludingAmountsPertainingToExaminedTaxReturnsRollForward
    - us-gaap_UnrecognizedTaxBenefits
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsReductionsResultingFromLapseOfApplicableStatuteOfLimitations
    - us-gaap_UnrecognizedTaxBenefits
  - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate

### http://www.amazon.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_SummaryOfIncomeTaxContingenciesTextBlock

### http://www.amazon.com/role/IncomeTaxesUSAndInternationalComponentsOfIncomeBeforeIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments [totalLabel]

### http://www.amazon.com/role/SegmentInformationNetSalesAttributedToCountriesRepresentingSignificantPortionOfConsolidatedDetails

- us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTable
  - us-gaap_StatementGeographicalAxis
  - us-gaap_SegmentReportingRevenueReconcilingItemLineItems
    - us-gaap_SalesRevenueNet

### http://www.amazon.com/role/SegmentInformationNetSalesOfSimilarProductsAndServicesDetails

- us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
  - us-gaap_ProductOrServiceAxis
  - us-gaap_EntityWideInformationRevenueFromExternalCustomerLineItems
    - us-gaap_SalesRevenueNet

### http://www.amazon.com/role/SegmentInformationReportableSegmentsAndReconciliationToConsolidatedNetIncomeDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_SalesRevenueNet
      - us-gaap_CostsAndExpenses
      - us-gaap_OperatingIncomeLoss [totalLabel]
      - us-gaap_NonoperatingIncomeExpense
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_IncomeLossFromEquityMethodInvestments
      - us-gaap_NetIncomeLoss [totalLabel]

### http://www.amazon.com/role/StockholdersEquityStockBasedCompensationExpenseDetails

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - amzn_FulfillmentExpenseMember
    - amzn_MarketingExpenseMember
    - amzn_TechnologyAndContentExpenseMember
    - us-gaap_GeneralAndAdministrativeExpenseMember

## 资产负债表结构 (Balance Sheet Structure)

### http://www.amazon.com/role/AccumulatedOtherComprehensiveLoss

- us-gaap_EquityAbstract
  - us-gaap_ComprehensiveIncomeNoteTextBlock

### http://www.amazon.com/role/AccumulatedOtherComprehensiveLossDetails

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_AccumulatedTranslationAdjustmentMember
    - us-gaap_AccumulatedNetUnrealizedInvestmentGainLossMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
- us-gaap_EquityAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossTable

### http://www.amazon.com/role/AccumulatedOtherComprehensiveLossTables

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfAccumulatedOtherComprehensiveIncomeLossTableTextBlock

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssets

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_BusinessCombinationDisclosureTextBlock

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsAcquiredIntangibleAssetsDetails

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetByMajorClassTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_AcquiredFiniteLivedIntangibleAssetsLineItems
      - us-gaap_IntangibleAssetsGrossExcludingGoodwill
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_IntangibleAssetsNetExcludingGoodwill
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsAdditionalInformationDetails

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationConsiderationTransferred1
      - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
      - amzn_BusinessCombinationConsiderationTransferredEquityInterestsIssuedAndIssuableFairValue
      - us-gaap_AmortizationOfIntangibleAssets

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsAllocationOfAggregatePurchasePriceOfAcquisitionsDetails

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationConsiderationTransferredAbstract
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredGoodwillAndLiabilitiesAssumedNetAbstract
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsExpectedFutureAmortizationExpenseOfAcquiredIntangibleAssetsDetails

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsProFormaFinancialInformationDetails

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationProFormaInformationRevenueOfAcquireeSinceAcquisitionDateActual
      - us-gaap_BusinessCombinationProFormaInformationEarningsOrLossOfAcquireeSinceAcquisitionDateActual
      - us-gaap_BusinessAcquisitionsProFormaRevenue
      - us-gaap_BusinessAcquisitionsProFormaNetIncomeLoss

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsSummaryOfGoodwillActivityBySegmentDetails

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfGoodwillTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_GoodwillLineItems
      - us-gaap_GoodwillRollForward

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsTables

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfRecognizedIdentifiedAssetsAcquiredAndLiabilitiesAssumedTableTextBlock
  - us-gaap_BusinessAcquisitionProFormaInformationTextBlock
  - us-gaap_ScheduleOfGoodwillTextBlock
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetsByMajorClassTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.amazon.com/role/CashCashEquivalentsAndMarketableSecurities

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_CashCashEquivalentsAndShortTermInvestmentsTextBlock

### http://www.amazon.com/role/CashCashEquivalentsAndMarketableSecuritiesContractualMaturitiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAmortizedCostAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesFairValueAbstract

### http://www.amazon.com/role/CashCashEquivalentsAndMarketableSecuritiesFairValuesOnRecurringBasisDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_ScheduleOfInvestmentsTable
- us-gaap_CashCashEquivalentsAndShortTermInvestmentsAbstract
  - us-gaap_AvailableForSaleSecuritiesEquitySecurities
  - us-gaap_AvailableForSaleSecuritiesDebtSecurities
  - amzn_CashCashEquivalentsAndShortTermInvestmentsCurrentAndNoncurrent [totalLabel]
  - us-gaap_RestrictedCashAndInvestments
  - amzn_CashCashEquivalentsAndShortTermInvestmentsExcludingRestrictedCashAndInvestments
- us-gaap_CashAndCashEquivalentsAxis
  - us-gaap_RestrictedCashAndCashEquivalentsCashAndCashEquivalentsMember
    - us-gaap_MoneyMarketFundsMember
- us-gaap_MajorTypesOfDebtAndEquitySecuritiesAxis
  - us-gaap_MajorTypesOfDebtAndEquitySecuritiesDomain
    - us-gaap_ForeignGovernmentDebtSecuritiesMember
    - us-gaap_USTreasuryAndGovernmentMember
    - us-gaap_CorporateDebtSecuritiesMember
    - us-gaap_AssetBackedSecuritiesMember
    - us-gaap_FixedIncomeSecuritiesMember
- amzn_CashCashEquivalentsAndAvailableForSaleSecuritiesAmortizedCostBasisAbstract
  - us-gaap_AvailableForSaleEquitySecuritiesAmortizedCostBasis [totalLabel]
  - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis [totalLabel]
  - amzn_CashCashEquivalentsAndShortTermInvestmentsAmortizedCostBasis [totalLabel]

### http://www.amazon.com/role/CashCashEquivalentsAndMarketableSecuritiesGrossGrainsAndGrossLossesRealizedOnSalesOfAvailableForSaleMarketableSecuritiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_AvailableForSaleSecuritiesGrossRealizedGains
  - us-gaap_AvailableForSaleSecuritiesGrossRealizedLosses

### http://www.amazon.com/role/CashCashEquivalentsAndMarketableSecuritiesTables

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_FairValueAssetsMeasuredOnRecurringBasisTextBlock
  - us-gaap_RealizedGainLossOnInvestmentsTableTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock

### http://www.amazon.com/role/CommitmentsAndContingenciesPledgedAssetsDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - amzn_SecuritiesAndFixedAssetsOwnedAndPledgedAsCollateralFairValue

### http://www.amazon.com/role/ConsolidatedBalanceSheets

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_AssetsAbstract
    - us-gaap_AssetsCurrentAbstract
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_MarketableSecuritiesCurrent
      - us-gaap_InventoryNet
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_AssetsCurrent [totalLabel]
    - us-gaap_PropertyPlantAndEquipmentNet
    - us-gaap_Goodwill
    - us-gaap_OtherAssetsNoncurrent
    - us-gaap_Assets [totalLabel]
  - us-gaap_LiabilitiesAndStockholdersEquityAbstract
    - us-gaap_LiabilitiesCurrentAbstract
      - us-gaap_AccountsPayableCurrent
      - amzn_AccruedLiabilitiesAndOtherCurrent
      - us-gaap_DeferredRevenueCurrent
      - us-gaap_LiabilitiesCurrent [totalLabel]
    - us-gaap_LongTermDebtNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent
    - us-gaap_CommitmentsAndContingencies
    - us-gaap_StockholdersEquityAbstract
      - us-gaap_PreferredStockValue
      - us-gaap_CommonStockValue
      - us-gaap_TreasuryStockValue
      - us-gaap_AdditionalPaidInCapital
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
      - us-gaap_RetainedEarningsAccumulatedDeficit
      - us-gaap_StockholdersEquity [totalLabel]
    - us-gaap_LiabilitiesAndStockholdersEquity [totalLabel]

### http://www.amazon.com/role/ConsolidatedBalanceSheetsParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_PreferredStockParOrStatedValuePerShare
  - us-gaap_PreferredStockSharesAuthorized
  - us-gaap_PreferredStockSharesIssued
  - us-gaap_PreferredStockSharesOutstanding
  - us-gaap_CommonStockParOrStatedValuePerShare
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_CommonStockSharesIssued
  - us-gaap_CommonStockSharesOutstanding

### http://www.amazon.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetIncomeLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_PaymentsForProceedsFromProductiveAssets
    - amzn_ProceedsFromRebatesOnPurchasesOfProductiveAssets
    - amzn_PaymentsToAcquireBusinessesNetOfCashAcquiredAndOther
    - us-gaap_ProceedsFromSaleAndMaturityOfMarketableSecurities
    - us-gaap_PaymentsToAcquireMarketableSecurities
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_ProceedsFromIssuanceOfLongTermDebt
    - us-gaap_RepaymentsOfDebt
    - us-gaap_RepaymentsOfLongTermCapitalLeaseObligations
    - amzn_RepaymentsOfLongTermFinanceLeaseObligations
    - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
  - us-gaap_EffectOfExchangeRateOnCashAndCashEquivalents
  - us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease [totalLabel]
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_SupplementalCashFlowInformationAbstract
    - amzn_InterestPaidOnLongTermDebt
    - amzn_InterestPaidOnCapitalAndFinanceLeaseObligations
    - us-gaap_IncomeTaxesPaidNet
    - us-gaap_CapitalLeaseObligationsIncurred
    - amzn_BuildToSuitLeaseObligationsIncurred

### http://www.amazon.com/role/ConsolidatedStatementsOfStockholdersEquity

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_SharesOutstanding
  - us-gaap_StockholdersEquity
  - us-gaap_CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTax
  - us-gaap_StockIssuedDuringPeriodSharesStockOptionsExercised
  - us-gaap_StockIssuedDuringPeriodValueStockOptionsExercised
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalTaxEffectFromShareBasedCompensation
  - us-gaap_StockIssuedDuringPeriodValueEmployeeBenefitPlan
  - us-gaap_StockIssuedDuringPeriodValueAcquisitions
  - us-gaap_SharesOutstanding
  - us-gaap_StockholdersEquity
- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember
    - us-gaap_TreasuryStockMember
    - us-gaap_AdditionalPaidInCapitalMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
    - us-gaap_RetainedEarningsMember

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesVideoAndMusicContentDetails

- amzn_OtherAssetsTableTable
  - us-gaap_RangeAxis
  - amzn_OtherAssetsAxis
    - amzn_OtherAssetsDomain
      - amzn_DigitalVideoandMusicContentMember
  - amzn_OtherAssetsLineItems
    - amzn_OtherAssetAmortizationPeriod

### http://www.amazon.com/role/SegmentInformationReconciliationOfAssetsFromSegmentToConsolidatedDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfAssetsFromSegmentToConsolidatedTable
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingAssetReconcilingItemLineItems
      - us-gaap_Assets

### http://www.amazon.com/role/StockholdersEquityRestrictedStockUnitActivityDetails

- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueAmount
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValueAmount
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodWeightedAverageGrantDateFairValueAmount
  - amzn_ShareBasedCompensationArrangementBySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValueAmount
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueAmount

### http://www.amazon.com/role/StockholdersEquityScheduledVestingForOutstandingRestrictedStockUnitsDetails

- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsAdditionalDisclosuresAbstract
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestingNextTwelveMonths
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestingYearTwo
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestingYearThree
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestingYearFour
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestingYearFive
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestingAfterYearFive
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber [totalLabel]

## 现金流量表结构 (Cash Flow Structure)

### http://www.amazon.com/role/CashCashEquivalentsAndMarketableSecuritiesContractualMaturitiesDetails

- us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAmortizedCostAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearAmortizedCost
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsAmortizedCost
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterFiveThroughTenYearsAmortizedCost
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterTenYearsAmortizedCost
  - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis [totalLabel]
- us-gaap_AvailableForSaleSecuritiesDebtMaturitiesFairValueAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterFiveThroughTenYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterTenYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtSecurities [totalLabel]

### http://www.amazon.com/role/CashCashEquivalentsAndMarketableSecuritiesFairValuesOnRecurringBasisDetails

- us-gaap_ScheduleOfInvestmentsTable
  - us-gaap_FairValueByMeasurementFrequencyAxis
    - us-gaap_FairValueMeasurementFrequencyDomain
      - us-gaap_FairValueMeasurementsRecurringMember
  - us-gaap_FairValueByFairValueHierarchyLevelAxis
    - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
      - us-gaap_FairValueInputsLevel1Member
      - us-gaap_FairValueInputsLevel2Member
  - us-gaap_CashAndCashEquivalentsAxis
  - us-gaap_MajorTypesOfDebtAndEquitySecuritiesAxis
  - us-gaap_ScheduleOfInvestmentsLineItems
    - us-gaap_Cash
    - us-gaap_CashEquivalentsAtCarryingValue
    - amzn_CashCashEquivalentsAndAvailableForSaleSecuritiesAmortizedCostBasisAbstract
    - us-gaap_AvailableForSaleSecuritiesAccumulatedGrossUnrealizedGainBeforeTaxAbstract
      - us-gaap_AvailableForSaleEquitySecuritiesAccumulatedGrossUnrealizedGainBeforeTax
      - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
      - us-gaap_AvailableForSaleSecuritiesAccumulatedGrossUnrealizedGainBeforeTax [totalLabel]
    - us-gaap_AvailableForSaleSecuritiesAccumulatedGrossUnrealizedLossBeforeTaxAbstract
      - us-gaap_AvailableForSaleEquitySecuritiesAccumulatedGrossUnrealizedLossBeforeTax
      - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
      - us-gaap_AvailableForSaleSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
    - us-gaap_CashCashEquivalentsAndShortTermInvestmentsAbstract

### http://www.amazon.com/role/CommitmentsAndContingenciesPrincipalContractualCommitmentsExcludingOpenOrdersDetails

- us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueCurrent
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInTwoYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInThreeYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFourYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFiveYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueThereafter
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDue [totalLabel]

### http://www.amazon.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInInventories
  - us-gaap_IncreaseDecreaseInAccountsReceivableAndOtherOperatingAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities
  - us-gaap_IncreaseDecreaseInDeferredRevenue

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesAccountsReceivableNetAndOtherDetails

- us-gaap_ScheduleOfAccountsNotesLoansAndFinancingReceivableTable
  - us-gaap_AccountsNotesLoansAndFinancingReceivableByReceivableTypeAxis
    - us-gaap_ReceivableTypeDomain
  - us-gaap_AccountsNotesAndLoansReceivableLineItems

## 股东权益结构 (Equity Structure)

### http://www.amazon.com/role/ConsolidatedStatementsOfOperations

- us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding

### http://www.amazon.com/role/ConsolidatedStatementsOfStockholdersEquity

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward

### http://www.amazon.com/role/QuarterlyResultsUnauditedDetails

- us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding

### http://www.amazon.com/role/StockholdersEquity

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ShareholdersEquityAndShareBasedPaymentsTextBlock

### http://www.amazon.com/role/StockholdersEquityAdditionalInformationDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfStockByClassTable
    - us-gaap_ShareRepurchaseProgramAxis
      - us-gaap_ShareRepurchaseProgramDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ClassOfStockLineItems
      - us-gaap_PreferredStockSharesAuthorized
      - us-gaap_PreferredStockParOrStatedValuePerShare
      - us-gaap_PreferredStockSharesOutstanding
      - amzn_CommonStockSharesOutstandingIncludingNonvestedStockAwards
      - us-gaap_StockRepurchaseProgramAuthorizedAmount1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - amzn_EmployeeServiceShareBasedCompensationNonvestedAwardsCompensationCostExpectedToBeExpensedInNextTwelveMonthsPercentage
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
      - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsForfeitureRate
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
      - us-gaap_StockIssuedDuringPeriodSharesEmployeeBenefitPlan
      - us-gaap_CommonStockCapitalSharesReservedForFutureIssuance

### http://www.amazon.com/role/StockholdersEquityRestrictedStockUnitActivityDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward

### http://www.amazon.com/role/StockholdersEquityScheduledVestingForOutstandingRestrictedStockUnitsDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsAdditionalDisclosuresAbstract

### http://www.amazon.com/role/StockholdersEquityStockBasedCompensationExpenseDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
      - us-gaap_AllocatedShareBasedCompensationExpense
      - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense

### http://www.amazon.com/role/StockholdersEquityTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfCompensationCostForShareBasedPaymentArrangementsAllocationOfShareBasedCompensationCostsByPlanTableTextBlock
  - us-gaap_ScheduleOfNonvestedRestrictedStockUnitsActivityTableTextBlock
  - us-gaap_ScheduleOfShareBasedCompensationArrangementByShareBasedPaymentAwardRestrictedStockUnitsVestedAndExpectedToVestTableTextBlock

## 其他结构 (Other Structure)

### http://www.amazon.com/role/AccumulatedOtherComprehensiveLossDetails

- us-gaap_AOCIAttributableToParentNetOfTaxRollForward
  - us-gaap_StockholdersEquity
  - us-gaap_OtherComprehensiveIncomeLossNetOfTax
  - us-gaap_StockholdersEquity

### http://www.amazon.com/role/CommitmentsAndContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.amazon.com/role/CommitmentsAndContingenciesCommitmentsDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_LeaseAndRentalExpense

### http://www.amazon.com/role/CommitmentsAndContingenciesLegalProceedingsDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_LossContingenciesTable
    - us-gaap_LitigationCaseAxis
      - us-gaap_LitigationCaseTypeDomain
    - us-gaap_LitigationStatusAxis
      - us-gaap_LitigationStatusDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_LossContingenciesLineItems
      - us-gaap_LossContingencyNewClaimsFiledNumber
      - us-gaap_LossContingencyPatentsAllegedlyInfringedNumber
      - us-gaap_LossContingencyEstimateOfPossibleLoss

### http://www.amazon.com/role/CommitmentsAndContingenciesPrincipalContractualCommitmentsExcludingOpenOrdersDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_LongTermDebtByMaturityAbstract
    - amzn_LongTermDebtMaturitiesRepaymentsOfPrincipalAndInterestInNextTwelveMonths
    - amzn_LongTermDebtMaturitiesRepaymentsOfPrincipalAndInterestInYearTwo
    - amzn_LongTermDebtMaturitiesRepaymentsOfPrincipalAndInterestInYearThree
    - amzn_LongTermDebtMaturitiesRepaymentsOfPrincipalAndInterestInYearFour
    - amzn_LongTermDebtMaturitiesRepaymentsOfPrincipalAndInterestInYearFive
    - amzn_LongTermDebtMaturitiesRepaymentsOfPrincipalAndInterestAfterYearFive
    - amzn_LongTermDebtIncludingInterest [totalLabel]
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueAbstract
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueCurrent
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInTwoYears
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInThreeYears
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInFourYears
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInFiveYears
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueThereafter
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDue [totalLabel]
    - us-gaap_CapitalLeaseObligationsCurrent
    - us-gaap_CapitalLeaseObligationsNoncurrent
  - amzn_FinanceLeasesFutureMinimumPaymentsDueFiscalYearMaturityAbstract
    - amzn_FinanceLeasesFutureMinimumPaymentsDueNextTwelveMonths
    - amzn_FinanceLeasesFutureMinimumPaymentsDueInTwoYears
    - amzn_FinanceLeasesFutureMinimumPaymentsDueInThreeYears
    - amzn_FinanceLeasesFutureMinimumPaymentsDueInFourYears
    - amzn_FinanceLeasesFutureMinimumPaymentsDueInFiveYears
    - amzn_FinanceLeasesFutureMinimumPaymentsDueThereafter
    - amzn_FinanceLeasesFutureMinimumPaymentsDue [totalLabel]
    - amzn_FinanceLeaseObligationsCurrent
    - amzn_FinanceLeaseObligationsNoncurrent
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract
  - us-gaap_UnrecordedUnconditionalPurchaseObligationAbstract
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnFirstAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnSecondAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnThirdAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnFourthAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceOnFifthAnniversary
    - us-gaap_UnrecordedUnconditionalPurchaseObligationDueAfterFiveYears
    - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceSheetAmount [totalLabel]
  - us-gaap_OtherCommitmentFiscalYearMaturityAbstract
    - us-gaap_OtherCommitmentDueInNextTwelveMonths
    - us-gaap_OtherCommitmentDueInSecondYear
    - us-gaap_OtherCommitmentDueInThirdYear
    - us-gaap_OtherCommitmentDueInFourthYear
    - us-gaap_OtherCommitmentDueInFifthYear
    - us-gaap_OtherCommitmentDueAfterFifthYear
    - us-gaap_OtherCommitment [totalLabel]
  - us-gaap_ContractualObligationFiscalYearMaturityAbstract
    - us-gaap_ContractualObligationDueInNextTwelveMonths [totalLabel]
    - us-gaap_ContractualObligationDueInSecondYear [totalLabel]
    - us-gaap_ContractualObligationDueInThirdYear [totalLabel]
    - us-gaap_ContractualObligationDueInFourthYear [totalLabel]
    - us-gaap_ContractualObligationDueInFifthYear [totalLabel]
    - us-gaap_ContractualObligationDueAfterFifthYear [totalLabel]
    - us-gaap_ContractualObligation [totalLabel]
  - us-gaap_UnrecognizedTaxBenefits

### http://www.amazon.com/role/CommitmentsAndContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_ContractualObligationFiscalYearMaturityScheduleTableTextBlock

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_OrganizationConsolidationBasisOfPresentationBusinessDescriptionAndAccountingPoliciesTextBlock

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesAccountingPronouncementsNotYetAdoptedDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NewAccountingPronouncementsOrChangeInAccountingPrincipleTable
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_NewAccountingPronouncementsOrChangeInAccountingPrincipleLineItems
      - us-gaap_NewAccountingPronouncementOrChangeInAccountingPrincipleCumulativeEffectOfChangeOnEquityOrNetAssets1

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesAccountingPronouncementsRecentlyAdoptedDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NewAccountingPronouncementsOrChangeInAccountingPrincipleTable
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_NewAccountingPronouncementsOrChangeInAccountingPrincipleLineItems
      - us-gaap_CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption
      - us-gaap_NetCashProvidedByUsedInOperatingActivities
      - us-gaap_NetCashProvidedByUsedInFinancingActivities

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesAccountsReceivableNetAndOtherDetails

- us-gaap_AccountsNotesAndLoansReceivableLineItems
  - us-gaap_AccountsReceivableNetCurrent
  - us-gaap_AllowanceForDoubtfulAccountsReceivableCurrent
  - us-gaap_ProvisionForDoubtfulAccounts
  - us-gaap_AllowanceForDoubtfulAccountsReceivableWriteOffs
- us-gaap_ReceivableTypeDomain
  - us-gaap_TradeAccountsReceivableMember
  - amzn_SellerAccountsReceivableMember
  - amzn_VendorAccountsReceivableMember
- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfAccountsNotesLoansAndFinancingReceivableTable

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesAccruedExpensesAndOtherDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_AccruedLiabilitiesForUnredeeemedGiftCards
  - amzn_UnredeemedGiftCardsPeriodofRecognition

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesCalculationOfDilutedSharesDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_IncrementalCommonSharesAttributableToShareBasedPaymentArrangements
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding [totalLabel]

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesDescriptionOfBusinessDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NumberOfOperatingSegments

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesFairValueOfFinancialInstrumentsDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_FairValueByBalanceSheetGroupingTable
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueBalanceSheetGroupingFinancialStatementCaptionsLineItems
      - us-gaap_DerivativeAssets
      - us-gaap_DerivativeGainLossOnDerivativeNet

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesForeignCurrencyDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_TranslationAdjustmentFunctionalToReportingCurrencyIncreaseDecreaseGrossOfTax

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesGoodwillDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_GoodwillImpairmentLoss

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesInternalUseSoftwareAndWebsiteDevelopmentDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_CapitalizedComputerSoftwareAdditions
  - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsCapitalizedAmount
  - us-gaap_CapitalizedComputerSoftwareAmortization1

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesMarketingDetails

- us-gaap_AccountingPoliciesAbstract
  - amzn_AdvertisingAndOtherPromotionalExpense

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_SegmentReportingPolicyPolicyTextBlock
  - us-gaap_PriorPeriodReclassificationAdjustmentDescription
  - us-gaap_ConsolidationPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_EarningsPerSharePolicyTextBlock
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - us-gaap_CostOfSalesPolicyTextBlock
  - us-gaap_CostOfSalesVendorAllowancesPolicy
  - amzn_FulfillmentExpensesPolicyPolicyTextBlock
  - us-gaap_AdvertisingCostsPolicyTextBlock
  - amzn_TechnologyAndContentExpensesPolicyPolicyTextBlock
  - us-gaap_SellingGeneralAndAdministrativeExpensesPolicyTextBlock
  - us-gaap_CompensationRelatedCostsPolicyTextBlock
  - amzn_OtherOperatingIncomeAndExpensePolicyPolicyTextBlock
  - amzn_OtherNonoperatingIncomeAndExpensePolicyPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_FairValueOfFinancialInstrumentsPolicy
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_ReceivablesPolicyTextBlock
  - us-gaap_InternalUseSoftwarePolicy
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_LesseeLeasesPolicyTextBlock
  - us-gaap_AssetRetirementObligationsPolicy
  - us-gaap_GoodwillAndIntangibleAssetsGoodwillPolicy
  - amzn_OtherAssetsNoncurrentPolicyPolicyTextBlock
  - amzn_VideoAndMusicContentPolicyPolicyTextBlock
  - us-gaap_InvestmentPolicyTextBlock
  - us-gaap_ImpairmentOrDisposalOfLongLivedAssetsPolicyTextBlock
  - amzn_AccruedExpensesAndOtherPolicyPolicyTextBlock
  - us-gaap_RevenueRecognitionDeferredRevenue
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesPropertyAndEquipmentNetDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfWeightedAverageNumberOfSharesTableTextBlock

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesTechnologyAndContentDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesVideoAndMusicContentDetails

- us-gaap_RangeAxis
  - us-gaap_RangeMember
    - us-gaap_MinimumMember
    - us-gaap_MaximumMember
- us-gaap_AccountingPoliciesAbstract
  - amzn_OtherAssetsTableTable

### http://www.amazon.com/role/DocumentAndEntityInformation

- amzn_DocumentAndEntityInformationAbstract
  - dei_DocumentType
  - dei_AmendmentFlag
  - dei_DocumentPeriodEndDate
  - dei_DocumentFiscalYearFocus
  - dei_DocumentFiscalPeriodFocus
  - dei_EntityRegistrantName
  - dei_EntityCentralIndexKey
  - dei_CurrentFiscalYearEndDate
  - dei_EntityWellKnownSeasonedIssuer
  - dei_EntityCurrentReportingStatus
  - dei_EntityVoluntaryFilers
  - dei_EntityFilerCategory
  - dei_EntityPublicFloat
  - dei_EntityCommonStockSharesOutstanding

### http://www.amazon.com/role/LongTermDebt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.amazon.com/role/LongTermDebtAdditionalInformationDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - amzn_VariableRateComponentAxis
      - amzn_VariableRateComponentDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LongTermDebt
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentUnamortizedDiscountPremiumNet
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_LongTermDebtFairValue
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_DebtInstrumentTerm
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - us-gaap_LineOfCreditFacilityUnusedCapacityCommitmentFeePercentage
      - us-gaap_LineOfCredit
      - us-gaap_LongtermDebtWeightedAverageInterestRate
      - us-gaap_DebtInstrumentCollateralAmount
      - amzn_LineOfCreditFacilityNumberOfExtensions
      - amzn_LineOfCreditFacilityAdditionalTerm

### http://www.amazon.com/role/LongTermDebtFuturePrincipalPaymentForDebtDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_LongTermDebtByMaturityAbstract
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive
    - us-gaap_LongTermDebt [totalLabel]

### http://www.amazon.com/role/LongTermDebtLongTermDebtObligationsDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_LongTermDebt [totalLabel]
      - us-gaap_LongTermDebtCurrent
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage

### http://www.amazon.com/role/LongTermDebtTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtInstrumentsTextBlock
  - us-gaap_ScheduleOfMaturitiesOfLongTermDebtTableTextBlock

### http://www.amazon.com/role/OtherLongTermLiabilities

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - us-gaap_OtherLiabilitiesDisclosureTextBlock

### http://www.amazon.com/role/OtherLongTermLiabilitiesLongTermCapitalLeaseObligationDetails

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - us-gaap_CapitalLeasesFutureMinimumPaymentsNetMinimumPayments1
  - us-gaap_CapitalLeasesFutureMinimumPaymentsInterestIncludedInPayments
  - us-gaap_CapitalLeasesFutureMinimumPaymentsPresentValueOfNetMinimumPayments [totalLabel]
  - us-gaap_CapitalLeaseObligationsCurrent
  - us-gaap_CapitalLeaseObligationsNoncurrent

### http://www.amazon.com/role/OtherLongTermLiabilitiesLongTermFinanceLeaseObligationDetails

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - amzn_FinanceLeasesFutureMinimumPaymentsNetMinimumPayments
  - amzn_FinanceLeasesFutureMinimumPaymentsInterestIncludedinPayments
  - amzn_FinanceLeasesFutureMinimumPaymentsPresentValueofNetMinimumPayments [totalLabel]
  - amzn_FinanceLeaseObligationsCurrent
  - amzn_FinanceLeaseObligationsNoncurrent

### http://www.amazon.com/role/OtherLongTermLiabilitiesOtherLongTermLiabilitiesSummaryDetails

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - us-gaap_CapitalLeaseObligationsNoncurrent
  - amzn_FinanceLeaseObligationsNoncurrent
  - amzn_ConstructionLiabilitiesNoncurrent
  - us-gaap_IncomeTaxExaminationPenaltiesAndInterestAccrued
  - us-gaap_DeferredIncomeTaxLiabilitiesNet
  - us-gaap_OtherLiabilitiesAndDeferredRevenueNoncurrent
  - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.amazon.com/role/OtherLongTermLiabilitiesTables

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - us-gaap_OtherLiabilitiesTableTextBlock
  - amzn_ScheduleOfCapitalLeaseObligationsTextBlock
  - amzn_ScheduleofFinanceLeaseObligationsTableTextBlock

### http://www.amazon.com/role/PropertyAndEquipment

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.amazon.com/role/PropertyAndEquipmentAdditionalInformationDetails

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_Depreciation
  - us-gaap_CapitalLeasesIncomeStatementAmortizationExpense
  - us-gaap_CapitalLeasedAssetsGross
  - us-gaap_CapitalLeasesLesseeBalanceSheetAssetsByMajorClassAccumulatedDeprecation
  - amzn_FinanceLeasedAssetsGross
  - amzn_FinanceLeasesLesseeBalanceSheetAssetsbyMajorClassAccumulatedDepreciation

### http://www.amazon.com/role/PropertyAndEquipmentComponentsDetails

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]
      - us-gaap_CapitalizedComputerSoftwareGross

### http://www.amazon.com/role/PropertyAndEquipmentTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.amazon.com/role/QuarterlyResultsUnaudited

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_QuarterlyFinancialInformationTextBlock

### http://www.amazon.com/role/QuarterlyResultsUnauditedDetails

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_SalesRevenueNet
  - us-gaap_OperatingIncomeLoss
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments
  - us-gaap_IncomeTaxExpenseBenefit
  - us-gaap_NetIncomeLoss
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted
  - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract

### http://www.amazon.com/role/QuarterlyResultsUnauditedTables

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_ScheduleOfQuarterlyFinancialInformationTableTextBlock

### http://www.amazon.com/role/SegmentInformation

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.amazon.com/role/SegmentInformationAdditionalInformationDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_NumberOfOperatingSegments
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementGeographicalAxis
      - us-gaap_SegmentGeographicalDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_PropertyPlantAndEquipmentNet

### http://www.amazon.com/role/SegmentInformationDepreciationExpenseBySegmentDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_Depreciation

### http://www.amazon.com/role/SegmentInformationNetSalesAttributedToCountriesRepresentingSignificantPortionOfConsolidatedDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTable
- us-gaap_StatementGeographicalAxis
  - us-gaap_SegmentGeographicalDomain
    - country_US
    - country_DE
    - country_GB
    - country_JP
    - us-gaap_NonUsMember

### http://www.amazon.com/role/SegmentInformationNetSalesOfSimilarProductsAndServicesDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
- us-gaap_ProductOrServiceAxis
  - us-gaap_ProductsAndServicesDomain
    - amzn_OnlineStoresMember
    - amzn_PhysicalStoresMember
    - amzn_ThirdPartySellerServicesMember
    - amzn_SubscriptionServicesMember
    - amzn_AmazonWebServicesMember
    - amzn_OtherServicesMember

### http://www.amazon.com/role/SegmentInformationReconciliationOfPropertyAndEquipmentAdditionsFromSegmentsToConsolidatedDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_PropertyPlantAndEquipmentAdditions

### http://www.amazon.com/role/SegmentInformationReconciliationOfPropertyAndEquipmentFromSegmentsToConsolidatedDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfOtherSignificantReconcilingItemsFromSegmentsToConsolidatedTable
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingOtherSignificantReconcilingItemLineItems
      - us-gaap_PropertyPlantAndEquipmentNet

### http://www.amazon.com/role/SegmentInformationTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTextBlock
  - us-gaap_RevenueFromExternalCustomersByGeographicAreasTableTextBlock
  - us-gaap_ReconciliationOfAssetsFromSegmentToConsolidatedTextBlock
  - us-gaap_LongLivedAssetsByGeographicAreasTableTextBlock
  - us-gaap_ReconciliationOfOtherSignificantReconcilingItemsFromSegmentsToConsolidatedTextBlock

