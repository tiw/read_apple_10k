# GOOGL 2016 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.google.com/role/BalanceSheetComponentsComponentsOfAccumulatedOtherComprehensiveIncomeDetails

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossTable
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_AccumulatedOtherComprehensiveIncomeLossLineItems
      - us-gaap_AOCIAttributableToParentNetOfTaxRollForward

### http://www.google.com/role/BalanceSheetComponentsNotesReceivableDetails

- us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsAxis
  - us-gaap_DisposalGroupsIncludingDiscontinuedOperationsNameDomain

### http://www.google.com/role/BalanceSheetComponentsReclassificationsOutOfAccumulatedOtherComprehensiveIncomeLossDetails

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeTable
    - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeAxis
      - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeDomain
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ReclassificationAdjustmentOutOfAccumulatedOtherComprehensiveIncomeLineItems
      - us-gaap_NonoperatingIncomeExpense
      - us-gaap_IncomeLossFromDiscontinuedOperationsNetOfTax
      - us-gaap_Revenues
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_ProfitLoss [totalLabel]

### http://www.google.com/role/CommitmentsAndContingenciesFutureMinimumPaymentsUnderNonCancelableOperatingLeasesAlongWithSubleaseIncomeAmountsDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDueCurrent
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInTwoYears
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInThreeYears
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFourYears
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFiveYears
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDueThereafter
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDue [totalLabel]
  - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableAbstract
    - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableCurrent
    - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInTwoYears
    - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInThreeYears
    - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInFourYears
    - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableInFiveYears
    - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivableThereafter
    - us-gaap_OperatingLeasesFutureMinimumPaymentsReceivable [totalLabel]
  - goog_OperatingLeasesFutureMinimumPaymentsDueNetFiscalYearMaturityAbstract
    - goog_OperatingLeasesFutureMinimumPaymentsDueNetNextTwelveMonths [totalLabel]
    - goog_OperatingLeasesFutureMinimumPaymentsDueNetinTwoYears [totalLabel]
    - goog_OperatingLeasesFutureMinimumPaymentsDueNetinThreeYears [totalLabel]
    - goog_OperatingLeasesFutureMinimumPaymentsDueNetinFourYears [totalLabel]
    - goog_OperatingLeasesFutureMinimumPaymentsDueNetinFiveYears [totalLabel]
    - goog_OperatingLeasesFutureMinimumPaymentsDueNetThereafter [totalLabel]
    - goog_OperatingLeasesFutureMinimumPaymentsDueNetTotal [totalLabel]

### http://www.google.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsAxis
  - us-gaap_DisposalGroupsIncludingDiscontinuedOperationsNameDomain
- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - goog_DepreciationandImpairmentonDispositionofPropertyandEquipment
  - goog_AmortizationandImpairmentofIntangibleandOtherAssets
  - us-gaap_ShareBasedCompensation
  - us-gaap_ExcessTaxBenefitFromShareBasedCompensationOperatingActivities
  - us-gaap_DeferredIncomeTaxesAndTaxCredits
  - goog_GainLossonSaleofBusinessIncludingDiscontinuedOperations
  - goog_GainLossonMarketableandNonmarketableInvestmentsNet
  - us-gaap_OtherNoncashIncomeExpense
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.google.com/role/ConsolidatedStatementsOfComprehensiveIncome

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_NetIncomeLoss
      - us-gaap_OtherComprehensiveIncomeLossNetOfTaxPeriodIncreaseDecreaseAbstract
      - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.google.com/role/ConsolidatedStatementsOfComprehensiveIncomeParenthetical

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_OtherComprehensiveIncomeLossAvailableForSaleSecuritiesTax
      - us-gaap_OtherComprehensiveIncomeLossDerivativesQualifyingAsHedgesTax

### http://www.google.com/role/ConsolidatedStatementsOfIncome

- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_StatementLineItems
      - us-gaap_Revenues
      - us-gaap_CostsAndExpensesAbstract
      - us-gaap_OperatingIncomeLoss [totalLabel]
      - us-gaap_NonoperatingIncomeExpense
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments [totalLabel]
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_IncomeLossFromContinuingOperations [totalLabel]
      - us-gaap_IncomeLossFromDiscontinuedOperationsNetOfTax
      - us-gaap_NetIncomeLoss [totalLabel]
      - us-gaap_PreferredStockDividendsAndOtherAdjustments
      - us-gaap_NetIncomeLossAvailableToCommonStockholdersBasic [totalLabel]
      - us-gaap_EarningsPerShareBasicAbstract
      - us-gaap_EarningsPerShareDilutedAbstract

### http://www.google.com/role/DiscontinuedOperationsMajorClassesOfAssetsAndLiabilitiesDivestedDetails

- us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsTable
  - us-gaap_DisposalGroupClassificationAxis
  - us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsAxis
    - us-gaap_DisposalGroupsIncludingDiscontinuedOperationsNameDomain
  - us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsLineItems
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationBalanceSheetDisclosuresAbstract

### http://www.google.com/role/DiscontinuedOperationsNarrativeDetails

- us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsTable
  - us-gaap_DisposalGroupClassificationAxis
  - us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsAxis
    - us-gaap_DisposalGroupsIncludingDiscontinuedOperationsNameDomain
  - us-gaap_LossContingenciesByNatureOfContingencyAxis
  - us-gaap_ScheduleOfEquityMethodInvestmentEquityMethodInvesteeNameAxis
  - us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsLineItems
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationConsideration
    - goog_DivestitureofBusinessConsiderationReceivedatTransactionCloseDate
    - goog_CashReceivedperaPurchaseandSaleAgreement
    - goog_SharesReceivedinConnectionwithDivestitureValue
    - goog_SharesReceivedInConnectionWithDivestiture
    - goog_PromissoryNoteReceivedinConnectionwithDivestiture
    - goog_PromissoryNoteReceivedinConnectionwithDivestitureTerm
    - us-gaap_LiabilitiesOfDisposalGroupIncludingDiscontinuedOperation
    - us-gaap_DiscontinuedOperationGainLossOnDisposalOfDiscontinuedOperationNetOfTax
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationOtherIncome
    - us-gaap_ProceedsFromDivestitureOfBusinesses
    - goog_ProceedsFromPreviousDivestiture
    - goog_InvestmentOwnershipPercentage

### http://www.google.com/role/DiscontinuedOperationsRevenuesAndEarningsAttributableToDivestitureDetails

- us-gaap_DiscontinuedOperationsAndDisposalGroupsAbstract
  - us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsTable
    - us-gaap_DisposalGroupClassificationAxis
      - us-gaap_DisposalGroupClassificationDomain
    - us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsAxis
      - us-gaap_DisposalGroupsIncludingDiscontinuedOperationsNameDomain
    - us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsLineItems
      - us-gaap_DisposalGroupNotDiscontinuedOperationIncomeStatementDisclosuresAbstract

