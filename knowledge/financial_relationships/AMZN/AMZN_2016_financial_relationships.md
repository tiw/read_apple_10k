# AMZN 2016 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.amazon.com/role/AccumulatedOtherComprehensiveLossChangesInCompositionOfAccumulatedOtherComprehensiveIncomeOrLossDetail

- us-gaap_EquityAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossTable
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_AccumulatedOtherComprehensiveIncomeLossLineItems
      - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward

### http://www.amazon.com/role/CashCashEquivalentsAndMarketableSecuritiesSummaryOfContractualMaturitiesOfCashEquivalentAndMarketableFixedIncomeSecuritiesDetail

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - amzn_InvestmentsClassifiedByContractualMaturityDateTable
    - amzn_PeriodAxis
      - amzn_PeriodDomain
    - amzn_InvestmentsClassifiedByContractualMaturityDateLineItems
      - amzn_CashEquivalentsandMarketableSecuritiesAmortizedCostBasis
      - amzn_CashEquivalentsandMarketableSecuritiesFairValueDisclosure

### http://www.amazon.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_DepreciationAndAmortization
  - us-gaap_ShareBasedCompensation
  - us-gaap_OtherOperatingIncomeExpenseNet
  - us-gaap_GainLossOnSaleOfInvestments
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_ExcessTaxBenefitFromShareBasedCompensationOperatingActivities
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.amazon.com/role/ConsolidatedStatementsOfComprehensiveIncome

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_NetIncomeLoss
      - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
      - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.amazon.com/role/ConsolidatedStatementsOfComprehensiveIncomeParenthetical

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentTax
  - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodTax
  - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesTax

### http://www.amazon.com/role/ConsolidatedStatementsOfOperations

- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
- us-gaap_CostsAndExpensesAbstract
  - us-gaap_CostOfGoodsAndServicesSold
  - amzn_FulfillmentExpense
  - us-gaap_MarketingExpense
  - amzn_TechnologyAndContentExpense
  - us-gaap_GeneralAndAdministrativeExpense
  - us-gaap_OtherCostAndExpenseOperating
  - us-gaap_CostsAndExpenses [totalLabel]

### http://www.amazon.com/role/ConsolidatedStatementsOfOperationsParenthetical

- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - amzn_FulfillmentExpenseMember
    - us-gaap_SellingAndMarketingExpenseMember
    - amzn_TechnologyAndContentExpenseMember
    - us-gaap_GeneralAndAdministrativeExpenseMember

### http://www.amazon.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.amazon.com/role/IncomeTaxesAdditionalInformationDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - amzn_IncomeTaxesTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - amzn_IncomeTaxesLineItems
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_IncomeTaxesPaidNet
      - us-gaap_UndistributedEarningsOfForeignSubsidiaries
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_OperatingLossCarryforwardsExpirationDate
      - us-gaap_TaxCreditCarryforwardAmount
      - us-gaap_TaxCreditCarryforwardExpirationDate
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestExpense
      - us-gaap_IncomeTaxExaminationDescription
      - us-gaap_IncomeTaxExaminationEstimateOfPossibleLoss
      - us-gaap_IncomeTaxExaminationYearUnderExamination

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
    - amzn_OperatingLossAndTaxCreditCarryforwardsAxis
      - amzn_OperatingLossAndTaxCreditCarryforwardsDomain
    - amzn_ScheduleOfDeferredIncomeTaxAssetsAndLiabilitiesLineItems
      - us-gaap_DeferredTaxAssetsNetAbstract
      - us-gaap_DeferredTaxLiabilitiesAbstract

### http://www.amazon.com/role/IncomeTaxesItemsAccountingForDifferencesBetweenIncomeTaxesComputedAtFederalStatutoryRateAndProvisionRecordedForIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
  - amzn_EffectiveIncomeTaxRateReconciliationOtherReconcilingItemsAbstract
    - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
    - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
    - us-gaap_IncomeTaxReconciliationTaxCredits
    - us-gaap_IncomeTaxReconciliationNondeductibleExpenseShareBasedCompensationCost
    - us-gaap_IncomeTaxReconciliationDeductionsQualifiedProductionActivities
    - us-gaap_IncomeTaxReconciliationOtherAdjustments
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.amazon.com/role/IncomeTaxesReconciliationOfTaxContingenciesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_UnrecognizedTaxBenefits
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
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

