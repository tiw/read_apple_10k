# TSLA 2019 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.teslamotors.com/20181231/taxonomy/role/StatementConsolidatedStatementsOfOperations

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

### http://www.teslamotors.com/20181231/taxonomy/role/StatementConsolidatedStatementsOfComprehensiveLoss

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeDerivativesQualifyingAsHedgesNetOfTaxPortionAttributableToParentAbstract
    - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodNetOfTax
    - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIOnDerivativesNetOfTax
    - us-gaap_OtherComprehensiveIncomeLossDerivativesQualifyingAsHedgesNetOfTax [totalLabel]
  - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.teslamotors.com/20181231/taxonomy/role/StatementConsolidatedStatementsOfCashFlows

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - tsla_DepreciationAmortizationAndImpairment
  - us-gaap_ShareBasedCompensation
  - us-gaap_AmortizationOfFinancingCostsAndDiscounts
  - us-gaap_InventoryWriteDown
  - us-gaap_GainLossOnSaleOfPropertyPlantEquipment
  - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
  - tsla_GainsLossOnAcquisition
  - tsla_NoncashInterestIncomeExpenseAndOtherOperatingActivities
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_SummaryOfPositionsForWhichSignificantChangeInUnrecognizedTaxBenefitsIsReasonablyPossibleTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfImpactOfNewRevenueStandardOnConsolidatedFinancialStatementsDetail

- us-gaap_AccountingPoliciesAbstract
  - tsla_SummaryOfSignificantAccountingPoliciesTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_InitialApplicationPeriodCumulativeEffectTransitionAxis
      - us-gaap_InitialApplicationPeriodCumulativeEffectTransitionDomain
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - tsla_SummaryOfSignificantAccountingPoliciesLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAbstract
      - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterestAbstract
      - us-gaap_RevenuesAbstract
      - us-gaap_CostOfRevenueAbstract
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_ProfitLoss
      - us-gaap_NetIncomeLossAttributableToNoncontrollingInterest
      - us-gaap_NetIncomeLoss
      - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
      - us-gaap_ComprehensiveIncomeNetOfTax

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfDeferredRevenueActivityDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ContractWithCustomerLiability
  - tsla_ContractWithCustomerLiabilityAdditions
  - tsla_ContractWithCustomerLiabilityIncreaseDecrease
  - us-gaap_ContractWithCustomerLiabilityRevenueRecognized
  - us-gaap_ContractWithCustomerLiability

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfDisaggregationOfRevenueByMajorSourceDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_DisaggregationOfRevenueTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_DisaggregationOfRevenueLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfPotentiallyDilutiveSharesThatWereExcludedFromComputationOfDilutedNetIncomeLossPerShareOfCommonStockDetail

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTable
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareByAntidilutiveSecuritiesAxis
      - us-gaap_AntidilutiveSecuritiesNameDomain
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareLineItems
      - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureInventoryAdditionalInformationDetail

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfOperationalMilestoneBasedOnRevenueOrAdjustedEBITDADetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_TitleOfIndividualAxis
      - us-gaap_TitleOfIndividualWithRelationshipToEntityDomain
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

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfStockBasedCompensationExpenseDetail

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember
    - tsla_SellingGeneralAndAdministrativeExpenseMember
    - tsla_RestructuringAndOtherMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIncomeTaxesAdditionalInformationDetail

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
      - us-gaap_ForeignEarningsRepatriated
      - us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings
      - tsla_UnrecognizedTaxBenefitsOfDeferredTaxAccountingThatWouldNotImpactAnnualEffectiveRate
      - us-gaap_IncomeTaxExaminationYearUnderExamination

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIncomeTaxesScheduleOfLossBeforeProvisionForIncomeTaxesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
  - tsla_IncomeLossFromContinuingOperationsBeforeIncomeTaxesAttributableToNoncontrollingInterestAndRedeemableNoncontrollingInterest
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIncomeTaxesComponentsOfProvisionForIncomeTaxesDetail

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

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIncomeTaxesScheduleOfDeferredTaxAssetsLiabilitiesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
    - us-gaap_DeferredTaxAssetsOperatingLossCarryforwards
    - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsResearch
    - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsOther
    - us-gaap_DeferredTaxAssetsDeferredIncome
    - us-gaap_DeferredTaxAssetsInventory
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
    - us-gaap_DeferredTaxAssetsInvestments
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccrualsOther
    - us-gaap_DeferredTaxAssetsGross [totalLabel]
    - us-gaap_DeferredTaxAssetsValuationAllowance
    - us-gaap_DeferredTaxAssetsNet [totalLabel]
  - us-gaap_ComponentsOfDeferredTaxLiabilitiesAbstract
    - us-gaap_DeferredTaxLiabilitiesPropertyPlantAndEquipment
    - us-gaap_DeferredTaxLiabilitiesOther
    - us-gaap_DeferredTaxLiabilitiesInvestments
    - us-gaap_DeferredIncomeTaxLiabilities
    - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]
    - us-gaap_DeferredTaxLiabilities

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIncomeTaxesScheduleOfReconciliationOfTaxesAtFederalStatutoryRateToProvisionForIncomeTaxesDetail

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
  - us-gaap_IncomeTaxReconciliationOtherReconcilingItems
  - us-gaap_IncomeTaxReconciliationChangeInDeferredTaxAssetsValuationAllowance
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIncomeTaxesScheduleOfReconciliationOfStatutoryFederalIncomeTaxesToEffectiveTaxesParentheticalDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIncomeTaxesScheduleOfChangesToGrossUnrecognizedTaxBenefitsDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_UnrecognizedTaxBenefits
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
  - tsla_UnrecognizedTaxBenefitsChangeInBalanceRelatedToEffectOfUSTaxLawChange
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromAcquisition
  - us-gaap_UnrecognizedTaxBenefits

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfTotalRevenuesAndGrossMarginByReportableSegmentDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingRevenueReconcilingItemLineItems
      - us-gaap_Revenues
      - us-gaap_GrossProfit

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfRevenuesByGeographicAreaDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
      - us-gaap_Revenues

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfLongLivedAssetsByGeographicAreaDetail

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - srt_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

## 资产负债表结构 (Balance Sheet Structure)