### http://www.google.com/role/FinancialInstrumentsEffectOfDerivativeInstrumentsOnIncomeAndAccumulatedOtherComprehensiveIncomeDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_IncomeStatementLocationAxis
      - us-gaap_IncomeStatementLocationDomain
    - us-gaap_DerivativeInstrumentsGainLossLineItems
      - us-gaap_DerivativeInstrumentsGainLossRecognizedInOtherComprehensiveIncomeEffectivePortionNet
      - us-gaap_DerivativeInstrumentsGainLossReclassifiedFromAccumulatedOCIIntoIncomeEffectivePortionNet
      - us-gaap_DerivativeInstrumentsGainLossRecognizedInIncomeIneffectivePortionAndAmountExcludedFromEffectivenessTestingNet
      - us-gaap_ChangeInUnrealizedGainLossOnForeignCurrencyFairValueHedgingInstruments1
      - us-gaap_ChangeInUnrealizedGainLossOnHedgedItemInForeignCurrencyFairValueHedge1
      - us-gaap_GainLossOnFairValueHedgesRecognizedInEarnings
      - us-gaap_IncreaseDecreaseInFairValueOfInterestRateFairValueHedgingInstruments1
      - us-gaap_IncreaseDecreaseInFairValueOfHedgedItemInInterestRateFairValueHedge1
      - us-gaap_GainLossOnInterestRateFairValueHedgeIneffectiveness
      - us-gaap_GainLossFromComponentsExcludedFromAssessmentOfFairValueHedgeEffectivenessNet
      - us-gaap_DerivativeInstrumentsNotDesignatedAsHedgingInstrumentsGainLossNet

### http://www.google.com/role/GoodwillAndOtherIntangibleAssetsExpectedAmortizationExpenseForAcquisitionRelatedIntangibleAssetsDetails

- us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.google.com/role/IncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.google.com/role/IncomeTaxesNarrativeDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - goog_IncomeTaxesTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - goog_IncomeTaxesLineItems
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
      - goog_EffectiveIncomeTaxRateReconciliationTaxCreditResearchRetroactiveExtensionOfPriorPeriodTaxLaw
      - us-gaap_UndistributedEarningsOfForeignSubsidiaries
      - goog_DeferredTaxAssetsDeferredCostSharing
      - us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings
      - us-gaap_OperatingLossCarryforwards
      - us-gaap_TaxCreditCarryforwardAmount
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - goog_NumberOfTaxJurisdictions
      - goog_IncomeTaxExaminationIssuesPlannedtobeLitigatedinCourt

### http://www.google.com/role/IncomeTaxesProvisionForIncomeTaxesDetails

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
      - us-gaap_DeferredIncomeTaxExpenseBenefit [totalLabel]
  - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.google.com/role/IncomeTaxesReconciliationOfFederalStatutoryIncomeTaxRateToEffectiveIncomeTaxRateDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
  - us-gaap_IncomeTaxExpenseBenefitContinuingOperationsIncomeTaxReconciliationAbstract
    - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
    - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
    - us-gaap_IncomeTaxReconciliationChangeInDeferredTaxAssetsValuationAllowance
    - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
    - us-gaap_IncomeTaxReconciliationTaxCreditsResearch
    - goog_IncomeTaxReconciliationBasisDifferenceInInvestmentInArris
    - us-gaap_IncomeTaxReconciliationOtherAdjustments
    - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.google.com/role/IncomeTaxesSignificantComponentsOfDeferredTaxAssetsAndLiabilitiesDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
    - us-gaap_DeferredTaxAssetsNetAbstract
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
      - us-gaap_DeferredTaxAssetsStateTaxes
      - us-gaap_DeferredTaxAssetsCapitalLossCarryforwards
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccrualsLegalSettlements
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsEmployeeBenefits
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccrualsOther
      - goog_DeferredTaxAssetsAcquiredNetOperatingLosses
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwardsOther
      - goog_DeferredTaxAssetsBasisDifferenceInInvestmentInHomeBusiness
      - goog_DeferredTaxAssetsDeferredCostSharing
      - us-gaap_DeferredTaxAssetsOther
      - us-gaap_DeferredTaxAssetsGross [totalLabel]
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_DeferredTaxAssetsNet [totalLabel]
    - us-gaap_DeferredTaxLiabilitiesAbstract
      - us-gaap_DeferredTaxLiabilitiesPropertyPlantAndEquipment
      - us-gaap_DeferredTaxLiabilitiesGoodwillAndIntangibleAssetsIntangibleAssets
      - us-gaap_DeferredTaxLiabilitiesOtherComprehensiveIncome
      - goog_DeferredTaxLiabilitiesRenewableEnergyInvestments
      - us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings
      - us-gaap_DeferredTaxLiabilitiesOther
      - us-gaap_DeferredIncomeTaxLiabilities
      - us-gaap_DeferredTaxLiabilities
      - us-gaap_DeferredTaxAssetsLiabilitiesNet [totalLabel]

### http://www.google.com/role/IncomeTaxesSummaryOfActivityRelatedToGrossUnrecognizedTaxBenefitsDetails

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ReconciliationOfUnrecognizedTaxBenefitsExcludingAmountsPertainingToExaminedTaxReturnsRollForward
    - us-gaap_UnrecognizedTaxBenefits
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
    - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
    - us-gaap_UnrecognizedTaxBenefits

### http://www.google.com/role/IncomeTaxesTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_SummaryOfIncomeTaxContingenciesTextBlock

### http://www.google.com/role/InformationAboutSegmentsAndGeographicAreasLongLivedAssetsByGeographicAreaDetails

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - us-gaap_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_AssetsNoncurrent

### http://www.google.com/role/InformationAboutSegmentsAndGeographicAreasOperatingIncomeLossBySegmentDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_OperatingIncomeLoss

### http://www.google.com/role/InformationAboutSegmentsAndGeographicAreasRevenueBySegmentDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_Revenues

### http://www.google.com/role/InformationAboutSegmentsAndGeographicAreasRevenuesByGeographicAreaDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
    - us-gaap_StatementGeographicalAxis
      - us-gaap_SegmentGeographicalDomain
    - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
      - us-gaap_Revenues

### http://www.google.com/role/NatureOfOperationsAndSummaryOfSignificantAccountingPoliciesRevenueByRevenueSourceDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_ProductOrServiceAxis
      - us-gaap_ProductsAndServicesDomain
    - us-gaap_EntityWideInformationRevenueFromExternalCustomerLineItems
      - us-gaap_AdvertisingRevenue
      - us-gaap_OtherSalesRevenueNet
      - us-gaap_Revenues

### http://www.google.com/role/NetIncomePerShare

- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareTextBlock

### http://www.google.com/role/NetIncomePerShareNarrativeDetails

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfEarningsPerShareBasicByCommonClassTable
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_EarningsPerShareBasicLineItems
      - goog_ClassCAdjustmentPayment
      - us-gaap_StockIssuedDuringPeriodSharesNewIssues
      - us-gaap_StockIssuedDuringPeriodValueNewIssues
      - us-gaap_PaymentsOfDividends
      - us-gaap_CommonStockParOrStatedValuePerShare

### http://www.google.com/role/NetIncomePerShareScheduleOfEarningsPerShareDetails

