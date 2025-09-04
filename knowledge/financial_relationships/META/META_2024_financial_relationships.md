# META 2024 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.facebook.com/role/CONSOLIDATEDSTATEMENTSOFINCOME

- us-gaap_IncomeStatementAbstract
  - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
  - us-gaap_CostsAndExpensesAbstract
    - us-gaap_CostOfRevenue
    - us-gaap_ResearchAndDevelopmentExpense
    - us-gaap_SellingAndMarketingExpense
    - us-gaap_GeneralAndAdministrativeExpense
    - us-gaap_CostsAndExpenses [totalLabel]
  - us-gaap_OperatingIncomeLoss [totalLabel]
  - us-gaap_NonoperatingIncomeExpense
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]
  - us-gaap_IncomeTaxExpenseBenefit
  - us-gaap_NetIncomeLoss [totalLabel]
  - us-gaap_EarningsPerShareAbstract
    - us-gaap_EarningsPerShareBasic
    - us-gaap_EarningsPerShareDiluted
  - us-gaap_WeightedAverageNumberOfSharesOutstandingDilutedDisclosureItemsAbstract
    - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
    - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding

### http://www.facebook.com/role/CONSOLIDATEDSTATEMENTSOFCOMPREHENSIVEINCOME

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
    - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
    - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodNetOfTax
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.facebook.com/role/CONSOLIDATEDSTATEMENTSOFCASHFLOWS

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_DepreciationDepletionAndAmortization
  - us-gaap_ShareBasedCompensation
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_ImpairmentOfLongLivedAssetsHeldForUse
  - us-gaap_RestructuringCharges
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.facebook.com/role/Revenue

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueFromContractWithCustomerTextBlock

### http://www.facebook.com/role/EarningsperShare

- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareTextBlock

### http://www.facebook.com/role/InterestandOtherIncomeExpenseNet

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_OtherNonoperatingIncomeAndExpenseTextBlock

### http://www.facebook.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.facebook.com/role/RevenueTables

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_DisaggregationOfRevenueTableTextBlock

### http://www.facebook.com/role/EarningsperShareTables

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock

### http://www.facebook.com/role/InterestandOtherIncomeExpenseNetTables

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_ScheduleOfOtherNonoperatingIncomeExpenseTableTextBlock

### http://www.facebook.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfUnrecognizedTaxBenefitsRollForwardTableTextBlock

### http://www.facebook.com/role/RevenueScheduleofDisaggregationofRevenueDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_DisaggregationOfRevenueTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_DisaggregationOfRevenueLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

### http://www.facebook.com/role/RevenueNarrativeDetails

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_ContractWithCustomerLiability
  - us-gaap_ContractWithCustomerLiabilityCurrent

### http://www.facebook.com/role/RestructuringRestructuringandRelatedCostsDetails

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember
    - us-gaap_SellingAndMarketingExpenseMember
    - us-gaap_GeneralAndAdministrativeExpenseMember

### http://www.facebook.com/role/EarningsperShareNarrativeDetails

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareLineItems
      - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount

### http://www.facebook.com/role/EarningsperShareScheduleofNumeratorsandDenominatorsofBasicandDilutedEPSComputationsforCommonStockDetails

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfEarningsPerShareBasicByCommonClassTable
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_EarningsPerShareBasicLineItems
      - us-gaap_EarningsPerShareBasicAbstract
      - us-gaap_EarningsPerShareDilutedAbstract

### http://www.facebook.com/role/AcquisitionsGoodwillandIntangibleAssetsScheduleofAmortizationExpenseDetails

- us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseCurrentAndFiveSucceedingFiscalYearsAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.facebook.com/role/StockholdersEquitySummaryofShareBasedCompensationExpenseDetails

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember
    - us-gaap_SellingAndMarketingExpenseMember
    - us-gaap_GeneralAndAdministrativeExpenseMember

### http://www.facebook.com/role/InterestandOtherIncomeExpenseNetDetails

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_InvestmentIncomeInterest
  - us-gaap_InterestExpense
  - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_NonoperatingIncomeExpense [totalLabel]

### http://www.facebook.com/role/IncomeTaxesScheduleforIncomeBeforeIncomeTaxDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]

