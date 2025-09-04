# TSLA 2024 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.tesla.com/role/ConsolidatedStatementsofOperations

- us-gaap_OperatingExpensesAbstract
  - us-gaap_ResearchAndDevelopmentExpense
  - us-gaap_SellingGeneralAndAdministrativeExpense
  - tsla_RestructuringAndOtherExpenses
  - us-gaap_OperatingExpenses [totalLabel]
- us-gaap_CostOfRevenueAbstract
  - us-gaap_CostOfRevenue
- tsla_AutomotiveRevenuesMember
  - tsla_AutomotiveSalesMember
  - tsla_AutomotiveRegulatoryCreditsMember
  - tsla_AutomotiveLeasingMember
- us-gaap_RevenuesAbstract
  - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable

### http://www.tesla.com/role/ConsolidatedStatementsofComprehensiveIncome

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_ProfitLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
    - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
    - us-gaap_UnrealizedGainLossOnInvestments
    - tsla_AdjustmentForNetLossRealizedAndIncludedInNetIncome
  - us-gaap_ComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterest [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTaxAttributableToNoncontrollingInterest
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.tesla.com/role/ConsolidatedStatementsofCashFlows

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - tsla_DepreciationAmortizationAndImpairment
  - us-gaap_ShareBasedCompensation
  - us-gaap_InventoryWriteDown
  - us-gaap_ForeignCurrencyTransactionGainLossUnrealized
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - tsla_NoncashInterestIncomeExpenseAndOtherOperatingActivities
  - tsla_GainLossOnDigitalAssets
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.tesla.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.tesla.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_SummaryOfPositionsForWhichSignificantChangeInUnrecognizedTaxBenefitsIsReasonablyPossibleTextBlock

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesScheduleofDisaggregationofRevenuebyMajorSourceDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_DisaggregationOfRevenueTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_DisaggregationOfRevenueLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesScheduleofDeferredRevenueActivityDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_MovementInDeferredRevenueRollForward
    - us-gaap_ContractWithCustomerLiability
    - tsla_ContractWithCustomerLiabilityAdditions
    - tsla_ContractWithCustomerLiabilityIncreaseDecrease
    - us-gaap_ContractWithCustomerLiabilityRevenueRecognized
    - us-gaap_ContractWithCustomerLiability

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesScheduleofReconciliationofNetIncomeUsedinComputingBasicandDilutedNetIncomePerShareofCommonStockandBasictoDilutedWeightedAverageSharesUsedinComputingNetIncomePerShareofCommonStockDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NetIncomeLoss
  - tsla_BuyOutOfNoncontrollingInterest
  - us-gaap_NetIncomeLossAvailableToCommonStockholdersBasic [totalLabel]
  - us-gaap_DilutiveSecuritiesEffectOnBasicEarningsPerShareOther
  - us-gaap_NetIncomeLossAvailableToCommonStockholdersDiluted [totalLabel]

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesScheduleofReconciliationofBasictoDilutedWeightedAverageSharesUsedinComputingNetIncomePerShareofCommonStockAttributabletoCommonStockholdersDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_IncrementalCommonSharesAttributableToShareBasedPaymentArrangements
  - us-gaap_IncrementalCommonSharesAttributableToConversionOfDebtSecurities
  - us-gaap_IncrementalCommonSharesAttributableToCallOptionsAndWarrants
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding [totalLabel]

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesScheduleofPotentiallyDilutiveSharesthatwereExcludedfromComputationofDilutedNetIncomeperShareofCommonStockDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTable
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareByAntidilutiveSecuritiesAxis
      - us-gaap_AntidilutiveSecuritiesNameDomain
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareLineItems
      - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount

### http://www.tesla.com/role/InventoryAdditionalInformationDetail

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember

### http://www.tesla.com/role/EquityIncentivePlansSummaryofOperationalMilestoneBasedonRevenueorAdjustedEBITDADetail

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

### http://www.tesla.com/role/EquityIncentivePlansSummaryofStockBasedCompensationExpenseDetail

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember
    - tsla_SellingGeneralAndAdministrativeExpenseMember

### http://www.tesla.com/role/IncomeTaxesScheduleofIncomebeforeProvisionForIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
  - tsla_IncomeLossFromContinuingOperationsBeforeIncomeTaxesAttributableToNoncontrollingInterestAndRedeemableNoncontrollingInterest
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]

### http://www.tesla.com/role/IncomeTaxesAdditionalInformationDetails

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
    - us-gaap_TaxCreditCarryforwardAxis
      - us-gaap_TaxCreditCarryforwardNameDomain
    - us-gaap_OperatingLossCarryforwardsLineItems
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_ValuationAllowanceDeferredTaxAssetChangeInAmount
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_DeferredTaxAssetsNet
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsResearch
      - us-gaap_TaxCreditCarryforwardAmount
      - tsla_ResearchTaxCreditCarryForwardExpirationDates
      - tsla_BeneficialCorporateIncomeTaxRateForCertainEnterprises
      - tsla_CorporateIncomeTaxRate
      - tsla_BeneficialCorporateIncomeTaxRate
      - us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings
      - us-gaap_DeferredTaxLiabilityNotRecognizedAmountOfUnrecognizedDeferredTaxLiabilityUndistributedEarningsOfForeignSubsidiaries
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestExpense
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate

