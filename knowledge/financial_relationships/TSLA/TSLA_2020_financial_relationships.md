# TSLA 2020 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.teslamotors.com/20191231/taxonomy/role/StatementConsolidatedStatementsOfOperations

- us-gaap_RevenuesAbstract
  - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
  - us-gaap_OperatingLeasesIncomeStatementLeaseRevenue
  - tsla_SalesRevenueAutomotive [totalLabel]
  - tsla_SalesRevenueServicesAndOtherNet
  - us-gaap_Revenues [totalLabel]
- us-gaap_OperatingExpensesAbstract
  - us-gaap_ResearchAndDevelopmentExpense
  - us-gaap_SellingGeneralAndAdministrativeExpense
  - tsla_RestructuringAndOtherExpenses
  - us-gaap_OperatingExpenses [totalLabel]
- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
- us-gaap_CostOfRevenueAbstract
  - us-gaap_CostOfGoodsAndServicesSold
  - tsla_CostOfAutomotiveLeasing
  - tsla_CostOfRevenuesAutomotive [totalLabel]
  - tsla_CostOfServicesAndOther
  - us-gaap_CostOfRevenue [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/StatementConsolidatedStatementsOfComprehensiveLoss

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_ProfitLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
    - us-gaap_OtherComprehensiveIncomeLossCashFlowHedgeGainLossAfterReclassificationAndTax
    - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
    - us-gaap_ComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterest [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTaxAttributableToNoncontrollingInterest
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/StatementConsolidatedStatementsOfCashFlows

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - tsla_DepreciationAmortizationAndImpairment
  - us-gaap_ShareBasedCompensation
  - us-gaap_AmortizationOfFinancingCostsAndDiscounts
  - us-gaap_InventoryWriteDown
  - us-gaap_GainLossOnSaleOfPropertyPlantEquipment
  - us-gaap_ForeignCurrencyTransactionGainLossRealized
  - tsla_GainsLossOnAcquisition
  - tsla_NoncashInterestIncomeExpenseAndOtherOperatingActivities
  - tsla_OperatingCashFlowRelatedToRepaymentOfDiscountedConvertibleNotes
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureIncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureIncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_SummaryOfPositionsForWhichSignificantChangeInUnrecognizedTaxBenefitsIsReasonablyPossibleTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfDeferredRevenueActivityDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ContractWithCustomerLiability
  - tsla_ContractWithCustomerLiabilityAdditions
  - tsla_ContractWithCustomerLiabilityIncreaseDecrease
  - us-gaap_ContractWithCustomerLiabilityRevenueRecognized
  - us-gaap_ContractWithCustomerLiability

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfDisaggregationOfRevenueByMajorSourceDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_DisaggregationOfRevenueTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_DisaggregationOfRevenueLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_OperatingLeasesIncomeStatementLeaseRevenue
      - us-gaap_Revenues

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfPotentiallyDilutiveSharesThatWereExcludedFromComputationOfDilutedNetIncomeLossPerShareOfCommonStockDetail

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTable
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareByAntidilutiveSecuritiesAxis
      - us-gaap_AntidilutiveSecuritiesNameDomain
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareLineItems
      - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureInventoryAdditionalInformationDetail

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfOperationalMilestoneBasedOnRevenueOrAdjustedEBITDADetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - srt_TitleOfIndividualAxis
      - srt_TitleOfIndividualWithRelationshipToEntityDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - tsla_OperationalMilestoneBasedOnRevenueOne
      - tsla_OperationalMilestoneBasedOnRevenueTwo
      - tsla_OperationalMilestoneBasedOnRevenueThree
      - tsla_OperationalMilestoneBasedOnRevenueFour
      - tsla_OperationalMilestoneBasedOnRevenueFive
      - tsla_OperationalMilestoneBasedOnRevenueSix
      - tsla_OperationalMilestoneBasedOnRevenueSeven
      - tsla_OperationalMilestoneBasedOnRevenueEight
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAOne
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDATwo
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAThree
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAFour
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAFive
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDASix
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDASeven
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAEight

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfStockBasedCompensationExpenseDetail

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember
    - tsla_SellingGeneralAndAdministrativeExpenseMember
    - tsla_RestructuringAndOtherMember

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureIncomeTaxesAdditionalInformationDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - tsla_IncomeTaxesTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_IncomeTaxAuthorityNameAxis
      - us-gaap_IncomeTaxAuthorityNameDomain
    - srt_RangeAxis
      - srt_RangeMember
    - tsla_IncomeTaxesLineItems
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_ValuationAllowanceDeferredTaxAssetChangeInAmount
      - us-gaap_DeferredTaxAssetsNet
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_OperatingLossCarryforwardsExpirationDate
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsResearch
      - tsla_ResearchTaxCreditCarryForwardExpirationDates
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsGeneralBusiness
      - tsla_TaxCreditCarryForwardExpirationYear
      - us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings
      - tsla_UnrecognizedTaxBenefitsOfDeferredTaxAccountingThatWouldNotImpactAnnualEffectiveRate
      - us-gaap_IncomeTaxExaminationYearUnderExamination

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureIncomeTaxesScheduleOfLossBeforeProvisionForIncomeTaxesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
  - tsla_IncomeLossFromContinuingOperationsBeforeIncomeTaxesAttributableToNoncontrollingInterestAndRedeemableNoncontrollingInterest
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureIncomeTaxesComponentsOfProvisionForIncomeTaxesDetail

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

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureIncomeTaxesScheduleOfDeferredTaxAssetsLiabilitiesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
    - us-gaap_DeferredTaxAssetsOperatingLossCarryforwards
    - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsResearch
    - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsOther
    - us-gaap_DeferredTaxAssetsDeferredIncome
    - us-gaap_DeferredTaxAssetsInventory
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
    - tsla_DeferredTaxAssetsOperatingLeaseRightOfUseLiabilities
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccrualsOther
    - us-gaap_DeferredTaxAssetsGross [totalLabel]
    - us-gaap_DeferredTaxAssetsValuationAllowance
    - us-gaap_DeferredTaxAssetsNet [totalLabel]
  - us-gaap_ComponentsOfDeferredTaxLiabilitiesAbstract
    - us-gaap_DeferredTaxLiabilitiesPropertyPlantAndEquipment
    - us-gaap_DeferredTaxLiabilitiesInvestments
    - tsla_DeferredTaxLiabilitiesOperatingLeaseRightOfUseAssets
    - us-gaap_DeferredTaxLiabilitiesOther
    - us-gaap_DeferredIncomeTaxLiabilities
    - us-gaap_DeferredTaxLiabilities

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureIncomeTaxesScheduleOfReconciliationOfTaxesAtFederalStatutoryRateToProvisionForIncomeTaxesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
  - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
  - us-gaap_IncomeTaxReconciliationNondeductibleExpense
  - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense
  - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
  - us-gaap_IncomeTaxReconciliationTaxCredits
  - us-gaap_IncomeTaxReconciliationMinorityInterestIncomeExpense
  - tsla_EffectiveIncomeTaxRateReconciliationChangeInUSTaxLaw
  - tsla_IncomeTaxReconciliationBargainInPurchaseGainLoss
  - tsla_EffectiveIncomeTaxRateReconciliationConvertibleDebt
  - tsla_EffectiveIncomeTaxRateReconciliationUnrecognizedTaxBenefits
  - us-gaap_IncomeTaxReconciliationChangeInDeferredTaxAssetsValuationAllowance
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureIncomeTaxesScheduleOfChangesToGrossUnrecognizedTaxBenefitsDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_UnrecognizedTaxBenefits
  - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
  - tsla_UnrecognizedTaxBenefitsChangeInBalanceRelatedToEffectOfUSTaxLawChange
  - us-gaap_UnrecognizedTaxBenefits

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfTotalRevenuesAndGrossProfitByReportableSegmentDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingRevenueReconcilingItemLineItems
      - us-gaap_Revenues
      - us-gaap_GrossProfit

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfRevenuesByGeographicAreaDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
      - us-gaap_Revenues

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfLongLivedAssetsByGeographicAreaDetail

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - srt_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

## 资产负债表结构 (Balance Sheet Structure)

### http://www.teslamotors.com/20191231/taxonomy/role/StatementConsolidatedBalanceSheets

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_StatementLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAbstract
      - us-gaap_CommitmentsAndContingencies
      - us-gaap_RedeemableNoncontrollingInterestEquityCarryingAmount
      - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterestAbstract
      - us-gaap_LiabilitiesAndStockholdersEquity [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/StatementConsolidatedBalanceSheetsParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_PreferredStockParOrStatedValuePerShare
  - us-gaap_PreferredStockSharesAuthorized
  - us-gaap_PreferredStockSharesIssued
  - us-gaap_PreferredStockSharesOutstanding
  - us-gaap_CommonStockParOrStatedValuePerShare
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_CommonStockSharesIssued
  - us-gaap_CommonStockSharesOutstanding

### http://www.teslamotors.com/20191231/taxonomy/role/StatementConsolidatedStatementsOfRedeemableNoncontrollingInterestAndStockholdersEquity

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - tsla_RedeemableNoncontrollingInterestsMember
    - us-gaap_CommonStockMember
    - us-gaap_AdditionalPaidInCapitalMember
    - us-gaap_RetainedEarningsMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
    - us-gaap_ParentMember
    - us-gaap_NoncontrollingInterestMember
- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable

### http://www.teslamotors.com/20191231/taxonomy/role/StatementConsolidatedStatementsOfRedeemableNoncontrollingInterestAndStockholdersEquityParenthetical

- us-gaap_StatementOfStockholdersEquityAbstract
  - tsla_CommonStockOfferingPricePerShare
  - tsla_CommonStockPublicOfferingIssuanceCosts

### http://www.teslamotors.com/20191231/taxonomy/role/StatementConsolidatedStatementsOfCashFlows

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_ProfitLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
    - tsla_PaymentsForSolarEnergySystems
    - us-gaap_PaymentsToAcquireIntangibleAssets
    - tsla_GovernmentGrantReceipt
    - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_ProceedsFromIssuanceOfCommonStock
    - tsla_ProceedsFromConvertibleAndOtherDebt
    - tsla_RepaymentsOfConvertibleAndOtherDebt
    - us-gaap_RepaymentsOfRelatedPartyDebt
    - us-gaap_ProceedsFromRepaymentsOfSecuredDebt
    - us-gaap_ProceedsFromIssuanceOfSharesUnderIncentiveAndShareBasedCompensationPlansIncludingStockOptions
    - us-gaap_FinanceLeasePrincipalPayments
    - us-gaap_PaymentsOfFinancingCosts
    - us-gaap_PaymentsForHedgeFinancingActivities
    - us-gaap_ProceedsFromHedgeFinancingActivities
    - us-gaap_ProceedsFromIssuanceOfWarrants
    - us-gaap_PaymentsForRepurchaseOfWarrants
    - us-gaap_ProceedsFromMinorityShareholders
    - us-gaap_PaymentsToMinorityShareholders
    - tsla_PaymentsForBuyOutsOfNoncontrollingInterestsInSubsidiaries
    - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
  - us-gaap_EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect [totalLabel]
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations
  - us-gaap_NoncashInvestingAndFinancingItemsAbstract
    - us-gaap_BusinessCombinationConsiderationTransferredEquityInterestsIssuedAndIssuable
    - us-gaap_NoncashOrPartNoncashAcquisitionValueOfAssetsAcquired1
    - tsla_NonCashEstimatedFairMarketValueOfManufacturingFacility
  - us-gaap_SupplementalCashFlowInformationAbstract
    - us-gaap_InterestPaidNet
    - us-gaap_IncomeTaxesPaid

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureGoodwillAndIntangibleAssets

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillAndIntangibleAssetsDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureGoodwillAndIntangibleAssetsTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetsByMajorClassTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_RegulatoryLiabilityAxis
  - us-gaap_RegulatoryLiabilityDomain
    - us-gaap_DeferredLeaseRevenueMember
- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_RetainedEarningsMember

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfCumulativeEffectOfChangesMadeToConsolidatedBalanceSheetForAdoptionOfNewLeaseStandardDetail

- us-gaap_AccountingPoliciesAbstract
  - tsla_SummaryOfSignificantAccountingPoliciesTable
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - srt_RestatementAxis
      - srt_RestatementDomain
    - tsla_SummaryOfSignificantAccountingPoliciesLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAbstract
      - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterestAbstract

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesEstimatedUsefulLivesOfRespectiveAssetsDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_LessorOperatingLeaseTermOfContract

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfEstimatedUsefulLivesOfRelatedAssetsDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureBusinessCombinationsAdditionalInformationDetail

- us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
  - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - tsla_PurchasedTechnologyMember

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureBusinessCombinationsScheduleOfFairValuesOfAssetsAcquiredAndLiabilitiesAssumedDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedAssetsAbstract
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedLiabilitiesAbstract
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedNet [totalLabel]
      - us-gaap_Goodwill
      - us-gaap_BusinessCombinationConsiderationTransferred1

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureBusinessCombinationsScheduleOfFairValueOfIdentifiedIntangibleAssetsAndTheirUsefulLivesDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_FiniteLivedIntangibleAssetsFairValueDisclosure
      - us-gaap_IntangibleAssetsGrossExcludingGoodwill
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureGoodwillAndIntangibleAssetsAdditionalInformationDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - tsla_ScheduleOfAcquiredIntangibleAssetsTable
    - us-gaap_IndefiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_IndefiniteLivedIntangibleAssetsMajorClassNameDomain
    - tsla_AcquiredIntangibleAssetsLineItems
      - us-gaap_GoodwillPeriodIncreaseDecrease
      - us-gaap_Goodwill
      - us-gaap_GoodwillImpairedAccumulatedImpairmentLoss
      - us-gaap_ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill
      - us-gaap_AmortizationOfIntangibleAssets

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureGoodwillAndIntangibleAssetsSummaryOfAcquiredIntangibleAssetsDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - tsla_ScheduleOfAcquiredIntangibleAssetsTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_IndefiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_IndefiniteLivedIntangibleAssetsMajorClassNameDomain
    - tsla_AcquiredIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - tsla_FiniteLivedIntangibleAssetsOther
      - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]
      - tsla_IndefiniteLivedIntangibleAssetsGrossExcludingGoodwill
      - tsla_IndefiniteLivedIntangibleAssetsOtherAdjustments
      - us-gaap_IndefiniteLivedIntangibleAssetsExcludingGoodwill [totalLabel]
      - us-gaap_IntangibleAssetsGrossExcludingGoodwill
      - tsla_IntangibleAssetsOther
      - us-gaap_IntangibleAssetsNetExcludingGoodwill [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureGoodwillAndIntangibleAssetsTotalFutureAmortizationExpenseForFiniteLivedIntangibleAssetsDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfAssetsAndLiabilitiesMeasuredAtFairValueOnRecurringBasisDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_InvestmentTypeAxis
      - us-gaap_InvestmentTypeCategorizationMember
    - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
      - us-gaap_AssetsFairValueDisclosure
      - us-gaap_LiabilitiesFairValueDisclosure
      - us-gaap_FairValueNetAssetLiability [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfInterestRateSwapsOutstandingDetail

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_DerivativeNotionalAmount
    - us-gaap_DerivativeLiabilityFairValueGrossAsset
    - us-gaap_DerivativeFairValueOfDerivativeLiability
    - us-gaap_DerivativeGainOnDerivative
    - us-gaap_DerivativeLossOnDerivative

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsAdditionalInformationDetail

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_LongtermDebtTypeAxis
  - us-gaap_DebtInstrumentAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_DebtInstrumentInterestRateStatedPercentage
    - us-gaap_DebtInstrumentMaturityDate

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfEstimatedFairValuesAndCarryingValuesDetail

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_DebtInstrumentAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_LongTermDebt
    - us-gaap_LongTermDebtFairValue

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfEstimatedFairValuesAndCarryingValuesParentheticalDetail

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_LongtermDebtTypeAxis
  - us-gaap_DebtInstrumentAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_DebtInstrumentInterestRateStatedPercentage
    - us-gaap_DebtInstrumentMaturityDate

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSolarEnergySystemsNetComponentsOfSolarEnergySystemsNetParentheticalDetail

- tsla_ScheduleOfFinanceLeasedAssetsTable
  - us-gaap_PropertyPlantAndEquipmentByTypeAxis
  - tsla_FinanceLeasedAssetsLineItems
    - us-gaap_DepreciationAndAmortization
    - tsla_FinanceLeaseRightOfUseAssetsGross
    - tsla_FinanceLeasedAssetsAccumulatedDepreciationAndAmortization

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtAutomotiveAssetBackedNotesAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_ProceedsFromIssuanceOfSecuredDebt

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtSolarAssetBackedNotesAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentCollateralAmount

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtPledgedAssetsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_PledgedAssetsSeparatelyReportedOnStatementOfFinancialPositionAtFairValue

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesAdditionalInformationDetail

- tsla_ScheduleOfOperatingAndFinanceLeasedAssetsTable
  - srt_RangeAxis
  - tsla_ScheduleOfOperatingAndFinanceLeasedAssetsLineItems
    - us-gaap_LesseeOperatingLeaseExistenceOfOptionToExtend
    - us-gaap_LesseeOperatingLeaseExistenceOfOptionToTerminate
    - us-gaap_LesseeFinanceLeaseExistenceOfOptionToExtend
    - us-gaap_LesseeFinanceLeaseExistenceOfOptionToTerminate
    - us-gaap_LesseeOperatingLeaseTermOfContract
    - us-gaap_LesseeFinanceLeaseTermOfContract1

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesScheduleOfOperatingAndFinancingLeasesPresentedInBalanceSheetsDetail

- us-gaap_LeasesAbstract
  - tsla_ScheduleOfOperatingAndFinanceLeasedAssetsTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - tsla_ScheduleOfOperatingAndFinanceLeasedAssetsLineItems
      - us-gaap_LesseeOperatingLeaseDescriptionAbstract
      - us-gaap_LesseeFinanceLeaseDescriptionAbstract

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesSupplementalCashFlowInformationRelatedToLeasesDetail

- tsla_CashPaidForAmountsIncludedInMeasurementOfLeaseLiabilitiesAbstract
  - us-gaap_OperatingLeasePayments
  - us-gaap_FinanceLeaseInterestPaymentOnLiability
  - us-gaap_FinanceLeasePrincipalPayments
  - us-gaap_RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability
  - us-gaap_RightOfUseAssetObtainedInExchangeForOperatingLeaseLiability

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureVariableInterestEntityArrangementsCarryingValuesOfAssetsAndLiabilitiesOfSubsidiaryInConsolidatedBalanceSheetsDetail

- tsla_VariableInterestEntityDisclosureAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTable
    - srt_ConsolidatedEntitiesAxis
      - srt_ConsolidatedEntitiesDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_VariableInterestEntityLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAbstract

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfLongLivedAssetsByGeographicAreaDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - tsla_InternationalMember

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureRestructuringAndOtherAdditionalInformationDetail

- us-gaap_IndefiniteLivedIntangibleAssetsByMajorClassAxis
  - us-gaap_IndefiniteLivedIntangibleAssetsMajorClassNameDomain
    - tsla_IndefiniteInProcessResearchAndDevelopmentMember

## 现金流量表结构 (Cash Flow Structure)

### http://www.teslamotors.com/20191231/taxonomy/role/StatementConsolidatedStatementsOfCashFlows

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInInventories
  - tsla_IncreaseDecreaseInOperatingLeaseVehicles
  - us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets
  - us-gaap_IncreaseDecreaseInOtherNoncurrentAssets
  - us-gaap_IncreaseDecreaseInAccountsPayableAndAccruedLiabilities
  - us-gaap_IncreaseDecreaseInContractWithCustomerLiability
  - tsla_IncreaseDecreaseInContractWithCustomerLiabilityCustomerDeposits
  - tsla_IncreaseDecreaseInResaleValueGuarantee
  - us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationTables

- tsla_LeasePassThroughFinancingObligationAbstract
  - tsla_ScheduleOfFutureMinimumLeasePaymentsToBeReceivedForOperatingLeasesTableTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfCashAndCashEquivalentsAndRestrictedCashDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_RestrictedCashCurrent
  - us-gaap_RestrictedCashNoncurrent
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtCashEquityDebtAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesScheduleOfComponentsOfLeaseExpenseDetail

- us-gaap_LesseeOperatingLeaseDescriptionAbstract
  - us-gaap_OperatingLeaseExpense

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesSupplementalCashFlowInformationRelatedToLeasesDetail

- us-gaap_LeasesAbstract
  - tsla_CashPaidForAmountsIncludedInMeasurementOfLeaseLiabilitiesAbstract

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesMaturitiesOfOperatingLeaseReceivablesFromCustomersDetail

- us-gaap_LessorOperatingLeasePaymentsToBeReceivedThereafter
  - us-gaap_LessorOperatingLeasePaymentsToBeReceived [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationAdditionalInformationDetail

- us-gaap_LeasesOperatingAbstract
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseByMajorPropertyClassTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
    - srt_RangeAxis
    - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseLineItems
      - tsla_NumberOfLeaseFinancingObligations
      - us-gaap_LessorOperatingLeaseTermOfContract
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseGross
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAccumulatedDepreciation
      - us-gaap_CapitalLeaseObligations
      - us-gaap_CapitalLeaseObligationsCurrent

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationScheduleOfFutureMinimumLeasePaymentsToBeReceivedForOperatingLeasesDetail

- us-gaap_LessorOperatingLeasePaymentsFiscalYearMaturityAbstract
  - us-gaap_LessorLeaseDescriptionTable

## 股东权益结构 (Equity Structure)

### http://www.teslamotors.com/20191231/taxonomy/role/StatementConsolidatedStatementsOfOperations

- us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding
- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.teslamotors.com/20191231/taxonomy/role/StatementConsolidatedStatementsOfRedeemableNoncontrollingInterestAndStockholdersEquity

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
    - us-gaap_TypeOfAdoptionMember
      - us-gaap_AccountingStandardsUpdate201409Member
      - us-gaap_AccountingStandardsUpdate201705Member
      - us-gaap_AccountingStandardsUpdate201609Member
      - us-gaap_AccountingStandardsUpdate201602Member
  - us-gaap_SubsidiarySaleOfStockAxis
    - us-gaap_SaleOfStockNameOfTransactionDomain
      - us-gaap_IPOMember
  - us-gaap_DebtInstrumentAxis
    - us-gaap_DebtInstrumentNameDomain
      - tsla_TwoPointThreeSevenFivePercentSeniorConvertibleNoteDueTwentyTwentyTwoMember
      - tsla_TwoPointZeroZeroPercentSeniorConvertibleNoteDueTwentyTwentyFourMember
  - us-gaap_StatementLineItems
    - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest
    - us-gaap_SharesIssued
    - us-gaap_NewAccountingPronouncementOrChangeInAccountingPrincipleEffectOfAdoptionQuantification
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalEquityComponentOfConvertibleDebt
    - tsla_AdjustmentsToAdditionalPaidInCapitalConvertibleDebtHedge
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalWarrantIssued
    - tsla_StockIssuedDuringPeriodValueAssumedAwards
    - tsla_StockIssuedDuringPeriodSharesAssumedAwards
    - us-gaap_StockIssuedDuringPeriodValueConversionOfConvertibleSecurities
    - us-gaap_StockIssuedDuringPeriodSharesConversionOfConvertibleSecurities
    - us-gaap_StockIssuedDuringPeriodValueAcquisitions
    - us-gaap_StockIssuedDuringPeriodSharesAcquisitions
    - us-gaap_StockIssuedDuringPeriodValueNewIssues
    - us-gaap_StockIssuedDuringPeriodSharesNewIssues
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
    - tsla_NoncontrollingInterestsIncreaseFromContributionsFromNoncontrollingInterests
    - us-gaap_MinorityInterestDecreaseFromDistributionsToNoncontrollingInterestHolders
    - us-gaap_StockholdersEquityOther
    - tsla_NetIncomeLossIncludingPortionAttributableToRedeemableNonControllingInterestAndNonControllingInterestInSubsidiaries
    - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent
    - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest
    - us-gaap_SharesIssued
    - tsla_StockIssuedDuringPeriodValueEquityIncentiveAwards
    - tsla_StockIssuedDuringPeriodSharesEquityIncentiveAwards

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureEquityIncentivePlans

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ShareholdersEquityAndShareBasedPaymentsTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureEquityIncentivePlansTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationActivityTableTextBlock
  - tsla_ScheduleOfShareBasedPaymentAwardStockOptionsAndEmployeeStockPurchasePlanValuationAssumptionsTableTextBlock
  - tsla_SummaryOfOperationalMilestoneBasedOnRevenueOrAdjustedEBITDATableTextBlock
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtZeroCouponConvertibleSeniorNotesDueIn2020AdditionalInformationDetail

- us-gaap_SubsidiarySaleOfStockAxis
  - us-gaap_SaleOfStockNameOfTransactionDomain
    - us-gaap_PrivatePlacementMember

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureEquityIncentivePlansAdditionalInformationDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_PlanNameAxis
      - us-gaap_PlanNameDomain
    - srt_TitleOfIndividualAxis
      - srt_TitleOfIndividualWithRelationshipToEntityDomain
    - us-gaap_VestingAxis
      - us-gaap_VestingDomain
    - us-gaap_FinancialInstrumentPerformanceStatusAxis
      - us-gaap_FinancialInstrumentPerformanceStatusDomain
    - us-gaap_SubsidiarySaleOfStockAxis
      - us-gaap_SaleOfStockNameOfTransactionDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_DeferredCompensationArrangementWithIndividualMaximumContractualTerm1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodGross
      - us-gaap_CommonStockCapitalSharesReservedForFutureIssuance
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue [totalLabel]
      - tsla_NumberOfTranches
      - tsla_IncreaseToMarketCapitalizationForEachRemainingMilestone
      - tsla_MarketCapitalization
      - tsla_NumberOfOperationalMilestonesFocusedOnRevenueTargets
      - tsla_NumberOfOperationalMilestonesFocusedOnAdjustedEBITDA
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingRights
      - tsla_NumberOfOperationalMilestonesFocusedOnRevenueTargetsAndAdjustedEBITDA
      - tsla_OperationalMilestoneBasedOnRevenue
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAOne
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDATwo
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardDividedEquallyInNumberOfTranches
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
      - us-gaap_ShareBasedCompensation
      - tsla_PortionOfStockOptionsScheduledToVestUponSuccessfulCompletionOfPerformanceObjectives
      - tsla_NumberOfVehicleProduction
      - tsla_GrossMargin
      - tsla_InitialMarketCapitalization
      - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromExerciseOfStockOptions
      - tsla_PercentageOfPayrollDeductionsOfEmployeesEligibleCompensation
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardDiscountFromMarketPriceOfferingDate
      - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockPurchasePlans
      - us-gaap_StockIssuedDuringPeriodValueEmployeeStockPurchasePlan
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForIssuance

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfStockOptionAndRSUActivityDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_PlanNameAxis
      - us-gaap_PlanNameDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodGross
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisedOrReleasedInPeriod
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsForfeituresInPeriod
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestOutstandingNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestExercisableNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsGrantsInPeriodWeightedAverageExercisePrice
      - tsla_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsExercisedOrReleasedInPeriodWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsForfeituresInPeriodWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestOutstandingWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestExercisableWeightedAverageExercisePrice
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsOutstandingWeightedAverageRemainingContractualTerm2
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsVestedAndExpectedToVestOutstandingWeightedAverageRemainingContractualTerm1
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsVestedAndExpectedToVestExercisableWeightedAverageRemainingContractualTerm1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingIntrinsicValue
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisedOrReleasedInPeriodAggregateIntrinsicValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingIntrinsicValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestOutstandingAggregateIntrinsicValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestExercisableAggregateIntrinsicValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExercisedOrReleasedInPeriod
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedAndExpectedToVest
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExercisableAndVested
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExercisedOrReleasedWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsToVestedAndExpectedToVestWeightedAverageGrantDateFairValue

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureEquityIncentivePlansScheduleOfFairValueOfStockOptionAwardAndESPPOnGrantDateDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsRiskFreeInterestRate
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardFairValueAssumptionsExpectedTerm1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsExpectedVolatilityRate
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsExpectedDividendRate
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfStockBasedCompensationExpenseDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
      - us-gaap_AllocatedShareBasedCompensationExpense

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureRelatedPartyTransactionsAdditionalInformationDetail

- us-gaap_SubsidiarySaleOfStockAxis
  - us-gaap_SaleOfStockNameOfTransactionDomain
    - us-gaap_PrivatePlacementMember

## 其他结构 (Other Structure)

### http://www.teslamotors.com/20191231/taxonomy/role/DocumentDocumentAndEntityInformation

- dei_CoverAbstract
  - dei_DocumentType
  - dei_AmendmentFlag
  - dei_DocumentPeriodEndDate
  - dei_DocumentFiscalYearFocus
  - dei_DocumentFiscalPeriodFocus
  - dei_TradingSymbol
  - dei_Security12bTitle
  - dei_SecurityExchangeName
  - dei_EntityRegistrantName
  - dei_EntityCentralIndexKey
  - dei_CurrentFiscalYearEndDate
  - dei_EntityWellKnownSeasonedIssuer
  - dei_EntityCurrentReportingStatus
  - dei_EntityInteractiveDataCurrent
  - dei_EntityVoluntaryFilers
  - dei_EntityFilerCategory
  - dei_EntitySmallBusiness
  - dei_EntityEmergingGrowthCompany
  - dei_EntityShellCompany
  - dei_EntityCommonStockSharesOutstanding
  - dei_EntityPublicFloat
  - dei_DocumentAnnualReport
  - dei_DocumentTransitionReport
  - dei_EntityFileNumber
  - dei_EntityIncorporationStateCountryCode
  - dei_EntityTaxIdentificationNumber
  - dei_EntityAddressAddressLine1
  - dei_EntityAddressCityOrTown
  - dei_EntityAddressStateOrProvince
  - dei_EntityAddressPostalZipCode
  - dei_CityAreaCode
  - dei_LocalPhoneNumber
  - dei_DocumentsIncorporatedByReferenceTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/StatementConsolidatedStatementsOfOperations

- us-gaap_StatementTable
  - srt_ProductOrServiceAxis
    - srt_ProductsAndServicesDomain
      - tsla_AutomotiveSegmentMember
      - tsla_EnergyGenerationAndStorageSegmentMember
  - us-gaap_StatementLineItems
    - us-gaap_RevenuesAbstract
    - us-gaap_CostOfRevenueAbstract
    - us-gaap_GrossProfit [totalLabel]
    - us-gaap_OperatingExpensesAbstract
    - us-gaap_OperatingIncomeLoss [totalLabel]
    - us-gaap_InvestmentIncomeInterest
    - us-gaap_InterestExpense
    - us-gaap_OtherNonoperatingIncomeExpense
    - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]
    - us-gaap_IncomeTaxExpenseBenefit
    - us-gaap_ProfitLoss [totalLabel]
    - us-gaap_NetIncomeLossAttributableToNoncontrollingInterest
    - us-gaap_NetIncomeLoss [totalLabel]
    - us-gaap_EarningsPerShareAbstract
    - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureOverview

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NatureOfOperations

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_SignificantAccountingPoliciesTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureBusinessCombinations

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_BusinessCombinationDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureFairValueOfFinancialInstruments

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueDisclosuresTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureInventory

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSolarEnergySystemsNet

- us-gaap_LeasesAbstract
  - tsla_SolarEnergySystemsNetDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosurePropertyPlantAndEquipmentNet

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureAccruedLiabilitiesAndOther

- us-gaap_PayablesAndAccrualsAbstract
  - us-gaap_AccountsPayableAndAccruedLiabilitiesDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureOtherLongTermLiabilities

- us-gaap_OtherLiabilitiesAbstract
  - us-gaap_OtherLiabilitiesDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureCustomerDeposits

- tsla_CustomerDepositsDisclosureAbstract
  - tsla_CustomerDepositsTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeases

- us-gaap_LeasesAbstract
  - tsla_LesseeOperatingAndFinanceLeasesDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureCommitmentsAndContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureVariableInterestEntityArrangements

- tsla_VariableInterestEntityDisclosureAbstract
  - us-gaap_VariableInterestEntityDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasePassThroughFinancingObligation

- us-gaap_LeasesAbstract
  - us-gaap_LeasesOfLessorDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDefinedContributionPlan

- us-gaap_CompensationAndRetirementDisclosureAbstract
  - us-gaap_CompensationAndEmployeeBenefitPlansTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureRelatedPartyTransactions

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_RelatedPartyTransactionsDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreas

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureRestructuringAndOther

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_RestructuringImpairmentAndOtherActivitiesDisclosureTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureQuarterlyResultsOfOperations

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_QuarterlyFinancialInformationTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ConsolidationPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - us-gaap_CostOfSalesPolicyTextBlock
  - us-gaap_LesseeLeasesPolicyTextBlock
  - us-gaap_ResearchAndDevelopmentExpensePolicy
  - us-gaap_AdvertisingCostsPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_ComprehensiveIncomePolicyPolicyTextBlock
  - us-gaap_ShareBasedCompensationOptionAndIncentivePlansPolicy
  - tsla_NoncontrollingInterestsPolicyTextBlock
  - us-gaap_EarningsPerSharePolicyTextBlock
  - us-gaap_BusinessCombinationsPolicy
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_CashAndCashEquivalentsRestrictedCashAndCashEquivalentsPolicy
  - us-gaap_ReceivablesPolicyTextBlock
  - us-gaap_TradeAndOtherAccountsReceivablePolicy
  - us-gaap_ConcentrationRiskCreditRisk
  - us-gaap_InventoryPolicyTextBlock
  - tsla_PropertySubjectToOrAvailableForOperatingLeasePolicyTextBlock
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_ImpairmentOrDisposalOfLongLivedAssetsIncludingIntangibleAssetsPolicyPolicyTextBlock
  - us-gaap_InternalUseSoftwarePolicy
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_StandardProductWarrantyPolicy
  - tsla_SolarRenewableEnergyCreditsPolicyTextBlock
  - tsla_DeferredInvestmentTaxCreditRevenuePolicyTextBlock
  - tsla_TaxIncentivePolicyTextBlock
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_StatementTable
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_StatementLineItems
      - us-gaap_ContractWithCustomerAssetAndLiabilityTableTextBlock
      - us-gaap_DisaggregationOfRevenueTableTextBlock
      - us-gaap_ScheduleOfProspectiveAdoptionOfNewAccountingPronouncementsTableTextBlock
      - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTextBlock
      - tsla_ScheduleOfCashAndCashEquivalentsAndRestrictedCashTableTextBlock
      - tsla_ScheduleOfDepreciationAndAmortizationComputedUsingStraightLineMethodOverEstimatedUsefulLivesOfAssetsTableTextBlock
      - tsla_ScheduleOfPropertyPlantAndEquipmentTextBlock
      - us-gaap_ScheduleOfProductWarrantyLiabilityTableTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureBusinessCombinationsTables

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_ScheduleOfRecognizedIdentifiedAssetsAcquiredAndLiabilitiesAssumedTableTextBlock
      - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsAcquiredAsPartOfBusinessCombinationTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_ScheduleOfFairValueAssetsAndLiabilitiesMeasuredOnRecurringBasisTableTextBlock
  - us-gaap_ScheduleOfInterestRateDerivativesTableTextBlock
  - us-gaap_ScheduleOfCarryingValuesAndEstimatedFairValuesOfDebtInstrumentsTableTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureInventoryTables

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_ScheduleOfInventoryCurrentTableTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSolarEnergySystemsNetTables

- us-gaap_LeasesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - tsla_ScheduleOfLeasedAssetsTableTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosurePropertyPlantAndEquipmentNetTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureAccruedLiabilitiesAndOtherTables

- us-gaap_PayablesAndAccrualsAbstract
  - tsla_ScheduleOfAccruedLiabilitiesAndOtherCurrentLiabilitiesTableTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureOtherLongTermLiabilitiesTables

- us-gaap_OtherLiabilitiesAbstract
  - us-gaap_OtherNoncurrentLiabilitiesTableTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtTableTextBlock
  - tsla_ScheduleOfInterestExpenseTableTextBlock
  - us-gaap_DebtInstrumentRedemptionTableTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesTables

- us-gaap_LeasesAbstract
  - tsla_ScheduleOfOperatingAndFinancingLeasesPresentedInBalanceSheetTableTextBlock
  - us-gaap_LeaseCostTableTextBlock
  - tsla_ScheduleOfSupplementalCashFlowInformationRelatedToLeasesTableTextBlock
  - tsla_ScheduleOfMaturitiesOfOperatingAndFinanceLeaseLiabilitiesTableTextBlock
  - tsla_ScheduleOfFutureMinimumLeasePaymentsUnderNonCancellableOperatingAndFinanceLeasesTableTextBlock
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedMaturityTableTextBlock
  - tsla_ScheduleOfFutureMinimumLeaseReceiptsTableTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureVariableInterestEntityArrangementsTables

- tsla_VariableInterestEntityDisclosureAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureRelatedPartyTransactionsTables

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_ScheduleOfRelatedPartyTransactionsTableTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTextBlock
  - us-gaap_ScheduleOfRevenueFromExternalCustomersAttributedToForeignCountriesByGeographicAreaTextBlock
  - us-gaap_ScheduleOfEntityWideDisclosureOnGeographicAreasLongLivedAssetsInIndividualForeignCountriesByCountryTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureQuarterlyResultsOfOperationsTables

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_ScheduleOfQuarterlyFinancialInformationTableTextBlock

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureOverviewAdditionalInformationDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NumberOfOperatingSegments
  - us-gaap_NumberOfReportableSegments

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_AccountingPoliciesAbstract
  - tsla_SummaryOfSignificantAccountingPoliciesTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_RegulatoryLiabilityAxis
    - us-gaap_GuaranteeObligationsByNatureAxis
      - us-gaap_GuaranteeObligationsNatureDomain
    - us-gaap_TypeOfArrangementAxis
      - us-gaap_ArrangementsAndNonarrangementTransactionsMember
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LeaseArrangementTypeAxis
      - us-gaap_LeaseArrangementTypeDomain
    - tsla_SummaryOfSignificantAccountingPoliciesLineItems
      - tsla_ReductionInAutomotiveSalesRevenuesFromBuybackOptions
      - tsla_ReductionInCostOfAutomotiveSalesFromBuybackOptions
      - tsla_ReductionInGrossProfitFromBuybackOptions
      - tsla_SalesReturnReserveFromBuybackOptions
      - tsla_SalesReturnReserveFromShortTermBuyBackOptions
      - tsla_ContractWithCustomerLiabilityRevenueRecognizedOutOfPriorPeriodBalance
      - tsla_ContractWithCustomerAssetAndLiabilityRevenueRecognizedInNextRollingTwelveMonths
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_ContractWithCustomerLiabilityRevenueRecognized
      - tsla_ContractWithCustomerLiabilityRevenueRecognitionPeriod
      - tsla_DirectLeaseTerm
      - us-gaap_ContractWithCustomerLiability
      - us-gaap_OperatingLeasesIncomeStatementLeaseRevenue
      - tsla_MaximumRepurchasePriceOfVehiclesUnderResaleValueArrangement
      - tsla_ResaleValueGuaranteesCurrentPortionSalesToLeasingPartners
      - tsla_ResaleValueGuarantee
      - us-gaap_DeferredCostsLeasingNetNoncurrent
      - tsla_ResaleValueGuaranteesCurrentPortionSalesToCustomers
      - tsla_ResaleValueGuaranteeLeaseRevenueRecognized
      - us-gaap_RevenueRemainingPerformanceObligation
      - us-gaap_OperatingLeaseRightOfUseAsset
      - us-gaap_OperatingLeaseLiability
      - tsla_DeRecognitionOfBuildToSuitLeaseAssets
      - tsla_DeRecognitionOfBuildToSuitLeaseLiabilities
      - us-gaap_NewAccountingPronouncementOrChangeInAccountingPrincipleCumulativeEffectOfChangeOnEquityOrNetAssets1
      - us-gaap_CostOfGoodsAndServicesSold
      - tsla_IncreaseDecreaseToNetIncomeLossAttributableToCommonStockholders
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - tsla_DebtInstrumentContractualMaturityYear
      - tsla_NumberOfCustomersWithKnownDisputesOrCollectionIssues
      - tsla_NumberOfCustomersWithMaterialNonAccrualOrPastDueNotesReceivable
      - tsla_LoansPayableTerm
      - tsla_NumberOfCustomersRepresentAccountReceivableThresholdPercentage
      - tsla_AccountsReceivableThresholdPercentage
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseGross
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAccumulatedDepreciation
      - us-gaap_DescriptionOfLesseeLeasingArrangementsOperatingLeases
      - us-gaap_OperatingLeasesOfLessorContingentRentalsBasisSpreadOnVariableRate
      - tsla_MinimumLeasePaymentPercentageOfFairValue
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - us-gaap_GoodwillImpairmentLoss
      - us-gaap_ForeignCurrencyTransactionGainLossRealized
      - us-gaap_StandardProductWarrantyDescription
      - us-gaap_ProductWarrantyExpense
      - tsla_IncentiveBeginningPeriod
      - tsla_IncentiveEndingPeriod
      - tsla_MaximumEligibleAmountOfTransferableInvestmentTaxCredits
      - tsla_ExpectedCapitalInvestment
      - us-gaap_InvestmentTaxCredit
      - us-gaap_CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption
      - us-gaap_Assets
      - us-gaap_Liabilities

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail1

- us-gaap_AccountingPoliciesAbstract
  - tsla_SummaryOfSignificantAccountingPoliciesTable
    - us-gaap_TypeOfArrangementAxis
      - us-gaap_ArrangementsAndNonarrangementTransactionsMember
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - tsla_SummaryOfSignificantAccountingPoliciesLineItems
      - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionPeriod1

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfAccruedWarrantyActivityDetail

- us-gaap_StandardProductWarrantyDisclosureAbstract
  - us-gaap_StandardProductWarrantyAccrual
  - us-gaap_ProductWarrantyAccrualAdditionsFromBusinessAcquisition
  - us-gaap_StandardProductWarrantyAccrualPayments
  - us-gaap_ProductWarrantyAccrualPreexistingIncreaseDecrease
  - tsla_StandardProductWarrantyAccrualAdditionsFromAdoptionOfNewRevenueStandard
  - us-gaap_StandardProductWarrantyAccrualWarrantiesIssued
  - us-gaap_StandardProductWarrantyAccrual

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureBusinessCombinationsAdditionalInformationDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionEffectiveDateOfAcquisition1
      - tsla_BusinessCombinationCommonStockConversionBasis
      - tsla_BusinessCombinationStockConversionRatio
      - us-gaap_BusinessCombinationConsiderationTransferred1
      - us-gaap_BusinessAcquisitionEquityInterestsIssuedOrIssuableNumberOfSharesIssued
      - us-gaap_BusinessAcquisitionSharePrice
      - us-gaap_PaymentsToAcquireBusinessesGross
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibleAssetsOtherThanGoodwill
      - us-gaap_Goodwill
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedNet
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfInterestRateSwapsOutstandingDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_InterestRateSwapMember

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_LongtermDebtTypeAxis
  - us-gaap_LongtermDebtTypeDomain
    - tsla_RecourseDebtMember
- us-gaap_DebtInstrumentAxis
  - us-gaap_DebtInstrumentNameDomain
    - tsla_OnePointTwoFivePercentConvertibleSeniorNoteDueInTwentyTwentyOneMember
    - tsla_FivePointThreeZeroPercentSeniorNotesDueTwentyTwentyFiveMember
    - tsla_TwoPointThreeSevenFivePercentConvertibleSeniorNotesDueInTwoThousandTwentyTwoMember
    - tsla_TwoPointZeroZeroPercentConvertibleSeniorNoteDueTwentyTwentyFourMember
    - tsla_ZeroCouponConvertibleSeniorNotesDueInTwoThousandTwentyMember

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfEstimatedFairValuesAndCarryingValuesDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_DebtInstrumentAxis
  - us-gaap_DebtInstrumentNameDomain
    - tsla_ConvertibleSeniorNotesMember
    - tsla_FivePointThreeZeroPercentSeniorNotesDueTwentyTwentyFiveMember
    - tsla_SolarAssetBackedNotesMember
    - tsla_SolarLoanBackedNotesMember

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfEstimatedFairValuesAndCarryingValuesParentheticalDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_LongtermDebtTypeAxis
  - us-gaap_LongtermDebtTypeDomain
    - tsla_RecourseDebtMember
- us-gaap_DebtInstrumentAxis
  - us-gaap_DebtInstrumentNameDomain
    - tsla_FivePointThreeZeroPercentSeniorNotesDueTwentyTwentyFiveMember

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureInventoryScheduleOfInventoryDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryRawMaterialsNetOfReserves
  - us-gaap_InventoryWorkInProcessNetOfReserves
  - us-gaap_InventoryFinishedGoodsNetOfReserves
  - us-gaap_InventoryPartsAndComponentsNetOfReserves
  - us-gaap_InventoryNet [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureInventoryAdditionalInformationDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryCurrentTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_InventoryLineItems
      - us-gaap_InventoryWriteDown

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSolarEnergySystemsNetComponentsOfSolarEnergySystemsNetDetail

- us-gaap_LeasesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - tsla_LeaseAssetsInService
      - tsla_LeaseAssetDirectCostsRelatedToAcquisition
      - tsla_LeasedAssetsGross [totalLabel]
      - tsla_LeasedAssetsAccumulatedDepreciationAndAmortization
      - tsla_LeasedAssetsNetBeforeConstructionAndPendingInterconnection [totalLabel]
      - tsla_AssetsToBeLeasedCIP
      - tsla_LeaseAssetsPendingInterconnection
      - tsla_LeasedAssetsNet [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSolarEnergySystemsNetComponentsOfSolarEnergySystemsNetParentheticalDetail

- us-gaap_LeasesAbstract
  - tsla_ScheduleOfFinanceLeasedAssetsTable
- us-gaap_PropertyPlantAndEquipmentByTypeAxis
  - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - tsla_SolarEnergySystemsMember

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosurePropertyPlantAndEquipmentNetScheduleOfPropertyPlantAndEquipmentNetDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosurePropertyPlantAndEquipmentNetAdditionalInformationDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentNet
      - us-gaap_InterestCostsCapitalized
      - us-gaap_Depreciation
      - tsla_FinanceLeaseRightOfUseAssetsBeforeAccumulatedDepreciation
      - tsla_FinanceLeaseAccumulatedDepreciation
      - us-gaap_ConstructionInProgressGross
      - tsla_IncentivesManufacturingEquipmentInvestments
      - tsla_IncentivesReceivedInCash
      - tsla_IncentivesReceivedInFormOfAssetsAndServices

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureAccruedLiabilitiesAndOtherScheduleOfAccruedLiabilitiesAndOtherCurrentLiabilitiesDetail

- us-gaap_PayablesAndAccrualsAbstract
  - tsla_AccruedPurchases
  - us-gaap_EmployeeRelatedLiabilitiesCurrent
  - us-gaap_TaxesPayableCurrent
  - us-gaap_DepositLiabilitiesAccruedInterest
  - tsla_FinancingObligationCurrent
  - us-gaap_ProductWarrantyAccrualClassifiedCurrent
  - tsla_SalesReturnReserveCurrent
  - tsla_BuildToSuitLeaseLiabilityAccruedCurrent
  - us-gaap_OperatingLeaseLiabilityCurrent
  - us-gaap_OtherLiabilitiesCurrent
  - tsla_AccruedAndOtherCurrentLiabilities [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureAccruedLiabilitiesAndOtherAdditionalInformationDetail

- us-gaap_PayablesAndAccrualsAbstract
  - tsla_BuildToSuitLeaseLiabilityAccruedCurrent

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureOtherLongTermLiabilitiesScheduleOfOtherLongTermLiabilitiesDetail

- us-gaap_OtherLiabilitiesNoncurrentAbstract
  - tsla_AccruedWarrantyReserveNoncurrent
  - tsla_BuildToSuitLeaseLiabilityNoncurrent
  - us-gaap_OperatingLeaseLiabilityNoncurrent
  - us-gaap_DeferredRentCreditNoncurrent
  - tsla_FinancingObligationNoncurrent
  - tsla_SalesReturnReserveNoncurrent
  - tsla_OtherLiabilitiesMiscellaneousNoncurrent
  - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureOtherLongTermLiabilitiesAdditionalInformationDetail

- us-gaap_OtherLiabilitiesNoncurrentAbstract
  - tsla_BuildToSuitLeaseLiabilityNoncurrent

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureCustomerDepositsAdditionalInformationDetail

- tsla_CustomerDepositsDisclosureAbstract
  - tsla_CustomerDepositsLiabilitiesCurrent

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtSummaryOfDebtDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_DebtCurrent
      - us-gaap_LongTermDebt
      - us-gaap_DebtInstrumentUnusedBorrowingCapacityAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentDescriptionOfVariableRateBasis
      - tsla_DebtInstrumentContractualMaturityMonthAndYear
      - tsla_DebtInstrumentContractualMaturityMonthAndYearRangeStart
      - tsla_DebtInstrumentContractualMaturityMonthAndYearRangeEnd

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebt2019Notes2021NotesBondHedgesAndWarrantTransactionsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtConversionByUniqueDescriptionAxis
      - us-gaap_DebtConversionNameDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - tsla_DebtInstrumentContractualMaturityMonthAndYear
      - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - us-gaap_DebtInstrumentConvertibleThresholdTradingDays
      - us-gaap_DebtInstrumentConvertibleThresholdConsecutiveTradingDays1
      - tsla_DebtInstrumentConvertibleConversionPricePercentage
      - us-gaap_DebtInstrumentRedemptionPricePercentage
      - tsla_PercentageOfPrincipalAmountOfConvertibleNotesIsEqualToRepurchasePrice
      - us-gaap_DebtInstrumentConvertibleCarryingAmountOfTheEquityComponent
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - tsla_NoteHedgesNumberOfSharesContractedToBuy
      - tsla_PurchasePricePerCommonStock
      - tsla_NoteHedgesTransactionCosts
      - us-gaap_ClassOfWarrantOrRightNumberOfSecuritiesCalledByWarrantsOrRights
      - us-gaap_ClassOfWarrantOrRightExercisePriceOfWarrantsOrRights1
      - us-gaap_ProceedsFromIssuanceOfWarrants
      - tsla_ConversionPricePerShare
      - us-gaap_RepaymentsOfLongTermDebt
      - us-gaap_DebtInstrumentConvertibleIfConvertedValueInExcessOfPrincipal

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebt2022NotesBondHedgesAndWarrantTransactionsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtConversionByUniqueDescriptionAxis
      - us-gaap_DebtConversionNameDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - tsla_DebtInstrumentContractualMaturityMonthAndYear
      - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - us-gaap_DebtInstrumentConvertibleThresholdTradingDays
      - us-gaap_DebtInstrumentConvertibleThresholdConsecutiveTradingDays1
      - tsla_DebtInstrumentConvertibleConversionPricePercentage
      - us-gaap_DebtInstrumentRedemptionPricePercentage
      - tsla_PercentageOfPrincipalAmountOfConvertibleNotesIsEqualToRepurchasePrice
      - us-gaap_DebtConversionOriginalDebtAmount1
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - tsla_NoteHedgesNumberOfSharesContractedToBuy
      - tsla_PurchasePricePerCommonStock
      - tsla_NoteHedgesTransactionCosts
      - us-gaap_ClassOfWarrantOrRightNumberOfSecuritiesCalledByWarrantsOrRights
      - us-gaap_ClassOfWarrantOrRightExercisePriceOfWarrantsOrRights1
      - us-gaap_ProceedsFromIssuanceOfWarrants
      - tsla_ConversionPricePerShare
      - us-gaap_DebtInstrumentConvertibleIfConvertedValueInExcessOfPrincipal

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebt2024NotesBondHedgesAndWarrantTransactionsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtConversionByUniqueDescriptionAxis
      - us-gaap_DebtConversionNameDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - tsla_DebtInstrumentContractualMaturityMonthAndYear
      - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - us-gaap_DebtInstrumentConvertibleThresholdTradingDays
      - us-gaap_DebtInstrumentConvertibleThresholdConsecutiveTradingDays1
      - tsla_DebtInstrumentConvertibleConversionPricePercentage
      - us-gaap_DebtInstrumentRedemptionPricePercentage
      - tsla_PercentageOfPrincipalAmountOfConvertibleNotesIsEqualToRepurchasePrice
      - us-gaap_DebtConversionOriginalDebtAmount1
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - tsla_NoteHedgesNumberOfSharesContractedToBuy
      - tsla_PurchasePricePerCommonStock
      - tsla_NoteHedgesTransactionCosts
      - us-gaap_ClassOfWarrantOrRightNumberOfSecuritiesCalledByWarrantsOrRights
      - us-gaap_ClassOfWarrantOrRightExercisePriceOfWarrantsOrRights1
      - us-gaap_ProceedsFromIssuanceOfWarrants
      - tsla_ConversionPricePerShare
      - us-gaap_DebtInstrumentConvertibleIfConvertedValueInExcessOfPrincipal

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebt2025NotesAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - tsla_DebtInstrumentContractualMaturityMonthAndYear
      - us-gaap_ProceedsFromDebtNetOfIssuanceCosts

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtCreditAgreementAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LineOfCreditFacilityAxis
      - us-gaap_LineOfCreditFacilityLenderDomain
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - us-gaap_ShortTermDebtTypeAxis
      - us-gaap_ShortTermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_LineOfCreditFacilityIncreaseDecreaseForPeriodNet
      - tsla_CommitmentsExtendedTerm

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebt1625ConvertibleSeniorNotesDueIn2019AdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentMaturityDate
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - us-gaap_RepaymentsOfLongTermDebt

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtZeroCouponConvertibleSeniorNotesDueIn2020AdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_SubsidiarySaleOfStockAxis
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - tsla_ConvertibleSeniorNotesIssueToRelatedParties
      - us-gaap_DebtInstrumentMaturityDate
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - us-gaap_DebtInstrumentRedemptionDescription
      - us-gaap_DebtInstrumentConvertibleThresholdPercentageOfStockPriceTrigger
      - us-gaap_DebtInstrumentConvertibleThresholdConsecutiveTradingDays1
      - us-gaap_DebtInstrumentRedemptionPricePercentageOfPrincipalAmountRedeemed
      - us-gaap_DebtInstrumentConvertibleIfConvertedValueInExcessOfPrincipal

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtSolarBondsAndOtherLoansAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentInterestRateStatedPercentage

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtChinaLoanAgreementsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - tsla_DebtInstrumentAnnualInterestRateAsPercentageOfOneYearLoanInterestRateQuotedByBank
      - tsla_DebtInstrumentPercentageOfInterestRateOnVariableRate
      - us-gaap_DebtInstrumentDescriptionOfVariableRateBasis
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtSolarLoanBackedNotesAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtWarehouseAgreementAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentMaturityDate
      - us-gaap_RepaymentsOfSecuredDebt

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtSolarTermLoansAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_RepaymentsOfLongTermDebt

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtSolarRenewableEnergyCreditAndOtherLoansAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - tsla_NumberOfWhollyOwnedSubsidiariesReceivedRemainingCashDistributions

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtScheduleOfInterestExpenseDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_InterestExpenseDebtExcludingAmortization
  - us-gaap_AmortizationOfFinancingCosts
  - us-gaap_AmortizationOfDebtDiscountPremium
  - us-gaap_InterestExpenseDebt [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDebtScheduleOfFuturePrincipalMaturitiesOfDebtDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive
      - us-gaap_DebtInstrumentCarryingAmount [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesAdditionalInformationDetail

- us-gaap_LeasesAbstract
  - tsla_ScheduleOfOperatingAndFinanceLeasedAssetsTable
- srt_RangeAxis
  - srt_RangeMember
    - srt_MaximumMember
    - srt_MinimumMember

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesScheduleOfComponentsOfLeaseExpenseDetail

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeaseDescriptionAbstract
  - us-gaap_LesseeFinanceLeaseDescriptionAbstract
    - us-gaap_FinanceLeaseRightOfUseAssetAmortization
    - us-gaap_FinanceLeaseInterestExpense
    - tsla_FinanceLeaseExpense [totalLabel]
  - us-gaap_LeaseCost [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesScheduleOfOtherInformationRelatedToLeasesDetail

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeaseWeightedAverageRemainingLeaseTerm1
  - us-gaap_FinanceLeaseWeightedAverageRemainingLeaseTerm1
  - us-gaap_OperatingLeaseWeightedAverageDiscountRatePercent
  - us-gaap_FinanceLeaseWeightedAverageDiscountRatePercent

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesScheduleOfMaturitiesOfOperatingAndFinanceLeaseLiabilitiesDetail

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueNextTwelveMonths
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearTwo
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearThree
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearFour
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearFive
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueAfterYearFive
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDue [totalLabel]
  - us-gaap_LesseeOperatingLeaseLiabilityUndiscountedExcessAmount
  - us-gaap_OperatingLeaseLiability [totalLabel]
  - us-gaap_OperatingLeaseLiabilityCurrent
  - us-gaap_OperatingLeaseLiabilityNoncurrent
  - us-gaap_FinanceLeaseLiabilityPaymentsDueNextTwelveMonths
  - us-gaap_FinanceLeaseLiabilityPaymentsDueYearTwo
  - us-gaap_FinanceLeaseLiabilityPaymentsDueYearThree
  - us-gaap_FinanceLeaseLiabilityPaymentsDueYearFour
  - us-gaap_FinanceLeaseLiabilityPaymentsDueYearFive
  - us-gaap_FinanceLeaseLiabilityPaymentsDueAfterYearFive
  - us-gaap_FinanceLeaseLiabilityPaymentsDue [totalLabel]
  - us-gaap_FinanceLeaseLiabilityUndiscountedExcessAmount
  - us-gaap_FinanceLeaseLiability [totalLabel]
  - us-gaap_FinanceLeaseLiabilityCurrent
  - us-gaap_FinanceLeaseLiabilityNoncurrent

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesScheduleOfFutureMinimumLeasePaymentsUnderNonCancellableLeasesASC840Detail

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueCurrent
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInTwoYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInThreeYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFourYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFiveYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueThereafter
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDue [totalLabel]
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueCurrent
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInTwoYears
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInThreeYears
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInFourYears
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInFiveYears
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueThereafter
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDue [totalLabel]
  - us-gaap_CapitalLeasesFutureMinimumPaymentsInterestIncludedInPayments
  - us-gaap_CapitalLeaseObligations [totalLabel]
  - us-gaap_CapitalLeaseObligationsCurrent
  - us-gaap_CapitalLeaseObligationsNoncurrent

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesMaturitiesOfOperatingLeaseReceivablesFromCustomersDetail

- us-gaap_LeasesAbstract
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedNextTwelveMonths
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedTwoYears
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedThreeYears
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedFourYears
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedFiveYears
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedThereafter

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasesFutureMinimumLeasePaymentsToBeReceivedFromCustomersUnderNonCancellableOperatingLeasesASC840Detail

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableCurrent
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInTwoYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInThreeYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInFourYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInFiveYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableThereafter
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivable [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureCommitmentsAndContingenciesAdditionalInformationDetail

- us-gaap_EnvironmentalRemediationObligationsAbstract
  - tsla_CommitmentsAndContingenciesTable
    - us-gaap_LeaseArrangementTypeAxis
      - us-gaap_LeaseArrangementTypeDomain
    - us-gaap_LongTermPurchaseCommitmentByCategoryOfItemPurchasedAxis
      - us-gaap_LongTermPurchaseCommitmentCategoryOfItemPurchasedDomain
    - srt_RangeAxis
      - srt_RangeMember
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - srt_LitigationCaseAxis
      - srt_LitigationCaseTypeDomain
    - tsla_CommitmentsAndContingenciesLineItems
      - us-gaap_CostOfGoodsAndServicesSold
      - us-gaap_TypeOfCostGoodOrServiceExtensibleList
      - us-gaap_LongTermPurchaseCommitmentAmount
      - tsla_AdditionalSpecifiedScopeCosts
      - us-gaap_LessorOperatingLeaseTermOfContract
      - tsla_OperatingLeaseOptionToRenewAmountPerYear
      - tsla_LeaseArrangementAmountRequiredToSpendOrIncur
      - us-gaap_ContractualObligation
      - us-gaap_LesseeOperatingLeaseTermOfContract
      - tsla_LesseeOperatingLeaseCapitalExpenditures
      - tsla_AnnualTaxRevenuesToBeGeneratedEndOfFiveYear
      - us-gaap_LossContingencyNumberOfPlaintiffs
      - tsla_CivilPenaltiesAmountPayable
      - tsla_NumberOfIndependentDirectors
      - tsla_IndependentDirectorServingPeriod
      - tsla_NumberOfAdditionalIndependentDirectors
      - us-gaap_LettersOfCreditOutstandingAmount

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationAdditionalInformationDetail

- us-gaap_PropertyPlantAndEquipmentByTypeAxis
  - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - tsla_SolarEnergySystemsUnderLeasePassThroughArrangementsMember
- srt_RangeAxis
  - srt_RangeMember
    - srt_MinimumMember
    - srt_MaximumMember

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationScheduleOfFutureMinimumLeasePaymentsToBeReceivedForOperatingLeasesDetail

- us-gaap_LessorLeaseDescriptionTable
  - us-gaap_BusinessAcquisitionAxis
    - us-gaap_BusinessAcquisitionAcquireeDomain
      - tsla_SolarCityMember
  - us-gaap_LessorLeaseDescriptionLineItems
    - us-gaap_LessorOperatingLeasePaymentsToBeReceivedNextTwelveMonths
    - us-gaap_LessorOperatingLeasePaymentsToBeReceivedTwoYears
    - us-gaap_LessorOperatingLeasePaymentsToBeReceivedThreeYears
    - us-gaap_LessorOperatingLeasePaymentsToBeReceivedFourYears
    - us-gaap_LessorOperatingLeasePaymentsToBeReceivedFiveYears
    - us-gaap_LessorOperatingLeasePaymentsToBeReceivedThereafter
    - us-gaap_LessorOperatingLeasePaymentsToBeReceived [totalLabel]

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureDefinedContributionPlanAdditionalInformationDetail

- us-gaap_CompensationAndRetirementDisclosureAbstract
  - us-gaap_DefinedContributionPlanMaximumAnnualContributionsPerEmployeePercent
  - us-gaap_DefinedContributionPlanEmployerDiscretionaryContributionAmount
  - us-gaap_DefinedContributionPlanSponsorLocationExtensibleList
  - us-gaap_DefinedContributionPlanTaxStatusExtensibleList

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureRelatedPartyTransactionsSummaryOfRelatedPartyTransactionsDetail

- us-gaap_RelatedPartyTransactionsAbstract
  - tsla_ConvertibleSeniorNotesIssueToRelatedParties

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureRelatedPartyTransactionsAdditionalInformationDetail

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_ScheduleOfRelatedPartyTransactionsByRelatedPartyTable
    - srt_TitleOfIndividualAxis
      - srt_TitleOfIndividualWithRelationshipToEntityDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_SubsidiarySaleOfStockAxis
    - us-gaap_RelatedPartyTransactionLineItems
      - tsla_ConvertibleSeniorNoteUnpaidPrincipalAmountDueToRelatedParties
      - us-gaap_StockIssuedDuringPeriodSharesNewIssues
      - us-gaap_StockIssuedDuringPeriodValueNewIssues
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_AdjustmentsToAdditionalPaidInCapitalEquityComponentOfConvertibleDebt

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasAdditionalInformationDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_NumberOfOperatingSegments
  - us-gaap_NumberOfReportableSegments

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureRestructuringAndOtherAdditionalInformationDetail

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_ScheduleOfRestructuringAndRelatedCostsTable
    - us-gaap_IndefiniteLivedIntangibleAssetsByMajorClassAxis
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_RestructuringCostAndReserveLineItems
      - us-gaap_BusinessExitCosts1
      - us-gaap_ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill
      - us-gaap_TangibleAssetImpairmentCharges
      - us-gaap_GainLossOnDispositionOfAssets1
      - us-gaap_PaymentsForRestructuring
      - us-gaap_RestructuringCosts
      - us-gaap_ImpairmentOfIntangibleAssetsExcludingGoodwill
      - us-gaap_LitigationSettlementExpense

### http://www.teslamotors.com/20191231/taxonomy/role/DisclosureQuarterlyResultsOfOperationsScheduleOfSelectedQuarterlyResultsOfOperationsDetail

- us-gaap_QuarterlyFinancialDataAbstract
  - us-gaap_Revenues
  - us-gaap_GrossProfit
  - us-gaap_NetIncomeLoss
  - us-gaap_IncomeLossFromContinuingOperationsPerBasicShare
  - us-gaap_IncomeLossFromContinuingOperationsPerDilutedShare

