# AMZN 2025 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.amazon.com/role/ConsolidatedStatementsofCashFlows

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_DepreciationDepletionAndAmortization
  - us-gaap_ShareBasedCompensation
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.amazon.com/role/ConsolidatedStatementsofOperations

- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
- us-gaap_CostsAndExpensesAbstract
  - us-gaap_CostOfGoodsAndServicesSold
  - amzn_FulfillmentExpense
  - amzn_TechnologyAndInfrastructureExpense
  - us-gaap_MarketingExpense
  - us-gaap_GeneralAndAdministrativeExpense
  - us-gaap_OtherOperatingIncomeExpenseNet
  - us-gaap_CostsAndExpenses [totalLabel]

### http://www.amazon.com/role/ConsolidatedStatementsofComprehensiveIncomeLoss

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
    - us-gaap_OtherComprehensiveIncomeForeignCurrencyTransactionAndTranslationGainLossArisingDuringPeriodNetOfTax
    - us-gaap_OtherComprehensiveIncomeAvailableforsaleSecuritiesTaxPortionAttributableToParentAbstract
      - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesAdjustmentNetOfTax [totalLabel]
      - us-gaap_OtherComprehensiveIncomeOtherNetOfTax
    - us-gaap_OtherComprehensiveIncomeLossNetOfTax [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.amazon.com/role/ConsolidatedStatementsofComprehensiveIncomeLossParenthetical

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_OtherComprehensiveIncomeForeignCurrencyTranslationGainLossArisingDuringPeriodTax
  - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodTax
  - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesTax
  - amzn_OtherComprehensiveIncomeOtherTax

### http://www.amazon.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.amazon.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfUnrecognizedTaxBenefitsRollForwardTableTextBlock

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresRevenueDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ContractWithCustomerRefundLiability
  - srt_ValuationAndQualifyingAccountsDisclosureTable
    - us-gaap_ValuationAllowancesAndReservesTypeAxis
      - us-gaap_ValuationAllowancesAndReservesDomain
    - srt_ValuationAndQualifyingAccountsDisclosureLineItems
      - us-gaap_ValuationAllowancesAndReservesChargedToCostAndExpense
      - us-gaap_ValuationAllowancesAndReservesDeductions
  - us-gaap_ContractWithCustomerRightToRecoverProduct

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresOtherIncomeExpenseNetDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_MarketableSecuritiesUnrealizedGainLoss
  - us-gaap_FairValueAdjustmentOfWarrants
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentAnnualAmount
  - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
  - amzn_MiscellaneousIncomeExpense
  - us-gaap_OtherNonoperatingIncomeExpense [totalLabel]
  - us-gaap_ScheduleOfEquityMethodInvestmentsTable
    - us-gaap_EquityMethodInvestmentNonconsolidatedInvesteeAxis
      - us-gaap_EquityMethodInvestmentNonconsolidatedInvesteeDomain
    - us-gaap_ScheduleOfEquityMethodInvestmentsLineItems
      - us-gaap_MarketableSecuritiesUnrealizedGainLoss
      - amzn_EquityInvestmentOwnershipNumberOfShares
      - amzn_EquityInvestmentOwnershipPercentage
      - amzn_EquityInvestmentVotingPercentage
      - amzn_EquityInvestmentFairValueDisclosure
      - amzn_EquityInvestmentDiscountDueToLackOfMarketability

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresAccruedExpensesandOtherDetails

- us-gaap_DisaggregationOfRevenueTable
  - srt_ProductOrServiceAxis
  - us-gaap_DisaggregationOfRevenueLineItems
    - us-gaap_EmployeeRelatedLiabilitiesCurrent
    - us-gaap_ContractWithCustomerLiability

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresUnearnedRevenueDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ContractWithCustomerLiability
  - us-gaap_ContractWithCustomerLiabilityRevenueRecognized
  - us-gaap_ContractWithCustomerLiabilityNoncurrent
  - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionTable
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionLineItems
      - us-gaap_RevenueRemainingPerformanceObligation
      - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionPeriod1

### http://www.amazon.com/role/AcquisitionsGoodwillandAcquiredIntangibleAssetsExpectedFutureAmortizationExpenseofAcquiredIntangibleAssetsDetails

- us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.amazon.com/role/StockholdersEquityStockbasedCompensationExpenseDetails

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - amzn_FulfillmentExpenseMember
    - amzn_TechnologyAndContentExpenseMember
    - us-gaap_SellingAndMarketingExpenseMember
    - us-gaap_GeneralAndAdministrativeExpenseMember

### http://www.amazon.com/role/IncomeTaxesAdditionalInformationDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxExpenseBenefit
  - us-gaap_IncomeTaxesPaidNet
  - us-gaap_OperatingLossCarryforwardsTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_OperatingLossCarryforwardsLineItems
      - us-gaap_IncomeTaxReconciliationPriorYearIncomeTaxes
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestExpense

### http://www.amazon.com/role/IncomeTaxesComponentsofProvisionforIncomeTaxesNetDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - amzn_IncomeTaxesTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - amzn_IncomeTaxesLineItems
      - us-gaap_IncomeTaxExpenseBenefitContinuingOperationsByJurisdictionAbstract

### http://www.amazon.com/role/IncomeTaxesUSandInternationalComponentsofIncomeBeforeIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments [totalLabel]

### http://www.amazon.com/role/IncomeTaxesItemsAccountingforDifferencesBetweenIncomeTaxesComputedatFederalStatutoryRateandProvisionRecordedforIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
  - amzn_EffectiveIncomeTaxRateReconciliationOtherReconcilingItemsAbstract
    - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
    - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
    - us-gaap_IncomeTaxReconciliationTaxCredits
    - us-gaap_IncomeTaxReconciliationNondeductibleExpenseShareBasedCompensationCost
    - us-gaap_EffectiveIncomeTaxRateReconciliationFdiiAmount
    - us-gaap_IncomeTaxReconciliationOtherAdjustments
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_EffectiveIncomeTaxRateReconciliationShareBasedCompensationExcessTaxBenefitAmount

### http://www.amazon.com/role/IncomeTaxesDeferredIncomeTaxAssetsandLiabilitiesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_DeferredTaxAssetsNetAbstract
    - us-gaap_DeferredTaxAssetsOperatingLossCarryforwardsDomestic
    - us-gaap_DeferredTaxAssetsOperatingLossCarryforwardsForeign
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccruals
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
    - us-gaap_DeferredTaxAssetsPropertyPlantAndEquipment
    - amzn_DeferredTaxAssetsOperatingLeaseLiabilities
    - us-gaap_DeferredTaxAssetsInProcessResearchAndDevelopment
    - us-gaap_DeferredTaxAssetsOther
    - us-gaap_DeferredTaxAssetsTaxCreditCarryforwards
    - us-gaap_DeferredTaxAssetsGross [totalLabel]
    - us-gaap_DeferredTaxAssetsValuationAllowance
    - us-gaap_DeferredTaxAssetsNet [totalLabel]
  - us-gaap_DeferredTaxLiabilitiesAbstract
    - us-gaap_DeferredTaxLiabilitiesPropertyPlantAndEquipment
    - amzn_DeferredTaxLiabilitiesOperatingLeaseAssets
    - us-gaap_DeferredTaxLiabilitiesOther
  - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]