### http://www.tesla.com/role/IncomeTaxesComponentsofProvisionforIncomeTaxesDetails

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

### http://www.tesla.com/role/IncomeTaxesScheduleofReconciliationofTaxesatFederalStatutoryRatetoProvisionforIncomeTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
  - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
  - us-gaap_IncomeTaxReconciliationNondeductibleExpenseShareBasedCompensationCost
  - us-gaap_EffectiveIncomeTaxRateReconciliationShareBasedCompensationExcessTaxBenefitAmount
  - tsla_EffectiveIncomeTaxRateReconciliationNontaxableManufacturingCreditAmount
  - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
  - us-gaap_IncomeTaxReconciliationTaxCredits
  - us-gaap_EffectiveIncomeTaxRateReconciliationGiltiAmount
  - tsla_Effectiveincometaxratereconciliationunrecognizedtaxbenefits
  - us-gaap_IncomeTaxReconciliationChangeInDeferredTaxAssetsValuationAllowance
  - us-gaap_IncomeTaxReconciliationNondeductibleExpenseOther
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.tesla.com/role/IncomeTaxesScheduleofDeferredTaxAssetsLiabilitiesDetails

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
    - us-gaap_DeferredTaxLiabilitiesOther
    - us-gaap_DeferredIncomeTaxLiabilities
    - tsla_DeferredTaxAssetLiabilitiesNet [totalLabel]

### http://www.tesla.com/role/IncomeTaxesScheduleofChangestoGrossUnrecognizedTaxBenefitsDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ReconciliationOfUnrecognizedTaxBenefitsExcludingAmountsPertainingToExaminedTaxReturnsRollForward
    - us-gaap_UnrecognizedTaxBenefits
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsReductionsResultingFromLapseOfApplicableStatuteOfLimitations
    - us-gaap_UnrecognizedTaxBenefits

### http://www.tesla.com/role/SegmentReportingandInformationaboutGeographicAreasScheduleofTotalRevenuesandGrossProfitbyReportableSegmentDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingRevenueReconcilingItemLineItems
      - us-gaap_Revenues
      - us-gaap_GrossProfit

### http://www.tesla.com/role/SegmentReportingandInformationaboutGeographicAreasScheduleofRevenuesbyGeographicAreaDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
      - us-gaap_Revenues

### http://www.tesla.com/role/SegmentReportingandInformationaboutGeographicAreasScheduleofLongLivedAssetsbyGeographicAreaDetail

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - srt_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

## 资产负债表结构 (Balance Sheet Structure)

### http://www.tesla.com/role/ConsolidatedBalanceSheets

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

### http://www.tesla.com/role/ConsolidatedBalanceSheetsParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_PreferredStockParOrStatedValuePerShare
  - us-gaap_PreferredStockSharesAuthorized
  - us-gaap_PreferredStockSharesIssued
  - us-gaap_PreferredStockSharesOutstanding
  - us-gaap_CommonStockParOrStatedValuePerShare
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_CommonStockSharesIssued
  - us-gaap_CommonStockSharesOutstanding

### http://www.tesla.com/role/ConsolidatedStatementsofRedeemableNoncontrollingInterestandEquity

- us-gaap_IncreaseDecreaseInTemporaryEquityRollForward
  - us-gaap_TemporaryEquityCarryingAmountIncludingPortionAttributableToNoncontrollingInterests
  - tsla_TemporaryEquityContributionsToNoncontrollingInterests
  - tsla_TemporaryEquityDistributionsToNoncontrollingInterests
  - tsla_TemporaryEquityBuyOutOfNoncontrollingInterests
  - us-gaap_TemporaryEquityNetIncome
  - us-gaap_TemporaryEquityCarryingAmountIncludingPortionAttributableToNoncontrollingInterests
- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_SharesIssued
  - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest
  - us-gaap_StockIssuedDuringPeriodSharesConversionOfConvertibleSecurities
  - us-gaap_StockIssuedDuringPeriodValueConversionOfConvertibleSecurities
  - tsla_WarrantsSettlementShares
  - tsla_WarrantsSettlement
  - tsla_StockIssuedDuringPeriodSharesEquityIncentiveAwards
  - tsla_StockIssuedDuringPeriodValueEquityIncentiveAwards
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
  - tsla_NoncontrollingInterestsIncreaseFromContributionsFromNoncontrollingInterests
  - us-gaap_MinorityInterestDecreaseFromDistributionsToNoncontrollingInterestHolders
  - us-gaap_MinorityInterestDecreaseFromRedemptions
  - tsla_NetIncomeLossIncludingPortionAttributableToRedeemableNonControllingInterestAndNonControllingInterestInSubsidiaries
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent
  - us-gaap_SharesIssued
  - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest
  - us-gaap_AccountingStandardsUpdateExtensibleList
- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_ParentMember
    - us-gaap_NoncontrollingInterestMember