- us-gaap_EarningsPerShareAbstract
  - goog_EarningsPerShareDisclosureTable
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_StatementOperatingActivitiesSegmentAxis
      - us-gaap_SegmentOperatingActivitiesDomain
    - goog_EarningsPerShareDisclosureLineItems
      - us-gaap_EarningsPerShareBasicAbstract
      - us-gaap_EarningsPerShareDilutedAbstract

### http://www.google.com/role/NetIncomePerShareTables

- us-gaap_EarningsPerShareAbstract
  - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock

### http://www.google.com/role/OtherIncomeExpenseNet

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_InterestAndOtherIncomeTextBlock

### http://www.google.com/role/OtherIncomeExpenseNetComponentsOfInterestAndOtherIncomeNetDetails

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_InterestIncomeOther
  - us-gaap_InterestExpense
  - us-gaap_AvailableForSaleSecuritiesGrossRealizedGainLossNet
  - us-gaap_ForeignCurrencyTransactionGainLossBeforeTax
  - goog_RealizedGainLossOnNonmarketableInvestments
  - us-gaap_GainLossOnSaleOfBusiness
  - us-gaap_OtherNonoperatingIncomeExpense
  - us-gaap_NonoperatingIncomeExpense [totalLabel]
  - goog_ForeignCurrencyTransactionGainLossNetofRecognizedForeignExchangeContracts

### http://www.google.com/role/OtherIncomeExpenseNetTables

- us-gaap_OtherIncomeAndExpensesAbstract
  - us-gaap_ScheduleOfOtherNonoperatingIncomeExpenseTableTextBlock

### http://www.google.com/role/RevisionOfPreviouslyIssuedFinancialStatementsComprehensiveIncomeLossDetails

- us-gaap_AccountingChangesAndErrorCorrectionsAbstract
  - us-gaap_ScheduleOfErrorCorrectionsAndPriorPeriodAdjustmentRestatementTable
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_ErrorCorrectionsAndPriorPeriodAdjustmentsRestatementLineItems
      - us-gaap_NetIncomeLoss
      - us-gaap_ComprehensiveIncomeNetOfTax

### http://www.google.com/role/RevisionOfPreviouslyIssuedFinancialStatementsIncomeStatementDetails

- us-gaap_AccountingChangesAndErrorCorrectionsAbstract
  - us-gaap_ScheduleOfErrorCorrectionsAndPriorPeriodAdjustmentRestatementTable
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_ErrorCorrectionsAndPriorPeriodAdjustmentsRestatementLineItems
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_IncomeLossFromContinuingOperations
      - us-gaap_NetIncomeLoss
      - us-gaap_IncomeLossFromContinuingOperationsPerBasicShare
      - us-gaap_EarningsPerShareBasic
      - us-gaap_IncomeLossFromContinuingOperationsPerDilutedShare
      - us-gaap_EarningsPerShareDiluted

### http://www.google.com/role/StockholdersEquityStockBasedCompensationExpenseDetails

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember
    - us-gaap_SellingAndMarketingExpenseMember
    - us-gaap_GeneralAndAdministrativeExpenseMember
    - us-gaap_SegmentDiscontinuedOperationsMember

## 资产负债表结构 (Balance Sheet Structure)

### http://www.google.com/role/AcquisitionsNarrativeDetails

- us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
  - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - goog_PatentsAndDevelopedTechnologyMember
    - us-gaap_CustomerRelationshipsMember
    - goog_TradenamesAndOtherMember

### http://www.google.com/role/BalanceSheetComponents

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_SupplementalBalanceSheetDisclosuresTextBlock

### http://www.google.com/role/BalanceSheetComponentsNotesReceivableDetails

- us-gaap_DisposalGroupsIncludingDiscontinuedOperationsNameDomain
  - goog_MotorolaMobilityHoldingsIncMember
- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_ScheduleOfAccountsNotesLoansAndFinancingReceivableTable
    - us-gaap_DisposalGroupClassificationAxis
      - us-gaap_DisposalGroupClassificationDomain
    - us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsAxis
    - us-gaap_AccountsNotesAndLoansReceivableLineItems
      - goog_PromissoryNoteReceivedinConnectionwithDivestitureTerm
      - us-gaap_ReceivableWithImputedInterestEffectiveYieldInterestRate
      - goog_PromissoryNoteReceivedinConnectionwithDivestiture
      - goog_PromissoryNoteReceivedinConnectionwithDivestitureUnamortizedDiscountonNoteReceivable
      - goog_PromissoryNoteReceivedinConnectionwithDivestitureNet [totalLabel]
      - goog_AllowanceforPromissoryNotedReceivedinConnectionwithDivestiture

### http://www.google.com/role/BalanceSheetComponentsPropertyAndEquipmentDetails

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentNetAbstract

### http://www.google.com/role/BalanceSheetComponentsTables

- goog_BalanceSheetComponentsDisclosureAbstract
  - us-gaap_PropertyPlantAndEquipmentTextBlock
  - us-gaap_ScheduleOfAccountsNotesLoansAndFinancingReceivableTextBlock
  - us-gaap_ScheduleOfAccumulatedOtherComprehensiveIncomeLossTableTextBlock
  - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeTableTextBlock

### http://www.google.com/role/ConsolidatedBalanceSheets

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAndStockholdersEquityAbstract

### http://www.google.com/role/ConsolidatedBalanceSheetsParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_StatementLineItems
      - goog_SecuritiesOwnedAndLoaned
      - us-gaap_AllowanceForDoubtfulAccountsReceivableCurrent
      - us-gaap_PreferredStockParOrStatedValuePerShare
      - us-gaap_PreferredStockSharesAuthorized
      - us-gaap_PreferredStockSharesIssued
      - us-gaap_PreferredStockSharesOutstanding
      - us-gaap_CommonStockParOrStatedValuePerShare
      - us-gaap_CommonStockSharesAuthorized
      - us-gaap_CommonStockValue
      - us-gaap_CommonStockSharesIssued
      - us-gaap_CommonStockSharesOutstanding

### http://www.google.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
  - goog_NetProceedsPaymentsRelatedToStockBasedAwardActivities
  - us-gaap_ExcessTaxBenefitFromShareBasedCompensationFinancingActivities
  - us-gaap_PaymentsOfDividends
  - goog_PaymentsforParentCompanyTransaction
  - us-gaap_PaymentsForRepurchaseOfCommonStock
  - us-gaap_ProceedsFromDebtNetOfIssuanceCosts
  - us-gaap_RepaymentsOfDebt
  - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
- us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
  - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
  - us-gaap_PaymentsToAcquireMarketableSecurities
  - us-gaap_ProceedsFromSaleAndMaturityOfMarketableSecurities
  - us-gaap_PaymentsToAcquireOtherInvestments
  - us-gaap_IncreaseDecreaseInCollateralHeldUnderSecuritiesLending
  - goog_InvestmentsInReverseRepurchaseAgreements
  - us-gaap_ProceedsFromDivestitureOfBusinesses
  - goog_AcquisitionsNetOfCashAcquiredAndPurchasesOfIntangibleAndOtherAssets
  - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
- us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_StatementTable
- us-gaap_SupplementalCashFlowInformationAbstract
  - us-gaap_IncomeTaxesPaid
  - us-gaap_InterestPaid

