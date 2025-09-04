# NVDA 2022 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.nvidia.com/role/CONSOLIDATEDSTATEMENTSOFINCOME

- us-gaap_IncomeStatementAbstract
  - us-gaap_Revenues
  - us-gaap_CostOfRevenue
  - us-gaap_GrossProfit [totalLabel]
  - us-gaap_OperatingExpensesAbstract
    - us-gaap_ResearchAndDevelopmentExpense
    - us-gaap_SellingGeneralAndAdministrativeExpense
    - us-gaap_OperatingExpenses [totalLabel]
  - us-gaap_OperatingIncomeLoss [totalLabel]
  - us-gaap_InvestmentIncomeInterest
  - us-gaap_InterestExpense
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_NonoperatingIncomeExpense [totalLabel]
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]
  - us-gaap_IncomeTaxExpenseBenefit
  - us-gaap_NetIncomeLoss [totalLabel]
  - us-gaap_EarningsPerShareAbstract
    - us-gaap_EarningsPerShareBasic
    - us-gaap_EarningsPerShareDiluted
  - us-gaap_WeightedAverageNumberOfSharesOutstandingDilutedDisclosureItemsAbstract
    - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
    - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding

### http://www.nvidia.com/role/CONSOLIDATEDSTATEMENTSOFCOMPREHENSIVEINCOME

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeAvailableforsaleSecuritiesAdjustmentNetOfTaxPortionAttributableToParentAbstract
    - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodNetOfTax
    - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesNetOfTax
    - us-gaap_OtherComprehensiveIncomeAvailableforsaleSecuritiesAdjustmentNetOfTaxPortionAttributableToParent [totalLabel]
  - us-gaap_OtherComprehensiveIncomeLossDerivativeExcludedComponentIncreaseDecreaseAfterAdjustmentsAndTaxParentAbstract
    - us-gaap_OtherComprehensiveIncomeLossCashFlowHedgeGainLossBeforeReclassificationAfterTax
    - us-gaap_OtherComprehensiveIncomeLossCashFlowHedgeGainLossReclassificationAfterTax
    - us-gaap_OtherComprehensiveIncomeLossCashFlowHedgeGainLossAfterReclassificationAndTax [totalLabel]
  - us-gaap_OtherComprehensiveIncomeLossNetOfTax [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.nvidia.com/role/CONSOLIDATEDSTATEMENTSOFCASHFLOWS

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_ShareBasedCompensation
  - us-gaap_DepreciationDepletionAndAmortization
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_GainLossOnInvestments
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.nvidia.com/role/StockBasedCompensationScheduleofStockBasedCompensationExpenseDetails

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember
    - us-gaap_SellingGeneralAndAdministrativeExpensesMember

### http://www.nvidia.com/role/StockBasedCompensationSummaryofEquityAwardsDetails

- nvda_SummaryofunearnedSBCexpenseAbstract
  - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
  - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]

### http://www.nvidia.com/role/NetIncomePerShare

- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareTextBlock

### http://www.nvidia.com/role/NetIncomePerShareTables

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfWeightedAverageNumberOfSharesTableTextBlock

### http://www.nvidia.com/role/NetIncomePerShareDetails

- us-gaap_EarningsPerShareAbstract
  - nvda_NumeratorAbstract
    - us-gaap_NetIncomeLoss
  - nvda_DenominatorAbstract
    - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
    - us-gaap_WeightedAverageNumberDilutedSharesOutstandingAdjustment
    - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding [totalLabel]
  - nvda_NetIncomeLossPerShareAbstract
    - us-gaap_EarningsPerShareBasic
    - us-gaap_EarningsPerShareDiluted
  - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount

### http://www.nvidia.com/role/AmortizableIntangibleAssetsDetails

- us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive

### http://www.nvidia.com/role/BalanceSheetComponentsDeferredRevenueDetails

- us-gaap_TextBlockAbstract
  - us-gaap_MovementInDeferredRevenueRollForward
    - us-gaap_ContractWithCustomerLiability
    - nvda_ContractWithCustomerLiabilityAdditions
    - us-gaap_ContractWithCustomerLiabilityIncreaseDecreaseForContractAcquiredInBusinessCombination
    - nvda_ContractWithCustomerLiabilityRevenueRecognizedOpeningBalanceAndCurrentPeriodAdditions
    - us-gaap_ContractWithCustomerLiability

### http://www.nvidia.com/role/BalanceSheetComponentsRevenueRemainingPerformanceObligationDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionTable
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionLineItems
      - us-gaap_RevenueRemainingPerformanceObligation
      - us-gaap_RevenueRemainingPerformanceObligationPercentage
      - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionPeriod1

### http://www.nvidia.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.nvidia.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_SummaryOfIncomeTaxContingenciesTextBlock

