# TSLA 2017 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.teslamotors.com/20161231/taxonomy/role/StatementConsolidatedStatementsOfOperations

- us-gaap_IncomeStatementAbstract
  - us-gaap_RevenuesAbstract
    - us-gaap_SalesRevenueGoodsNet
    - us-gaap_OperatingLeasesIncomeStatementLeaseRevenue
    - tsla_SalesRevenueAutomotive [totalLabel]
    - us-gaap_SalesRevenueEnergyServices
    - tsla_SalesRevenueServicesAndOtherNet
    - us-gaap_Revenues [totalLabel]
  - us-gaap_CostOfRevenueAbstract
    - us-gaap_CostOfGoodsSold
    - tsla_CostOfAutomotiveLeasing
    - tsla_CostOfRevenuesAutomotive [totalLabel]
    - us-gaap_CostOfServicesEnergyServices
    - tsla_CostOfServicesAndOther
    - us-gaap_CostOfRevenue [totalLabel]
    - us-gaap_GrossProfit [totalLabel]
  - us-gaap_OperatingExpensesAbstract
    - us-gaap_ResearchAndDevelopmentExpense
    - us-gaap_SellingGeneralAndAdministrativeExpense
    - us-gaap_OperatingExpenses [totalLabel]
  - us-gaap_OperatingIncomeLoss [totalLabel]
  - us-gaap_InvestmentIncomeInterest
  - us-gaap_InterestExpense
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]
  - us-gaap_IncomeTaxExpenseBenefit
  - us-gaap_ProfitLoss [totalLabel]
  - us-gaap_NetIncomeLossAttributableToNoncontrollingInterest
  - us-gaap_NetIncomeLossAvailableToCommonStockholdersBasic [totalLabel]
  - us-gaap_EarningsPerShareBasicAndDiluted
  - us-gaap_WeightedAverageNumberOfShareOutstandingBasicAndDiluted

### http://www.teslamotors.com/20161231/taxonomy/role/StatementConsolidatedStatementsOfComprehensiveLoss

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParentAbstract
  - tsla_OtherComprehensiveIncomeChangeInUnrealizedGainLossOnDerivativesAndSecuritiesArisingDuringPeriodNetOfTax
  - tsla_OtherComprehensiveGainLossReclassificationAdjustmentOnDerivativesAndSecuritiesNetOfTax
  - tsla_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesAndSecuritiesArisingDuringPeriodNetOfTax [totalLabel]
  - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.teslamotors.com/20161231/taxonomy/role/StatementConsolidatedStatementsOfCashFlows

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_DepreciationAndAmortization
  - us-gaap_ShareBasedCompensation
  - tsla_AmortizationOfDebtDiscountLessCapitalizedInterest
  - us-gaap_InventoryWriteDown
  - us-gaap_GainLossOnSaleOfPropertyPlantEquipment
  - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
  - tsla_GainsLossOnAcquisition
  - tsla_NoncashInterestIncomeExpenseAndOtherOperatingActivities
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureIncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureIncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_SummaryOfPositionsForWhichSignificantChangeInUnrecognizedTaxBenefitsIsReasonablyPossibleTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_DeferredRevenueArrangementTypeAxis
  - us-gaap_DeferredRevenueArrangementTypeDomain
    - tsla_VehicleMaintenanceAndServicePlanMember
    - tsla_CustomerAdvancePaymentsMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfAccountActivityRelatedToResaleValueGuaranteeProgramDetail

- us-gaap_DeferredRevenueLeasesNetAbstract
  - us-gaap_DeferredRevenue
  - tsla_IncreaseDecreaseInDeferredRevenueAndReclassificationOfCollateralizedBorrowingFromLongTermToShortTerm
  - tsla_IncreaseDecreaseInDeferredRevenueFromAmortizationOfDeferredRevenue
  - tsla_IncreaseDecreaseInDeferredRevenueFromDepreciationExpenseOfEarlyCancellationOfResaleValueGuarantee
  - tsla_IncreaseDecreaseInReleaseOfDeferredRevenueUnderTradeInProgressExpirationAndExercisesOfResaleValueGuarantee
  - us-gaap_DeferredRevenue

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsAdditionalInformationDetail

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - tsla_AutomotiveCostMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfStockBasedCompensationExpenseDetail

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember
    - tsla_SellingGeneralAndAdministrativeExpenseMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureIncomeTaxesAdditionalInformationDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - tsla_IncomeTaxesTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - tsla_IncomeTaxesLineItems
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_ValuationAllowanceDeferredTaxAssetChangeInAmount
      - us-gaap_DeferredTaxAssetsNet
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_IncomeTaxEffectsAllocatedDirectlyToEquityEmployeeStockOptions
      - us-gaap_OperatingLossCarryforwardsExpirationDate
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsResearch
      - tsla_ResearchTaxCreditCarryForwardExpirationDates
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsGeneralBusiness
      - tsla_TaxCreditCarryForwardExpirationYear
      - us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings
      - tsla_UnrecognizedTaxBenefitsOfDeferredTaxAccountingThatWouldNotImpactAnnualEffectiveRate
      - us-gaap_IncomeTaxExaminationYearUnderExamination

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureIncomeTaxesScheduleOfLossBeforeIncomeTaxesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
  - tsla_IncomeLossFromContinuingOperationsBeforeIncomeTaxesAttributableToNoncontrollingInterestAndRedeemableNoncontrollingInterest
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureIncomeTaxesComponentsOfProvisionForIncomeTaxesDetail

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

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureIncomeTaxesScheduleOfDeferredTaxAssetsLiabilitiesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
    - us-gaap_DeferredTaxAssetsOperatingLossCarryforwards
    - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsResearch
    - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsOther
    - us-gaap_DeferredTaxAssetsDeferredIncome
    - us-gaap_DeferredTaxAssetsInventory
    - us-gaap_DeferredTaxAssetsPropertyPlantAndEquipment
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
    - us-gaap_DeferredTaxAssetsDerivativeInstruments
    - us-gaap_DeferredTaxAssetsInvestments
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccrualsOther
    - us-gaap_DeferredTaxAssetsGross [totalLabel]
    - us-gaap_DeferredTaxAssetsValuationAllowance
    - us-gaap_DeferredTaxAssetsNet [totalLabel]
  - us-gaap_ComponentsOfDeferredTaxLiabilitiesAbstract
    - us-gaap_DeferredTaxLiabilitiesPropertyPlantAndEquipment
    - us-gaap_DeferredTaxLiabilitiesOther
    - us-gaap_DeferredTaxLiabilitiesDerivatives
    - us-gaap_DeferredIncomeTaxLiabilities
    - us-gaap_DeferredTaxLiabilities
    - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureIncomeTaxesScheduleOfReconciliationOfStatutoryFederalIncomeTaxesToEffectiveTaxesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
  - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
  - us-gaap_IncomeTaxReconciliationNondeductibleExpense
  - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
  - us-gaap_IncomeTaxReconciliationTaxCredits
  - us-gaap_IncomeTaxReconciliationMinorityInterestIncomeExpense
  - us-gaap_IncomeTaxReconciliationTaxCreditsInvestment
  - us-gaap_IncomeTaxReconciliationOtherReconcilingItems
  - us-gaap_IncomeTaxReconciliationChangeInDeferredTaxAssetsValuationAllowance
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureIncomeTaxesScheduleOfAggregateChangesInBalanceOfGrossUnrecognizedTaxBenefitsDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_UnrecognizedTaxBenefits
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromAcquisition
  - us-gaap_UnrecognizedTaxBenefits

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfTotalRevenuesAndGrossMarginByReportableSegmentDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingRevenueReconcilingItemLineItems
      - us-gaap_Revenues
      - us-gaap_GrossProfit

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfRevenuesByGeographicAreaDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
    - us-gaap_StatementGeographicalAxis
      - us-gaap_SegmentGeographicalDomain
    - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
      - us-gaap_Revenues

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfLongLivedAssetsByGeographicAreaDetail

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - us-gaap_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