### http://www.google.com/role/ConsolidatedStatementsOfStockholdersEquity

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_SharesIssued
  - us-gaap_StockholdersEquity
  - us-gaap_StockIssuedDuringPeriodSharesNewIssues
  - us-gaap_StockIssuedDuringPeriodValueNewIssues
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalTaxEffectFromShareBasedCompensation
  - goog_TaxWithholdingRelatedToVestingOfRestrictedStockUnits
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
  - goog_AdjustmentstoAdditionalPaidinCapitalParentCompanyTransaction
  - goog_AdjustmentstoAdditionalPaidinCapitalSharesIssuedforLitigationSettlement
  - goog_AdjustmentstoAdditionalPaidinCapitalValueofSharesIssuedandDividendPaymentforLitigationSettlement
  - us-gaap_NetIncomeLoss
  - us-gaap_OtherComprehensiveIncomeLossNetOfTax
  - us-gaap_StockholdersEquity
  - us-gaap_SharesIssued
- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockIncludingAdditionalPaidInCapitalMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
    - us-gaap_RetainedEarningsMember

### http://www.google.com/role/DiscontinuedOperationsMajorClassesOfAssetsAndLiabilitiesDivestedDetails

- us-gaap_DisposalGroupsIncludingDiscontinuedOperationsNameDomain
  - goog_MotorolaMobilityHoldingsIncMember
  - goog_MotorolaHomeMember
- us-gaap_DisposalGroupClassificationAxis
  - us-gaap_DisposalGroupClassificationDomain
    - us-gaap_DiscontinuedOperationsDisposedOfBySaleMember
- us-gaap_DisposalGroupIncludingDiscontinuedOperationBalanceSheetDisclosuresAbstract
  - us-gaap_AssetsOfDisposalGroupIncludingDiscontinuedOperationAbstract
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationCashAndCashEquivalents
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationAccountsNotesAndLoansReceivableNet
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationInventoryCurrent
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationDeferredTaxAssetCurrent
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationPrepaidAndOtherAssetsCurrent
    - goog_DisposalGroupIncludingDiscontinuedOperationPrepaidRevenueShareExpensesAndOtherAssetsNoncurrent
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationPropertyPlantAndEquipment
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationIntangibleAssets
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationOtherNoncurrentAssets
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationGoodwill1
    - us-gaap_AssetsOfDisposalGroupIncludingDiscontinuedOperation [totalLabel]
  - us-gaap_LiabilitiesOfDisposalGroupIncludingDiscontinuedOperationAbstract
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationAccountsPayable
    - goog_DisposalGroupIncludingDiscontinuedOperationAccruedCompensationandBenefits
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationAccruedLiabilitiesCurrent
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationDeferredRevenueCurrent
    - us-gaap_DisposalGroupIncludingDiscontinuedOperationOtherNoncurrentLiabilities
    - us-gaap_LiabilitiesOfDisposalGroupIncludingDiscontinuedOperation [totalLabel]
- us-gaap_DiscontinuedOperationsAndDisposalGroupsAbstract
  - us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsTable

### http://www.google.com/role/DiscontinuedOperationsNarrativeDetails

- us-gaap_ScheduleOfEquityMethodInvestmentEquityMethodInvesteeNameAxis
  - us-gaap_EquityMethodInvesteeNameDomain
    - goog_ArrisMember

### http://www.google.com/role/FinancialInstrumentsCashCashEquivalentsAndMarketableSecuritiesMeasuredAtAdjustedCostGrossUnrealizedGainsGrossUnrealizedLossesAndFairValueBySignificantInvestmentCategoryDetails

- goog_CashCashEquivalentsAndMarketableSecuritiesTable
  - us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_InvestmentTypeAxis
  - goog_CashCashEquivalentsAndMarketableSecuritiesLineItems
    - goog_CashCashEquivalentsAndShortTermInvestmentsAmortizedCost [totalLabel]
    - goog_CashCashEquivalentsAndShortTermInvestmentsUnrealizedGains
    - goog_CashCashEquivalentsAndShortTermInvestmentsUnrealizedLosses
    - us-gaap_CashCashEquivalentsAndShortTermInvestments
    - us-gaap_CashAndCashEquivalentsAtCarryingValue
    - us-gaap_AvailableForSaleSecuritiesCurrent

### http://www.google.com/role/FinancialInstrumentsFairValuesOfOutstandingDerivativeInstrumentsDetails

- us-gaap_DerivativeAssetsAbstract
  - us-gaap_DerivativeFairValueOfDerivativeAsset

### http://www.google.com/role/FinancialInstrumentsGrossUnrealizedLossesAndFairValuesForInvestmentsInUnrealizedLossPositionDetails

- us-gaap_FairValueDisclosuresAbstract
  - goog_InvestmentsUnrealizedLossPositionTable
    - us-gaap_MajorTypesOfDebtAndEquitySecuritiesAxis
      - us-gaap_MajorTypesOfDebtAndEquitySecuritiesDomain
    - goog_InvestmentsUnrealizedLossPositionLineItems
      - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionAbstract

### http://www.google.com/role/FinancialInstrumentsOffsettingOfFinancialAssetsAndFinancialLiabilitiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_OffsettingAssetsTable
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_OffsettingAssetsLineItems
      - us-gaap_DerivativeAssetsAbstract
      - us-gaap_OffsettingSecuritiesPurchasedUnderAgreementsToResellAbstract
      - us-gaap_OffsettingDerivativeAssetSecuritiesPurchasedUnderAgreementsToResellSecuritiesBorrowedAbstract
      - us-gaap_OffsettingDerivativeLiabilitiesAbstract
      - us-gaap_OffsettingSecuritiesLoanedAbstract
      - us-gaap_OffsettingDerivativeLiabilitySecuritiesSoldUnderAgreementsToResellSecuritiesLoanedAbstract

### http://www.google.com/role/FinancialInstrumentsSecuritiesLendingProgramDetails

- us-gaap_ScheduleOfAssetsSoldUnderAgreementsToRepurchaseTable
  - us-gaap_InvestmentTypeAxis
  - us-gaap_AssetsSoldUnderAgreementsToRepurchaseMaturityPeriodsAxis
    - us-gaap_AssetsSoldUnderAgreementsToRepurchaseMaturityPeriodDomain
      - us-gaap_MaturityOvernightMember
      - us-gaap_MaturityUpTo30DaysMember
      - us-gaap_Maturity30To90DaysMember
      - us-gaap_MaturityOver90DaysMember
  - us-gaap_AssetsSoldUnderAgreementsToRepurchaseLineItems
    - us-gaap_SecuritiesLoanedIncludingNotSubjectToMasterNettingArrangementAndAssetsOtherThanSecuritiesTransferred [totalLabel]
    - us-gaap_DepositsReceivedForSecuritiesLoanedAtCarryingValue
    - us-gaap_SecuredBorrowingsGrossDifferenceAmount

### http://www.google.com/role/GoodwillAndOtherIntangibleAssets

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_GoodwillAndIntangibleAssetsDisclosureTextBlock