### http://www.nvidia.com/role/IncomeTaxesComponentsofIncomeTaxExpenseDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_CurrentIncomeTaxExpenseBenefitContinuingOperationsAbstract
    - us-gaap_CurrentFederalTaxExpenseBenefit
    - us-gaap_CurrentStateAndLocalTaxExpenseBenefit
    - us-gaap_CurrentForeignTaxExpenseBenefit
    - us-gaap_CurrentIncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_DeferredIncomeTaxExpenseBenefitContinuingOperationsAbstract
    - us-gaap_DeferredFederalIncomeTaxExpenseBenefit
    - us-gaap_DeferredForeignIncomeTaxExpenseBenefit
    - us-gaap_DeferredIncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestmentsAbstract
    - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
    - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
    - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]

### http://www.nvidia.com/role/IncomeTaxesIncomeTaxReconciliationDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
  - us-gaap_IncomeTaxExpenseBenefitContinuingOperationsIncomeTaxReconciliationAbstract
    - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
    - nvda_EffectiveIncomeTaxRateReconciliationForeignDerivedIntangibleIncomeAmount
    - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
    - us-gaap_IncomeTaxReconciliationNondeductibleExpenseShareBasedCompensationCost
    - us-gaap_IncomeTaxReconciliationTaxCreditsResearch
    - nvda_EffectiveIncomeTaxRateReconciliationIntellectualPropertyDomestication
    - us-gaap_IncomeTaxReconciliationOtherAdjustments
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.nvidia.com/role/IncomeTaxesDeferredTaxesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxContingencyTable
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_IncomeTaxContingencyLineItems
      - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
      - us-gaap_ComponentsOfDeferredTaxLiabilitiesAbstract
      - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]

### http://www.nvidia.com/role/IncomeTaxesNarrativeDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxContingencyTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_IncomeTaxContingencyLineItems
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_EffectiveIncomeTaxRateContinuingOperations
      - us-gaap_IncomeTaxExpenseBenefitContinuingOperationsAdjustmentOfDeferredTaxAssetLiability
      - nvda_DeferredIncomeTaxLiabilitiesIntangiblesAndUndistributedEarningsFromForeignSubsidiaries
      - nvda_DeferredIncomeTaxLiabilitiesInsideBasisDifferenceInAcquiredBusiness
      - us-gaap_UndistributedEarningsOfForeignSubsidiaries
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsResearch
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - nvda_UnrecognizedTaxBenefitsRelatedtoStateIncomeTaxPositions
      - nvda_ReductionOfDeferredTaxAssetIncludedInUnrecognizedTaxBenefit
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued

### http://www.nvidia.com/role/IncomeTaxesUnrecognizedTaxBenefitsDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ReconciliationOfUnrecognizedTaxBenefitsExcludingAmountsPertainingToExaminedTaxReturnsRollForward
    - us-gaap_UnrecognizedTaxBenefits
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
    - us-gaap_UnrecognizedTaxBenefitsReductionsResultingFromLapseOfApplicableStatuteOfLimitations
    - us-gaap_UnrecognizedTaxBenefits

### http://www.nvidia.com/role/SegmentInformationRevenueandLonglivedAssetsbyRegionDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_NoncurrentAssets

### http://www.nvidia.com/role/SegmentInformationRevenueandAccountsReceivablebyMajorCustomerDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfEntityWideRevenueByMajorCustomersByReportingSegmentsTable
    - srt_MajorCustomersAxis
      - srt_NameOfMajorCustomerDomain
    - us-gaap_ConcentrationRiskByTypeAxis
      - us-gaap_ConcentrationRiskTypeDomain
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - us-gaap_EntityWideRevenueMajorCustomerLineItems
      - us-gaap_ConcentrationRiskPercentage1

### http://www.nvidia.com/role/SegmentInformationScheduleofRevenuebyMarketDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_EntityWideInformationRevenueFromExternalCustomerLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

## 资产负债表结构 (Balance Sheet Structure)