### http://www.amazon.com/role/IncomeTaxesReconciliationofIncomeTaxContingenciesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ReconciliationOfUnrecognizedTaxBenefitsExcludingAmountsPertainingToExaminedTaxReturnsRollForward
    - us-gaap_UnrecognizedTaxBenefits
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
    - us-gaap_UnrecognizedTaxBenefitsReductionsResultingFromLapseOfApplicableStatuteOfLimitations
    - us-gaap_UnrecognizedTaxBenefits
  - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate

### http://www.amazon.com/role/SegmentInformationAdditionalInformationDetails

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - srt_StatementGeographicalAxis
  - us-gaap_SegmentReportingInformationLineItems

### http://www.amazon.com/role/SegmentInformationReportableSegmentsandReconciliationtoConsolidatedNetIncomeDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_CostsAndExpenses
      - us-gaap_OperatingIncomeLoss
      - us-gaap_NonoperatingIncomeExpense
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_IncomeLossFromEquityMethodInvestments
      - us-gaap_NetIncomeLoss [totalLabel]

### http://www.amazon.com/role/SegmentInformationDisaggregationofRevenueDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_DisaggregationOfRevenueTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_DisaggregationOfRevenueLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

### http://www.amazon.com/role/SegmentInformationNetSalesAttributedtoCountriesRepresentingPortionofConsolidatedNetSalesDetails

- us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTable
  - srt_StatementGeographicalAxis
  - us-gaap_SegmentReportingRevenueReconcilingItemLineItems
    - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

## 资产负债表结构 (Balance Sheet Structure)

### http://www.amazon.com/role/ConsolidatedStatementsofCashFlows

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetIncomeLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_PaymentsToAcquireProductiveAssets
    - amzn_ProceedsFromPropertyPlantAndEquipmentSalesAndIncentives
    - amzn_PaymentsToAcquireBusinessesNetOfCashAcquiredAndPaymentsToAcquireNonmarketableSecuritiesAndOther
    - us-gaap_ProceedsFromSaleAndMaturityOfMarketableSecurities
    - us-gaap_PaymentsToAcquireMarketableSecurities
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_PaymentsForRepurchaseOfCommonStock
    - us-gaap_ProceedsFromShortTermDebt
    - us-gaap_RepaymentsOfShortTermDebt
    - us-gaap_ProceedsFromIssuanceOfLongTermDebt
    - us-gaap_RepaymentsOfLongTermDebt
    - us-gaap_FinanceLeasePrincipalPayments
    - amzn_RepaymentsOfLongTermFinancingObligations
    - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
  - us-gaap_EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect [totalLabel]
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents

### http://www.amazon.com/role/ConsolidatedBalanceSheets

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_AssetsAbstract
    - us-gaap_AssetsCurrentAbstract
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_MarketableSecuritiesCurrent
      - us-gaap_InventoryNet
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_AssetsCurrent [totalLabel]
    - us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization
    - us-gaap_OperatingLeaseRightOfUseAsset
    - us-gaap_Goodwill
    - us-gaap_OtherAssetsNoncurrent
    - us-gaap_Assets [totalLabel]
  - us-gaap_LiabilitiesAndStockholdersEquityAbstract
    - us-gaap_LiabilitiesCurrentAbstract
      - us-gaap_AccountsPayableCurrent
      - us-gaap_AccruedLiabilitiesCurrent
      - us-gaap_ContractWithCustomerLiabilityCurrent
      - us-gaap_LiabilitiesCurrent [totalLabel]
    - amzn_LeaseLiabilityNoncurrent
    - us-gaap_LongTermDebtNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent
    - us-gaap_CommitmentsAndContingencies
    - us-gaap_StockholdersEquityAbstract
      - us-gaap_PreferredStockValue
      - us-gaap_CommonStockValue
      - us-gaap_TreasuryStockCommonValue
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

### http://www.amazon.com/role/ConsolidatedStatementsofStockholdersEquity

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember
    - us-gaap_TreasuryStockCommonMember
    - us-gaap_AdditionalPaidInCapitalMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
    - us-gaap_RetainedEarningsMember
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTax
  - us-gaap_StockIssuedDuringPeriodSharesEmployeeBenefitPlan
  - us-gaap_StockIssuedDuringPeriodValueEmployeeBenefitPlan
  - us-gaap_TreasuryStockSharesAcquired
  - us-gaap_TreasuryStockValueAcquiredCostMethod
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable

### http://www.amazon.com/role/FinancialInstruments

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_FinancialInstrumentsDisclosureTextBlock

### http://www.amazon.com/role/AcquisitionsGoodwillandAcquiredIntangibleAssets

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_BusinessCombinationDisclosureTextBlock

### http://www.amazon.com/role/FinancialInstrumentsTables

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_FairValueAssetsMeasuredOnRecurringBasisTextBlock
  - us-gaap_RealizedGainLossOnInvestmentsTableTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock
  - us-gaap_ScheduleOfCashAndCashEquivalentsTableTextBlock
  - us-gaap_ScheduleOfRestrictedCashAndCashEquivalentsTextBlock

### http://www.amazon.com/role/AcquisitionsGoodwillandAcquiredIntangibleAssetsTables

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfGoodwillTextBlock
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetsByMajorClassTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresSupplementalCashFlowInformationDetails

- us-gaap_SupplementalCashFlowInformationAbstract
  - amzn_InterestPaidOnLongTermDebt
  - us-gaap_OperatingLeasePayments
  - us-gaap_FinanceLeaseInterestPaymentOnLiability
  - amzn_InterestPaidFinancingObligations
  - us-gaap_IncomeTaxesPaidNet
  - us-gaap_RightOfUseAssetObtainedInExchangeForOperatingLeaseLiability
  - us-gaap_RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability
  - amzn_PropertyAndEquipmentObtainedInExchangeForFinancingObligations
  - amzn_PropertyAndEquipmentDerecognizedAfterConstructionPeriodBuildToSuitArrangement

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresGoodwillandIndefiniteLivedIntangibleAssetsDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_GoodwillAndIntangibleAssetImpairment

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresCashEquivalentsandMarketableSecuritiesDetails

- us-gaap_ScheduleOfEquityMethodInvestmentsTable
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_ScheduleOfEquityMethodInvestmentsLineItems
    - amzn_PaymentsToAcquireNonmarketableSecurities
    - amzn_NonmarketableSecuritiesAgreedAdditionalInvestment
    - amzn_ConvertibleNoteInstrumentsFairValueDisclosure
    - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueAmount
    - us-gaap_EquityMethodInvestments
    - us-gaap_DerivativeAssets

### http://www.amazon.com/role/FinancialInstrumentsFairValuesonRecurringBasisDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_ScheduleOfInvestmentsTable
- us-gaap_CashAndCashEquivalentsAxis
  - us-gaap_RestrictedCashAndCashEquivalentsCashAndCashEquivalentsMember
    - us-gaap_MoneyMarketFundsMember
- amzn_CashCashEquivalentsAndDebtAvailableForSaleSecuritiesAmortizedCostBasisAbstract
  - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis
  - amzn_CashCashEquivalentsAndMarketableSecuritiesAmortizedCostBasis [totalLabel]
- us-gaap_CashCashEquivalentsAndShortTermInvestmentsAbstract
  - us-gaap_EquitySecuritiesFvNi
  - us-gaap_AvailableForSaleSecuritiesDebtSecurities
  - amzn_CashCashEquivalentsAndMarketableSecurities [totalLabel]
  - us-gaap_RestrictedCashAndInvestments
  - amzn_CashCashEquivalentsAndMarketableSecuritiesExcludingRestrictedCashAndInvestments
  - us-gaap_EquitySecuritiesFvNiGainLossAbstract
    - us-gaap_EquitySecuritiesFvNiUnrealizedGainLoss