### http://www.amazon.com/role/SegmentInformationNetSalesAttributedToForeignCountriesDetails

- us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTable
  - us-gaap_StatementGeographicalAxis
  - us-gaap_SegmentReportingRevenueReconcilingItemLineItems
    - us-gaap_SalesRevenueNet

### http://www.amazon.com/role/SegmentInformationNetSalesOfSimilarProductsAndServicesDetail

- us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
  - us-gaap_ProductOrServiceAxis
  - us-gaap_EntityWideInformationRevenueFromExternalCustomerLineItems
    - us-gaap_SalesRevenueNet

### http://www.amazon.com/role/SegmentInformationReportableSegmentsAndReconciliationToConsolidatedNetIncomeDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_SalesRevenueNet
      - us-gaap_CostsAndExpenses
      - us-gaap_OperatingIncomeLoss
      - us-gaap_ShareBasedCompensation
      - us-gaap_OtherCostAndExpenseOperating
      - us-gaap_NonoperatingIncomeExpense
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_IncomeLossFromEquityMethodInvestments
      - us-gaap_NetIncomeLoss [totalLabel]

## 资产负债表结构 (Balance Sheet Structure)

### http://www.amazon.com/role/AccumulatedOtherComprehensiveLoss

- us-gaap_EquityAbstract
  - us-gaap_ComprehensiveIncomeNoteTextBlock

### http://www.amazon.com/role/AccumulatedOtherComprehensiveLossTables

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfAccumulatedOtherComprehensiveIncomeLossTableTextBlock

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssets

- amzn_AcquisitionsGoodwillandAcquiredIntangibleAssetsAbstract
  - amzn_AcquisitionsGoodwillAndIntangibleAssetsDisclosureTextBlock

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsAcquiredIntangibleAssetsDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetByMajorClassTable
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_AcquiredFiniteLivedIntangibleAssetsLineItems
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsAdditionalInformationDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationConsiderationTransferred1
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedStockOptions [totalLabel]
      - amzn_Fairvalueofassumedstockoptionsandrestrictedstockoptions
      - us-gaap_BusinessAcquisitionEffectiveDateOfAcquisition1
      - us-gaap_BusinessCombinationProFormaInformationRevenueOfAcquireeSinceAcquisitionDateActual
      - us-gaap_BusinessCombinationProFormaInformationEarningsOrLossOfAcquireeSinceAcquisitionDateActual
      - us-gaap_Goodwill
      - us-gaap_AmortizationOfIntangibleAssets

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsAllocationOfAggregatePurchasePriceOfAcquisitionsDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
      - us-gaap_BusinessCombinationConsiderationTransferredLiabilitiesIncurred
      - us-gaap_BusinessCombinationConsiderationTransferredOther1
      - us-gaap_BusinessCombinationConsiderationTransferred1 [totalLabel]
      - amzn_PurchasePriceAllocationAbstract
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsBusinessAcquisitionsProFormaFinancialInformationDetails

- amzn_ProFormaFinancialInformationAbstract
  - us-gaap_BusinessAcquisitionsProFormaRevenue
  - us-gaap_BusinessAcquisitionsProFormaNetIncomeLoss

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsExpectedFutureAmortizationExpenseOfAcquiredIntangibleAssetsDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsSummaryOfGoodwillActivityBySegmentDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfGoodwillTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_GoodwillLineItems
      - us-gaap_Goodwill
      - us-gaap_GoodwillAcquiredDuringPeriod
      - us-gaap_GoodwillOtherChanges
      - amzn_SegmentReallocation
      - us-gaap_Goodwill

### http://www.amazon.com/role/AcquisitionsGoodwillAndAcquiredIntangibleAssetsTables

- amzn_AcquisitionsGoodwillandAcquiredIntangibleAssetsAbstract
  - us-gaap_ScheduleOfRecognizedIdentifiedAssetsAcquiredAndLiabilitiesAssumedTableTextBlock
  - us-gaap_BusinessAcquisitionProFormaInformationTextBlock
  - us-gaap_ScheduleOfGoodwillTextBlock
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetsByMajorClassTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.amazon.com/role/CashCashEquivalentsAndMarketableSecurities

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_CashCashEquivalentsAndShortTermInvestmentsTextBlock

