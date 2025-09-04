# TSLA 2016 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.teslamotors.com/20151231/taxonomy/role/StatementConsolidatedStatementsOfOperations

- us-gaap_IncomeStatementAbstract
  - us-gaap_RevenuesAbstract
    - us-gaap_SalesRevenueGoodsNet
    - tsla_SalesRevenueServicesAndOtherNet
    - us-gaap_Revenues [totalLabel]
  - us-gaap_CostOfRevenueAbstract
    - us-gaap_CostOfGoodsSold
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
  - us-gaap_NetIncomeLoss [totalLabel]
  - us-gaap_EarningsPerShareBasicAndDiluted
  - us-gaap_WeightedAverageNumberOfShareOutstandingBasicAndDiluted

### http://www.teslamotors.com/20151231/taxonomy/role/StatementConsolidatedStatementsOfComprehensiveLoss

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPortionAttributableToParentAbstract
    - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodNetOfTax
    - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTransactionAndTranslationAdjustmentNetOfTax
    - us-gaap_OtherComprehensiveIncomeLossNetOfTax [totalLabel]
  - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.teslamotors.com/20151231/taxonomy/role/StatementConsolidatedStatementsOfCashFlows

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_DepreciationAndAmortization
  - us-gaap_ShareBasedCompensation
  - tsla_AmortizationOfDebtDiscountLessCapitalizedInterest
  - us-gaap_InventoryWriteDown
  - tsla_WriteOffOfLoanOriginationCosts
  - us-gaap_UnrealizedGainLossOnDerivatives
  - us-gaap_GainLossOnDispositionOfAssets1
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureIncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureIncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_SummaryOfPositionsForWhichSignificantChangeInUnrecognizedTaxBenefitsIsReasonablyPossibleTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfActivityRelatedToResaleValueGuaranteeProgramDetail

- us-gaap_DeferredRevenueLeasesNetAbstract
  - us-gaap_DeferredRevenue
  - tsla_IncreaseDecreaseInDeferredRevenueAndReclassificationOfCollateralizedBorrowingFromLongTermToShortTerm
  - tsla_IncreaseDecreaseInDeferredRevenueFromAmortizationOfDeferredRevenue
  - tsla_IncreaseDecreaseInDeferredRevenueFromDepreciationExpenseOfEarlyCancellationOfResaleValueGuarantee
  - tsla_IncreaseDecreaseInReleaseOfDeferredRevenueUnderTradeInProgress
  - us-gaap_DeferredRevenue

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfStockBasedCompensationExpenseDetail

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember
    - tsla_SellingGeneralAndAdministrativeExpenseMember

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureIncomeTaxesAdditionalInformationDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - tsla_IncomeTaxesTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
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

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureIncomeTaxesScheduleOfNetLossBeforeProvisionForIncomeTaxesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureIncomeTaxesComponentsOfProvisionForIncomeTaxesDetail

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

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureIncomeTaxesScheduleOfDeferredTaxAssetsLiabilitiesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
    - us-gaap_DeferredTaxAssetsOperatingLossCarryforwards
    - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsResearch
    - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsOther
    - us-gaap_DeferredTaxAssetsDeferredIncome
    - us-gaap_DeferredTaxAssetsInventory
    - us-gaap_DeferredTaxAssetsPropertyPlantAndEquipment
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
    - tsla_DeferredTaxAssetsConvertibleNotes
    - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccrualsOther
    - us-gaap_DeferredTaxAssetsGross [totalLabel]
    - us-gaap_DeferredTaxAssetsValuationAllowance
    - us-gaap_DeferredTaxAssetsNet [totalLabel]
  - us-gaap_ComponentsOfDeferredTaxLiabilitiesAbstract
    - us-gaap_DeferredTaxLiabilitiesPropertyPlantAndEquipment
    - us-gaap_DeferredTaxLiabilitiesOther
    - us-gaap_DeferredIncomeTaxLiabilities
    - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]
  - us-gaap_DeferredTaxLiabilities

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureIncomeTaxesScheduleOfReconciliationOfStatutoryFederalIncomeTaxesToEffectiveTaxesDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
  - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
  - us-gaap_IncomeTaxReconciliationNondeductibleExpense
  - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
  - us-gaap_IncomeTaxReconciliationTaxCredits
  - us-gaap_IncomeTaxReconciliationOtherReconcilingItems
  - us-gaap_IncomeTaxReconciliationChangeInDeferredTaxAssetsValuationAllowance
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureIncomeTaxesScheduleOfAggregateChangesInBalanceOfGrossUnrecognizedTaxBenefitsDetail

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_UnrecognizedTaxBenefits
  - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
  - us-gaap_UnrecognizedTaxBenefits

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureInformationAboutGeographicAreasScheduleOfRevenuesByGeographicAreaDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
    - us-gaap_StatementGeographicalAxis
      - us-gaap_SegmentGeographicalDomain
    - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
      - us-gaap_Revenues

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureInformationAboutGeographicAreasScheduleOfLongLivedAssetsByGeographicAreaDetail

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - us-gaap_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