### http://www.tesla.com/role/ConsolidatedStatementsofCashFlows

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
    - us-gaap_ProceedsFromSaleOfShortTermInvestments
    - tsla_GovernmentGrantReceipt
    - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_ProceedsFromIssuanceOfDebt
    - us-gaap_RepaymentsOfDebt
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

### http://www.tesla.com/role/DigitalAssetsNet

- us-gaap_IntangibleAssetsNetExcludingGoodwillAbstract
  - tsla_DigitalAssetsNetTextBlock

### http://www.tesla.com/role/GoodwillandIntangibleAssets

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_IntangibleAssetsDisclosureTextBlock

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_RetainedEarningsMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesEstimatedUsefulLivesofRespectiveAssetsDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_LessorOperatingLeaseTermOfContract

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesScheduleofEstimatedUsefulLivesofRelatedAssetsDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife

### http://www.tesla.com/role/DigitalAssetsNetDetail

- us-gaap_IntangibleAssetsNetExcludingGoodwillAbstract
  - us-gaap_ImpairmentOfIntangibleAssetsExcludingGoodwill
  - us-gaap_GainLossOnDispositionOfIntangibleAssets
  - tsla_CumulativeImpairmentOfIntangibleAssetsExcludingGoodwill

### http://www.tesla.com/role/GoodwillandIntangibleAssetsDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillPeriodIncreaseDecrease
  - us-gaap_Goodwill
  - us-gaap_GoodwillImpairedAccumulatedImpairmentLoss
  - us-gaap_IntangibleAssetsNetExcludingGoodwill

### http://www.tesla.com/role/FairValueofFinancialInstrumentsScheduleofAssetsandLiabilitiesMeasuredatFairValueonRecurringBasisDetail

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FinancialInstrumentAxis
      - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
    - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
      - us-gaap_AvailableForSaleSecuritiesDebtSecurities
      - us-gaap_AssetsFairValueDisclosure

### http://www.tesla.com/role/FairValueofFinancialInstrumentsAdditionalInformationDetail

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_DebtInstrumentAxis
  - us-gaap_LongtermDebtTypeAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_DebtInstrumentInterestRateStatedPercentage
    - tsla_DebtInstrumentContractualMaturityYear

### http://www.tesla.com/role/FairValueofFinancialInstrumentsScheduleofEstimatedFairValuesandCarryingValuesDetail

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_DebtInstrumentAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_LongTermDebt
    - us-gaap_LongTermDebtFairValue
    - tsla_DigitalAssetsNetNonCurrent
    - tsla_FairMarketValueOfIntangibleAssets

### http://www.tesla.com/role/LeasesScheduleofOperatingandFinancingLeasesPresentedinBalanceSheetsDetail

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_LesseeLeaseDescriptionLineItems
      - us-gaap_LesseeOperatingLeaseDescriptionAbstract
      - us-gaap_LesseeFinanceLeaseDescriptionAbstract

### http://www.tesla.com/role/EquityIncentivePlansSummaryofStockOptionandRSUActivityDetail

- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
  - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExercisedOrReleasedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsAdditionalDisclosuresAbstract
  - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedAndExpectedToVest
  - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsToVestedAndExpectedToVestWeightedAverageGrantDateFairValue
- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
  - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExercisedOrReleasedWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue

### http://www.tesla.com/role/VariableInterestEntityArrangementsCarryingValuesofAssetsandLiabilitiesofSubsidiaryinConsolidatedBalanceSheetsDetail

- tsla_VariableInterestEntityDisclosureAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTable
    - srt_ConsolidatedEntitiesAxis
      - srt_ConsolidatedEntitiesDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_VariableInterestEntityLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAbstract

### http://www.tesla.com/role/SegmentReportingandInformationaboutGeographicAreasScheduleofLongLivedAssetsbyGeographicAreaDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - country_DE
    - country_CN
    - tsla_OtherInternationalMember

## 现金流量表结构 (Cash Flow Structure)

### http://www.tesla.com/role/ConsolidatedStatementsofCashFlows

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInInventories
  - tsla_IncreaseDecreaseInOperatingLeaseVehicles
  - us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets
  - us-gaap_IncreaseDecreaseInAccountsPayableAndAccruedLiabilities
  - us-gaap_IncreaseDecreaseInContractWithCustomerLiability

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_FinancingReceivablePortfolioSegmentAxis
  - us-gaap_FinancingReceivablePortfolioSegmentDomain
    - tsla_MyPowerMember
- us-gaap_AccountsNotesLoansAndFinancingReceivableByReceivableTypeAxis
  - us-gaap_ReceivableTypeDomain

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesScheduleofCashandCashEquivalentsandRestrictedCashDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_RestrictedCashCurrent
  - us-gaap_RestrictedCashNoncurrent
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations [totalLabel]

### http://www.tesla.com/role/FairValueofFinancialInstrumentsScheduleofCashCashEquivalentsandMarketableSecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_MarketableSecuritiesTable
    - us-gaap_FinancialInstrumentAxis
      - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_MarketableSecuritiesLineItems
      - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis [totalLabel]
      - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
      - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
      - us-gaap_AvailableForSaleSecuritiesDebtSecurities