### http://www.facebook.com/role/IncomeTaxesScheduleofProvisionforIncomeTaxesDetails

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
      - meta_TotalDeferredIncomeTaxExpenseBenefit [totalLabel]
    - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.facebook.com/role/IncomeTaxesScheduleofEffectiveIncomeTaxRateReconciliationDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_EffectiveIncomeTaxRateContinuingOperationsTaxRateReconciliationAbstract
    - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
    - us-gaap_EffectiveIncomeTaxRateReconciliationStateAndLocalIncomeTaxes
    - us-gaap_EffectiveIncomeTaxRateReconciliationNondeductibleExpenseShareBasedCompensationCost
    - us-gaap_EffectiveIncomeTaxRateReconciliationTaxCreditsResearch
    - us-gaap_EffectiveIncomeTaxRateReconciliationFdiiPercent
    - us-gaap_EffectiveIncomeTaxRateReconciliationForeignIncomeTaxRateDifferential
    - us-gaap_EffectiveIncomeTaxRateReconciliationOtherAdjustments
    - us-gaap_EffectiveIncomeTaxRateContinuingOperations [totalLabel]

### http://www.facebook.com/role/IncomeTaxesScheduleofDeferredTaxAssetsandLiabilitiesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ComponentsOfDeferredTaxAssetsAndLiabilitiesAbstract
    - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
      - us-gaap_DeferredTaxAssetsOperatingLossCarryforwards
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwards
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccrualsAccruedLiabilities
      - meta_DeferredTaxAssetsLeaseLiabilities
      - meta_DeferredTaxAssetsTaxDeferredExpenseCapitalizedResearchAndDevelopmentCosts
      - us-gaap_DeferredTaxAssetsUnrealizedLossesOnAvailableforSaleSecuritiesGross
      - us-gaap_DeferredTaxAssetsOther
      - us-gaap_DeferredTaxAssetsGross [totalLabel]
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_DeferredTaxAssetsNet [totalLabel]
    - us-gaap_ComponentsOfDeferredTaxLiabilitiesAbstract
      - us-gaap_DeferredTaxLiabilitiesPropertyPlantAndEquipment
      - us-gaap_DeferredTaxLiabilitiesLeasingArrangements
      - us-gaap_DeferredIncomeTaxLiabilities
    - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]

### http://www.facebook.com/role/IncomeTaxesNarrativeDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - meta_IncomeTaxDisclosureTable
    - us-gaap_TaxPeriodAxis
      - us-gaap_TaxPeriodDomain
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_IncomeTaxAuthorityNameAxis
      - us-gaap_IncomeTaxAuthorityNameDomain
    - meta_IncomeTaxDisclosureLineItems
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_TaxCreditCarryforwardAmount
      - meta_EventCausingOwnershipChangeAndLossInNetOperatingLossAndTaxCreditCarryforwardCumulativeStockOwnershipChangeThreshold
      - meta_EventCausingOwnershipChangeAndLossInNetOperatingLossAndTaxCreditCarryforwardChangeInOwnershipPercentageOverPeriod
      - us-gaap_IncomeTaxExaminationPenaltiesAndInterestAccrued
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - us-gaap_IncomeTaxExaminationEstimateOfPossibleLoss
      - meta_IncomeTaxExaminationNumberOfNotices

### http://www.facebook.com/role/IncomeTaxesScheduleofUnrecognizedTaxBenefitsDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ReconciliationOfUnrecognizedTaxBenefitsExcludingAmountsPertainingToExaminedTaxReturnsRollForward
    - us-gaap_UnrecognizedTaxBenefits
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
    - us-gaap_UnrecognizedTaxBenefits

### http://www.facebook.com/role/SegmentandGeographicalInformationSegmentRevenueandIncomeforOperationsDetails

- us-gaap_SegmentsGeographicalAreasAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_EntityWideInformationRevenueFromExternalCustomerLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_OperatingIncomeLoss

### http://www.facebook.com/role/SegmentandGeographicalInformationScheduleofPropertyandEquipmentDetails

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - srt_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

## 资产负债表结构 (Balance Sheet Structure)

### http://www.facebook.com/role/CONSOLIDATEDBALANCESHEETS

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_AssetsAbstract
    - us-gaap_AssetsCurrentAbstract
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_MarketableSecuritiesCurrent
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_PrepaidExpenseAndOtherAssetsCurrent
      - us-gaap_AssetsCurrent [totalLabel]
    - meta_NonmarketableEquitySecuritiesCarryingValue
    - us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization
    - us-gaap_OperatingLeaseRightOfUseAsset
    - us-gaap_IntangibleAssetsNetExcludingGoodwill
    - us-gaap_Goodwill
    - us-gaap_OtherAssetsNoncurrent
    - us-gaap_Assets [totalLabel]
  - us-gaap_LiabilitiesAndStockholdersEquityAbstract
    - us-gaap_LiabilitiesCurrentAbstract
      - us-gaap_AccountsPayableTradeCurrent
      - us-gaap_AccountsPayableOtherCurrent
      - us-gaap_OperatingLeaseLiabilityCurrent
      - us-gaap_AccruedLiabilitiesCurrent
      - us-gaap_LiabilitiesCurrent [totalLabel]
    - us-gaap_OperatingLeaseLiabilityNoncurrent
    - us-gaap_LongTermDebtNoncurrent
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