## 资产负债表结构 (Balance Sheet Structure)

### http://www.teslamotors.com/20151231/taxonomy/role/StatementConsolidatedBalanceSheets

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_AssetsAbstract
    - us-gaap_AssetsCurrentAbstract
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_RestrictedCashAndInvestmentsCurrent
      - us-gaap_AccountsReceivableNetCurrent
      - us-gaap_InventoryNet
      - us-gaap_PrepaidExpenseAndOtherAssetsCurrent
      - us-gaap_AssetsCurrent [totalLabel]
    - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseNet
    - us-gaap_PropertyPlantAndEquipmentNet
    - us-gaap_RestrictedCashAndCashEquivalentsNoncurrent
    - us-gaap_OtherAssetsNoncurrent
    - us-gaap_Assets [totalLabel]
  - us-gaap_LiabilitiesAndStockholdersEquityAbstract
    - us-gaap_LiabilitiesCurrentAbstract
      - us-gaap_AccountsPayableCurrent
      - us-gaap_AccruedLiabilitiesCurrent
      - us-gaap_DeferredRevenueCurrent
      - tsla_ResaleValueGuaranteesCurrentPortion
      - us-gaap_CustomerAdvancesCurrent
      - us-gaap_LongTermDebtAndCapitalLeaseObligationsCurrent
      - us-gaap_LiabilitiesCurrent [totalLabel]
    - us-gaap_DeferredRevenueNoncurrent
    - us-gaap_LongTermDebtAndCapitalLeaseObligations
    - tsla_ResaleValueGuaranteesNoncurrentPortion
    - us-gaap_OtherLiabilitiesNoncurrent
    - us-gaap_Liabilities [totalLabel]
    - us-gaap_DebtInstrumentConvertibleCarryingAmountOfTheEquityComponent
    - us-gaap_StockholdersEquityAbstract
      - us-gaap_PreferredStockValue
      - us-gaap_CommonStockValue
      - us-gaap_AdditionalPaidInCapitalCommonStock
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
      - us-gaap_RetainedEarningsAccumulatedDeficit
      - us-gaap_StockholdersEquity [totalLabel]
    - us-gaap_LiabilitiesAndStockholdersEquity [totalLabel]

### http://www.teslamotors.com/20151231/taxonomy/role/StatementConsolidatedBalanceSheetsParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_PreferredStockParOrStatedValuePerShare
  - us-gaap_PreferredStockSharesAuthorized
  - us-gaap_PreferredStockSharesIssued
  - us-gaap_PreferredStockSharesOutstanding
  - us-gaap_CommonStockParOrStatedValuePerShare
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_CommonStockSharesIssued
  - us-gaap_CommonStockSharesOutstanding

### http://www.teslamotors.com/20151231/taxonomy/role/StatementConsolidatedStatementsOfStockholdersEquity

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember
    - us-gaap_AdditionalPaidInCapitalMember
    - us-gaap_RetainedEarningsMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable

### http://www.teslamotors.com/20151231/taxonomy/role/StatementConsolidatedStatementsOfStockholdersEquityParenthetical

- us-gaap_StatementOfStockholdersEquityAbstract
  - tsla_CommonStockOfferingPricePerShare
  - tsla_CommonStockPublicOfferingIssuanceCosts
  - tsla_CommonStockPrivatePlacementPricePerShare

### http://www.teslamotors.com/20151231/taxonomy/role/StatementConsolidatedStatementsOfCashFlows

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetIncomeLoss
    - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperations [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
    - tsla_IncreaseDecreaseInRestrictedCashAndCashEquivalents
    - us-gaap_IncreaseDecreaseInRestrictedCash
    - us-gaap_PaymentsToAcquireMarketableSecurities
    - us-gaap_ProceedsFromSaleAndMaturityOfMarketableSecurities
    - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
    - us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperations [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - tsla_ProceedsFromConvertibleAndOtherDebt
    - us-gaap_ProceedsFromIssuanceOfCommonStock
    - us-gaap_ProceedsFromIssuanceOfWarrants
    - us-gaap_ProceedsFromIssuanceOfSharesUnderIncentiveAndShareBasedCompensationPlansIncludingStockOptions
    - us-gaap_ProceedsFromIssuanceOfPrivatePlacement
    - us-gaap_RepaymentsOfLongTermDebt
    - us-gaap_PaymentsForProceedsFromHedgeFinancingActivities
    - us-gaap_PaymentsOfStockIssuanceCosts
    - us-gaap_ProceedsFromRepaymentsOfLongTermDebtAndCapitalSecurities
    - us-gaap_ProceedsFromSecuredNotesPayable
    - us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperations [totalLabel]
  - us-gaap_EffectOfExchangeRateOnCashAndCashEquivalents
  - us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease [totalLabel]
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_SupplementalCashFlowInformationAbstract
    - us-gaap_InterestPaid
    - us-gaap_IncomeTaxesPaid
  - us-gaap_OtherNoncashInvestingAndFinancingItemsAbstract
    - us-gaap_NoncashOrPartNoncashAcquisitionValueOfAssetsAcquired1
    - tsla_NonCashEstimatedFairMarketValueOfManufacturingFacility

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureCommonStock

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_RegulatoryLiabilityAxis
  - us-gaap_RegulatoryLiabilityDomain
    - us-gaap_DeferredLeaseRevenueMember

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfActivityRelatedToResaleValueGuaranteeProgramDetail

- us-gaap_ScheduleOfOperatingLeasedAssetsTable
  - us-gaap_GuaranteeObligationsByNatureAxis
  - us-gaap_OperatingLeasedAssetsLineItems
    - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseNetAbstract
    - us-gaap_DeferredRevenueLeasesNetAbstract
    - us-gaap_DisclosureOfResaleAgreementsAbstract

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfEstimatedUsefulLivesOfRelatedAssetsDetail

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentUsefulLife

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureFinancialInstrumentsScheduleOfFairValueHierarchyOfFinancialAssetsCarriedAtFairValueDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
    - us-gaap_InvestmentTypeAxis
      - us-gaap_InvestmentTypeCategorizationMember
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
      - us-gaap_AssetsFairValueDisclosure

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureConvertibleNotesAndLongTermDebtObligations025And125ConvertibleSeniorNotesAndBondHedgeAndWarrantTransactionsAdditionalInformationDetail

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_WarrantMember

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureConvertibleNotesAndLongTermDebtObligations150ConvertibleSeniorNotesAndBondHedgeAndWarrantTransactionsAdditionalInformationDetail

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_WarrantMember

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureConvertibleNotesAndLongTermDebtObligationsFullRepaymentOfDepartmentOfEnergyLoanFacilityAdditionalInformationDetail

- us-gaap_MajorTypesOfDebtAndEquitySecuritiesAxis
  - us-gaap_MajorTypesOfDebtAndEquitySecuritiesDomain
    - us-gaap_WarrantMember

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureConvertibleNotesAndLongTermDebtObligationsAssetBasedCreditAgreementAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LineOfCreditFacilityAxis
      - us-gaap_LineOfCreditFacilityLenderDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
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
      - us-gaap_ProceedsFromLinesOfCredit

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureConvertibleNotesAndLongTermDebtObligationsPledgedAssetsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_PledgedAssetsSeparatelyReportedOnStatementOfFinancialPositionAtFairValue

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureEquityIncentivePlansAdditionalInformationDetail

- us-gaap_MajorTypesOfDebtAndEquitySecuritiesAxis
  - us-gaap_MajorTypesOfDebtAndEquitySecuritiesDomain
    - tsla_FirstModelXProductionVehicleMember
    - tsla_TwelveMonthMemberMember
    - tsla_FirstGenThreeProductionVehicleMemberMember
    - tsla_ThreeYearPeriodMemberMember

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureInformationAboutGeographicAreasScheduleOfLongLivedAssetsByGeographicAreaDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- us-gaap_StatementGeographicalAxis
  - us-gaap_SegmentGeographicalDomain
    - country_US
    - tsla_InternationalMember

## 现金流量表结构 (Cash Flow Structure)

### http://www.teslamotors.com/20151231/taxonomy/role/StatementConsolidatedStatementsOfCashFlows

- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - tsla_IncreaseDecreaseInInventoriesAndPropertySubjectToOrAvailableForOperatingLease
  - us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets
  - us-gaap_IncreaseDecreaseInOtherOperatingAssets
  - us-gaap_IncreaseDecreaseInAccountsPayableAndAccruedLiabilities
  - us-gaap_IncreaseDecreaseInDeferredRevenue
  - us-gaap_IncreaseDecreaseInDeferredRevenueAndCustomerAdvancesAndDeposits
  - tsla_IncreaseDecreaseInResaleValueGuarantee
  - us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfActivityRelatedToResaleValueGuaranteeProgramDetail

- us-gaap_PropertySubjectToOrAvailableForOperatingLeaseNetAbstract
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseGross
  - tsla_IncreaseDecreaseInInventoriesAndPropertySubjectToOrAvailableForOperatingLease
  - tsla_IncreaseDecreaseInPropertySubjectToOrAvailableForOperatingLeaseGrossFromDepreciationExpenseOfAutomotiveSales
  - tsla_IncreaseDecreaseInPropertySubjectToOrAvailableForOperatingLeaseGrossFromDepreciationExpenseOfEarlyCancellationOfResaleValueGuarantee
  - tsla_IncreaseDecreaseInPropertySubjectToOrAvailableForOperatingLeaseGrossFromReclassificationToInventoryUnderTradeInProgram
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseGross

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureCommitmentsAndContingenciesAdditionalInformationDetail

- us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAxis
  - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseDomain
    - tsla_CaliforniaLeaseMember
    - tsla_NetherlandsLeaseMember

## 股东权益结构 (Equity Structure)

### http://www.teslamotors.com/20151231/taxonomy/role/StatementConsolidatedStatementsOfStockholdersEquity

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_StockholdersEquity
    - us-gaap_SharesIssued
    - us-gaap_StockIssuedDuringPeriodValueNewIssues
    - us-gaap_StockIssuedDuringPeriodSharesNewIssues
    - tsla_StockIssuedDuringPeriodConcurrentPrivatePlacementsValueNewIssues
    - tsla_StockIssuedDuringPeriodConcurrentPrivatePlacementsSharesNewIssues
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalEquityComponentOfConvertibleDebt
    - tsla_AdjustmentsToAdditionalPaidInCapitalConvertibleDebtDiscount
    - tsla_AdjustmentsToAdditionalPaidInCapitalConvertibleDebtHedge
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalWarrantIssued
    - tsla_ReclassificationsOfPermanentEquityToTemporaryEquity
    - tsla_ReclassificationsOfPermanentEquityToTemporaryEquityShares
    - us-gaap_StockIssuedDuringPeriodValueStockOptionsExercised
    - us-gaap_StockIssuedDuringPeriodSharesStockOptionsExercised
    - tsla_StockIssuedDuringPeriodValueRestrictedStock
    - tsla_StockIssuedDuringPeriodShareBasedCompensationNetOfSharesWithheldForTaxes
    - us-gaap_StockIssuedDuringPeriodValueEmployeeStockPurchasePlan
    - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockPurchasePlans
    - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
    - us-gaap_NetIncomeLoss
    - us-gaap_OtherComprehensiveIncomeLossNetOfTax
    - us-gaap_StockholdersEquity
    - us-gaap_SharesIssued

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureEquityIncentivePlans

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ShareholdersEquityAndShareBasedPaymentsTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureEquityIncentivePlansTables

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationActivityTableTextBlock
  - us-gaap_ScheduleOfShareBasedCompensationSharesAuthorizedUnderStockOptionPlansByExercisePriceRangeTextBlock
  - tsla_ScheduleOfShareBasedPaymentAwardStockOptionsAndEmployeeStockPurchasePlanValuationAssumptionsTableTextBlock
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfPotentialWeightedCommonSharesOutstandingThatWereExcludedFromComputationOfBasicAndDilutedNetLossPerShareOfCommonStockDetail

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTable
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareByAntidilutiveSecuritiesAxis
      - us-gaap_AntidilutiveSecuritiesNameDomain
    - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareLineItems
      - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureCommonStockAdditionalInformationDetail

- us-gaap_CompensationRelatedCostsAbstract
  - tsla_OverviewOfCompanyTable
    - us-gaap_TitleOfIndividualAxis
      - us-gaap_TitleOfIndividualWithRelationshipToEntityDomain
    - us-gaap_SubsidiarySaleOfStockAxis
      - us-gaap_SaleOfStockNameOfTransactionDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - tsla_OverviewOfCompanyLineItems
      - us-gaap_CommonStockSharesIssued
      - us-gaap_ProceedsFromIssuanceOfCommonStock
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_ProceedsFromDebtNetOfIssuanceCosts

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureEquityIncentivePlansAdditionalInformationDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_PlanNameAxis
      - us-gaap_PlanNameDomain
    - us-gaap_MajorTypesOfDebtAndEquitySecuritiesAxis
    - us-gaap_FinancialInstrumentPerformanceStatusAxis
      - us-gaap_FinancialInstrumentPerformanceStatusDomain
    - us-gaap_TitleOfIndividualAxis
      - us-gaap_TitleOfIndividualWithRelationshipToEntityDomain
    - us-gaap_VestingAxis
      - us-gaap_VestingDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriods
      - us-gaap_DeferredCompensationArrangementWithIndividualMaximumContractualTerm1
      - tsla_SharesReservedToCoverStockAwardsIssuedAndOutstanding
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingIntrinsicValue
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsExercisableIntrinsicValue1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestOutstandingAggregateIntrinsicValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue [totalLabel]
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsAggregateIntrinsicValueOutstanding
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
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsRiskFreeInterestRate
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsExpectedTermForForeignGrants
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsExpectedVolatilityRate
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsExpectedDividendRate
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfTranchesVested
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
      - tsla_CashCompensationReceivedForServices
      - tsla_PercentageOfPayrollDeductionsOfEmployeesEligibleCompensation
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardDiscountFromMarketPriceOfferingDate
      - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockPurchasePlans
      - us-gaap_StockIssuedDuringPeriodValueEmployeeStockPurchasePlan
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForIssuance

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfStockOptionAndRSUActivityUnderPlanDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardSharesAvailableForGrantAdditionalOptionsReserved
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardSharesAvailableForGrantGranted
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardSharesAvailableForGrantExercised
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardSharesAvailableForGrantCancelled
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesTradedForTaxes
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodGross
      - us-gaap_StockIssuedDuringPeriodSharesStockOptionsExercised
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsForfeituresInPeriod
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsGrantsInPeriodWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsExercisesInPeriodWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsForfeituresInPeriodWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExercised
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsReleased
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExercisedInPeriodWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValue
      - tsla_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsReleasedInPeriodWeightedAverageGrantDateFairValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureEquityIncentivePlansScheduleOfStockOptionsOutstandingAndExercisableDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationSharesAuthorizedUnderStockOptionPlansByExercisePriceRangeTable
    - us-gaap_ShareBasedCompensationSharesAuthorizedUnderStockOptionPlansByExercisePriceRangeAxis
      - us-gaap_ShareBasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeDomain
    - us-gaap_ShareBasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeLineItems
      - us-gaap_ShareBasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeLowerRangeLimit
      - us-gaap_ShareBasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeUpperRangeLimit
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
      - us-gaap_SharebasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeOutstandingOptionsWeightedAverageExercisePriceBeginningBalance1
      - us-gaap_SharebasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeOutstandingOptionsWeightedAverageRemainingContractualTerm2
      - us-gaap_ShareBasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeNumberOfExercisableOptions
      - us-gaap_SharebasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeExercisableOptionsWeightedAverageExercisePrice1
      - us-gaap_SharebasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeExercisableOptionsWeightedAverageRemainingContractualTerm2

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureEquityIncentivePlansScheduleOfFairValueOfOptionAwardAndESPPOnGrantDateDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsRiskFreeInterestRate
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardFairValueAssumptionsExpectedTerm1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsExpectedVolatilityRate
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsExpectedDividendRate

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureEquityIncentivePlansSummaryOfStockBasedCompensationExpenseDetail

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
    - us-gaap_IncomeStatementLocationAxis
    - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
      - us-gaap_AllocatedShareBasedCompensationExpense

## 其他结构 (Other Structure)

### http://www.teslamotors.com/20151231/taxonomy/role/DocumentDocumentAndEntityInformation

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

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureOverviewOfCompany

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NatureOfOperations

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_SignificantAccountingPoliciesTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureFinancialInstruments

- us-gaap_InvestmentsAllOtherInvestmentsAbstract
  - us-gaap_FinancialInstrumentsDisclosureTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureInventory

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryDisclosureTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosurePropertyPlantAndEquipment

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentDisclosureTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureAccruedLiabilities

- us-gaap_PayablesAndAccrualsAbstract
  - us-gaap_AccountsPayableAndAccruedLiabilitiesDisclosureTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureCustomerDeposits

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - tsla_CustomerDepositsTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureConvertibleNotesAndLongTermDebtObligations

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureInformationAboutGeographicAreas

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureCommitmentsAndContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureQuarterlyResultsOfOperations

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_QuarterlyFinancialInformationTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ConsolidationPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_MarketableSecuritiesPolicy
  - us-gaap_CashAndCashEquivalentsRestrictedCashAndCashEquivalentsPolicy
  - us-gaap_ReceivablesPolicyTextBlock
  - us-gaap_ConcentrationRiskCreditRisk
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - tsla_PropertySubjectToOrAvailableForOperatingLeaseTextBlock
  - us-gaap_ImpairmentOrDisposalOfLongLivedAssetsPolicyTextBlock
  - us-gaap_ResearchAndDevelopmentExpensePolicy
  - us-gaap_AdvertisingCostsPolicyTextBlock
  - us-gaap_ShippingAndHandlingCostPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_ShareBasedCompensationOptionAndIncentivePlansPolicy
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_DerivativesPolicyTextBlock
  - us-gaap_ComprehensiveIncomeNoteTextBlock
  - us-gaap_StandardProductWarrantyPolicy
  - us-gaap_EarningsPerSharePolicyTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - tsla_ScheduleOfActivityRelatedToResaleValueGuaranteeProgramTableTextBlock
  - us-gaap_SchedulesOfConcentrationOfRiskByRiskFactorTextBlock
  - tsla_ScheduleOfPropertyPlantAndEquipmentTextBlock
  - us-gaap_ScheduleOfProductWarrantyLiabilityTableTextBlock
  - us-gaap_ScheduleOfAntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureFinancialInstrumentsTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTableTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureInventoryTables

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_ScheduleOfInventoryCurrentTableTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosurePropertyPlantAndEquipmentTables

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureAccruedLiabilitiesTables

- us-gaap_PayablesAndAccrualsAbstract
  - us-gaap_ScheduleOfAccruedLiabilitiesTableTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureConvertibleNotesAndLongTermDebtObligationsTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ConvertibleDebtTableTextBlock
  - tsla_ScheduleOfAggregateAmountOfInterestExpenseRecognizedTableTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureInformationAboutGeographicAreasTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenueFromExternalCustomersAttributedToForeignCountriesByGeographicAreaTextBlock
  - us-gaap_ScheduleOfEntityWideDisclosureOnGeographicAreasLongLivedAssetsInIndividualForeignCountriesByCountryTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureCommitmentsAndContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - tsla_ScheduleOfFutureMinimumCommitmentsForCapitalAndOperatingLeasesTableTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureQuarterlyResultsOfOperationsTables

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_ScheduleOfQuarterlyFinancialInformationTableTextBlock

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformationDetail

- us-gaap_AccountingPoliciesAbstract
  - tsla_SummaryOfSignificantAccountingPoliciesTable
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_GuaranteeObligationsByNatureAxis
      - us-gaap_GuaranteeObligationsNatureDomain
    - us-gaap_RegulatoryLiabilityAxis
    - us-gaap_ProductOrServiceAxis
      - us-gaap_ProductsAndServicesDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - tsla_SummaryOfSignificantAccountingPoliciesLineItems
      - us-gaap_PrepaidExpenseAndOtherAssetsCurrent
      - us-gaap_OtherAssetsNoncurrent
      - us-gaap_DeferredTaxAssetsNetNoncurrent
      - tsla_GuaranteePeriod
      - tsla_ResaleValueGuaranteesCurrentPortion
      - tsla_MaximumRepurchasePriceOfVehiclesUnderResaleValueArrangement
      - us-gaap_DeferredRevenue
      - tsla_ResaleValueGuarantee
      - tsla_DirectLeaseTerm
      - us-gaap_SalesRevenueGoodsNet
      - tsla_ExpectedCapitalInvestment
      - us-gaap_InvestmentTaxCredit
      - tsla_IncentiveBeginningPeriod
      - tsla_IncentiveEndingPeriod
      - tsla_ExtendedWarrantyCoverageVehicleMileage
      - tsla_ExtendedProductWarrantyPeriod
      - tsla_AccountsReceivableThresholdPercentage
      - tsla_NumberOfVehiclesProductiveLifeForTooling
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseGross
      - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAccumulatedDepreciation
      - us-gaap_MarketingAndAdvertisingExpense
      - tsla_AdjustmentAttributableToCurrentRateTranslationOfNonMonetaryAssets
      - us-gaap_ForeignCurrencyTransactionGainLossRealized
      - us-gaap_MaximumLengthOfTimeHedgedInCashFlowHedge1
      - us-gaap_ProductWarrantyExpense
      - us-gaap_DebtInstrumentConvertibleConversionPrice1

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfActivityRelatedToResaleValueGuaranteeProgramDetail

- us-gaap_DisclosureOfResaleAgreementsAbstract
  - tsla_ResaleValueGuarantee
  - tsla_IncreaseDecreaseInResaleValueGuarantee
  - tsla_ReclassificationFromLongTermToShortTermCollateralizedBorrowing
  - tsla_IncreaseDecreaseInResaleValueGuaranteeFromDepreciationExpenseOfEarlyCancellation
  - tsla_IncreaseDecreaseInReleaseOfResaleValueGuaranteeUnderTradeInProgress
  - tsla_ResaleValueGuarantee
- us-gaap_LeasesAbstract
  - us-gaap_ScheduleOfOperatingLeasedAssetsTable
- us-gaap_GuaranteeObligationsByNatureAxis
  - us-gaap_GuaranteeObligationsNatureDomain
    - us-gaap_PropertyLeaseGuaranteeMember

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesSummaryOfAccountsReceivableFromCustomersInExcessOf10OfTotalAccountsReceivableDetail

- us-gaap_RisksAndUncertaintiesAbstract
  - us-gaap_ConcentrationRiskTable
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - us-gaap_ConcentrationRiskByTypeAxis
      - us-gaap_ConcentrationRiskTypeDomain
    - us-gaap_ConcentrationRiskLineItems
      - us-gaap_ConcentrationRiskPercentage1

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesScheduleOfAccruedWarrantyActivityDetail

- us-gaap_StandardProductWarrantyDisclosureAbstract
  - us-gaap_StandardProductWarrantyAccrual
  - us-gaap_StandardProductWarrantyAccrualPayments
  - us-gaap_ProductWarrantyAccrualPreexistingIncreaseDecrease
  - us-gaap_StandardProductWarrantyAccrualWarrantiesIssued
  - us-gaap_StandardProductWarrantyAccrual

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureFinancialInstrumentsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_UnrealizedGainLossOnSecurities
      - us-gaap_LongTermDebtFairValue
      - us-gaap_DebtInstrumentFaceAmount
      - tsla_CarryingValueOfCreditAgreementLiability
      - us-gaap_MaximumLengthOfTimeHedgedInCashFlowHedge1
      - tsla_DerivativeNotionalAmountNet
      - us-gaap_ForeignCurrencyCashFlowHedgeGainLossToBeReclassifiedDuringNext12Months
      - us-gaap_DerivativeAssetsCurrent
      - us-gaap_DerivativeNetHedgeIneffectivenessGainLoss

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureInventoryScheduleOfInventoryDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryRawMaterials
  - us-gaap_InventoryWorkInProcess
  - us-gaap_InventoryFinishedGoods
  - us-gaap_OtherInventoriesSpareParts
  - us-gaap_InventoryNet [totalLabel]

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureInventoryAdditionalInformationDetail

- us-gaap_InventoryDisclosureAbstract
  - us-gaap_InventoryWriteDown

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosurePropertyPlantAndEquipmentScheduleOfPropertyPlantAndEquipmentNetDetail

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosurePropertyPlantAndEquipmentAdditionalInformationDetail

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

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureAccruedLiabilitiesScheduleOfAccruedLiabilitiesDetail

- us-gaap_PayablesAndAccrualsAbstract
  - us-gaap_TaxesPayableCurrent
  - tsla_AccruedPurchases
  - us-gaap_EmployeeRelatedLiabilitiesCurrent
  - tsla_WarrantyAndOtherLiabilitiesCurrent
  - us-gaap_AccruedLiabilitiesCurrent [totalLabel]

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureCustomerDepositsAdditionalInformationDetail

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - us-gaap_CustomerAdvancesCurrent

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureConvertibleNotesAndLongTermDebtObligations025And125ConvertibleSeniorNotesAndBondHedgeAndWarrantTransactionsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
      - us-gaap_DebtIssuanceCosts
      - tsla_DebtInstrumentMaturityYear
      - us-gaap_DebtInstrumentPaymentTerms
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - us-gaap_DebtInstrumentConvertibleThresholdConsecutiveTradingDays
      - us-gaap_DebtInstrumentConvertibleThresholdTradingDays
      - tsla_DebtInstrumentConvertibleConversionPricePercentage
      - tsla_PercentOfCommonStockConversionTrigger
      - tsla_PercentageOfPrincipalAmountOfConvertibleNotesIsEqualToRepurchasePrice
      - us-gaap_DebtInstrumentConvertibleThresholdPercentageOfStockPriceTrigger
      - us-gaap_DebtInstrumentConvertibleCarryingAmountOfTheEquityComponent
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - tsla_NoteHedgesNumberOfSharesContractedToBuy
      - tsla_PurchasePricePerCommonStock
      - tsla_NoteHedgesTransactionCosts
      - us-gaap_ClassOfWarrantOrRightNumberOfSecuritiesCalledByWarrantsOrRights
      - us-gaap_ClassOfWarrantOrRightExercisePriceOfWarrantsOrRights1
      - us-gaap_ProceedsFromIssuanceOfWarrants
      - tsla_ConversionPricePerShare

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureConvertibleNotesAndLongTermDebtObligations150ConvertibleSeniorNotesAndBondHedgeAndWarrantTransactionsAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - tsla_DebtInstrumentMaturityYear
      - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
      - us-gaap_DebtIssuanceCosts
      - us-gaap_DebtInstrumentFrequencyOfPeriodicPayment
      - us-gaap_DebtConversionConvertedInstrumentAmount1
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - us-gaap_DebtInstrumentConvertibleThresholdConsecutiveTradingDays
      - us-gaap_DebtInstrumentConvertibleThresholdTradingDays
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
      - us-gaap_DebtInstrumentConvertibleThresholdPercentageOfStockPriceTrigger
      - us-gaap_ConvertibleDebtCurrent
      - us-gaap_DebtInstrumentUnamortizedDiscount

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureConvertibleNotesAndLongTermDebtObligationsScheduleOfDebtDiscountsDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_ConvertibleNotesPayable [totalLabel]
      - us-gaap_DebtInstrumentUnamortizedDiscount
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentConvertibleRemainingDiscountAmortizationPeriod1
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - us-gaap_DebtInstrumentConvertibleCarryingAmountOfTheEquityComponent
      - us-gaap_DebtInstrumentConvertibleIfConvertedValueInExcessOfPrincipal

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureConvertibleNotesAndLongTermDebtObligationsFullRepaymentOfDepartmentOfEnergyLoanFacilityAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LineOfCreditFacilityAxis
      - us-gaap_LineOfCreditFacilityLenderDomain
    - us-gaap_MajorTypesOfDebtAndEquitySecuritiesAxis
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LineOfCreditFacilityInitiationDate1
      - us-gaap_RepaymentsOfDebt
      - us-gaap_LongTermDebt
      - us-gaap_PaymentsOfDebtExtinguishmentCosts
      - tsla_ReserveForLoanPrincipalRepayment
      - us-gaap_DebtInstrumentFairValue
      - us-gaap_DebtRelatedCommitmentFeesAndDebtIssuanceCosts

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureConvertibleNotesAndLongTermDebtObligationsWarehouseLineOfCreditAdditionalInformationDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_VariableRateAxis
      - us-gaap_VariableRateDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_LineOfCreditFacilityIncreaseDecreaseForPeriodNet
      - tsla_BorrowingsLimitsBasedOnPresentValueOfRemainingLeasePaymentAndResidualVehicleValue
      - us-gaap_DebtInstrumentBasisSpreadOnVariableRate1
      - us-gaap_LineOfCreditFacilityUnusedCapacityCommitmentFeePercentage
      - us-gaap_LineOfCreditFacilityExpirationDate1

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureConvertibleNotesAndLongTermDebtObligationsScheduleOfAggregateAmountOfInterestExpenseRecognizedDetail

- us-gaap_DebtDisclosureAbstract
  - us-gaap_InterestExpenseDebtExcludingAmortization
  - us-gaap_AmortizationOfFinancingCosts
  - us-gaap_AmortizationOfDebtDiscountPremium
  - us-gaap_InterestExpenseDebt [totalLabel]

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureInformationAboutGeographicAreasAdditionalInformationDetail

- us-gaap_SegmentReportingAbstract
  - us-gaap_NumberOfReportableSegments

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureCommitmentsAndContingenciesAdditionalInformationDetail

- us-gaap_EnvironmentalRemediationObligationsAbstract
  - tsla_CommitmentsAndContingenciesTable
    - us-gaap_PropertySubjectToOrAvailableForOperatingLeaseAxis
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_EnvironmentalRemediationContingencyAxis
      - us-gaap_EnvironmentalRemediationContingencyDomain
    - tsla_CommitmentsAndContingenciesLineItems
      - us-gaap_AreaOfRealEstateProperty
      - us-gaap_LeaseExpirationDate1
      - us-gaap_OperatingLeasesRentExpenseNet
      - tsla_TermsOfAgreementsToLeaseEquipmentUnderCapitalLeases
      - tsla_SiteContingencyCostToBePaidByCompany
      - tsla_SiteContingencyCostToBePaidInExcessByCompany
      - tsla_LowerThresholdThirdPartyLiability
      - tsla_UpperThresholdThirdPartyLiability
      - tsla_AgreementTermForGovernmentallyRequiredRemediationActivitiesForContamination
      - us-gaap_AccrualForEnvironmentalLossContingenciesPayments
      - us-gaap_AccruedEnvironmentalLossContingenciesNoncurrent

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureCommitmentsAndContingenciesScheduleOfFutureMinimumCommitmentsForLeasesDetail

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueCurrent
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInTwoYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInThreeYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFourYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueThereafter
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDue [totalLabel]
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueCurrent
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInTwoYears
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInThreeYears
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInFourYears
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueThereafter
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDue [totalLabel]
  - us-gaap_CapitalLeasesFutureMinimumPaymentsInterestIncludedInPayments
  - us-gaap_CapitalLeaseObligations [totalLabel]
  - us-gaap_CapitalLeaseObligationsCurrent
  - us-gaap_CapitalLeaseObligationsNoncurrent

### http://www.teslamotors.com/20151231/taxonomy/role/DisclosureQuarterlyResultsOfOperationsScheduleOfSelectedQuarterlyResultsOfOperationsDetail

- us-gaap_QuarterlyFinancialDataAbstract
  - us-gaap_Revenues
  - us-gaap_GrossProfit
  - us-gaap_NetIncomeLoss
  - us-gaap_IncomeLossFromContinuingOperationsPerBasicShare
  - us-gaap_IncomeLossFromContinuingOperationsPerDilutedShare