### http://www.tesla.com/role/LeasesScheduleofComponentsofLeaseExpenseandOtherInformationRelatedtoLeasesDetail

- us-gaap_LesseeOperatingLeaseDescriptionAbstract
  - us-gaap_OperatingLeaseCost

### http://www.tesla.com/role/LeasesSupplementalCashFlowInformationRelatedtoLeasesDetail

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeasePayments
  - us-gaap_FinanceLeaseInterestPaymentOnLiability
  - us-gaap_RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability
  - us-gaap_RightOfUseAssetObtainedInExchangeForOperatingLeaseLiability

### http://www.tesla.com/role/LeasesScheduleofMaturitiesofOperatingandFinanceLeaseLiabilitiesDetail

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

### http://www.tesla.com/role/LeasesMaturitiesofOperatingLeaseandSalesTypeLeaseReceivablesfromCustomersDetail

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

### http://www.tesla.com/role/ConsolidatedStatementsofOperations

- us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding
- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.tesla.com/role/ConsolidatedStatementsofRedeemableNoncontrollingInterestandEquity

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - srt_RestatementAxis
    - srt_RestatementDomain
      - srt_RevisionOfPriorPeriodAccountingStandardsUpdateAdjustmentMember
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInTemporaryEquityRollForward
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
- us-gaap_ParentMember
  - us-gaap_CommonStockMember
  - us-gaap_AdditionalPaidInCapitalMember
  - us-gaap_AccumulatedOtherComprehensiveIncomeMember
  - us-gaap_RetainedEarningsMember

### http://www.tesla.com/role/EquityIncentivePlans

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ShareholdersEquityAndShareBasedPaymentsTextBlock

### http://www.tesla.com/role/EquityIncentivePlansTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationActivityTableTextBlock
  - tsla_ScheduleOfShareBasedPaymentAwardStockOptionsAndEmployeeStockPurchasePlanValuationAssumptionsTableTextBlock
  - tsla_SummaryOfOperationalMilestoneBasedOnRevenueOrAdjustedEBITDATableTextBlock
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
  - tsla_StockOptionsAndRestrictedStockUnitsMember
  - us-gaap_EmployeeStockMember

### http://www.tesla.com/role/EquityIncentivePlansAdditionalInformationDetail

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
    - us-gaap_SubsidiarySaleOfStockAxis
      - us-gaap_SaleOfStockNameOfTransactionDomain
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
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardOfferingPeriod
      - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockPurchasePlans
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardValueOfSharesAvailableForIssuance
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodGross
      - tsla_NumberOfTranches
      - tsla_MarketCapitalization
      - tsla_IncreaseToMarketCapitalizationForEachRemainingMilestone
      - tsla_NumberOfOperationalMilestonesFocusedOnRevenueTargets
      - tsla_NumberOfOperationalMilestonesFocusedOnAdjustedEBITDA
      - tsla_ShareBasedCompensationArrangementPaymentOfExercisePricePerShare
      - tsla_ShareBasedCompensationArrangementHoldingPeriodOfSharesPostExercise
      - us-gaap_ShareBasedCompensation
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - tsla_ShareBasedPaymentArrangementNonvestedAwardProbableOfAchievementCostNotYetRecognizedAmount
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense
      - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsCapitalizedAmount

### http://www.tesla.com/role/EquityIncentivePlansSummaryofStockOptionandRSUActivityDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_PlanNameAxis
      - us-gaap_PlanNameDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePriceRollforward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsAdditionalDisclosuresAbstract
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsAdditionalDisclosuresAbstract

### http://www.tesla.com/role/EquityIncentivePlansScheduleofFairValueofStockOptionAwardandESPPonGrantDateDetail

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

### http://www.tesla.com/role/EquityIncentivePlansSummaryofStockBasedCompensationExpenseDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
      - us-gaap_AllocatedShareBasedCompensationExpense

### http://xbrl.sec.gov/ecd/role/AwardTimingDisclosure

- us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
  - us-gaap_EmployeeStockOptionMember
  - us-gaap_StockAppreciationRightsSARSMember
  - tsla_StockOptionsAndRestrictedStockUnitsMember
  - us-gaap_EmployeeStockMember
  - us-gaap_RestrictedStockUnitsRSUMember
  - tsla_TwoThousandAndTwelvePerformanceAwardMember
  - tsla_TwoThousandAndEighteenPerformanceAwardMember
  - tsla_PerformanceBasedRestrictedStockUnitsAndStockOptionsMember

## 其他结构 (Other Structure)

### http://www.tesla.com/role/Cover

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
  - dei_EntityCentralIndexKey
  - dei_DocumentFiscalYearFocus
  - dei_DocumentFiscalPeriodFocus

### http://www.tesla.com/role/AuditInformation

- tsla_AuditorInformationAbstract
  - dei_AuditorName
  - dei_AuditorFirmId
  - dei_AuditorLocation

### http://www.tesla.com/role/ConsolidatedStatementsofOperations

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