### http://www.google.com/role/GoodwillAndOtherIntangibleAssetsAcquisitionRelatedIntangibleAssetsThatAreBeingAmortizedDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetByMajorClassTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_AcquiredFiniteLivedIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_IntangibleAssetsNetExcludingGoodwill [totalLabel]

### http://www.google.com/role/GoodwillAndOtherIntangibleAssetsChangesInCarryingAmountOfGoodwillDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_GoodwillLineItems
      - us-gaap_GoodwillRollForward

### http://www.google.com/role/GoodwillAndOtherIntangibleAssetsExpectedAmortizationExpenseForAcquisitionRelatedIntangibleAssetsDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract

### http://www.google.com/role/GoodwillAndOtherIntangibleAssetsNarrativeDetails

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - us-gaap_AmortizationOfIntangibleAssets
      - us-gaap_ImpairmentOfIntangibleAssetsFinitelived

### http://www.google.com/role/GoodwillAndOtherIntangibleAssetsTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfGoodwillTextBlock
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetsByMajorClassTextBlock
  - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.google.com/role/InformationAboutSegmentsAndGeographicAreasLongLivedAssetsByGeographicAreaDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- us-gaap_StatementGeographicalAxis
  - us-gaap_SegmentGeographicalDomain
    - country_US
    - us-gaap_NonUsMember

### http://www.google.com/role/NatureOfOperationsAndSummaryOfSignificantAccountingPoliciesNarrativeDetails

- us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
  - us-gaap_FiniteLivedIntangibleAssetsMajorClassNameDomain
    - goog_PatentRoyaltyLicensingAgreementMember

### http://www.google.com/role/NonMarketableInvestmentsNonMarketableDebtSecuritiesDetails

- us-gaap_ScheduleOfEquityMethodInvestmentEquityMethodInvesteeNameAxis
  - us-gaap_EquityMethodInvesteeNameDomain
    - goog_SpaceXMember

### http://www.google.com/role/RevisionOfPreviouslyIssuedFinancialStatementsBalanceSheetDetails

- us-gaap_AccountingChangesAndErrorCorrectionsAbstract
  - us-gaap_ScheduleOfErrorCorrectionsAndPriorPeriodAdjustmentRestatementTable
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_ErrorCorrectionsAndPriorPeriodAdjustmentsRestatementLineItems
      - us-gaap_IncomeTaxesReceivable
      - us-gaap_AssetsCurrent
      - us-gaap_Assets
      - us-gaap_LiabilityForUncertainTaxPositionsNoncurrent
      - us-gaap_RetainedEarningsAccumulatedDeficit
      - us-gaap_StockholdersEquity
      - us-gaap_LiabilitiesAndStockholdersEquity

### http://www.google.com/role/StockholdersEquity

- us-gaap_EquityAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.google.com/role/StockholdersEquityNarrativeDetails

- us-gaap_EquityAbstract
  - goog_StockholdersEquityNoteTable
    - us-gaap_LitigationCaseAxis
    - us-gaap_SubsequentEventTypeAxis
    - dei_LegalEntityAxis
    - us-gaap_StatementOperatingActivitiesSegmentAxis
    - us-gaap_StatementClassOfStockAxis
    - us-gaap_ShareRepurchaseProgramAxis
    - us-gaap_AwardTypeAxis
    - goog_StockholdersEquityNoteLineItems
      - us-gaap_CommonStockParOrStatedValuePerShare
      - us-gaap_CommonStockSharesAuthorized
      - us-gaap_PreferredStockParOrStatedValuePerShare
      - us-gaap_PreferredStockSharesAuthorized
      - us-gaap_CommonStockSharesOutstanding
      - us-gaap_PreferredStockSharesIssued
      - us-gaap_PreferredStockSharesOutstanding
      - goog_NumberOfClassesOfCommonStock
      - goog_CommonStockNumberofVotes
      - goog_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExpirationTerm
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_CommonStockCapitalSharesReservedForFutureIssuance
      - us-gaap_EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsShareBasedLiabilitiesPaid
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsVestedInPeriodFairValue1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
      - us-gaap_StockRepurchaseProgramAuthorizedAmount1
      - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
      - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
      - goog_StockRepurchaseProgramAdditionalSharesAuthorizedtobeRepurchased

### http://www.google.com/role/StockholdersEquityStockBasedCompensationExpenseDetails

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable

### http://www.google.com/role/StockholdersEquityStockOptionActivityDetails

- us-gaap_EquityAbstract
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePriceRollforward
  - goog_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsWeightedAverageRemainingContractualTermAbstract
  - goog_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsAggregateIntrinsicValueAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable

### http://www.google.com/role/StockholdersEquityTables

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock
  - us-gaap_ScheduleOfShareBasedCompensationStockOptionsActivityTableTextBlock
  - us-gaap_ScheduleOfShareBasedCompensationRestrictedStockUnitsAwardActivityTableTextBlock

### http://www.google.com/role/StockholdersEquityUnvestedRestrictedStockUnitsActivityDetails

- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber
  - goog_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExpectedToVestNumber
- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValue
  - goog_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsExpectedToVestWeightedAverageGrantDateFairValue
- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable

## 现金流量表结构 (Cash Flow Structure)

### http://www.google.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
      - us-gaap_SubsidiariesMember
  - us-gaap_BusinessAcquisitionAxis
    - us-gaap_BusinessAcquisitionAcquireeDomain
      - goog_BebopTechnologiesMember
  - us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsAxis
  - us-gaap_StatementLineItems
    - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_EffectOfExchangeRateOnCashAndCashEquivalents
    - us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease [totalLabel]
    - us-gaap_CashAndCashEquivalentsAtCarryingValue
    - us-gaap_CashAndCashEquivalentsAtCarryingValue
    - us-gaap_SupplementalCashFlowInformationAbstract
- us-gaap_DisposalGroupsIncludingDiscontinuedOperationsNameDomain
  - goog_MotorolaMobilityHoldingsIncMember
  - goog_MotorolaHomeMember
- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInIncomeTaxes
  - goog_IncreaseDecreaseInPrepaidRevenueShareExpensesAndOtherAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInAccruedLiabilities
  - goog_IncreaseDecreaseInAccruedRevenueShare
  - us-gaap_IncreaseDecreaseInDeferredRevenue

### http://www.google.com/role/FinancialInstrumentsCashCashEquivalentsAndMarketableSecuritiesMeasuredAtAdjustedCostGrossUnrealizedGainsGrossUnrealizedLossesAndFairValueBySignificantInvestmentCategoryDetails

- us-gaap_FairValueDisclosuresAbstract
  - goog_CashCashEquivalentsAndMarketableSecuritiesTable
- us-gaap_InvestmentTypeAxis
  - us-gaap_InvestmentTypeCategorizationMember
    - us-gaap_CashMember
    - goog_MoneyMarketAndOtherFundsMember
    - goog_FixedincomeBondFundsMember
    - us-gaap_USGovernmentDebtSecuritiesMember
    - us-gaap_EquitySecuritiesMember
    - us-gaap_BankTimeDepositsMember
    - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
    - us-gaap_ForeignGovernmentDebtMember
    - us-gaap_MunicipalNotesMember
    - us-gaap_CorporateDebtSecuritiesMember
    - us-gaap_ResidentialMortgageBackedSecuritiesMember
    - us-gaap_AssetBackedSecuritiesMember
