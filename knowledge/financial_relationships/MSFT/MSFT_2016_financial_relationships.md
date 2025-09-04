# MSFT 2016 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.microsoft.com/taxonomy/role/StatementOfIncome

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

### http://www.microsoft.com/taxonomy/role/StatementOfOtherComprehensiveIncome

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_NetIncomeLoss
      - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
      - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.microsoft.com/taxonomy/role/StatementOfOtherComprehensiveIncomeParenthetical

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_OtherComprehensiveIncomeLossDerivativesQualifyingAsHedgesTax
      - us-gaap_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesTax
      - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentTax

### http://www.microsoft.com/taxonomy/role/StatementOfCashFlowsIndirect

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_AssetImpairmentCharges
  - msft_DepreciationAmortizationAndOther
  - us-gaap_AllocatedShareBasedCompensationExpense
  - msft_GainLossOnInvestmentsAndDerivativeInstruments
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_IncreaseDecreaseInDeferredRevenue
  - us-gaap_RecognitionOfDeferredRevenue
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.microsoft.com/taxonomy/role/StatementOfShareholdersEquityAndOtherComprehensiveIncome

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_StatementLineItems
      - us-gaap_StockholdersEquity
      - us-gaap_StockIssuedDuringPeriodValueNewIssues
      - us-gaap_NetIncomeLoss
      - us-gaap_OtherComprehensiveIncomeLossNetOfTax
      - us-gaap_DividendsCommonStockCash
      - us-gaap_StockRepurchasedDuringPeriodValue
      - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
      - us-gaap_AdjustmentToAdditionalPaidInCapitalIncomeTaxEffectFromShareBasedCompensationNet
      - us-gaap_StockholdersEquityOther
      - us-gaap_StockholdersEquity

### http://www.microsoft.com/taxonomy/role/DisclosureAccountingPoliciesAdditionalInformation

- us-gaap_DeferredRevenueArrangementTypeAxis
  - us-gaap_DeferredRevenueArrangementTypeDomain
    - msft_WindowsTenDeferralMember

### http://www.microsoft.com/taxonomy/role/DisclosureBasicAndDilutedEarningsPerShare

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

### http://www.microsoft.com/taxonomy/role/DisclosureComponentsOfOtherIncomeExpenseNet

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

### http://www.microsoft.com/taxonomy/role/DisclosureNetRecognizedGainsLossesOnInvestments

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_ScheduleOfGainLossOnInvestmentsTable
- us-gaap_ScheduleOfGainLossOnInvestmentsIncludingMarketableSecuritiesAndInvestmentsHeldAtCostIncomeStatementReportedAmountsSummaryLineItems
  - us-gaap_MarketableSecuritiesRealizedGainLossOtherThanTemporaryImpairmentsAmount
  - us-gaap_AvailableForSaleSecuritiesGrossRealizedGains
  - us-gaap_AvailableForSaleSecuritiesGrossRealizedLosses
  - us-gaap_GainLossOnInvestments [totalLabel]

### http://www.microsoft.com/taxonomy/role/DisclosureGainsLossesOnFairValueHedgesAndRelatedHedgedItems

- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - dei_LegalEntityAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.microsoft.com/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedges

- us-gaap_DerivativeInstrumentsGainLossRecognizedInIncomeIneffectivePortionAndAmountExcludedFromEffectivenessTestingNetAbstract
  - us-gaap_DerivativeInstrumentsGainLossRecognizedInIncomeIneffectivePortionAndAmountExcludedFromEffectivenessTestingNet
- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - dei_LegalEntityAxis
  - us-gaap_HedgingDesignationAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.microsoft.com/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedgesParenthetical

- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - us-gaap_HedgingDesignationAxis
  - dei_LegalEntityAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.microsoft.com/taxonomy/role/DisclosureNonDesignatedDerivativeGainsLosses

- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - dei_LegalEntityAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.microsoft.com/taxonomy/role/DisclosureProvisionForIncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - msft_ReconciliationOfProvisionOfIncomeTaxesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - msft_ReconciliationOfProvisionOfIncomeTaxesLineItems
      - us-gaap_CurrentIncomeTaxExpenseBenefitContinuingOperationsAbstract
      - us-gaap_DeferredIncomeTaxExpenseBenefitContinuingOperationsAbstract
      - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.microsoft.com/taxonomy/role/DisclosureIncomeLossBeforeIncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - msft_ScheduleOfComponentsOfIncomeBeforeIncomeTaxExpenseBenefitTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - msft_ScheduleOfComponentsOfIncomeBeforeIncomeTaxExpenseBenefitLineItems
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments [totalLabel]

### http://www.microsoft.com/taxonomy/role/DisclosureIncomeTaxesAdditionalInformation

- us-gaap_IncomeTaxDisclosureAbstract
  - msft_IncomeTaxesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_IncomeStatementLocationAxis
      - us-gaap_IncomeStatementLocationDomain
    - us-gaap_DeferredRevenueArrangementTypeAxis
      - us-gaap_DeferredRevenueArrangementTypeDomain
    - msft_IncomeTaxesLineItems
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
      - msft_ForeignEarningsTaxedAtRatesLowerThanUsRate
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_UndistributedEarningsOfForeignSubsidiaries
      - us-gaap_DeferredTaxLiabilityNotRecognizedAmountOfUnrecognizedDeferredTaxLiabilityUndistributedEarningsOfForeignSubsidiaries
      - us-gaap_IncomeTaxesPaidNet
      - us-gaap_AccruedIncomeTaxesNoncurrent
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestExpense

### http://www.microsoft.com/taxonomy/role/DisclosureDifferenceBetweenIncomeTaxesComputedAtFederalStatutoryRateAndProvisionForIncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - msft_ReconciliationOfStatutoryFederalTaxRateTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - msft_ReconciliationOfStatutoryFederalTaxRateLineItems
      - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
      - us-gaap_EffectiveIncomeTaxRateContinuingOperationsTaxRateReconciliationAbstract
      - us-gaap_EffectiveIncomeTaxRateContinuingOperations [totalLabel]

### http://www.microsoft.com/taxonomy/role/DisclosureDeferredIncomeTaxAssetsAndLiabilities

- us-gaap_IncomeTaxDisclosureAbstract
  - msft_ScheduleOfDeferredIncomeTaxAssetsAndLiabilitiesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - msft_DeferredTaxesAxis
      - msft_DeferredTaxesDomain
    - msft_ScheduleOfDeferredIncomeTaxAssetsAndLiabilitiesLineItems
      - us-gaap_DeferredTaxAssetsNetAbstract
      - us-gaap_DeferredTaxLiabilitiesAbstract
      - us-gaap_DeferredTaxAssetsLiabilitiesNetAbstract

### http://www.microsoft.com/taxonomy/role/DisclosureChangesInUnrecognizedTaxBenefits

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

### http://www.microsoft.com/taxonomy/role/DisclosureIncomeTaxesAdditionalInformationRegardingExaminations

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxExaminationTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_IncomeTaxAuthorityNameAxis
      - us-gaap_IncomeTaxAuthorityNameDomain
    - us-gaap_TaxPeriodAxis
      - us-gaap_TaxPeriodDomain
    - us-gaap_IncomeTaxExaminationLineItems
      - us-gaap_IncomeTaxExaminationYearUnderExamination
      - us-gaap_OpenTaxYear

### http://www.microsoft.com/taxonomy/role/DisclosureUnearnedRevenueBySegment

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

### http://www.microsoft.com/taxonomy/role/DisclosureUnearnedRevenueAdditionalInformation

- us-gaap_DeferredRevenueDisclosureAbstract
  - us-gaap_DeferredRevenueArrangementByTypeTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DeferredRevenueArrangementTypeAxis
      - us-gaap_DeferredRevenueArrangementTypeDomain
    - us-gaap_DeferredRevenueArrangementLineItems
      - us-gaap_DeferredRevenue

### http://www.microsoft.com/taxonomy/role/DisclosureCommitmentsAdditionalInformation

- us-gaap_LeaseAndRentalExpense
  - us-gaap_BusinessAcquisitionSharePrice
  - msft_BusinessAcquisitionCostOfAcquiredEntityExpectedPurchasePrice

### http://www.microsoft.com/taxonomy/role/DisclosureSummaryOfChangesInAccumulatedOtherComprehensiveIncomeByComponent

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_IncomeStatementLocationAxis
      - us-gaap_IncomeStatementLocationDomain
    - us-gaap_AccumulatedOtherComprehensiveIncomeLossLineItems
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
      - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodNetOfTax
      - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIOnDerivativesBeforeTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesBeforeTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIOnDerivativesTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIOnDerivativesNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossDerivativesQualifyingAsHedgesNetOfTax [totalLabel]
      - us-gaap_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesAdjustmentNetOfTax [totalLabel]
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax

### http://www.microsoft.com/taxonomy/role/DisclosureSummaryOfChangesInAccumulatedOtherComprehensiveIncomeByComponentParenthetical

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_AccumulatedOtherComprehensiveIncomeLossLineItems
      - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodTax
      - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodTax
      - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentTax

### http://www.microsoft.com/taxonomy/role/DisclosureStockBasedCompensationExpenseAndRelatedIncomeTaxBenefits

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
      - us-gaap_AllocatedShareBasedCompensationExpense
      - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense

### http://www.microsoft.com/taxonomy/role/DisclosureSegmentRevenue

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

### http://www.microsoft.com/taxonomy/role/DisclosureOperatingIncomeLossBySegment

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

### http://www.microsoft.com/taxonomy/role/DisclosureCorporateAndOtherOperatingIncomeLossActivity

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_IncomeStatementLocationAxis
      - us-gaap_IncomeStatementLocationDomain
    - us-gaap_SegmentReportingReconcilingItemForOperatingProfitLossFromSegmentToConsolidatedLineItems
      - us-gaap_OperatingIncomeLoss

### http://www.microsoft.com/taxonomy/role/DisclosureCorporateAndOtherOperatingIncomeLossActivityParenthetical

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTable
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DeferredRevenueArrangementTypeAxis
      - us-gaap_DeferredRevenueArrangementTypeDomain
    - us-gaap_IncomeStatementLocationAxis
      - us-gaap_IncomeStatementLocationDomain
    - us-gaap_SegmentReportingReconcilingItemForOperatingProfitLossFromSegmentToConsolidatedLineItems
      - us-gaap_OperatingIncomeLoss

### http://www.microsoft.com/taxonomy/role/DisclosureRevenueClassifiedByMajorGeographicAreas

- us-gaap_SegmentReportingAbstract
  - msft_GeographicInformationTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementGeographicalAxis
      - us-gaap_SegmentGeographicalDomain
    - msft_GeographicInformationLineItems
      - us-gaap_SalesRevenueNet

### http://www.microsoft.com/taxonomy/role/DisclosureRevenueClassifiedBySignificantProductAndServiceOfferings

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ProductOrServiceAxis
      - us-gaap_ProductsAndServicesDomain
    - us-gaap_EntityWideInformationRevenueFromExternalCustomerLineItems
      - us-gaap_SalesRevenueNet

### http://www.microsoft.com/taxonomy/role/DisclosureRevenueClassifiedBySignificantProductAndServiceOfferingsParenthetical

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DeferredRevenueArrangementTypeAxis
      - us-gaap_DeferredRevenueArrangementTypeDomain
    - msft_ProductsOrServicesSecondaryCategorizationAxis
      - msft_ProductsOrServicesNameSecondaryCategorizationDomain
    - us-gaap_EntityWideInformationRevenueFromExternalCustomerLineItems
      - us-gaap_SalesRevenueNet

### http://www.microsoft.com/taxonomy/role/DisclosureQuarterlyInformationUnauditedParenthetical

- us-gaap_DeferredRevenueArrangementTypeAxis
  - us-gaap_DeferredRevenueArrangementTypeDomain
    - msft_WindowsTenDeferralMember

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsEarningsPerShareTextBlock

- us-gaap_EarningsPerShareAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_EarningsPerShareTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsEarningsPerShareTextBlockTables

- us-gaap_EarningsPerShareAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsOtherIncomeAndOtherExpenseDisclosureTextBlock

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_OtherIncomeAndOtherExpenseDisclosureTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsOtherIncomeAndOtherExpenseDisclosureTextBlockTables

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfOtherNonoperatingIncomeExpenseTableTextBlock
      - us-gaap_RealizedGainLossOnInvestmentsTableTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsIncomeTaxDisclosureTextBlock

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsIncomeTaxDisclosureTextBlockTables

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

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsDeferredRevenueDisclosureTextBlock

- us-gaap_DeferredRevenueDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_DeferredRevenueDisclosureTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsDeferredRevenueDisclosureTextBlockTables

- us-gaap_DeferredRevenueDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - msft_DeferredRevenueBySegmentTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsComprehensiveIncomeNoteTextBlock

- us-gaap_EquityAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ComprehensiveIncomeNoteTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsComprehensiveIncomeNoteTextBlockTables

- us-gaap_EquityAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfAccumulatedOtherComprehensiveIncomeLossTableTextBlock

## 资产负债表结构 (Balance Sheet Structure)

### http://www.microsoft.com/taxonomy/role/StatementOfFinancialPositionClassified

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAndStockholdersEquityAbstract

### http://www.microsoft.com/taxonomy/role/StatementOfFinancialPositionClassifiedParenthetical

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

### http://www.microsoft.com/taxonomy/role/StatementOfCashFlowsIndirect

- us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperationsAbstract
  - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
  - msft_AcquisitionsNetofCashAcquiredAndPurchasesOfIntangibleandOtherAssets
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

### http://www.microsoft.com/taxonomy/role/DisclosureInvestmentComponentsIncludingAssociatedDerivativesButExcludingHeldToMaturityInvestments

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
      - us-gaap_Cash
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_AvailableForSaleSecuritiesCurrent
      - msft_LongTermInvestmentsExcludingHeldToMaturity

### http://www.microsoft.com/taxonomy/role/DisclosureInvestmentsCostMethodAdditionalInformation

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_ScheduleOfCostMethodInvestmentsTable

### http://www.microsoft.com/taxonomy/role/DisclosureInvestmentsSecuredBorrowingsAndLoanedSecuritiesAdditionalInformation

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - invest_InvestmentTable

### http://www.microsoft.com/taxonomy/role/DisclosureUnrealizedLossesOnInvestments

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - msft_InvestmentsUnrealizedLossPositionTable
- us-gaap_MajorTypesOfDebtAndEquitySecuritiesAxis
  - us-gaap_MajorTypesOfDebtAndEquitySecuritiesDomain
    - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
    - us-gaap_ForeignGovernmentDebtSecuritiesMember
    - us-gaap_AssetBackedSecuritiesMember
    - us-gaap_CorporateDebtSecuritiesMember
    - us-gaap_USStatesAndPoliticalSubdivisionsMember
    - us-gaap_EquitySecuritiesMember

### http://www.microsoft.com/taxonomy/role/DisclosureDebtInvestmentMaturities

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - msft_InvestmentsClassifiedByContractualMaturityDateTable

### http://www.microsoft.com/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedges

- msft_GainLossOnCashFlowHedgeEffectivenessNetAbstract
  - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodNetOfTax
  - us-gaap_ForeignCurrencyCashFlowHedgeGainLossReclassifiedToEarningsNet