### http://www.amazon.com/role/CashCashEquivalentsAndMarketableSecuritiesGrossGrainsAndGrossLossesRealizedOnSalesOfAvailableForSaleMarketableSecuritiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_AvailableForSaleSecuritiesGrossRealizedGains
  - us-gaap_AvailableForSaleSecuritiesGrossRealizedLosses

### http://www.amazon.com/role/CashCashEquivalentsAndMarketableSecuritiesSummaryByMajorSecurityTypeCashCashEquivalentsAndMarketableSecuritiesMeasuredAtFairValueOnRecurringBasisAndCategorizedUsingFairValueHierarchyDetail

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - amzn_CashCashEquivalentsAndMarketableSecuritiesTable
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
    - us-gaap_InvestmentTypeAxis
    - amzn_CashCashEquivalentsAndMarketableSecuritiesLineItems
      - amzn_CashCashEquivalentsAndMarketableSecuritiesAmortizedCost
      - amzn_CashCashEquivalentsAndMarketableSecuritiesUnrealizedGains
      - amzn_CashCashEquivalentsAndMarketableSecuritiesUnrealizedLosses
      - us-gaap_SecurityOwnedAndPledgedAsCollateralFairValue
      - us-gaap_CashCashEquivalentsAndShortTermInvestments [totalLabel]

### http://www.amazon.com/role/CashCashEquivalentsAndMarketableSecuritiesTables

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_FairValueAssetsMeasuredOnRecurringBasisTextBlock
  - us-gaap_RealizedGainLossOnInvestmentsTableTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock

### http://www.amazon.com/role/ConsolidatedBalanceSheets

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAndStockholdersEquityAbstract

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

- us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
  - us-gaap_ExcessTaxBenefitFromShareBasedCompensationFinancingActivities
  - us-gaap_ProceedsFromRepaymentsOfLongTermDebtAndCapitalSecurities
  - us-gaap_RepaymentsOfDebt
  - us-gaap_RepaymentsOfLongTermCapitalLeaseObligations
  - amzn_RepaymentsOfLongTermfFinancingLeaseObligations
  - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
- us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
  - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
  - us-gaap_PaymentsToAcquireBusinessesAndInterestInAffiliates
  - us-gaap_ProceedsFromSaleMaturityAndCollectionsOfInvestments
  - us-gaap_PaymentsToAcquireMarketableSecurities
  - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
- us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_StatementTable
- us-gaap_SupplementalCashFlowInformationAbstract
  - us-gaap_InterestPaid
  - amzn_CashPaidForInterestCapitalandFinanceLeases
  - us-gaap_IncomeTaxesPaidNet
  - us-gaap_NoncashOrPartNoncashAcquisitionFixedAssetsAcquired1

### http://www.amazon.com/role/ConsolidatedStatementsOfStockholdersEquity

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember
    - us-gaap_TreasuryStockMember
    - us-gaap_AdditionalPaidInCapitalMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
    - us-gaap_RetainedEarningsMember
- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesAdditionalInformationDetail

- amzn_OtherAssetsAxis
  - amzn_OtherAssetsDomain
    - amzn_DigitalVideoandMusicContentMember

### http://www.amazon.com/role/SegmentInformationReconciliationOfAssetsFromSegmentToConsolidatedDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfAssetsFromSegmentToConsolidatedTable
    - us-gaap_LeaseArrangementTypeAxis
      - us-gaap_LeaseArrangementTypeDomain
    - us-gaap_StatementGeographicalAxis
      - us-gaap_SegmentGeographicalDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingAssetReconcilingItemLineItems
      - us-gaap_Assets

### http://www.amazon.com/role/StockholdersEquity

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.amazon.com/role/StockholdersEquityAdditionalInformationDetail