### http://www.teslamotors.com/20181231/taxonomy/role/StatementConsolidatedBalanceSheets

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_StatementLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAbstract
      - us-gaap_CommitmentsAndContingencies
      - us-gaap_RedeemableNoncontrollingInterestEquityCarryingAmount
      - us-gaap_TemporaryEquityCarryingAmountAttributableToParent
      - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterestAbstract
      - us-gaap_LiabilitiesAndStockholdersEquity [totalLabel]

### http://www.teslamotors.com/20181231/taxonomy/role/StatementConsolidatedBalanceSheetsParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_PreferredStockParOrStatedValuePerShare
  - us-gaap_PreferredStockSharesAuthorized
  - us-gaap_PreferredStockSharesIssued
  - us-gaap_PreferredStockSharesOutstanding
  - us-gaap_CommonStockParOrStatedValuePerShare
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_CommonStockSharesIssued
  - us-gaap_CommonStockSharesOutstanding

### http://www.teslamotors.com/20181231/taxonomy/role/StatementConsolidatedStatementsOfRedeemableNoncontrollingInterestAndStockholdersEquity

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

### http://www.teslamotors.com/20181231/taxonomy/role/StatementConsolidatedStatementsOfRedeemableNoncontrollingInterestAndStockholdersEquityParenthetical

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable

### http://www.teslamotors.com/20181231/taxonomy/role/StatementConsolidatedStatementsOfCashFlows

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_ProfitLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
    - us-gaap_ProceedsFromSaleAndMaturityOfMarketableSecurities
    - tsla_PaymentsForSolarEnergySystemsLeasedAndToBeLeased
    - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_ProceedsFromIssuanceOfCommonStock
    - tsla_ProceedsFromConvertibleAndOtherDebt
    - tsla_RepaymentsOfConvertibleAndOtherDebt
    - us-gaap_RepaymentsOfRelatedPartyDebt
    - us-gaap_ProceedsFromRepaymentsOfSecuredDebt
    - us-gaap_ProceedsFromIssuanceOfSharesUnderIncentiveAndShareBasedCompensationPlansIncludingStockOptions
    - us-gaap_ProceedsFromRepaymentsOfLongTermDebtAndCapitalSecurities
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
    - tsla_SharesIssuedInConnectionOfBusinessCombinationAndAssumedVestedAwards
    - us-gaap_NoncashOrPartNoncashAcquisitionValueOfAssetsAcquired1
    - tsla_NonCashEstimatedFairMarketValueOfManufacturingFacility
  - us-gaap_SupplementalCashFlowInformationAbstract
    - us-gaap_InterestPaidNet
    - us-gaap_IncomeTaxesPaid

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIntangibleAssets

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_IntangibleAssetsDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureCommonStock

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIntangibleAssetsTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetsByMajorClassTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_RegulatoryLiabilityAxis
  - us-gaap_RegulatoryLiabilityDomain
    - us-gaap_DeferredLeaseRevenueMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesEstimatedUsefulLivesOfRespectiveAssetsDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_LessorOperatingLeaseTermOfContract

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfEstimatedUsefulLivesOfRelatedAssetsDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureBusinessCombinationsScheduleOfFairValuesOfAssetsAcquiredAndLiabilitiesAssumedDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedAssetsAbstract
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedLiabilitiesAbstract
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedNet [totalLabel]
      - us-gaap_Goodwill
      - tsla_BusinessCombinationAcquisitionOfLessThan100PercentRedeemableAndNonRedeemableNoncontrollingInterestFairValue
      - tsla_BusinessCombinationCappedCallOptionsAssociatedWithConvertibleNotes
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredGoodwillAndLiabilitiesAssumedLessNoncontrollingInterest [totalLabel]
      - us-gaap_BusinessCombinationSeparatelyRecognizedTransactionsNetGainsAndLosses
      - us-gaap_BusinessCombinationConsiderationTransferred1

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureBusinessCombinationsScheduleOfFairValuesOfIdentifiedIntangibleAssetsAndTheirUsefulLivesDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_IndefiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_IndefiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_FiniteLivedIntangibleAssetsFairValueDisclosure
      - us-gaap_IntangibleAssetsGrossExcludingGoodwill
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureBusinessCombinationsScheduleOfFairValueOfConsiderationTransferredAsOfAcquisitionDateParentheticalDetail

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIntangibleAssetsSummaryOfAcquiredIntangibleAssetsDetail

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

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIntangibleAssetsAdditionalInformationDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - tsla_ScheduleOfAcquiredIntangibleAssetsTable
    - us-gaap_IndefiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_IndefiniteLivedIntangibleAssetsMajorClassNameDomain
    - tsla_AcquiredIntangibleAssetsLineItems
      - tsla_AbandonmentLossInRestructuringAndOtherOperatingExpenses
      - us-gaap_ResearchAndDevelopmentInProcess

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureIntangibleAssetsTotalFutureAmortizationExpenseForIntangibleAssetsDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfFairValueHierarchyOfFinancialAssetsCarriedAtFairValueDetail

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
      - us-gaap_FairValueNetAssetLiability

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfInterestRateSwapsOutstandingDetail

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - invest_DerivativeNotionalAmount
    - us-gaap_DerivativeLiabilityFairValueGrossAsset
    - us-gaap_DerivativeFairValueOfDerivativeLiability
    - us-gaap_DerivativeGainOnDerivative
    - us-gaap_DerivativeLossOnDerivative

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsAdditionalInformationDetail

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_LongtermDebtTypeAxis
  - us-gaap_DebtInstrumentAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_DebtInstrumentInterestRateStatedPercentage
    - us-gaap_DebtInstrumentMaturityDate

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfEstimatedFairValuesAndCarryingValuesDetail

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_DebtInstrumentAxis
  - us-gaap_LongtermDebtTypeAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_LongTermDebt
    - us-gaap_LongTermDebtFairValue

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNetComponentsOfSolarEnergySystemsLeasedAndToBeLeasedParentheticalDetail