### http://www.tesla.com/role/Overview

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NatureOfOperations

### http://www.tesla.com/role/SummaryofSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_SignificantAccountingPoliciesTextBlock

### http://www.tesla.com/role/FairValueofFinancialInstruments

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueDisclosuresTextBlock

### http://www.tesla.com/role/Inventory

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryDisclosureTextBlock

### http://www.tesla.com/role/SolarEnergySystemsNet

- us-gaap_LeasesAbstract
  - tsla_SolarEnergySystemsNetDisclosureTextBlock

### http://www.tesla.com/role/PropertyPlantandEquipmentNet

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.tesla.com/role/AccruedLiabilitiesandOther

- us-gaap_PayablesAndAccrualsAbstract
  - us-gaap_AccountsPayableAndAccruedLiabilitiesDisclosureTextBlock

### http://www.tesla.com/role/OtherLongTermLiabilities

- us-gaap_OtherLiabilitiesAbstract
  - us-gaap_OtherLiabilitiesDisclosureTextBlock

### http://www.tesla.com/role/Debt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.tesla.com/role/Leases

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeasesTextBlock
  - us-gaap_LesseeFinanceLeasesTextBlock
  - us-gaap_LessorSalesTypeLeasesTextBlock
  - us-gaap_OperatingLeasesOfLessorDisclosureTextBlock

### http://www.tesla.com/role/CommitmentsandContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.tesla.com/role/VariableInterestEntityArrangements

- tsla_VariableInterestEntityDisclosureAbstract
  - us-gaap_VariableInterestEntityDisclosureTextBlock

### http://www.tesla.com/role/RelatedPartyTransactions

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_RelatedPartyTransactionsDisclosureTextBlock

### http://www.tesla.com/role/SegmentReportingandInformationaboutGeographicAreas

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.tesla.com/role/RestructuringandOther

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_RestructuringImpairmentAndOtherActivitiesDisclosureTextBlock

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ConsolidationPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_PriorPeriodReclassificationAdjustmentDescription
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - us-gaap_CostOfSalesPolicyTextBlock
  - us-gaap_ResearchAndDevelopmentExpensePolicy
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_ComprehensiveIncomePolicyPolicyTextBlock
  - us-gaap_ShareBasedCompensationOptionAndIncentivePlansPolicy
  - tsla_NoncontrollingInterestsPolicyTextBlock
  - us-gaap_EarningsPerSharePolicyTextBlock
  - us-gaap_BusinessCombinationsPolicy
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_CashAndCashEquivalentsRestrictedCashAndCashEquivalentsPolicy
  - us-gaap_InvestmentPolicyTextBlock
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
  - tsla_DefinedContributionPlanPolicyTextBlock
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_DisaggregationOfRevenueTableTextBlock
  - us-gaap_ContractWithCustomerAssetAndLiabilityTableTextBlock
  - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock
  - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTextBlock
  - tsla_ScheduleOfCashAndCashEquivalentsAndRestrictedCashTableTextBlock
  - tsla_ScheduleOfDepreciationAndAmortizationComputedUsingStraightLineMethodOverEstimatedUsefulLivesOfAssetsTableTextBlock
  - tsla_ScheduleOfPropertyPlantAndEquipmentTableTextBlock
  - us-gaap_ScheduleOfProductWarrantyLiabilityTableTextBlock

### http://www.tesla.com/role/FairValueofFinancialInstrumentsTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_ScheduleOfFairValueAssetsAndLiabilitiesMeasuredOnRecurringBasisTableTextBlock
  - us-gaap_UnrealizedGainLossOnInvestmentsTableTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock
  - us-gaap_ScheduleOfCarryingValuesAndEstimatedFairValuesOfDebtInstrumentsTableTextBlock

### http://www.tesla.com/role/InventoryTables

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_ScheduleOfInventoryCurrentTableTextBlock

### http://www.tesla.com/role/SolarEnergySystemsNetTables

- us-gaap_LeasesAbstract
  - us-gaap_ScheduleOfPropertySubjectToOrAvailableForOperatingLeaseTextBlock

### http://www.tesla.com/role/PropertyPlantandEquipmentNetTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.tesla.com/role/AccruedLiabilitiesandOtherTables

- us-gaap_PayablesAndAccrualsAbstract
  - tsla_ScheduleOfAccruedLiabilitiesAndOtherCurrentLiabilitiesTableTextBlock

### http://www.tesla.com/role/OtherLongTermLiabilitiesTables

- us-gaap_OtherLiabilitiesAbstract
  - us-gaap_OtherNoncurrentLiabilitiesTableTextBlock

### http://www.tesla.com/role/DebtTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtTableTextBlock
  - us-gaap_DebtInstrumentRedemptionTableTextBlock

### http://www.tesla.com/role/LeasesTables