- us-gaap_EquityAbstract
  - amzn_StockholdersEquityNoteTable
    - us-gaap_RangeAxis
    - amzn_StockholdersEquityNoteLineItems
      - us-gaap_PreferredStockSharesAuthorized
      - us-gaap_PreferredStockParOrStatedValuePerShare
      - amzn_CommonStockSharesOutstandingIncludingStockAwards
      - us-gaap_StockRepurchaseProgramAuthorizedAmount1
      - us-gaap_StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
      - amzn_StockIssuedDuringPeriodSharesFourZeroOneKEmployerMatch
      - us-gaap_CommonStockCapitalSharesReservedForFutureIssuance

### http://www.amazon.com/role/StockholdersEquityRestrictedStockUnitActivityDetail

- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsAdditionalDisclosuresAbstract
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable

### http://www.amazon.com/role/StockholdersEquityScheduledVestingForOutstandingRestrictedStockUnitsDetail

- us-gaap_EquityAbstract
  - amzn_ScheduleOfVestingTable

### http://www.amazon.com/role/StockholdersEquityTables

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfNonvestedRestrictedStockUnitsActivityTableTextBlock
  - us-gaap_ScheduleOfNonvestedShareActivityTableTextBlock

## 现金流量表结构 (Cash Flow Structure)

### http://www.amazon.com/role/CashCashEquivalentsAndMarketableSecuritiesSummaryByMajorSecurityTypeCashCashEquivalentsAndMarketableSecuritiesMeasuredAtFairValueOnRecurringBasisAndCategorizedUsingFairValueHierarchyDetail

- us-gaap_InvestmentTypeAxis
  - us-gaap_InvestmentTypeCategorizationMember
    - us-gaap_CashMember
    - us-gaap_MoneyMarketFundsMember
    - us-gaap_EquitySecuritiesMember
    - us-gaap_ForeignGovernmentDebtSecuritiesMember
    - us-gaap_USTreasuryAndGovernmentMember
    - us-gaap_CorporateDebtSecuritiesMember
    - us-gaap_AssetBackedSecuritiesMember
    - us-gaap_FixedIncomeSecuritiesMember
    - amzn_CashCashEquivalentsAndShortTermInvestmentsMember
- us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueInputsLevel1Member
    - us-gaap_FairValueInputsLevel2Member

### http://www.amazon.com/role/CommitmentsAndContingenciesContractualCommitmentsExcludingOpenOrdersForPurchasesThatSupportNormalOperationsDetail

- us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueCurrent
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInTwoYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInThreeYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFourYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFiveYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueThereafter
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDue [totalLabel]

### http://www.amazon.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_StatementTable
  - us-gaap_MajorPropertyClassAxis
    - us-gaap_MajorPropertyClassDomain
      - us-gaap_AssetsHeldUnderCapitalLeasesMember
      - amzn_AssetsHeldUnderBuildToSuitLeasesMember
  - us-gaap_StatementLineItems
    - us-gaap_CashAndCashEquivalentsAtCarryingValue
    - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_EffectOfExchangeRateOnCashAndCashEquivalents
    - us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease [totalLabel]
    - us-gaap_CashAndCashEquivalentsAtCarryingValue
    - us-gaap_SupplementalCashFlowInformationAbstract
- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInInventories
  - us-gaap_IncreaseDecreaseInAccountsReceivableAndOtherOperatingAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities
  - us-gaap_IncreaseDecreaseInDeferredRevenue
  - us-gaap_RecognitionOfDeferredRevenue

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesAdditionalInformationDetail

- us-gaap_AccountsNotesLoansAndFinancingReceivableByReceivableTypeAxis
  - us-gaap_ReceivableTypeDomain

## 股东权益结构 (Equity Structure)

### http://www.amazon.com/role/ConsolidatedStatementsOfOperations

- us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding

### http://www.amazon.com/role/ConsolidatedStatementsOfStockholdersEquity

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_SharesOutstanding
    - us-gaap_StockholdersEquity
    - us-gaap_NetIncomeLoss
    - us-gaap_OtherComprehensiveIncomeLossNetOfTax
    - us-gaap_StockIssuedDuringPeriodSharesStockOptionsExercised
    - us-gaap_StockIssuedDuringPeriodValueStockOptionsExercised
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalTaxEffectFromShareBasedCompensation
    - us-gaap_StockIssuedDuringPeriodValueShareBasedCompensation
    - us-gaap_StockIssuedDuringPeriodValueAcquisitions
    - us-gaap_SharesOutstanding
    - us-gaap_StockholdersEquity

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesCalculationOfDilutedSharesAdditionalInformationDetails

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTable
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareByAntidilutiveSecuritiesAxis
      - us-gaap_AntidilutiveSecuritiesNameDomain
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareLineItems
      - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount

### http://www.amazon.com/role/QuarterlyResultsUnauditedUnauditedQuarterlyResultsDetail

- us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding

### http://www.amazon.com/role/StockholdersEquityAdditionalInformationDetail

- us-gaap_RangeAxis
  - us-gaap_RangeMember
    - us-gaap_MinimumMember
    - us-gaap_MaximumMember

### http://www.amazon.com/role/StockholdersEquityRestrictedStockUnitActivityDetail

- us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_AwardTypeAxis
    - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
      - us-gaap_RestrictedStockUnitsRSUMember
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsAdditionalDisclosuresAbstract

### http://www.amazon.com/role/StockholdersEquityScheduledVestingForOutstandingRestrictedStockUnitsDetail

- amzn_ScheduleOfVestingTable
  - us-gaap_AwardTypeAxis
    - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
      - us-gaap_RestrictedStockUnitsRSUMember
  - amzn_ScheduleOfVestingLineItems
    - amzn_ScheduledVestingYearOne
    - amzn_ScheduledVestingYearTwo
    - amzn_ScheduledVestingYearThree
    - amzn_ScheduledVestingYearFour
    - amzn_ScheduledVestingYearFive
    - amzn_ScheduledVestingThereafter
    - amzn_ScheduledVestingDisclosure [totalLabel]

## 其他结构 (Other Structure)

### http://www.amazon.com/role/CommitmentsAndContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.amazon.com/role/CommitmentsAndContingenciesAdditionalInformationDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_LossContingenciesTable
    - us-gaap_LitigationCaseAxis
      - us-gaap_LitigationCaseTypeDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - amzn_LossContingenciesByNameOfPlaintiffAxis
      - amzn_LossContingenciesByNameOfPlaintiffDomain
    - us-gaap_ProductOrServiceAxis
      - us-gaap_ProductsAndServicesDomain
    - us-gaap_LossContingenciesLineItems
      - us-gaap_LeaseAndRentalExpense
      - amzn_SecuritiesandFixedAssetsOwnedandPledgedasCollateralFairValue
      - us-gaap_LossContingencyPatentsAllegedlyInfringedNumber

### http://www.amazon.com/role/CommitmentsAndContingenciesContractualCommitmentsExcludingOpenOrdersForPurchasesThatSupportNormalOperationsDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_LongTermPurchaseCommitmentTable
    - us-gaap_LossContingenciesByNatureOfContingencyAxis
      - us-gaap_LossContingencyNatureDomain
    - us-gaap_LongTermPurchaseCommitmentLineItems
      - us-gaap_ContractualObligationDueInNextTwelveMonths
      - us-gaap_ContractualObligationDueInSecondYear
      - us-gaap_ContractualObligationDueInThirdYear
      - us-gaap_ContractualObligationDueInFourthYear
      - us-gaap_ContractualObligationDueInFifthYear
      - us-gaap_ContractualObligationDueAfterFifthYear
      - us-gaap_CommitmentsFairValueDisclosure [totalLabel]
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueAbstract
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueCurrent
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInTwoYears
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInThreeYears
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInFourYears
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInFiveYears
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueThereafter
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDue [totalLabel]
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract
  - us-gaap_RecordedUnconditionalPurchaseObligationPaymentScheduleAbstract
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
    - us-gaap_UnrecognizedTaxBenefits

### http://www.amazon.com/role/CommitmentsAndContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_ContractualObligationFiscalYearMaturityScheduleTableTextBlock

### http://www.amazon.com/role/ConsolidatedStatementsOfOperations

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_SalesRevenueGoodsNet
    - us-gaap_SalesRevenueServicesNet
    - us-gaap_SalesRevenueNet [totalLabel]
    - us-gaap_CostsAndExpensesAbstract
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