### http://www.microsoft.com/taxonomy/role/DisclosureAssetsAndLiabilitiesMeasuredAtFairValueOnRecurringBasis

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - msft_RightOfOffsetAndNettingAxis
      - msft_RightOfOffsetAndNettingDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueByAssetClassAxis
      - us-gaap_FairValueAssetsMeasuredOnRecurringBasisUnobservableInputReconciliationByAssetClassDomain
    - us-gaap_FairValueByLiabilityClassAxis
      - us-gaap_FairValueLiabilitiesMeasuredOnRecurringBasisUnobservableInputReconciliationByLiabilityClassDomain
    - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
      - us-gaap_AssetsFairValueDisclosureRecurring
      - us-gaap_LiabilitiesFairValueDisclosureRecurring

### http://www.microsoft.com/taxonomy/role/DisclosureReconciliationOfTotalAssetsMeasuredAtFairValueOnRecurringBasisToBalanceSheetPresentation

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
      - us-gaap_DerivativeAssetsCurrent
      - us-gaap_OtherAssetsFairValueDisclosure
      - us-gaap_AvailableForSaleSecurities [totalLabel]

### http://www.microsoft.com/taxonomy/role/DisclosureMajorClassesOfAssetsAndLiabilitiesToWhichWeAllocatedThePurchasePrice

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCashAndEquivalents
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCurrentAssetsReceivables
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedInventory
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCurrentAssetsOther
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedPropertyPlantAndEquipment
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles
      - us-gaap_Goodwill
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedOtherNoncurrentAssets
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCurrentLiabilities
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedNoncurrentLiabilities
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredGoodwillAndLiabilitiesAssumedNet [totalLabel]

### http://www.microsoft.com/taxonomy/role/DisclosureMajorClassesOfAssetsAndLiabilitiesToWhichWeAllocatedThePurchasePriceParenthetical

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationAcquiredReceivablesGrossContractualAmount
      - us-gaap_BusinessCombinationAcquiredReceivablesEstimatedUncollectible

### http://www.microsoft.com/taxonomy/role/DisclosureAcquiredIntangibleAssets

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

### http://www.microsoft.com/taxonomy/role/DisclosureCarryingAmountOfGoodwill

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTable

### http://www.microsoft.com/taxonomy/role/DisclosureGoodwillAdditionalInformation

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTable

### http://www.microsoft.com/taxonomy/role/DisclosureFiniteLivedIntangibleAssets

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

### http://www.microsoft.com/taxonomy/role/DisclosureFiniteLivedIntangibleAssetsParenthetical

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_CapitalizedSoftwareDevelopmentCostsForSoftwareSoldToCustomers

### http://www.microsoft.com/taxonomy/role/DisclosureIntangibleAssetsAdditionalInformation

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_ImpairmentOfIntangibleAssetsFinitelived
      - us-gaap_AmortizationOfIntangibleAssets
      - us-gaap_CapitalizedComputerSoftwareAmortization1

### http://www.microsoft.com/taxonomy/role/DisclosureIntangibleAssetsAcquired

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetByMajorClassTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_AcquiredFiniteLivedIntangibleAssetsLineItems
      - msft_AcquiredFiniteLivedIntangibleAssets
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.microsoft.com/taxonomy/role/DisclosureEstimatedFutureAmortizationExpenseRelatedToIntangibleAssets

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

### http://www.microsoft.com/taxonomy/role/DisclosureChangesInRestructuringLiability

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_ScheduleOfRestructuringAndRelatedCostsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_RestructuringCostAndReserveAxis
      - us-gaap_TypeOfRestructuringDomain
    - us-gaap_RestructuringCostAndReserveLineItems
      - us-gaap_RestructuringReserve
      - us-gaap_RestructuringCharges
      - us-gaap_RestructuringReserveAccrualAdjustment1
      - us-gaap_PaymentsForRestructuring
      - us-gaap_RestructuringReserveSettledWithoutCash2
      - us-gaap_RestructuringReserve

### http://www.microsoft.com/taxonomy/role/DisclosureFutureMinimumRentalCommitmentsUnderNoncancellableOperatingLeases

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

### http://www.microsoft.com/taxonomy/role/DisclosureSharesOfCommonStockOutstanding

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfCapitalUnitsTable

### http://www.microsoft.com/taxonomy/role/DisclosureStockholdersEquityAdditionalInformation

- us-gaap_StatementOfStockholdersEquityAbstract
  - msft_ShareRepurchasesTable

### http://www.microsoft.com/taxonomy/role/DisclosureShareRepurchases

- us-gaap_EquityAbstract
  - msft_ShareRepurchasesTable

### http://www.microsoft.com/taxonomy/role/DisclosureShareRepurchasesParenthetical

- us-gaap_EquityAbstract
  - msft_ShareRepurchasesTable

### http://www.microsoft.com/taxonomy/role/DisclosureDividendsDeclared

- us-gaap_EquityAbstract
  - msft_DividendsTable

### http://www.microsoft.com/taxonomy/role/DisclosureStockPlanActivity

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

### http://www.microsoft.com/taxonomy/role/DisclosureLongLivedAssetsExcludingFinancialInstrumentsAndTaxAssetsClassifiedByLocationOfControllingStatutoryCompany