### http://www.nvidia.com/role/CONSOLIDATEDBALANCESHEETS

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_AssetsAbstract
    - us-gaap_AssetsCurrentAbstract
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_MarketableSecuritiesCurrent
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_InventoryNet
      - us-gaap_PrepaidExpenseAndOtherAssetsCurrent
      - us-gaap_AssetsCurrent [totalLabel]
    - us-gaap_PropertyPlantAndEquipmentNet
    - us-gaap_OperatingLeaseRightOfUseAsset
    - us-gaap_Goodwill
    - us-gaap_IntangibleAssetsNetExcludingGoodwill
    - us-gaap_DeferredIncomeTaxAssetsNet
    - us-gaap_OtherAssetsNoncurrent
    - us-gaap_Assets [totalLabel]
  - us-gaap_LiabilitiesAndStockholdersEquityAbstract
    - us-gaap_LiabilitiesCurrentAbstract
      - us-gaap_AccountsPayableCurrent
      - us-gaap_AccruedLiabilitiesCurrent
      - us-gaap_DebtCurrent
      - us-gaap_LiabilitiesCurrent [totalLabel]
    - us-gaap_LongTermDebtNoncurrent
    - us-gaap_OperatingLeaseLiabilityNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent
    - us-gaap_Liabilities [totalLabel]
    - us-gaap_CommitmentsAndContingencies
    - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterestAbstract
      - us-gaap_PreferredStockValueOutstanding
      - us-gaap_CommonStockValue
      - us-gaap_AdditionalPaidInCapital
      - us-gaap_TreasuryStockValue
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
      - us-gaap_RetainedEarningsAccumulatedDeficit
      - us-gaap_StockholdersEquity [totalLabel]
    - us-gaap_LiabilitiesAndStockholdersEquity [totalLabel]

### http://www.nvidia.com/role/CONSOLIDATEDBALANCESHEETSParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_PreferredStockParOrStatedValuePerShare
  - us-gaap_PreferredStockSharesAuthorized
  - us-gaap_PreferredStockSharesIssued
  - us-gaap_CommonStockParOrStatedValuePerShare
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_CommonStockSharesIssued
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_TreasuryStockShares

### http://www.nvidia.com/role/CONSOLIDATEDSTATEMENTSOFSHAREHOLDERSEQUITY

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTax
  - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockOwnershipPlan
  - us-gaap_StockIssuedDuringPeriodValueEmployeeStockOwnershipPlan
  - us-gaap_SharesPaidForTaxWithholdingForShareBasedCompensation
  - us-gaap_AdjustmentsRelatedToTaxWithholdingForShareBasedCompensation
  - us-gaap_DividendsCommonStockCash
  - nvda_APICShareBasedPaymentArrangementIncreaseForCostRecognitionOfAwardsAssumedInAcquisition
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
  - us-gaap_TreasuryStockRetiredCostMethodAmount
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember
    - us-gaap_AdditionalPaidInCapitalMember
    - us-gaap_TreasuryStockMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
    - us-gaap_RetainedEarningsMember

### http://www.nvidia.com/role/CONSOLIDATEDSTATEMENTSOFSHAREHOLDERSEQUITYParenthetical

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_CommonStockDividendsPerShareCashPaid

### http://www.nvidia.com/role/CONSOLIDATEDSTATEMENTSOFCASHFLOWS

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetIncomeLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities
    - us-gaap_ProceedsFromSaleOfAvailableForSaleSecuritiesDebt
    - us-gaap_PaymentsToAcquireAvailableForSaleSecuritiesDebt
    - nvda_PurchasesOfPropertyAndEquipmentAndIntangibleAssets
    - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
    - us-gaap_PaymentsForProceedsFromOtherInvestingActivities
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
    - nvda_Netproceedspaymentsrelatedtoemployeestockplans
    - us-gaap_PaymentsRelatedToTaxWithholdingForShareBasedCompensation
    - us-gaap_RepaymentsOfDebt
    - us-gaap_PaymentsOfDividends
    - nvda_PaymentsForFinancedPropertyPlantAndEquipmentFinancingActivities
    - us-gaap_ProceedsFromPaymentsForOtherFinancingActivities
    - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect [totalLabel]
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
  - us-gaap_SupplementalCashFlowInformationAbstract
    - us-gaap_IncomeTaxesPaidNet
    - us-gaap_InterestPaidNet

### http://www.nvidia.com/role/BusinessCombination

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_BusinessCombinationDisclosureTextBlock

### http://www.nvidia.com/role/BusinessCombinationTables

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfRecognizedIdentifiedAssetsAcquiredAndLiabilitiesAssumedTableTextBlock
  - us-gaap_FiniteLivedAndIndefiniteLivedIntangibleAssetsAcquiredAsPartOfBusinessCombinationTableTextBlock
  - us-gaap_BusinessAcquisitionProFormaInformationTextBlock

### http://www.nvidia.com/role/BusinessCombinationTerminationoftheArmSharePurchaseAgreementAdditionalInformationDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable

### http://www.nvidia.com/role/BusinessCombinationAcquisitionofMellanoxTechnologiesAdditionalInformationDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable

### http://www.nvidia.com/role/BusinessCombinationAssetsAcquiredandLiabilitiesAssumedDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationConsiderationTransferredAbstract
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredGoodwillAndLiabilitiesAssumedNetAbstract
      - us-gaap_BusinessAcquisitionSharePrice
      - us-gaap_BusinessAcquisitionEquityInterestsIssuedOrIssuableNumberOfSharesIssued
      - nvda_BusinessAcquisitionAcquireeStockOptionsSettledInCashNumberOfOptions