- us-gaap_LeasesAbstract
  - tsla_ScheduleOfOperatingAndFinancingLeasesPresentedInBalanceSheetTableTextBlock
  - us-gaap_LeaseCostTableTextBlock
  - us-gaap_LesseeOperatingLeaseLiabilityMaturityTableTextBlock
  - us-gaap_FinanceLeaseLiabilityMaturityTableTextBlock
  - us-gaap_LessorOperatingLeasePaymentsToBeReceivedMaturityTableTextBlock
  - us-gaap_SalesTypeAndDirectFinancingLeasesLeaseReceivableMaturityTableTextBlock
  - tsla_NetInvestmentInSalesTypeLeasesTableTextBlock
  - tsla_LeasePassThroughFinancingObligationTableTextBlock

### http://www.tesla.com/role/VariableInterestEntityArrangementsTables

- tsla_VariableInterestEntityDisclosureAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTextBlock

### http://www.tesla.com/role/SegmentReportingandInformationaboutGeographicAreasTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTextBlock
  - us-gaap_ScheduleOfRevenueFromExternalCustomersAttributedToForeignCountriesByGeographicAreaTextBlock
  - us-gaap_ScheduleOfEntityWideDisclosureOnGeographicAreasLongLivedAssetsInIndividualForeignCountriesByCountryTextBlock
  - us-gaap_ReconciliationOfAssetsFromSegmentToConsolidatedTextBlock

### http://www.tesla.com/role/OverviewDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NumberOfOperatingSegments
  - us-gaap_NumberOfReportableSegments

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_ReceivableTypeDomain
  - tsla_GovernmentRebatesReceivablesMember
- us-gaap_AccountingPoliciesAbstract
  - tsla_SummaryOfSignificantAccountingPoliciesTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_AccountsNotesLoansAndFinancingReceivableByReceivableTypeAxis
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_GuaranteeObligationsByNatureAxis
      - us-gaap_GuaranteeObligationsNatureDomain
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - srt_CumulativeEffectPeriodOfAdoptionAxis
      - srt_CumulativeEffectPeriodOfAdoptionDomain
    - us-gaap_FinancingReceivablePortfolioSegmentAxis
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_StatementEquityComponentsAxis
    - tsla_SummaryOfSignificantAccountingPoliciesLineItems
      - us-gaap_ContractWithCustomerLiabilityRevenueRecognized
      - us-gaap_RevenueRemainingPerformanceObligation
      - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionPeriod1
      - us-gaap_NotesAndLoansReceivableNetCurrent
      - us-gaap_NotesAndLoansReceivableNetNoncurrent
      - us-gaap_ContractWithCustomerLiability
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - tsla_RevenueDueToChangesInRegulation
      - tsla_DirectLeaseTerm
      - us-gaap_OperatingLeaseLeaseIncome
      - us-gaap_LeaseDepositLiability
      - us-gaap_LessorSalesTypeLeaseTermOfContract1
      - us-gaap_CostOfGoodsSoldSalesTypeLease
      - us-gaap_OtherAssetsNoncurrent
      - tsla_LoansPayableTerm
      - us-gaap_AccountsAndNotesReceivableNet
      - us-gaap_FinancingReceivableAllowanceForCreditLosses
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseGross
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAccumulatedDepreciation
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - us-gaap_GoodwillImpairmentLoss
      - tsla_ForeignCurrencyTransactionGainLossRealizedAndUnrealized
      - tsla_StandardProductWarrantyTerm
      - tsla_GrantFundingAmountReceived
      - us-gaap_InvestmentTaxCredit
      - tsla_AgreementTerm
      - tsla_GrantFundingEqualPercentageOnPropertyTaxesPaid
      - us-gaap_DefinedContributionPlanEmployersMatchingContributionAnnualVestingPercentage
      - us-gaap_DefinedContributionPlanEmployerMatchingContributionPercentOfMatch
      - tsla_PercentageOfEmployeesEligibleCompensationVested
      - us-gaap_DefinedContributionPlanMaximumAnnualContributionsPerEmployeeAmount
      - us-gaap_DefinedContributionPlanEmployerDiscretionaryContributionAmount
      - us-gaap_SalesTypeLeaseRevenue
      - us-gaap_OperatingLeaseIncomeComprehensiveIncomeExtensibleList
      - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest
      - us-gaap_TemporaryEquityCarryingAmountAttributableToParent
      - us-gaap_DebtAndCapitalLeaseObligations
      - us-gaap_PropertyPlantAndEquipmentNet

### http://www.tesla.com/role/SummaryofSignificantAccountingPoliciesScheduleofAccruedWarrantyActivityDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_MovementInStandardProductWarrantyAccrualRollForward
    - us-gaap_StandardProductWarrantyAccrual
    - us-gaap_StandardProductWarrantyAccrualPayments
    - us-gaap_ProductWarrantyAccrualPreexistingIncreaseDecrease
    - us-gaap_StandardProductWarrantyAccrualWarrantiesIssued
    - us-gaap_StandardProductWarrantyAccrual

### http://www.tesla.com/role/FairValueofFinancialInstrumentsSummaryofFairValueofMarketableSecuritiesbyContractualMaturitiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesNextRollingTwelveMonthsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearTwoThroughFiveFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearSixThroughTenFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesSingleMaturityDate [totalLabel]