- us-gaap_CapitalLeasedAssetsLineItems
  - us-gaap_CapitalLeasedAssetsGross
  - tsla_CapitalLeasesLesseeBalanceSheetAssetsByMajorClassAccumulatedDeprecationAndAmortization

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligations2019Notes2021NotesBondHedgesAndWarrantTransactionsAdditionalInformationDetail

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_WarrantMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligations2022NotesBondHedgesAndWarrantTransactionsAdditionalInformationDetail

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_WarrantMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsSolarAssetBackedNotesAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentCollateralAmount
      - tsla_DebtDiscountPercentage
      - tsla_NumberOfWhollyOwnedSubsidiariesReceivedRemainingCashDistributions
      - tsla_LeaseFinancingObligations
      - tsla_LeaseFinancingObligationPayments

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsAutomotiveAssetBackedNotesAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_ProceedsFromIssuanceOfSecuredDebt
      - tsla_NumberOfWhollyOwnedSubsidiariesReceivedRemainingCashDistributions

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsPledgedAssetsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_PledgedAssetsSeparatelyReportedOnStatementOfFinancialPositionAtFairValue

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureCommonStockAdditionalInformationDetail

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureVariableInterestEntityArrangementsCarryingValuesOfAssetsAndLiabilitiesOfSubsidiaryInConsolidatedBalanceSheetsDetail

- tsla_VariableInterestEntityAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTable
    - us-gaap_VariableInterestEntitiesByClassificationOfEntityAxis
      - us-gaap_ClassificationOfVariableInterestEntityDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_VariableInterestEntityLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAbstract

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfLongLivedAssetsByGeographicAreaDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - tsla_InternationalMember

## 现金流量表结构 (Cash Flow Structure)

### http://www.teslamotors.com/20181231/taxonomy/role/StatementConsolidatedStatementsOfCashFlows

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInInventories
  - tsla_IncreaseDecreaseInOperatingLeaseVehicles
  - us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets
  - tsla_IncreaseDecreaseInOtherOperatingAssetsAndNotesReceivables
  - us-gaap_IncreaseDecreaseInAccountsPayableAndAccruedLiabilities
  - us-gaap_IncreaseDecreaseInContractWithCustomerLiability
  - tsla_IncreaseDecreaseInContractWithCustomerLiabilityCustomerDeposits
  - tsla_IncreaseDecreaseInResaleValueGuarantee
  - us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNetTables

- us-gaap_PropertySubjectToOrAvailableForOperatingLeaseByMajorPropertyClassTable
  - us-gaap_MajorPropertyClassAxis
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseLineItems
    - us-gaap_ScheduleOfPropertySubjectToOrAvailableForOperatingLeaseTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationTables

- tsla_LeasePassThroughFinancingObligationAbstract
  - tsla_ScheduleOfFutureMinimumLeasePaymentsToBeReceivedForOperatingLeasesTableTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfCashAndCashEquivalentsAndRestrictedCashDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_RestrictedCashCurrent
  - us-gaap_RestrictedCashAndCashEquivalentsNoncurrent
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations [totalLabel]

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfCashAndCashEquivalentsAndRestrictedCashParentheticalDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_RestrictedCashAndInvestmentsCurrent
  - us-gaap_MarketableSecuritiesCurrent

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNetComponentsOfSolarEnergySystemsLeasedAndToBeLeasedDetail

- us-gaap_PropertySubjectToOrAvailableForOperatingLeaseByMajorPropertyClassTable
  - us-gaap_PropertyPlantAndEquipmentByTypeAxis
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseLineItems
    - tsla_LeasedAssetsBeforeOverhead
    - tsla_LeaseAssetDirectCostsRelatedToAcquisition
    - tsla_LeasedAssetsGross [totalLabel]
    - tsla_PropertySubjectToOrAvailableForOperatingLeaseAccumulatedDepreciationAndAmortization
    - tsla_LeasedAssetsNet [totalLabel]
    - tsla_AssetsToBeLeasedCIP
    - tsla_AssetsToBeLeased
    - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseNet [totalLabel]

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsCashEquityDebtAdditionalInformationDetail

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

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationAdditionalInformationDetail

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

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationScheduleOfFutureMinimumLeasePaymentsToBeReceivedForOperatingLeasesDetail

- us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableAbstract
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseByMajorPropertyClassTable
    - us-gaap_BusinessAcquisitionAxis
    - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseLineItems
      - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableCurrent
      - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInTwoYears
      - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInThreeYears
      - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInFourYears
      - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInFiveYears
      - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableThereafter
      - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivable [totalLabel]

## 股东权益结构 (Equity Structure)

### http://www.teslamotors.com/20181231/taxonomy/role/StatementConsolidatedStatementsOfOperations

- us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding
- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.teslamotors.com/20181231/taxonomy/role/StatementConsolidatedStatementsOfRedeemableNoncontrollingInterestAndStockholdersEquity

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_BusinessAcquisitionAxis
    - us-gaap_BusinessAcquisitionAcquireeDomain
      - tsla_SolarCityAndAssumedAwardsMember
  - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
    - us-gaap_TypeOfAdoptionMember
      - us-gaap_AccountingStandardsUpdate201609Member
      - us-gaap_AccountingStandardsUpdate201409Member
      - us-gaap_AccountingStandardsUpdate201705Member
  - us-gaap_StatementLineItems
    - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest
    - us-gaap_SharesIssued
    - us-gaap_CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalEquityComponentOfConvertibleDebt
    - tsla_AdjustmentsToAdditionalPaidInCapitalConvertibleDebtHedge
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalWarrantIssued
    - tsla_ReclassificationsOfTemporaryEquityToEquityComponentOfDebtInstrument
    - us-gaap_StockIssuedDuringPeriodValueConversionOfConvertibleSecurities
    - us-gaap_StockIssuedDuringPeriodSharesConversionOfConvertibleSecurities
    - tsla_StockIssuedDuringPeriodValueWithheldForEmployeeTaxes
    - tsla_StockIssuedDuringPeriodSharesWithheldForEmployeeTaxes
    - us-gaap_StockIssuedDuringPeriodValueNewIssues
    - us-gaap_StockIssuedDuringPeriodSharesNewIssues
    - us-gaap_StockIssuedDuringPeriodValueAcquisitions
    - us-gaap_StockIssuedDuringPeriodSharesAcquisitions
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
    - tsla_NoncontrollingInterestsIncreaseFromContributionsFromNoncontrollingInterests
    - us-gaap_MinorityInterestDecreaseFromDistributionsToNoncontrollingInterestHolders
    - tsla_AssumptionOfCappedCall
    - tsla_AcquisitionOfNoncontrollingInterestInSubsidiaries
    - us-gaap_NoncontrollingInterestIncreaseFromBusinessCombination
    - tsla_MinorityInterestDecreaseFromDistributionsToNoncontrollingInterestHoldersThroughAcquisition
    - us-gaap_MinorityInterestDecreaseFromRedemptions
    - us-gaap_NetIncomeLossIncludingPortionAttributableToNonredeemableNoncontrollingInterest
    - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent
    - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest
    - us-gaap_SharesIssued