### http://www.facebook.com/role/CONSOLIDATEDBALANCESHEETSParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_StatementLineItems
      - us-gaap_StockholdersEquityAbstract

### http://www.facebook.com/role/CONSOLIDATEDSTATEMENTSOFSTOCKHOLDERSEQUITY

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
  - us-gaap_StockIssuedDuringPeriodSharesNewIssues
  - us-gaap_SharesPaidForTaxWithholdingForShareBasedCompensation
  - us-gaap_AdjustmentsRelatedToTaxWithholdingForShareBasedCompensation
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
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

### http://www.facebook.com/role/CONSOLIDATEDSTATEMENTSOFCASHFLOWS

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_StatementTable
- us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
- us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
  - us-gaap_PaymentsRelatedToTaxWithholdingForShareBasedCompensation
  - us-gaap_PaymentsForRepurchaseOfCommonStock
  - us-gaap_ProceedsFromIssuanceOfLongTermDebt
  - us-gaap_FinanceLeasePrincipalPayments
  - us-gaap_ProceedsFromPaymentsForOtherFinancingActivities
  - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
- us-gaap_RestrictedCashAndCashEquivalentsCashAndCashEquivalentsAxis
  - us-gaap_RestrictedCashAndCashEquivalentsCashAndCashEquivalentsMember
    - us-gaap_PrepaidExpensesAndOtherCurrentAssetsMember
    - us-gaap_OtherAssetsMember
- us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
  - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
  - us-gaap_ProceedsFromSaleOfPropertyPlantAndEquipment
  - us-gaap_PaymentsToAcquireAvailableForSaleSecuritiesDebt
  - us-gaap_ProceedsFromSaleAndMaturityOfAvailableForSaleSecurities
  - meta_PaymentsToAcquireBusinessesNetOfCashAcquiredAndPurchasesOfIntangibleAndOtherAssets
  - us-gaap_PaymentsForProceedsFromOtherInvestingActivities
  - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
- us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffectAbstract
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_RestrictedCashAndCashEquivalents
  - us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents [totalLabel]
- us-gaap_SupplementalCashFlowInformationAbstract
  - us-gaap_IncomeTaxesPaidNet
  - us-gaap_InterestPaidNet
  - us-gaap_CashFlowNoncashInvestingAndFinancingActivitiesDisclosureAbstract
    - us-gaap_CapitalExpendituresIncurredButNotYetPaid
    - meta_AcquisitionIncurredButNotYetPaid
    - meta_OtherSignificantNoncashTransaction
    - meta_RepurchaseOfCommonStockInAccruedExpensesAndOtherCurrentLiabilities

### http://www.facebook.com/role/NonmarketableEquitySecurities

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - meta_NonMarketableEquityInvestmentsTextBlock

### http://www.facebook.com/role/AcquisitionsGoodwillandIntangibleAssets

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillAndIntangibleAssetsDisclosureTextBlock

### http://www.facebook.com/role/StockholdersEquity

- us-gaap_EquityAbstract
  - us-gaap_ShareholdersEquityAndShareBasedPaymentsTextBlock

### http://www.facebook.com/role/NonmarketableEquitySecuritiesTables

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueTableTextBlock

### http://www.facebook.com/role/AcquisitionsGoodwillandIntangibleAssetsTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTextBlock
  - meta_ScheduleOfFiniteLivedAndIndefiniteLivedIntangibleAssetsTableTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.facebook.com/role/StockholdersEquityTables

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock
  - us-gaap_ScheduleOfShareBasedCompensationRestrictedStockUnitsAwardActivityTableTextBlock

### http://www.facebook.com/role/FinancialInstrumentsScheduleofAssetsMeasuredatFairValueonaRecurringBasisDetails

- meta_FinancialInstrumentsAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_CashAndCashEquivalentsAxis
      - us-gaap_RestrictedCashAndCashEquivalentsCashAndCashEquivalentsMember
    - us-gaap_FinancialInstrumentAxis
      - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
    - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
      - us-gaap_CashAndCashEquivalentsFairValueDisclosure
      - us-gaap_DebtSecuritiesAvailableForSaleExcludingAccruedInterest
      - us-gaap_EquitySecuritiesFvNi
      - us-gaap_MarketableSecuritiesCurrent [totalLabel]
      - us-gaap_RestrictedCashEquivalents
      - us-gaap_OtherAssetsFairValueDisclosure
      - us-gaap_AssetsFairValueDisclosure [totalLabel]

