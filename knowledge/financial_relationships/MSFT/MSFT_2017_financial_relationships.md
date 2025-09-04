# MSFT 2017 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.microsoft.com/20170630/taxonomy/role/StatementINCOMESTATEMENTS

- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_SalesRevenueNetAbstract
      - us-gaap_CostOfRevenueAbstract
      - us-gaap_GrossProfit [totalLabel]
      - us-gaap_ResearchAndDevelopmentExpense
      - us-gaap_SellingAndMarketingExpense
      - us-gaap_GeneralAndAdministrativeExpense
      - msft_ImpairmentIntegrationAndRestructuringExpenses
      - us-gaap_OperatingIncomeLoss [totalLabel]
      - us-gaap_NonoperatingIncomeExpense
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments [totalLabel]
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_NetIncomeLoss [totalLabel]
      - us-gaap_EarningsPerShareAbstract
      - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
      - us-gaap_CommonStockDividendsPerShareDeclared

### http://www.microsoft.com/20170630/taxonomy/role/StatementCOMPREHENSIVEINCOMESTATEMENTS

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_NetIncomeLoss
      - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
      - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/StatementCOMPREHENSIVEINCOMESTATEMENTSParenthetical

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_OtherComprehensiveIncomeLossDerivativesQualifyingAsHedgesTax
      - us-gaap_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesTax
      - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentTax

### http://www.microsoft.com/20170630/taxonomy/role/StatementCASHFLOWSSTATEMENTS

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_AssetImpairmentCharges
  - msft_DepreciationAmortizationAndOther
  - us-gaap_ShareBasedCompensation
  - msft_GainLossOnInvestmentsAndDerivativeInstruments
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_IncreaseDecreaseInDeferredRevenue
  - us-gaap_RecognitionOfDeferredRevenue
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureEARNINGSPERSHARE

- us-gaap_EarningsPerShareAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_EarningsPerShareTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureOTHERINCOMEEXPENSENET

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_OtherNonoperatingIncomeAndExpenseTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureINCOMETAXES

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureUNEARNEDREVENUE

- us-gaap_DeferredRevenueDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_DeferredRevenueDisclosureTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureACCUMULATEDOTHERCOMPREHENSIVEINCOME

- us-gaap_EquityAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ComprehensiveIncomeNoteTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureEARNINGSPERSHARETables

- us-gaap_EarningsPerShareAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureOTHERINCOMEEXPENSENETTables

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfOtherNonoperatingIncomeExpenseTableTextBlock
      - us-gaap_RealizedGainLossOnInvestmentsTableTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureINCOMETAXESTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
      - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
      - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
      - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
      - us-gaap_SummaryOfIncomeTaxContingenciesTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureUNEARNEDREVENUETables

- us-gaap_DeferredRevenueDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - msft_DeferredRevenueBySegmentTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureACCUMULATEDOTHERCOMPREHENSIVEINCOMETables

- us-gaap_EquityAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfAccumulatedOtherComprehensiveIncomeLossTableTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureAccountingPoliciesAdditionalInformationDetail

- us-gaap_DeferredRevenueArrangementTypeAxis
  - us-gaap_DeferredRevenueArrangementTypeDomain
    - msft_WindowsTenDeferralMember

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureExpectedImpactsOfAdoptionOfStandardsRelatedToRevenueRecognitionAndLeasesToReportedResultsDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NewAccountingPronouncementsOrChangeInAccountingPrincipleTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_NewAccountingPronouncementsOrChangeInAccountingPrincipleLineItems
      - us-gaap_IncomeStatementAbstract
      - us-gaap_StatementOfFinancialPositionAbstract

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureBasicAndDilutedEarningsPerShareDetail

- us-gaap_EarningsPerShareBasicAndDilutedAbstract
  - msft_ScheduleOfEarningsPerShareBasicAndDilutedByCommonClassTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - msft_ScheduleOfEarningsPerShareBasicAndDilutedByCommonClassLineItems
      - us-gaap_NetIncomeLoss
      - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
      - us-gaap_IncrementalCommonSharesAttributableToShareBasedPaymentArrangements
      - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding [totalLabel]
      - us-gaap_EarningsPerShareAbstract

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureComponentsOfOtherIncomeExpenseNetDetail