- us-gaap_SegmentReportingAbstract
  - msft_CertainLongLivedAssetsByGeographyTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementGeographicalAxis
      - us-gaap_SegmentGeographicalDomain
    - msft_CertainLongLivedAssetsByGeographyLineItems
      - us-gaap_NoncurrentAssets

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsInvestmentsInDebtAndEquityInstrumentsCashAndCashEquivalentsUnrealizedAndRealizedGainsLossesTextBlock

- us-gaap_CashAndCashEquivalentsAbstract
  - us-gaap_StatementTable

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsInvestmentsInDebtAndEquityInstrumentsCashAndCashEquivalentsUnrealizedAndRealizedGainsLossesTextBlockTables

- us-gaap_CashAndCashEquivalentsAbstract
  - us-gaap_StatementTable

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsMergersAcquisitionsAndDispositionsDisclosuresTextBlock

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_MergersAcquisitionsAndDispositionsDisclosuresTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsMergersAcquisitionsAndDispositionsDisclosuresTextBlockTables

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTextBlock
      - us-gaap_BusinessAcquisitionProFormaInformationTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsIntangibleAssetsDisclosureTextBlockTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetsByMajorClassTextBlock
      - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTableTextBlock
      - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsGoodwillDisclosureTextBlock

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_StatementTable

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsGoodwillDisclosureTextBlockTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_StatementTable

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsIntangibleAssetsDisclosureTextBlock

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_IntangibleAssetsDisclosureTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsStockholdersEquityNoteDisclosureTextBlock

- us-gaap_EquityAbstract
  - us-gaap_StatementTable

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsStockholdersEquityNoteDisclosureTextBlockTables

- us-gaap_EquityAbstract
  - us-gaap_StatementTable

## 现金流量表结构 (Cash Flow Structure)

### http://www.microsoft.com/taxonomy/role/StatementOfCashFlowsIndirect

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

### http://www.microsoft.com/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedges

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

### http://www.microsoft.com/taxonomy/role/DisclosureGainsLossesRelatedToCashFlowHedgesParenthetical

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

### http://www.microsoft.com/taxonomy/role/DisclosureCommitmentsAdditionalInformation

- us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAxis
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseDomain
    - us-gaap_BuildingMember

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsInvestmentsInDebtAndEquityInstrumentsCashAndCashEquivalentsUnrealizedAndRealizedGainsLossesTextBlock

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_InvestmentsInDebtAndEquityInstrumentsCashAndCashEquivalentsUnrealizedAndRealizedGainsLossesTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsInvestmentsInDebtAndEquityInstrumentsCashAndCashEquivalentsUnrealizedAndRealizedGainsLossesTextBlockTables

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - msft_ScheduleOfCashCashEquivalentsAndInvestmentsTableTextBlock
    - us-gaap_ScheduleOfUnrealizedLossOnInvestmentsTableTextBlock
    - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock

## 股东权益结构 (Equity Structure)

### http://www.microsoft.com/taxonomy/role/DisclosureSharesOfCommonStockOutstanding

- us-gaap_ScheduleOfCapitalUnitsTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_CapitalUnitLineItems
    - us-gaap_CommonStockSharesOutstanding
    - us-gaap_StockIssuedDuringPeriodSharesNewIssues
    - us-gaap_StockRepurchasedDuringPeriodShares
    - us-gaap_CommonStockSharesOutstanding

### http://www.microsoft.com/taxonomy/role/DisclosureStockholdersEquityAdditionalInformation

- msft_ShareRepurchasesTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - msft_ShareRepurchasesLineItems
    - us-gaap_StockRepurchaseProgramAuthorizedAmount1
    - us-gaap_StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1

### http://www.microsoft.com/taxonomy/role/DisclosureShareRepurchases

- msft_ShareRepurchasesTable
  - dei_LegalEntityAxis
  - msft_ShareRepurchasesLineItems
    - us-gaap_StockRepurchasedDuringPeriodShares
    - us-gaap_StockRepurchasedDuringPeriodValue

### http://www.microsoft.com/taxonomy/role/DisclosureShareRepurchasesParenthetical

- msft_ShareRepurchasesTable
  - dei_LegalEntityAxis
  - us-gaap_ShareRepurchaseProgramAxis
    - us-gaap_ShareRepurchaseProgramDomain
      - msft_ShareRepurchaseProgramTwentyThirteenMember
      - msft_ShareRepurchaseProgramTwentyZeroEightMember
  - msft_ShareRepurchasesLineItems
    - us-gaap_StockRepurchasedDuringPeriodShares
    - us-gaap_StockRepurchasedDuringPeriodValue

### http://www.microsoft.com/taxonomy/role/DisclosureEmployeeStockAndSavingsPlansAdditionalInformation

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - msft_CompensationRelatedCostsDisclosureTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_PlanNameAxis
      - us-gaap_PlanNameDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_DeferredCompensationArrangementWithIndividualPostretirementBenefitsByTypeOfDeferredCompensationAxis
      - us-gaap_OtherPostretirementBenefitsIndividualContractsTypeOfDeferredCompensationDomain
    - msft_CompensationRelatedCostsDisclosureLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAuthorized
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardPurchasePriceOfCommonStockPercent
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardMaximumEmployeeSubscriptionRate
      - msft_ShareBasedCompensationArrangementByEmployeeStockPurchasePlanNumberOfSharesAuthorized
      - us-gaap_DefinedContributionPlanEmployerMatchingContributionPercentOfMatch
      - us-gaap_DefinedContributionPlanEmployerMatchingContributionPercent
      - us-gaap_DefinedContributionPlanCostRecognized

### http://www.microsoft.com/taxonomy/role/DisclosureAssumptionsUsedInEstimatingTheFairValueOfStockAwardGrants

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

### http://www.microsoft.com/taxonomy/role/DisclosureStockPlanActivity

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward

### http://www.microsoft.com/taxonomy/role/DisclosureEmployeePurchasedShares

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - msft_EmployeeStockPurchasePlanTable
    - dei_LegalEntityAxis
    - msft_EmployeeStockPurchasePlanLineItems
      - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockPurchasePlans
      - msft_StockIssuedEmployeeStockPurchasePlanAveragePricePerShare

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsStockholdersEquityNoteDisclosureTextBlock

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsStockholdersEquityNoteDisclosureTextBlockTables

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_ScheduleOfCommonStockOutstandingRollForwardTableTextBlock
    - msft_ShareRepurchaseProgramDisclosureTableTextBlock
    - us-gaap_DividendsDeclaredTableTextBlock

## 其他结构 (Other Structure)

### http://www.microsoft.com/taxonomy/role/DocumentandEntityInformation

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

### http://www.microsoft.com/taxonomy/role/DisclosureAccountingPoliciesAdditionalInformation

- us-gaap_AccountingPoliciesAbstract
  - msft_SignificantAccountingPoliciesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DeferredRevenueArrangementTypeAxis
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - msft_SignificantAccountingPoliciesLineItems
      - msft_RevenueRecognitionPeriod
      - us-gaap_AdvertisingExpense
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperations
      - us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperations
      - us-gaap_IncomeTaxExpenseBenefit

### http://www.microsoft.com/taxonomy/role/DisclosureAllowanceForDoubtfulAccounts

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

### http://www.microsoft.com/taxonomy/role/DisclosureAdoptionOfNewStandardImpactOnPreviouslyReportedResults

- us-gaap_AccountingChangesAndErrorCorrectionsAbstract
  - us-gaap_NewAccountingPronouncementsOrChangeInAccountingPrincipleTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_NewAccountingPronouncementsOrChangeInAccountingPrincipleLineItems
      - us-gaap_StatementOfFinancialPositionAbstract

### http://www.microsoft.com/taxonomy/role/DisclosureNetRecognizedGainsLossesOnInvestments

- us-gaap_ScheduleOfGainLossOnInvestmentsTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_ScheduleOfGainLossOnInvestmentsIncludingMarketableSecuritiesAndInvestmentsHeldAtCostIncomeStatementReportedAmountsSummaryLineItems

### http://www.microsoft.com/taxonomy/role/DisclosureInvestmentComponentsIncludingAssociatedDerivativesButExcludingHeldToMaturityInvestments

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

### http://www.microsoft.com/taxonomy/role/DisclosureInvestmentsCostMethodAdditionalInformation

- us-gaap_ScheduleOfCostMethodInvestmentsTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_FairValueByMeasurementFrequencyAxis
    - us-gaap_FairValueMeasurementFrequencyDomain
      - us-gaap_FairValueMeasurementsNonrecurringMember
  - us-gaap_ScheduleOfCostMethodInvestmentsLineItems
    - us-gaap_CostMethodInvestments

### http://www.microsoft.com/taxonomy/role/DisclosureInvestmentsSecuredBorrowingsAndLoanedSecuritiesAdditionalInformation

- invest_InvestmentTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - invest_InvestmentLineItems
    - us-gaap_SecuritiesReceivedAsCollateral

### http://www.microsoft.com/taxonomy/role/DisclosureUnrealizedLossesOnInvestments

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

### http://www.microsoft.com/taxonomy/role/DisclosureDebtInvestmentMaturities

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

### http://www.microsoft.com/taxonomy/role/DisclosureDerivativesAdditionalInformation

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_PositionAxis
      - us-gaap_PositionDomain
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DerivativeLineItems
      - us-gaap_MaximumLengthOfTimeForeignCurrencyCashFlowHedge
      - invest_DerivativeNotionalAmount
      - msft_FinancialInstrumentCovenantMinimumLiquidityRequirement
      - us-gaap_DebtInstrumentCreditRating
      - msft_FinancialInstrumentCovenantMinimumLiquidity
      - us-gaap_ForeignCurrencyCashFlowHedgeGainLossToBeReclassifiedDuringNext12Months

### http://www.microsoft.com/taxonomy/role/DisclosureFairValuesOfDerivativeInstruments

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_FairValuesDerivativesBalanceSheetLocationByDerivativeContractTypeByHedgingDesignationTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
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

### http://www.microsoft.com/taxonomy/role/DisclosureGainsLossesOnFairValueHedgesAndRelatedHedgedItems

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

### http://www.microsoft.com/taxonomy/role/DisclosureNonDesignatedDerivativeGainsLosses

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

### http://www.microsoft.com/taxonomy/role/DisclosureComponentsOfInventories

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryCurrentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_InventoryLineItems
      - us-gaap_InventoryRawMaterialsNetOfReserves
      - us-gaap_InventoryWorkInProcessNetOfReserves
      - us-gaap_InventoryFinishedGoodsNetOfReserves
      - us-gaap_InventoryNet [totalLabel]