### http://www.amazon.com/role/ConsolidatedStatementsOfOperationsParenthetical

- us-gaap_StatementTable
  - us-gaap_IncomeStatementLocationAxis
  - us-gaap_StatementLineItems
    - us-gaap_AllocatedShareBasedCompensationExpense

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BusinessDescriptionAndAccountingPoliciesTextBlock

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesAdditionalInformationDetail

- us-gaap_ReceivableTypeDomain
  - amzn_VendorReceivableMember
  - amzn_CustomerandSellerReceivablesMember
- us-gaap_AccountingPoliciesAbstract
  - amzn_SignificantAccountingPoliciesTable
    - amzn_OtherAssetsAxis
    - us-gaap_MajorPropertyClassAxis
      - us-gaap_MajorPropertyClassDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_AccountsNotesLoansAndFinancingReceivableByReceivableTypeAxis
    - amzn_SignificantAccountingPoliciesLineItems
      - us-gaap_NumberOfOperatingSegments
      - us-gaap_RevenueRecognitionSalesReturnsReserveForSalesReturns
      - us-gaap_SalesReturnsAndAllowancesGoods
      - amzn_SalesReturnsandAllowancesDeductions
      - us-gaap_MarketingAndAdvertisingExpense
      - us-gaap_ForeignCurrencyTransactionGainLossRealized
      - us-gaap_MarketableSecuritiesRealizedGainLoss
      - us-gaap_UndistributedEarningsOfForeignSubsidiaries
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_AllowanceForDoubtfulAccountsReceivable
      - us-gaap_ProvisionForDoubtfulAccounts
      - us-gaap_AllowanceForDoubtfulAccountsReceivableWriteOffs
      - us-gaap_CapitalizedComputerSoftwareAdditions
      - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsCapitalizedAmount
      - us-gaap_CapitalizedComputerSoftwareAmortization
      - us-gaap_PropertyPlantAndEquipmentEstimatedUsefulLives
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_DisclosureOfChangeOfDateForAnnualGoodwillImpairmentTest
      - us-gaap_ReasonForChangeInDateOfAnnualGoodwillImpairmentTest
      - amzn_LicenseAgreementTerm
      - amzn_OtherAssetAmortizationPeriod
      - us-gaap_AccruedLiabilitiesForUnredeeemedGiftCards
      - amzn_UnredeemedGiftCardsPeriodOfRecognition
      - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
      - us-gaap_DeferredTaxAssetsGrossCurrent
      - us-gaap_DeferredTaxLiabilitiesCurrent

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesCalculationOfDilutedSharesDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_IncrementalCommonSharesAttributableToShareBasedPaymentArrangements
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding [totalLabel]

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NatureOfOperations
  - us-gaap_ComparabilityOfPriorYearFinancialData
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
  - us-gaap_ShareBasedCompensationOptionAndIncentivePlansPolicy
  - us-gaap_OtherOperatingIncomeAndExpenseTextBlock
  - us-gaap_OtherNonoperatingIncomeAndExpenseTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_FairValueOfFinancialInstrumentsPolicy
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_ReceivablesPolicyTextBlock
  - us-gaap_InternalUseSoftwarePolicy
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_LeasePolicyTextBlock
  - us-gaap_GoodwillAndIntangibleAssetsGoodwillPolicy
  - amzn_OtherAssetsPolicyPolicyTextBlock
  - us-gaap_FilmCostsPolicyPolicyTextBlock
  - us-gaap_InvestmentPolicyTextBlock
  - us-gaap_ImpairmentOrDisposalOfLongLivedAssetsPolicyTextBlock
  - amzn_AccruedLiabilitiesPolicyPolicyTextBlock
  - us-gaap_RevenueRecognitionDeferredRevenue
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock

### http://www.amazon.com/role/DescriptionOfBusinessAndAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfWeightedAverageNumberOfSharesTableTextBlock

### http://www.amazon.com/role/DocumentAndEntityInformation

- amzn_DocumentDocumentAndEntityInformationAbstract
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
  - dei_EntityPublicFloat
  - dei_EntityCommonStockSharesOutstanding