### http://www.teslamotors.com/20181231/taxonomy/role/StatementConsolidatedStatementsOfRedeemableNoncontrollingInterestAndStockholdersEquityParenthetical

- us-gaap_StatementTable
  - us-gaap_DebtInstrumentAxis
    - us-gaap_DebtInstrumentNameDomain
      - tsla_OnePointFiveZeroPercentSeniorConvertibleNoteDueTwentyEighteenMember
  - us-gaap_StatementLineItems
    - us-gaap_DebtInstrumentInterestRateStatedPercentage
    - tsla_CommonStockOfferingPricePerShare
    - tsla_CommonStockPublicOfferingIssuanceCosts

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureEquityIncentivePlans

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ShareholdersEquityAndShareBasedPaymentsTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureEquityIncentivePlansTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationActivityTableTextBlock
  - tsla_ScheduleOfShareBasedPaymentAwardStockOptionsAndEmployeeStockPurchasePlanValuationAssumptionsTableTextBlock
  - tsla_SummaryOfOperationalMilestoneBasedOnRevenueOrAdjustedEBITDATableTextBlock
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsZeroCouponConvertibleSeniorNotesDueIn2020AdditionalInformationDetail

- us-gaap_SubsidiarySaleOfStockAxis
  - us-gaap_SaleOfStockNameOfTransactionDomain
    - us-gaap_PrivatePlacementMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureCommonStockAdditionalInformationDetail

- us-gaap_CompensationRelatedCostsAbstract
  - tsla_OverviewOfCompanyTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_TitleOfIndividualAxis
      - us-gaap_TitleOfIndividualWithRelationshipToEntityDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_InvestmentTypeAxis
      - us-gaap_InvestmentTypeCategorizationMember
    - us-gaap_SubsidiarySaleOfStockAxis
      - us-gaap_SaleOfStockNameOfTransactionDomain
    - tsla_OverviewOfCompanyLineItems
      - us-gaap_StockIssuedDuringPeriodSharesNewIssues
      - us-gaap_StockIssuedDuringPeriodValueNewIssues
      - us-gaap_ConversionOfStockSharesIssued1
      - us-gaap_ConversionOfStockSharesConverted1
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_AdjustmentsToAdditionalPaidInCapitalEquityComponentOfConvertibleDebt
      - us-gaap_RepaymentsOfConvertibleDebt
      - us-gaap_DebtConversionConvertedInstrumentWarrantsOrOptionsIssued1
      - us-gaap_BusinessAcquisitionEquityInterestsIssuedOrIssuableNumberOfSharesIssued
      - us-gaap_DebtConversionConvertedInstrumentAmount1

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureEquityIncentivePlansAdditionalInformationDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PlanNameAxis
      - us-gaap_PlanNameDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_TitleOfIndividualAxis
      - us-gaap_TitleOfIndividualWithRelationshipToEntityDomain
    - us-gaap_VestingAxis
      - us-gaap_VestingDomain
    - us-gaap_FinancialInstrumentPerformanceStatusAxis
      - us-gaap_FinancialInstrumentPerformanceStatusDomain
    - us-gaap_SubsidiarySaleOfStockAxis
      - us-gaap_SaleOfStockNameOfTransactionDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_DeferredCompensationArrangementWithIndividualMaximumContractualTerm1
      - us-gaap_CommonStockCapitalSharesReservedForFutureIssuance
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue [totalLabel]
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodGross
      - tsla_NumberOfTranches
      - tsla_IncreaseToMarketCapitalizationForEachRemainingMilestone
      - tsla_MarketCapitalization
      - tsla_NumberOfOperationalMilestonesFocusedOnRevenueTargets
      - tsla_NumberOfOperationalMilestonesFocusedOnAdjustedEBITDA
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingRights
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
      - tsla_CashCompensationReceivedForServices
      - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromExerciseOfStockOptions
      - tsla_PercentageOfPayrollDeductionsOfEmployeesEligibleCompensation
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardDiscountFromMarketPriceOfferingDate
      - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockPurchasePlans
      - us-gaap_StockIssuedDuringPeriodValueEmployeeStockPurchasePlan
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForIssuance

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfStockOptionAndRSUActivityDetail

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
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisedOrReleasedInPeriodTotalIntrinsicValue [totalLabel]
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

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureEquityIncentivePlansScheduleOfFairValueOfStockOptionAwardAndESPPOnGrantDateDetail

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

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfStockBasedCompensationExpenseDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
      - us-gaap_AllocatedShareBasedCompensationExpense

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureRelatedPartyTransactionsAdditionalInformationDetail

- us-gaap_SubsidiarySaleOfStockAxis
  - us-gaap_SaleOfStockNameOfTransactionDomain
    - us-gaap_PrivatePlacementMember

## 其他结构 (Other Structure)

### http://www.teslamotors.com/20181231/taxonomy/role/DocumentDocumentAndEntityInformation

- tsla_DocumentAndEntityInformationAbstract
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
  - dei_EntitySmallBusiness
  - dei_EntityEmergingGrowthCompany
  - dei_EntityShellCompany
  - dei_EntityCommonStockSharesOutstanding
  - dei_EntityPublicFloat

### http://www.teslamotors.com/20181231/taxonomy/role/StatementConsolidatedStatementsOfOperations

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

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureOverview

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NatureOfOperations

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_SignificantAccountingPoliciesTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureBusinessCombinations

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_BusinessCombinationDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureFairValueOfFinancialInstruments

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueDisclosuresTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureInventory

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNet

- us-gaap_LeasesAbstract
  - tsla_ComponentsOfPropertyLeasedAndToBeLeasedDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosurePropertyPlantAndEquipment

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureNonCancellableOperatingLeasePaymentsReceivable

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeasesOfLessorDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureAccruedLiabilitiesAndOther

- us-gaap_PayablesAndAccrualsAbstract
  - us-gaap_AccountsPayableAndAccruedLiabilitiesDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureOtherLongTermLiabilities

- us-gaap_OtherLiabilitiesAbstract
  - us-gaap_OtherLiabilitiesDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureCustomerDeposits

- tsla_CustomerDepositsDisclosureAbstract
  - tsla_CustomerDepositsTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligations

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureCommitmentsAndContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureVariableInterestEntityArrangements

- tsla_VariableInterestEntityDisclosureAbstract
  - us-gaap_VariableInterestEntityDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLeasePassThroughFinancingObligation

- us-gaap_LeasesAbstract
  - us-gaap_LeasesOfLessorDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureDefinedContributionPlan

- us-gaap_CompensationAndRetirementDisclosureAbstract
  - us-gaap_CompensationAndEmployeeBenefitPlansTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureRelatedPartyTransactions

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_RelatedPartyTransactionsDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreas

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureRestructuringAndOther

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_RestructuringImpairmentAndOtherActivitiesDisclosureTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSubsequentEvents

- us-gaap_SubsequentEventsAbstract
  - us-gaap_SubsequentEventsTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureQuarterlyResultsOfOperations

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_QuarterlyFinancialInformationTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ConsolidationPolicyTextBlock
  - us-gaap_PriorPeriodReclassificationAdjustmentDescription
  - us-gaap_UseOfEstimates
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - us-gaap_CostOfSalesPolicyTextBlock
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
  - us-gaap_MinimumGuaranteesPolicy
  - tsla_SolarRenewableEnergyCreditsPolicyTextBlock
  - tsla_DeferredInvestmentTaxCreditRevenuePolicyTextBlock
  - tsla_TaxIncentivePolicyTextBlock
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_StatementTable
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfProspectiveAdoptionOfNewAccountingPronouncementsTableTextBlock
      - us-gaap_ContractWithCustomerAssetAndLiabilityTableTextBlock
      - us-gaap_DisaggregationOfRevenueTableTextBlock
      - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTextBlock
      - tsla_ScheduleOfCashAndCashEquivalentsAndRestrictedCashTableTextBlock
      - tsla_ScheduleOfDepreciationAndAmortizationComputedUsingStraightLineMethodOverEstimatedUsefulLivesOfAssetsTableTextBlock
      - tsla_ScheduleOfPropertyPlantAndEquipmentTextBlock
      - us-gaap_ScheduleOfProductWarrantyLiabilityTableTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureBusinessCombinationsTables

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_StatementTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfRecognizedIdentifiedAssetsAcquiredAndLiabilitiesAssumedTableTextBlock
      - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsAcquiredAsPartOfBusinessCombinationTextBlock
      - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTextBlock
      - us-gaap_BusinessAcquisitionProFormaInformationTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_ScheduleOfFairValueAssetsAndLiabilitiesMeasuredOnRecurringBasisTableTextBlock
  - us-gaap_ScheduleOfInterestRateDerivativesTableTextBlock
  - us-gaap_ScheduleOfCarryingValuesAndEstimatedFairValuesOfDebtInstrumentsTableTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureInventoryTables

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_ScheduleOfInventoryCurrentTableTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNetTables

- us-gaap_MajorPropertyClassAxis
  - us-gaap_MajorPropertyClassDomain
    - tsla_SolarEnergySystemsLeasedAndToBeLeasedMember
- us-gaap_LeasesAbstract
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseByMajorPropertyClassTable

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosurePropertyPlantAndEquipmentTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureNonCancellableOperatingLeasePaymentsReceivableTables

- us-gaap_LeasesAbstract
  - tsla_ScheduleOfFutureMinimumLeaseReceiptsTableTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureAccruedLiabilitiesAndOtherTables

- us-gaap_PayablesAndAccrualsAbstract
  - tsla_ScheduleOfAccruedLiabilitiesAndOtherCurrentLiabilitiesTableTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureOtherLongTermLiabilitiesTables

- us-gaap_OtherLiabilitiesAbstract
  - us-gaap_OtherNoncurrentLiabilitiesTableTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtTableTextBlock
  - tsla_ScheduleOfInterestExpenseTableTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureCommitmentsAndContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - tsla_ScheduleOfFutureMinimumCommitmentsForCapitalAndOperatingLeasesTableTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureVariableInterestEntityArrangementsTables

- tsla_VariableInterestEntityAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureRelatedPartyTransactionsTables

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_ScheduleOfRelatedPartyTransactionsTableTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTextBlock
  - us-gaap_ScheduleOfRevenueFromExternalCustomersAttributedToForeignCountriesByGeographicAreaTextBlock
  - us-gaap_ScheduleOfEntityWideDisclosureOnGeographicAreasLongLivedAssetsInIndividualForeignCountriesByCountryTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureQuarterlyResultsOfOperationsTables

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_ScheduleOfQuarterlyFinancialInformationTableTextBlock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureOverviewAdditionalInformationDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NumberOfOperatingSegments
  - us-gaap_NumberOfReportableSegments

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_AccountingPoliciesAbstract
  - tsla_SummaryOfSignificantAccountingPoliciesTable
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
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
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_LeaseArrangementTypeAxis
      - us-gaap_LeaseArrangementTypeDomain
    - tsla_SummaryOfSignificantAccountingPoliciesLineItems
      - tsla_IncreaseDecreaseInCollateralizedLeaseBorrowings
      - tsla_RepaymentOfSecuredNotesPayable
      - us-gaap_RepaymentsOfNotesPayable
      - tsla_ContractWithCustomerLiabilityRevenueRecognizedOutOfPriorPeriodBalance
      - tsla_ContractWithCustomerAssetAndLiabilityRevenueRecognizedInNextRollingTwelveMonths
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - tsla_ContractWithCustomerLiabilityRevenueAndCredits
      - tsla_DirectLeaseTerm
      - us-gaap_ContractWithCustomerLiability
      - us-gaap_OperatingLeasesIncomeStatementLeaseRevenue
      - tsla_MaximumRepurchasePriceOfVehiclesUnderResaleValueArrangement
      - tsla_ResaleValueGuaranteesCurrentPortionSalesToLeasingPartners
      - tsla_ResaleValueGuarantee
      - tsla_ResaleValueGuaranteesCurrentPortionSalesToCustomers
      - tsla_ResaleValueGuaranteeLeaseRevenueRecognized
      - us-gaap_ContractWithCustomerLiabilityRevenueRecognized
      - us-gaap_RevenueRemainingPerformanceObligation
      - us-gaap_CostOfGoodsAndServicesSold
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentMaturityDate
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
      - tsla_NumberOfVehiclesProductiveLifeForTooling
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - us-gaap_ForeignCurrencyTransactionGainLossRealized
      - us-gaap_StandardProductWarrantyDescription
      - us-gaap_ProductWarrantyExpense
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_AccruedLiabilitiesCurrent
      - tsla_IncentiveBeginningPeriod
      - tsla_IncentiveEndingPeriod
      - tsla_MaximumEligibleAmountOfTransferableInvestmentTaxCredits
      - tsla_ExpectedCapitalInvestment
      - us-gaap_InvestmentTaxCredit
      - us-gaap_CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption
      - us-gaap_Assets
      - us-gaap_Liabilities

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail1

