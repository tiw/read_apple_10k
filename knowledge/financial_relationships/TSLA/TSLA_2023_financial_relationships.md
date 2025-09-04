# TSLA 2023 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.tesla.com/20221231/taxonomy/role/StatementConsolidatedStatementsOfOperations1

- us-gaap_RevenuesAbstract
  - tsla_AutomotiveSalesRevenue
  - tsla_AutomotiveRegulatoryCredits
  - tsla_AutomotiveLeasing
  - tsla_AutomotiveRevenues [totalLabel]
  - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
  - us-gaap_Revenues [totalLabel]
- us-gaap_OperatingExpensesAbstract
  - us-gaap_ResearchAndDevelopmentExpense
  - us-gaap_SellingGeneralAndAdministrativeExpense
  - tsla_RestructuringAndOtherExpenses
  - us-gaap_OperatingExpenses [totalLabel]
- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
- us-gaap_CostOfRevenueAbstract
  - tsla_AutomotiveSales
  - us-gaap_DirectCostsOfLeasedAndRentedPropertyOrEquipment
  - tsla_AutomotiveCostOfRevenues [totalLabel]
  - us-gaap_CostOfGoodsAndServicesSold
  - us-gaap_CostOfRevenue [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/StatementConsolidatedStatementsOfOperationsParenthetical

- us-gaap_IncomeStatementAbstract
  - us-gaap_StockholdersEquityNoteStockSplit
  - us-gaap_StockholdersEquityNoteStockSplitConversionRatio1

### http://www.tesla.com/20221231/taxonomy/role/StatementConsolidatedStatementsOfComprehensiveIncomeUnaudited

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_ProfitLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
    - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
    - us-gaap_UnrealizedGainLossOnInvestments
  - us-gaap_ComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterest [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTaxAttributableToNoncontrollingInterest
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/Role_StatementConsolidatedStatementsOfCashFlowsUnaudited

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - tsla_DepreciationAmortizationAndImpairment
  - us-gaap_ShareBasedCompensation
  - us-gaap_InventoryWriteDown
  - us-gaap_ForeignCurrencyTransactionGainLossUnrealized
  - tsla_NoncashInterestIncomeExpenseAndOtherOperatingActivities
  - tsla_GainLossOnDigitalAssets
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.tesla.com/20221231/taxonomy/role/DisclosureIncomeTaxes1

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/DisclosureIncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_SummaryOfPositionsForWhichSignificantChangeInUnrecognizedTaxBenefitsIsReasonablyPossibleTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfDisaggregationOfRevenueByMajorSourceDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_DisaggregationOfRevenueTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_DisaggregationOfRevenueLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_Revenues

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfDisaggregationOfRevenueByMajorSourceParentheticalDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_DisaggregationOfRevenueTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_DisaggregationOfRevenueLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_ContractWithCustomerLiabilityRevenueRecognized

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_DeferredRevenueArrangementTypeAxis
  - us-gaap_DeferredRevenueArrangementTypeDomain
    - tsla_RebatesAndIncentivesMember
- us-gaap_IncomeTaxAuthorityAxis
  - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_DomesticCountryMember
    - stpr_CA
    - tsla_UnitedStatesAndForeignJurisdictionsMember
- us-gaap_IncomeTaxAuthorityNameAxis
  - us-gaap_IncomeTaxAuthorityNameDomain
    - us-gaap_InternalRevenueServiceIRSMember

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfDeferredRevenueActivityDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ContractWithCustomerLiability
  - tsla_ContractWithCustomerLiabilityAdditions
  - tsla_ContractWithCustomerLiabilityIncreaseDecrease
  - us-gaap_ContractWithCustomerLiabilityRevenueRecognized
  - us-gaap_ContractWithCustomerLiability

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfReconciliationOfNetIncomeUsedInComputingBasicAndDilutedNetIncomePerShareOfCom

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NetIncomeLoss
  - tsla_BuyOutOfNoncontrollingInterest
  - us-gaap_NetIncomeLossAvailableToCommonStockholdersBasic [totalLabel]
  - us-gaap_DilutiveSecuritiesEffectOnBasicEarningsPerShareOther
  - us-gaap_NetIncomeLossAvailableToCommonStockholdersDiluted [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfReconciliationOfBasicToDilutedWeightedAverageSharesUsedInComputingNetIncomePer

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_IncrementalCommonSharesAttributableToShareBasedPaymentArrangements
  - us-gaap_IncrementalCommonSharesAttributableToConversionOfDebtSecurities
  - us-gaap_IncrementalCommonSharesAttributableToCallOptionsAndWarrants
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfPotentiallyDilutiveSharesThatWereExcludedFromComputationOfDilutedNetIncomePerSh

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTable
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareByAntidilutiveSecuritiesAxis
      - us-gaap_AntidilutiveSecuritiesNameDomain
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareLineItems
      - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureInventoryAdditionalInformationDetail

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureEquityIncentivePlansSummaryOfOperationalMilestoneBasedOnRevenueOrAdjustedEBITDADetail

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
      - tsla_OperationalMilestoneBasedOnRevenueAchievementStatusOne
      - tsla_OperationalMilestoneBasedOnRevenueAchievementStatusTwo
      - tsla_OperationalMilestoneBasedOnRevenueAchievementStatusThree
      - tsla_OperationalMilestoneBasedOnRevenueAchievementStatusFour
      - tsla_OperationalMilestoneBasedOnRevenueAchievementStatusFive
      - tsla_OperationalMilestoneBasedOnRevenueAchievementStatusSix
      - tsla_OperationalMilestoneBasedOnRevenueAchievementStatusSeven
      - tsla_OperationalMilestoneBasedOnRevenueAchievementStatusEight
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAOne
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDATwo
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAThree
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAFour
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAFive
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDASix
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDASeven
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAEight
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAAchievementStatusOne
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAAchievementStatusTwo
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAAchievementStatusThree
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAAchievementStatusFour
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAAchievementStatusFive
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAAchievementStatusSix
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAAchievementStatusSeven
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDAAchievementStatusEight

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureEquityIncentivePlansSummaryOfStockBasedCompensationExpenseDetail

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember
    - tsla_SellingGeneralAndAdministrativeExpenseMember
    - tsla_RestructuringAndOtherMember

### http://www.tesla.com/20221231/taxonomy/role/DisclosureIncomeTaxesAdditionalInformationDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_OperatingLossCarryforwardsTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_TaxPeriodAxis
      - us-gaap_TaxPeriodDomain
    - us-gaap_OperatingLossCarryforwardsLineItems
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_DeferredTaxAssetsNet
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsResearch
      - us-gaap_UndistributedEarningsOfForeignSubsidiaries
      - us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings
      - us-gaap_DeferredTaxLiabilityNotRecognizedAmountOfUnrecognizedDeferredTaxLiabilityUndistributedEarningsOfForeignSubsidiaries
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - us-gaap_IncomeTaxExaminationYearUnderExamination
      - tsla_BeneficialCorporateIncomeTaxRateForCertainEnterprises
      - tsla_CorporateIncomeTaxRate
      - tsla_BeneficialCorporateIncomeTaxRate
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_IncomeTaxReconciliationDeductionsOther
      - tsla_ResearchTaxCreditCarryForwardExpirationDates
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsGeneralBusiness
      - tsla_TaxCreditCarryForwardExpirationYear
      - us-gaap_DeferredTaxAssetsOperatingLossCarryforwardsDomestic
      - us-gaap_DeferredTaxAssetsOperatingLossCarryforwardsStateAndLocal
      - us-gaap_ValuationAllowanceDeferredTaxAssetChangeInAmount

### http://www.tesla.com/20221231/taxonomy/role/DisclosureIncomeTaxesScheduleOfIncomeBeforeProvisionForIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
  - tsla_IncomeLossFromContinuingOperationsBeforeIncomeTaxesAttributableToNoncontrollingInterestAndRedeemableNoncontrollingInterest
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/DisclosureIncomeTaxesComponentsOfProvisionForIncomeTaxesDetails

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

### http://www.tesla.com/20221231/taxonomy/role/DisclosureIncomeTaxesScheduleOfDeferredTaxAssetsLiabilitiesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
    - us-gaap_DeferredTaxAssetsOperatingLossCarryforwards
    - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsResearch
    - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsOther
    - us-gaap_DeferredTaxAssetsDeferredIncome
    - us-gaap_DeferredTaxAssetsInventory
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
    - tsla_DeferredTaxAssetsOperatingLeaseRightOfUseLiabilities
    - tsla_DeferredTaxAssetsCapitalizedResearchAndDevelopmentCosts
    - tsla_DeferredTaxAssetsDeferredGlobalIntangibleLowTaxedIncomeTaxAssets
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccrualsOther
    - us-gaap_DeferredTaxAssetsGross [totalLabel]
    - us-gaap_DeferredTaxAssetsValuationAllowance
    - us-gaap_DeferredTaxAssetsNet [totalLabel]
  - us-gaap_ComponentsOfDeferredTaxLiabilitiesAbstract
    - us-gaap_DeferredTaxLiabilitiesPropertyPlantAndEquipment
    - us-gaap_DeferredTaxLiabilitiesInvestments
    - tsla_DeferredTaxLiabilitiesOperatingLeaseRightOfUseAssets
    - us-gaap_DeferredTaxLiabilitiesTaxDeferredIncome
    - us-gaap_DeferredTaxLiabilitiesOther
    - us-gaap_DeferredIncomeTaxLiabilities
    - tsla_DeferredTaxAssetLiabilitiesNet [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/DisclosureIncomeTaxesScheduleOfReconciliationOfTaxesAtFederalStatutoryRateToProvisionForIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
  - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
  - us-gaap_IncomeTaxReconciliationNondeductibleExpenseShareBasedCompensationCost
  - us-gaap_IncomeTaxReconciliationNondeductibleExpenseOther
  - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense
  - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
  - us-gaap_IncomeTaxReconciliationTaxCredits
  - us-gaap_IncomeTaxReconciliationMinorityInterestIncomeExpense
  - tsla_Effectiveincometaxratereconciliationglobalintangiblelowtaxedincomeinclusion
  - tsla_Effectiveincometaxratereconciliationunrecognizedtaxbenefits
  - us-gaap_IncomeTaxReconciliationChangeInDeferredTaxAssetsValuationAllowance
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/DisclosureIncomeTaxesScheduleOfChangesToGrossUnrecognizedTaxBenefitsDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_UnrecognizedTaxBenefits
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsReductionsResultingFromLapseOfApplicableStatuteOfLimitations
  - us-gaap_UnrecognizedTaxBenefits

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfTotalRevenuesAndGrossProfitByReportableSegmentDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingRevenueReconcilingItemLineItems
      - us-gaap_Revenues
      - us-gaap_GrossProfit

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfRevenuesByGeographicAreaDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
      - us-gaap_Revenues

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfLongLivedAssetsByGeographicAreaDetail

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - srt_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

## 资产负债表结构 (Balance Sheet Structure)

### http://www.tesla.com/20221231/taxonomy/role/StatementConsolidatedBalanceSheets1

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

### http://www.tesla.com/20221231/taxonomy/role/StatementConsolidatedBalanceSheetsParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_PreferredStockParOrStatedValuePerShare
  - us-gaap_PreferredStockSharesAuthorized
  - us-gaap_PreferredStockSharesIssued
  - us-gaap_PreferredStockSharesOutstanding
  - us-gaap_CommonStockParOrStatedValuePerShare
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_CommonStockSharesIssued
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquityNoteStockSplit
  - us-gaap_StockholdersEquityNoteStockSplitConversionRatio1

### http://www.tesla.com/20221231/taxonomy/role/StatementConsolidatedStatementsOfRedeemableNoncontrollingInterestAndStockholdersEquityUnaudited

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - tsla_RedeemableNoncontrollingInterestsMember
    - us-gaap_CommonStockMember
    - us-gaap_AdditionalPaidInCapitalMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
    - us-gaap_RetainedEarningsMember
    - us-gaap_ParentMember
    - us-gaap_NoncontrollingInterestMember
- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable

### http://www.tesla.com/20221231/taxonomy/role/StatementConsolidatedStatementsOfRedeemableNoncontrollingInterestAndStockholdersEquityUnauditedParenthetical

- us-gaap_StatementOfStockholdersEquityAbstract
  - tsla_CommonStockPublicOfferingIssuanceCosts
  - us-gaap_StockholdersEquityNoteStockSplitConversionRatio1
  - us-gaap_StockholdersEquityNoteStockSplit

### http://www.tesla.com/20221231/taxonomy/role/Role_StatementConsolidatedStatementsOfCashFlowsUnaudited

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_ProfitLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
    - tsla_PaymentsForSolarEnergySystemsNetOfSales
    - tsla_PurchaseOfDigitalAssets
    - tsla_ProceedsFromSalesOfDigitalAssets
    - tsla_PaymentsToAcquireOtherIndefiniteLivedIntangibleAssets
    - us-gaap_PaymentsToAcquireInvestments
    - us-gaap_ProceedsFromSaleMaturityAndCollectionsOfInvestments
    - tsla_GovernmentGrantReceipt
    - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_ProceedsFromIssuanceOfCommonStock
    - us-gaap_ProceedsFromIssuanceOfDebt
    - tsla_RepaymentsOfConvertibleAndOtherDebt
    - us-gaap_ProceedsFromRepaymentsOfSecuredDebt
    - us-gaap_ProceedsFromIssuanceOfSharesUnderIncentiveAndShareBasedCompensationPlansIncludingStockOptions
    - us-gaap_FinanceLeasePrincipalPayments
    - us-gaap_PaymentsOfDebtIssuanceCosts
    - us-gaap_ProceedsFromMinorityShareholders
    - us-gaap_PaymentsToMinorityShareholders
    - tsla_PaymentsForBuyOutsOfNoncontrollingInterestsInSubsidiaries
    - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
  - us-gaap_EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect [totalLabel]
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations
  - us-gaap_NoncashInvestingAndFinancingItemsAbstract
    - us-gaap_NoncashOrPartNoncashAcquisitionValueOfAssetsAcquired1
  - us-gaap_SupplementalCashFlowInformationAbstract
    - us-gaap_InterestPaidNet
    - us-gaap_IncomeTaxesPaid

### http://www.tesla.com/20221231/taxonomy/role/DisclosureDigitalAssetsNet

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - tsla_DigitalAssetsNetTextBlock

### http://www.tesla.com/20221231/taxonomy/role/DisclosureGoodwillAndIntangibleAssets1

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_IntangibleAssetsDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/DisclosureIntangibleAssetsTables

- tsla_IntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetsByMajorClassTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_RegulatoryLiabilityAxis
  - us-gaap_RegulatoryLiabilityDomain
    - us-gaap_DeferredLeaseRevenueMember

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesEstimatedUsefulLivesOfRespectiveAssetsDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_LessorOperatingLeaseTermOfContract

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfEstimatedUsefulLivesOfRelatedAssetsDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesCumulativeEffectOfChangesMadeOnConsolidatedBalanceSheetForAdoptionOfAsu202006Detail

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - srt_RestatementAxis
      - srt_RestatementDomain
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_StatementLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAbstract
      - us-gaap_TemporaryEquityAbstract
      - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterestAbstract

### http://www.tesla.com/20221231/taxonomy/role/DisclosureDigitalAssetsNetAdditionalInformationDetail

- us-gaap_IntangibleAssetsNetExcludingGoodwillAbstract
  - us-gaap_PaymentsToAcquireIntangibleAssets
  - tsla_DigitalAssetsPurchaseCurrencyConversionRate
  - us-gaap_ImpairmentOfIntangibleAssetsExcludingGoodwill
  - us-gaap_GainLossOnDispositionOfIntangibleAssets
  - tsla_DigitalAssetsNetNonCurrent
  - tsla_CumulativeImpairmentOfIntangibleAssetsExcludingGoodwill
  - tsla_FairMarketValueOfIntangibleAssets

### http://www.tesla.com/20221231/taxonomy/role/DisclosureGoodwillAndIntangibleAssetsAdditionalInformationDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillPeriodIncreaseDecrease
  - us-gaap_Goodwill
  - us-gaap_GoodwillImpairedAccumulatedImpairmentLoss
  - us-gaap_IntangibleAssetsNetExcludingGoodwill

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureFairValueOfFinancialInstrumentsScheduleOfAssetsAndLiabilitiesMeasuredAtFairValueOnRecurringBasisDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_InvestmentTypeAxis
      - us-gaap_InvestmentTypeCategorizationMember
    - us-gaap_SecurityOwnedAndSoldNotYetPurchasedAtFairValueAxis
      - us-gaap_SecurityOwnedAndSoldNotYetPurchasedFairValueSecurityNameDomain
    - us-gaap_FinancialInstrumentAxis
      - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
    - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
      - us-gaap_AssetsFairValueDisclosure
      - us-gaap_LiabilitiesFairValueDisclosure
      - us-gaap_FairValueNetAssetLiability [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfCashCashEquivalentsAndMarketableSecuritiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_MarketableSecuritiesTable
- us-gaap_CashAndCashEquivalentsAxis
  - us-gaap_RestrictedCashAndCashEquivalentsCashAndCashEquivalentsMember
    - us-gaap_USGovernmentCorporationsAndAgenciesSecuritiesMember

### http://www.tesla.com/20221231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsSummaryOfFairValueOfMarketableSecuritiesByContractualMaturitiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesNextRollingTwelveMonthsAmortizedCostBasis
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearTwoThroughFiveAmortizedCostBasis
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearSixThroughTenAmortizedCostBasis
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingAfterYearTenAmortizedCostBasis
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesSingleMaturityDateAmortizedCostBasis [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureFairValueOfFinancialInstrumentsScheduleOfInterestRateSwapsOutstandingDetail

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_DerivativeNotionalAmount
    - us-gaap_DerivativeLiabilityFairValueGrossAsset
    - us-gaap_DerivativeFairValueOfDerivativeLiability
    - us-gaap_DerivativeLossOnDerivative
    - us-gaap_DerivativeLossStatementOfIncomeOrComprehensiveIncomeExtensibleEnumeration
    - us-gaap_DerivativeGainOnDerivative
    - us-gaap_DerivativeGainStatementOfIncomeOrComprehensiveIncomeExtensibleEnumeration

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureFairValueOfFinancialInstrumentsAdditionalInformationDetail

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_DebtInstrumentAxis
  - us-gaap_LongtermDebtTypeAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_DebtInstrumentInterestRateStatedPercentage
    - tsla_DebtInstrumentContractualMaturityYear

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureFairValueOfFinancialInstrumentsScheduleOfEstimatedFairValuesAndCarryingValuesDetail

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_DebtInstrumentAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_LongTermDebt
    - us-gaap_LongTermDebtFairValue

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSolarEnergySystemsNetComponentsOfSolarEnergySystemsNetParentheticalDetails

- tsla_FinanceLeasedAssetsLineItems
  - us-gaap_DepreciationAndAmortization
  - tsla_GrossSolarEnergySystemUnderLeasePassThroughFundArrangement
  - tsla_GrossSolarEnergySystemUnderLeasePassThroughFundArrangementAccumulatedDepreciation

### http://www.tesla.com/20221231/taxonomy/role/DisclosureDebt2022NotesBondHedgesAndWarrantTransactionsAdditionalInformationDetails

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember

### http://www.tesla.com/20221231/taxonomy/role/DisclosureDebt2024NotesBondHedgesAndWarrantTransactionsAdditionalInformationDetails

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember

### http://www.tesla.com/20221231/taxonomy/role/DisclosureDebtSolarAssetAndLoanbackedNotesAdditionalInformationDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentCollateralAmount
      - us-gaap_ProceedsFromRepaymentsOfLinesOfCredit
      - us-gaap_ExtinguishmentOfDebtAmount

### http://www.tesla.com/20221231/taxonomy/role/DisclosureDebtPledgedAssetsAdditionalInformationDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_PledgedStatusAxis
      - us-gaap_PledgedStatusDomain
    - us-gaap_FairValueByMeasurementBasisAxis
      - us-gaap_FairValueDisclosureItemAmountsDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_AssetsFairValueDisclosure

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeasesScheduleOfOperatingAndFinancingLeasesPresentedInBalanceSheetsDetail

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_LesseeLeaseDescriptionLineItems
      - us-gaap_LesseeOperatingLeaseDescriptionAbstract
      - us-gaap_LesseeFinanceLeaseDescriptionAbstract

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureVariableInterestEntityArrangementsCarryingValuesOfAssetsAndLiabilitiesOfSubsidiaryInConsolidatedBalanceSheetsDetail

- tsla_VariableInterestEntityDisclosureAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTable
    - srt_ConsolidatedEntitiesAxis
      - srt_ConsolidatedEntitiesDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_VariableInterestEntityLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAbstract

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfLongLivedAssetsByGeographicAreaDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - country_DE
    - country_CN
    - tsla_OtherInternationalMember

## 现金流量表结构 (Cash Flow Structure)

### http://www.tesla.com/20221231/taxonomy/role/Role_StatementConsolidatedStatementsOfCashFlowsUnaudited

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInInventories
  - tsla_IncreaseDecreaseInOperatingLeaseVehicles
  - us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets
  - us-gaap_IncreaseDecreaseInOtherNoncurrentAssets
  - us-gaap_IncreaseDecreaseInAccountsPayableAndAccruedLiabilities
  - us-gaap_IncreaseDecreaseInContractWithCustomerLiability
  - tsla_IncreaseDecreaseInContractWithCustomerLiabilityCustomerDeposits
  - us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_AccountsNotesLoansAndFinancingReceivableByReceivableTypeAxis
  - us-gaap_ReceivableTypeDomain

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfCashAndCashEquivalentsAndRestrictedCashDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_RestrictedCashCurrent
  - us-gaap_RestrictedCashNoncurrent
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfCashCashEquivalentsAndMarketableSecuritiesDetails

- us-gaap_MarketableSecuritiesTable
  - us-gaap_FinancialInstrumentAxis
    - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
      - us-gaap_CorporateDebtSecuritiesMember
      - us-gaap_CertificatesOfDepositMember
      - tsla_CertificatesOfDepositAndTimeDepositsMember
      - us-gaap_CashMember
      - us-gaap_MoneyMarketFundsMember
  - us-gaap_InvestmentTypeAxis
    - us-gaap_InvestmentTypeCategorizationMember
      - us-gaap_CashAndCashEquivalentsMember
  - us-gaap_CashAndCashEquivalentsAxis
  - us-gaap_SecurityOwnedAndSoldNotYetPurchasedAtFairValueAxis
    - us-gaap_SecurityOwnedAndSoldNotYetPurchasedFairValueSecurityNameDomain
      - us-gaap_USGovernmentDebtSecuritiesMember
  - us-gaap_MarketableSecuritiesLineItems
    - us-gaap_AvailableForSaleSecuritiesAmortizedCost
    - tsla_AvailableForSaleOfSecuritiesAmortizedCost
    - us-gaap_AvailableForSaleDebtSecuritiesGrossUnrealizedGain
    - us-gaap_AvailableForSaleDebtSecuritiesGrossUnrealizedLoss
    - us-gaap_AvailableForSaleSecuritiesDebtSecurities
    - us-gaap_ShortTermInvestments
    - us-gaap_MarketableSecurities
    - us-gaap_CashCashEquivalentsAndShortTermInvestments

### http://www.tesla.com/20221231/taxonomy/role/DisclosureDebtCashEquityDebtAdditionalInformationDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeasesScheduleOfComponentsOfLeaseExpenseAndOtherInformationRelatedToLeasesDetail

- us-gaap_LesseeOperatingLeaseDescriptionAbstract
  - us-gaap_OperatingLeaseExpense

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeasesSupplementalCashFlowInformationRelatedToLeasesDetail

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeasePayments
  - us-gaap_FinanceLeaseInterestPaymentOnLiability
  - us-gaap_FinanceLeasePrincipalPayments
  - us-gaap_RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability
  - us-gaap_RightOfUseAssetObtainedInExchangeForOperatingLeaseLiability

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeasesScheduleOfMaturitiesOfOperatingAndFinanceLeaseLiabilitiesDetail

- us-gaap_OperatingLeaseLiabilitiesPaymentsDueAbstract
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

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeasesMaturitiesOfOperatingLeaseAndSalestypeLeaseReceivablesFromCustomersDetail

- us-gaap_SalesTypeAndDirectFinancingLeasesLeaseReceivableFiscalYearMaturityAbstract
  - us-gaap_SalesTypeAndDirectFinancingLeasesLeaseReceivablePaymentsToBeReceivedNextTwelveMonths
  - us-gaap_SalesTypeAndDirectFinancingLeasesLeaseReceivablePaymentsToBeReceivedTwoYears
  - us-gaap_SalesTypeAndDirectFinancingLeasesLeaseReceivablePaymentsToBeReceivedThreeYears
  - us-gaap_SalesTypeAndDirectFinancingLeasesLeaseReceivablePaymentsToBeReceivedFourYears
  - us-gaap_SalesTypeAndDirectFinancingLeasesLeaseReceivablePaymentsToBeReceivedFiveYears
  - us-gaap_SalesTypeAndDirectFinancingLeasesLeaseReceivablePaymentsToBeReceivedThereafter
  - us-gaap_SalesTypeAndDirectFinancingLeasesLeaseReceivablePaymentsToBeReceived [totalLabel]
- us-gaap_LessorOperatingLeasePaymentsFiscalYearMaturityAbstract
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedNextTwelveMonths
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedTwoYears
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedThreeYears
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedFourYears
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedFiveYears
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedThereafter
  - us-gaap_LessorOperatingLeasePaymentsToBeReceived [totalLabel]

## 股东权益结构 (Equity Structure)

### http://www.tesla.com/20221231/taxonomy/role/StatementConsolidatedStatementsOfOperations1

- us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding
- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.tesla.com/20221231/taxonomy/role/StatementConsolidatedStatementsOfRedeemableNoncontrollingInterestAndStockholdersEquityUnaudited

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - srt_RestatementAxis
    - srt_RestatementDomain
      - srt_RevisionOfPriorPeriodAccountingStandardsUpdateAdjustmentMember
  - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
    - us-gaap_TypeOfAdoptionMember
      - us-gaap_AccountingStandardsUpdate201602Member
      - us-gaap_AccountingStandardsUpdate201613Member
      - tsla_AdjustmentsForPriorPeriodsFromAdoptingAsu202006Member
  - us-gaap_SubsidiarySaleOfStockAxis
    - us-gaap_SaleOfStockNameOfTransactionDomain
      - tsla_FebruaryTwoThousandTwentyPublicOfferingMember
      - tsla_MayTwoThousandNineteenPublicOfferingMember
      - tsla_AtMarketOfferingProgramMember
  - us-gaap_DebtInstrumentAxis
    - us-gaap_DebtInstrumentNameDomain
      - tsla_TwoPointZeroZeroPercentSeniorConvertibleNoteDueTwentyTwentyFourMember
  - us-gaap_StatementLineItems
    - us-gaap_RedeemableNoncontrollingInterestEquityCarryingAmount
    - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest
    - us-gaap_SharesIssued
    - tsla_ReclassificationsOfPermanentEquityToTemporaryEquity
    - us-gaap_StockIssuedDuringPeriodValueConversionOfConvertibleSecurities
    - us-gaap_StockIssuedDuringPeriodSharesConversionOfConvertibleSecurities
    - tsla_WarrantsSettlement
    - tsla_WarrantsSettlementShares
    - tsla_StockIssuedDuringPeriodValueEquityIncentiveAwards
    - tsla_StockIssuedDuringPeriodSharesEquityIncentiveAwards
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
    - us-gaap_StockIssuedDuringPeriodSharesNewIssues
    - us-gaap_StockIssuedDuringPeriodValueNewIssues
    - tsla_NoncontrollingInterestsIncreaseFromContributionsFromNoncontrollingInterests
    - us-gaap_MinorityInterestDecreaseFromDistributionsToNoncontrollingInterestHolders
    - us-gaap_MinorityInterestDecreaseFromRedemptions
    - tsla_NetIncomeLossIncludingPortionAttributableToRedeemableNonControllingInterestAndNonControllingInterestInSubsidiaries
    - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent
    - us-gaap_RedeemableNoncontrollingInterestEquityCarryingAmount
    - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest
    - us-gaap_SharesIssued

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureEquityIncentivePlans

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ShareholdersEquityAndShareBasedPaymentsTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureEquityIncentivePlansTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationActivityTableTextBlock
  - tsla_ScheduleOfShareBasedPaymentAwardStockOptionsAndEmployeeStockPurchasePlanValuationAssumptionsTableTextBlock
  - tsla_SummaryOfOperationalMilestoneBasedOnRevenueOrAdjustedEBITDATableTextBlock
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureEquityIncentivePlansAdditionalInformationDetail

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
    - srt_StatementScenarioAxis
      - srt_ScenarioUnspecifiedDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_DeferredCompensationArrangementWithIndividualMaximumContractualTerm1
      - us-gaap_CommonStockCapitalSharesReservedForFutureIssuance
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue [totalLabel]
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardOfRemainingVestingOption
      - tsla_PercentageOfPayrollDeductionsOfEmployeesEligibleCompensation
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardDiscountFromMarketPriceOfferingDate
      - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockPurchasePlans
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardValueOfSharesAvailableForIssuance
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodGross
      - us-gaap_StockholdersEquityReverseStockSplit
      - tsla_NumberOfTranches
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingRights
      - tsla_MarketCapitalization
      - tsla_IncreaseToMarketCapitalizationForEachRemainingMilestone
      - tsla_NumberOfOperationalMilestonesFocusedOnRevenueTargets
      - tsla_NumberOfOperationalMilestonesFocusedOnAdjustedEBITDA
      - tsla_NumberOfOperationalMilestonesAchieved
      - tsla_ShareBasedCompensationArrangementPaymentOfExercisePricePerShare
      - tsla_ShareBasedCompensationArrangementHoldingPeriodOfSharesPostExercise
      - tsla_RecognizedCatchUpExpenseDuringPeriod
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
      - us-gaap_ShareBasedCompensation
      - tsla_AggregateCatchUpExpense
      - tsla_PercentageOfPerformanceMilestoneGrossMargin
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardDividedEquallyInNumberOfTranches
      - tsla_GrossMargin
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsVestedInPeriodFairValue1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
      - tsla_NumberOfTranches
      - tsla_OperationalMilestoneBasedOnRevenue
      - tsla_OperationalMilestoneBasedOnAdjustedEBITDA
      - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsCapitalizedAmount
      - tsla_MarketCapitalizationAchieved
      - us-gaap_UnamortizedDebtIssuanceExpense
      - tsla_RemainingMarketCapitalization
      - tsla_MarketCapitalizationMilestone
      - tsla_PortionOfStockOptionsScheduledToVestUponSuccessfulCompletionOfPerformanceObjectives
      - tsla_NumberOfVehicleProduction
      - tsla_InitialMarketCapitalization
      - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromExerciseOfStockOptions

### http://www.tesla.com/20221231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfStockOptionAndRsuActivityDetail

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
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestOutstandingAggregateIntrinsicValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestExercisableAggregateIntrinsicValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExercisedOrReleasedInPeriod
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedAndExpectedToVest
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExercisedOrReleasedWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsToVestedAndExpectedToVestWeightedAverageGrantDateFairValue

### http://www.tesla.com/20221231/taxonomy/role/DisclosureEquityIncentivePlansScheduleOfFairValueOfStockOptionAwardAndEsppOnGrantDateDetail

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

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureEquityIncentivePlansSummaryOfStockBasedCompensationExpenseDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
      - us-gaap_AllocatedShareBasedCompensationExpense

## 其他结构 (Other Structure)

### http://www.tesla.com/20221231/taxonomy/role/Role_DocumentDocumentAndEntityInformation

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
  - dei_EntityFilerCategory
  - dei_EntitySmallBusiness
  - dei_EntityEmergingGrowthCompany
  - dei_EntityShellCompany
  - dei_EntityPublicFloat
  - dei_EntityVoluntaryFilers
  - dei_EntityCommonStockSharesOutstanding
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
  - dei_IcfrAuditorAttestationFlag
  - dei_DocumentsIncorporatedByReferenceTextBlock
  - dei_AuditorName
  - dei_AuditorFirmId
  - dei_AuditorLocation

### http://www.tesla.com/20221231/taxonomy/role/StatementConsolidatedStatementsOfOperations1

- us-gaap_StatementTable
  - srt_ProductOrServiceAxis
    - srt_ProductsAndServicesDomain
      - tsla_AutomotiveRevenuesMember
      - tsla_EnergyGenerationAndStorageMember
      - tsla_ServicesAndOtherMember
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

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureOverview

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NatureOfOperations

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSummaryOfSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_SignificantAccountingPoliciesTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureFairValueOfFinancialInstruments

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueDisclosuresTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureInventory

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSolarEnergySystemsNet

- us-gaap_LeasesAbstract
  - tsla_SolarEnergySystemsNetDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosurePropertyPlantAndEquipmentNet

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureAccruedLiabilitiesAndOther

- us-gaap_PayablesAndAccrualsAbstract
  - us-gaap_AccountsPayableAndAccruedLiabilitiesDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureOtherLongTermLiabilities

- us-gaap_OtherLiabilitiesAbstract
  - us-gaap_OtherLiabilitiesDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureDebt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeases

- us-gaap_LeasesAbstract
  - tsla_LesseeOperatingAndFinanceLeasesDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureCommitmentsAndContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureVariableInterestEntityArrangements

- tsla_VariableInterestEntityDisclosureAbstract
  - us-gaap_VariableInterestEntityDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureRelatedPartyTransactions

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_RelatedPartyTransactionsDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSegmentReportingAndInformationAboutGeographicAreas

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/DisclosureRestructuringAndOther

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_RestructuringImpairmentAndOtherActivitiesDisclosureTextBlock

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSubsequentEvents

- us-gaap_SubsequentEventsAbstract
  - us-gaap_SubsequentEventsTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSummaryOfSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - tsla_UnauditedInterimFinancialStatementPolicyTextBlock
  - us-gaap_ConsolidationPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_PriorPeriodReclassificationAdjustmentDescription
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - us-gaap_ResearchAndDevelopmentExpensePolicy
  - us-gaap_CostOfSalesPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_ComprehensiveIncomePolicyPolicyTextBlock
  - us-gaap_ShareBasedCompensationOptionAndIncentivePlansPolicy
  - tsla_NoncontrollingInterestsPolicyTextBlock
  - us-gaap_EarningsPerSharePolicyTextBlock
  - us-gaap_BusinessCombinationsPolicy
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_CashAndCashEquivalentsRestrictedCashAndCashEquivalentsPolicy
  - us-gaap_InvestmentPolicyTextBlock
  - us-gaap_MarketableSecuritiesPolicy
  - us-gaap_ReceivablesPolicyTextBlock
  - us-gaap_FinanceLoansAndLeasesReceivablePolicy
  - us-gaap_ConcentrationRiskCreditRisk
  - us-gaap_InventoryPolicyTextBlock
  - tsla_PropertySubjectToOrAvailableForOperatingLeasePolicyTextBlock
  - tsla_DigitalAssetsNetPolicyTextBlock
  - tsla_SolarRenewableEnergyCreditsPolicyTextBlock
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_ImpairmentOrDisposalOfLongLivedAssetsIncludingIntangibleAssetsPolicyPolicyTextBlock
  - us-gaap_GoodwillAndIntangibleAssetsGoodwillPolicy
  - us-gaap_InternalUseSoftwarePolicy
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_StandardProductWarrantyPolicy
  - tsla_CustomerDepositsPolicyTextBlock
  - tsla_GovernmentAssistanceProgramsAndIncentivesPolicyTextBlock
  - tsla_TaxIncentivePolicyTextBlock
  - tsla_DefinedContributionPlanPolicyTextBlock
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSummaryOfSignificantAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_DisaggregationOfRevenueTableTextBlock
  - us-gaap_ContractWithCustomerAssetAndLiabilityTableTextBlock
  - tsla_SalesTypeAndDirectFinancingLeasesLeaseReceivablesGrossDifferenceTableTextBlock
  - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock
  - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTextBlock
  - tsla_ScheduleOfCashAndCashEquivalentsAndRestrictedCashTableTextBlock
  - tsla_ScheduleOfCreditLossesRelatedToFinancingReceivablesCurrentAndNonCurrentTableTextBlock
  - us-gaap_PastDueFinancingReceivablesTableTextBlock
  - tsla_ScheduleOfDepreciationAndAmortizationComputedUsingStraightLineMethodOverEstimatedUsefulLivesOfAssetsTableTextBlock
  - tsla_ScheduleOfPropertyPlantAndEquipmentTextBlock
  - us-gaap_ScheduleOfProductWarrantyLiabilityTableTextBlock
  - us-gaap_ScheduleOfNewAccountingPronouncementsAndChangesInAccountingPrinciplesTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureFairValueOfFinancialInstrumentsTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_ScheduleOfFairValueAssetsAndLiabilitiesMeasuredOnRecurringBasisTableTextBlock
  - us-gaap_CashCashEquivalentsAndMarketableSecuritiesTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock
  - us-gaap_ScheduleOfInterestRateDerivativesTableTextBlock
  - us-gaap_ScheduleOfCarryingValuesAndEstimatedFairValuesOfDebtInstrumentsTableTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureInventoryTables

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_ScheduleOfInventoryCurrentTableTextBlock

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSolarEnergySystemsNetTables

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_ScheduleOfPropertySubjectToOrAvailableForOperatingLeaseTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosurePropertyPlantAndEquipmentNetTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureAccruedLiabilitiesAndOtherTables

- us-gaap_PayablesAndAccrualsAbstract
  - tsla_ScheduleOfAccruedLiabilitiesAndOtherCurrentLiabilitiesTableTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureOtherLongTermLiabilitiesTables

- us-gaap_OtherLiabilitiesAbstract
  - us-gaap_OtherNoncurrentLiabilitiesTableTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureDebtTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtTableTextBlock
  - tsla_ScheduleOfInterestExpenseTableTextBlock
  - us-gaap_DebtInstrumentRedemptionTableTextBlock

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeasesTables

- us-gaap_LeasesAbstract
  - tsla_ScheduleOfOperatingAndFinancingLeasesPresentedInBalanceSheetTableTextBlock
  - us-gaap_LeaseCostTableTextBlock
  - tsla_ScheduleOfSupplementalCashFlowInformationRelatedToLeasesTableTextBlock
  - tsla_ScheduleOfMaturitiesOfOperatingAndFinanceLeaseLiabilitiesTableTextBlock
  - tsla_LessorOperatingLeaseAndSalesTypeLeasePaymentsToBeReceivedMaturityTableTextBlock
  - tsla_NetInvestmentInSalesTypeLeasesTableTextBlock
  - tsla_LeasePassThroughFinancingObligationTableTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureVariableInterestEntityArrangementsTables

- tsla_VariableInterestEntityDisclosureAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSegmentReportingAndInformationAboutGeographicAreasTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTextBlock
  - us-gaap_ScheduleOfRevenueFromExternalCustomersAttributedToForeignCountriesByGeographicAreaTextBlock
  - us-gaap_ScheduleOfEntityWideDisclosureOnGeographicAreasLongLivedAssetsInIndividualForeignCountriesByCountryTextBlock
  - tsla_ScheduleOfInventoryByReportableSegmentTableTextBlock

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureOverviewAdditionalInformationDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NumberOfOperatingSegments
  - us-gaap_NumberOfReportableSegments
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_StockholdersEquityNoteStockSplitConversionRatio1

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_ReceivableTypeDomain
  - tsla_GovernmentRebatesReceivablesMember
- us-gaap_AccountingPoliciesAbstract
  - tsla_SummaryOfSignificantAccountingPoliciesTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_TypeOfArrangementAxis
      - us-gaap_ArrangementsAndNonarrangementTransactionsMember
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - srt_CumulativeEffectPeriodOfAdoptionAxis
      - srt_CumulativeEffectPeriodOfAdoptionDomain
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_IncomeTaxAuthorityNameAxis
    - us-gaap_IncomeTaxAuthorityAxis
    - us-gaap_AccountsNotesLoansAndFinancingReceivableByReceivableTypeAxis
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_RegulatoryLiabilityAxis
    - us-gaap_DeferredRevenueArrangementTypeAxis
    - us-gaap_GuaranteeObligationsByNatureAxis
      - us-gaap_GuaranteeObligationsNatureDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - tsla_SummaryOfSignificantAccountingPoliciesLineItems
      - us-gaap_ContractWithCustomerLiability
      - tsla_ContractWithCustomerLiabilityRevenueRecognizedOutOfPriorPeriodBalance
      - tsla_ContractWithCustomerAssetAndLiabilityRevenueRecognizedInNextRollingTwelveMonths
      - tsla_RevenueDueToChangesInRegulation
      - tsla_ForeignCurrencyTransactionGainLossRealizedAndUnrealized
      - tsla_LessorContingentRentalsBasisSpreadOnVariableRate
      - tsla_MinimumLeasePaymentPercentageOfFairValue
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - tsla_MaximumEligibleAmountOfTransferableInvestmentTaxCredits
      - us-gaap_InvestmentTaxCredit
      - tsla_AgreementTerm
      - tsla_GrantFundingEqualPercentageOnPropertyTaxesPaid
      - tsla_GrantFundingAmountReceived
      - us-gaap_GoodwillImpairmentLoss
      - us-gaap_LessorOperatingLeaseDescription
      - us-gaap_LessorSalesTypeLeaseTermOfContract1
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - tsla_DirectLeaseTerm
      - us-gaap_NotesReceivableNet
      - tsla_SalesReturnReserveFromBuybackOptions
      - tsla_SalesReturnReserveFromShortTermBuyBackOptions
      - us-gaap_ContractWithCustomerLiabilityRevenueRecognized
      - tsla_LoansPayableTerm
      - us-gaap_RevenueRemainingPerformanceObligation
      - tsla_NumberOfCustomersRepresentAccountReceivableThresholdPercentage
      - us-gaap_FinancingReceivableAllowanceForCreditLosses
      - us-gaap_AccountsAndNotesReceivableNet
      - us-gaap_NotesAndLoansReceivableNetCurrent
      - us-gaap_OtherAssetsNoncurrent
      - tsla_AccountsReceivableThresholdPercentage
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseGross
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAccumulatedDepreciation
      - us-gaap_StandardProductWarrantyDescription
      - tsla_DecreaseInNetInterestExpense
      - tsla_IncreaseInBasicNetIncomePerShareOfCommonStockAttributableToCompany
      - tsla_IncreaseInDilutedNetIncomePerShareOfCommonStockAttributableToCompany
      - tsla_IncreaseInAutomotiveSalesRevenue
      - tsla_IncreaseInCostOfAutomotiveSales
      - tsla_NetBenefitInGrossProfit
      - us-gaap_SalesTypeLeaseRevenue
      - us-gaap_CostOfGoodsSoldSalesTypeLease
      - us-gaap_PaymentsToAcquireIntangibleAssets
      - us-gaap_EarningsPerShareDiluted
      - us-gaap_DefinedContributionPlanMaximumAnnualContributionsPerEmployeePercent
      - us-gaap_DefinedContributionPlanEmployerDiscretionaryContributionAmount
      - us-gaap_DefinedContributionPlanEmployerMatchingContributionPercentOfMatch
      - us-gaap_DefinedContributionPlanEmployersMatchingContributionAnnualVestingPercentage
      - tsla_IncreaseInNetIncomeLossAttributableToCommonStockHolders
      - tsla_PercentageOfEmployeesEligibleCompensationVested
      - us-gaap_DefinedContributionPlanMaximumAnnualContributionsPerEmployeeAmount
      - us-gaap_UnrecognizedTaxBenefits
      - tsla_UnrecognizedTaxBenefitsOfDeferredTaxAccountingThatWouldNotImpactAnnualEffectiveRate
      - tsla_BeneficialCorporateIncomeTaxRateForCertainEnterprises
      - tsla_CorporateIncomeTaxRate
      - tsla_BeneficialCorporateIncomeTaxRate
      - us-gaap_IncomeTaxExaminationYearUnderExamination
      - tsla_MinimumTaxRate
      - tsla_ProfitsFromIncomeOfCorporations

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail1

- us-gaap_AccountingPoliciesAbstract
  - tsla_SummaryOfSignificantAccountingPoliciesTable
    - us-gaap_TypeOfArrangementAxis
      - us-gaap_ArrangementsAndNonarrangementTransactionsMember
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - tsla_SummaryOfSignificantAccountingPoliciesLineItems
      - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionPeriod1

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfAccruedWarrantyActivityDetail

- us-gaap_StandardProductWarrantyDisclosureAbstract
  - us-gaap_StandardProductWarrantyAccrual
  - us-gaap_StandardProductWarrantyAccrualPayments
  - us-gaap_ProductWarrantyAccrualPreexistingIncreaseDecrease
  - us-gaap_StandardProductWarrantyAccrualWarrantiesIssued
  - us-gaap_StandardProductWarrantyAccrual

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureFairValueOfFinancialInstrumentsScheduleOfInterestRateSwapsOutstandingDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_InterestRateSwapMember

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureFairValueOfFinancialInstrumentsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_LongtermDebtTypeAxis
  - us-gaap_LongtermDebtTypeDomain
    - tsla_RecourseDebtMember
- us-gaap_DebtInstrumentAxis
  - us-gaap_DebtInstrumentNameDomain
    - tsla_OnePointTwoFivePercentSeniorConvertibleNoteDueTwentyTwentyOneMember
    - tsla_FivePointThreeZeroPercentSeniorNotesDueTwentyTwentyFiveMember
    - tsla_TwoPointThreeSevenFivePercentSeniorConvertibleNoteDueTwentyTwentyTwoMember
    - tsla_TwoPointZeroZeroPercentSeniorConvertibleNoteDueTwentyTwentyFourMember
    - tsla_ZeroCouponConvertibleSeniorNotesDueInTwoThousandTwentyMember
    - tsla_FivePointFiveZeroPercentSeniorConvertibleNoteDueTwentyTwentyTwoMember

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureFairValueOfFinancialInstrumentsScheduleOfEstimatedFairValuesAndCarryingValuesDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_DebtInstrumentAxis
  - us-gaap_DebtInstrumentNameDomain
    - tsla_ConvertibleSeniorNotesMember
    - tsla_FivePointThreeZeroPercentSeniorNotesDueTwentyTwentyFiveMember

### http://www.tesla.com/20221231/taxonomy/role/DisclosureInventoryScheduleOfInventoryDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryRawMaterialsNetOfReserves
  - us-gaap_InventoryWorkInProcessNetOfReserves
  - us-gaap_InventoryFinishedGoodsNetOfReserves
  - us-gaap_InventoryPartsAndComponentsNetOfReserves
  - us-gaap_InventoryNet [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureInventoryAdditionalInformationDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryCurrentTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_InventoryLineItems
      - us-gaap_InventoryWriteDown

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSolarEnergySystemsNetComponentsOfSolarEnergySystemsNetDetails

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
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

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSolarEnergySystemsNetComponentsOfSolarEnergySystemsNetParentheticalDetails

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - tsla_FinanceLeasedAssetsLineItems

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosurePropertyPlantAndEquipmentNetAdditionalInformationDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_InterestCostsCapitalized
      - us-gaap_Depreciation
      - tsla_FinanceLeaseRightOfUseAssetsBeforeAccumulatedDepreciation
      - tsla_FinanceLeaseAccumulatedDepreciation
      - us-gaap_PropertyPlantAndEquipmentGross

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosurePropertyPlantAndEquipmentNetScheduleOfPropertyPlantAndEquipmentNetDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/DisclosureAccruedLiabilitiesAndOtherScheduleOfAccruedLiabilitiesAndOtherCurrentLiabilitiesDetail

- us-gaap_PayablesAndAccrualsAbstract
  - tsla_AccruedPurchases
  - us-gaap_TaxesPayableCurrent
  - us-gaap_EmployeeRelatedLiabilitiesCurrent
  - tsla_AccruedWarrantyReserveCurrentPortion
  - tsla_SalesReturnReserveCurrent
  - us-gaap_OperatingLeaseLiabilityCurrent
  - us-gaap_OtherLiabilitiesCurrent
  - tsla_AccruedAndOtherCurrentLiabilities [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/DisclosureOtherLongtermLiabilitiesScheduleOfOtherLongtermLiabilitiesDetail

- us-gaap_LiabilitiesNoncurrentAbstract
  - us-gaap_OperatingLeaseLiabilityNoncurrent
  - tsla_AccruedWarrantyReserveNoncurrent
  - tsla_SalesReturnReserveNoncurrent
  - us-gaap_DeferredTaxAndOtherLiabilitiesNoncurrent
  - tsla_OtherLiabilitiesMiscellaneousNoncurrent
  - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureDebtSummaryOfDebtAndFinanceLeasesDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtCurrent
      - us-gaap_LongTermDebt
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_DebtInstrumentUnusedBorrowingCapacityAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - tsla_DebtInstrumentContractualMaturityMonthAndYear
      - tsla_DebtInstrumentContractualMaturityMonthAndYearRangeStart
      - tsla_DebtInstrumentContractualMaturityMonthAndYearRangeEnd
      - us-gaap_FinanceLeaseLiabilityCurrent
      - us-gaap_FinanceLeaseLiabilityNoncurrent
      - tsla_LongTermDebtAndFinanceLeasesCurrent
      - tsla_LongTermDebtAndFinanceLeasesNoncurrent

### http://www.tesla.com/20221231/taxonomy/role/DisclosureDebt2022NotesBondHedgesAndWarrantTransactionsAdditionalInformationDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - us-gaap_ClassOfWarrantOrRightNumberOfSecuritiesCalledByEachWarrantOrRight
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - tsla_NumberOfCommonSharesReceived

### http://www.tesla.com/20221231/taxonomy/role/DisclosureDebt2024NotesBondHedgesAndWarrantTransactionsAdditionalInformationDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtConversionByUniqueDescriptionAxis
      - us-gaap_DebtConversionNameDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - tsla_ConvertiblePrincipalAmount
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - us-gaap_DebtInstrumentConvertibleThresholdConsecutiveTradingDays1
      - tsla_DebtInstrumentConvertibleConversionPricePercentage
      - us-gaap_DebtInstrumentRedemptionPricePercentage
      - us-gaap_DebtInstrumentConvertibleThresholdTradingDays
      - tsla_PercentageOfPrincipalAmountOfConvertibleNotesIsEqualToRepurchasePrice
      - tsla_NoteHedgesNumberOfSharesContractedToBuy
      - tsla_PurchasePricePerCommonStock
      - tsla_NoteHedgesTransactionCosts
      - us-gaap_ClassOfWarrantOrRightNumberOfSecuritiesCalledByWarrantsOrRights
      - us-gaap_ClassOfWarrantOrRightExercisePriceOfWarrantsOrRights1
      - us-gaap_ProceedsFromIssuanceOfWarrants
      - tsla_ConversionPricePerShare
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - tsla_NumberOfCommonSharesReceived
      - us-gaap_DebtInstrumentConvertibleIfConvertedValueInExcessOfPrincipal

### http://www.tesla.com/20221231/taxonomy/role/DisclosureDebtCreditAgreementAdditionalInformationDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - srt_StatementScenarioAxis
      - srt_ScenarioUnspecifiedDomain
    - us-gaap_ShortTermDebtTypeAxis
      - us-gaap_ShortTermDebtTypeDomain
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LineOfCreditFacilityAxis
      - us-gaap_LineOfCreditFacilityLenderDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - tsla_TermOfCreditFacility
      - us-gaap_LineOfCreditFacilityCommitmentFeeAmount
      - us-gaap_DebtInstrumentUnusedBorrowingCapacityAmount
      - tsla_LineOfCreditFacilityMaximumCommitmentAmount
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity

### http://www.tesla.com/20221231/taxonomy/role/DisclosureDebtInterestExpensesAdditionalInformationDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentInterestRateStatedPercentage

### http://www.tesla.com/20221231/taxonomy/role/DisclosureDebtScheduleOfFuturePrincipalMaturitiesOfDebtDetails

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

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeasesAdditionalInformationDetail

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_LeaseContractualTermAxis
      - us-gaap_LeaseContractualTermDomain
    - us-gaap_LesseeLeaseDescriptionLineItems
      - us-gaap_LesseeFinanceLeaseTermOfContract1
      - tsla_OperatingLeasesNotYetCommencedValueWithAggregateRentPayments
      - us-gaap_LesseeOperatingLeaseTermOfContract
      - tsla_NumberOfTransactions

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeasesScheduleOfComponentsOfLeaseExpenseAndOtherInformationRelatedToLeasesDetail

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeaseDescriptionAbstract
  - us-gaap_LesseeFinanceLeaseDescriptionAbstract
    - us-gaap_FinanceLeaseRightOfUseAssetAmortization
    - us-gaap_FinanceLeaseInterestExpense
    - tsla_FinanceLeaseExpense [totalLabel]
    - us-gaap_LeaseCost [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeasesScheduleOfOtherInformationRelatedToLeasesDetail

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeaseWeightedAverageRemainingLeaseTerm1
  - us-gaap_FinanceLeaseWeightedAverageRemainingLeaseTerm1
  - us-gaap_OperatingLeaseWeightedAverageDiscountRatePercent
  - us-gaap_FinanceLeaseWeightedAverageDiscountRatePercent

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeasesScheduleOfMaturitiesOfOperatingAndFinanceLeaseLiabilitiesDetail

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
    - us-gaap_FinanceLeaseLiability [totalLabel]
    - us-gaap_FinanceLeaseLiabilityCurrent
    - us-gaap_FinanceLeaseLiabilityNoncurrent

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeasesMaturitiesOfOperatingLeaseAndSalestypeLeaseReceivablesFromCustomersDetail

- us-gaap_LeasesAbstract
  - us-gaap_LessorOperatingLeasePaymentsFiscalYearMaturityAbstract
  - us-gaap_SalesTypeAndDirectFinancingLeasesLeaseReceivableFiscalYearMaturityAbstract

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeasesScheduleOfLeaseReceivablesRelatingToSalestypeLeasesDetail

- us-gaap_LeasesAbstract
  - us-gaap_SalesTypeLeaseNetInvestmentInLeasePastDueTable
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_SalesTypeLeaseNetInvestmentInLeasePastDueLineItems
      - us-gaap_SalesTypeLeaseLeaseReceivable
      - tsla_SalesTypeLeaseUnearnedInterestIncome
      - us-gaap_SalesTypeLeaseNetInvestmentInLeaseAllowanceForCreditLoss
      - us-gaap_SalesTypeLeaseNetInvestmentInLeaseAfterAllowanceForCreditLoss

### http://www.tesla.com/20221231/taxonomy/role/DisclosureLeasesScheduleOfFutureMinimumMasterLeasePaymentsToBeReceivedFromInvestorsDetail

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LessorLeaseDescriptionLineItems
      - us-gaap_LessorOperatingLeasePaymentsToBeReceivedNextTwelveMonths
      - us-gaap_LessorOperatingLeasePaymentsToBeReceivedTwoYears
      - us-gaap_LessorOperatingLeasePaymentsToBeReceivedThreeYears
      - us-gaap_LessorOperatingLeasePaymentsToBeReceivedFourYears
      - us-gaap_LessorOperatingLeasePaymentsToBeReceivedFiveYears
      - us-gaap_LessorOperatingLeasePaymentsToBeReceivedThereafter
      - us-gaap_LessorOperatingLeasePaymentsToBeReceived [totalLabel]

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureCommitmentsAndContingenciesAdditionalInformationDetail

- us-gaap_EnvironmentalRemediationObligationsAbstract
  - tsla_CommitmentsAndContingenciesTable
    - us-gaap_LeaseContractualTermAxis
      - us-gaap_LeaseContractualTermDomain
    - us-gaap_LongTermPurchaseCommitmentByCategoryOfItemPurchasedAxis
      - us-gaap_LongTermPurchaseCommitmentCategoryOfItemPurchasedDomain
    - srt_ConsolidatedEntitiesAxis
      - srt_ConsolidatedEntitiesDomain
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - srt_LitigationCaseAxis
      - srt_LitigationCaseTypeDomain
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - tsla_CommitmentsAndContingenciesLineItems
      - tsla_LeaseArrangementAmountObligatedToSpendOrIncur
      - us-gaap_ContractualObligation
      - tsla_TargetProjectsDeferredPeriod
      - us-gaap_LesseeOperatingLeaseTermOfContract
      - tsla_LesseeOperatingLeaseCapitalExpenditures
      - tsla_AnnualTaxRevenuesToBeGeneratedEndOfFiveYear
      - tsla_LossContingencyNumberOfPurportedStockholderClassActionsFiled
      - us-gaap_LossContingencyNumberOfPlaintiffs
      - tsla_AdditionalSharesClaimValue
      - tsla_NumberOfConsolidatedActions
      - tsla_NumberOfPendingResolutions
      - tsla_NumberOfTeslaStockholders
      - us-gaap_LitigationSettlementAmountAwardedFromOtherParty
      - us-gaap_LossContingencyDamagesSoughtValue
      - us-gaap_LossContingencyDamagesAwardedValue
      - us-gaap_LettersOfCreditOutstandingAmount

### http://www.tesla.com/20221231/taxonomy/role/DisclosureRelatedPartyTransactionsAdditionalInformationDetail

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_ScheduleOfRelatedPartyTransactionsByRelatedPartyTable
    - us-gaap_RelatedPartyTransactionsByRelatedPartyAxis
      - us-gaap_RelatedPartyDomain
    - us-gaap_TypeOfArrangementAxis
      - us-gaap_ArrangementsAndNonarrangementTransactionsMember
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_RelatedPartyTransactionLineItems
      - us-gaap_StockIssuedDuringPeriodSharesNewIssues
      - us-gaap_StockIssuedDuringPeriodValueNewIssues
      - tsla_InterimTerm
      - tsla_LiabilityInsurancePolicyWithAnAggregateCoverageLimit
      - us-gaap_ManagementFeeExpense
      - tsla_PercentageOfFurtherDiscountedOnMarketBasedPremiumForMarketQuote

### http://www.tesla.com/20221231/taxonomy/role/Role_DisclosureSegmentReportingAndInformationAboutGeographicAreasAdditionalInformationDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_NumberOfOperatingSegments
  - us-gaap_NumberOfReportableSegments

### http://www.tesla.com/20221231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfInventoryByReportableSegmentDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_InventoryNet

### http://www.tesla.com/20221231/taxonomy/role/DisclosureRestructuringAndOtherAdditionalInformationDetail

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_ImpairmentOfIntangibleAssetIndefiniteLivedExcludingGoodwillStatementOfIncomeOrComprehensiveIncomeExtensibleEnumeration
  - us-gaap_ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill
  - us-gaap_GainLossOnInvestments
  - us-gaap_BusinessExitCosts1

