# MSFT 2019 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.microsoft.com/20190630/taxonomy/role/StatementINCOMESTATEMENTS

- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_StatementLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
      - us-gaap_CostOfGoodsAndServicesSold
      - us-gaap_GrossProfit [totalLabel]
      - us-gaap_ResearchAndDevelopmentExpense
      - us-gaap_SellingAndMarketingExpense
      - us-gaap_GeneralAndAdministrativeExpense
      - us-gaap_RestructuringCharges
      - us-gaap_OperatingIncomeLoss [totalLabel]
      - us-gaap_NonoperatingIncomeExpense
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments [totalLabel]
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_NetIncomeLoss [totalLabel]
      - us-gaap_EarningsPerShareAbstract
      - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract

### http://www.microsoft.com/20190630/taxonomy/role/StatementCOMPREHENSIVEINCOMESTATEMENTS

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
    - us-gaap_OtherComprehensiveIncomeLossDerivativesQualifyingAsHedgesNetOfTax
    - us-gaap_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesAdjustmentNetOfTax
    - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
    - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/StatementCASHFLOWSSTATEMENTS

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - msft_DepreciationAmortizationAndOther
  - us-gaap_ShareBasedCompensation
  - msft_GainLossOnInvestmentsAndDerivativeInstruments
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureEARNINGSPERSHARE

- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureOTHERINCOMEEXPENSENET

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_OtherNonoperatingIncomeAndExpenseTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureINCOMETAXES

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureUNEARNEDREVENUE

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueFromContractWithCustomerTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureACCUMULATEDOTHERCOMPREHENSIVEINCOMELOSS

- us-gaap_EquityAbstract
  - us-gaap_ComprehensiveIncomeNoteTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureEARNINGSPERSHARETables

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureOTHERINCOMEEXPENSENETTables

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_StatementTable
    - us-gaap_InvestmentTypeAxis
      - us-gaap_InvestmentTypeCategorizationMember
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfOtherNonoperatingIncomeExpenseTableTextBlock
      - us-gaap_RealizedGainLossOnInvestmentsTableTextBlock
      - us-gaap_GainLossOnInvestmentsTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureINCOMETAXESTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_SummaryOfIncomeTaxContingenciesTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureUNEARNEDREVENUETables

- us-gaap_RevenueFromContractWithCustomerAbstract
  - msft_ContractWithCustomerLiabilityBySegmentTableTextBlock
  - us-gaap_ContractWithCustomerAssetAndLiabilityTableTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureACCUMULATEDOTHERCOMPREHENSIVEINCOMELOSSTables

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfAccumulatedOtherComprehensiveIncomeLossTableTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureBasicAndDilutedEarningsPerShareDetail