- us-gaap_FairValueByFairValueHierarchyLevelAxis
  - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueInputsLevel1Member
    - us-gaap_FairValueInputsLevel2Member

### http://www.google.com/role/RevisionOfPreviouslyIssuedFinancialStatementsCashFlowDetails

- us-gaap_AccountingChangesAndErrorCorrectionsAbstract
  - us-gaap_ScheduleOfErrorCorrectionsAndPriorPeriodAdjustmentRestatementTable
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_ErrorCorrectionsAndPriorPeriodAdjustmentsRestatementLineItems
      - us-gaap_NetIncomeLoss
      - us-gaap_IncreaseDecreaseInIncomeTaxes

### http://www.google.com/role/StockholdersEquityNarrativeDetails

- us-gaap_StatementOperatingActivitiesSegmentAxis
  - us-gaap_SegmentOperatingActivitiesDomain
    - us-gaap_SegmentContinuingOperationsMember
    - us-gaap_SegmentDiscontinuedOperationsMember

## 股东权益结构 (Equity Structure)

### http://www.google.com/role/AcquisitionsNarrativeDetails

- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - goog_CapitalClassCMember

### http://www.google.com/role/ConsolidatedStatementsOfStockholdersEquity

- us-gaap_StatementTable
  - us-gaap_StatementClassOfStockAxis
    - us-gaap_ClassOfStockDomain
      - goog_CapitalClassCMember
  - dei_LegalEntityAxis
    - dei_EntityDomain
      - us-gaap_SubsidiariesMember
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward

### http://www.google.com/role/DocumentAndEntityInformation

- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - us-gaap_CommonClassAMember
    - us-gaap_CommonClassBMember
    - goog_CapitalClassCMember

### http://www.google.com/role/InformationAboutSegmentsAndGeographicAreasStockBasedCompensationAndDepreciationAmortizationAndImpairmentBySegmentDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - goog_SharebasedCompensationExcludingDiscontinuedOperationsandCashSettledAwards
      - goog_DepreciationAmortizationandImpairmentonDispositionofPropertyandEquipment

### http://www.google.com/role/StockholdersEquityNarrativeDetails

- us-gaap_LitigationCaseAxis
  - us-gaap_LitigationCaseTypeDomain
    - goog_AlteraCorp.v.CommissionerMember
- us-gaap_AwardTypeAxis
  - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_EmployeeStockOptionMember
    - us-gaap_RestrictedStockUnitsRSUMember
- us-gaap_ShareRepurchaseProgramAxis
  - us-gaap_ShareRepurchaseProgramDomain
    - goog_October2015ShareRepurchaseProgramMember
- us-gaap_StatementClassOfStockAxis
  - us-gaap_ClassOfStockDomain
    - us-gaap_CommonClassAMember
    - us-gaap_CommonClassBMember
    - goog_CapitalClassCMember
- dei_LegalEntityAxis
  - dei_EntityDomain
    - us-gaap_SubsidiariesMember
- us-gaap_SubsequentEventTypeAxis
  - us-gaap_SubsequentEventTypeDomain
    - us-gaap_SubsequentEventMember

### http://www.google.com/role/StockholdersEquityStockBasedCompensationExpenseDetails

- us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_IncomeStatementLocationAxis
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
    - us-gaap_AllocatedShareBasedCompensationExpense

### http://www.google.com/role/StockholdersEquityStockOptionActivityDetails

- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePriceRollforward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
  - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsExercisesInPeriodWeightedAverageExercisePrice
  - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsForfeituresInPeriodWeightedAverageExercisePrice
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisableWeightedAverageExercisePrice
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestExercisableWeightedAverageExercisePrice
- goog_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsAggregateIntrinsicValueAbstract
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingIntrinsicValue
  - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsExercisableIntrinsicValue1
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestExercisableAggregateIntrinsicValue
- us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_StatementClassOfStockAxis
    - us-gaap_ClassOfStockDomain
      - us-gaap_CommonClassAMember
      - goog_CapitalClassCMember
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
    - us-gaap_SharePrice
- goog_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsWeightedAverageRemainingContractualTermAbstract
  - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsOutstandingWeightedAverageRemainingContractualTerm2
  - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsExercisableWeightedAverageRemainingContractualTerm1
  - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsVestedAndExpectedToVestExercisableWeightedAverageRemainingContractualTerm1
- us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingRollForward
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriod
  - us-gaap_StockIssuedDuringPeriodSharesStockOptionsExercised
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsForfeituresAndExpirationsInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisableNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestExercisableNumber

### http://www.google.com/role/StockholdersEquityUnvestedRestrictedStockUnitsActivityDetails

- us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_AwardTypeAxis
    - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
      - us-gaap_RestrictedStockUnitsRSUMember
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward

## 其他结构 (Other Structure)

### http://www.google.com/role/A401KPlans

- us-gaap_DefinedContributionPensionAndOtherPostretirementPlansDisclosureAbstract
  - us-gaap_CompensationAndEmployeeBenefitPlansTextBlock

### http://www.google.com/role/A401KPlansNarrativeDetails

- us-gaap_DefinedContributionPensionAndOtherPostretirementPlansDisclosureAbstract
  - goog_DefinedContributionPlanNumberofPlans
  - us-gaap_DefinedContributionPlanCostRecognized

### http://www.google.com/role/Acquisitions

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_BusinessCombinationDisclosureTextBlock

### http://www.google.com/role/AcquisitionsNarrativeDetails

- us-gaap_BusinessCombinationsAbstract
  - us-gaap_ScheduleOfBusinessAcquisitionsByAcquisitionTable
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_StatementClassOfStockAxis
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
    - us-gaap_BusinessAcquisitionLineItems
      - us-gaap_BusinessCombinationConsiderationTransferred1
      - us-gaap_PaymentsToAcquireBusinessesGross
      - us-gaap_BusinessCombinationConsiderationTransferredEquityInterestsIssuedAndIssuable
      - us-gaap_StockIssuedDuringPeriodSharesAcquisitions
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedCashAndEquivalents
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibleAssetsOtherThanGoodwill
      - us-gaap_Goodwill
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedLiabilities
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedAssets
      - us-gaap_BusinessAcquisitionPurchasePriceAllocationGoodwillExpectedTaxDeductibleAmount
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife
      - us-gaap_BusinessCombinationStepAcquisitionEquityInterestInAcquireePercentage
      - us-gaap_BusinessCombinationStepAcquisitionEquityInterestInAcquireeFairValue1
      - us-gaap_BusinessCombinationStepAcquisitionEquityInterestInAcquireeRemeasurementGain

### http://www.google.com/role/CollaborationAgreement

- us-gaap_ResearchAndDevelopmentAbstract
  - us-gaap_ResearchDevelopmentAndComputerSoftwareDisclosureTextBlock

### http://www.google.com/role/CollaborationAgreementNarrativeDetails