- us-gaap_AccountingPoliciesAbstract
  - tsla_SummaryOfSignificantAccountingPoliciesTable
    - us-gaap_TypeOfArrangementAxis
      - us-gaap_ArrangementsAndNonarrangementTransactionsMember
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - tsla_SummaryOfSignificantAccountingPoliciesLineItems
      - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionPeriod1

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfAccruedWarrantyActivityDetail

- us-gaap_StandardProductWarrantyDisclosureAbstract
  - us-gaap_StandardProductWarrantyAccrual
  - us-gaap_ProductWarrantyAccrualAdditionsFromBusinessAcquisition
  - us-gaap_StandardProductWarrantyAccrualPayments
  - us-gaap_ProductWarrantyAccrualPreexistingIncreaseDecrease
  - tsla_StandardProductWarrantyAccrualAdditionsFromAdoptionOfNewRevenueStandard
  - us-gaap_StandardProductWarrantyAccrualWarrantiesIssued
  - us-gaap_StandardProductWarrantyAccrual

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureBusinessCombinationsAdditionalInformationDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionEffectiveDateOfAcquisition1
      - us-gaap_PaymentsToAcquireBusinessesGross
      - us-gaap_BusinessCombinationLiabilitiesArisingFromContingenciesAmountRecognized
      - tsla_BusinessCombinationIncentiveCompensationArrangementEmployeeServicePeriod
      - tsla_BusinessCombinationShareBasedCompensationExpense
      - tsla_BusinessCombinationCommonStockConversionBasis
      - tsla_BusinessCombinationStockConversionRatio
      - tsla_BusinessCombinationStockBasedCompensationExpenseRecognizedOfAssumedUnvestedShareBasedAwards
      - us-gaap_BusinessAcquisitionCostOfAcquiredEntityTransactionCosts
      - us-gaap_BusinessCombinationSeparatelyRecognizedTransactionsNetGainsAndLosses
      - tsla_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedChangeInNotesReceivableNetOfCurrentPortion
      - tsla_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedChangeInAccruedLiabilities
      - us-gaap_BusinessCombinationProFormaInformationRevenueOfAcquireeSinceAcquisitionDateActual
      - tsla_BusinessCombinationProFormaInformationOperatingIncomeLossOfAcquireeSinceAcquisitionDateActual

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureBusinessCombinationsScheduleOfFairValueOfConsiderationTransferredAsOfAcquisitionDateDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationStepAcquisitionEquityInterestInAcquireeFairValue1
      - tsla_BusinessCombinationFairValueOfReplacementStockOptionsAndRestrictedStockUnitsForAcquireVestedAwards
      - us-gaap_BusinessCombinationConsiderationTransferredIncludingEquityInterestInAcquireeHeldPriorToCombination1 [totalLabel]

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureBusinessCombinationsScheduleOfFairValueOfConsiderationTransferredAsOfAcquisitionDateParentheticalDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionEquityInterestsIssuedOrIssuableNumberOfSharesIssued
      - us-gaap_BusinessAcquisitionSharePrice

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureBusinessCombinationsScheduleOfUnauditedProFormaInformationDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionsProFormaRevenue
      - us-gaap_BusinessAcquisitionsProFormaNetIncomeLoss
      - tsla_BusinessAcquisitionProFormaEarningsPerShareBasicAndDiluted
      - tsla_BusinessAcquisitionProFormaWeightedAverageNumberOfShareOutstandingBasicAndDiluted

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfInterestRateSwapsOutstandingDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_InterestRateSwapMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_LongtermDebtTypeAxis
  - us-gaap_LongtermDebtTypeDomain
    - tsla_RecourseDebtMember
- us-gaap_DebtInstrumentAxis
  - us-gaap_DebtInstrumentNameDomain
    - tsla_FivePointThreeZeroPercentSeniorNotesDueTwentyTwentyFiveMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfEstimatedFairValuesAndCarryingValuesDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_LongtermDebtTypeAxis
  - us-gaap_LongtermDebtTypeDomain
    - us-gaap_SeniorNotesMember
- us-gaap_DebtInstrumentAxis
  - us-gaap_DebtInstrumentNameDomain
    - tsla_ConvertibleSeniorNotesMember
    - tsla_ParticipationInterestMember
    - tsla_SolarAssetBackedNotesMember
    - tsla_SolarLoanBackedNotesMember
    - tsla_AutomotiveAssetBackedNotesMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureInventoryScheduleOfInventoryDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryRawMaterialsNetOfReserves
  - us-gaap_InventoryWorkInProcessNetOfReserves
  - us-gaap_InventoryFinishedGoodsNetOfReserves
  - us-gaap_InventoryPartsAndComponentsNetOfReserves
  - us-gaap_InventoryNet [totalLabel]

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureInventoryAdditionalInformationDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryCurrentTable
    - us-gaap_ErrorCorrectionsAndPriorPeriodAdjustmentsRestatementByRestatementPeriodAndAmountAxis
      - us-gaap_AdjustmentsForErrorCorrectionDomain
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_InventoryLineItems
      - us-gaap_PropertyPlantAndEquipmentNet
      - us-gaap_InventoryWriteDown

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNetComponentsOfSolarEnergySystemsLeasedAndToBeLeasedDetail