- us-gaap_OtherIncomeAndExpensesAbstract
  - msft_OtherIncomeExpenseTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ComponentOfOtherIncomeNonoperatingLineItems
      - us-gaap_InvestmentIncomeNet
      - us-gaap_InterestExpense
      - us-gaap_GainLossOnInvestments
      - us-gaap_GainLossOnDerivativeInstrumentsNetPretax
      - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
      - us-gaap_OtherNonoperatingIncomeExpense
      - us-gaap_NonoperatingIncomeExpense [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureNetRecognizedGainsLossesOnInvestmentsDetail

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_ScheduleOfGainLossOnInvestmentsTable
- us-gaap_ScheduleOfGainLossOnInvestmentsIncludingMarketableSecuritiesAndInvestmentsHeldAtCostIncomeStatementReportedAmountsSummaryLineItems
  - us-gaap_MarketableSecuritiesRealizedGainLossOtherThanTemporaryImpairmentsAmount
  - us-gaap_AvailableForSaleSecuritiesGrossRealizedGains
  - us-gaap_AvailableForSaleSecuritiesGrossRealizedLosses
  - us-gaap_GainLossOnInvestments [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureGainsLossesOnFairValueHedgesAndRelatedHedgedItemsDetail

- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - dei_LegalEntityAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedgesDetail

- us-gaap_DerivativeInstrumentsGainLossRecognizedInIncomeIneffectivePortionAndAmountExcludedFromEffectivenessTestingNetAbstract
  - us-gaap_DerivativeInstrumentsGainLossRecognizedInIncomeIneffectivePortionAndAmountExcludedFromEffectivenessTestingNet
- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - dei_LegalEntityAxis
  - us-gaap_HedgingDesignationAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedgesParentheticalDetail

- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - dei_LegalEntityAxis
  - us-gaap_HedgingDesignationAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureNonDesignatedDerivativeGainsLossesDetail

- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - dei_LegalEntityAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureRevenueAndOperatingLossAttributableToAcquireeSinceDateOfAcquisitionDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationProFormaInformationRevenueOfAcquireeSinceAcquisitionDateActual
      - us-gaap_BusinessCombinationProFormaInformationEarningsOrLossOfAcquireeSinceAcquisitionDateActual

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureProvisionForIncomeTaxesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - msft_ReconciliationOfProvisionOfIncomeTaxesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - msft_ReconciliationOfProvisionOfIncomeTaxesLineItems
      - us-gaap_CurrentIncomeTaxExpenseBenefitContinuingOperationsAbstract
      - us-gaap_CurrentIncomeTaxExpenseBenefit [totalLabel]
      - us-gaap_DeferredIncomeTaxExpenseBenefitContinuingOperationsAbstract
      - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureIncomeTaxesAdditionalInformationDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - msft_IncomeTaxesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_IncomeStatementLocationAxis
      - us-gaap_IncomeStatementLocationDomain
    - us-gaap_DeferredRevenueArrangementTypeAxis
      - us-gaap_DeferredRevenueArrangementTypeDomain
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - msft_IncomeTaxesLineItems
      - us-gaap_DeferredFederalStateAndLocalTaxExpenseBenefit
      - us-gaap_DeferredForeignIncomeTaxExpenseBenefit
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
      - msft_ForeignEarningsTaxedAtRatesLowerThanUsRate
      - us-gaap_DeferredTaxAssetsOperatingLossCarryforwards
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_UndistributedEarningsOfForeignSubsidiaries
      - us-gaap_DeferredTaxLiabilityNotRecognizedAmountOfUnrecognizedDeferredTaxLiabilityUndistributedEarningsOfForeignSubsidiaries
      - us-gaap_IncomeTaxesPaidNet
      - us-gaap_AccruedIncomeTaxesNoncurrent
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestExpense

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureIncomeLossBeforeIncomeTaxesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - msft_ScheduleOfComponentsOfIncomeBeforeIncomeTaxExpenseBenefitTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - msft_ScheduleOfComponentsOfIncomeBeforeIncomeTaxExpenseBenefitLineItems
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureDifferenceBetweenIncomeTaxesComputedAtFederalStatutoryRateAndProvisionForIncomeTaxesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - msft_ReconciliationOfStatutoryFederalTaxRateTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - msft_ReconciliationOfStatutoryFederalTaxRateLineItems
      - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
      - us-gaap_EffectiveIncomeTaxRateContinuingOperationsTaxRateReconciliationAbstract

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureDeferredIncomeTaxAssetsAndLiabilitiesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - msft_ScheduleOfDeferredIncomeTaxAssetsAndLiabilitiesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - msft_ScheduleOfDeferredIncomeTaxAssetsAndLiabilitiesLineItems
      - us-gaap_DeferredTaxAssetsNetAbstract
      - us-gaap_DeferredTaxLiabilitiesAbstract
      - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]
      - us-gaap_DeferredTaxLiabilities

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureChangesInUnrecognizedTaxBenefitsDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxContingencyTable
    - dei_LegalEntityAxis
    - us-gaap_IncomeTaxContingencyLineItems
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
      - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
      - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
      - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
      - us-gaap_UnrecognizedTaxBenefitsReductionsResultingFromLapseOfApplicableStatuteOfLimitations
      - us-gaap_UnrecognizedTaxBenefits

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureIncomeTaxesAdditionalInformationRegardingExaminationsDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxExaminationTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_IncomeTaxAuthorityNameAxis
      - us-gaap_IncomeTaxAuthorityNameDomain
    - us-gaap_TaxPeriodAxis
      - us-gaap_TaxPeriodDomain
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_IncomeTaxExaminationLineItems
      - us-gaap_IncomeTaxExaminationYearUnderExamination
      - us-gaap_OpenTaxYear

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureUnearnedRevenueBySegmentDetail

- us-gaap_DeferredRevenueDisclosureAbstract
  - us-gaap_DeferredRevenueArrangementByTypeTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_DeferredRevenueArrangementLineItems
      - us-gaap_DeferredRevenue

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureSummaryOfChangesInAccumulatedOtherComprehensiveIncomeByComponentDetail

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
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
      - us-gaap_StockholdersEquity

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureSummaryOfChangesInAccumulatedOtherComprehensiveIncomeByComponentParentheticalDetail

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_AccumulatedOtherComprehensiveIncomeLossLineItems
      - us-gaap_OtherComprehensiveIncomeLossBeforeReclassificationsTax
      - us-gaap_OtherComprehensiveIncomeLossTaxPortionAttributableToParent1

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureStockBasedCompensationExpenseAndRelatedIncomeTaxBenefitsDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
      - us-gaap_AllocatedShareBasedCompensationExpense
      - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureSegmentRevenueDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_SalesRevenueNet

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureOperatingIncomeLossBySegmentDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_OperatingIncomeLoss

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureCorporateAndOtherOperatingIncomeLossActivityDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_IncomeStatementLocationAxis
      - us-gaap_IncomeStatementLocationDomain
    - us-gaap_DeferredRevenueArrangementTypeAxis
      - us-gaap_DeferredRevenueArrangementTypeDomain
    - us-gaap_SegmentReportingReconcilingItemForOperatingProfitLossFromSegmentToConsolidatedLineItems
      - us-gaap_OperatingIncomeLoss

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureRevenueClassifiedByMajorGeographicAreasDetail

- us-gaap_SegmentReportingAbstract
  - msft_GeographicInformationTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementGeographicalAxis
      - us-gaap_SegmentGeographicalDomain
    - msft_GeographicInformationLineItems
      - us-gaap_SalesRevenueNet

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureRevenueClassifiedBySignificantProductAndServiceOfferingsDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ProductOrServiceAxis
      - us-gaap_ProductsAndServicesDomain
    - us-gaap_EntityWideInformationRevenueFromExternalCustomerLineItems
      - us-gaap_SalesRevenueNet

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureRevenueClassifiedBySignificantProductAndServiceOfferingsParentheticalDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - msft_ProductsOrServicesSecondaryCategorizationAxis
      - msft_ProductsOrServicesNameSecondaryCategorizationDomain
    - us-gaap_EntityWideInformationRevenueFromExternalCustomerLineItems
      - us-gaap_SalesRevenueNet

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureQuarterlyInformationUnauditedParentheticalDetail

- us-gaap_DeferredRevenueArrangementTypeAxis
  - us-gaap_DeferredRevenueArrangementTypeDomain
    - msft_WindowsTenDeferralMember

## 资产负债表结构 (Balance Sheet Structure)

### http://www.microsoft.com/20170630/taxonomy/role/StatementBALANCESHEETS

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAndStockholdersEquityAbstract

### http://www.microsoft.com/20170630/taxonomy/role/StatementBALANCESHEETSParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_SecuritiesLoaned
      - us-gaap_AllowanceForDoubtfulAccountsReceivableCurrent
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_CommonStockSharesAuthorized
      - us-gaap_CommonStockSharesOutstanding

### http://www.microsoft.com/20170630/taxonomy/role/StatementCASHFLOWSSTATEMENTS

- us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperationsAbstract
  - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
  - msft_AcquisitionsNetOfCashAcquiredAndPurchasesOfIntangibleAndOtherAssets
  - us-gaap_PaymentsToAcquireInvestments
  - us-gaap_ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities
  - us-gaap_ProceedsFromSaleOfAvailableForSaleSecurities
  - us-gaap_IncreaseDecreaseInCollateralHeldUnderSecuritiesLending
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperations [totalLabel]
- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_StatementTable
- us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperationsAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperations [totalLabel]
- us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperationsAbstract
  - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInThreeMonthsOrLess
  - us-gaap_ProceedsFromDebtMaturingInMoreThanThreeMonths
  - us-gaap_RepaymentsOfDebtMaturingInMoreThanThreeMonths
  - us-gaap_ProceedsFromIssuanceOfCommonStock
  - us-gaap_PaymentsForRepurchaseOfCommonStock
  - us-gaap_PaymentsOfDividendsCommonStock
  - us-gaap_ProceedsFromPaymentsForOtherFinancingActivities
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperations [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/StatementSTOCKHOLDERSEQUITYSTATEMENTS

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockIncludingAdditionalPaidInCapitalMember
    - us-gaap_RetainedEarningsMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureINVESTMENTS

- us-gaap_CashAndCashEquivalentsAbstract
  - us-gaap_StatementTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureGOODWILL

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_StatementTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureINTANGIBLEASSETS

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_IntangibleAssetsDisclosureTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureSTOCKHOLDERSEQUITY

- us-gaap_EquityAbstract
  - us-gaap_StatementTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureINVESTMENTSTables

- us-gaap_CashAndCashEquivalentsAbstract
  - us-gaap_StatementTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureGOODWILLTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_StatementTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureINTANGIBLEASSETSTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTableTextBlock
      - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetsByMajorClassTextBlock
      - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureSTOCKHOLDERSEQUITYTables

- us-gaap_EquityAbstract
  - us-gaap_StatementTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureInvestmentComponentsIncludingAssociatedDerivativesDetail

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - msft_CashCashEquivalentsAndInvestmentsTable
    - dei_LegalEntityAxis
    - us-gaap_InvestmentTypeAxis
    - msft_CashCashEquivalentsAndInvestmentsLineItems
      - us-gaap_AvailableForSaleSecuritiesAmortizedCost [totalLabel]
      - us-gaap_EquityMethodInvestmentAggregateCost [totalLabel]
      - us-gaap_Cash
      - us-gaap_AvailableForSaleSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
      - us-gaap_AvailableForSaleSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
      - us-gaap_AvailableForSaleSecurities
      - us-gaap_EquityMethodInvestments
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_AvailableForSaleSecuritiesCurrent
      - us-gaap_LongTermInvestments

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureInvestmentsCostMethodAdditionalInformationDetail

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_ScheduleOfCostMethodInvestmentsTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureInvestmentsSecuredBorrowingsAndLoanedSecuritiesAdditionalInformationDetail

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - invest_InvestmentTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureUnrealizedLossesOnInvestmentsDetail

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - msft_InvestmentsUnrealizedLossPositionTable
- us-gaap_MajorTypesOfDebtAndEquitySecuritiesAxis
  - us-gaap_MajorTypesOfDebtAndEquitySecuritiesDomain
    - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
    - us-gaap_ForeignGovernmentDebtSecuritiesMember
    - us-gaap_AssetBackedSecuritiesMember
    - us-gaap_CorporateDebtSecuritiesMember
    - us-gaap_EquitySecuritiesMember

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureDebtInvestmentMaturitiesDetail

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - msft_InvestmentsClassifiedByContractualMaturityDateTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedgesDetail

- msft_GainLossOnCashFlowHedgeEffectivenessNetAbstract
  - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodNetOfTax
  - us-gaap_ForeignCurrencyCashFlowHedgeGainLossReclassifiedToEarningsNet

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureFinancialAssetsAndLiabilitiesMeasuredAtFairValueOnRecurringBasisDetail

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_FairValueByLiabilityClassAxis
      - us-gaap_FairValueLiabilitiesMeasuredOnRecurringBasisUnobservableInputReconciliationByLiabilityClassDomain
    - msft_RightOfOffsetAndNettingAxis
      - msft_RightOfOffsetAndNettingDomain
    - us-gaap_FairValueByAssetClassAxis
      - us-gaap_FairValueAssetsMeasuredOnRecurringBasisUnobservableInputReconciliationByAssetClassDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
      - us-gaap_AssetsFairValueDisclosureRecurring
      - us-gaap_LiabilitiesFairValueDisclosureRecurring

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureReconciliationOfTotalAssetsMeasuredAtFairValueOnRecurringBasisToBalanceSheetPresentationDetail

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_FairValueByMeasurementFrequencyAxis
      - us-gaap_FairValueMeasurementFrequencyDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
      - us-gaap_AssetsFairValueDisclosureRecurring
      - us-gaap_Cash
      - us-gaap_CostMethodInvestments
      - us-gaap_EquityMethodInvestments
      - us-gaap_DerivativeAssets
      - us-gaap_OtherAssetsFairValueDisclosure
      - us-gaap_AvailableForSaleSecurities [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureMajorClassesOfAssetsAndLiabilitiesToWhichWeAllocatedPurchasePriceDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCashAndEquivalents
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCurrentAssetsMarketableSecurities
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCurrentAssetsOther
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedPropertyPlantAndEquipment
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles
      - us-gaap_Goodwill
      - msft_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCurrentLiabilitiesShortTermDebt
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCurrentLiabilitiesOther
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedDeferredTaxLiabilitiesNoncurrent
      - msft_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedOtherLiabilitiesNet
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredGoodwillAndLiabilitiesAssumedNet [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureMajorClassesOfAssetsAndLiabilitiesToWhichWeAllocatedPurchasePriceParentheticalDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionPurchasePriceAllocationGoodwillExpectedTaxDeductibleAmount
      - us-gaap_DebtInstrumentFaceAmount

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureAcquiredIntangibleAssetsDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAcquiredAsPartOfBusinessCombinationTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_AcquiredFiniteLivedIntangibleAssetsLineItems
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureCarryingAmountOfGoodwillDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureGoodwillAdditionalInformationDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureFiniteLivedIntangibleAssetsDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureFiniteLivedIntangibleAssetsParentheticalDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_CapitalizedSoftwareDevelopmentCostsForSoftwareSoldToCustomers

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureIntangibleAssetsAdditionalInformationDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_ImpairmentOfIntangibleAssetsFinitelived
      - us-gaap_AmortizationOfIntangibleAssets
      - us-gaap_CapitalizedComputerSoftwareAmortization1

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureIntangibleAssetsAcquiredDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetByMajorClassTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_AcquiredFiniteLivedIntangibleAssetsLineItems
      - msft_AcquiredFiniteLivedIntangibleAssets
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureEstimatedFutureAmortizationExpenseRelatedToIntangibleAssetsDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
      - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
      - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
      - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
      - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
      - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
      - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureChangesInRestructuringLiabilityDetail

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_ScheduleOfRestructuringAndRelatedCostsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_RestructuringCostAndReserveAxis
      - us-gaap_TypeOfRestructuringDomain
    - us-gaap_RestructuringCostAndReserveLineItems
      - us-gaap_RestructuringReserve
      - us-gaap_RestructuringCharges
      - us-gaap_PaymentsForRestructuring
      - us-gaap_RestructuringReserveSettledWithoutCash2
      - us-gaap_RestructuringReserve

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureFutureMinimumRentalCommitmentsUnderNonCancellableOperatingLeasesDetail

- us-gaap_ScheduleOfOperatingLeasedAssetsTable
  - dei_LegalEntityAxis
  - us-gaap_PropertyPlantAndEquipmentByTypeAxis
  - us-gaap_OperatingLeasedAssetsLineItems
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDueCurrent
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInTwoYears
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInThreeYears
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFourYears
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFiveYears
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDueThereafter
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDue [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureSharesOfCommonStockOutstandingDetail

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfCapitalUnitsTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureStockholdersEquityAdditionalInformationDetail

- us-gaap_StatementOfStockholdersEquityAbstract
  - msft_ShareRepurchasesTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureShareRepurchasesDetail

- us-gaap_EquityAbstract
  - msft_ShareRepurchasesTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureDividendsDeclaredDetail

- us-gaap_EquityAbstract
  - msft_DividendsTable

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureStockPlanActivityDetail

- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
  - msft_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsAssumedAcquisitionInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
  - msft_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsAssumedInAcquisitionsWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureLongLivedAssetsExcludingFinancialInstrumentsAndTaxAssetsClassifiedByLocationOfControllingStatutoryCompanyDetail

- us-gaap_SegmentReportingAbstract
  - msft_CertainLongLivedAssetsByGeographyTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementGeographicalAxis
      - us-gaap_SegmentGeographicalDomain
    - msft_CertainLongLivedAssetsByGeographyLineItems
      - us-gaap_NoncurrentAssets

## 现金流量表结构 (Cash Flow Structure)

### http://www.microsoft.com/20170630/taxonomy/role/StatementCASHFLOWSSTATEMENTS

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperationsAbstract
    - us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperationsAbstract
    - us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperationsAbstract
    - us-gaap_EffectOfExchangeRateOnCashAndCashEquivalents
    - us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease [totalLabel]
    - us-gaap_CashAndCashEquivalentsAtCarryingValue
    - us-gaap_CashAndCashEquivalentsAtCarryingValue
- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInInventories
  - us-gaap_IncreaseDecreaseInOtherCurrentAssets
  - us-gaap_IncreaseDecreaseInOtherNoncurrentAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInOtherCurrentLiabilities
  - us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedgesDetail

- us-gaap_HedgingDesignationAxis
  - us-gaap_HedgingDesignationDomain
    - us-gaap_DesignatedAsHedgingInstrumentMember
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ForeignExchangeContractMember
- dei_LegalEntityAxis
  - dei_EntityDomain
- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
- us-gaap_DerivativeInstrumentsGainLossLineItems
  - msft_GainLossOnCashFlowHedgeEffectivenessNetAbstract
  - us-gaap_DerivativeInstrumentsGainLossRecognizedInIncomeIneffectivePortionAndAmountExcludedFromEffectivenessTestingNetAbstract

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedgesParentheticalDetail

- us-gaap_HedgingDesignationAxis
  - us-gaap_HedgingDesignationDomain
    - us-gaap_DesignatedAsHedgingInstrumentMember
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ForeignExchangeContractMember
- dei_LegalEntityAxis
  - dei_EntityDomain
- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
- us-gaap_DerivativeInstrumentsGainLossLineItems
  - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodTax

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureCommitmentsAdditionalInformationDetail

- us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAxis
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseDomain
    - us-gaap_BuildingMember

## 股东权益结构 (Equity Structure)

### http://www.microsoft.com/20170630/taxonomy/role/StatementSTOCKHOLDERSEQUITYSTATEMENTS

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_StockholdersEquity
    - us-gaap_StockIssuedDuringPeriodValueNewIssues
    - us-gaap_NetIncomeLoss
    - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent
    - us-gaap_DividendsCommonStockCash
    - us-gaap_StockRepurchasedDuringPeriodValue
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
    - us-gaap_AdjustmentToAdditionalPaidInCapitalIncomeTaxEffectFromShareBasedCompensationNet
    - us-gaap_StockholdersEquityOther
    - us-gaap_StockholdersEquity

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureSTOCKHOLDERSEQUITY

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureEMPLOYEESTOCKANDSAVINGSPLANS

- us-gaap_PostemploymentBenefitsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_CompensationAndEmployeeBenefitPlansTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureSTOCKHOLDERSEQUITYTables

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_ScheduleOfCommonStockOutstandingRollForwardTableTextBlock
    - msft_ShareRepurchaseProgramDisclosureTableTextBlock
    - us-gaap_DividendsDeclaredTableTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureEMPLOYEESTOCKANDSAVINGSPLANSTables

- us-gaap_PostemploymentBenefitsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfCompensationCostForShareBasedPaymentArrangementsAllocationOfShareBasedCompensationCostsByPlanTableTextBlock
      - msft_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsMethodUsedTableTextBlock
      - us-gaap_DisclosureOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTextBlock
      - us-gaap_ScheduleOfShareBasedCompensationEmployeeStockPurchasePlanActivityTableTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureSharesOfCommonStockOutstandingDetail

- us-gaap_ScheduleOfCapitalUnitsTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_CapitalUnitLineItems
    - us-gaap_CommonStockSharesOutstanding
    - us-gaap_StockIssuedDuringPeriodSharesNewIssues
    - us-gaap_StockRepurchasedDuringPeriodShares
    - us-gaap_CommonStockSharesOutstanding

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureStockholdersEquityAdditionalInformationDetail

- msft_ShareRepurchasesTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_ShareRepurchaseProgramAxis
    - us-gaap_ShareRepurchaseProgramDomain
      - msft_ShareRepurchaseProgramTwentyThirteenMember
      - msft_ShareRepurchaseProgramTwentySixteenMember
  - msft_ShareRepurchasesLineItems
    - us-gaap_StockRepurchaseProgramAuthorizedAmount1
    - us-gaap_StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureShareRepurchasesDetail

- msft_ShareRepurchasesTable
  - dei_LegalEntityAxis
  - us-gaap_ShareRepurchaseProgramAxis
    - us-gaap_ShareRepurchaseProgramDomain
      - msft_ShareRepurchaseProgramTwentyThirteenMember
      - msft_ShareRepurchaseProgramTwentySixteenMember
  - msft_ShareRepurchasesLineItems
    - us-gaap_StockRepurchasedDuringPeriodShares
    - us-gaap_StockRepurchasedDuringPeriodValue

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureEmployeeStockAndSavingsPlansAdditionalInformationDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - msft_CompensationRelatedCostsDisclosureTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
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

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureAssumptionsUsedInEstimatingFairValueOfStockAwardGrantsDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - msft_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsMethodUsedTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - msft_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsMethodUsedLineItems
      - msft_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsExpectedDividendsPerShare
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsRiskFreeInterestRateMinimum
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsRiskFreeInterestRateMaximum

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureStockPlanActivityDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureStockPlanActivityParentheticalDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureEmployeePurchasedSharesDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - msft_EmployeeStockPurchasePlanTable
    - dei_LegalEntityAxis
    - msft_EmployeeStockPurchasePlanLineItems
      - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockPurchasePlans
      - msft_StockIssuedEmployeeStockPurchasePlanAveragePricePerShare

## 其他结构 (Other Structure)

### http://www.microsoft.com/20170630/taxonomy/role/DocumentDocumentAndEntityInformation

- msft_DocumentAndEntityInformationAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
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
      - dei_EntityListingParValuePerShare
      - dei_EntityCommonStockSharesOutstanding
      - dei_EntityPublicFloat
      - dei_EntityTaxIdentificationNumber

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureACCOUNTINGPOLICIES

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_SignificantAccountingPoliciesTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureINVESTMENTS

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_InvestmentsInDebtAndEquityInstrumentsCashAndCashEquivalentsUnrealizedAndRealizedGainsLossesTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureDERIVATIVES

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureFAIRVALUEMEASUREMENTS

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_FairValueDisclosuresTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureINVENTORIES

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_InventoryDisclosureTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosurePROPERTYANDEQUIPMENT

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureBUSINESSCOMBINATIONS

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_MergersAcquisitionsAndDispositionsDisclosuresTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureGOODWILL

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_GoodwillDisclosureTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureDEBT

- us-gaap_DebtDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_DebtDisclosureTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureRESTRUCTURINGCHARGES

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_RestructuringAndRelatedActivitiesDisclosureTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureCOMMITMENTS

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_CommitmentsDisclosureTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureCONTINGENCIES

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_LegalMattersAndContingenciesTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureSEGMENTINFORMATIONANDGEOGRAPHICDATA

- us-gaap_SegmentReportingAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureQUARTERLYINFORMATIONUNAUDITED

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_QuarterlyFinancialInformationTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureACCOUNTINGPOLICIESPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_BasisOfAccountingPolicyPolicyTextBlock
      - us-gaap_ConsolidationPolicyTextBlock
      - us-gaap_UseOfEstimates
      - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
      - msft_ProductRevenueAndServiceAndOtherRevenuePolicyTextBlock
      - us-gaap_RevenueRecognitionPolicyTextBlock
      - us-gaap_CostOfSalesPolicyTextBlock
      - us-gaap_StandardProductWarrantyPolicy
      - us-gaap_ResearchDevelopmentAndComputerSoftwarePolicyTextBlock
      - msft_SellingAndMarketingPolicyTextBlock
      - us-gaap_ShareBasedCompensationOptionAndIncentivePlansPolicy
      - us-gaap_IncomeTaxPolicyTextBlock
      - us-gaap_FairValueOfFinancialInstrumentsPolicy
      - us-gaap_InvestmentPolicyTextBlock
      - us-gaap_DerivativesPolicyTextBlock
      - us-gaap_TradeAndOtherAccountsReceivablePolicy
      - us-gaap_InventoryPolicyTextBlock
      - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
      - us-gaap_GoodwillAndIntangibleAssetsGoodwillPolicy
      - us-gaap_IntangibleAssetsFiniteLivedPolicy
      - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock
      - us-gaap_EarningsPerSharePolicyTextBlock
      - us-gaap_SegmentReportingPolicyPolicyTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureACCOUNTINGPOLICIESTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfCreditLossesForFinancingReceivablesCurrentTableTextBlock
      - us-gaap_ScheduleOfNewAccountingPronouncementsAndChangesInAccountingPrinciplesTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureINVESTMENTSTables

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - msft_ScheduleOfCashCashEquivalentsAndInvestmentsTableTextBlock
    - us-gaap_ScheduleOfUnrealizedLossOnInvestmentsTableTextBlock
    - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureDERIVATIVESTables

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfDerivativeInstrumentsInStatementOfFinancialPositionFairValueTextBlock
      - us-gaap_ScheduleOfDerivativeInstrumentsGainLossInStatementOfFinancialPerformanceTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureFAIRVALUEMEASUREMENTSTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfFairValueAssetsAndLiabilitiesMeasuredOnRecurringBasisTableTextBlock
      - msft_ReconciliationOfAssetsMeasuredAtFairValueOnRecurringBasisToBalanceSheetPresentationTableTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureINVENTORIESTables

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfInventoryCurrentTableTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosurePROPERTYANDEQUIPMENTTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureBUSINESSCOMBINATIONSTables

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTextBlock
      - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetsByMajorClassTextBlock
      - msft_RevenueAndOperatingLossAttributableToAcquireeSinceAcquisitionDateTableTextBlock
      - us-gaap_BusinessAcquisitionProFormaInformationTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureGOODWILLTables

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_ScheduleOfGoodwillTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureDEBTTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfDebtInstrumentsTextBlock
      - us-gaap_ScheduleOfMaturitiesOfLongTermDebtTableTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureRESTRUCTURINGCHARGESTables

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfRestructuringReserveByTypeOfCostTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureCOMMITMENTSTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfFutureMinimumRentalPaymentsForOperatingLeasesTableTextBlock
      - us-gaap_ScheduleOfFutureMinimumLeasePaymentsForCapitalLeasesTableTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureSEGMENTINFORMATIONANDGEOGRAPHICDATATables

- us-gaap_SegmentReportingAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTextBlock
      - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTextBlock
      - us-gaap_ScheduleOfRevenueFromExternalCustomersAttributedToForeignCountriesByGeographicAreaTextBlock
      - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTextBlock
      - us-gaap_ScheduleOfEntityWideDisclosureOnGeographicAreasLongLivedAssetsInIndividualForeignCountriesByCountryTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureQUARTERLYINFORMATIONUNAUDITEDTables

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfQuarterlyFinancialInformationTableTextBlock

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureAccountingPoliciesAdditionalInformationDetail

- us-gaap_AccountingPoliciesAbstract
  - msft_SignificantAccountingPoliciesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DeferredRevenueArrangementTypeAxis
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - msft_SignificantAccountingPoliciesLineItems
      - msft_RevenueRecognitionPeriod
      - us-gaap_AdvertisingExpense
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - msft_OperatingLeaseRightOfUseAssets
      - msft_OperatingLeaseLiabilities
      - us-gaap_SalesRevenueNet
      - us-gaap_IncomeTaxExpenseBenefit
      - msft_AccountsReceivableNetAndOtherAssets
      - us-gaap_DeferredRevenue
      - us-gaap_DeferredTaxLiabilitiesNoncurrent

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureAllowanceForDoubtfulAccountsDetail

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_ValuationAndQualifyingAccountsDisclosureTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ValuationAllowancesAndReservesTypeAxis
      - us-gaap_ValuationAllowancesAndReservesDomain
    - us-gaap_ValuationAndQualifyingAccountsDisclosureLineItems
      - us-gaap_ValuationAllowancesAndReservesBalance
      - msft_ValuationAllowancesAndReservesChargedToCostsAndOther
      - us-gaap_ValuationAllowancesAndReservesDeductions
      - us-gaap_ValuationAllowancesAndReservesBalance

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureNetRecognizedGainsLossesOnInvestmentsDetail

- us-gaap_ScheduleOfGainLossOnInvestmentsTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_ScheduleOfGainLossOnInvestmentsIncludingMarketableSecuritiesAndInvestmentsHeldAtCostIncomeStatementReportedAmountsSummaryLineItems

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureInvestmentComponentsIncludingAssociatedDerivativesDetail

- us-gaap_InvestmentTypeAxis
  - us-gaap_InvestmentTypeCategorizationMember
    - us-gaap_CashMember
    - us-gaap_MoneyMarketFundsMember
    - us-gaap_CommercialPaperMember
    - us-gaap_CertificatesOfDepositMember
    - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
    - us-gaap_ForeignGovernmentDebtSecuritiesMember
    - us-gaap_AssetBackedSecuritiesMember
    - us-gaap_CorporateDebtSecuritiesMember
    - us-gaap_USStatesAndPoliticalSubdivisionsMember
    - us-gaap_EquitySecuritiesMember
    - msft_OtherSecurityInvestmentsMember
- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureInvestmentsCostMethodAdditionalInformationDetail

- us-gaap_ScheduleOfCostMethodInvestmentsTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_FairValueByMeasurementFrequencyAxis
    - us-gaap_FairValueMeasurementFrequencyDomain
      - us-gaap_FairValueMeasurementsNonrecurringMember
  - us-gaap_ScheduleOfCostMethodInvestmentsLineItems
    - us-gaap_CostMethodInvestments

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureInvestmentsSecuredBorrowingsAndLoanedSecuritiesAdditionalInformationDetail

- invest_InvestmentTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_InvestmentTypeAxis
    - us-gaap_InvestmentTypeCategorizationMember
      - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
      - us-gaap_CashMember
  - invest_InvestmentLineItems
    - us-gaap_SecuritiesReceivedAsCollateral

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureUnrealizedLossesOnInvestmentsDetail

- msft_InvestmentsUnrealizedLossPositionTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_MajorTypesOfDebtAndEquitySecuritiesAxis
  - msft_InvestmentsUnrealizedLossPositionLineItems
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionLessThanTwelveMonthsFairValue
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionLessThan12MonthsAccumulatedLoss
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionTwelveMonthsOrLongerFairValue
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPosition12MonthsOrLongerAccumulatedLoss
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionFairValue [totalLabel]
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionAccumulatedLoss

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureDebtInvestmentMaturitiesDetail

- msft_InvestmentsClassifiedByContractualMaturityDateTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - msft_InvestmentsClassifiedByContractualMaturityDateLineItems
    - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAmortizedCostBasisRollingMaturityAbstract
      - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesNextRollingTwelveMonthsAmortizedCostBasis
      - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearTwoThroughFiveAmortizedCostBasis
      - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearSixThroughTenAmortizedCostBasis
      - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingAfterYearTenAmortizedCostBasis
      - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis [totalLabel]
    - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesFairValueRollingMaturityAbstract
      - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesNextRollingTwelveMonthsFairValue
      - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearTwoThroughFiveFairValue
      - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingYearSixThroughTenFairValue
      - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesRollingAfterYearTenFairValue
      - us-gaap_AvailableForSaleSecuritiesDebtSecurities [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureDerivativesAdditionalInformationDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_PositionAxis
      - us-gaap_PositionDomain
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DerivativeLineItems
      - us-gaap_MaximumLengthOfTimeForeignCurrencyCashFlowHedge
      - invest_DerivativeNotionalAmount
      - msft_FinancialInstrumentCovenantMinimumLiquidityRequirement
      - us-gaap_DebtInstrumentCreditRating
      - msft_FinancialInstrumentCovenantMinimumLiquidity
      - us-gaap_ForeignCurrencyCashFlowHedgeGainLossToBeReclassifiedDuringNext12Months

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureFairValuesOfDerivativeInstrumentsDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_FairValuesDerivativesBalanceSheetLocationByDerivativeContractTypeByHedgingDesignationTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - msft_BalanceSheetOffsettingEligibilityAxis
      - msft_BalanceSheetOffsettingEligibilityDomain
    - us-gaap_DerivativesFairValueLineItems
      - us-gaap_DerivativeFairValueOfDerivativeAsset
      - us-gaap_DerivativeAssetFairValueGrossLiability
      - msft_DerivativeAssetsNetAmountsPresentedInBalanceSheet [totalLabel]
      - msft_DerivativeFairValueOfDerivativeAssetAmountNotOffset
      - us-gaap_DerivativeCollateralRightToReclaimCash
      - msft_DerivativeAssetsPotentialNetAmountsNotPresentedInBalanceSheet [totalLabel]
      - us-gaap_DerivativeFairValueOfDerivativeLiability
      - us-gaap_DerivativeLiabilityFairValueGrossAsset
      - msft_DerivativeLiabilitiesNetAmountsPresentedInBalanceSheet
      - msft_DerivativeFairValueOfDerivativeLiabilityAmountNotOffset
      - us-gaap_DerivativeCollateralObligationToReturnCash
      - msft_DerivativeLiabilitiesPotentialNetAmountsNotPresentedInBalanceSheet

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureGainsLossesOnFairValueHedgesAndRelatedHedgedItemsDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
- us-gaap_DerivativeInstrumentsGainLossLineItems
  - us-gaap_ChangeInUnrealizedGainLossOnFairValueHedgingInstruments1
  - us-gaap_ChangeInUnrealizedGainLossOnHedgedItemInFairValueHedge1
  - us-gaap_GainLossOnFairValueHedgeIneffectivenessNet [totalLabel]
  - us-gaap_GainLossFromComponentsExcludedFromAssessmentOfFairValueHedgeEffectivenessNet
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ForeignExchangeContractMember
    - us-gaap_EquityContractMember
- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureNonDesignatedDerivativeGainsLossesDetail

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
- us-gaap_DerivativeInstrumentsGainLossLineItems
  - us-gaap_DerivativeInstrumentsNotDesignatedAsHedgingInstrumentsGainLossNet
- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ForeignExchangeContractMember
    - us-gaap_EquityContractMember
    - us-gaap_InterestRateContractMember
    - us-gaap_CreditRiskContractMember
    - us-gaap_CommodityContractMember
- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureComponentsOfInventoriesDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryCurrentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_InventoryLineItems
      - us-gaap_InventoryRawMaterialsNetOfReserves
      - us-gaap_InventoryWorkInProcessNetOfReserves
      - us-gaap_InventoryFinishedGoodsNetOfReserves
      - us-gaap_InventoryNet [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureComponentsOfPropertyAndEquipmentDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_Land
      - us-gaap_BuildingsAndImprovementsGross
      - us-gaap_LeaseholdImprovementsGross
      - msft_ComputerHardwareAndSoftware
      - us-gaap_FurnitureAndFixturesGross
      - us-gaap_PropertyPlantAndEquipmentGross [totalLabel]
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/DisclosurePropertyAndEquipmentAdditionalInformationDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_CapitalLeasedAssetsGross
      - us-gaap_CapitalLeasesLesseeBalanceSheetAssetsByMajorClassAccumulatedDeprecation
      - us-gaap_CapitalLeaseObligationsIncurred
      - us-gaap_Depreciation

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureBusinessCombinationsAdditionalInformationDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionEffectiveDateOfAcquisition1
      - us-gaap_BusinessAcquisitionNameOfAcquiredEntity
      - us-gaap_BusinessCombinationConsiderationTransferred1
      - us-gaap_PaymentsToAcquireBusinessesGross

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureSupplementalConsolidatedFinancialResultsOnUnauditedProFormaBasisAsIfAcquisitionHadBeenConsummatedOnBeginningOfPeriodDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionsProFormaRevenue
      - us-gaap_BusinessAcquisitionsProFormaNetIncomeLoss
      - us-gaap_BusinessAcquisitionProFormaEarningsPerShareDiluted

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureCarryingAmountOfGoodwillDetail

- us-gaap_ScheduleOfGoodwillTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
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

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureGoodwillAdditionalInformationDetail

- us-gaap_ScheduleOfGoodwillTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementBusinessSegmentsAxis
    - us-gaap_SegmentDomain
      - msft_PhoneHardwareMember
  - us-gaap_GoodwillLineItems
    - us-gaap_GoodwillImpairedAccumulatedImpairmentLoss
    - us-gaap_GoodwillImpairmentLoss

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureDebtAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ShortTermDebtTypeAxis
      - us-gaap_ShortTermDebtTypeDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_CommercialPaper
      - us-gaap_ShortTermDebtWeightedAverageInterestRate
      - us-gaap_DebtInstrumentTerm
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_LineOfCreditFacilityExpirationDate1
      - us-gaap_LineOfCreditFacilityCovenantCompliance
      - us-gaap_ProceedsFromLinesOfCredit
      - us-gaap_LongTermDebt
      - us-gaap_LongTermDebtFairValue
      - us-gaap_InterestPaid
      - us-gaap_DebtInstrumentUnamortizedDiscountPremiumAndDebtIssuanceCostsNet

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureLongTermDebtDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentMaturityDate
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureLongTermDebtParentheticalDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureMaturitiesOfLongTermDebtDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive
      - us-gaap_DebtInstrumentFaceAmount [totalLabel]

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureChangesInUnrecognizedTaxBenefitsDetail

- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureRestructuringChargesAdditionalInformationDetail

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_ScheduleOfRestructuringAndRelatedCostsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_RestructuringPlanAxis
      - us-gaap_RestructuringPlanDomain
    - us-gaap_RestructuringCostAndReserveAxis
      - us-gaap_TypeOfRestructuringDomain
    - us-gaap_RestructuringCostAndReserveLineItems
      - us-gaap_RestructuringAndRelatedCostNumberOfPositionsEliminated
      - us-gaap_RestructuringCharges
      - us-gaap_RestructuringReserveAccrualAdjustment1
      - us-gaap_RestructuringAndRelatedActivitiesCompletionDate

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureCommitmentsAdditionalInformationDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - msft_CommitmentsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_LongTermPurchaseCommitmentByCategoryOfItemPurchasedAxis
      - us-gaap_LongTermPurchaseCommitmentCategoryOfItemPurchasedDomain
    - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAxis
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_UnrecordedUnconditionalPurchaseObligationByCategoryOfItemPurchasedAxis
      - us-gaap_UnconditionalPurchaseObligationCategoryOfGoodsOrServicesAcquiredDomain
    - msft_CommitmentsLineItems
      - us-gaap_CommitmentsFairValueDisclosure
      - us-gaap_LeaseAndRentalExpense
      - us-gaap_CapitalLeaseObligationsCurrent
      - us-gaap_CapitalLeaseObligationsNoncurrent
      - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceSheetAmount

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureFutureMinimumRentalCommitmentsUnderNonCancellableOperatingLeasesDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_ScheduleOfOperatingLeasedAssetsTable
- us-gaap_PropertyPlantAndEquipmentByTypeAxis
  - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_BuildingMember
- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureFutureMinimumLeasePaymentsUnderNonCancellableCapitalLeasesDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - msft_FutureMinimumLeasePaymentsUnderNonCancellableCapitalLeasesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - msft_FutureMinimumLeasePaymentsUnderNonCancellableCapitalLeasesLineItems
      - us-gaap_CapitalLeasesFutureMinimumPaymentsDueAbstract

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureFutureMinimumLeasePaymentsUnderNonCancellableCapitalLeasesParentheticalDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - msft_FutureMinimumLeasePaymentsUnderNonCancellableCapitalLeasesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - msft_FutureMinimumLeasePaymentsUnderNonCancellableCapitalLeasesLineItems
      - us-gaap_CapitalLeasesFutureMinimumPaymentsDueAbstract

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureContingenciesAdditionalInformationDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_LossContingenciesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_LossContingenciesLineItems
      - us-gaap_LossContingencyAccrualCarryingValueCurrent
      - us-gaap_LossContingencyRangeOfPossibleLossPortionNotAccrued

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureShareRepurchasesDetail

- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureDividendsDeclaredDetail

- msft_DividendsTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - msft_DividendsLineItems
    - us-gaap_DividendsPayableDateDeclaredDayMonthAndYear
    - us-gaap_CommonStockDividendsPerShareDeclared
    - us-gaap_DividendsPayableDateOfRecordDayMonthAndYear
    - us-gaap_DividendsCommonStockCash
    - us-gaap_DividendPayableDateToBePaidDayMonthAndYear

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureEmployeePurchasedSharesDetail

- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureSegmentInformationAndGeographicDataAdditionalInformationDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_SegmentReportingDisclosureOfMajorCustomers

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureQuarterlyInformationUnauditedDetail

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - msft_QuarterlyFinancialInformationTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - msft_QuarterlyFinancialInformationLineItems
      - us-gaap_SalesRevenueNet
      - us-gaap_GrossProfit
      - us-gaap_OperatingIncomeLoss
      - us-gaap_NetIncomeLoss
      - us-gaap_EarningsPerShareBasic
      - us-gaap_EarningsPerShareDiluted

### http://www.microsoft.com/20170630/taxonomy/role/DisclosureQuarterlyInformationUnauditedParentheticalDetail

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - msft_QuarterlyFinancialInformationTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DeferredRevenueArrangementTypeAxis
    - us-gaap_RestructuringPlanAxis
      - us-gaap_RestructuringPlanDomain
    - us-gaap_RestructuringCostAndReserveAxis
      - us-gaap_TypeOfRestructuringDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - msft_QuarterlyFinancialInformationLineItems
      - us-gaap_SalesRevenueNet
      - us-gaap_RestructuringCharges
      - msft_ImpairmentIntegrationAndRestructuringEffectOnOperatingIncomeLossAfterTax
      - msft_ImpairmentIntegrationAndRestructuringEffectOnEarningsAfterTax
      - msft_ImpairmentIntegrationAndRestructuringEffectOnEarningsPerShareAfterTax
      - us-gaap_AssetImpairmentCharges