- us-gaap_ResearchAndDevelopmentAbstract
  - us-gaap_ScheduleOfResearchAndDevelopmentArrangementContractToPerformForOthersTable
    - us-gaap_OtherCommitmentsAxis
      - us-gaap_OtherCommitmentsDomain
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ResearchAndDevelopmentArrangementContractToPerformForOthersLineItems
      - us-gaap_PaymentsToAcquireInterestInSubsidiariesAndAffiliates
      - us-gaap_OtherCommitment
      - goog_AccumulatedPaymentstoAcquiredInterestinSubsidiariesandAffiliates

### http://www.google.com/role/CommitmentsAndContingencies

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.google.com/role/CommitmentsAndContingenciesNarrativeDetails

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - goog_CommitmentsAndContingenciesDisclosureTable
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - goog_CommitmentsAndContingenciesDisclosureLineItems
      - goog_NonCancelableFutureMinimumLeasePayments
      - goog_LeaseRecordedOnBalanceSheetDuringThePeriod
      - goog_LeaseRelatedLiabilityRecordedOnBalanceSheetDuringThePeriod
      - us-gaap_LeaseAndRentalExpense
      - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceSheetAmount
      - us-gaap_LettersOfCreditOutstandingAmount

### http://www.google.com/role/CommitmentsAndContingenciesTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_ScheduleOfFutureMinimumRentalPaymentsForOperatingLeasesTableTextBlock

### http://www.google.com/role/Debt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.google.com/role/DebtFuturePrincipalPaymentsForBorrowingsDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_LongTermDebtByMaturityAbstract
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree
    - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour
    - goog_LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFour
    - us-gaap_LongTermDebt [totalLabel]

### http://www.google.com/role/DebtLongTermDebtDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LongTermDebtCurrentAbstract
      - us-gaap_LongTermDebtNoncurrentAbstract

### http://www.google.com/role/DebtNarrativeDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_CreditFacilityAxis
      - us-gaap_CreditFacilityDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_LineOfCreditFacilityMaximumBorrowingCapacity
      - us-gaap_CommercialPaper
      - us-gaap_ShortTermDebtWeightedAverageInterestRate
      - us-gaap_LinesOfCreditCurrent
      - us-gaap_DebtInstrumentFaceAmount
      - goog_NumberOfTranches
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - us-gaap_LongTermDebtFairValue
      - goog_DebtInstrumentAuthorizedDebtLimit

### http://www.google.com/role/DebtTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfDebtInstrumentsTextBlock
  - us-gaap_ScheduleOfMaturitiesOfLongTermDebtTableTextBlock

### http://www.google.com/role/DiscontinuedOperations

- us-gaap_DiscontinuedOperationsAndDisposalGroupsAbstract
  - us-gaap_DisposalGroupsIncludingDiscontinuedOperationsDisclosureTextBlock

### http://www.google.com/role/DiscontinuedOperationsNarrativeDetails

- us-gaap_LossContingenciesByNatureOfContingencyAxis
  - us-gaap_LossContingencyNatureDomain
    - us-gaap_IndemnificationGuaranteeMember
- us-gaap_DisposalGroupsIncludingDiscontinuedOperationsNameDomain
  - goog_MotorolaMobilityHoldingsIncMember
  - goog_MotorolaHomeMember
- us-gaap_DisposalGroupClassificationAxis
  - us-gaap_DisposalGroupClassificationDomain
    - us-gaap_DiscontinuedOperationsDisposedOfBySaleMember
- us-gaap_DiscontinuedOperationsAndDisposalGroupsAbstract
  - us-gaap_IncomeStatementBalanceSheetAndAdditionalDisclosuresByDisposalGroupsIncludingDiscontinuedOperationsTable

### http://www.google.com/role/DiscontinuedOperationsTables

- us-gaap_DiscontinuedOperationsAndDisposalGroupsAbstract
  - us-gaap_ScheduleOfDisposalGroupsIncludingDiscontinuedOperationsIncomeStatementBalanceSheetAndAdditionalDisclosuresTextBlock

### http://www.google.com/role/DocumentAndEntityInformation

- goog_DocumentandEntityInformationAbstract
  - dei_EntitiesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementClassOfStockAxis
    - dei_DocumentInformationLineItems
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

### http://www.google.com/role/FinancialInstruments

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FinancialInstrumentsDisclosureTextBlock

### http://www.google.com/role/FinancialInstrumentsContractualMaturityDateOfMarketableDebtSecuritiesDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesSingleMaturityDateAbstract
    - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearFairValue
    - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsFairValue
    - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterFiveThroughTenYearsFairValue
    - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterTenYearsFairValue
    - us-gaap_AvailableForSaleSecuritiesDebtSecurities [totalLabel]

### http://www.google.com/role/FinancialInstrumentsFairValuesOfOutstandingDerivativeInstrumentsDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_FairValuesDerivativesBalanceSheetLocationByDerivativeContractTypeByHedgingDesignationTable
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_InvestmentTypeAxis
      - us-gaap_InvestmentTypeCategorizationMember
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_DerivativesFairValueLineItems
      - us-gaap_DerivativeAssetsAbstract
      - us-gaap_DerivativeLiabilitiesAbstract

### http://www.google.com/role/FinancialInstrumentsNarrativeDetails

- us-gaap_FairValueDisclosuresAbstract
  - goog_FinancialInstrumentsAndFairValueTable
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - goog_FinancialInstrumentsAndFairValueLineItems
      - us-gaap_AvailableForSaleSecuritiesGrossRealizedGains
      - us-gaap_AvailableForSaleSecuritiesGrossRealizedLosses
      - us-gaap_OtherThanTemporaryImpairmentLossesInvestmentsAvailableforsaleSecurities
      - goog_CashCollateralReceivedFromDerivativeFinancialInstruments
      - invest_DerivativeNotionalAmount
      - us-gaap_DerivativeHigherRemainingMaturityRange1
      - us-gaap_DerivativeAmountOfHedgedItem
      - goog_AccumulatedOtherComprehensiveIncomeLossCumulativeChangesInNetGainLossFromCashFlowHedgesEffectPretax
      - us-gaap_ForeignCurrencyCashFlowHedgeGainLossToBeReclassifiedDuringNext12Months

### http://www.google.com/role/FinancialInstrumentsSecuritiesLendingProgramDetails

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_ScheduleOfAssetsSoldUnderAgreementsToRepurchaseTable
- us-gaap_InvestmentTypeAxis
  - us-gaap_InvestmentTypeCategorizationMember
    - us-gaap_USGovernmentDebtSecuritiesMember
    - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
    - us-gaap_CorporateDebtSecuritiesMember

### http://www.google.com/role/FinancialInstrumentsTables

- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_ScheduleOfCashCashEquivalentsAndShortTermInvestmentsTableTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock
  - us-gaap_ScheduleOfUnrealizedLossOnInvestmentsTableTextBlock
  - us-gaap_ScheduleOfRepurchaseAgreements
  - us-gaap_ScheduleOfDerivativeInstrumentsInStatementOfFinancialPositionFairValueTextBlock
  - us-gaap_ScheduleOfDerivativeInstrumentsGainLossInStatementOfFinancialPerformanceTextBlock
  - us-gaap_OffsettingAssetsTableTextBlock
  - us-gaap_OffsettingLiabilitiesTableTextBlock