- us-gaap_LeasesAbstract
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseByMajorPropertyClassTable
- us-gaap_PropertyPlantAndEquipmentByTypeAxis
  - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - tsla_SolarEnergySystemsMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNetComponentsOfSolarEnergySystemsLeasedAndToBeLeasedParentheticalDetail

- us-gaap_LeasesAbstract
  - us-gaap_ScheduleOfCapitalLeasedAsssetsTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_CapitalLeasedAssetsLineItems

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosurePropertyPlantAndEquipmentScheduleOfPropertyPlantAndEquipmentNetDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosurePropertyPlantAndEquipmentAdditionalInformationDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_InterestCostsCapitalized
      - us-gaap_PropertyPlantAndEquipmentNet
      - us-gaap_AccruedLiabilitiesCurrent
      - us-gaap_OtherLiabilitiesNoncurrent
      - us-gaap_Depreciation
      - us-gaap_CapitalLeasedAssetsGross
      - us-gaap_CapitalLeasesLesseeBalanceSheetAssetsByMajorClassAccumulatedDeprecation
      - us-gaap_ConstructionInProgressGross

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureNonCancellableOperatingLeasePaymentsReceivableScheduleOfFutureMinimumLeasePaymentsNonCancellableOperatingLeasesDetail

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableCurrent
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInTwoYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInThreeYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInFourYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInFiveYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableThereafter
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivable [totalLabel]

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureAccruedLiabilitiesAndOtherScheduleOfAccruedLiabilitiesAndOtherCurrentLiabilitiesDetail

- us-gaap_PayablesAndAccrualsAbstract
  - tsla_AccruedPurchases
  - us-gaap_EmployeeRelatedLiabilitiesCurrent
  - us-gaap_TaxesPayableCurrent
  - tsla_FinancingObligationCurrent
  - us-gaap_ProductWarrantyAccrualClassifiedCurrent
  - tsla_SalesReturnReserveCurrent
  - us-gaap_DepositLiabilitiesAccruedInterest
  - tsla_BuildToSuitLeaseLiabilityAccruedCurrent
  - us-gaap_OtherLiabilitiesCurrent
  - tsla_AccruedAndOtherCurrentLiabilities [totalLabel]

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureOtherLongTermLiabilitiesScheduleOfOtherLongTermLiabilitiesDetail

- us-gaap_OtherLiabilitiesNoncurrentAbstract
  - tsla_AccruedWarrantyReserveNoncurrent
  - tsla_BuildToSuitLeaseLiabilityNoncurrent
  - us-gaap_DeferredRentCreditNoncurrent
  - tsla_FinancingObligationNoncurrent
  - tsla_LiabilityForReceiptsFromInvestor
  - tsla_SalesReturnReserveNoncurrent
  - tsla_OtherLiabilitiesMiscellaneousNoncurrent
  - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureCustomerDepositsAdditionalInformationDetail

- tsla_CustomerDepositsDisclosureAbstract
  - tsla_CustomerDepositsTable
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - tsla_CustomerDepositsLineItems
      - tsla_CustomerDepositsLiabilitiesCurrent
      - tsla_IncreaseDecreaseInContractWithCustomerLiabilityCustomerDeposits

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsSummaryOfDebtDetail

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
      - us-gaap_DebtInstrumentMaturityDate
      - us-gaap_DebtInstrumentMaturityDateRangeStart1
      - us-gaap_DebtInstrumentMaturityDateRangeEnd1

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligations2018NotesBondHedgesAndWarrantTransactionsAdditionalInformationDetail

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
      - us-gaap_DebtInstrumentMaturityDate
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
      - us-gaap_RepaymentsOfConvertibleDebt
      - us-gaap_GainsLossesOnExtinguishmentOfDebt

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligations2019Notes2021NotesBondHedgesAndWarrantTransactionsAdditionalInformationDetail

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
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentMaturityDate
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

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligations2022NotesBondHedgesAndWarrantTransactionsAdditionalInformationDetail

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
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentMaturityDate
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

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligations2025NotesAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentMaturityDate
      - us-gaap_ProceedsFromDebtNetOfIssuanceCosts

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsCreditAgreementAdditionalInformationDetail

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

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligations275ConvertibleSeniorNotesDueIn2018AdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentMaturityDate
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - us-gaap_DebtInstrumentDescription
      - us-gaap_RepaymentsOfDebt

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligations1625ConvertibleSeniorNotesDueIn2019AdditionalInformationDetail

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
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentMaturityDate
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - tsla_CommonStockReceiveUponExerciseOfOption
      - us-gaap_DerivativeDescriptionOfObjective
      - us-gaap_DerivativeCapPrice
      - us-gaap_DerivativePriceRiskOptionStrikePrice
      - us-gaap_DerivativeMaturityDates

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsZeroCouponConvertibleSeniorNotesDueIn2020AdditionalInformationDetail

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

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsRelatedPartyPromissoryNotesAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_RelatedPartyTransactionsByRelatedPartyAxis
      - us-gaap_RelatedPartyDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtConversionOriginalDebtAmount1
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentMaturityDate
      - us-gaap_RepaymentsOfRelatedPartyDebt

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsWarehouseAgreementsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentMaturityDate
      - us-gaap_RepaymentsOfSecuredDebt

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsCanadaCreditFacilityAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - tsla_NumberOfSubsidiariesEnteredIntoFacilityAgreement

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsTermLoanAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_TypeOfArrangementAxis
      - us-gaap_ArrangementsAndNonarrangementTransactionsMember
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - us-gaap_LineOfCreditFacilityUnusedCapacityCommitmentFeePercentage
      - us-gaap_DebtInstrumentMaturityDate

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsRevolvingAggregationCreditFacilityAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - us-gaap_LineOfCreditFacilityInterestRateDescription
      - us-gaap_RepaymentsOfLongTermDebt

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsSolarLoanBackedNotesAdditionalInformationDetail

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
      - tsla_DebtDiscountPercentage
      - tsla_NumberOfWhollyOwnedSubsidiariesReceivedRemainingCashDistributions

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsSolarRenewableEnergyCreditAndOtherLoansAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - tsla_NumberOfWhollyOwnedSubsidiariesReceivedRemainingCashDistributions

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLongTermDebtObligationsScheduleOfInterestExpenseDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_InterestExpenseDebtExcludingAmortization
  - us-gaap_AmortizationOfFinancingCosts
  - us-gaap_AmortizationOfDebtDiscountPremium
  - us-gaap_InterestExpenseDebt [totalLabel]

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureCommitmentsAndContingenciesAdditionalInformationDetail