### http://www.nvidia.com/role/BusinessCombinationIntangibleAssetsAcquiredDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAcquiredAsPartOfBusinessCombinationTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_AcquiredFiniteLivedIntangibleAssetsLineItems
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIndefiniteLivedIntangibleAssets
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibleAssetsOtherThanGoodwill [totalLabel]
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.nvidia.com/role/BusinessCombinationProFormaInformationDetails

- us-gaap_BusinessCombinationAndAssetAcquisitionAbstract
  - us-gaap_BusinessAcquisitionsProFormaRevenue
  - us-gaap_BusinessAcquisitionsProFormaNetIncomeLoss

### http://www.nvidia.com/role/StockBasedCompensationEquityIncentivePlansDetails

- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNonOptionEquityInstrumentsOutstandingRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNonOptionEquityInstrumentsOutstandingNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNonOptionEquityInstrumentsOutstandingNumber

### http://www.nvidia.com/role/Goodwill

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillDisclosureTextBlock

### http://www.nvidia.com/role/GoodwillDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTable

### http://www.nvidia.com/role/AmortizableIntangibleAssets

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_IntangibleAssetsDisclosureTextBlock

### http://www.nvidia.com/role/AmortizableIntangibleAssetsTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTableTextBlock

### http://www.nvidia.com/role/AmortizableIntangibleAssetsDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIndefiniteLivedIntangibleAssets
  - us-gaap_AmortizationOfIntangibleAssets
  - us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecurities

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_InvestmentsInDebtAndMarketableEquitySecuritiesAndCertainTradingAssetsDisclosureTextBlock

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesTables

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_DebtSecuritiesAvailableForSaleTableTextBlock
  - us-gaap_ScheduleOfUnrealizedLossOnInvestmentsTableTextBlock

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_DebtSecuritiesAvailableForSaleTable

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesUnrealizedLossesAggregatedbyInvestmentCategoryDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_ScheduleOfAvailableForSaleSecuritiesTable

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesAmortizedCostandEstimatedFairValueofCashEquivalentsandMarketableSecuritiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAmortizedCostBasisRollingMaturityAbstract
  - us-gaap_FairValueDisclosuresAbstract

### http://www.nvidia.com/role/FairValueofFinancialAssetsandLiabilities

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueDisclosuresTextBlock

### http://www.nvidia.com/role/FairValueofFinancialAssetsandLiabilitiesTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_ScheduleOfFairValueAssetsAndLiabilitiesMeasuredOnRecurringBasisTableTextBlock

### http://www.nvidia.com/role/FairValueofFinancialAssetsandLiabilitiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueByAssetClassAxis
      - us-gaap_FairValueAssetsMeasuredOnRecurringBasisUnobservableInputReconciliationByAssetClassDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
      - us-gaap_AssetsFairValueDisclosureAbstract
      - us-gaap_LiabilitiesFairValueDisclosureAbstract
      - us-gaap_LongTermDebtPercentageBearingFixedInterestRate
      - us-gaap_EquitySecuritiesFvNiUnrealizedGain

### http://www.nvidia.com/role/BalanceSheetComponents

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_SupplementalBalanceSheetDisclosuresTextBlock

### http://www.nvidia.com/role/BalanceSheetComponentsTables

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_ScheduleOfInventoryCurrentTableTextBlock
  - us-gaap_PropertyPlantAndEquipmentTextBlock
  - us-gaap_ScheduleOfOtherAssetsTableTextBlock
  - us-gaap_ScheduleOfAccountsPayableAndAccruedLiabilitiesTableTextBlock
  - us-gaap_OtherNoncurrentLiabilitiesTableTextBlock
  - us-gaap_ContractWithCustomerAssetAndLiabilityTableTextBlock

### http://www.nvidia.com/role/BalanceSheetComponentsInventoriesDetails

- us-gaap_TextBlockAbstract
  - us-gaap_InventoryNetAbstract
    - us-gaap_InventoryRawMaterials
    - us-gaap_InventoryWorkInProcess
    - us-gaap_InventoryFinishedGoods
    - us-gaap_InventoryNet [totalLabel]

### http://www.nvidia.com/role/BalanceSheetComponentsPropertyandEquipmentDetails

- us-gaap_TextBlockAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]
      - us-gaap_PropertyPlantAndEquipmentUsefulLife

### http://www.nvidia.com/role/BalanceSheetComponentsNarrativeDetails

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_Depreciation
  - nvda_Accumulatedamortizationofleaseholdimprovementsandcapitallease
  - us-gaap_CapitalExpendituresIncurredButNotYetPaid