### http://www.google.com/role/InformationAboutSegmentsAndGeographicAreas

- us-gaap_SegmentReportingAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.google.com/role/InformationAboutSegmentsAndGeographicAreasCapitalExpendituresBySegmentDetails

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment

### http://www.google.com/role/InformationAboutSegmentsAndGeographicAreasTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
  - us-gaap_RevenueFromExternalCustomersByGeographicAreasTableTextBlock
  - us-gaap_LongLivedAssetsByGeographicAreasTableTextBlock

### http://www.google.com/role/NatureOfOperationsAndSummaryOfSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_BusinessDescriptionAndAccountingPoliciesTextBlock

### http://www.google.com/role/NatureOfOperationsAndSummaryOfSignificantAccountingPoliciesNarrativeDetails

- us-gaap_AccountingPoliciesAbstract
  - goog_OrganizationAndSummaryOfSignificantAccountingPoliciesTable
    - us-gaap_NewAccountingPronouncementEarlyAdoptionAxis
      - us-gaap_NewAccountingPrinciplesEarlyAdoptionMember
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - goog_OrganizationAndSummaryOfSignificantAccountingPoliciesLineItems
      - us-gaap_StockholdersEquityNoteStockSplitConversionRatio1
      - us-gaap_ProceedsFromStockOptionsExercised
      - goog_TaxBenefitFromStockBasedAwardActivity
      - goog_PercentageOfTotalRevenuesInUnitedStates [totalLabel]
      - goog_ConcentrationRiskNumberofCustomers
      - us-gaap_ConcentrationRiskPercentage1
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_ImpairmentOfIntangibleAssetsFinitelived
      - us-gaap_GoodwillImpairmentLoss
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - us-gaap_MarketingAndAdvertisingExpense
      - us-gaap_DeferredTaxAssetsLiabilitiesNetCurrent
      - us-gaap_DeferredTaxAssetsLiabilitiesNetNoncurrent
      - us-gaap_DeferredTaxLiabilitiesCurrent
      - us-gaap_DeferredTaxLiabilitiesNoncurrent
      - goog_ErrorCorrectionsandPriorPeriodAdjustmentsCumulativeAdjustmentIncomeTaxExpenseBenefit

### http://www.google.com/role/NatureOfOperationsAndSummaryOfSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - goog_NatureOfOperationsPolicyPolicyTextBlock
  - us-gaap_ConsolidationPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - us-gaap_CostOfSalesPolicyTextBlock
  - us-gaap_ShareBasedCompensationOptionAndIncentivePlansPolicy
  - us-gaap_ConcentrationRiskCreditRisk
  - us-gaap_FairValueOfFinancialInstrumentsPolicy
  - goog_CashAndCashEquivalentsAndMarketableSecuritiesPolicyPolicyTextBlock
  - goog_NonMarketableEquityInvestmentsPolicyPolicyTextBlock
  - us-gaap_ConsolidationVariableInterestEntityPolicy
  - goog_ImpairmentOfMarketableAndNonMarketableSecuritiesPolicyPolicyTextBlock
  - us-gaap_ReceivablesPolicyTextBlock
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_ResearchDevelopmentAndComputerSoftwarePolicyTextBlock
  - us-gaap_BusinessCombinationsPolicy
  - goog_LongLivedAssetsPolicyPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_AdvertisingCostsPolicyTextBlock
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock
  - us-gaap_PriorPeriodReclassificationAdjustmentDescription

### http://www.google.com/role/NatureOfOperationsAndSummaryOfSignificantAccountingPoliciesTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTextBlock

### http://www.google.com/role/NonMarketableInvestments

- us-gaap_InvestmentsAllOtherInvestmentsAbstract
  - us-gaap_InvestmentsAndOtherNoncurrentAssetsTextBlock

### http://www.google.com/role/NonMarketableInvestmentsNarrativeDetails

- us-gaap_InvestmentsAllOtherInvestmentsAbstract
  - us-gaap_EquityMethodInvestments
  - us-gaap_CostMethodInvestments
  - us-gaap_CostMethodInvestmentsFairValueDisclosure
  - us-gaap_IncomeLossFromEquityMethodInvestments
  - us-gaap_ScheduleOfVariableInterestEntitiesTable
    - us-gaap_VariableInterestEntitiesByClassificationOfEntityAxis
      - us-gaap_ClassificationOfVariableInterestEntityDomain
    - us-gaap_VariableInterestEntityLineItems
      - us-gaap_VariableInterestEntityNonconsolidatedCarryingAmountAssetsAndLiabilitiesNet
      - us-gaap_VariableInterestEntityEntityMaximumLossExposureAmount

### http://www.google.com/role/NonMarketableInvestmentsNonMarketableDebtSecuritiesDetails

- us-gaap_InvestmentsAllOtherInvestmentsAbstract
  - us-gaap_SecurityOwnedNotReadilyMarketableTable
    - us-gaap_ScheduleOfEquityMethodInvestmentEquityMethodInvesteeNameAxis
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_SecurityOwnedNotReadilyMarketableLineItems
      - goog_OtherInvestmentsNotReadilyMarketableRollForward

### http://www.google.com/role/NonMarketableInvestmentsTables

- us-gaap_InvestmentsAllOtherInvestmentsAbstract
  - us-gaap_ScheduleOfOtherInvestmentsNotReadilyMarketableTextBlock

### http://www.google.com/role/RevisionOfPreviouslyIssuedFinancialStatements

- us-gaap_AccountingChangesAndErrorCorrectionsAbstract
  - us-gaap_AccountingChangesAndErrorCorrectionsTextBlock

### http://www.google.com/role/RevisionOfPreviouslyIssuedFinancialStatementsNarrativeDetails

- us-gaap_AccountingChangesAndErrorCorrectionsAbstract
  - us-gaap_ScheduleOfErrorCorrectionsAndPriorPeriodAdjustmentRestatementTable
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_ErrorCorrectionsAndPriorPeriodAdjustmentsRestatementLineItems
      - goog_ErrorCorrectionsandPriorPeriodAdjustmentsCumulativeAdjustmentIncomeTaxExpenseBenefit

### http://www.google.com/role/RevisionOfPreviouslyIssuedFinancialStatementsTables

- us-gaap_AccountingChangesAndErrorCorrectionsAbstract
  - us-gaap_ScheduleOfErrorCorrectionsAndPriorPeriodAdjustmentsTextBlock

### http://www.google.com/role/ScheduleIiValuationAndQualifyingAccounts

- us-gaap_ValuationAndQualifyingAccountsAbstract
  - us-gaap_ScheduleOfValuationAndQualifyingAccountsDisclosureTextBlock

### http://www.google.com/role/ScheduleIiValuationAndQualifyingAccountsDetails

- us-gaap_ValuationAndQualifyingAccountsAbstract
  - us-gaap_ValuationAndQualifyingAccountsDisclosureTable
    - us-gaap_ValuationAllowancesAndReservesTypeAxis
      - us-gaap_ValuationAllowancesAndReservesDomain
    - us-gaap_ValuationAndQualifyingAccountsDisclosureLineItems
      - us-gaap_MovementInValuationAllowancesAndReservesRollForward