### http://www.amazon.com/role/LongTermDebt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_LongTermDebtTextBlock

### http://www.amazon.com/role/LongTermDebtAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentUnamortizedDiscount
      - us-gaap_OtherLongTermDebt
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - us-gaap_DebtInstrumentFrequencyOfPeriodicPayment
      - us-gaap_LongTermDebtFairValue
      - us-gaap_LongtermDebtWeightedAverageInterestRate
      - us-gaap_LineOfCreditFacilityInitiationDate1
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_DebtInstrumentTerm
      - us-gaap_LineOfCreditFacilityDescription
      - us-gaap_DebtInstrumentDescriptionOfVariableRateBasis
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - us-gaap_LineOfCreditFacilityFairValueOfAmountOutstanding

### http://www.amazon.com/role/LongTermDebtFuturePrincipalPaymentForDebtDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive
  - us-gaap_LongTermDebt [totalLabel]

### http://www.amazon.com/role/LongTermDebtLongTermDebtObligationsDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_OtherLongTermDebt
      - us-gaap_LongTermDebt [totalLabel]
      - us-gaap_LongTermDebtCurrent
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage

### http://www.amazon.com/role/LongTermDebtTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtInstrumentsTextBlock
  - amzn_FuturePrincipalPaymentsTextBlock

### http://www.amazon.com/role/OtherLongTermLiabilities

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - us-gaap_OtherLiabilitiesDisclosureTextBlock

### http://www.amazon.com/role/OtherLongTermLiabilitiesLongTermCapitalLeaseObligationDetail

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - us-gaap_CapitalLeaseObligations
  - us-gaap_CapitalLeasesFutureMinimumPaymentsInterestIncludedInPayments
  - us-gaap_CapitalLeasesFutureMinimumPaymentsPresentValueOfNetMinimumPayments [totalLabel]
  - us-gaap_CapitalLeaseObligationsCurrent
  - us-gaap_CapitalLeaseObligationsNoncurrent

### http://www.amazon.com/role/OtherLongTermLiabilitiesLongTermFinanceLeaseObligationDetail

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - amzn_FinanceLeaseObligations
  - amzn_FinanceLeasesFutureMinimumPaymentsInterestIncludedinPayments
  - amzn_FinanceLeasesFutureMinimumPaymentsPresentValueofNetMinimumPayments [totalLabel]
  - amzn_FinanceLeaseObligationsCurrent
  - amzn_FinanceLeaseObligationsNoncurrent

### http://www.amazon.com/role/OtherLongTermLiabilitiesSummaryDetail

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - amzn_OtherLiabilitiesTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - amzn_OtherLiabilitiesLineItems
      - us-gaap_CapitalLeaseObligationsNoncurrent
      - amzn_FinanceLeaseObligationsNoncurrent
      - us-gaap_ConstructionLoanNoncurrent
      - us-gaap_IncomeTaxExaminationPenaltiesAndInterestAccrued
      - us-gaap_DeferredTaxLiabilitiesNoncurrent
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

### http://www.amazon.com/role/PropertyAndEquipmentAdditionalInformationDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_LeaseArrangementTypeAxis
      - us-gaap_LeaseArrangementTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_CapitalizedComputerSoftwareGross
      - us-gaap_DepreciationDepletionAndAmortization
      - us-gaap_AmortizationOfLeasedAsset
      - us-gaap_CapitalLeasedAssetsGross
      - us-gaap_CapitalLeasesLesseeBalanceSheetAssetsByMajorClassAccumulatedDeprecation
      - amzn_FinanceLeasedAssetsGross
      - amzn_FinanceLeasesLesseeBalanceSheetAssetsbyMajorClassAccumulatedDepreciation
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet

### http://www.amazon.com/role/PropertyAndEquipmentTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems

### http://www.amazon.com/role/QuarterlyResultsUnaudited

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_QuarterlyFinancialInformationTextBlock

### http://www.amazon.com/role/QuarterlyResultsUnauditedTables

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_ScheduleOfQuarterlyFinancialInformationTableTextBlock