### http://www.amazon.com/role/FinancialInstrumentsGrossGainsandGrossLossesRealizedonSalesofAvailableForSaleMarketableSecuritiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_DebtSecuritiesAvailableForSaleRealizedGain
  - us-gaap_DebtSecuritiesAvailableForSaleRealizedLoss

### http://www.amazon.com/role/FinancialInstrumentsContractualMaturitiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesSingleMaturityDateAmortizedCostBasisAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesFairValueAbstract

### http://www.amazon.com/role/FinancialInstrumentsReconciliationtoCashFlowDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_RestrictedCashCurrent
  - us-gaap_RestrictedCashNoncurrent
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents [totalLabel]

### http://www.amazon.com/role/AcquisitionsGoodwillandAcquiredIntangibleAssetsAdditionalInformationDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedNoncurrentLiabilitiesLongTermDebt
      - amzn_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedVideoContentCapitalizedCosts
      - us-gaap_Goodwill
      - us-gaap_BusinessCombinationConsiderationTransferred1
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibleAssetsOtherThanGoodwill
      - us-gaap_AmortizationOfIntangibleAssets

### http://www.amazon.com/role/AcquisitionsGoodwillandAcquiredIntangibleAssetsSummaryofGoodwillActivitybySegmentDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfGoodwillTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_GoodwillLineItems
      - us-gaap_GoodwillRollForward

### http://www.amazon.com/role/AcquisitionsGoodwillandAcquiredIntangibleAssetsAcquiredIntangibleAssetsDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetByMajorClassTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_AcquiredFiniteLivedIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]
      - us-gaap_IndefiniteLivedIntangibleAssetsExcludingGoodwill
      - us-gaap_IntangibleAssetsGrossExcludingGoodwill [totalLabel]
      - us-gaap_IntangibleAssetsNetExcludingGoodwill [totalLabel]
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife

### http://www.amazon.com/role/AcquisitionsGoodwillandAcquiredIntangibleAssetsExpectedFutureAmortizationExpenseofAcquiredIntangibleAssetsDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract

### http://www.amazon.com/role/StockholdersEquityRestrictedStockUnitActivityDetails

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

### http://www.amazon.com/role/StockholdersEquityScheduledVestingforOutstandingRestrictedStockUnitsDetails

- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsAdditionalDisclosuresAbstract
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestingNextTwelveMonths
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestingYearTwo
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestingYearThree
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestingYearFour
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestingYearFive
  - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestingAfterYearFive
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber [totalLabel]

### http://www.amazon.com/role/SegmentInformationReconciliationofAssetsfromSegmenttoConsolidatedDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfAssetsFromSegmentToConsolidatedTable
    - srt_ConsolidationItemsAxis
      - srt_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingAssetReconcilingItemLineItems
      - us-gaap_Assets

## 现金流量表结构 (Cash Flow Structure)

### http://www.amazon.com/role/ConsolidatedStatementsofCashFlows

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInInventories
  - us-gaap_IncreaseDecreaseInAccountsReceivableAndOtherOperatingAssets
  - us-gaap_IncreaseDecreaseInOtherNoncurrentAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities
  - us-gaap_IncreaseDecreaseInContractWithCustomerLiability

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresSupplementalCashFlowInformationDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_SupplementalCashFlowInformationAbstract

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresAccountsReceivableNetandOtherDetails

- us-gaap_ScheduleOfAccountsNotesLoansAndFinancingReceivableTable
  - us-gaap_AccountsNotesLoansAndFinancingReceivableByReceivableTypeAxis
    - us-gaap_ReceivableTypeDomain
  - us-gaap_AccountsNotesAndLoansReceivableLineItems

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresCashEquivalentsandMarketableSecuritiesDetails

- us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueInputsLevel2Member
    - us-gaap_FairValueInputsLevel3Member
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_WarrantMember
- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfEquityMethodInvestmentsTable

### http://www.amazon.com/role/CommitmentsandContingenciesPrincipalContractualCommitmentsExcludingOpenOrdersDetails

- amzn_FinancingObligationsFutureMinimumPaymentsDueFiscalYearMaturityAbstract
  - amzn_FinancingObligationsFutureMinimumPaymentsDueNextTwelveMonths
  - amzn_FinancingObligationsFutureMinimumPaymentsDueInTwoYears
  - amzn_FinancingObligationsFutureMinimumPaymentsDueInThreeYears
  - amzn_FinancingObligationsFutureMinimumPaymentsDueInFourYears
  - amzn_FinancingObligationsFutureMinimumPaymentsDueInFiveYears
  - amzn_FinancingObligationsFutureMinimumPaymentsDueAfterYearFive
  - amzn_FinancingObligationsFutureMinimumPaymentsDue [totalLabel]
- us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueNextTwelveMonths
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearTwo
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearThree
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearFour
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearFive
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueAfterYearFive
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDue [totalLabel]

## 股东权益结构 (Equity Structure)

### http://www.amazon.com/role/ConsolidatedStatementsofOperations

- us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding

### http://www.amazon.com/role/ConsolidatedStatementsofStockholdersEquity

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward

### http://www.amazon.com/role/StockholdersEquity

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ShareholdersEquityAndShareBasedPaymentsTextBlock

### http://www.amazon.com/role/StockholdersEquityTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfCompensationCostForShareBasedPaymentArrangementsAllocationOfShareBasedCompensationCostsByPlanTableTextBlock
  - us-gaap_ScheduleOfNonvestedRestrictedStockUnitsActivityTableTextBlock
  - us-gaap_ScheduleOfShareBasedCompensationArrangementByShareBasedPaymentAwardRestrictedStockUnitsVestedAndExpectedToVestTableTextBlock

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresCommonStockSplitDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_StockholdersEquityNoteStockSplitConversionRatio1
  - us-gaap_CommonStockParOrStatedValuePerShare

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresStockBasedCompensationDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_VestingAxis
      - us-gaap_VestingDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardAwardVestingRightsPercentage

### http://www.amazon.com/role/StockholdersEquityAdditionalInformationDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfStockByClassTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - srt_ShareRepurchaseProgramAxis
      - srt_ShareRepurchaseProgramDomain
    - us-gaap_ClassOfStockLineItems
      - us-gaap_PreferredStockSharesAuthorized
      - us-gaap_PreferredStockParOrStatedValuePerShare
      - us-gaap_PreferredStockSharesOutstanding
      - amzn_CommonStockSharesOutstandingIncludingNonvestedStockAwards
      - srt_StockRepurchaseProgramAuthorizedAmount1
      - us-gaap_StockRepurchasedDuringPeriodShares
      - us-gaap_StockRepurchasedDuringPeriodValue
      - us-gaap_StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - amzn_EmployeeServiceShareBasedCompensationNonvestedAwardsCompensationCostExpensedInNextTwelveMonthsExpectedToExceedPercentage
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
      - amzn_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsForfeitureRate
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
      - us-gaap_CommonStockCapitalSharesReservedForFutureIssuance

### http://www.amazon.com/role/StockholdersEquityStockbasedCompensationExpenseDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
      - us-gaap_AllocatedShareBasedCompensationExpense
      - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense

### http://www.amazon.com/role/StockholdersEquityRestrictedStockUnitActivityDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward

### http://www.amazon.com/role/StockholdersEquityScheduledVestingforOutstandingRestrictedStockUnitsDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsAdditionalDisclosuresAbstract

### http://xbrl.sec.gov/ecd/role/AwardTimingDisclosure

- us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
  - us-gaap_EmployeeStockOptionMember
  - us-gaap_StockAppreciationRightsSARSMember

## 其他结构 (Other Structure)

### http://www.amazon.com/role/CoverPage

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
  - dei_AmendmentFlag
  - dei_DocumentFiscalYearFocus
  - dei_DocumentFiscalPeriodFocus
  - dei_EntityCentralIndexKey

### http://www.amazon.com/role/AuditInformation

- amzn_AuditInformationAbstract
  - dei_AuditorName
  - dei_AuditorFirmId
  - dei_AuditorLocation

### http://www.amazon.com/role/ConsolidatedStatementsofOperations

- us-gaap_StatementTable
  - srt_ProductOrServiceAxis
    - srt_ProductsAndServicesDomain
      - us-gaap_ProductMember
      - us-gaap_ServiceMember
  - us-gaap_StatementLineItems
    - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
    - us-gaap_CostsAndExpensesAbstract
    - us-gaap_OperatingIncomeLoss [totalLabel]
    - us-gaap_InvestmentIncomeInterest
    - us-gaap_InterestExpenseNonoperating
    - us-gaap_OtherNonoperatingIncomeExpense
    - us-gaap_NonoperatingIncomeExpense [totalLabel]
    - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments [totalLabel]
    - us-gaap_IncomeTaxExpenseBenefit
    - us-gaap_IncomeLossFromEquityMethodInvestments
    - us-gaap_NetIncomeLoss [totalLabel]
    - us-gaap_EarningsPerShareBasic
    - us-gaap_EarningsPerShareDiluted
    - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosures

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_OrganizationConsolidationBasisOfPresentationBusinessDescriptionAndAccountingPoliciesTextBlock

### http://www.amazon.com/role/PropertyandEquipment

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.amazon.com/role/Leases

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeasesTextBlock
  - us-gaap_LesseeFinanceLeasesTextBlock