### http://www.microsoft.com/taxonomy/role/DisclosureComponentsOfPropertyAndEquipment

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

### http://www.microsoft.com/taxonomy/role/DisclosurePropertyAndEquipmentAdditionalInformation

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_Depreciation

### http://www.microsoft.com/taxonomy/role/DisclosureBusinessCombinationsAdditionalInformation

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_InvestmentTypeAxis
      - us-gaap_InvestmentTypeCategorizationMember
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - invest_InvestmentIssuerAxis
      - invest_InvestmentIssuerDomain
    - us-gaap_OtherCommitmentsAxis
      - us-gaap_OtherCommitmentsDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionNameOfAcquiredEntity
      - us-gaap_BusinessAcquisitionEffectiveDateOfAcquisition1
      - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
      - us-gaap_Goodwill
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife
      - us-gaap_BusinessCombinationConsiderationTransferred1
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCashAndEquivalents
      - us-gaap_PaymentsToAcquireBusinessesGross
      - msft_ComponentOfNonCashTransactionToAcquireBusiness
      - us-gaap_BusinessCombinationConsiderationTransferredLiabilitiesIncurred
      - us-gaap_AssetImpairmentCharges
      - us-gaap_DisposalGroupIncludingDiscontinuedOperationConsideration
      - us-gaap_BusinessCombinationProFormaInformationRevenueOfAcquireeSinceAcquisitionDateActual
      - us-gaap_BusinessCombinationProFormaInformationEarningsOrLossOfAcquireeSinceAcquisitionDateActual
      - us-gaap_BusinessCombinationAcquisitionRelatedCosts
      - us-gaap_GainLossOnContractTermination
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - us-gaap_NumberOfBusinessesAcquired

### http://www.microsoft.com/taxonomy/role/DisclosureSupplementalConsolidatedResultsOnUnauditedProFormaBasisAsIfTheAcquisitionHadBeenConsummatedOnBeginningOfPeriod

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionsProFormaRevenue
      - us-gaap_BusinessAcquisitionsProFormaNetIncomeLoss
      - us-gaap_BusinessAcquisitionProFormaEarningsPerShareDiluted

### http://www.microsoft.com/taxonomy/role/DisclosureCarryingAmountOfGoodwill

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

### http://www.microsoft.com/taxonomy/role/DisclosureGoodwillAdditionalInformation

- us-gaap_ScheduleOfGoodwillTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementBusinessSegmentsAxis
    - us-gaap_SegmentDomain
      - msft_PhoneHardwareMember
  - us-gaap_GoodwillLineItems
    - us-gaap_GoodwillImpairmentLoss
    - us-gaap_GoodwillImpairedAccumulatedImpairmentLoss

### http://www.microsoft.com/taxonomy/role/DisclosureDebtAdditionalInformation

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
      - us-gaap_DebtInstrumentUnamortizedDiscount

### http://www.microsoft.com/taxonomy/role/DisclosureLongtermDebt

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

### http://www.microsoft.com/taxonomy/role/DisclosureLongtermDebtParenthetical

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount

### http://www.microsoft.com/taxonomy/role/DisclosureMaturitiesOfLongtermDebt

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

### http://www.microsoft.com/taxonomy/role/DisclosureChangesInUnrecognizedTaxBenefits

- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.microsoft.com/taxonomy/role/DisclosureRestructuringChargesAdditionalInformation

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_ScheduleOfRestructuringAndRelatedCostsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_RestructuringPlanAxis
      - us-gaap_RestructuringPlanDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_RestructuringCostAndReserveLineItems
      - us-gaap_RestructuringAndRelatedCostNumberOfPositionsEliminated
      - us-gaap_RestructuringAndRelatedActivitiesCompletionDate
      - us-gaap_RestructuringCharges
      - us-gaap_RestructuringReserveAccrualAdjustment1
      - us-gaap_RestructuringAndRelatedCostExpectedNumberOfPositionsEliminated

### http://www.microsoft.com/taxonomy/role/DisclosureCommitmentsAdditionalInformation

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - msft_CommitmentsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_LongTermPurchaseCommitmentByCategoryOfItemPurchasedAxis
      - us-gaap_LongTermPurchaseCommitmentCategoryOfItemPurchasedDomain
    - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAxis
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - msft_CommitmentsLineItems
      - us-gaap_CommitmentsFairValueDisclosure
      - us-gaap_LeaseAndRentalExpense

### http://www.microsoft.com/taxonomy/role/DisclosureFutureMinimumRentalCommitmentsUnderNoncancellableOperatingLeases

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_ScheduleOfOperatingLeasedAssetsTable
- us-gaap_PropertyPlantAndEquipmentByTypeAxis
  - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_BuildingMember
- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.microsoft.com/taxonomy/role/DisclosureContingenciesAdditionalInformation

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_LossContingenciesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_LossContingenciesLineItems
      - us-gaap_LossContingencyAccrualCarryingValueCurrent
      - us-gaap_LossContingencyRangeOfPossibleLossPortionNotAccrued

### http://www.microsoft.com/taxonomy/role/DisclosureShareRepurchases

- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.microsoft.com/taxonomy/role/DisclosureShareRepurchasesParenthetical

- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.microsoft.com/taxonomy/role/DisclosureDividendsDeclared

- msft_DividendsTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - msft_DividendsLineItems
    - us-gaap_DividendsPayableDateDeclaredDayMonthAndYear
    - us-gaap_CommonStockDividendsPerShareDeclared
    - us-gaap_DividendsPayableDateOfRecordDayMonthAndYear
    - us-gaap_DividendsCommonStockCash
    - us-gaap_DividendPayableDateToBePaidDayMonthAndYear

### http://www.microsoft.com/taxonomy/role/DisclosureEmployeePurchasedShares

- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.microsoft.com/taxonomy/role/DisclosureSegmentInformationAndGeographicDataAdditionalInformation

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_SegmentReportingDisclosureOfMajorCustomers

### http://www.microsoft.com/taxonomy/role/DisclosureQuarterlyInformationUnaudited

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

### http://www.microsoft.com/taxonomy/role/DisclosureQuarterlyInformationUnauditedParenthetical

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - msft_QuarterlyFinancialInformationTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_DeferredRevenueArrangementTypeAxis
    - msft_QuarterlyFinancialInformationLineItems
      - us-gaap_SalesRevenueNet
      - us-gaap_AssetImpairmentCharges
      - msft_IntegrationAndRestructuringExpenses
      - msft_ImpairmentIntegrationAndRestructuringEffectOnEarningsAfterTax
      - msft_ImpairmentIntegrationAndRestructuringEffectOnEarningsPerShareAfterTax

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsSignificantAccountingPoliciesTextBlock

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_SignificantAccountingPoliciesTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsSignificantAccountingPoliciesTextBlockPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_BasisOfAccountingPolicyPolicyTextBlock
      - us-gaap_ConsolidationPolicyTextBlock
      - us-gaap_SegmentReportingPolicyPolicyTextBlock
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

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsSignificantAccountingPoliciesTextBlockTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfCreditLossesForFinancingReceivablesCurrentTableTextBlock
      - us-gaap_ScheduleOfNewAccountingPronouncementsAndChangesInAccountingPrinciplesTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsDerivativeInstrumentsAndHedgingActivitiesDisclosureTextBlock

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsDerivativeInstrumentsAndHedgingActivitiesDisclosureTextBlockTables

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_StatementTable
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfDerivativeInstrumentsInStatementOfFinancialPositionFairValueTextBlock
      - us-gaap_ScheduleOfDerivativeInstrumentsGainLossInStatementOfFinancialPerformanceTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsFairValueDisclosuresTextBlock

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_FairValueDisclosuresTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsFairValueDisclosuresTextBlockTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfFairValueAssetsAndLiabilitiesMeasuredOnRecurringBasisTableTextBlock
      - msft_ReconciliationOfAssetsMeasuredAtFairValueOnRecurringBasisToBalanceSheetPresentationTableTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsInventoryDisclosureTextBlock

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_InventoryDisclosureTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsInventoryDisclosureTextBlockTables

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfInventoryCurrentTableTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsPropertyPlantAndEquipmentDisclosureTextBlock

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsPropertyPlantAndEquipmentDisclosureTextBlockTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsGoodwillDisclosureTextBlock

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_GoodwillDisclosureTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsGoodwillDisclosureTextBlockTables

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_ScheduleOfGoodwillTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsDebtDisclosureTextBlock

- us-gaap_DebtDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_DebtDisclosureTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsDebtDisclosureTextBlockTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfDebtInstrumentsTextBlock
      - us-gaap_ScheduleOfMaturitiesOfLongTermDebtTableTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsRestructuringAndRelatedActivitiesDisclosureTextBlock

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_RestructuringAndRelatedActivitiesDisclosureTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsRestructuringAndRelatedActivitiesDisclosureTextBlockTables

- us-gaap_RestructuringAndRelatedActivitiesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfRestructuringReserveByTypeOfCostTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsCommitmentsDisclosureTextBlock

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_CommitmentsDisclosureTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsCommitmentsDisclosureTextBlockTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfFutureMinimumRentalPaymentsForOperatingLeasesTableTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsLegalMattersAndContingenciesTextBlock

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_LegalMattersAndContingenciesTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsCompensationAndEmployeeBenefitPlansTextBlock

- us-gaap_PostemploymentBenefitsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_CompensationAndEmployeeBenefitPlansTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsCompensationAndEmployeeBenefitPlansTextBlockTables

- us-gaap_PostemploymentBenefitsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfCompensationCostForShareBasedPaymentArrangementsAllocationOfShareBasedCompensationCostsByPlanTableTextBlock
      - msft_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsMethodUsedTableTextBlock
      - us-gaap_DisclosureOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTextBlock
      - us-gaap_ScheduleOfShareBasedCompensationEmployeeStockPurchasePlanActivityTableTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsSegmentReportingDisclosureTextBlock

- us-gaap_SegmentReportingAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsSegmentReportingDisclosureTextBlockTables

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

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsQuarterlyFinancialInformationTextBlock

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_QuarterlyFinancialInformationTextBlock

### http://www.microsoft.com/taxonomy/role/NotesToFinancialStatementsQuarterlyFinancialInformationTextBlockTables

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfQuarterlyFinancialInformationTableTextBlock