### http://www.amazon.com/role/QuarterlyResultsUnauditedUnauditedQuarterlyResultsDetail

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_SalesRevenueNet
  - us-gaap_OperatingIncomeLoss
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments
  - us-gaap_IncomeTaxExpenseBenefit
  - us-gaap_NetIncomeLoss
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted
  - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract

### http://www.amazon.com/role/SegmentInformation

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.amazon.com/role/SegmentInformationAdditionalInformationDetail

- us-gaap_SegmentReportingAbstract
  - amzn_SegmentReportingDisclosureTable
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - us-gaap_StatementGeographicalAxis
      - us-gaap_SegmentGeographicalDomain
    - us-gaap_ConcentrationRiskByTypeAxis
      - us-gaap_ConcentrationRiskTypeDomain
    - amzn_RegionReportingInformationByRegionAxis
      - amzn_ReportingRegionDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - amzn_SegmentReportingDisclosureLineItems
      - us-gaap_PropertyPlantAndEquipmentNet
      - us-gaap_NumberOfOperatingSegments
      - us-gaap_ConcentrationRiskPercentage1

### http://www.amazon.com/role/SegmentInformationDepreciationExpenseBySegmentDetails

- us-gaap_SegmentReportingAbstract
  - amzn_ReconciliationOfDepreciationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - amzn_ReconciliationOfDepreciationBySegmentLineItems
      - us-gaap_DepreciationDepletionAndAmortization

### http://www.amazon.com/role/SegmentInformationNetSalesAttributedToForeignCountriesDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTable
- us-gaap_StatementGeographicalAxis
  - us-gaap_SegmentGeographicalDomain
    - country_US
    - country_DE
    - country_JP
    - country_GB
    - amzn_RestofWorldDomain

### http://www.amazon.com/role/SegmentInformationNetSalesOfSimilarProductsAndServicesDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
- us-gaap_ProductOrServiceAxis
  - us-gaap_ProductsAndServicesDomain
    - amzn_MediaMember
    - amzn_ElectronicsAndOtherGeneralMerchandiseMember
    - amzn_AmazonWebServicesMember
    - amzn_OtherNonRetailMember

### http://www.amazon.com/role/SegmentInformationReconciliationOfPropertyAndEquipmentAdditionsFromSegmentsToConsolidatedDetails

- amzn_ReconciliationofPropertyandEquipmentAdditionsfromSegmentstoConsolidatedAbstract
  - amzn_ReconciliationofPropertyandEquipmentAdditionsfromSegmentstoConsolidatedTable
    - us-gaap_LeaseArrangementTypeAxis
      - us-gaap_LeaseArrangementTypeDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - amzn_ReconciliationofPropertyandEquipmentAdditionsfromSegmentstoConsolidatedLineItems
      - us-gaap_PropertyPlantAndEquipmentAdditions
      - us-gaap_CapitalLeasedAssetsGross
      - amzn_FinanceLeasedAssetsGross

### http://www.amazon.com/role/SegmentInformationReconciliationOfPropertyAndEquipmentFromSegmentsToConsolidatedDetails

- amzn_ReconciliationofPropertyandEquipmentfromSegmentstoConsolidatedAbstract
  - us-gaap_ReconciliationOfOtherSignificantReconcilingItemsFromSegmentsToConsolidatedTable
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SubsegmentsAxis
      - us-gaap_SubsegmentsDomain
    - us-gaap_SubsegmentsConsolidationItemsAxis
      - us-gaap_SubsegmentsConsolidationItemsDomain
    - us-gaap_SegmentReportingOtherSignificantReconcilingItemLineItems
      - us-gaap_PropertyPlantAndEquipmentNet

### http://www.amazon.com/role/SegmentInformationTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTextBlock
  - us-gaap_ScheduleOfRevenueFromExternalCustomersAttributedToForeignCountriesByGeographicAreaTextBlock
  - us-gaap_ReconciliationOfAssetsFromSegmentToConsolidatedTextBlock
  - us-gaap_ReconciliationOfOtherSignificantReconcilingItemsFromSegmentsToConsolidatedTextBlock
  - amzn_ReconciliationofPropertyandEquipmentAdditionsfromSegmentstoConsolidatedTableTextBlock
  - amzn_ScheduleOfDepreciationExpenseBySegmentTextBlock