### http://www.amazon.com/role/Debt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.amazon.com/role/CommitmentsandContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.amazon.com/role/SegmentInformation

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_SegmentReportingPolicyPolicyTextBlock
  - us-gaap_ConsolidationPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_EarningsPerSharePolicyTextBlock
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - amzn_FulfillmentExpensesPolicyPolicyTextBlock
  - amzn_TechnologyAndContentExpensesPolicyPolicyTextBlock
  - us-gaap_AdvertisingCostsPolicyTextBlock
  - us-gaap_SellingGeneralAndAdministrativeExpensesPolicyTextBlock
  - us-gaap_CompensationRelatedCostsPolicyTextBlock
  - amzn_OtherOperatingIncomeAndExpensePolicyPolicyTextBlock
  - amzn_OtherIncomeExpenseNetPolicyPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_FairValueOfFinancialInstrumentsPolicy
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_ReceivablesPolicyTextBlock
  - us-gaap_InternalUseSoftwarePolicy
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_LesseeLeasesPolicyTextBlock
  - amzn_FinancingObligationsPolicyTextBlock
  - us-gaap_GoodwillAndIntangibleAssetsPolicyTextBlock
  - amzn_OtherAssetsNoncurrentPolicyPolicyTextBlock
  - amzn_VideoAndMusicContentPolicyPolicyTextBlock
  - us-gaap_InvestmentPolicyTextBlock
  - us-gaap_ImpairmentOrDisposalOfLongLivedAssetsPolicyTextBlock
  - amzn_AccruedExpensesAndOtherPolicyPolicyTextBlock
  - us-gaap_SelfInsuranceReservePolicyTextBlock
  - amzn_RevenuefromContractwithCustomerContractLiabilityPolicyTextBlock
  - amzn_OtherLongTermLiabilitiesPolicyTextBlock
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfCashFlowSupplementalDisclosuresTableTextBlock
  - us-gaap_ScheduleOfWeightedAverageNumberOfSharesTableTextBlock
  - us-gaap_ScheduleOfOtherNonoperatingIncomeExpenseTableTextBlock

### http://www.amazon.com/role/PropertyandEquipmentTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.amazon.com/role/LeasesTables

- us-gaap_LeasesAbstract
  - us-gaap_LeaseCostTableTextBlock
  - amzn_OtherOperatingandFinanceLeaseInformationTableTextBlock
  - amzn_OperatingandFinanceLeaseLiabilityReconciliationTableTextBlock

### http://www.amazon.com/role/DebtTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtInstrumentsTextBlock
  - us-gaap_ScheduleOfMaturitiesOfLongTermDebtTableTextBlock

### http://www.amazon.com/role/CommitmentsandContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - srt_ContractualObligationFiscalYearMaturityScheduleTableTextBlock

### http://www.amazon.com/role/SegmentInformationTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
  - us-gaap_DisaggregationOfRevenueTableTextBlock
  - us-gaap_RevenueFromExternalCustomersByGeographicAreasTableTextBlock
  - us-gaap_ReconciliationOfAssetsFromSegmentToConsolidatedTextBlock
  - us-gaap_LongLivedAssetsByGeographicAreasTableTextBlock
  - us-gaap_ReconciliationOfOtherSignificantReconcilingItemsFromSegmentsToConsolidatedTextBlock

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresDescriptionofBusinessDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NumberOfOperatingSegments

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresUseofEstimatesDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_ChangeInAccountingEstimateByTypeAxis
      - us-gaap_ChangeInAccountingEstimateTypeDomain
    - srt_StatementScenarioAxis
      - srt_ScenarioUnspecifiedDomain
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_NetIncomeLoss
      - us-gaap_DepreciationDepletionAndAmortization
      - us-gaap_EarningsPerShareBasic
      - us-gaap_EarningsPerShareDiluted
      - us-gaap_AssetImpairmentCharges
      - us-gaap_GainLossOnContractTermination
      - us-gaap_SeveranceCosts1

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresCalculationofDilutedSharesDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_IncrementalCommonSharesAttributableToShareBasedPaymentArrangements
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding [totalLabel]

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresMarketingDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_AdvertisingExpense

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresInventoriesDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_InventoryValuationReserves

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresAccountsReceivableNetandOtherDetails

- us-gaap_AccountsNotesAndLoansReceivableLineItems
  - us-gaap_AccountsReceivableNetCurrent
  - us-gaap_PrepaidExpenseAndOtherAssetsCurrent
  - us-gaap_AllowanceForDoubtfulAccountsReceivableCurrent
  - us-gaap_ProvisionForDoubtfulAccounts
  - us-gaap_AllowanceForDoubtfulAccountsReceivableWriteOffs
- us-gaap_ReceivableTypeDomain
  - us-gaap_TradeAccountsReceivableMember
  - amzn_VendorAccountsReceivableMember
  - amzn_OtherReceivablesMember
- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfAccountsNotesLoansAndFinancingReceivableTable

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresPropertyandEquipmentNetDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresLeasesDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_LesseeLeaseDescriptionLineItems
      - amzn_LesseeOperatingandFinanceLeaseTermofContract

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresDigitalVideoandMusicContentDetails

- us-gaap_AccountingPoliciesAbstract
  - amzn_WeightedAverageLifeCapitalizedVideoContent
  - amzn_VideoandMusicContentCapitalizedCosts
  - amzn_VideoandMusicContentExpense

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresAccruedExpensesandOtherDetails

- srt_ProductOrServiceAxis
  - srt_ProductsAndServicesDomain
    - amzn_GiftCardMember
- us-gaap_AccountingPoliciesAbstract
  - us-gaap_DisaggregationOfRevenueTable

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresSelfInsuranceLiabilitiesDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_IncreaseDecreaseInSelfInsuranceReserve
  - us-gaap_SelfInsuranceReserve

### http://www.amazon.com/role/DescriptionofBusinessAccountingPoliciesandSupplementalDisclosuresForeignCurrencyDetails

- us-gaap_AccountingPoliciesAbstract
  - amzn_ForeignCurrencyTransactionGainLossOnIntercompanyBalances

### http://www.amazon.com/role/FinancialInstrumentsFairValuesonRecurringBasisDetails

- us-gaap_ScheduleOfInvestmentsTable
  - us-gaap_FairValueByMeasurementFrequencyAxis
    - us-gaap_FairValueMeasurementFrequencyDomain
      - us-gaap_FairValueMeasurementsRecurringMember
  - us-gaap_FairValueByFairValueHierarchyLevelAxis
    - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
      - us-gaap_FairValueInputsLevel1Member
      - us-gaap_FairValueInputsLevel2Member
  - us-gaap_CashAndCashEquivalentsAxis
  - us-gaap_FinancialInstrumentAxis
    - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
      - us-gaap_MoneyMarketFundsMember
      - us-gaap_ForeignGovernmentDebtSecuritiesMember
      - us-gaap_USTreasuryAndGovernmentMember
      - us-gaap_CorporateDebtSecuritiesMember
      - us-gaap_AssetBackedSecuritiesMember
      - us-gaap_FixedIncomeSecuritiesMember
  - us-gaap_ScheduleOfInvestmentsLineItems
    - us-gaap_Cash
    - us-gaap_CashEquivalentsAtCarryingValue
    - amzn_CashCashEquivalentsAndDebtAvailableForSaleSecuritiesAmortizedCostBasisAbstract
    - amzn_GrossUnrealizedGainsAbstract
      - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
    - amzn_GrossUnrealizedLossesAbstract
      - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
    - us-gaap_CashCashEquivalentsAndShortTermInvestmentsAbstract

### http://www.amazon.com/role/FinancialInstrumentsContractualMaturitiesDetails

- us-gaap_AvailableForSaleSecuritiesDebtMaturitiesSingleMaturityDateAmortizedCostBasisAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearAmortizedCost
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsAmortizedCost
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterFiveThroughTenYearsAmortizedCost
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterTenYearsAmortizedCost
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesSingleMaturityDateAmortizedCostBasis [totalLabel]
- us-gaap_AvailableForSaleSecuritiesDebtMaturitiesFairValueAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterFiveThroughTenYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterTenYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesSingleMaturityDate [totalLabel]

### http://www.amazon.com/role/PropertyandEquipmentComponentsDetails

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetBeforeAccumulatedDepreciationAndAmortization
      - us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAccumulatedDepreciationAndAmortization
      - us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization [totalLabel]

### http://www.amazon.com/role/PropertyandEquipmentAdditionalInformationDetails

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_Depreciation
  - us-gaap_FinanceLeaseRightOfUseAssetAmortization

### http://www.amazon.com/role/LeasesAdditionalInformationDetails

- us-gaap_LeasesAbstract
  - us-gaap_FinanceLeaseRightOfUseAssetStatementOfFinancialPositionExtensibleList
  - us-gaap_FinanceLeaseRightOfUseAssetBeforeAccumulatedAmortization
  - us-gaap_FinanceLeaseRightOfUseAssetAccumulatedAmortization

### http://www.amazon.com/role/LeasesLeaseCostsDetails

- us-gaap_LeaseCostAbstract
  - us-gaap_OperatingLeaseCost
  - amzn_FinanceLeaseCostComponentsAbstract
    - us-gaap_FinanceLeaseRightOfUseAssetAmortization
    - us-gaap_FinanceLeaseInterestExpense
    - amzn_FinanceLeaseCost [totalLabel]
  - us-gaap_VariableLeaseCost
  - us-gaap_LeaseCost [totalLabel]

### http://www.amazon.com/role/LeasesOtherOperatingandFinanceLeaseInformationDetails

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeaseWeightedAverageRemainingLeaseTerm1
  - us-gaap_FinanceLeaseWeightedAverageRemainingLeaseTerm1
  - us-gaap_OperatingLeaseWeightedAverageDiscountRatePercent
  - us-gaap_FinanceLeaseWeightedAverageDiscountRatePercent

### http://www.amazon.com/role/LeasesOperatingandFinanceLeaseReconciliationDetails

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDue [totalLabel]
  - us-gaap_FinanceLeaseLiabilityPaymentsDue [totalLabel]
  - amzn_LeaseLiabilityPaymentsDue [totalLabel]
  - us-gaap_LesseeOperatingLeaseLiabilityUndiscountedExcessAmount
  - us-gaap_FinanceLeaseLiabilityUndiscountedExcessAmount
  - amzn_LeaseLiabilityUndiscountedExcessAmount
  - us-gaap_OperatingLeaseLiability [totalLabel]
  - us-gaap_FinanceLeaseLiability [totalLabel]
  - amzn_LeaseLiability [totalLabel]
  - us-gaap_OperatingLeaseLiabilityCurrent
  - us-gaap_FinanceLeaseLiabilityCurrent
  - amzn_LeaseLiabilityCurrent
  - us-gaap_OperatingLeaseLiabilityNoncurrent
  - us-gaap_FinanceLeaseLiabilityNoncurrent
  - amzn_LeaseLiabilityNoncurrent
  - us-gaap_OperatingLeaseLiabilityCurrentStatementOfFinancialPositionExtensibleList
  - us-gaap_FinanceLeaseLiabilityCurrentStatementOfFinancialPositionExtensibleList
  - us-gaap_OperatingLeaseLiabilityNoncurrentStatementOfFinancialPositionExtensibleList
  - us-gaap_FinanceLeaseLiabilityNoncurrentStatementOfFinancialPositionExtensibleList

### http://www.amazon.com/role/DebtAdditionalInformationDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - us-gaap_ShortTermDebtTypeAxis
      - us-gaap_ShortTermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LongTermDebt
      - us-gaap_LongTermDebtFairValue
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - us-gaap_LineOfCreditFacilityUnusedCapacityCommitmentFeePercentage
      - us-gaap_LineOfCredit
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentCollateralAmount
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentTerm
      - amzn_CommercialPaperMaximumBorrowingCapacity
      - us-gaap_CommercialPaper
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - amzn_LineOfCreditFacilityAdditionalTerm
      - us-gaap_ShortTermBorrowings
      - amzn_LineOfCreditFacilityNumberOfExtensions
      - us-gaap_LineOfCreditFacilityRemainingBorrowingCapacity

### http://www.amazon.com/role/DebtLongTermDebtObligationsDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - us-gaap_LongTermDebt
      - us-gaap_DebtInstrumentUnamortizedDiscountPremiumNet
      - us-gaap_LongTermDebtCurrent
      - us-gaap_DebtInstrumentCarryingAmount
      - amzn_DebtInstrumentWeightedAverageRemainingLivesTerm

### http://www.amazon.com/role/DebtFuturePrincipalPaymentforDebtDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_LongTermDebtByMaturityAbstract
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive
    - us-gaap_LongTermDebt [totalLabel]

### http://www.amazon.com/role/CommitmentsandContingenciesPrincipalContractualCommitmentsExcludingOpenOrdersDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_UnrecordedUnconditionalPurchaseObligationTable
    - us-gaap_UnrecordedUnconditionalPurchaseObligationByCategoryOfItemPurchasedAxis
      - us-gaap_UnconditionalPurchaseObligationCategoryOfGoodsOrServicesAcquiredDomain
    - us-gaap_UnrecordedUnconditionalPurchaseObligationLineItems
      - us-gaap_LongTermDebtByMaturityAbstract
      - us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract
      - us-gaap_CapitalLeaseObligationsAbstract
      - amzn_FinancingObligationsFutureMinimumPaymentsDueFiscalYearMaturityAbstract
      - us-gaap_UnrecordedUnconditionalPurchaseObligationAbstract
      - us-gaap_OtherCommitmentFiscalYearMaturityAbstract
      - us-gaap_ContractualObligationFiscalYearMaturityAbstract
      - amzn_FinancingObligationsCurrent
      - amzn_FinancingObligationsNoncurrent
      - amzn_FinancingObligationWeightedAverageRemainingTerm
      - amzn_FinancingObligationsWeightedAverageInterestRate
      - us-gaap_UnrecognizedTaxBenefits

### http://www.amazon.com/role/CommitmentsandContingenciesLegalProceedingsDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_LossContingenciesTable
    - srt_LitigationCaseAxis
      - srt_LitigationCaseTypeDomain
    - us-gaap_LitigationStatusAxis
      - us-gaap_LitigationStatusDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_LossContingenciesLineItems
      - us-gaap_LossContingencyEstimateOfPossibleLoss
      - us-gaap_LitigationSettlementAmountAwardedToOtherParty
      - us-gaap_LitigationSettlementInterest

### http://www.amazon.com/role/SegmentInformationAdditionalInformationDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_NumberOfOperatingSegments
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - us-gaap_NonUsMember
- us-gaap_SegmentReportingInformationLineItems
  - us-gaap_NoncurrentAssets

### http://www.amazon.com/role/SegmentInformationNetSalesAttributedtoCountriesRepresentingPortionofConsolidatedNetSalesDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - country_DE
    - country_GB
    - country_JP
    - us-gaap_NonUsMember

### http://www.amazon.com/role/SegmentInformationReconciliationofPropertyandEquipmentfromSegmentstoConsolidatedDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - srt_ConsolidationItemsAxis
      - srt_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingOtherSignificantReconcilingItemLineItems
      - us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization

### http://www.amazon.com/role/SegmentInformationReconciliationofPropertyandEquipmentAdditionsfromSegmentstoConsolidatedDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - srt_ConsolidationItemsAxis
      - srt_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_SegmentExpenditureAdditionToLongLivedAssets

### http://www.amazon.com/role/SegmentInformationDepreciationandAmortizationExpensebySegmentDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_Depreciation

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