## 资产负债表结构 (Balance Sheet Structure)

### http://www.teslamotors.com/20161231/taxonomy/role/StatementConsolidatedBalanceSheets

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_StatementLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAndStockholdersEquityAbstract

### http://www.teslamotors.com/20161231/taxonomy/role/StatementConsolidatedBalanceSheetsParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_PreferredStockParOrStatedValuePerShare
  - us-gaap_PreferredStockSharesAuthorized
  - us-gaap_PreferredStockSharesIssued
  - us-gaap_PreferredStockSharesOutstanding
  - us-gaap_CommonStockParOrStatedValuePerShare
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_CommonStockSharesIssued
  - us-gaap_CommonStockSharesOutstanding

### http://www.teslamotors.com/20161231/taxonomy/role/StatementConsolidatedStatementsOfRedeemableNoncontrollingInterestAndStockholdersEquity

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember
    - us-gaap_AdditionalPaidInCapitalMember
    - us-gaap_RetainedEarningsMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
    - us-gaap_ParentMember
    - us-gaap_NoncontrollingInterestMember
- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable

### http://www.teslamotors.com/20161231/taxonomy/role/StatementConsolidatedStatementsOfRedeemableNoncontrollingInterestAndStockholdersEquityParenthetical

- us-gaap_StatementOfStockholdersEquityAbstract
  - tsla_CommonStockOfferingPricePerShare
  - tsla_CommonStockPublicOfferingIssuanceCosts