### http://www.nvidia.com/role/BalanceSheetComponentsOtherAssetsDetails

- us-gaap_TextBlockAbstract
  - nvda_PrepaidSupplyAgreementsNoncurrent
  - nvda_BusinessCombinationAdvancedConsideration
  - nvda_PrepaidRoyaltiesNoncurrent
  - us-gaap_OtherLongTermInvestments
  - us-gaap_OtherAssetsMiscellaneousNoncurrent
  - us-gaap_OtherAssetsNoncurrent [totalLabel]

### http://www.nvidia.com/role/BalanceSheetComponentsAccruedandOtherCurrentLiabilitiesDetails

- us-gaap_TextBlockAbstract
  - us-gaap_AccruedLiabilitiesCurrentAbstract
    - nvda_AccruedCustomerProgramsCurrent
    - us-gaap_EmployeeRelatedLiabilitiesCurrent
    - us-gaap_ContractWithCustomerLiabilityCurrent
    - nvda_ExcessInventoryPurchaseObligationsCurrent
    - us-gaap_OtherAccruedLiabilitiesCurrent
    - us-gaap_AccruedLiabilitiesCurrent [totalLabel]

### http://www.nvidia.com/role/BalanceSheetComponentsOtherLongTermLiabilitiesDetails

- us-gaap_TextBlockAbstract
  - us-gaap_OtherLiabilitiesNoncurrentAbstract
    - us-gaap_AccruedIncomeTaxesNoncurrent
    - us-gaap_DeferredIncomeTaxLiabilitiesNet
    - us-gaap_ContractWithCustomerLiabilityNoncurrent
    - us-gaap_OtherSundryLiabilitiesNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]
    - nvda_Onetimetransitiontaxpayablenoncurrent
    - nvda_UnrecognizedTaxBenefitNoncurrent
    - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued

### http://www.nvidia.com/role/ShareholdersEquity

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.nvidia.com/role/ShareholdersEquityDetails

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_AdditionalPaidInCapitalMember
    - us-gaap_RetainedEarningsMember
- us-gaap_EquityClassOfTreasuryStockLineItems
  - nvda_AggregateNumberOfSharesRepurchasedUnderStockRepurchaseProgram
  - nvda_Aggregatedcostofsharesrepurchased
  - us-gaap_StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1
  - us-gaap_TreasuryStockSharesAcquired
  - us-gaap_TreasuryStockValueAcquiredCostMethod
  - us-gaap_PaymentsOfDividends
  - us-gaap_TreasuryStockSharesRetired
  - us-gaap_TreasuryStockRetiredCostMethodAmount
- us-gaap_EquityAbstract
  - us-gaap_ClassOfTreasuryStockTable

## 现金流量表结构 (Cash Flow Structure)

### http://www.nvidia.com/role/CONSOLIDATEDSTATEMENTSOFCASHFLOWS

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInInventories
  - us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities
  - us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesDetails

- us-gaap_DebtSecuritiesAvailableForSaleTable
  - us-gaap_FinancialInstrumentAxis
    - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
      - us-gaap_CorporateDebtSecuritiesMember
      - us-gaap_USTreasurySecuritiesMember
      - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
      - us-gaap_CertificatesOfDepositMember
      - us-gaap_MoneyMarketFundsMember
      - us-gaap_ForeignGovernmentDebtSecuritiesMember
  - us-gaap_ScheduleOfAvailableForSaleSecuritiesLineItems
    - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis [totalLabel]
    - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
    - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
    - us-gaap_AvailableForSaleSecuritiesDebtSecurities
    - us-gaap_CashEquivalentsAtCarryingValue
    - us-gaap_MarketableSecurities

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesUnrealizedLossesAggregatedbyInvestmentCategoryDetails

- us-gaap_ScheduleOfAvailableForSaleSecuritiesTable
  - us-gaap_FinancialInstrumentAxis
    - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
      - us-gaap_CorporateDebtSecuritiesMember
      - us-gaap_USTreasurySecuritiesMember
  - us-gaap_ScheduleOfAvailableForSaleSecuritiesLineItems
    - nvda_DebtSecuritiesAvailableForSaleUnrealizedLossPositionAbstract
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPositionLessThan12Months
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPosition12MonthsOrLonger
      - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPosition [totalLabel]
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionAccumulatedLossAbstract
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPositionLessThan12MonthsAccumulatedLoss
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPosition12MonthsOrLongerAccumulatedLoss
      - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPositionAccumulatedLoss

### http://www.nvidia.com/role/CashEquivalentsandMarketableSecuritiesAmortizedCostandEstimatedFairValueofCashEquivalentsandMarketableSecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtSecurities [totalLabel]
- us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAmortizedCostBasisRollingMaturityAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearAmortizedCost
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsAmortizedCost
  - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis [totalLabel]