### http://www.tesla.com/role/FairValueofFinancialInstrumentsAdditionalInformationDetail

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_LongtermDebtTypeAxis
  - us-gaap_LongtermDebtTypeDomain
    - tsla_RecourseDebtMember
- us-gaap_DebtInstrumentAxis
  - us-gaap_DebtInstrumentNameDomain
    - tsla_TwoPointZeroZeroPercentSeniorConvertibleNoteDueTwentyTwentyFourMember

### http://www.tesla.com/role/FairValueofFinancialInstrumentsScheduleofEstimatedFairValuesandCarryingValuesDetail

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_DebtInstrumentAxis
  - us-gaap_DebtInstrumentNameDomain
    - tsla_ConvertibleSeniorNotesMember
    - tsla_DigitalAssetsMember

### http://www.tesla.com/role/InventoryScheduleofInventoryDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryRawMaterialsNetOfReserves
  - us-gaap_InventoryWorkInProcessNetOfReserves
  - us-gaap_InventoryFinishedGoodsNetOfReserves
  - us-gaap_InventoryPartsAndComponentsNetOfReserves
  - us-gaap_InventoryNet [totalLabel]

### http://www.tesla.com/role/InventoryAdditionalInformationDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryCurrentTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_InventoryLineItems
      - us-gaap_InventoryWriteDown

### http://www.tesla.com/role/SolarEnergySystemsNetComponentsofSolarEnergySystemsNetDetails

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
      - us-gaap_DepreciationAndAmortization
      - tsla_GrossSolarEnergySystemUnderLeasePassThroughFundArrangement
      - tsla_GrossSolarEnergySystemUnderLeasePassThroughFundArrangementAccumulatedDepreciation

### http://www.tesla.com/role/PropertyPlantandEquipmentNetScheduleofPropertyPlantandEquipmentNetDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]

### http://www.tesla.com/role/PropertyPlantandEquipmentNetAdditionalInformationDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_Depreciation
      - us-gaap_PropertyPlantAndEquipmentGross

### http://www.tesla.com/role/AccruedLiabilitiesandOtherScheduleofAccruedLiabilitiesandOtherCurrentLiabilitiesDetail

- us-gaap_PayablesAndAccrualsAbstract
  - tsla_AccruedPurchases
  - tsla_AccruedWarrantyReserveCurrentPortion
  - us-gaap_EmployeeRelatedLiabilitiesCurrent
  - us-gaap_TaxesPayableCurrent
  - tsla_CustomerDepositsLiabilitiesCurrent
  - us-gaap_OperatingLeaseLiabilityCurrent
  - tsla_SalesReturnReserveCurrent
  - us-gaap_OtherLiabilitiesCurrent
  - tsla_AccruedAndOtherCurrentLiabilities [totalLabel]

### http://www.tesla.com/role/OtherLongTermLiabilitiesScheduleofOtherLongtermLiabilitiesDetail

- us-gaap_OtherLiabilitiesAbstract
  - us-gaap_OperatingLeaseLiabilityNoncurrent
  - tsla_AccruedWarrantyReserveNoncurrent
  - tsla_OtherLiabilitiesMiscellaneousNoncurrent
  - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.tesla.com/role/DebtSummaryofDebtandFinanceLeasesDetail

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

### http://www.tesla.com/role/DebtAdditionalInformationDetails

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
    - us-gaap_FairValueByMeasurementBasisAxis
      - us-gaap_FairValueDisclosureItemAmountsDomain
    - us-gaap_PledgedStatusAxis
      - us-gaap_PledgedStatusDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_LineOfCreditFacilityAxis
      - us-gaap_LineOfCreditFacilityLenderDomain
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - us-gaap_ShortTermDebtTypeAxis
      - us-gaap_ShortTermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
      - us-gaap_DebtInstrumentConvertibleConversionRatio1
      - us-gaap_DebtInstrumentConvertibleThresholdConsecutiveTradingDays1
      - tsla_DebtInstrumentConvertibleConversionPricePercentage
      - us-gaap_DebtInstrumentConvertibleIfConvertedValueInExcessOfPrincipal
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - tsla_TermOfCreditFacility
      - tsla_DebtInstrumentNumberOfExtensionOptions
      - tsla_DebtInstrumentExtensionTerm
      - tsla_LineOfCreditFacilityMaximumCommitmentAmount
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_AssetsFairValueDisclosure

### http://www.tesla.com/role/DebtPrincipalofMaturitiesofDebtDetails

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

### http://www.tesla.com/role/LeasesAdditionalInformationDetail

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_LeaseContractualTermAxis
      - us-gaap_LeaseContractualTermDomain
    - us-gaap_LesseeLeaseDescriptionLineItems
      - tsla_LesseeRenewalTerm
      - tsla_OperatingLeasesNotYetCommencedValueWithAggregateRentPayments
      - us-gaap_LesseeOperatingLeaseLeaseNotYetCommencedTermOfContract1
      - tsla_NumberOfTransactions
      - us-gaap_LesseeFinanceLeaseTermOfContract1