- us-gaap_EnvironmentalRemediationObligationsAbstract
  - tsla_CommitmentsAndContingenciesTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_LeaseArrangementTypeAxis
      - us-gaap_LeaseArrangementTypeDomain
    - us-gaap_LongTermPurchaseCommitmentByCategoryOfItemPurchasedAxis
      - us-gaap_LongTermPurchaseCommitmentCategoryOfItemPurchasedDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_EnvironmentalRemediationContingencyAxis
      - us-gaap_EnvironmentalRemediationContingencyDomain
    - srt_LitigationCaseAxis
      - srt_LitigationCaseTypeDomain
    - tsla_CommitmentsAndContingenciesLineItems
      - us-gaap_OperatingLeasesRentExpenseNet
      - tsla_TermsOfAgreementsToLeaseEquipmentUnderCapitalLeases
      - us-gaap_CostOfGoodsAndServicesSold
      - us-gaap_TypeOfCostGoodOrServiceExtensibleList
      - us-gaap_LongTermPurchaseCommitmentAmount
      - tsla_AdditionalSpecifiedScopeCosts
      - us-gaap_LessorOperatingLeaseTermOfContract
      - tsla_OperatingLeaseOptionToRenewAmountPerYear
      - tsla_LeaseArrangementAmountRequiredToSpendOrIncur
      - us-gaap_ContractualObligation
      - us-gaap_CapitalExpendituresIncurredButNotYetPaid
      - tsla_SiteContingencyCostToBePaidByCompany
      - tsla_SiteContingencyCostToBePaidInExcessByCompany
      - tsla_AgreementTermForGovernmentallyRequiredRemediationActivitiesForContamination
      - tsla_LowerThresholdThirdPartyLiability
      - tsla_UpperThresholdThirdPartyLiability
      - us-gaap_LossContingencyNumberOfPlaintiffs
      - tsla_CivilPenaltiesAmountPayable
      - tsla_NumberOfIndependentDirectors
      - tsla_IndependentDirectorServingPeriod
      - tsla_NumberOfAdditionalIndependentDirectors
      - us-gaap_LettersOfCreditOutstandingAmount

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureCommitmentsAndContingenciesScheduleOfFutureMinimumCommitmentsForLeasesDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
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

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureVariableInterestEntityArrangementsAdditionalInformationDetail

- tsla_VariableInterestEntityAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTable
    - us-gaap_VariableInterestEntitiesByClassificationOfEntityAxis
      - us-gaap_ClassificationOfVariableInterestEntityDomain
    - us-gaap_VariableInterestEntityLineItems
      - us-gaap_PledgedAssetsSeparatelyReportedSecuritiesPledgedAsCollateralAtFairValue

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationAdditionalInformationDetail

- us-gaap_PropertyPlantAndEquipmentByTypeAxis
  - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - tsla_SolarEnergySystemsUnderLeasePassThroughArrangementsMember
- srt_RangeAxis
  - srt_RangeMember
    - srt_MinimumMember
    - srt_MaximumMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationScheduleOfFutureMinimumLeasePaymentsToBeReceivedForOperatingLeasesDetail

- us-gaap_BusinessAcquisitionAxis
  - us-gaap_BusinessAcquisitionAcquireeDomain
    - tsla_SolarCityMember

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureDefinedContributionPlanAdditionalInformationDetail

- us-gaap_CompensationAndRetirementDisclosureAbstract
  - us-gaap_DefinedContributionPlanMaximumAnnualContributionsPerEmployeePercent
  - us-gaap_DefinedContributionPlanEmployerDiscretionaryContributionAmount
  - us-gaap_DefinedContributionPlanSponsorLocationExtensibleList
  - us-gaap_DefinedContributionPlanTaxStatusExtensibleList

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureRelatedPartyTransactionsSummaryOfRelatedPartyTransactionsDetail

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_DueToRelatedPartiesCurrentAndNoncurrent
  - tsla_ConvertibleSeniorNotesIssueToRelatedParties
  - us-gaap_NotesPayableRelatedPartiesCurrentAndNoncurrent

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureRelatedPartyTransactionsAdditionalInformationDetail

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_ScheduleOfRelatedPartyTransactionsByRelatedPartyTable
    - us-gaap_TitleOfIndividualAxis
      - us-gaap_TitleOfIndividualWithRelationshipToEntityDomain
    - us-gaap_SubsidiarySaleOfStockAxis
    - us-gaap_RelatedPartyTransactionLineItems
      - tsla_ConvertibleSeniorNoteUnpaidPrincipalAmountDueToRelatedParties
      - us-gaap_StockIssuedDuringPeriodSharesNewIssues
      - us-gaap_StockIssuedDuringPeriodValueNewIssues

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasAdditionalInformationDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_NumberOfOperatingSegments
  - us-gaap_NumberOfReportableSegments

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureRestructuringAndOtherAdditionalInformationDetail

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_BusinessExitCosts1
  - us-gaap_PaymentsForRestructuring
  - us-gaap_RestructuringCosts
  - us-gaap_ImpairmentOfIntangibleAssetsExcludingGoodwill
  - us-gaap_LitigationSettlementExpense

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureSubsequentEventsAdditionalInformationDetail

- us-gaap_SubsequentEventsAbstract
  - us-gaap_SubsequentEventTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_SubsequentEventLineItems
      - us-gaap_BusinessAcquisitionEquityInterestIssuedOrIssuableDescription
      - tsla_ConversionOfCommonStockPerShare
      - tsla_CashPaidInLieuOfFractionalSharesOfCommonStock

### http://www.teslamotors.com/20181231/taxonomy/role/DisclosureQuarterlyResultsOfOperationsScheduleOfSelectedQuarterlyResultsOfOperationsDetail

- us-gaap_QuarterlyFinancialDataAbstract
  - us-gaap_Revenues
  - us-gaap_GrossProfit
  - us-gaap_NetIncomeLoss
  - us-gaap_IncomeLossFromContinuingOperationsPerBasicShare
  - us-gaap_IncomeLossFromContinuingOperationsPerDilutedShare