## 股东权益结构 (Equity Structure)

### http://www.nvidia.com/role/CONSOLIDATEDSTATEMENTSOFSHAREHOLDERSEQUITY

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward

### http://www.nvidia.com/role/StockBasedCompensation

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_DisclosureOfCompensationRelatedCostsShareBasedPaymentsTextBlock

### http://www.nvidia.com/role/StockBasedCompensationTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock
  - us-gaap_DisclosureOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTextBlock
  - us-gaap_ScheduleOfShareBasedPaymentAwardStockOptionsValuationAssumptionsTableTextBlock
  - us-gaap_ScheduleOfShareBasedCompensationActivityTableTextBlock

### http://www.nvidia.com/role/StockBasedCompensationScheduleofStockBasedCompensationExpenseDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
      - us-gaap_AllocatedShareBasedCompensationExpense

### http://www.nvidia.com/role/StockBasedCompensationSummaryofEquityAwardsDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
      - nvda_ShareBasedCompensationArrangementByShareBasedPaymentAwardRsuGrantsInPeriodGrantDateTotalFairValue [totalLabel]
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockPurchasePlans
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardPerShareWeightedAveragePriceOfSharesPurchased
      - nvda_SummaryofunearnedSBCexpenseAbstract
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsAndMethodologyAbstract

### http://www.nvidia.com/role/StockBasedCompensationNarrativeDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_VestingAxis
      - us-gaap_VestingDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - nvda_NumberOfSharesMayBeIssuedUnderRestated2007Plan
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestExercisableNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardAwardVestingRightsPercentage
      - nvda_QuarterlyVestingSchedulePeriodOne
      - nvda_MaximumissuablesharesofMarketBasedPSUspercentage
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardMaximumEmployeeSubscriptionRate
      - nvda_EmployeeStockPurchasePlanOfferingPeriodDuration
      - nvda_EmployeeStockPurchasePlanNumberOfPurchasePeriodsInOfferingPeriod
      - nvda_EmployeeStockPurchasePlanPurchasePeriodDuration
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardPurchasePriceOfCommonStockPercent
      - nvda_Sharesreservedforfutureissuance
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsExercisableIntrinsicValue1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingIntrinsicValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisableWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
      - us-gaap_SharebasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeExercisableOptionsWeightedAverageRemainingContractualTerm2
      - us-gaap_SharebasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeOutstandingOptionsWeightedAverageRemainingContractualTerm2
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue [totalLabel]
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]

### http://www.nvidia.com/role/StockBasedCompensationEquityIncentivePlansDetails

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNonOptionEquityInstrumentsOutstandingRollForward
  - nvda_VestedandexpectedtovestRSUsPSUsandMarketbasedPSUs
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
  - nvda_SharebasedCompensationArrangementbySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedandExpectedtoVestOutstandingWeightedAverageExercisePrice

### http://www.nvidia.com/role/ShareholdersEquityDetails

- us-gaap_ClassOfTreasuryStockTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_SubsequentEventTypeAxis
    - us-gaap_SubsequentEventTypeDomain
      - us-gaap_SubsequentEventMember
  - us-gaap_EquityClassOfTreasuryStockLineItems

## 其他结构 (Other Structure)

### http://www.nvidia.com/role/CoverPage

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
  - dei_EntityShellCompany
  - dei_EntityPublicFloat
  - dei_EntityCommonStockSharesOutstanding
  - dei_DocumentsIncorporatedByReferenceTextBlock
  - dei_EntityCentralIndexKey
  - dei_DocumentFiscalYearFocus
  - dei_DocumentFiscalPeriodFocus
  - dei_AmendmentFlag

### http://www.nvidia.com/role/AuditInformation

- nvda_AuditInformationAbstract
  - dei_AuditorFirmId
  - dei_AuditorName
  - dei_AuditorLocation

### http://www.nvidia.com/role/OrganizationandSummaryofSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_SignificantAccountingPoliciesTextBlock

### http://www.nvidia.com/role/OrganizationandSummaryofSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - nvda_NatureOfOperationsPolicyTextBlock
  - us-gaap_FiscalPeriod
  - us-gaap_PriorPeriodReclassificationAdjustmentDescription
  - us-gaap_ConsolidationPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_RevenueFromContractWithCustomerPolicyTextBlock
  - us-gaap_CommitmentsAndContingenciesPolicyTextBlock
  - us-gaap_CompensationRelatedCostsPolicyTextBlock
  - us-gaap_LegalCostsPolicyTextBlock
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_EarningsPerSharePolicyTextBlock
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_MarketableSecuritiesPolicy
  - us-gaap_InvestmentPolicyTextBlock
  - us-gaap_ConcentrationRiskCreditRisk
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_LesseeLeasesPolicyTextBlock
  - us-gaap_GoodwillAndIntangibleAssetsPolicyTextBlock
  - us-gaap_IntangibleAssetsFiniteLivedPolicy
  - us-gaap_BusinessCombinationsPolicy
  - us-gaap_EquityMethodInvestmentsPolicy
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock

### http://www.nvidia.com/role/OrganizationandSummaryofSignificantAccountingPoliciesDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_StockholdersEquityNoteStockSplitConversionRatio1
      - nvda_WarrantyLiabilityTermOfWarranties
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife

### http://www.nvidia.com/role/BusinessCombinationTerminationoftheArmSharePurchaseAgreementAdditionalInformationDetails

- us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
  - us-gaap_BusinessAcquisitionAxis
    - us-gaap_BusinessAcquisitionAcquireeDomain
      - nvda_ArmLimitedMember
  - srt_StatementScenarioAxis
    - srt_ScenarioUnspecifiedDomain
      - srt_ScenarioForecastMember
  - us-gaap_BusinessAcquisitionLineItems
    - nvda_BusinessCombinationAdvancedConsiderationWrittenOff

### http://www.nvidia.com/role/BusinessCombinationAcquisitionofMellanoxTechnologiesAdditionalInformationDetails

- us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
  - us-gaap_BusinessAcquisitionAxis
    - us-gaap_BusinessAcquisitionAcquireeDomain
      - nvda_MellanoxTechnologiesLtdMember
  - us-gaap_ConcentrationRiskByBenchmarkAxis
    - us-gaap_ConcentrationRiskBenchmarkDomain
      - us-gaap_SalesRevenueNetMember
  - us-gaap_ConcentrationRiskByTypeAxis
    - us-gaap_ConcentrationRiskTypeDomain
      - nvda_RevenueStreamConcentrationRiskMember
  - us-gaap_BusinessAcquisitionLineItems
    - us-gaap_BusinessCombinationConsiderationTransferred1
    - us-gaap_ConcentrationRiskPercentage1
    - us-gaap_BusinessCombinationAcquisitionRelatedCosts
    - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIndefiniteLivedIntangibleAssets
    - us-gaap_BusinessCombinationProvisionalInformationInitialAccountingIncompleteAdjustmentInventory

### http://www.nvidia.com/role/Leases

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeasesTextBlock

### http://www.nvidia.com/role/LeasesTables

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeaseLiabilityMaturityTableTextBlock
  - nvda_OtherInformationRelatedtoLeasesTableTextBlock

### http://www.nvidia.com/role/LeasesNarrativeDetails

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeaseCost
  - us-gaap_OperatingLeaseWeightedAverageRemainingLeaseTerm1
  - us-gaap_OperatingLeaseWeightedAverageDiscountRatePercent
  - us-gaap_LesseeOperatingLeaseLeaseNotYetCommencedTermOfContract1
  - nvda_LesseeOperatingLeaseLeaseNotYetCommencedUndiscountedAmount

### http://www.nvidia.com/role/LeasesScheduleoffutureminimumpaymentsDetails

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
  - us-gaap_OperatingLeaseLiabilityCurrentStatementOfFinancialPositionExtensibleList
  - us-gaap_OperatingLeaseLiabilityCurrent
  - us-gaap_OperatingLeaseLiabilityNoncurrent

### http://www.nvidia.com/role/LeasesScheduleofotherleaseinformationDetails

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LesseeLeaseDescriptionLineItems
      - us-gaap_OperatingLeasePayments
      - us-gaap_RightOfUseAssetObtainedInExchangeForOperatingLeaseLiability

### http://www.nvidia.com/role/GoodwillDetails

- us-gaap_ScheduleOfGoodwillTable
  - us-gaap_StatementBusinessSegmentsAxis
    - us-gaap_SegmentDomain
      - nvda_GraphicsMember
      - nvda_ComputeAndNetworkingMember
  - us-gaap_GoodwillLineItems
    - us-gaap_Goodwill
    - us-gaap_GoodwillAcquiredDuringPeriod
    - us-gaap_GoodwillPeriodIncreaseDecrease
    - us-gaap_GoodwillImpairmentLoss

### http://www.nvidia.com/role/DerivativeFinancialInstruments

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureTextBlock

### http://www.nvidia.com/role/DerivativeFinancialInstrumentsTables

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_ScheduleOfNotionalAmountsOfOutstandingDerivativePositionsTableTextBlock

### http://www.nvidia.com/role/DerivativeFinancialInstrumentsDetails

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - nvda_NotionalamountofFXforwardcontractdesignatedashedge
  - nvda_NotionalamountofFXforwardcontractnondesignatedashedge

### http://www.nvidia.com/role/DerivativeFinancialInstrumentsNarrativeDetails

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeTable
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativeLineItems
      - us-gaap_MaximumRemainingMaturityOfForeignCurrencyDerivatives1

### http://www.nvidia.com/role/Debt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.nvidia.com/role/DebtTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtInstrumentsTextBlock

### http://www.nvidia.com/role/DebtNarrativeDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
      - us-gaap_RepaymentsOfDebt
      - us-gaap_LongTermDebtPercentageBearingFixedInterestRate
      - us-gaap_LineOfCreditFacilityCurrentBorrowingCapacity
      - us-gaap_CommercialPaper

### http://www.nvidia.com/role/DebtScheduleofDebtDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LongTermDebtPercentageBearingFixedInterestRate
      - us-gaap_DebtInstrumentTerm
      - us-gaap_DebtInstrumentInterestRateDuringPeriod
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_DebtInstrumentUnamortizedDiscountPremiumAndDebtIssuanceCostsNet
      - us-gaap_LongTermDebt [totalLabel]
      - us-gaap_LongTermDebtCurrent
      - us-gaap_LongTermDebtNoncurrent

### http://www.nvidia.com/role/CommitmentsandContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.nvidia.com/role/CommitmentandContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - srt_ContractualObligationFiscalYearMaturityScheduleTableTextBlock

### http://www.nvidia.com/role/CommitmentsandContingenciesNarrativeDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_SupplyCommitmentTable
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - us-gaap_SupplyCommitmentLineItems
      - nvda_PurchaseObligationSupplyAgreements
      - nvda_PurchaseObligationInventoryPurchaseAndSupplyAgreements
      - us-gaap_OtherCommitment
      - nvda_PurchaseObligationSupplyAgreementsTerm
      - us-gaap_ProductWarrantyAccrual

### http://www.nvidia.com/role/CommitmentandContingenciesSummaryofFutureCommitmentsDuebyYearDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_PurchaseObligationFiscalYearMaturityAbstract
    - us-gaap_PurchaseObligationDueInNextTwelveMonths
    - us-gaap_PurchaseObligationDueInSecondYear
    - us-gaap_PurchaseObligationDueInThirdYear
    - us-gaap_PurchaseObligationDueInFourthYear
    - us-gaap_PurchaseObligation [totalLabel]

### http://www.nvidia.com/role/EmployeeRetirementPlans

- us-gaap_CompensationAndRetirementDisclosureAbstract
  - us-gaap_PensionAndOtherPostretirementBenefitsDisclosureTextBlock

### http://www.nvidia.com/role/EmployeeRetirementPlansDetails

- us-gaap_CompensationAndRetirementDisclosureAbstract
  - us-gaap_DefinedContributionPlanCostRecognized

### http://www.nvidia.com/role/SegmentInformation

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.nvidia.com/role/SegmentInformationTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsByGeographicalAreasTableTextBlock
  - nvda_ScheduleofRevenuebyMarketsTableTextBlock
  - us-gaap_LongLivedAssetsByGeographicAreasTableTextBlock

### http://www.nvidia.com/role/SegmentInformationNarrativeDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_NumberOfReportableSegments
  - us-gaap_ConcentrationRiskPercentage1

### http://www.nvidia.com/role/SegmentInformationReportableSegmentsDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - srt_ConsolidationItemsAxis
      - srt_ConsolidationItemsDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_OperatingIncomeLoss

### http://www.nvidia.com/role/SegmentInformationReconcilingItemsDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - srt_ConsolidationItemsAxis
      - srt_ConsolidationItemsDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_ShareBasedCompensation
      - nvda_AcquisitionRelatedIntangibleAssetAmortizationInventoryStepUpChargeAndOtherCosts
      - nvda_UnallocatedCorporateExpensesAndOtherExpenses
      - nvda_IPRelatedCosts
      - us-gaap_OperatingIncomeLoss

### http://www.nvidia.com/role/SCHEDULEIIVALUATIONANDQUALIFYINGACCOUNTS

- srt_ValuationAndQualifyingAccountsAbstract
  - srt_ScheduleOfValuationAndQualifyingAccountsDisclosureTextBlock

### http://www.nvidia.com/role/SCHEDULEIIVALUATIONANDQUALIFYINGACCOUNTSDetails

- srt_ValuationAndQualifyingAccountsAbstract
  - srt_ValuationAndQualifyingAccountsDisclosureTable
    - us-gaap_ValuationAllowancesAndReservesTypeAxis
      - us-gaap_ValuationAllowancesAndReservesDomain
    - srt_ValuationAndQualifyingAccountsDisclosureLineItems
      - us-gaap_MovementInValuationAllowancesAndReservesRollForward