### http://www.tesla.com/role/LeasesScheduleofComponentsofLeaseExpenseandOtherInformationRelatedtoLeasesDetail

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeaseDescriptionAbstract
  - us-gaap_LesseeFinanceLeaseDescriptionAbstract
    - us-gaap_FinanceLeaseRightOfUseAssetAmortization
    - us-gaap_FinanceLeaseInterestExpense
    - tsla_FinanceLeaseExpense [totalLabel]
    - us-gaap_LeaseCost [totalLabel]
  - tsla_WeightedAverageRemainingLeaseTermAbstract
    - us-gaap_OperatingLeaseWeightedAverageRemainingLeaseTerm1
    - us-gaap_FinanceLeaseWeightedAverageRemainingLeaseTerm1
  - tsla_WeightedAverageDiscountRateAbstract
    - us-gaap_OperatingLeaseWeightedAverageDiscountRatePercent
    - us-gaap_FinanceLeaseWeightedAverageDiscountRatePercent

### http://www.tesla.com/role/LeasesScheduleofMaturitiesofOperatingandFinanceLeaseLiabilitiesDetail

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

### http://www.tesla.com/role/LeasesMaturitiesofOperatingLeaseandSalesTypeLeaseReceivablesfromCustomersDetail

- us-gaap_LeasesAbstract
  - us-gaap_LessorOperatingLeasePaymentsFiscalYearMaturityAbstract
  - us-gaap_SalesTypeAndDirectFinancingLeasesLeaseReceivableFiscalYearMaturityAbstract

### http://www.tesla.com/role/LeasesScheduleofLeaseReceivablesRelatingtoSalesTypeLeasesDetail

- us-gaap_LeasesAbstract
  - us-gaap_SalesTypeAndDirectFinancingLeasesLeaseReceivablePaymentsToBeReceived
  - us-gaap_SalesTypeAndDirectFinancingLeasesLeaseReceivableUndiscountedExcessAmount
  - us-gaap_SalesTypeLeaseNetInvestmentInLeaseAllowanceForCreditLoss
  - us-gaap_SalesTypeLeaseNetInvestmentInLeaseAfterAllowanceForCreditLossCurrent
  - us-gaap_SalesTypeLeaseNetInvestmentInLeaseAfterAllowanceForCreditLossNoncurrent
  - us-gaap_SalesTypeLeaseNetInvestmentInLeaseAfterAllowanceForCreditLoss [totalLabel]

### http://www.tesla.com/role/LeasesScheduleoffutureminimummasterleasepaymentstobereceivedfrominvestorsDetail

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

### http://www.tesla.com/role/CommitmentsandContingenciesDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - tsla_CommitmentsAndContingenciesTable
    - srt_ConsolidatedEntitiesAxis
      - srt_ConsolidatedEntitiesDomain
    - us-gaap_LongTermPurchaseCommitmentByCategoryOfItemPurchasedAxis
      - us-gaap_LongTermPurchaseCommitmentCategoryOfItemPurchasedDomain
    - us-gaap_LeaseContractualTermAxis
      - us-gaap_LeaseContractualTermDomain
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - tsla_CommitmentsAndContingenciesLineItems
      - tsla_LeaseArrangementAmountObligatedToSpendOrIncur
      - us-gaap_LesseeOperatingLeaseTermOfContract
      - us-gaap_ContractualObligation
      - tsla_LesseeOperatingLeaseCapitalExpenditures
      - tsla_AnnualTaxRevenuesToBeGeneratedEndOfFiveYear
      - tsla_LossContingencyNumberOfPurportedStockholderClassActionsFiled
      - us-gaap_LossContingencyNumberOfPlaintiffs
      - tsla_NumberOfConsolidatedActions
      - tsla_NumberOfPendingResolutions
      - tsla_AdditionalSharesClaimValue
      - us-gaap_LossContingencyDamagesSoughtValue
      - us-gaap_LossContingencyDamagesAwardedValue
      - tsla_NumberOfTeslaStockholders
      - us-gaap_LettersOfCreditOutstandingAmount

### http://www.tesla.com/role/SegmentReportingandInformationaboutGeographicAreasAdditionalInformationDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_NumberOfOperatingSegments
  - us-gaap_NumberOfReportableSegments

### http://www.tesla.com/role/SegmentReportingandInformationaboutGeographicAreasScheduleofinventorybyreportablesegmentDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_InventoryNet

### http://www.tesla.com/role/RestructuringandOtherDetail

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill
  - us-gaap_ImpairmentOfIntangibleAssetIndefiniteLivedExcludingGoodwillStatementOfIncomeOrComprehensiveIncomeExtensibleEnumeration
  - us-gaap_GainLossOnInvestments
  - us-gaap_BusinessExitCosts1

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
  - ecd_TrdArrDuration
  - ecd_TrdArrSecuritiesAggAvailAmt

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

### http://xbrl.sec.gov/ecd/role/InsiderTradingPoliciesProc

- ecd_InsiderTradingPoliciesProcLineItems
  - ecd_InsiderTrdPoliciesProcAdoptedFlag
  - ecd_InsiderTrdPoliciesProcNotAdoptedTextBlock