- us-gaap_EarningsPerShareBasicAndDilutedAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
  - us-gaap_IncrementalCommonSharesAttributableToShareBasedPaymentArrangements
  - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding [totalLabel]
  - us-gaap_EarningsPerShareAbstract
    - us-gaap_EarningsPerShareBasic
    - us-gaap_EarningsPerShareDiluted

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureComponentsOfOtherIncomeExpenseNetDetail

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_InvestmentIncomeNet
  - us-gaap_InterestExpense
  - us-gaap_GainLossOnInvestments
  - us-gaap_GainLossOnDerivativeInstrumentsNetPretax
  - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_NonoperatingIncomeExpense [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureNetRecognizedGainsLossesOnDebtInvestmentsDetail

- us-gaap_ScheduleOfGainLossOnInvestmentsIncludingMarketableSecuritiesAndInvestmentsHeldAtCostIncomeStatementReportedAmountsSummaryLineItems
  - us-gaap_DebtSecuritiesAvailableForSaleRealizedGain
  - us-gaap_DebtSecuritiesAvailableForSaleRealizedLoss
  - us-gaap_ImpairmentOfInvestments
  - us-gaap_GainLossOnInvestments [totalLabel]
- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_ScheduleOfGainLossOnInvestmentsTable

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureNetRecognizedGainsLossesOnEquityInvestmentsDetail

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_ScheduleOfGainLossOnInvestmentsTable
- us-gaap_ScheduleOfGainLossOnInvestmentsIncludingMarketableSecuritiesAndInvestmentsHeldAtCostIncomeStatementReportedAmountsSummaryLineItems
  - us-gaap_EquitySecuritiesFvNiRealizedGainLoss
  - us-gaap_EquitySecuritiesFvNiUnrealizedGainLoss
  - us-gaap_ImpairmentOfInvestments
  - us-gaap_GainLossOnInvestments [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureGainsLossesOnFairValueHedgesAndRelatedHedgedItemsDetail

- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedgesDetail

- us-gaap_DerivativeInstrumentsGainLossRecognizedInIncomeIneffectivePortionAndAmountExcludedFromEffectivenessTestingNetAbstract
  - us-gaap_DerivativeInstrumentsGainLossRecognizedInIncomeIneffectivePortionAndAmountExcludedFromEffectivenessTestingNet
- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - us-gaap_HedgingDesignationAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedgesParentheticalDetail

- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - us-gaap_HedgingDesignationAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureNonDesignatedDerivativeGainsLossesDetail

- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureRevenueAndOperatingLossAttributableToAcquireeSinceDateOfAcquisitionDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationProFormaInformationRevenueOfAcquireeSinceAcquisitionDateActual
      - us-gaap_BusinessCombinationProFormaInformationEarningsOrLossOfAcquireeSinceAcquisitionDateActual

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureIncomeTaxesAdditionalInformationDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - msft_IncomeTaxesTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_IndefiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_IndefiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_TaxPeriodAxis
      - us-gaap_TaxPeriodDomain
    - msft_IncomeTaxesLineItems
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_IncomeTaxReconciliationRepatriationOfForeignEarnings
      - us-gaap_IncomeTaxReconciliationChangeInEnactedTaxRate
      - msft_ForeignEarningsTaxedAtRatesLowerThanUsRate
      - us-gaap_OperatingLossCarryforwards
      - msft_OperatingLossCarryforwardsExpirationYear
      - us-gaap_IncomeTaxesPaidNet
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestExpense

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureProvisionForIncomeTaxesDetail

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

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureIncomeBeforeIncomeTaxesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureDifferenceBetweenIncomeTaxesComputedAtFederalStatutoryRateAndProvisionForIncomeTaxesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
  - us-gaap_EffectiveIncomeTaxRateContinuingOperationsTaxRateReconciliationAbstract
    - us-gaap_EffectiveIncomeTaxRateReconciliationForeignIncomeTaxRateDifferential
    - msft_EffectiveIncomeTaxRateReconciliationTaxCutsAndJobsActPercent
    - msft_EffectiveIncomeTaxRateReconciliationPhoneBusinessGainsLosses
    - msft_EffectiveIncomeTaxRateReconciliationIntangiblePropertyTransfers
    - msft_EffectiveIncomeTaxRateReconciliationForeignDerivedIntangibleIncomeDeduction
    - us-gaap_EffectiveIncomeTaxRateReconciliationTaxCreditsResearch
    - msft_EffectiveIncomeTaxRateReconciliationDeductionsExcessTaxBenefitsStockBasedCompensation
    - msft_EffectiveIncomeTaxRateReconciliationInterestIncomeExpense
    - us-gaap_EffectiveIncomeTaxRateReconciliationOtherAdjustments
    - us-gaap_EffectiveIncomeTaxRateContinuingOperations [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureDeferredIncomeTaxAssetsAndLiabilitiesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - msft_ScheduleOfDeferredIncomeTaxAssetsAndLiabilitiesTable
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - msft_ScheduleOfDeferredIncomeTaxAssetsAndLiabilitiesLineItems
      - us-gaap_DeferredTaxAssetsNetAbstract
      - us-gaap_DeferredTaxLiabilitiesAbstract
      - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]
      - us-gaap_DeferredTaxAssetsLiabilitiesNetNoncurrent
      - us-gaap_DeferredTaxLiabilitiesNoncurrent

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureChangesInGrossUnrecognizedTaxBenefitsRelatedToUncertainTaxPositionsDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_UnrecognizedTaxBenefits
  - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsReductionsResultingFromLapseOfApplicableStatuteOfLimitations
  - us-gaap_UnrecognizedTaxBenefits

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureIncomeTaxesAdditionalInformationRegardingExaminationsDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxExaminationTable
    - us-gaap_IncomeTaxAuthorityNameAxis
      - us-gaap_IncomeTaxAuthorityNameDomain
    - us-gaap_TaxPeriodAxis
      - us-gaap_TaxPeriodDomain
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_IncomeTaxExaminationLineItems
      - us-gaap_IncomeTaxExaminationYearUnderExamination
      - us-gaap_OpenTaxYear
      - msft_IncomeTaxExaminationYearExpectedToBeUnderExamination

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureUnearnedRevenueBySegmentDetail

- us-gaap_RevenueFromContractWithCustomerAbstract
  - msft_ContractWithCustomerLiabilityTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - msft_ContractWithCustomerLiabilityLineItems
      - us-gaap_ContractWithCustomerLiability

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureChangesInUnearnedRevenueDetail

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_ContractWithCustomerLiability
  - msft_ContractWithCustomerLiabilityRevenueDeferred
  - us-gaap_ContractWithCustomerLiabilityRevenueRecognized
  - us-gaap_ContractWithCustomerLiability

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureUnearnedRevenueAdditionalInformationDetail

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueRemainingPerformanceObligation

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureUnearnedRevenueRemainingPerformanceObligationAdditionalInformationDetail

- us-gaap_RevenueFromContractWithCustomerAbstract
  - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionTable
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionStartDateAxis
    - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionLineItems
      - us-gaap_RevenueRemainingPerformanceObligationPercentage
      - us-gaap_RevenueRemainingPerformanceObligationExpectedTimingOfSatisfactionPeriod1

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureSummaryOfChangesInAccumulatedOtherComprehensiveIncomeLossByComponentDetail

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossTable
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_IncomeStatementLocationAxis
      - us-gaap_IncomeStatementLocationDomain
    - us-gaap_AccumulatedOtherComprehensiveIncomeLossLineItems
      - us-gaap_StockholdersEquity
      - us-gaap_OciBeforeReclassificationsNetOfTaxAttributableToParent
      - us-gaap_ReclassificationFromAociCurrentPeriodBeforeTaxAttributableToParent
      - us-gaap_ReclassificationFromAociCurrentPeriodTax
      - us-gaap_ReclassificationFromAociCurrentPeriodNetOfTaxAttributableToParent
      - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent
      - us-gaap_NewAccountingPronouncementOrChangeInAccountingPrincipleEffectOfAdoptionQuantification
      - us-gaap_StockholdersEquity

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureSummaryOfChangesInAccumulatedOtherComprehensiveIncomeLossByComponentParentheticalDetail

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossTable
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_AccumulatedOtherComprehensiveIncomeLossLineItems
      - us-gaap_OtherComprehensiveIncomeLossBeforeReclassificationsTax
      - us-gaap_OtherComprehensiveIncomeLossTaxPortionAttributableToParent1

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureStockBasedCompensationExpenseAndRelatedIncomeTaxBenefitsDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_AllocatedShareBasedCompensationExpense
  - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureSegmentRevenueDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureOperatingIncomeLossBySegmentDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - srt_ConsolidationItemsAxis
      - srt_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_OperatingIncomeLoss

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureRevenueClassifiedByMajorGeographicAreasDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
    - srt_StatementGeographicalAxis
      - srt_SegmentGeographicalDomain
    - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureRevenueClassifiedBySignificantProductAndServiceOfferingsDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
    - srt_ProductOrServiceAxis
      - srt_ProductsAndServicesDomain
    - us-gaap_EntityWideInformationRevenueFromExternalCustomerLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureRevenueClassifiedBySignificantProductAndServiceOfferingsParentheticalDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
    - msft_ProductsOrServicesSecondaryCategorizationAxis
      - msft_ProductsOrServicesNameSecondaryCategorizationDomain
    - us-gaap_EntityWideInformationRevenueFromExternalCustomerLineItems
      - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureLongLivedAssetsExcludingFinancialInstrumentsAndTaxAssetsClassifiedByLocationOfControllingStatutoryCompanyDetail

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - srt_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureQuarterlyInformationUnauditedParentheticalDetail

- us-gaap_IncomeTaxAuthorityAxis
  - us-gaap_IncomeTaxAuthorityDomain
    - msft_TaxCutsAndJobsActMember

## 资产负债表结构 (Balance Sheet Structure)

### http://www.microsoft.com/20190630/taxonomy/role/StatementBALANCESHEETS

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_AssetsAbstract
    - us-gaap_AssetsCurrentAbstract
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_ShortTermInvestments
      - us-gaap_CashCashEquivalentsAndShortTermInvestments [totalLabel]
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_InventoryNet
      - us-gaap_OtherAssetsCurrent
      - us-gaap_AssetsCurrent [totalLabel]
    - us-gaap_PropertyPlantAndEquipmentNet
    - us-gaap_OperatingLeaseRightOfUseAsset
    - us-gaap_LongTermInvestments
    - us-gaap_Goodwill
    - us-gaap_FiniteLivedIntangibleAssetsNet
    - us-gaap_OtherAssetsNoncurrent
    - us-gaap_Assets [totalLabel]
  - us-gaap_LiabilitiesAndStockholdersEquityAbstract
    - us-gaap_LiabilitiesCurrentAbstract
      - us-gaap_AccountsPayableCurrent
      - us-gaap_LongTermDebtCurrent
      - us-gaap_EmployeeRelatedLiabilitiesCurrent
      - us-gaap_AccruedIncomeTaxesCurrent
      - us-gaap_ContractWithCustomerLiabilityCurrent
      - us-gaap_OtherLiabilitiesCurrent
      - us-gaap_LiabilitiesCurrent [totalLabel]
    - us-gaap_LongTermDebtNoncurrent
    - us-gaap_AccruedIncomeTaxesNoncurrent
    - us-gaap_ContractWithCustomerLiabilityNoncurrent
    - us-gaap_DeferredTaxLiabilitiesNoncurrent
    - us-gaap_OperatingLeaseLiabilityNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent
    - us-gaap_Liabilities [totalLabel]
    - us-gaap_CommitmentsAndContingencies
    - us-gaap_StockholdersEquityAbstract
      - us-gaap_CommonStocksIncludingAdditionalPaidInCapital
      - us-gaap_RetainedEarningsAccumulatedDeficit
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
      - us-gaap_StockholdersEquity [totalLabel]
    - us-gaap_LiabilitiesAndStockholdersEquity [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/StatementBALANCESHEETSParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_AllowanceForDoubtfulAccountsReceivableCurrent
  - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_CommonStockSharesOutstanding

### http://www.microsoft.com/20190630/taxonomy/role/StatementCASHFLOWSSTATEMENTS

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetIncomeLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInThreeMonthsOrLess
    - us-gaap_ProceedsFromDebtMaturingInMoreThanThreeMonths
    - us-gaap_RepaymentsOfDebtMaturingInMoreThanThreeMonths
    - us-gaap_ProceedsFromIssuanceOfCommonStock
    - us-gaap_PaymentsForRepurchaseOfCommonStock
    - us-gaap_PaymentsOfDividendsCommonStock
    - us-gaap_ProceedsFromPaymentsForOtherFinancingActivities
    - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
    - msft_AcquisitionsNetOfCashAcquiredAndPurchasesOfIntangibleAndOtherAssets
    - us-gaap_PaymentsToAcquireInvestments
    - us-gaap_ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities
    - msft_ProceedsFromInvestments
    - us-gaap_IncreaseDecreaseInCollateralHeldUnderSecuritiesLending
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_EffectOfExchangeRateOnCashAndCashEquivalents
  - us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease [totalLabel]
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_CashAndCashEquivalentsAtCarryingValue

### http://www.microsoft.com/20190630/taxonomy/role/StatementSTOCKHOLDERSEQUITYSTATEMENTS

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockIncludingAdditionalPaidInCapitalMember
    - us-gaap_RetainedEarningsMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureINVESTMENTS

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_InvestmentsInDebtAndEquityInstrumentsCashAndCashEquivalentsUnrealizedAndRealizedGainsLossesTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureGOODWILL

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillDisclosureTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureINTANGIBLEASSETS

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_IntangibleAssetsDisclosureTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureSTOCKHOLDERSEQUITY

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureINVESTMENTSTables

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - msft_ScheduleOfCashCashEquivalentsAndInvestmentsTableTextBlock
  - us-gaap_ScheduleOfUnrealizedLossOnInvestmentsTableTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureGOODWILLTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureINTANGIBLEASSETSTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTableTextBlock
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetsByMajorClassTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureSTOCKHOLDERSEQUITYTables

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfCommonStockOutstandingRollForwardTableTextBlock
  - msft_ShareRepurchaseProgramDisclosureTableTextBlock
  - us-gaap_DividendsDeclaredTableTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureInvestmentComponentsDetail

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - msft_CashCashEquivalentsAndInvestmentsTable
    - us-gaap_FairValueByAssetClassAxis
      - us-gaap_FairValueAssetsMeasuredOnRecurringBasisUnobservableInputReconciliationByAssetClassDomain
    - us-gaap_InvestmentTypeAxis
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
    - us-gaap_MeasurementInputTypeAxis
    - msft_CashCashEquivalentsAndInvestmentsLineItems
      - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis [totalLabel]
      - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
      - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
      - us-gaap_AvailableForSaleSecuritiesDebtSecurities
      - us-gaap_EquitySecuritiesFvNi
      - us-gaap_Cash
      - us-gaap_DerivativeAssets
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_ShortTermInvestments
      - us-gaap_LongTermInvestments
      - msft_CashCashEquivalentsAndInvestments [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureInvestmentsAdditionalInformationDetail

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - invest_InvestmentTable

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureUnrealizedLossesOnDebtInvestmentsDetail

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - msft_InvestmentsUnrealizedLossPositionTable

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureDebtInvestmentMaturitiesDetail

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAmortizedCostBasisRollingMaturityAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesFairValueRollingMaturityAbstract

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedgesDetail

- msft_GainLossOnCashFlowHedgeEffectivenessNetAbstract
  - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodNetOfTax
  - us-gaap_ForeignCurrencyCashFlowHedgeGainLossReclassifiedToEarningsNet

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureMajorClassesOfAssetsAndLiabilitiesAllocatedPurchasePriceDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCashAndEquivalents
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCurrentAssetsMarketableSecurities
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCurrentAssetsOther
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedPropertyPlantAndEquipment
      - msft_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCashCashEquivalentsAndShortTermInvestments
      - us-gaap_Goodwill
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles
      - msft_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedOtherAssets
      - msft_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCurrentLiabilitiesShortTermDebt
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCurrentLiabilitiesOther
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedDeferredTaxLiabilitiesNoncurrent
      - msft_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedOtherLiabilitiesNet
      - msft_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedOtherLiabilities
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredGoodwillAndLiabilitiesAssumedNet [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureAcquiredIntangibleAssetsDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAcquiredAsPartOfBusinessCombinationTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_AcquiredFiniteLivedIntangibleAssetsLineItems
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureMajorClassesOfAssetsAndLiabilitiesAllocatedPurchasePriceParentheticalDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionPurchasePriceAllocationGoodwillExpectedTaxDeductibleAmount
      - us-gaap_DebtInstrumentFaceAmount

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureCarryingAmountOfGoodwillDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTable

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureCarryingAmountOfGoodwillParentheticalDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTable

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureGoodwillAdditionalInformationDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillImpairmentLoss
  - us-gaap_GoodwillImpairedAccumulatedImpairmentLoss

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureFiniteLivedIntangibleAssetsDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureFiniteLivedIntangibleAssetsParentheticalDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureIntangibleAssetsAcquiredDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetByMajorClassTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_AcquiredFiniteLivedIntangibleAssetsLineItems
      - us-gaap_FinitelivedIntangibleAssetsAcquired1
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureIntangibleAssetsAdditionalInformationDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_AmortizationOfIntangibleAssets

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureEstimatedFutureAmortizationExpenseRelatedToIntangibleAssetsDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureSupplementalCashFlowInformationRelatedToLeasesDetail

- msft_CashPaidForAmountsIncludedInMeasurementOfLeaseLiabilitiesAbstract
  - us-gaap_OperatingLeasePayments
  - us-gaap_FinanceLeaseInterestPaymentOnLiability
  - us-gaap_FinanceLeasePrincipalPayments
- msft_RightOfUseAssetsObtainedInExchangeForLeaseObligationsAbstract
  - us-gaap_RightOfUseAssetObtainedInExchangeForOperatingLeaseLiability
  - us-gaap_RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureSupplementalBalanceSheetInformationRelatedToLeasesDetail

- us-gaap_LeasesAbstract
  - msft_LeasesTable
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_LeaseArrangementTypeAxis
      - us-gaap_LeaseArrangementTypeDomain
    - msft_LeasesLineItems
      - us-gaap_LeasesOperatingAbstract
      - msft_FinanceLeaseAbstract
      - msft_WeightedAverageRemainingLeaseTermAbstract
      - msft_WeightedAverageDiscountRateAbstract

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureSharesOfCommonStockOutstandingDetail

- us-gaap_EquityAbstract
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockIssuedDuringPeriodSharesNewIssues
  - us-gaap_StockRepurchasedDuringPeriodShares
  - us-gaap_CommonStockSharesOutstanding

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureStockholdersEquityAdditionalInformationDetail

- us-gaap_StatementOfStockholdersEquityAbstract
  - msft_ShareRepurchasesTable

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureShareRepurchasesDetail

- us-gaap_EquityAbstract
  - msft_ShareRepurchasesTable

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureDividendsDeclaredDetail

- us-gaap_EquityAbstract
  - us-gaap_DividendsPayableDateDeclaredDayMonthAndYear
  - us-gaap_DividendsPayableDateOfRecordDayMonthAndYear
  - us-gaap_DividendPayableDateToBePaidDayMonthAndYear
  - us-gaap_CommonStockDividendsPerShareDeclared
  - us-gaap_DividendsCommonStockCash

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureStockPlanActivityDetail

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

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureLongLivedAssetsExcludingFinancialInstrumentsAndTaxAssetsClassifiedByLocationOfControllingStatutoryCompanyDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- srt_StatementGeographicalAxis
  - srt_SegmentGeographicalDomain
    - country_US
    - country_IE
    - msft_OtherCountriesMember

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureQuarterlyInformationUnauditedParentheticalDetail

- us-gaap_IndefiniteLivedIntangibleAssetsByMajorClassAxis
  - us-gaap_IndefiniteLivedIntangibleAssetsMajorClassNameDomain
    - msft_TransferOfIntangiblePropertiesMember

## 现金流量表结构 (Cash Flow Structure)

### http://www.microsoft.com/20190630/taxonomy/role/StatementCASHFLOWSSTATEMENTS

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInInventories
  - us-gaap_IncreaseDecreaseInOtherCurrentAssets
  - us-gaap_IncreaseDecreaseInOtherNoncurrentAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInContractWithCustomerLiability
  - us-gaap_IncreaseDecreaseInAccruedIncomeTaxesPayable
  - us-gaap_IncreaseDecreaseInOtherCurrentLiabilities
  - us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedgesDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
- us-gaap_HedgingDesignationAxis
  - us-gaap_HedgingDesignationDomain
    - us-gaap_DesignatedAsHedgingInstrumentMember
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ForeignExchangeContractMember
- us-gaap_DerivativeInstrumentsGainLossLineItems
  - msft_GainLossOnCashFlowHedgeEffectivenessNetAbstract
  - us-gaap_DerivativeInstrumentsGainLossRecognizedInIncomeIneffectivePortionAndAmountExcludedFromEffectivenessTestingNetAbstract

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedgesParentheticalDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
- us-gaap_HedgingDesignationAxis
  - us-gaap_HedgingDesignationDomain
    - us-gaap_DesignatedAsHedgingInstrumentMember
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ForeignExchangeContractMember
- us-gaap_DerivativeInstrumentsGainLossLineItems
  - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodTax

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureSupplementalCashFlowInformationRelatedToLeasesDetail

- us-gaap_LeasesAbstract
  - msft_CashPaidForAmountsIncludedInMeasurementOfLeaseLiabilitiesAbstract
  - msft_RightOfUseAssetsObtainedInExchangeForLeaseObligationsAbstract

## 股东权益结构 (Equity Structure)

### http://www.microsoft.com/20190630/taxonomy/role/StatementSTOCKHOLDERSEQUITYSTATEMENTS

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_StockholdersEquity
    - us-gaap_StockIssuedDuringPeriodValueNewIssues
    - us-gaap_NetIncomeLoss
    - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent
    - us-gaap_DividendsCommonStockCash
    - us-gaap_StockRepurchasedDuringPeriodValue
    - us-gaap_NewAccountingPronouncementOrChangeInAccountingPrincipleEffectOfAdoptionQuantification
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
    - us-gaap_StockholdersEquityOther
    - us-gaap_StockholdersEquity
    - us-gaap_CommonStockDividendsPerShareDeclared

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureEMPLOYEESTOCKANDSAVINGSPLANS

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_CompensationAndEmployeeBenefitPlansTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureEMPLOYEESTOCKANDSAVINGSPLANSTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfCompensationCostForShareBasedPaymentArrangementsAllocationOfShareBasedCompensationCostsByPlanTableTextBlock
  - msft_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsMethodUsedTableTextBlock
  - us-gaap_DisclosureOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTextBlock
  - us-gaap_ScheduleOfShareBasedCompensationEmployeeStockPurchasePlanActivityTableTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureNetRecognizedGainsLossesOnEquityInvestmentsDetail

- us-gaap_ScheduleOfGainLossOnInvestmentsTable
  - us-gaap_InvestmentTypeAxis
    - us-gaap_InvestmentTypeCategorizationMember
      - us-gaap_EquitySecuritiesMember
  - us-gaap_ScheduleOfGainLossOnInvestmentsIncludingMarketableSecuritiesAndInvestmentsHeldAtCostIncomeStatementReportedAmountsSummaryLineItems

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureStockholdersEquityAdditionalInformationDetail

- msft_ShareRepurchasesTable
  - us-gaap_ShareRepurchaseProgramAxis
    - us-gaap_ShareRepurchaseProgramDomain
      - msft_ShareRepurchaseProgramTwentyThirteenMember
      - msft_ShareRepurchaseProgramTwentySixteenMember
  - msft_ShareRepurchasesLineItems
    - us-gaap_StockRepurchaseProgramAuthorizedAmount1
    - us-gaap_StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1
    - us-gaap_PaymentsRelatedToTaxWithholdingForShareBasedCompensation

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureShareRepurchasesDetail

- msft_ShareRepurchasesTable
  - us-gaap_ShareRepurchaseProgramAxis
    - us-gaap_ShareRepurchaseProgramDomain
      - msft_ShareRepurchaseProgramTwentySixteenMember
  - msft_ShareRepurchasesLineItems
    - us-gaap_StockRepurchasedDuringPeriodShares
    - us-gaap_StockRepurchasedDuringPeriodValue

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureEmployeeStockAndSavingsPlansAdditionalInformationDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - msft_CompensationRelatedCostsDisclosureTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PlanNameAxis
      - us-gaap_PlanNameDomain
    - us-gaap_DeferredCompensationArrangementWithIndividualPostretirementBenefitsByTypeOfDeferredCompensationAxis
      - us-gaap_OtherPostretirementBenefitsIndividualContractsTypeOfDeferredCompensationDomain
    - msft_CompensationRelatedCostsDisclosureLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardPurchasePriceOfCommonStockPercent
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardMaximumEmployeeSubscriptionRate
      - us-gaap_DefinedContributionPlanEmployerMatchingContributionPercentOfMatch
      - us-gaap_DefinedContributionPlanEmployerMatchingContributionPercent
      - us-gaap_DefinedContributionPlanCostRecognized

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureAssumptionsUsedInEstimatingFairValueOfStockAwardGrantsDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - msft_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsMethodUsedTable
    - srt_RangeAxis
      - srt_RangeMember
    - msft_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsMethodUsedLineItems
      - msft_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsExpectedDividendsPerShare
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsRiskFreeInterestRateMinimum
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsRiskFreeInterestRateMaximum

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureStockPlanActivityDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureStockPlanActivityParentheticalDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureEmployeePurchasedSharesDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockPurchasePlans
  - msft_StockIssuedEmployeeStockPurchasePlanAveragePricePerShare

## 其他结构 (Other Structure)

### http://www.microsoft.com/20190630/taxonomy/role/DocumentDocumentAndEntityInformation

- msft_DocumentAndEntityInformationAbstract
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
  - dei_EntityListingParValuePerShare
  - dei_EntityCommonStockSharesOutstanding
  - dei_EntityPublicFloat
  - dei_EntityTaxIdentificationNumber
  - dei_EntityShellCompany
  - dei_EntityAddressStateOrProvince
  - dei_EntityAddressCountry

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureACCOUNTINGPOLICIES

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_SignificantAccountingPoliciesTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureDERIVATIVES

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureINVENTORIES

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryDisclosureTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosurePROPERTYANDEQUIPMENT

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureBUSINESSCOMBINATIONS

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_MergersAcquisitionsAndDispositionsDisclosuresTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureDEBT

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureRESTRUCTURINGCHARGES

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_RestructuringAndRelatedActivitiesDisclosureTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureLEASES

- us-gaap_LeasesAbstract
  - us-gaap_LeasesOfLesseeDisclosureTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureCONTINGENCIES

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_LegalMattersAndContingenciesTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureSEGMENTINFORMATIONANDGEOGRAPHICDATA

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureQUARTERLYINFORMATIONUNAUDITED

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_QuarterlyFinancialInformationTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureACCOUNTINGPOLICIESPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BasisOfAccountingPolicyPolicyTextBlock
  - us-gaap_ConsolidationPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_RevenueFromContractWithCustomerPolicyTextBlock
  - us-gaap_CostOfSalesPolicyTextBlock
  - us-gaap_StandardProductWarrantyPolicy
  - us-gaap_ResearchDevelopmentAndComputerSoftwarePolicyTextBlock
  - msft_SellingAndMarketingPolicyTextBlock
  - us-gaap_ShareBasedCompensationOptionAndIncentivePlansPolicy
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_InvestmentPolicyTextBlock
  - us-gaap_DerivativesPolicyTextBlock
  - us-gaap_FairValueOfFinancialInstrumentsPolicy
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_LesseeLeasesPolicyTextBlock
  - us-gaap_GoodwillAndIntangibleAssetsGoodwillPolicy
  - us-gaap_IntangibleAssetsFiniteLivedPolicy
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock
  - us-gaap_EarningsPerSharePolicyTextBlock
  - us-gaap_SegmentReportingPolicyPolicyTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureACCOUNTINGPOLICIESTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfCreditLossesRelatedToFinancingReceivablesCurrentAndNoncurrentTableTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureDERIVATIVESTables

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_StatementTable
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfNotionalAmountsOfOutstandingDerivativePositionsTableTextBlock
      - us-gaap_ScheduleOfDerivativeInstrumentsInStatementOfFinancialPositionFairValueTextBlock
      - us-gaap_ScheduleOfDerivativeInstrumentsGainLossInStatementOfFinancialPerformanceTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureINVENTORIESTables

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_ScheduleOfInventoryCurrentTableTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosurePROPERTYANDEQUIPMENTTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureBUSINESSCOMBINATIONSTables

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_StatementTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTextBlock
      - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetsByMajorClassTextBlock
      - msft_RevenueAndOperatingLossAttributableToAcquireeSinceAcquisitionDateTableTextBlock
      - us-gaap_BusinessAcquisitionProFormaInformationTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureDEBTTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtInstrumentsTextBlock
  - us-gaap_ScheduleOfMaturitiesOfLongTermDebtTableTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureLEASESTables

- us-gaap_LeasesAbstract
  - us-gaap_LeaseCostTableTextBlock
  - msft_ScheduleOfSupplementalCashFlowInformationRelatedToLeasesTableTextBlock
  - msft_ScheduleOfSupplementalBalanceSheetInformationRelatedToLeasesTableTextBlock
  - msft_ScheduleOfMaturitiesOfOperatingAndFinanceLeasesLiabilitiesTableTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureSEGMENTINFORMATIONANDGEOGRAPHICDATATables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTextBlock
  - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTextBlock
  - us-gaap_RevenueFromExternalCustomersByGeographicAreasTableTextBlock
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTextBlock
  - us-gaap_LongLivedAssetsByGeographicAreasTableTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureQUARTERLYINFORMATIONUNAUDITEDTables

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_ScheduleOfQuarterlyFinancialInformationTableTextBlock

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureAccountingPoliciesAdditionalInformationDetail

- us-gaap_AccountingPoliciesAbstract
  - msft_SignificantAccountingPoliciesTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - msft_SignificantAccountingPoliciesLineItems
      - us-gaap_AccountsReceivableNetNoncurrent
      - us-gaap_RevenuePerformanceObligationDescriptionOfPaymentTerms
      - us-gaap_AdvertisingExpense
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - us-gaap_RetainedEarningsAccumulatedDeficit
      - us-gaap_DeferredTaxAssetsNetNoncurrent
      - us-gaap_DeferredTaxLiabilitiesNoncurrent
      - us-gaap_OtherAssetsCurrent

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureAllowanceForDoubtfulAccountsDetail

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - srt_ValuationAndQualifyingAccountsDisclosureTable
    - us-gaap_ValuationAllowancesAndReservesTypeAxis
      - us-gaap_ValuationAllowancesAndReservesDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - srt_ValuationAndQualifyingAccountsDisclosureLineItems
      - us-gaap_ValuationAllowancesAndReservesBalance
      - msft_ValuationAllowancesAndReservesChargedToCostsAndOther
      - us-gaap_ValuationAllowancesAndReservesDeductions
      - us-gaap_ValuationAllowancesAndReservesBalance

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureNetRecognizedGainsLossesOnDebtInvestmentsDetail

- us-gaap_ScheduleOfGainLossOnInvestmentsTable
  - us-gaap_InvestmentTypeAxis
    - us-gaap_InvestmentTypeCategorizationMember
      - us-gaap_DebtSecuritiesMember
  - us-gaap_ScheduleOfGainLossOnInvestmentsIncludingMarketableSecuritiesAndInvestmentsHeldAtCostIncomeStatementReportedAmountsSummaryLineItems

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureInvestmentComponentsDetail

- us-gaap_InvestmentTypeAxis
  - us-gaap_InvestmentTypeCategorizationMember
    - us-gaap_CommercialPaperMember
    - us-gaap_CertificatesOfDepositMember
    - us-gaap_USTreasurySecuritiesMember
    - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
    - us-gaap_ForeignGovernmentDebtSecuritiesMember
    - us-gaap_AssetBackedSecuritiesMember
    - us-gaap_CorporateDebtSecuritiesMember
    - us-gaap_USStatesAndPoliticalSubdivisionsMember
    - us-gaap_EquitySecuritiesMember
    - us-gaap_CashMember
    - us-gaap_DerivativeMember
- us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueInputsLevel2Member
    - us-gaap_FairValueInputsLevel1Member
    - us-gaap_FairValueInputsLevel3Member
- us-gaap_MeasurementInputTypeAxis
  - us-gaap_MeasurementInputTypeDomain
    - msft_OtherMeasurementMember

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureInvestmentsAdditionalInformationDetail

- invest_InvestmentTable
  - us-gaap_InvestmentTypeAxis
    - us-gaap_InvestmentTypeCategorizationMember
      - us-gaap_USTreasuryAndGovernmentMember
  - invest_InvestmentLineItems
    - us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueAmount
    - us-gaap_SecuritiesReceivedAsCollateral

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureUnrealizedLossesOnDebtInvestmentsDetail

- msft_InvestmentsUnrealizedLossPositionTable
  - us-gaap_InvestmentTypeAxis
    - us-gaap_InvestmentTypeCategorizationMember
      - us-gaap_USTreasuryAndGovernmentMember
      - us-gaap_ForeignGovernmentDebtSecuritiesMember
      - us-gaap_AssetBackedSecuritiesMember
      - us-gaap_CorporateDebtSecuritiesMember
      - us-gaap_USStatesAndPoliticalSubdivisionsMember
  - msft_InvestmentsUnrealizedLossPositionLineItems
    - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPositionLessThan12Months
    - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPositionLessThan12MonthsAccumulatedLoss
    - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPosition12MonthsOrLonger
    - us-gaap_DebtSecuritiesAvailableForSaleContinuousUnrealizedLossPosition12MonthsOrLongerAccumulatedLoss
    - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPosition [totalLabel]
    - us-gaap_DebtSecuritiesAvailableForSaleUnrealizedLossPositionAccumulatedLoss

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureDebtInvestmentMaturitiesDetail

- us-gaap_AvailableForSaleSecuritiesDebtMaturitiesFairValueRollingMaturityAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesNextRollingTwelveMonthsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearTwoThroughFiveFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearSixThroughTenFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingAfterYearTenFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtSecurities [totalLabel]
- us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAmortizedCostBasisRollingMaturityAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesNextRollingTwelveMonthsAmortizedCostBasis
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearTwoThroughFiveAmortizedCostBasis
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearSixThroughTenAmortizedCostBasis
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingAfterYearTenAmortizedCostBasis
  - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureDerivativesAdditionalInformationDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DerivativeLineItems
      - msft_FinancialInstrumentCovenantMinimumLiquidityRequirement
      - us-gaap_DebtInstrumentCreditRating
      - msft_FinancialInstrumentCovenantMinimumLiquidity
      - us-gaap_DerivativeFairValueOfDerivativeAsset
      - us-gaap_DerivativeFairValueOfDerivativeLiability
      - us-gaap_ForeignCurrencyCashFlowHedgeGainLossToBeReclassifiedDuringNext12Months

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureNotionalAmountsOfOutstandingDerivativeInstrumentsMeasuredInUSDollarEquivalentsDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeTable
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_PositionAxis
      - us-gaap_PositionDomain
    - us-gaap_DerivativeLineItems
      - invest_DerivativeNotionalAmount

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureFairValuesOfDerivativeInstrumentsDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_FairValuesDerivativesBalanceSheetLocationByDerivativeContractTypeByHedgingDesignationTable
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_DerivativesFairValueLineItems
      - us-gaap_DerivativeAssetFairValueGrossAssetIncludingNotSubjectToMasterNettingArrangement
      - us-gaap_DerivativeAssetFairValueGrossLiability
      - us-gaap_DerivativeCollateralRightToReclaimCash
      - us-gaap_DerivativeAssets [totalLabel]
      - us-gaap_DerivativeLiabilityFairValueGrossLiabilityIncludingNotSubjectToMasterNettingArrangement
      - us-gaap_DerivativeLiabilityFairValueGrossAsset
      - us-gaap_DerivativeCollateralObligationToReturnCash
      - us-gaap_DerivativeLiabilities

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureGainsLossesOnFairValueHedgesAndRelatedHedgedItemsDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ForeignExchangeContractMember
    - us-gaap_EquityContractMember
- us-gaap_DerivativeInstrumentsGainLossLineItems
  - us-gaap_ChangeInUnrealizedGainLossOnFairValueHedgingInstruments1
  - us-gaap_ChangeInUnrealizedGainLossOnHedgedItemInFairValueHedge1
  - us-gaap_GainLossOnFairValueHedgeIneffectivenessNet [totalLabel]
  - us-gaap_GainLossFromComponentsExcludedFromAssessmentOfFairValueHedgeEffectivenessNet

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureNonDesignatedDerivativeGainsLossesDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ForeignExchangeContractMember
    - us-gaap_EquityContractMember
    - us-gaap_OtherContractMember
- us-gaap_DerivativeInstrumentsGainLossLineItems
  - us-gaap_DerivativeInstrumentsNotDesignatedAsHedgingInstrumentsGainLossNet

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureComponentsOfInventoriesDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryRawMaterialsNetOfReserves
  - us-gaap_InventoryWorkInProcessNetOfReserves
  - us-gaap_InventoryFinishedGoodsNetOfReserves
  - us-gaap_InventoryNet [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureComponentsOfPropertyAndEquipmentDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_Land
  - us-gaap_BuildingsAndImprovementsGross
  - us-gaap_LeaseholdImprovementsGross
  - msft_ComputerHardwareAndSoftware
  - us-gaap_FurnitureAndFixturesGross
  - us-gaap_PropertyPlantAndEquipmentGross [totalLabel]
  - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
  - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/DisclosurePropertyAndEquipmentAdditionalInformationDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_LongTermPurchaseCommitmentByCategoryOfItemPurchasedAxis
      - us-gaap_LongTermPurchaseCommitmentCategoryOfItemPurchasedDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_Depreciation
      - us-gaap_CommitmentsFairValueDisclosure

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureBusinessCombinationsAdditionalInformationDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionEffectiveDateOfAcquisition1
      - us-gaap_BusinessCombinationConsiderationTransferred1
      - us-gaap_PaymentsToAcquireBusinessesGross
      - us-gaap_BusinessCombinationSeparatelyRecognizedTransactionsAdditionalDisclosuresAcquisitionCosts
      - us-gaap_NumberOfBusinessesAcquired

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureSupplementalConsolidatedFinancialResultsOnUnauditedProFormaBasisAsIfAcquisitionHadBeenConsummatedOnBeginningOfPeriodDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionsProFormaRevenue
      - us-gaap_BusinessAcquisitionsProFormaNetIncomeLoss
      - us-gaap_BusinessAcquisitionProFormaEarningsPerShareDiluted

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureCarryingAmountOfGoodwillDetail

- us-gaap_ScheduleOfGoodwillTable
  - us-gaap_StatementBusinessSegmentsAxis
    - us-gaap_SegmentDomain
      - msft_ProductivityAndBusinessProcessesMember
      - msft_IntelligentCloudMember
      - msft_MorePersonalComputingMember
  - us-gaap_GoodwillLineItems
    - us-gaap_Goodwill
    - us-gaap_GoodwillAcquiredDuringPeriod
    - us-gaap_GoodwillOtherIncreaseDecrease
    - us-gaap_Goodwill

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureCarryingAmountOfGoodwillParentheticalDetail

- us-gaap_ScheduleOfGoodwillTable
  - us-gaap_BusinessAcquisitionAxis
    - us-gaap_BusinessAcquisitionAcquireeDomain
      - msft_GitHubIncMember
  - us-gaap_GoodwillLineItems
    - us-gaap_Goodwill

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureDebtAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_CommercialPaper
  - us-gaap_LongTermDebt
  - us-gaap_LongTermDebtFairValue
  - us-gaap_InterestPaid
  - us-gaap_DebtInstrumentUnamortizedDiscountPremiumAndDebtIssuanceCostsNet

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureLongTermDebtDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentMaturityDate
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureMaturitiesOfLongTermDebtDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive
  - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive
  - us-gaap_DebtInstrumentFaceAmount [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureRestructuringChargesAdditionalInformationDetail

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_ScheduleOfRestructuringAndRelatedCostsTable
    - us-gaap_RestructuringPlanAxis
      - us-gaap_RestructuringPlanDomain
    - us-gaap_RestructuringCostAndReserveAxis
      - us-gaap_TypeOfRestructuringDomain
    - us-gaap_RestructuringCostAndReserveLineItems
      - us-gaap_RestructuringCharges
      - us-gaap_RestructuringAndRelatedActivitiesCompletionDate

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureLeasesAdditionalInformationDetail

- us-gaap_LeasesAbstract
  - msft_LeasesTable
    - srt_RangeAxis
      - srt_RangeMember
    - us-gaap_LeaseArrangementTypeAxis
      - us-gaap_LeaseArrangementTypeDomain
    - msft_LeasesLineItems
      - msft_LesseeOperatingAndFinanceLeasesRemainingLeaseTerm
      - us-gaap_LesseeOperatingLeaseRenewalTerm
      - us-gaap_LesseeFinanceLeaseRenewalTerm1
      - msft_LesseeOperatingAndFinanceLeasesOptionsToTerminateLeasesTerm
      - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceSheetAmount
      - us-gaap_LesseeOperatingLeaseLeaseNotYetCommencedTermOfContract1
      - us-gaap_LesseeFinanceLeaseLeaseNotYetCommencedTermOfContract1

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureComponentsOfLeaseExpenseDetail

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeaseCost
  - us-gaap_FinanceLeaseCostAbstract
    - us-gaap_FinanceLeaseRightOfUseAssetAmortization
    - us-gaap_FinanceLeaseInterestExpense
  - msft_FinanceLeaseCost [totalLabel]

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureMaturitiesOfLeaseLiabilitiesDetail

- us-gaap_LeasesAbstract
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueNextTwelveMonths
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearTwo
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearThree
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearFour
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueYearFive
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDueAfterYearFive
  - us-gaap_LesseeOperatingLeaseLiabilityPaymentsDue [totalLabel]
  - us-gaap_LesseeOperatingLeaseLiabilityUndiscountedExcessAmount
  - us-gaap_OperatingLeaseLiability
  - us-gaap_FinanceLeaseLiabilityPaymentsDueNextTwelveMonths
  - us-gaap_FinanceLeaseLiabilityPaymentsDueYearTwo
  - us-gaap_FinanceLeaseLiabilityPaymentsDueYearThree
  - us-gaap_FinanceLeaseLiabilityPaymentsDueYearFour
  - us-gaap_FinanceLeaseLiabilityPaymentsDueYearFive
  - us-gaap_FinanceLeaseLiabilityPaymentsDueAfterYearFive
  - us-gaap_FinanceLeaseLiabilityPaymentsDue [totalLabel]
  - us-gaap_FinanceLeaseLiabilityUndiscountedExcessAmount
  - us-gaap_FinanceLeaseLiability

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureContingenciesAdditionalInformationDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_LossContingencyAccrualCarryingValueCurrent
  - us-gaap_LossContingencyRangeOfPossibleLossPortionNotAccrued

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureSegmentInformationAndGeographicDataAdditionalInformationDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureOfMajorCustomers

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureQuarterlyInformationUnauditedDetail

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax
  - us-gaap_GrossProfit
  - us-gaap_OperatingIncomeLoss
  - us-gaap_NetIncomeLoss
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.microsoft.com/20190630/taxonomy/role/DisclosureQuarterlyInformationUnauditedParentheticalDetail

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - msft_QuarterlyFinancialInformationTable
    - us-gaap_IncomeTaxAuthorityAxis
    - us-gaap_IndefiniteLivedIntangibleAssetsByMajorClassAxis
    - msft_QuarterlyFinancialInformationLineItems
      - us-gaap_IncomeTaxExpenseBenefit
      - msft_IncreaseDecreaseInNetIncome
      - msft_IncomeTaxExpenseBenefitEffectOnEarningsPerShare