### http://www.facebook.com/role/FinancialInstrumentsNarrativeDetails

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - meta_NonmarketableEquitySecuritiesCarryingValue

### http://www.facebook.com/role/NonmarketableEquitySecuritiesScheduleofNonMarketableEquitySecuritiesDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - meta_EquitySecuritiesWithoutReadilyDeterminableFairValueInitialCost
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueUpwardPriceAdjustmentCumulativeAmount
  - meta_EquitySecuritiesWithoutReadilyDeterminableFairValueImpairmentAndDownwardPriceAdjustmentCumulativeAmount
  - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueAmount
  - us-gaap_EquityMethodInvestments
  - meta_NonmarketableEquitySecuritiesCarryingValue [totalLabel]

### http://www.facebook.com/role/NonmarketableEquitySecuritiesNarrativeDetails

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - meta_EquitySecuritiesWithoutReadilyDeterminableFairValueImpairmentAndDownwardPriceAdjustmentCurrentYearAmount

### http://www.facebook.com/role/LeasesLeaseBalanceSheetInformationDetails

- us-gaap_LeasesAbstract
  - meta_LesseeWeightedAverageRemainingLeaseTermAbstract
    - us-gaap_FinanceLeaseWeightedAverageRemainingLeaseTerm1
    - us-gaap_OperatingLeaseWeightedAverageRemainingLeaseTerm1
  - meta_LesseeWeightedAverageDiscountRateAbstract
    - us-gaap_FinanceLeaseWeightedAverageDiscountRatePercent
    - us-gaap_OperatingLeaseWeightedAverageDiscountRatePercent

### http://www.facebook.com/role/LeasesScheduleofSupplementalCashFlowDetails

- meta_CashFlowLesseeAbstract
  - us-gaap_OperatingLeasePayments
  - us-gaap_FinanceLeaseInterestPaymentOnLiability
  - us-gaap_FinanceLeasePrincipalPayments
- meta_RightOfUseAssetObtainedInExchangeForLeaseLiabilityAbstract
  - us-gaap_RightOfUseAssetObtainedInExchangeForOperatingLeaseLiability
  - us-gaap_RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability

### http://www.facebook.com/role/AcquisitionsGoodwillandIntangibleAssetsNarrativeDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationConsiderationTransferred1
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibleAssetsOtherThanGoodwill
      - us-gaap_Goodwill
      - us-gaap_AmortizationOfIntangibleAssets

### http://www.facebook.com/role/AcquisitionsGoodwillandIntangibleAssetsScheduleofChangeinGoodwillDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_GoodwillLineItems
      - us-gaap_GoodwillRollForward

### http://www.facebook.com/role/AcquisitionsGoodwillandIntangibleAssetsScheduleofIntangibleAssetsDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife
      - us-gaap_FiniteLivedIntangibleAssetsNetAbstract
      - us-gaap_IndefiniteLivedIntangibleAssetsExcludingGoodwillAbstract
      - us-gaap_IntangibleAssetsNetExcludingGoodwillAbstract

### http://www.facebook.com/role/AcquisitionsGoodwillandIntangibleAssetsScheduleofAmortizationExpenseDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseCurrentAndFiveSucceedingFiscalYearsAbstract

### http://www.facebook.com/role/StockholdersEquityCommonStockNarrativeDetails

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfStockByClassTable

### http://www.facebook.com/role/StockholdersEquitySummaryofShareBasedCompensationExpenseDetails

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable

### http://www.facebook.com/role/StockholdersEquityCapitalReturnProgramNarrativeDetails

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfStockByClassTable

### http://www.facebook.com/role/StockholdersEquitySharebasedCompensationPlansNarrativeDetails

- us-gaap_EquityAbstract
  - us-gaap_ShareBasedCompensationAbstract

### http://www.facebook.com/role/StockholdersEquityRSUAwardActivityDetails

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
- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable

### http://www.facebook.com/role/StockholdersEquityAdditionalAwardDisclosuresNarrativeDetails

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable

## 现金流量表结构 (Cash Flow Structure)

### http://www.facebook.com/role/CONSOLIDATEDSTATEMENTSOFCASHFLOWS

- us-gaap_StatementTable
  - us-gaap_RestructuringCostAndReserveAxis
    - us-gaap_TypeOfRestructuringDomain
      - meta_DataCenterAssetsMember
  - us-gaap_RestrictedCashAndCashEquivalentsCashAndCashEquivalentsAxis
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
  - us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities

### http://www.facebook.com/role/LeasesScheduleofMaturitiesofLeaseLiabilitiesDetails

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

### http://www.facebook.com/role/LeasesScheduleofSupplementalCashFlowDetails

- us-gaap_LeasesAbstract
  - meta_CashFlowLesseeAbstract
  - meta_RightOfUseAssetObtainedInExchangeForLeaseLiabilityAbstract

## 股东权益结构 (Equity Structure)

### http://www.facebook.com/role/Coverpage

- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - us-gaap_CommonClassAMember
    - us-gaap_CommonClassBMember

### http://www.facebook.com/role/CONSOLIDATEDSTATEMENTSOFSTOCKHOLDERSEQUITY

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward

### http://www.facebook.com/role/SummaryofSignificantAccountingPoliciesNarrativeDetails

- us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
  - us-gaap_RestrictedStockUnitsRSUMember

### http://www.facebook.com/role/StockholdersEquityCommonStockNarrativeDetails

- us-gaap_ScheduleOfStockByClassTable
  - us-gaap_StatementClassOfStockAxis
    - us-gaap_ClassOfStockDomain
      - us-gaap_CommonClassAMember
      - us-gaap_CommonClassBMember
  - us-gaap_ClassOfStockLineItems
    - us-gaap_CommonStockSharesAuthorized
    - us-gaap_CommonStockParOrStatedValuePerShare
    - meta_CommonStockNumberOfVotesByClass
    - us-gaap_CommonStockSharesIssued
    - us-gaap_CommonStockSharesOutstanding

### http://www.facebook.com/role/StockholdersEquitySummaryofShareBasedCompensationExpenseDetails

- us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_IncomeStatementLocationAxis
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
    - us-gaap_AllocatedShareBasedCompensationExpense

### http://www.facebook.com/role/StockholdersEquityCapitalReturnProgramNarrativeDetails

- us-gaap_ScheduleOfStockByClassTable
  - us-gaap_StatementClassOfStockAxis
    - us-gaap_ClassOfStockDomain
      - us-gaap_CommonClassAMember
  - us-gaap_SubsequentEventTypeAxis
    - us-gaap_SubsequentEventTypeDomain
      - us-gaap_SubsequentEventMember
  - us-gaap_ClassOfStockLineItems
    - us-gaap_StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1
    - us-gaap_StockRepurchaseProgramAuthorizedAmount1
    - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
    - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
    - us-gaap_CommonStockDividendsPerShareDeclared
    - meta_CommonStockDividendsPerShareDeclaredAnnualBasis

### http://www.facebook.com/role/StockholdersEquitySharebasedCompensationPlansNarrativeDetails

- us-gaap_ShareBasedCompensationAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_PlanNameAxis
      - us-gaap_PlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - meta_ShareBasedEmployeeCompensationPlansNumber
      - us-gaap_CommonStockCapitalSharesReservedForFutureIssuance
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfAdditionalSharesAuthorized

### http://www.facebook.com/role/StockholdersEquityRSUAwardActivityDetails

- us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_AwardTypeAxis
    - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
      - us-gaap_RestrictedStockUnitsRSUMember
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward

### http://www.facebook.com/role/StockholdersEquityAdditionalAwardDisclosuresNarrativeDetails

- us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_AwardTypeAxis
    - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
      - us-gaap_RestrictedStockUnitsRSUMember
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
    - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense
    - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
    - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]

### http://xbrl.sec.gov/ecd/role/AwardTimingDisclosure

- us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
  - us-gaap_EmployeeStockOptionMember
  - us-gaap_StockAppreciationRightsSARSMember
  - us-gaap_RestrictedStockUnitsRSUMember

## 其他结构 (Other Structure)

### http://www.facebook.com/role/Coverpage

- dei_CoverAbstract
  - dei_EntitiesTable
    - us-gaap_StatementClassOfStockAxis
    - dei_EntityInformationLineItems
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

### http://www.facebook.com/role/AuditInformation

- meta_AuditorAbstract
  - dei_AuditorFirmId
  - dei_AuditorName
  - dei_AuditorLocation

### http://www.facebook.com/role/SummaryofSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfPresentationAndSignificantAccountingPoliciesTextBlock

### http://www.facebook.com/role/Restructuring

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_RestructuringImpairmentAndOtherActivitiesDisclosureTextBlock

### http://www.facebook.com/role/FinancialInstruments

- meta_FinancialInstrumentsAbstract
  - us-gaap_FinancialInstrumentsDisclosureTextBlock

### http://www.facebook.com/role/PropertyandEquipment

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.facebook.com/role/Leases

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeasesTextBlock
  - us-gaap_LesseeFinanceLeasesTextBlock

### http://www.facebook.com/role/LongtermDebt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_LongTermDebtTextBlock

### http://www.facebook.com/role/Liabilities

- us-gaap_AccountsPayableAndAccruedLiabilitiesCurrentAndNoncurrentAbstract
  - us-gaap_AccountsPayableAndAccruedLiabilitiesDisclosureTextBlock

### http://www.facebook.com/role/CommitmentsandContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.facebook.com/role/SegmentandGeographicalInformation

- us-gaap_SegmentsGeographicalAreasAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.facebook.com/role/SummaryofSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfAccountingPolicyPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_RevenueFromContractWithCustomerPolicyTextBlock
  - us-gaap_ResearchDevelopmentAndComputerSoftwarePolicyTextBlock
  - us-gaap_ShareBasedCompensationOptionAndIncentivePlansPolicy
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_AdvertisingCostsPolicyTextBlock
  - us-gaap_CostsAssociatedWithExitOrDisposalActivitiesOrRestructuringsPolicyTextBlock
  - meta_CashAndCashEquivalentsAndMarketableSecuritiesPolicyTextBlock
  - meta_EquityAndAlternativeMethodInvestmentsPolicyTextBlock
  - us-gaap_FairValueOfFinancialInstrumentsPolicy
  - us-gaap_TradeAndOtherAccountsReceivablePolicy
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_LesseeLeasesPolicyTextBlock
  - us-gaap_ImpairmentOrDisposalOfLongLivedAssetsPolicyTextBlock
  - us-gaap_CommitmentsAndContingenciesPolicyTextBlock
  - us-gaap_BusinessCombinationsPolicy
  - us-gaap_GoodwillAndIntangibleAssetsPolicyTextBlock
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_ConcentrationRiskCreditRisk
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock
  - us-gaap_EarningsPerSharePolicyTextBlock

### http://www.facebook.com/role/SummaryofSignificantAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - meta_PropertyPlantandEquipmentUsefulLifeTableTextBlock

### http://www.facebook.com/role/RestructuringTables

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_ScheduleOfRestructuringAndRelatedCostsTable
    - us-gaap_RestructuringPlanAxis
      - us-gaap_RestructuringPlanDomain
    - us-gaap_RestructuringCostAndReserveAxis
      - us-gaap_TypeOfRestructuringDomain
    - us-gaap_RestructuringCostAndReserveLineItems
      - us-gaap_ScheduleOfRestructuringAndRelatedCostsTextBlock
      - us-gaap_ScheduleOfRestructuringReserveByTypeOfCostTextBlock

### http://www.facebook.com/role/FinancialInstrumentsTables

- meta_FinancialInstrumentsAbstract
  - us-gaap_FairValueAssetsMeasuredOnRecurringBasisTextBlock
  - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPositionFairValueTableTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock

### http://www.facebook.com/role/PropertyandEquipmentTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.facebook.com/role/LeasesTables

- us-gaap_LeasesAbstract
  - us-gaap_LeaseCostTableTextBlock
  - meta_LeaseBalanceSheetInformationTableTextBlock
  - us-gaap_FinanceLeaseLiabilityMaturityTableTextBlock
  - us-gaap_LesseeOperatingLeaseLiabilityMaturityTableTextBlock
  - meta_LeaseCashFlowsInformationTableTextBlock

### http://www.facebook.com/role/LongtermDebtTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtInstrumentsTextBlock
  - us-gaap_ScheduleOfMaturitiesOfLongTermDebtTableTextBlock

### http://www.facebook.com/role/LiabilitiesTables

- us-gaap_AccountsPayableAndAccruedLiabilitiesCurrentAndNoncurrentAbstract
  - us-gaap_ScheduleOfAccruedLiabilitiesTableTextBlock
  - us-gaap_OtherNoncurrentLiabilitiesTableTextBlock

### http://www.facebook.com/role/CommitmentandContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - srt_ContractualObligationFiscalYearMaturityScheduleTableTextBlock

### http://www.facebook.com/role/SegmentandGeographicalInformationTables

- us-gaap_SegmentsGeographicalAreasAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
  - us-gaap_LongLivedAssetsByGeographicAreasTableTextBlock

### http://www.facebook.com/role/SummaryofSignificantAccountingPoliciesNarrativeDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
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
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_RestructuringCostAndReserveAxis
      - us-gaap_TypeOfRestructuringDomain
    - us-gaap_RestructuringPlanAxis
      - us-gaap_RestructuringPlanDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_NumberOfReportableSegments
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_AdvertisingExpense
      - us-gaap_RestructuringCharges
      - us-gaap_NumberOfReportingUnits
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentNetOfTax
      - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
      - us-gaap_ConcentrationRiskPercentage1

### http://www.facebook.com/role/SummaryofSignificantAccountingPoliciesEstimatedUsefulLivesofPropertyandEquipmentDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife

### http://www.facebook.com/role/RestructuringNarrativeDetails

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_ScheduleOfRestructuringAndRelatedCostsTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_RestructuringPlanAxis
      - us-gaap_RestructuringPlanDomain
    - us-gaap_RestructuringCostAndReserveAxis
      - us-gaap_TypeOfRestructuringDomain
    - us-gaap_RestructuringCostAndReserveLineItems
      - us-gaap_RestructuringAndRelatedCostExpectedNumberOfPositionsEliminated
      - us-gaap_RestructuringCharges
      - us-gaap_RestructuringAndRelatedCostCostIncurredToDate1

### http://www.facebook.com/role/RestructuringRestructuringandRelatedCostsDetails

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_ScheduleOfRestructuringAndRelatedCostsTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_RestructuringCostAndReserveAxis
      - us-gaap_TypeOfRestructuringDomain
    - us-gaap_RestructuringPlanAxis
      - us-gaap_RestructuringPlanDomain
    - us-gaap_RestructuringCostAndReserveLineItems
      - us-gaap_RestructuringCharges
      - us-gaap_AllocatedShareBasedCompensationExpense

### http://www.facebook.com/role/RestructuringChangesintheLiabilitiesRelatedtoWorkforceReductionDetails

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_ScheduleOfRestructuringAndRelatedCostsTable
    - us-gaap_RestructuringCostAndReserveAxis
      - us-gaap_TypeOfRestructuringDomain
    - us-gaap_RestructuringPlanAxis
      - us-gaap_RestructuringPlanDomain
    - us-gaap_RestructuringCostAndReserveLineItems
      - us-gaap_RestructuringReserveRollForward

### http://www.facebook.com/role/FinancialInstrumentsAvailableforsaleMarketableSecuritiesDetails

- meta_FinancialInstrumentsAbstract
  - us-gaap_MarketableSecuritiesTable
    - us-gaap_FinancialInstrumentAxis
      - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
    - us-gaap_MarketableSecuritiesLineItems
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPositionLessThan12Months
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPositionLessThan12MonthsAccumulatedLoss
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPosition12MonthsOrLonger
      - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPosition12MonthsOrLongerAccumulatedLoss
      - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPosition [totalLabel]
      - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPositionAccumulatedLoss

### http://www.facebook.com/role/FinancialInstrumentsContractualMaturitiesofMarketableDebtSecuritiesDetails

- meta_FinancialInstrumentsAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesFairValueAbstract
    - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearFairValue
    - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsFairValue
    - us-gaap_DebtSecuritiesAvailableForSaleExcludingAccruedInterest [totalLabel]

### http://www.facebook.com/role/FinancialInstrumentsNarrativeDetails

- meta_FinancialInstrumentsAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueInputsLevel3Member

### http://www.facebook.com/role/PropertyandEquipmentScheduleofPropertyandEquipmentDetails

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_FinanceLeaseRightOfUseAssetBeforeAccumulatedAmortization
      - us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetBeforeAccumulatedDepreciationAndAmortization [totalLabel]
      - us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAccumulatedDepreciationAndAmortization
      - us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization [totalLabel]

### http://www.facebook.com/role/PropertyandEquipmentNarrativeDetails

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_RestructuringCostAndReserveAxis
      - us-gaap_TypeOfRestructuringDomain
    - us-gaap_RestructuringPlanAxis
      - us-gaap_RestructuringPlanDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_ConstructionInProgressGross
      - us-gaap_Depreciation
      - us-gaap_InterestCostsCapitalized
      - us-gaap_RestructuringCharges

### http://www.facebook.com/role/LeasesComponentsofLeaseCostandSupplementaryInfoDetails

- us-gaap_LeasesAbstract
  - us-gaap_LeaseCostAbstract
    - us-gaap_FinanceLeaseRightOfUseAssetAmortization
    - us-gaap_FinanceLeaseInterestExpense
  - us-gaap_OperatingLeaseCost
  - us-gaap_VariableLeaseCost
  - us-gaap_LeaseCost [totalLabel]

### http://www.facebook.com/role/LeasesNarrativeDetails

- us-gaap_LeasesAbstract
  - us-gaap_LesseeLeaseDescriptionTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_RestructuringCostAndReserveAxis
      - us-gaap_TypeOfRestructuringDomain
    - us-gaap_RestructuringPlanAxis
      - us-gaap_RestructuringPlanDomain
    - us-gaap_LesseeLeaseDescriptionLineItems
      - us-gaap_RestructuringCharges
      - meta_LesseeOperatingLeaseLeaseNotYetCommencedAmount
      - meta_LesseeFinanceLeaseLeaseNotYetCommencedAmount
      - meta_LesseeLeaseLeaseNotYetCommencedTermOfContract

### http://www.facebook.com/role/LeasesScheduleofMaturitiesofLeaseLiabilitiesDetails

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
  - us-gaap_FinanceLeaseLiabilityStatementOfFinancialPositionExtensibleList
  - us-gaap_FinanceLeaseLiabilityNoncurrentStatementOfFinancialPositionExtensibleList

### http://www.facebook.com/role/LongtermDebtNarrativeDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueByMeasurementBasisAxis
      - us-gaap_FairValueDisclosureItemAmountsDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_InterestExpenseDebt
      - us-gaap_LongTermDebtFairValue

### http://www.facebook.com/role/LongtermDebtScheduleofCarryingValuesandEstimatedFairValuesofDebtInstrumentsDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_DebtInstrumentUnamortizedDiscountPremiumAndDebtIssuanceCostsNet
      - us-gaap_LongTermDebt [totalLabel]

### http://www.facebook.com/role/LongtermDebtScheduleofMaturitiesofLongTermDebtDetails

- us-gaap_DebtDisclosureAbstract
  - meta_LongTermDebtMaturityYearOneToYearThree
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive
  - us-gaap_DebtInstrumentCarryingAmount [totalLabel]

### http://www.facebook.com/role/LiabilitiesScheduleofAccruedExpensesandOtherCurrentLiabilitiesDetails

- us-gaap_PayablesAndAccrualsAbstract
  - meta_LegalRelatedAccruedLiabilitiesCurrent
  - us-gaap_EmployeeRelatedLiabilitiesCurrent
  - meta_PropertyAndEquipmentAccruedLiabilitiesCurrent
  - us-gaap_TaxesPayableCurrent
  - us-gaap_OtherAccruedLiabilitiesCurrent
  - us-gaap_AccruedLiabilitiesCurrent [totalLabel]

### http://www.facebook.com/role/LiabilitiesScheduleofOtherLiabilitiesDetails

- us-gaap_PayablesAndAccrualsAbstract
  - us-gaap_OtherLiabilitiesAbstract
    - us-gaap_AccruedIncomeTaxesNoncurrent
    - us-gaap_OtherSundryLiabilitiesNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.facebook.com/role/CommitmentsandContingenciesNarrativeDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - meta_CommitmentsAndContingenciesDisclosureTable
    - srt_LitigationCaseAxis
      - srt_LitigationCaseTypeDomain
    - meta_CommitmentsAndContingenciesDisclosureLineItems
      - us-gaap_ContractualObligation
      - us-gaap_LongTermPurchaseCommitmentAmount
      - us-gaap_LongtermPurchaseCommitmentPeriod
      - us-gaap_LitigationSettlementAmountAwardedToOtherParty
      - us-gaap_LossContingencyAccrualPayments
      - us-gaap_LossContingencyAccrualAtCarryingValue
      - us-gaap_LossContingencyNewClaimsFiledNumber
      - meta_LossContingencyNumberOfStatesThatHaveFiledPublicNuisanceClaims

### http://www.facebook.com/role/CommitmentsandContingenciesContractualCommitmentsDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_ContractualObligationDueInNextTwelveMonths
  - us-gaap_ContractualObligationDueInSecondYear
  - us-gaap_ContractualObligationDueInThirdYear
  - us-gaap_ContractualObligationDueInFourthYear
  - us-gaap_ContractualObligationDueInFifthYear
  - us-gaap_ContractualObligationDueAfterFifthYear
  - us-gaap_ContractualObligation [totalLabel]

### http://www.facebook.com/role/SegmentandGeographicalInformationNarrativeDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_NumberOfReportableSegments

### http://www.facebook.com/role/SegmentandGeographicalInformationScheduleofPropertyandEquipmentDetails

- us-gaap_SegmentsGeographicalAreasAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - us-gaap_NonUsMember

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