### http://www.teslamotors.com/20161231/taxonomy/role/StatementConsolidatedStatementsOfCashFlows

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_ProfitLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperations [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
    - tsla_PaymentsForSolarEnergySystemsLeasedAndToBeLeased
    - us-gaap_PaymentsToAcquireMarketableSecurities
    - us-gaap_ProceedsFromSaleAndMaturityOfMarketableSecurities
    - us-gaap_IncreaseDecreaseInRestrictedCash
    - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
    - us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperations [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_ProceedsFromIssuanceOfCommonStock
    - tsla_ProceedsFromConvertibleAndOtherDebt
    - tsla_RepaymentsOfConvertibleAndOtherDebt
    - us-gaap_ProceedsFromSecuredNotesPayable
    - us-gaap_ProceedsFromIssuanceOfSharesUnderIncentiveAndShareBasedCompensationPlansIncludingStockOptions
    - us-gaap_ProceedsFromRepaymentsOfLongTermDebtAndCapitalSecurities
    - us-gaap_PaymentsOfFinancingCosts
    - us-gaap_ProceedsFromIssuanceOfWarrants
    - us-gaap_ProceedsFromIssuanceOfPrivatePlacement
    - us-gaap_PaymentsForProceedsFromHedgeFinancingActivities
    - us-gaap_ProceedsFromMinorityShareholders
    - us-gaap_PaymentsToMinorityShareholders
    - us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperations [totalLabel]
  - us-gaap_EffectOfExchangeRateOnCashAndCashEquivalents
  - us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease [totalLabel]
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_OtherNoncashInvestingAndFinancingItemsAbstract
    - tsla_SharesIssuedInConnectionOfBusinessCombinationAndAssumedVestedAwards
    - us-gaap_NoncashOrPartNoncashAcquisitionValueOfAssetsAcquired1
    - tsla_NonCashEstimatedFairMarketValueOfManufacturingFacility
  - us-gaap_SupplementalCashFlowInformationAbstract
    - us-gaap_InterestPaid
    - us-gaap_IncomeTaxesPaid

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureIntangibleAssets

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_IntangibleAssetsDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureCommonStock

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureIntangibleAssetsTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetsByMajorClassTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_RegulatoryLiabilityAxis
  - us-gaap_RegulatoryLiabilityDomain
    - us-gaap_DeferredLeaseRevenueMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfAccountActivityRelatedToResaleValueGuaranteeProgramDetail

- us-gaap_ScheduleOfOperatingLeasedAssetsTable
  - us-gaap_GuaranteeObligationsByNatureAxis
  - us-gaap_OperatingLeasedAssetsLineItems
    - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseNetAbstract
    - us-gaap_DeferredRevenueLeasesNetAbstract
    - us-gaap_DisclosureOfResaleAgreementsAbstract
    - tsla_IncreaseDecreaseInReleaseOfResaleValueGuaranteeUnderTradeInProgressAndExercises
    - tsla_IncreaseDecreaseInReleaseOfResaleValueGuaranteeFromExpiration

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesEstimatedUsefulLivesOfRespectiveAssetsDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_LesseeLeasingArrangementsOperatingLeasesTermOfContract

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfEstimatedUsefulLivesOfRelatedAssetsDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureAcquisitionOfSolarcityAdditionalInformationDetail

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureAcquisitionOfSolarcityScheduleOfFairValueOfConsiderationTransferredAsOfAcquisitionDateParentheticalDetail

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureAcquisitionOfSolarcityScheduleOfFairValuesOfAssetsAcquiredAndLiabilitiesAssumedDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedAssetsAbstract
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedLiabilitiesAbstract
      - tsla_BusinessCombinationAcquisitionOfLessThan100PercentRedeemableAndNonRedeemableNoncontrollingInterestFairValue
      - tsla_BusinessCombinationCappedCallOptionsAssociatedWithConvertibleNotes
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredGoodwillAndLiabilitiesAssumedLessNoncontrollingInterest [totalLabel]
      - us-gaap_BusinessCombinationSeparatelyRecognizedTransactionsNetGainsAndLosses
      - us-gaap_BusinessCombinationConsiderationTransferred1

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureAcquisitionOfSolarcityScheduleOfFairValueOfIdentifiedIntangibleAssetsAndTheirUsefulLivesDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_IndefiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_IndefiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_FiniteLivedIntangibleAssetsFairValueDisclosure
      - us-gaap_IndefiniteLivedIntangibleAssetsExcludingGoodwill
      - us-gaap_IntangibleAssetsGrossExcludingGoodwill
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureIntangibleAssetsSummaryOfAcquiredIntangibleAssetsDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - tsla_ScheduleOfAcquiredIntangibleAssetsTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_IndefiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_IndefiniteLivedIntangibleAssetsMajorClassNameDomain
    - tsla_AcquiredIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]
      - us-gaap_IndefiniteLivedIntangibleAssetsExcludingGoodwill
      - us-gaap_IntangibleAssetsGrossExcludingGoodwill
      - us-gaap_IntangibleAssetsNetExcludingGoodwill [totalLabel]

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureIntangibleAssetsTotalFutureAmortizationExpenseForIntangibleAssetsDetail

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfFairValueHierarchyOfFinancialAssetsCarriedAtFairValueDetail

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

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfEstimatedFairValuesAndTheirCarryingValuesDetail

- us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
  - us-gaap_DebtInstrumentAxis
  - us-gaap_FinancialInstrumentAxis
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
    - us-gaap_NotesReceivableNet
    - us-gaap_LongTermDebt
    - us-gaap_LongTermDebtFairValue
    - us-gaap_NotesReceivableFairValueDisclosure

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNetComponentsOfSolarEnergySystemsLeasedAndToBeLeasedParentheticalDetail

- us-gaap_CapitalLeasedAssetsLineItems
  - us-gaap_CapitalLeasedAssetsGross
  - us-gaap_CapitalLeasesLesseeBalanceSheetAssetsByMajorClassAccumulatedDeprecation

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligations025And125ConvertibleSeniorNotesDueIn2019And2021AndBondHedgeAndWarrantTransactionsAdditionalInformationDetail

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_WarrantMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligations150ConvertibleSeniorNotesDueIn2018AndBondHedgeAndWarrantTransactionsAdditionalInformationDetail

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_WarrantMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsAssetBasedCreditFacilityAdditionalInformationDetail

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
      - tsla_LineOfCreditFacilityAdditionalBorrowingCapacity
      - us-gaap_LineOfCreditFacilityCurrentBorrowingCapacity
      - us-gaap_LineOfCredit
      - tsla_LinesOfCreditSwingLineLoan
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - us-gaap_LongTermDebt

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsSolarAssetBackedNotesAdditionalInformationDetail

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
      - tsla_LeaseFinancingObligations
      - tsla_LeaseFinancingObligationPayments

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsPledgedAssetsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_PledgedAssetsSeparatelyReportedOnStatementOfFinancialPositionAtFairValue

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureCommonStockAdditionalInformationDetail

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureEquityIncentivePlansAdditionalInformationDetail

- us-gaap_MajorTypesOfDebtAndEquitySecuritiesAxis
  - us-gaap_MajorTypesOfDebtAndEquitySecuritiesDomain
    - tsla_FirstModelXProductionVehicleMember
    - tsla_TwelveMonthMemberMember
    - tsla_FirstGenThreeProductionVehicleMemberMember
    - tsla_ThreeYearPeriodMemberMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureVIEArrangementsCarryingValuesOfAssetsAndLiabilitiesOfSubsidiaryInConsolidatedBalanceSheetsDetail

- tsla_VariableInterestEntityAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_VariableInterestEntityLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAbstract

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasScheduleOfLongLivedAssetsByGeographicAreaDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- us-gaap_StatementGeographicalAxis
  - us-gaap_SegmentGeographicalDomain
    - country_US
    - tsla_InternationalMember

## 现金流量表结构 (Cash Flow Structure)

### http://www.teslamotors.com/20161231/taxonomy/role/StatementConsolidatedStatementsOfCashFlows

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - tsla_IncreaseDecreaseInInventoriesAndPropertySubjectToOrAvailableForOperatingLease
  - us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets
  - us-gaap_IncreaseDecreaseInNotesReceivables
  - us-gaap_IncreaseDecreaseInOtherOperatingAssets
  - us-gaap_IncreaseDecreaseInAccountsPayableAndAccruedLiabilities
  - us-gaap_IncreaseDecreaseInDeferredRevenue
  - us-gaap_IncreaseDecreaseInDeferredRevenueAndCustomerAdvancesAndDeposits
  - tsla_IncreaseDecreaseInResaleValueGuarantee
  - us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNetTables

- us-gaap_PropertySubjectToOrAvailableForOperatingLeaseByMajorPropertyClassTable
  - us-gaap_MajorPropertyClassAxis
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseLineItems
    - us-gaap_ScheduleOfPropertySubjectToOrAvailableForOperatingLeaseTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationTables

- tsla_LeasePassThroughFinancingObligationAbstract
  - tsla_ScheduleOfFutureMinimumLeasePaymentsToBeReceivedForOperatingLeasesTableTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfAccountActivityRelatedToResaleValueGuaranteeProgramDetail

- us-gaap_PropertySubjectToOrAvailableForOperatingLeaseNetAbstract
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseGross
  - tsla_IncreaseDecreaseInInventoriesAndPropertySubjectToOrAvailableForOperatingLease
  - tsla_IncreaseDecreaseInPropertySubjectToOrAvailableForOperatingLeaseGrossFromDepreciationExpenseOfAutomotiveSales
  - tsla_IncreaseDecreaseInPropertySubjectToOrAvailableForOperatingLeaseGrossFromDepreciationExpenseOfEarlyCancellationOfResaleValueGuarantee
  - tsla_IncreaseDecreaseInPropertySubjectToOrAvailableForOperatingLeaseGrossFromDepreciationExpenseOfExpiration
  - tsla_IncreaseDecreaseInPropertySubjectToOrAvailableForOperatingLeaseGrossFromReclassificationToInventoryUnderTradeInProgramAndExercisesOfResaleValueGuarantee
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseGross

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNetComponentsOfSolarEnergySystemsLeasedAndToBeLeasedDetail

- us-gaap_PropertySubjectToOrAvailableForOperatingLeaseByMajorPropertyClassTable
  - us-gaap_PropertyPlantAndEquipmentByTypeAxis
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseLineItems
    - tsla_LeasedAssetsBeforeOverhead
    - tsla_LeasedAssetOverheadAllocation
    - tsla_LeasedAssetsGross [totalLabel]
    - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAccumulatedDepreciation
    - tsla_LeasedAssetsNet [totalLabel]
    - tsla_AssetsToBeLeasedCIP
    - tsla_AssetsToBeLeased
    - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseNet [totalLabel]

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsCashEquityDebtAdditionalInformationDetail

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
      - us-gaap_DebtInstrumentInterestRateStatedPercentage

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationAdditionalInformationDetail

- us-gaap_LeasesOperatingAbstract
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseByMajorPropertyClassTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
    - us-gaap_RangeAxis
    - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseLineItems
      - tsla_NumberOfLeaseFinancingObligations
      - us-gaap_LessorLeasingArrangementsOperatingLeasesTermOfContract
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseGross
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAccumulatedDepreciation
      - us-gaap_CapitalLeaseObligations
      - us-gaap_CapitalLeaseObligationsCurrent
      - us-gaap_LessorLeasingArrangementsOperatingLeasesRenewalTerm

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationScheduleOfFutureMinimumLeasePaymentsToBeReceivedForOperatingLeasesDetail

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

### http://www.teslamotors.com/20161231/taxonomy/role/StatementConsolidatedStatementsOfRedeemableNoncontrollingInterestAndStockholdersEquity

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementClassOfStockAxis
    - us-gaap_ClassOfStockDomain
      - tsla_RedeemableNoncontrollingInterestsMember
  - us-gaap_StatementLineItems
    - us-gaap_StockholdersEquity
    - us-gaap_SharesIssued
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalEquityComponentOfConvertibleDebt
    - tsla_AdjustmentsToAdditionalPaidInCapitalConvertibleDebtDiscount
    - tsla_AdjustmentsToAdditionalPaidInCapitalConvertibleDebtHedge
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalWarrantIssued
    - tsla_ReclassificationsOfPermanentEquityToTemporaryEquity
    - tsla_ReclassificationsOfPermanentEquityToTemporaryEquityShares
    - tsla_ReclassificationsOfTemporaryEquityToEquityComponentOfDebtInstrument
    - tsla_ReclassificationsOfTemporaryEquityToEquityComponentOfDebtInstrumentShares
    - tsla_AdjustmentsToAdditionalPaidInCapitalExerciseOfConversionFeatureOfConvertibleSeniorNotes
    - tsla_StockIssuedDuringPeriodValueWithheldForEmployeeTaxes
    - tsla_StockIssuedDuringPeriodSharesWithheldForEmployeeTaxes
    - us-gaap_StockIssuedDuringPeriodValueNewIssues
    - us-gaap_StockIssuedDuringPeriodSharesNewIssues
    - us-gaap_StockIssuedDuringPeriodValueAcquisitions
    - us-gaap_StockIssuedDuringPeriodSharesAcquisitions
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
    - tsla_AssumptionOfCappedCall
    - tsla_AcquisitionOfNoncontrollingInterestInSubsidiaries
    - us-gaap_NoncontrollingInterestIncreaseFromBusinessCombination
    - tsla_MinorityInterestDecreaseFromDistributionsToNoncontrollingInterestHoldersThroughAcquisition
    - us-gaap_ProfitLoss
    - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParent
    - us-gaap_StockholdersEquity
    - us-gaap_SharesIssued
    - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureEquityIncentivePlans

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ShareholdersEquityAndShareBasedPaymentsTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureEquityIncentivePlansTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationActivityTableTextBlock
  - tsla_ScheduleOfShareBasedPaymentAwardStockOptionsAndEmployeeStockPurchasePlanValuationAssumptionsTableTextBlock
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfPotentialWeightedCommonSharesOutstandingThatWereExcludedFromComputationOfBasicAndDilutedNetLossPerShareOfCommonStockDetail

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTable
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareByAntidilutiveSecuritiesAxis
      - us-gaap_AntidilutiveSecuritiesNameDomain
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareLineItems
      - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsZeroCouponConvertibleSeniorNotesDueIn2020AdditionalInformationDetail

- us-gaap_SubsidiarySaleOfStockAxis
  - us-gaap_SaleOfStockNameOfTransactionDomain
    - us-gaap_PrivatePlacementMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureCommonStockAdditionalInformationDetail

- us-gaap_CompensationRelatedCostsAbstract
  - tsla_OverviewOfCompanyTable
    - us-gaap_TitleOfIndividualAxis
      - us-gaap_TitleOfIndividualWithRelationshipToEntityDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_StatementEquityComponentsAxis
    - tsla_OverviewOfCompanyLineItems
      - us-gaap_StockIssuedDuringPeriodSharesNewIssues
      - us-gaap_StockIssuedDuringPeriodValueNewIssues
      - us-gaap_ConversionOfStockSharesIssued1
      - us-gaap_ConversionOfStockSharesConverted1

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureEquityIncentivePlansAdditionalInformationDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_PlanNameAxis
      - us-gaap_PlanNameDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_MajorTypesOfDebtAndEquitySecuritiesAxis
    - us-gaap_FinancialInstrumentPerformanceStatusAxis
      - us-gaap_FinancialInstrumentPerformanceStatusDomain
    - us-gaap_TitleOfIndividualAxis
      - us-gaap_TitleOfIndividualWithRelationshipToEntityDomain
    - us-gaap_VestingAxis
      - us-gaap_VestingDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_DeferredCompensationArrangementWithIndividualMaximumContractualTerm1
      - us-gaap_CommonStockCapitalSharesReservedForFutureIssuance
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue [totalLabel]
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodGross
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardDividedEquallyInNumberOfTranches
      - tsla_PortionOfStockOptionsScheduledToVestUponSuccessfulCompletionOfPerformanceObjectives
      - tsla_NumberOfVehicleProduction
      - tsla_GrossMargin
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - us-gaap_ShareBasedCompensation
      - tsla_NumberOfTranches
      - tsla_MarketCapitalization
      - tsla_InitialMarketCapitalization
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
      - tsla_CashCompensationReceivedForServices
      - tsla_PercentageOfPayrollDeductionsOfEmployeesEligibleCompensation
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardDiscountFromMarketPriceOfferingDate
      - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockPurchasePlans
      - us-gaap_StockIssuedDuringPeriodValueEmployeeStockPurchasePlan
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForIssuance

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfStockOptionAndRSUActivityUnderPlanDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_PlanNameAxis
      - us-gaap_PlanNameDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardSharesAssumedThroughAcquisition
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodGross
      - us-gaap_StockIssuedDuringPeriodSharesStockOptionsExercised
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsForfeituresInPeriod
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestOutstandingNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestExercisableNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
      - tsla_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsAssumedThroughAcquisitionWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsGrantsInPeriodWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsExercisesInPeriodWeightedAverageExercisePrice
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
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsAssumedThroughAcquisition
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExercised
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsReleased
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedAndExpectedToVest
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExercisableAndVested
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsAssumedThroughAcquisitionWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExercisedInPeriodWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValue
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsReleasedInPeriodWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureEquityIncentivePlansScheduleOfFairValueOfOptionAwardAndESPPOnGrantDateDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsRiskFreeInterestRate
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardFairValueAssumptionsExpectedTerm1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsExpectedVolatilityRate
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsExpectedDividendRate

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfStockBasedCompensationExpenseDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
      - us-gaap_AllocatedShareBasedCompensationExpense

## 其他结构 (Other Structure)

### http://www.teslamotors.com/20161231/taxonomy/role/DocumentDocumentAndEntityInformation

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
  - dei_EntityCommonStockSharesOutstanding
  - dei_EntityPublicFloat

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureOverviewOfCompany

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NatureOfOperations

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_SignificantAccountingPoliciesTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureAcquisitionOfSolarcity

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_BusinessCombinationDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureFairValueOfFinancialInstruments

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueDisclosuresTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureInventory

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNet

- us-gaap_LeasesAbstract
  - tsla_ComponentsOfPropertyLeasedAndToBeLeasedDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosurePropertyPlantAndEquipment

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureNonCancellableOperatingLeasePaymentsReceivable

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeasesOfLessorDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureAccruedLiabilitiesAndOther

- us-gaap_PayablesAndAccrualsAbstract
  - us-gaap_AccountsPayableAndAccruedLiabilitiesDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureOtherLongTermLiabilities

- us-gaap_OtherLiabilitiesAbstract
  - us-gaap_OtherLiabilitiesDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureCustomerDeposits

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - tsla_CustomerDepositsTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligations

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureCommitmentsAndContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureVIEArrangements

- tsla_VariableInterestEntityDisclosureAbstract
  - us-gaap_VariableInterestEntityDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureLeasePassThroughFinancingObligation

- us-gaap_LeasesAbstract
  - us-gaap_LeasesOfLessorDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureDefinedContributionPlan

- us-gaap_CompensationAndRetirementDisclosureAbstract
  - us-gaap_CompensationAndEmployeeBenefitPlansTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureRelatedPartyTransactions

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_RelatedPartyTransactionsDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureQuarterlyResultsOfOperations

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_QuarterlyFinancialInformationTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreas

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSubsequentEvents

- us-gaap_SubsequentEventsAbstract
  - us-gaap_SubsequentEventsTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesPolicies

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
  - tsla_PropertySubjectToOrAvailableForOperatingLeaseTextBlock
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_ImpairmentOrDisposalOfLongLivedAssetsIncludingIntangibleAssetsPolicyPolicyTextBlock
  - us-gaap_InternalUseSoftwarePolicy
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_StandardProductWarrantyPolicy
  - us-gaap_MinimumGuaranteesPolicy
  - tsla_SolarRenewableEnergyCreditsPolicyTextBlock
  - us-gaap_RevenueRecognitionDeferredRevenue
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - tsla_ScheduleOfActivityRelatedToResaleValueGuaranteeProgramTableTextBlock
  - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTextBlock
  - tsla_ScheduleOfDepreciationAndAmortizationComputedUsingStraightLineMethodOverEstimatedUsefulLivesOfAssetsTableTextBlock
  - tsla_ScheduleOfPropertyPlantAndEquipmentTextBlock
  - us-gaap_ScheduleOfProductWarrantyLiabilityTableTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureAcquisitionOfSolarcityTables

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTextBlock
  - us-gaap_ScheduleOfRecognizedIdentifiedAssetsAcquiredAndLiabilitiesAssumedTableTextBlock
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsAcquiredAsPartOfBusinessCombinationTextBlock
  - us-gaap_BusinessAcquisitionProFormaInformationTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTableTextBlock
  - us-gaap_ScheduleOfCarryingValuesAndEstimatedFairValuesOfDebtInstrumentsTableTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureInventoryTables

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_ScheduleOfInventoryCurrentTableTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNetTables

- us-gaap_MajorPropertyClassAxis
  - us-gaap_MajorPropertyClassDomain
    - tsla_SolarEnergySystemsLeasedAndToBeLeasedMember
- us-gaap_LeasesAbstract
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseByMajorPropertyClassTable

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosurePropertyPlantAndEquipmentTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureNonCancellableOperatingLeasePaymentsReceivableTables

- us-gaap_LeasesAbstract
  - tsla_ScheduleOfFutureMinimumLeaseReceiptsTableTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureAccruedLiabilitiesAndOtherTables

- us-gaap_PayablesAndAccrualsAbstract
  - tsla_ScheduleOfAccruedLiabilitiesAndOtherCurrentLiabilitiesTableTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureOtherLongTermLiabilitiesTables

- us-gaap_OtherLiabilitiesAbstract
  - us-gaap_OtherNoncurrentLiabilitiesTableTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtTableTextBlock
  - tsla_ScheduleOfAggregateAmountOfInterestExpenseRecognizedTableTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureCommitmentsAndContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - tsla_ScheduleOfFutureMinimumCommitmentsForCapitalAndOperatingLeasesTableTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureVIEArrangementsTables

- tsla_VariableInterestEntityAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_VariableInterestEntityLineItems
      - tsla_SummaryOfNumberOfCurrentVariableInterestEntitiesFundsByTypeOfInvestorTableTextBlock
      - us-gaap_ScheduleOfVariableInterestEntitiesTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureRelatedPartyTransactionsTables

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_ScheduleOfRelatedPartyTransactionsTableTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureQuarterlyResultsOfOperationsTables

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_ScheduleOfQuarterlyFinancialInformationTableTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfRevenueFromSegmentsToConsolidatedTextBlock
  - us-gaap_ScheduleOfRevenueFromExternalCustomersAttributedToForeignCountriesByGeographicAreaTextBlock
  - us-gaap_ScheduleOfEntityWideDisclosureOnGeographicAreasLongLivedAssetsInIndividualForeignCountriesByCountryTextBlock

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureOverviewOfCompanyAdditionalInformationDetail

- us-gaap_AccountingPoliciesAbstract
  - tsla_OrganizationConsolidationAndPresentationOfFinancialStatementsTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - tsla_ScheduleOfOrganizationConsolidationAndPresentationOfFinancialStatementsLineItems
      - us-gaap_NumberOfReportableSegments
      - us-gaap_BusinessAcquisitionEffectiveDateOfAcquisition1

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_AccountingPoliciesAbstract
  - tsla_SummaryOfSignificantAccountingPoliciesTable
    - us-gaap_DeferredRevenueArrangementTypeAxis
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_GuaranteeObligationsByNatureAxis
      - us-gaap_GuaranteeObligationsNatureDomain
    - us-gaap_RegulatoryLiabilityAxis
    - us-gaap_ProductOrServiceAxis
      - us-gaap_ProductsAndServicesDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - tsla_SummaryOfSignificantAccountingPoliciesLineItems
      - us-gaap_DeferredRevenue
      - tsla_GuaranteePeriod
      - tsla_ResaleValueGuaranteesCurrentPortion
      - tsla_MaximumRepurchasePriceOfVehiclesUnderResaleValueArrangement
      - tsla_ResaleValueGuarantee
      - us-gaap_AccountsReceivableNetCurrent
      - tsla_DirectLeaseTerm
      - us-gaap_SalesRevenueGoodsNet
      - tsla_ExpectedCapitalInvestment
      - us-gaap_InvestmentTaxCredit
      - tsla_IncentiveBeginningPeriod
      - tsla_IncentiveEndingPeriod
      - us-gaap_AdvertisingRevenueCost
      - tsla_NumberOfCustomersWithKnownDisputesOrCollectionIssues
      - tsla_NumberOfCustomersWithMaterialNonAccrualOrPastDueNotesReceivable
      - tsla_NumberOfCustomers
      - tsla_AccountsReceivableThresholdPercentage
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseGross
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAccumulatedDepreciation
      - us-gaap_DescriptionOfLesseeLeasingArrangementsOperatingLeases
      - us-gaap_OperatingLeasesOfLessorContingentRentalsBasisSpreadOnVariableRate
      - tsla_MinimumLeasePaymentPercentageOfFairValue
      - tsla_NumberOfVehiclesProductiveLifeForTooling
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - tsla_AdjustmentAttributableToCurrentRateTranslationOfNonMonetaryAssets
      - us-gaap_ForeignCurrencyTransactionGainLossRealized
      - us-gaap_StandardProductWarrantyDescription
      - us-gaap_ProductWarrantyAccrualAdditionsFromBusinessAcquisition
      - us-gaap_ProductWarrantyExpense
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_AccruedLiabilitiesCurrent
      - us-gaap_PrepaidExpenseAndOtherAssetsCurrent
      - us-gaap_OtherAssetsNoncurrent
      - us-gaap_NewAccountingPronouncementOrChangeInAccountingPrincipleCumulativeEffectOfChangeOnEquityOrNetAssets1

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfAccountActivityRelatedToResaleValueGuaranteeProgramDetail

- us-gaap_DisclosureOfResaleAgreementsAbstract
  - tsla_ResaleValueGuarantee
  - tsla_IncreaseDecreaseInResaleValueGuarantee
  - tsla_ReclassificationFromLongTermToShortTermCollateralizedBorrowing
  - tsla_IncreaseDecreaseInResaleValueGuaranteeFromDepreciationExpenseOfEarlyCancellation
  - tsla_ResaleValueGuarantee
- us-gaap_LeasesAbstract
  - us-gaap_ScheduleOfOperatingLeasedAssetsTable
- us-gaap_GuaranteeObligationsByNatureAxis
  - us-gaap_GuaranteeObligationsNatureDomain
    - us-gaap_PropertyLeaseGuaranteeMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfAccruedWarrantyActivityDetail

- us-gaap_StandardProductWarrantyDisclosureAbstract
  - us-gaap_StandardProductWarrantyAccrual
  - us-gaap_ProductWarrantyAccrualAdditionsFromBusinessAcquisition
  - us-gaap_StandardProductWarrantyAccrualPayments
  - us-gaap_ProductWarrantyAccrualPreexistingIncreaseDecrease
  - us-gaap_StandardProductWarrantyAccrualWarrantiesIssued
  - us-gaap_StandardProductWarrantyAccrual

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureAcquisitionOfSolarcityAdditionalInformationDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionEffectiveDateOfAcquisition1
      - tsla_BusinessCombinationCommonStockConversionBasis
      - tsla_BusinessCombinationStockConversionRatio
      - us-gaap_BusinessCombinationConsiderationTransferred1
      - tsla_BusinessCombinationStockBasedCompensationExpenseRecognizedOfAssumedUnvestedShareBasedAwards
      - us-gaap_BusinessAcquisitionCostOfAcquiredEntityTransactionCosts
      - us-gaap_BusinessCombinationSeparatelyRecognizedTransactionsNetGainsAndLosses
      - us-gaap_SharePrice
      - us-gaap_Revenues
      - us-gaap_OperatingIncomeLoss

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureAcquisitionOfSolarcityScheduleOfFairValueOfConsiderationTransferredAsOfAcquisitionDateDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationStepAcquisitionEquityInterestInAcquireeFairValue1
      - tsla_BusinessCombinationFairValueOfReplacementStockOptionsAndRestrictedStockUnitsForAcquireVestedAwards
      - us-gaap_BusinessCombinationConsiderationTransferred1 [totalLabel]

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureAcquisitionOfSolarcityScheduleOfFairValueOfConsiderationTransferredAsOfAcquisitionDateParentheticalDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionEquityInterestsIssuedOrIssuableNumberOfSharesIssued
      - us-gaap_BusinessAcquisitionSharePrice

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureAcquisitionOfSolarcityScheduleOfUnauditedProFormaInformationDetail

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessAcquisitionsProFormaRevenue
      - us-gaap_BusinessAcquisitionsProFormaNetIncomeLoss
      - tsla_BusinessAcquisitionProFormaEarningsPerShareBasicAndDiluted
      - tsla_BusinessAcquisitionProFormaWeightedAverageNumberOfShareOutstandingBasicAndDiluted

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_UnrealizedGainLossOnSecurities
      - us-gaap_MaximumLengthOfTimeHedgedInCashFlowHedge1
      - us-gaap_DerivativeNetHedgeIneffectivenessGainLoss
      - us-gaap_DerivativeAmountOfHedgedItem
      - tsla_DerivativeNotionalAmountNet
      - us-gaap_ForeignCurrencyCashFlowHedgeGainLossToBeReclassifiedDuringNext12Months
      - us-gaap_DerivativeAssetsCurrent
      - us-gaap_DerivativeInstrumentsGainReclassifiedFromAccumulatedOCIIntoIncomeEffectivePortion
      - us-gaap_DerivativeInstrumentsLossReclassifiedFromAccumulatedOCIIntoIncomeEffectivePortion
      - invest_DerivativeNotionalAmount
      - us-gaap_DerivativeLiabilityFairValueGrossAsset
      - us-gaap_DerivativeFairValueOfDerivativeLiability
      - us-gaap_DerivativeGainOnDerivative

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureFairValueOfFinancialInstrumentsScheduleOfEstimatedFairValuesAndTheirCarryingValuesDetail

- us-gaap_FinancialInstrumentAxis
  - us-gaap_TransfersAndServicingOfFinancialInstrumentsTypesOfFinancialInstrumentsDomain
    - tsla_MyPowerCustomerNotesReceivableMember
- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
- us-gaap_DebtInstrumentAxis
  - us-gaap_DebtInstrumentNameDomain
    - tsla_ConvertibleSeniorNotesMember
    - tsla_ParticipationInterestMember
    - tsla_SolarAssetBackedNotesMember
    - tsla_SolarLoanBackedNotesMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureInventoryScheduleOfInventoryDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryRawMaterials
  - us-gaap_InventoryWorkInProcess
  - us-gaap_InventoryFinishedGoods
  - us-gaap_OtherInventoriesSpareParts
  - us-gaap_InventoryNet [totalLabel]

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureInventoryAdditionalInformationDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryAdjustments

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNetComponentsOfSolarEnergySystemsLeasedAndToBeLeasedDetail

- us-gaap_LeasesAbstract
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseByMajorPropertyClassTable
- us-gaap_PropertyPlantAndEquipmentByTypeAxis
  - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - tsla_SolarEnergySystemsMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSolarEnergySystemsLeasedAndToBeLeasedNetComponentsOfSolarEnergySystemsLeasedAndToBeLeasedParentheticalDetail

- us-gaap_LeasesAbstract
  - us-gaap_ScheduleOfCapitalLeasedAsssetsTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_CapitalLeasedAssetsLineItems

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosurePropertyPlantAndEquipmentScheduleOfPropertyPlantAndEquipmentNetDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosurePropertyPlantAndEquipmentAdditionalInformationDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_InterestCostsCapitalized
      - us-gaap_PropertyPlantAndEquipmentNet
      - us-gaap_AccruedLiabilitiesCurrent
      - us-gaap_OtherLiabilitiesNoncurrent
      - us-gaap_DepreciationDepletionAndAmortization
      - us-gaap_CapitalLeasesBalanceSheetAssetsByMajorClassNet
      - us-gaap_CapitalLeasesLesseeBalanceSheetAssetsByMajorClassAccumulatedDeprecation
      - us-gaap_ConstructionInProgressGross

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureNonCancellableOperatingLeasePaymentsReceivableScheduleOfFutureMinimumLeasePaymentsNonCancellableOperatingLeasesDetail

- us-gaap_LeasesAbstract
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableCurrent
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInTwoYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInThreeYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInFourYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInFiveYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableThereafter
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivable [totalLabel]

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureAccruedLiabilitiesAndOtherScheduleOfAccruedLiabilitiesAndOtherCurrentLiabilitiesDetail

- us-gaap_PayablesAndAccrualsAbstract
  - tsla_AccruedPurchases
  - us-gaap_EmployeeRelatedLiabilitiesCurrent
  - us-gaap_TaxesPayableCurrent
  - tsla_FinancingObligationCurrent
  - tsla_AccruedWarrantyAndOtherLiabilitiesCurrent
  - us-gaap_AccruedLiabilitiesCurrent [totalLabel]

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureOtherLongTermLiabilitiesScheduleOfOtherLongTermLiabilitiesDetail

- us-gaap_OtherLiabilitiesNoncurrentAbstract
  - tsla_AccruedWarrantyReserveNoncurrent
  - tsla_BuildToSuitLeaseLiabilityNoncurrent
  - us-gaap_DeferredRentCreditNoncurrent
  - tsla_FinancingObligationNoncurrent
  - tsla_LiabilityForReceiptsFromInvestor
  - tsla_OtherLiabilitiesMiscellaneousNoncurrent
  - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureCustomerDepositsAdditionalInformationDetail

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - us-gaap_CustomerAdvancesCurrent

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsSummaryOfDebtDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
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

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsSummaryOfDebtParentheticalDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_LineOfCreditFacilityRemainingBorrowingCapacity

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligations025And125ConvertibleSeniorNotesDueIn2019And2021AndBondHedgeAndWarrantTransactionsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtConversionByUniqueDescriptionAxis
      - us-gaap_DebtConversionNameDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
      - us-gaap_UnamortizedDebtIssuanceExpense
      - tsla_DebtInstrumentMaturityYear
      - us-gaap_DebtInstrumentPaymentTerms
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - us-gaap_DebtInstrumentConvertibleThresholdTradingDays
      - us-gaap_DebtInstrumentConvertibleThresholdConsecutiveTradingDays
      - tsla_DebtInstrumentConvertibleConversionPricePercentage
      - tsla_PercentOfCommonStockConversionTrigger
      - tsla_PercentageOfPrincipalAmountOfConvertibleNotesIsEqualToRepurchasePrice
      - us-gaap_DebtInstrumentConvertibleThresholdPercentageOfStockPriceTrigger
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_LongTermDebt
      - us-gaap_DebtInstrumentConvertibleCarryingAmountOfTheEquityComponent
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - tsla_NoteHedgesNumberOfSharesContractedToBuy
      - tsla_PurchasePricePerCommonStock
      - tsla_NoteHedgesTransactionCosts
      - us-gaap_ClassOfWarrantOrRightNumberOfSecuritiesCalledByWarrantsOrRights
      - us-gaap_ClassOfWarrantOrRightExercisePriceOfWarrantsOrRights1
      - us-gaap_ProceedsFromIssuanceOfWarrants
      - tsla_ConversionPricePerShare

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligations150ConvertibleSeniorNotesDueIn2018AndBondHedgeAndWarrantTransactionsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtConversionByUniqueDescriptionAxis
      - us-gaap_DebtConversionNameDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - tsla_DebtInstrumentMaturityYear
      - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
      - us-gaap_UnamortizedDebtIssuanceExpense
      - us-gaap_DebtInstrumentFrequencyOfPeriodicPayment
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - us-gaap_DebtInstrumentConvertibleThresholdTradingDays
      - us-gaap_DebtInstrumentConvertibleThresholdConsecutiveTradingDays
      - tsla_DebtInstrumentConvertibleConversionPricePercentage
      - us-gaap_DebtInstrumentRedemptionPricePercentage
      - tsla_PercentageOfPrincipalAmountOfConvertibleNotesIsEqualToRepurchasePrice
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_LongTermDebt
      - us-gaap_DebtConversionOriginalDebtAmount1
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - tsla_NoteHedgesNumberOfSharesContractedToBuy
      - tsla_PurchasePricePerCommonStock
      - tsla_NoteHedgesTransactionCosts
      - us-gaap_ClassOfWarrantOrRightNumberOfSecuritiesCalledByWarrantsOrRights
      - us-gaap_ClassOfWarrantOrRightExercisePriceOfWarrantsOrRights1
      - us-gaap_ProceedsFromIssuanceOfWarrants
      - tsla_ConversionPricePerShare
      - us-gaap_DebtInstrumentConvertibleThresholdPercentageOfStockPriceTrigger
      - us-gaap_ConvertibleDebtCurrent
      - us-gaap_DebtInstrumentUnamortizedDiscount
      - us-gaap_RepaymentsOfLongTermDebt
      - us-gaap_ConvertibleLongTermNotesPayable
      - us-gaap_ClassOfWarrantOrRightOutstanding

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsSecuredRevolvingCreditFacilityAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_ShortTermDebtTypeAxis
      - us-gaap_ShortTermDebtTypeDomain
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - us-gaap_LineOfCreditFacilityAxis
      - us-gaap_LineOfCreditFacilityLenderDomain
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_DebtInstrumentLineItems
      - tsla_DebtInstrumentAdditionalBasisSpread
      - us-gaap_LineOfCreditFacilityUnusedCapacityCommitmentFeePercentage
      - us-gaap_LineOfCreditFacilityInterestRateDescription
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligations275ConvertibleSeniorNotesDueIn2018AdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentMaturityDate
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - us-gaap_DebtInstrumentDescription

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligations1625ConvertibleSeniorNotesDueIn2019AdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
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

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsZeroCouponConvertibleSeniorNotesDueIn2020AdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_SubsidiarySaleOfStockAxis
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
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
      - us-gaap_DebtInstrumentConvertibleThresholdConsecutiveTradingDays

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsSolarBondsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_RelatedPartyTransactionsByRelatedPartyAxis
      - us-gaap_RelatedPartyDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentRedemptionDescription
      - us-gaap_ProceedsFromRelatedPartyDebt
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentMaturityDate

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsCanadaCreditFacilityAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_LineOfCreditFacilityAxis
      - us-gaap_LineOfCreditFacilityLenderDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LineOfCredit
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - tsla_LineOfCreditFacilityTermOfLoan

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsWarehouseAgreementFacilityAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_ExtinguishmentOfDebtAxis
      - us-gaap_ExtinguishmentOfDebtTypeDomain
    - us-gaap_LineOfCreditFacilityAxis
      - us-gaap_LineOfCreditFacilityLenderDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_LineOfCreditFacilityDescription
      - us-gaap_LineOfCreditFacilityExpirationDate1
      - us-gaap_LineOfCredit

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsTermLoanAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_TypeOfArrangementAxis
      - us-gaap_ArrangementsAndNonarrangementTransactionsMember
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - us-gaap_LineOfCreditFacilityUnusedCapacityCommitmentFeePercentage

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsMypowerRevolvingCreditFacilityAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_LineOfCreditFacilityInterestRateDescription
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - tsla_DebtInstrumentInterestRateStatedPercentage2
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - us-gaap_LineOfCreditFacilityUnusedCapacityCommitmentFeePercentage

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsRevolvingAggregationCreditFacilityAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - us-gaap_LineOfCreditFacilityInterestRateDescription

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsSolarRenewableEnergyCreditTermLoanAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_LineOfCreditFacilityAxis
      - us-gaap_LineOfCreditFacilityLenderDomain
    - us-gaap_ShortTermDebtTypeAxis
      - us-gaap_ShortTermDebtTypeDomain
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - us-gaap_LineOfCreditFacilityInterestRateDescription
      - us-gaap_RepaymentsOfLongTermDebt

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureConvertibleAndLongTermDebtObligationsScheduleOfAggregateAmountOfInterestExpenseRecognizedDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_InterestExpenseDebtExcludingAmortization
      - us-gaap_AmortizationOfFinancingCosts
      - us-gaap_AmortizationOfDebtDiscountPremium
      - us-gaap_InterestExpenseDebt [totalLabel]

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureCommitmentsAndContingenciesAdditionalInformationDetail

- us-gaap_EnvironmentalRemediationObligationsAbstract
  - tsla_CommitmentsAndContingenciesTable
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_LeaseArrangementTypeAxis
      - us-gaap_LeaseArrangementTypeDomain
    - us-gaap_LongTermPurchaseCommitmentByCategoryOfItemPurchasedAxis
      - us-gaap_LongTermPurchaseCommitmentCategoryOfItemPurchasedDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_EnvironmentalRemediationContingencyAxis
      - us-gaap_EnvironmentalRemediationContingencyDomain
    - us-gaap_LitigationCaseAxis
      - us-gaap_LitigationCaseTypeDomain
    - tsla_CommitmentsAndContingenciesLineItems
      - us-gaap_LeaseExpirationDate1
      - us-gaap_OperatingLeasesRentExpenseNet
      - tsla_TermsOfAgreementsToLeaseEquipmentUnderCapitalLeases
      - us-gaap_ConstructionAndDevelopmentCosts
      - us-gaap_LongTermPurchaseCommitmentAmount
      - tsla_AdditionalSpecifiedScopeCosts
      - us-gaap_LesseeLeasingArrangementsOperatingLeasesTermOfContract
      - tsla_OperatingLeaseOptionToRenewAmountPerYear
      - tsla_LeaseArrangementAmountRequiredToSpendOrIncur
      - us-gaap_ContractualObligation
      - us-gaap_CapitalExpendituresIncurredButNotYetPaid
      - tsla_SiteContingencyCostToBePaidByCompany
      - tsla_SiteContingencyCostToBePaidInExcessByCompany
      - tsla_LowerThresholdThirdPartyLiability
      - tsla_UpperThresholdThirdPartyLiability
      - tsla_AgreementTermForGovernmentallyRequiredRemediationActivitiesForContamination
      - us-gaap_LossContingencyNumberOfPlaintiffs
      - us-gaap_LossContingencyDamagesSoughtValue
      - us-gaap_LettersOfCreditOutstandingAmount

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureCommitmentsAndContingenciesScheduleOfFutureMinimumCommitmentsForLeasesDetail

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

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureVIEArrangementsSummaryOfNumberOfCurrentVIEFundsByClassificationOfInvestorCarryingValueTotalInvestorContributionsReceivedAndUndrawnInvestorContributionsDetail

- tsla_VariableInterestEntityAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_VariableInterestEntitiesByClassificationOfEntityAxis
      - us-gaap_ClassificationOfVariableInterestEntityDomain
    - us-gaap_VariableInterestEntityLineItems
      - tsla_NumberOfFunds
      - us-gaap_VariableInterestEntityFinancialOrOtherSupportAmount
      - tsla_UndrawnInvestorContributions
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseNet

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureVIEArrangementsAdditionalInformationDetail

- tsla_VariableInterestEntityAbstract
  - us-gaap_ScheduleOfVariableInterestEntitiesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_VariableInterestEntityLineItems
      - us-gaap_PledgedAssetsSeparatelyReportedSecuritiesPledgedAsCollateralAtFairValue
      - tsla_DistributionPayableToNonControllingInterestHolders

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationAdditionalInformationDetail

- us-gaap_PropertyPlantAndEquipmentByTypeAxis
  - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - tsla_SolarEnergySystemsUnderLeasePassThroughArrangementsMember
- us-gaap_RangeAxis
  - us-gaap_RangeMember
    - us-gaap_MinimumMember
    - us-gaap_MaximumMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureLeasePassThroughFinancingObligationScheduleOfFutureMinimumLeasePaymentsToBeReceivedForOperatingLeasesDetail

- us-gaap_BusinessAcquisitionAxis
  - us-gaap_BusinessAcquisitionAcquireeDomain
    - tsla_SolarCityMember

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureDefinedContributionPlanAdditionalInformationDetail

- us-gaap_CompensationAndRetirementDisclosureAbstract
  - us-gaap_DefinedContributionPlanMaximumAnnualContributionsPerEmployeePercent
  - us-gaap_DefinedContributionPlanEmployerDiscretionaryContributionAmount

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureRelatedPartyTransactionsSummaryOfRelatedPartyTransactionsDetail

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_DueToRelatedPartiesCurrentAndNoncurrent
  - tsla_ConvertibleSeniorNotesIssueToRelatedParties
  - us-gaap_DueToOtherRelatedPartiesClassifiedCurrent

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureRelatedPartyTransactionsAdditionalInformationDetail

- us-gaap_RelatedPartyTransactionsAbstract
  - us-gaap_ScheduleOfRelatedPartyTransactionsByRelatedPartyTable
    - us-gaap_RelatedPartyTransactionsByRelatedPartyAxis
      - us-gaap_RelatedPartyDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_RelatedPartyTransactionLineItems
      - us-gaap_DueToRelatedPartiesCurrent
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentMaturityDate

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureQuarterlyResultsOfOperationsScheduleOfSelectedQuarterlyResultsOfOperationsDetail

- us-gaap_QuarterlyFinancialDataAbstract
  - us-gaap_Revenues
  - us-gaap_GrossProfit
  - us-gaap_NetIncomeLoss
  - us-gaap_IncomeLossFromContinuingOperationsPerBasicShare
  - us-gaap_IncomeLossFromContinuingOperationsPerDilutedShare

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSegmentReportingAndInformationAboutGeographicAreasAdditionalInformationDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_NumberOfReportableSegments

### http://www.teslamotors.com/20161231/taxonomy/role/DisclosureSubsequentEventsAdditionalInformationDetail

- us-gaap_SubsequentEventsAbstract
  - us-gaap_SubsequentEventTable
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_SubsequentEventLineItems
      - us-gaap_BusinessAcquisitionEffectiveDateOfAcquisition1
      - us-gaap_PaymentsToAcquireBusinessesGross
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentMaturityDate

