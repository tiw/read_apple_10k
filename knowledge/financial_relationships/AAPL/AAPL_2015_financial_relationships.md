# AAPL 2015 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.apple.com/taxonomy/role/StatementOfIncome

- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_SalesRevenueNet
      - us-gaap_CostOfGoodsAndServicesSold
      - us-gaap_GrossProfit [totalLabel]
      - us-gaap_OperatingExpensesAbstract
      - us-gaap_OperatingIncomeLoss [totalLabel]
      - us-gaap_NonoperatingIncomeExpense
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest [totalLabel]
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_NetIncomeLoss [totalLabel]
      - us-gaap_EarningsPerShareAbstract
      - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
      - us-gaap_CommonStockDividendsPerShareDeclared

### http://www.apple.com/taxonomy/role/StatementOfOtherComprehensiveIncome

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_NetIncomeLoss
      - us-gaap_ComprehensiveIncomeNetOfTaxAbstract
      - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.apple.com/taxonomy/role/StatementOfOtherComprehensiveIncomeParenthetical

- us-gaap_StatementOfIncomeAndComprehensiveIncomeAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_OtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentTax
      - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIOnDerivativesTax
      - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodTax
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesTax

### http://www.apple.com/taxonomy/role/StatementOfShareholdersEquityAndOtherComprehensiveIncome

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_CommonStockSharesOutstanding
      - us-gaap_StockholdersEquity
      - us-gaap_NetIncomeLoss
      - us-gaap_OtherComprehensiveIncomeLossNetOfTax
      - aapl_DividendsAndDividendEquivalentsDeclaredOnCommonStockAndRestrictedStockUnits
      - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
      - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
      - us-gaap_AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue
      - aapl_SharesOfStockIssuedDuringPeriodShareBasedCompensationNetOfSharesWithheldForTaxes
      - aapl_StockIssuedDuringPeriodValueShareBasedCompensationNetOfSharesWithheldForTaxes
      - aapl_AdjustmentsToAdditionalPaidInCapitalTaxEffectFromShareBasedCompensationIncludingTransferPricing
      - us-gaap_CommonStockSharesOutstanding
      - us-gaap_StockholdersEquity

### http://www.apple.com/taxonomy/role/StatementOfCashFlowsIndirect

- us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_DepreciationAmortizationAndAccretionNet
  - us-gaap_ShareBasedCompensation
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract

### http://www.apple.com/taxonomy/role/DisclosureComputationOfBasicAndDilutedEarningsPerShare

- us-gaap_EarningsPerShareAbstract
  - aapl_EarningsPerShareDisclosureTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - aapl_EarningsPerShareDisclosureLineItems
      - us-gaap_NetIncomeLossAbstract
      - us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract
      - us-gaap_EarningsPerShareBasic
      - us-gaap_EarningsPerShareDiluted

### http://www.apple.com/taxonomy/role/DisclosurePreTaxGainsAndLossesOfDerivativeAndNonDerivativeInstrumentsDesignatedAsCashFlowNetInvestmentAndFairValueHedges

- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
  - dei_LegalEntityAxis
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeInstrumentsGainLossLineItems

### http://www.apple.com/taxonomy/role/DisclosureOtherIncomeExpenseNet

- us-gaap_OtherIncomeAndExpensesAbstract
  - aapl_OtherIncomeExpenseTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - aapl_OtherIncomeExpenseLineItems
      - us-gaap_InvestmentIncomeInterestAndDividend
      - us-gaap_InterestExpense
      - us-gaap_OtherNonoperatingIncomeExpense
      - us-gaap_NonoperatingIncomeExpense [totalLabel]

### http://www.apple.com/taxonomy/role/DisclosureExpectedAnnualAmortizationExpenseRelatedToAcquiredIntangibleAssets

- us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseAfterYearFive
  - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]

### http://www.apple.com/taxonomy/role/DisclosureProvisionForIncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - aapl_IncomeTaxesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - aapl_IncomeTaxesLineItems
      - us-gaap_FederalIncomeTaxExpenseBenefitContinuingOperationsAbstract
      - us-gaap_StateAndLocalIncomeTaxExpenseBenefitContinuingOperationsAbstract
      - us-gaap_ForeignIncomeTaxExpenseBenefitContinuingOperationsAbstract
      - us-gaap_IncomeTaxExpenseBenefit [totalLabel]

### http://www.apple.com/taxonomy/role/DisclosureIncomeTaxesAdditionalInformation

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_IncomeTaxContingencyTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_IncomeTaxContingencyLineItems
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
      - us-gaap_EffectiveIncomeTaxRateReconciliationForeignIncomeTaxRateDifferential
      - us-gaap_UndistributedEarningsOfForeignSubsidiaries
      - us-gaap_DeferredTaxLiabilityNotRecognizedAmountOfUnrecognizedDeferredTaxLiabilityUndistributedEarningsOfForeignSubsidiaries
      - aapl_CashCashEquivalentsAndMarketableSecuritiesHeldByForeignSubsidiaries
      - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
      - aapl_ShareBasedCompensationTaxExpenseBenefit
      - aapl_PercentageOfIncomeTaxExaminationMinimumLikelihoodOfTaxBenefitsBeingRealizedUponSettlement
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccrued
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestExpense
      - aapl_IncomeTaxContingencyNumberOfSubsidiaries
      - aapl_IncomeTaxContingencyPeriodOfOccurrence

### http://www.apple.com/taxonomy/role/DisclosureReconciliationOfTheProvisionForIncomeTaxes

- us-gaap_IncomeTaxDisclosureAbstract
  - aapl_IncomeTaxesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - aapl_IncomeTaxesLineItems
      - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
      - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
      - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
      - us-gaap_IncomeTaxReconciliationDeductionsQualifiedProductionActivities
      - us-gaap_IncomeTaxReconciliationTaxCreditsResearch
      - us-gaap_IncomeTaxReconciliationOtherAdjustments
      - us-gaap_IncomeTaxExpenseBenefit [totalLabel]
      - us-gaap_EffectiveIncomeTaxRateContinuingOperations

### http://www.apple.com/taxonomy/role/DisclosureSignificantComponentsOfTheCompanysDeferredTaxAssetsAndLiabilities

- us-gaap_IncomeTaxDisclosureAbstract
  - aapl_ComponentsOfDeferredTaxAssetsAndLiabilitiesTable

### http://www.apple.com/taxonomy/role/DisclosureSignificantComponentsOfTheCompanysDeferredTaxAssetsAndLiabilitiesParenthetical

- us-gaap_IncomeTaxDisclosureAbstract
  - aapl_ComponentsOfDeferredTaxAssetsAndLiabilitiesTable

### http://www.apple.com/taxonomy/role/DisclosureAggregateChangesInGrossUnrecognizedTaxBenefitsExcludingInterestAndPenalties

- us-gaap_IncomeTaxDisclosureAbstract
  - aapl_IncomeTaxesTable
    - dei_LegalEntityAxis
    - aapl_IncomeTaxesLineItems
      - us-gaap_UnrecognizedTaxBenefits
      - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromPriorPeriodTaxPositions
      - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromPriorPeriodTaxPositions
      - us-gaap_UnrecognizedTaxBenefitsIncreasesResultingFromCurrentPeriodTaxPositions
      - us-gaap_UnrecognizedTaxBenefitsDecreasesResultingFromSettlementsWithTaxingAuthorities
      - us-gaap_UnrecognizedTaxBenefitsReductionsResultingFromLapseOfApplicableStatuteOfLimitations
      - us-gaap_UnrecognizedTaxBenefits

### http://www.apple.com/taxonomy/role/DisclosurePretaxAmountsReclassifiedFromAOCIIntoConsolidatedStatementsOfOperations

- us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeTable
  - dei_LegalEntityAxis
  - us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_IncomeStatementLocationAxis
    - us-gaap_IncomeStatementLocationDomain
      - us-gaap_SalesMember
      - us-gaap_CostOfSalesMember
      - us-gaap_NonoperatingIncomeExpenseMember
  - us-gaap_ReclassificationAdjustmentOutOfAccumulatedOtherComprehensiveIncomeLineItems
    - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIOnDerivativesBeforeTax
    - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesBeforeTax
    - us-gaap_ReclassificationFromAccumulatedOtherComprehensiveIncomeCurrentPeriodBeforeTax

### http://www.apple.com/taxonomy/role/DisclosureChangeInAccumulatedOtherComprehensiveIncomeByComponent

- aapl_UncategorizedAbstract
  - us-gaap_AccumulatedOtherComprehensiveIncomeLossTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementEquityComponentsAxis
      - us-gaap_EquityComponentDomain
    - us-gaap_AccumulatedOtherComprehensiveIncomeLossLineItems
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossBeforeReclassificationsBeforeTax
      - us-gaap_ReclassificationFromAccumulatedOtherComprehensiveIncomeCurrentPeriodBeforeTax
      - us-gaap_OtherComprehensiveIncomeLossTax
      - us-gaap_OtherComprehensiveIncomeLossNetOfTax [totalLabel]
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax

### http://www.apple.com/taxonomy/role/DisclosureSummaryOfShareBasedCompensationExpense

- us-gaap_IncomeStatementLocationAxis
  - us-gaap_IncomeStatementLocationDomain
    - us-gaap_CostOfSalesMember
    - us-gaap_ResearchAndDevelopmentExpenseMember
    - us-gaap_SellingGeneralAndAdministrativeExpensesMember

### http://www.apple.com/taxonomy/role/DisclosureReconciliationOfSegmentOperatingIncomeToConsolidatedStatementsOfOperations

- us-gaap_SegmentReportingAbstract
  - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ConsolidationItemsAxis
      - us-gaap_ConsolidationItemsDomain
    - us-gaap_SegmentReportingReconcilingItemForOperatingProfitLossFromSegmentToConsolidatedLineItems
      - us-gaap_OperatingIncomeLoss
      - us-gaap_ResearchAndDevelopmentExpense
      - us-gaap_OtherOperatingIncomeExpenseNet

### http://www.apple.com/taxonomy/role/DisclosureNetSales

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - dei_LegalEntityAxis
  - us-gaap_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_SalesRevenueNet

### http://www.apple.com/taxonomy/role/DisclosureLongLivedAssets

- us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
  - dei_LegalEntityAxis
  - us-gaap_StatementGeographicalAxis
  - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
    - us-gaap_NoncurrentAssets

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsIncomeTaxDisclosureTextBlock

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsIncomeTaxDisclosureTextBlockTables

- us-gaap_IncomeTaxDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
      - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
      - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
      - us-gaap_SummaryOfPositionsForWhichSignificantChangeInUnrecognizedTaxBenefitsIsReasonablyPossibleTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsComprehensiveIncomeNoteTextBlock

- us-gaap_EquityAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ComprehensiveIncomeNoteTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsComprehensiveIncomeNoteTextBlockTables

- us-gaap_EquityAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeTableTextBlock
      - us-gaap_ScheduleOfAccumulatedOtherComprehensiveIncomeLossTableTextBlock

## 资产负债表结构 (Balance Sheet Structure)

### http://www.apple.com/taxonomy/role/StatementOfFinancialPositionClassified

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_AssetsAbstract
      - us-gaap_LiabilitiesAndStockholdersEquityAbstract

### http://www.apple.com/taxonomy/role/StatementOfFinancialPositionClassifiedParenthetical

- us-gaap_StatementOfFinancialPositionAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_AllowanceForDoubtfulAccountsReceivableCurrent
      - us-gaap_CommonStockParOrStatedValuePerShare
      - us-gaap_CommonStockSharesAuthorized
      - us-gaap_CommonStockSharesIssued
      - us-gaap_CommonStockSharesOutstanding

### http://www.apple.com/taxonomy/role/StatementOfCashFlowsIndirect

- us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperationsAbstract
  - us-gaap_NetIncomeLoss
  - us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperations [totalLabel]
- us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperationsAbstract
  - us-gaap_PaymentsToAcquireAvailableForSaleSecurities
  - us-gaap_ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities
  - us-gaap_ProceedsFromSaleOfAvailableForSaleSecurities
  - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
  - us-gaap_PaymentsToAcquirePropertyPlantAndEquipment
  - us-gaap_PaymentsToAcquireIntangibleAssets
  - us-gaap_PaymentsForProceedsFromOtherInvestingActivities
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperations [totalLabel]
- us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperationsAbstract
  - us-gaap_ProceedsFromIssuanceOfCommonStock
  - us-gaap_ExcessTaxBenefitFromShareBasedCompensationFinancingActivities
  - us-gaap_PaymentsRelatedToTaxWithholdingForShareBasedCompensation
  - aapl_PaymentsOfDividendsAndDividendEquivalentsOnCommonStockAndRestrictedStockUnits
  - us-gaap_PaymentsForRepurchaseOfCommonStock
  - us-gaap_ProceedsFromIssuanceOfLongTermDebt
  - us-gaap_ProceedsFromRepaymentsOfCommercialPaper
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperations [totalLabel]
- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_StatementTable
- us-gaap_SupplementalCashFlowInformationAbstract
  - us-gaap_IncomeTaxesPaidNet
  - us-gaap_InterestPaid

### http://www.apple.com/taxonomy/role/DisclosureCashAndAvailableforSaleSecuritiesAdjustedCostGrossUnrealizedGainsGrossUnrealizedLossesAndFairValueRecordedAsCashAndCashEquivalentsOrShortTermOrLongTermMarketableSecurities

- us-gaap_InvestmentsDebtAndEquitySecuritiesAbstract
  - us-gaap_ScheduleOfAvailableForSaleSecuritiesTable

### http://www.apple.com/taxonomy/role/DisclosureDerivativeInstrumentsAtGrossFairValue

- us-gaap_DerivativeAssetsAbstract
  - us-gaap_DerivativeFairValueOfDerivativeAsset

### http://www.apple.com/taxonomy/role/DisclosureGoodwillAndOtherIntangibleAssetsAdditionalInformation

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfAcquiredFiniteLivedIntangibleAssetByMajorClassTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_BusinessAcquisitionAxis
      - us-gaap_BusinessAcquisitionAcquireeDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_VestingAxis
      - us-gaap_VestingDomain
    - us-gaap_AcquiredFiniteLivedIntangibleAssetsLineItems
      - us-gaap_BusinessCombinationConsiderationTransferred1
      - us-gaap_GoodwillAcquiredDuringPeriod
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibleAssetsOtherThanGoodwill
      - us-gaap_BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedLiabilities
      - us-gaap_RepaymentsOfAssumedDebt
      - us-gaap_StockIssuedDuringPeriodSharesAcquisitions
      - us-gaap_StockIssuedDuringPeriodValueAcquisitions
      - us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife
      - us-gaap_AmortizationOfIntangibleAssets
      - us-gaap_AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife

### http://www.apple.com/taxonomy/role/DisclosureComponentsOfGrossAndNetIntangibleAssetBalances

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - aapl_AcquiredIntangibleAssetsIncludingGoodwillTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - aapl_AcquiredIntangibleAssetsIncludingGoodwillLineItems
      - us-gaap_FiniteLivedIntangibleAssetsGross
      - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization
      - us-gaap_FiniteLivedIntangibleAssetsNet [totalLabel]
      - us-gaap_IndefiniteLivedIntangibleAssetsExcludingGoodwill
      - us-gaap_IntangibleAssetsNetExcludingGoodwill [totalLabel]

### http://www.apple.com/taxonomy/role/DisclosureExpectedAnnualAmortizationExpenseRelatedToAcquiredIntangibleAssets

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_FiniteLivedIntangibleAssetsLineItems
      - us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract

### http://www.apple.com/taxonomy/role/DisclosureSignificantComponentsOfTheCompanysDeferredTaxAssetsAndLiabilities

- aapl_ComponentsOfDeferredTaxAssetsAndLiabilitiesTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - aapl_ComponentsOfDeferredTaxAssetsAndLiabilitiesLineItems
    - us-gaap_DeferredTaxAssetsGrossAbstract
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccruals
      - aapl_DeferredTaxAssetsBasisOfCapitalAssetsAndInvestments
      - us-gaap_DeferredTaxAssetsDeferredIncome
      - aapl_DeferredTaxAssetsDeferredCostSharing
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
      - aapl_DeferredTaxAssetsUnrealizedLosses
      - us-gaap_DeferredTaxAssetsOther
      - us-gaap_DeferredTaxAssetsNet [totalLabel]
    - us-gaap_DeferredTaxLiabilitiesAbstract
      - us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings
      - us-gaap_DeferredTaxLiabilitiesOther
      - us-gaap_DeferredIncomeTaxLiabilities [totalLabel]
    - us-gaap_DeferredIncomeTaxLiabilitiesNet

### http://www.apple.com/taxonomy/role/DisclosureSignificantComponentsOfTheCompanysDeferredTaxAssetsAndLiabilitiesParenthetical

- aapl_ComponentsOfDeferredTaxAssetsAndLiabilitiesTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - aapl_ComponentsOfDeferredTaxAssetsAndLiabilitiesLineItems
    - us-gaap_DeferredTaxAssetsGrossAbstract
      - us-gaap_DeferredTaxAssetsValuationAllowance

### http://www.apple.com/taxonomy/role/DisclosureSummaryOfDividendsDeclaredAndPaid

- us-gaap_EquityAbstract
  - aapl_DividendsTable

### http://www.apple.com/taxonomy/role/DisclosureShareholdersEquityAdditionalInformation

- aapl_StockholdersEquityNoteDisclosureTable
  - dei_LegalEntityAxis
  - aapl_StockholdersEquityNoteDisclosureLineItems
    - us-gaap_StockRepurchaseProgramAuthorizedAmount1
    - aapl_AmountUtilizedUnderShareRepurchaseProgram

### http://www.apple.com/taxonomy/role/DisclosureRestrictedStockUnitsActivityAndRelatedInformation

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
- us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsAggregateIntrinsicValueAbstract
  - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsAggregateIntrinsicValueNonvested

### http://www.apple.com/taxonomy/role/DisclosureSummaryOfShareBasedCompensationExpense

- us-gaap_EquityAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable

### http://www.apple.com/taxonomy/role/DisclosureChangesInAccruedWarrantiesAndRelatedCosts

- us-gaap_ProductWarrantyLiabilityTable
  - dei_LegalEntityAxis
  - us-gaap_ProductWarrantyLiabilityLineItems
    - us-gaap_MovementInStandardProductWarrantyAccrualRollForward

### http://www.apple.com/taxonomy/role/DisclosureFutureMinimumLeasePaymentsUnderNoncancelableOperatingLeases

- us-gaap_ScheduleOfOperatingLeasedAssetsTable
  - dei_LegalEntityAxis
  - us-gaap_OperatingLeasedAssetsLineItems
    - us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract

### http://www.apple.com/taxonomy/role/DisclosureLongLivedAssets

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- us-gaap_StatementGeographicalAxis
  - us-gaap_SegmentGeographicalDomain
    - country_US
    - country_CN
    - aapl_OtherCountriesMember
- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsGoodwillAndIntangibleAssetsDisclosureTextBlock

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_GoodwillAndIntangibleAssetsDisclosureTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsGoodwillAndIntangibleAssetsDisclosureTextBlockTables

- us-gaap_GoodwillAndIntangibleAssetsDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTableTextBlock
      - us-gaap_ScheduleOfIndefiniteLivedIntangibleAssetsTableTextBlock
      - us-gaap_ScheduleofFiniteLivedIntangibleAssetsFutureAmortizationExpenseTableTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsStockholdersEquityNoteDisclosureTextBlock

- us-gaap_EquityAbstract
  - us-gaap_StatementTable

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsStockholdersEquityNoteDisclosureTextBlockTables

- us-gaap_EquityAbstract
  - us-gaap_StatementTable

## 现金流量表结构 (Cash Flow Structure)

### http://www.apple.com/taxonomy/role/StatementOfCashFlowsIndirect

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_CashAndCashEquivalentsAtCarryingValue
    - us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperationsAbstract
    - us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperationsAbstract
    - us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperationsAbstract
    - us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease [totalLabel]
    - us-gaap_CashAndCashEquivalentsAtCarryingValue
    - us-gaap_SupplementalCashFlowInformationAbstract
- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInInventories
  - aapl_IncreaseDecreaseInNonTradeReceivables
  - us-gaap_IncreaseDecreaseInOtherOperatingAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInDeferredRevenue
  - us-gaap_IncreaseDecreaseInOtherOperatingLiabilities

### http://www.apple.com/taxonomy/role/DisclosureCashAndAvailableforSaleSecuritiesAdjustedCostGrossUnrealizedGainsGrossUnrealizedLossesAndFairValueRecordedAsCashAndCashEquivalentsOrShortTermOrLongTermMarketableSecurities

- us-gaap_ScheduleOfAvailableForSaleSecuritiesTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_FairValueByFairValueHierarchyLevelAxis
    - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
      - us-gaap_FairValueInputsLevel1Member
      - us-gaap_FairValueInputsLevel2Member
  - us-gaap_InvestmentTypeAxis
    - us-gaap_InvestmentTypeCategorizationMember
      - us-gaap_CashMember
      - us-gaap_MoneyMarketFundsMember
      - us-gaap_EquitySecuritiesMember
      - us-gaap_USTreasurySecuritiesMember
      - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
      - us-gaap_ForeignGovernmentDebtSecuritiesMember
      - us-gaap_BankTimeDepositsMember
      - us-gaap_CommercialPaperMember
      - us-gaap_CorporateDebtSecuritiesMember
      - us-gaap_USStatesAndPoliticalSubdivisionsMember
      - us-gaap_AssetBackedSecuritiesMember
  - us-gaap_ScheduleOfAvailableForSaleSecuritiesLineItems
    - us-gaap_AvailableForSaleSecuritiesAmortizedCost [totalLabel]
    - us-gaap_AvailableForSaleSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
    - us-gaap_AvailableForSaleSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
    - us-gaap_AvailableForSaleSecurities
    - us-gaap_CashAndCashEquivalentsAtCarryingValue
    - us-gaap_AvailableForSaleSecuritiesCurrent
    - us-gaap_AvailableForSaleSecuritiesNoncurrent

### http://www.apple.com/taxonomy/role/DisclosurePreTaxGainsAndLossesOfDerivativeAndNonDerivativeInstrumentsDesignatedAsCashFlowNetInvestmentAndFairValueHedges

- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ForeignExchangeContractMember
    - us-gaap_InterestRateContractMember
    - aapl_ForeignCurrencyDebtMember
- dei_LegalEntityAxis
  - dei_EntityDomain
- us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
  - us-gaap_HedgingRelationshipDomain
    - us-gaap_CashFlowHedgingMember
    - us-gaap_NetInvestmentHedgingMember
    - us-gaap_FairValueHedgingMember
- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipByIncomeStatementLocationByDerivativeInstrumentRiskTable
- us-gaap_DerivativeInstrumentsGainLossLineItems
  - us-gaap_DerivativeInstrumentsGainLossRecognizedInOtherComprehensiveIncomeEffectivePortionNet
  - us-gaap_DerivativeInstrumentsGainLossReclassifiedFromAccumulatedOCIIntoIncomeEffectivePortionNet
  - us-gaap_DerivativeGainLossOnDerivativeNet
  - us-gaap_ChangeInUnrealizedGainLossOnHedgedItemInFairValueHedge1

### http://www.apple.com/taxonomy/role/DisclosureSummaryOfCashFlowsAssociatedWithIssuanceAndMaturitiesOfCommercialPaper

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ScheduleOfShortTermDebtTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ShortTermDebtLineItems
      - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInThreeMonthsOrLessAlternativeAbstract
      - us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInMoreThanThreeMonthsAlternativeAbstract
      - us-gaap_ProceedsFromRepaymentsOfCommercialPaper [totalLabel]

### http://www.apple.com/taxonomy/role/DisclosureFutureMinimumLeasePaymentsUnderNoncancelableOperatingLeases

- us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueCurrent
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInTwoYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInThreeYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFourYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFiveYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueThereafter
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDue [totalLabel]

## 股东权益结构 (Equity Structure)

### http://www.apple.com/taxonomy/role/DisclosureShareholdersEquityAdditionalInformation

- dei_LegalEntityAxis
  - dei_EntityDomain
- aapl_UncategorizedAbstract
  - aapl_StockholdersEquityNoteDisclosureTable

### http://www.apple.com/taxonomy/role/DisclosureAcceleratedShareRepurchaseActivityAndRelatedInformation

- us-gaap_AcceleratedShareRepurchasesTable
  - dei_LegalEntityAxis
  - us-gaap_ShareRepurchaseProgramAxis
    - us-gaap_ShareRepurchaseProgramDomain
      - aapl_AcceleratedShareRepurchaseAgreementMayTwentyFifteenMember
      - aapl_AcceleratedShareRepurchaseAgreementAugustTwentyFourteenMember
      - aapl_AcceleratedShareRepurchaseAgreementJanuaryTwentyFourteenMember
      - aapl_AcceleratedShareRepurchaseAgreementAprilTwentyThirteenMember
  - us-gaap_AcceleratedShareRepurchasesLineItems
    - aapl_StockRepurchaseProgramCompletionDate
    - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
    - us-gaap_AcceleratedShareRepurchasesFinalPricePaidPerShare
    - aapl_UpfrontPaymentUnderAcceleratedShareRepurchaseProgram

### http://www.apple.com/taxonomy/role/DisclosureAcceleratedShareRepurchaseActivityAndRelatedInformationParenthetical

- us-gaap_AcceleratedShareRepurchasesTable
  - us-gaap_ShareRepurchaseProgramAxis
    - us-gaap_ShareRepurchaseProgramDomain
      - aapl_AcceleratedShareRepurchaseAgreementMayTwentyFifteenMember
      - aapl_AcceleratedShareRepurchaseAgreementAugustTwentyFourteenMember
  - dei_LegalEntityAxis
  - us-gaap_AcceleratedShareRepurchasesLineItems
    - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares

### http://www.apple.com/taxonomy/role/DisclosureRepurchasesOfCommonSharesInOpenMarket

- aapl_ScheduleOfStockRepurchaseProgramTable
  - dei_LegalEntityAxis
  - us-gaap_ShareRepurchaseProgramAxis
    - us-gaap_ShareRepurchaseProgramDomain
      - aapl_OpenMarketRepurchasesMember
  - aapl_StockRepurchaseProgramLineItems
    - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
    - aapl_StockRepurchasedAndRetiredDuringPeriodWeightedAveragePrice
    - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue

### http://www.apple.com/taxonomy/role/DisclosureBenefitPlansAdditionalInformation

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - dei_LegalEntityAxis
    - us-gaap_PlanNameAxis
    - us-gaap_RangeAxis
    - us-gaap_AwardTypeAxis
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAuthorized
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardExpirationPeriod
      - aapl_ShareBasedCompensationArrangementByShareBasedPaymentAwardPeriodOfTimeOptionsBecomeExercisable
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardExpirationDate
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardPurchasePriceOfCommonStockPercent
      - aapl_ShareBasedCompensationArrangementByShareBasedPaymentAwardOfferingTerm
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardMaximumEmployeeSubscriptionRate
      - aapl_EmployeeStockPurchaseProgramAuthorizedAmount
      - us-gaap_DefinedContributionPlanMaximumAnnualContributionsPerEmployeeAmount
      - us-gaap_DefinedContributionPlanEmployerMatchingContributionPercent
      - aapl_DefinedContributionPlanContributionRatesAsPercentageOfEmployeesEarnings
      - us-gaap_DefinedContributionPlanCostRecognized
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue [totalLabel]
      - us-gaap_SharesPaidForTaxWithholdingForShareBasedCompensation
      - us-gaap_EmployeeServiceShareBasedCompensationCashFlowEffectCashUsedToSettleAwards
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsOutstandingWeightedAverageRemainingContractualTerm2
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingIntrinsicValue
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue [totalLabel]
      - us-gaap_IncomeTaxReconciliationNondeductibleExpenseShareBasedCompensationCost
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
      - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
- us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
  - aapl_EmployeeStockPurchasePlanMember

### http://www.apple.com/taxonomy/role/DisclosureRestrictedStockUnitsActivityAndRelatedInformation

- us-gaap_DisclosureOfCompensationRelatedCostsSharebasedPaymentsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_AwardTypeAxis
      - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardLineItems
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedRollForward
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedWeightedAverageGrantDateFairValueRollForward
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardEquityInstrumentsOtherThanOptionsAggregateIntrinsicValueAbstract

### http://www.apple.com/taxonomy/role/DisclosureSummaryOfShareBasedCompensationExpense

- us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTable
  - dei_LegalEntityAxis
  - us-gaap_IncomeStatementLocationAxis
  - us-gaap_EmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsLineItems
    - us-gaap_AllocatedShareBasedCompensationExpense

### http://www.apple.com/taxonomy/role/DisclosureSummaryOfQuarterlyFinancialInformation

- us-gaap_EarningsPerShareAbstract
  - us-gaap_EarningsPerShareBasic
  - us-gaap_EarningsPerShareDiluted

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsStockholdersEquityNoteDisclosureTextBlock

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsStockholdersEquityNoteDisclosureTextBlockTables

- us-gaap_StatementTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - us-gaap_StatementLineItems
    - us-gaap_DividendsDeclaredTableTextBlock
    - us-gaap_AcceleratedShareRepurchasesTextBlock
    - aapl_ScheduleOfCommonStockRepurchasedTableTextBlock

## 其他结构 (Other Structure)

### http://www.apple.com/taxonomy/role/DocumentandEntityInformation

- aapl_DocumentAndEntityInformationAbstract
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
      - dei_EntityCommonStockSharesOutstanding
      - dei_EntityPublicFloat

### http://www.apple.com/taxonomy/role/DisclosureSummaryOfSignificantAccountingPoliciesAdditionalInformation

- us-gaap_AccountingPoliciesAbstract
  - aapl_SignificantAccountingPoliciesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - aapl_SignificantAccountingPoliciesLineItems
      - aapl_DeliverablesInArrangement
      - aapl_RevenueRecognitionMultipleDeliverableArrangementsDecreaseInSellingPriceAmount
      - us-gaap_AdvertisingExpense
      - aapl_PercentageOfIncomeTaxExaminationMinimumLikelihoodOfTaxBenefitsBeingRealizedUponSettlement
      - us-gaap_PropertyPlantAndEquipmentUsefulLife
      - us-gaap_DepreciationAndAmortization
      - us-gaap_GoodwillImpairmentLoss
      - us-gaap_ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill
      - us-gaap_FiniteLivedIntangibleAssetUsefulLife

### http://www.apple.com/taxonomy/role/DisclosureFinancialInstrumentsAdditionalInformation

- us-gaap_FairValueDisclosuresAbstract
  - aapl_FinancialInstrumentsTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ConcentrationRiskByBenchmarkAxis
      - us-gaap_ConcentrationRiskBenchmarkDomain
    - us-gaap_ConcentrationRiskByTypeAxis
      - us-gaap_ConcentrationRiskTypeDomain
    - us-gaap_MajorCustomersAxis
      - us-gaap_NameOfMajorCustomerDomain
    - aapl_FinancialInstrumentsLineItems
      - aapl_LongTermMarketableSecuritiesMaturitiesTermMinimum
      - aapl_LongTermMarketableSecuritiesMaturitiesTermMaximum
      - us-gaap_MaximumLengthOfTimeForeignCurrencyCashFlowHedge
      - us-gaap_MaximumLengthOfTimeHedgedInInterestRateCashFlowHedge1
      - aapl_CollateralAlreadyReceivedAggregateFairValue
      - aapl_DerivativeAssetsReducedForMasterNettingArrangements
      - aapl_DerivativeLiabilitiesReducedForMasterNettingArrangements
      - us-gaap_DerivativeFairValueOfDerivativeNet
      - aapl_NumberOfCustomersWithSignificantAccountsReceivableBalance
      - us-gaap_ConcentrationRiskPercentage1
      - aapl_NumberOfSignificantVendors

### http://www.apple.com/taxonomy/role/DisclosureDerivativeInstrumentsAtGrossFairValue

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_FairValuesDerivativesBalanceSheetLocationByDerivativeContractTypeByHedgingDesignationTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_BalanceSheetLocationAxis
      - us-gaap_BalanceSheetLocationDomain
    - us-gaap_DerivativesFairValueLineItems
      - us-gaap_DerivativeAssetsAbstract
      - us-gaap_DerivativeLiabilitiesAbstract

### http://www.apple.com/taxonomy/role/DisclosureNotionalAmountsOfOutstandingDerivativeInstrumentsAndCreditRiskAmountsAssociatedWithOutstandingOrUnsettledDerivativeInstruments

- us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureAbstract
  - us-gaap_DerivativeTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_HedgingDesignationAxis
      - us-gaap_HedgingDesignationDomain
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativeLineItems
      - invest_DerivativeNotionalAmount
      - aapl_CreditRiskAmountOfForeignCurrencyDerivativeInstrumentsDesignatedAsHedgingInstruments
      - aapl_CreditRiskAmountOfInterestRateDerivativeInstrumentsDesignatedAsHedgingInstruments
      - aapl_CreditRiskAmountOfForeignCurrencyDerivativeInstrumentsNotDesignatedAsHedgingInstruments

### http://www.apple.com/taxonomy/role/DisclosurePropertyPlantAndEquipmentNet

- us-gaap_PropertyPlantAndEquipmentAbstract
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet [totalLabel]

### http://www.apple.com/taxonomy/role/DisclosureOtherNonCurrentLiabilities

- us-gaap_OtherLiabilitiesDisclosureAbstract
  - aapl_ScheduleOfOtherLiabilitiesTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - aapl_ScheduleOfOtherLiabilitiesLineItems
      - us-gaap_DeferredTaxLiabilitiesNoncurrent
      - us-gaap_OtherAccruedLiabilitiesNoncurrent
      - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.apple.com/taxonomy/role/DisclosureAggregateChangesInGrossUnrecognizedTaxBenefitsExcludingInterestAndPenalties

- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.apple.com/taxonomy/role/DisclosureDebtAdditionalInformation

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_ShortTermDebtTypeAxis
      - us-gaap_ShortTermDebtTypeDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_DerivativeInstrumentRiskAxis
      - us-gaap_DerivativeContractTypeDomain
    - us-gaap_DerivativeInstrumentsGainLossByHedgingRelationshipAxis
      - us-gaap_HedgingRelationshipDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_CommercialPaper
      - us-gaap_ShortTermDebtWeightedAverageInterestRate
      - us-gaap_DebtInstrumentTerm
      - us-gaap_DebtInstrumentCarryingAmount
      - invest_DerivativeNotionalAmount
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_SeniorNotes
      - us-gaap_InterestExpenseDebt
      - us-gaap_LongTermDebtFairValue

### http://www.apple.com/taxonomy/role/DisclosureSummaryOfTermDebt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_SeniorNotes
      - us-gaap_DebtInstrumentCarryingAmount
      - aapl_DebtInstrumentMaturityYear
      - us-gaap_DebtInstrumentUnamortizedDiscount
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - aapl_HedgeAccountingAdjustmentsRelatedToLongTermDebt
      - us-gaap_LongTermDebtCurrent
      - us-gaap_LongTermDebtNoncurrent
      - aapl_DebtInstrumentMaturityYearRangeStart
      - aapl_DebtInstrumentMaturityYearRangeEnd
      - us-gaap_DebtInstrumentInterestRateEffectivePercentageRateRangeMinimum
      - us-gaap_DebtInstrumentInterestRateEffectivePercentageRateRangeMaximum

### http://www.apple.com/taxonomy/role/DisclosureSummaryOfTermDebtParenthetical

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_DebtInstrumentLineItems
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentInterestRateStatedPercentageRateRangeMinimum
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_DebtInstrumentInterestRateStatedPercentageRateRangeMaximum

### http://www.apple.com/taxonomy/role/DisclosureDebtInstrumentFuturePrincipalPayments

- us-gaap_DebtDisclosureAbstract
  - aapl_LongTermDebtMaturitiesRepaymentsOfPrincipalTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - aapl_LongTermDebtMaturitiesRepaymentsOfPrincipalLineItems
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive
      - us-gaap_LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive
      - us-gaap_DebtInstrumentCarryingAmount [totalLabel]

### http://www.apple.com/taxonomy/role/DisclosureSummaryOfDividendsDeclaredAndPaid

- aapl_DividendsTable
  - dei_LegalEntityAxis
    - dei_EntityDomain
  - aapl_DividendsLineItems
    - us-gaap_CommonStockDividendsPerShareDeclared
    - us-gaap_PaymentsOfDividends

### http://www.apple.com/taxonomy/role/DisclosureAcceleratedShareRepurchaseActivityAndRelatedInformation

- dei_LegalEntityAxis
  - dei_EntityDomain
- aapl_UncategorizedAbstract
  - us-gaap_AcceleratedShareRepurchasesTable

### http://www.apple.com/taxonomy/role/DisclosureAcceleratedShareRepurchaseActivityAndRelatedInformationParenthetical

- dei_LegalEntityAxis
  - dei_EntityDomain
- aapl_UncategorizedAbstract
  - us-gaap_AcceleratedShareRepurchasesTable

### http://www.apple.com/taxonomy/role/DisclosureRepurchasesOfCommonSharesInOpenMarket

- dei_LegalEntityAxis
  - dei_EntityDomain
- aapl_UncategorizedAbstract
  - aapl_ScheduleOfStockRepurchaseProgramTable

### http://www.apple.com/taxonomy/role/DisclosurePretaxAmountsReclassifiedFromAOCIIntoConsolidatedStatementsOfOperations

- us-gaap_DerivativeInstrumentRiskAxis
  - us-gaap_DerivativeContractTypeDomain
    - us-gaap_ForeignExchangeContractMember
    - us-gaap_InterestRateContractMember
- dei_LegalEntityAxis
  - dei_EntityDomain
- aapl_UncategorizedAbstract
  - us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeTable

### http://www.apple.com/taxonomy/role/DisclosureBenefitPlansAdditionalInformation

- us-gaap_PlanNameAxis
  - us-gaap_PlanNameDomain
    - aapl_EmployeeStockPurchasePlanTwentyFourteenMember
    - aapl_EmployeeStockPlanTwentyZeroThreePlanMember
    - aapl_DirectorsPlanMember
- us-gaap_AwardTypeAxis
  - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
- us-gaap_RangeAxis
  - us-gaap_RangeMember
    - us-gaap_MinimumMember
    - us-gaap_MaximumMember
- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.apple.com/taxonomy/role/DisclosureSummaryOfShareBasedCompensationExpense

- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.apple.com/taxonomy/role/DisclosureChangesInAccruedWarrantiesAndRelatedCosts

- us-gaap_MovementInStandardProductWarrantyAccrualRollForward
  - us-gaap_StandardProductWarrantyAccrual
  - us-gaap_StandardProductWarrantyAccrualPayments
  - us-gaap_StandardProductWarrantyAccrualWarrantiesIssued
  - us-gaap_StandardProductWarrantyAccrual
- dei_LegalEntityAxis
  - dei_EntityDomain
- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_ProductWarrantyLiabilityTable

### http://www.apple.com/taxonomy/role/DisclosureCommitmentsAndContingenciesAdditionalInformation

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - aapl_CommitmentsAndContingenciesDisclosureTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_LeaseArrangementTypeAxis
      - us-gaap_LeaseArrangementTypeDomain
    - us-gaap_RangeAxis
      - us-gaap_RangeMember
    - us-gaap_LossContingenciesByNatureOfContingencyAxis
      - us-gaap_LossContingencyNatureDomain
    - us-gaap_LitigationCaseAxis
      - us-gaap_LitigationCaseTypeDomain
    - aapl_CommitmentsAndContingenciesDisclosureLineItems
      - us-gaap_LossContingencyAccrualAtCarryingValue
      - us-gaap_LongtermPurchaseCommitmentPeriod
      - us-gaap_LesseeLeasingArrangementsOperatingLeasesTermOfContract
      - us-gaap_NumberOfStores
      - us-gaap_OperatingLeasesFutureMinimumPaymentsDue
      - us-gaap_OperatingLeasesRentExpenseNet
      - aapl_OffBalanceSheetInventoryPurchaseCommitment
      - us-gaap_UnrecordedUnconditionalPurchaseObligationBalanceSheetAmount
      - aapl_ResultOfLegalProceedings
      - us-gaap_GainContingencyUnrecordedAmount

### http://www.apple.com/taxonomy/role/DisclosureFutureMinimumLeasePaymentsUnderNoncancelableOperatingLeases

- dei_LegalEntityAxis
  - dei_EntityDomain
- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_ScheduleOfOperatingLeasedAssetsTable

### http://www.apple.com/taxonomy/role/DisclosureSummaryInformationByOperatingSegment

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_SalesRevenueNet
      - us-gaap_OperatingIncomeLoss

### http://www.apple.com/taxonomy/role/DisclosureSegmentInformationAndGeographicDataAdditionalInformation

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_EntityWideDisclosureOnGeographicAreasDescriptionOfRevenueFromExternalCustomers
      - us-gaap_SegmentReportingDisclosureOfMajorCustomers

### http://www.apple.com/taxonomy/role/DisclosureNetSales

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
- us-gaap_StatementGeographicalAxis
  - us-gaap_SegmentGeographicalDomain
    - country_US
    - country_CN
    - aapl_OtherCountriesMember
- dei_LegalEntityAxis
  - dei_EntityDomain

### http://www.apple.com/taxonomy/role/DisclosureNetSalesByProduct

- us-gaap_SegmentReportingAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_ProductOrServiceAxis
      - us-gaap_ProductsAndServicesDomain
    - us-gaap_SegmentReportingInformationLineItems
      - us-gaap_SalesRevenueNet

### http://www.apple.com/taxonomy/role/DisclosureSummaryOfQuarterlyFinancialInformation

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - aapl_QuarterlyFinancialInformationTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - aapl_QuarterlyFinancialInformationLineItems
      - us-gaap_SelectedQuarterlyFinancialInformationAbstract

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsBasisOfPresentationAndSignificantAccountingPoliciesTextBlock

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_BasisOfPresentationAndSignificantAccountingPoliciesTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsBasisOfPresentationAndSignificantAccountingPoliciesTextBlockPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_BasisOfAccountingPolicyPolicyTextBlock
      - us-gaap_RevenueRecognitionPolicyTextBlock
      - us-gaap_ShippingAndHandlingCostPolicyTextBlock
      - us-gaap_StandardProductWarrantyPolicy
      - us-gaap_ResearchDevelopmentAndComputerSoftwarePolicyTextBlock
      - us-gaap_AdvertisingCostsPolicyTextBlock
      - us-gaap_CompensationRelatedCostsPolicyTextBlock
      - us-gaap_IncomeTaxPolicyTextBlock
      - us-gaap_EarningsPerSharePolicyTextBlock
      - us-gaap_CashAndCashEquivalentsPolicyTextBlock
      - us-gaap_DerivativesPolicyTextBlock
      - us-gaap_ReceivablesTradeAndOtherAccountsReceivableAllowanceForDoubtfulAccountsPolicy
      - us-gaap_InventoryPolicyTextBlock
      - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
      - us-gaap_GoodwillAndIntangibleAssetsPolicyTextBlock
      - us-gaap_FairValueMeasurementPolicyPolicyTextBlock
      - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsBasisOfPresentationAndSignificantAccountingPoliciesTextBlockTables

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfEarningsPerShareBasicAndDilutedTableTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsFinancialInstrumentsDisclosureTextBlock

- us-gaap_InvestmentsAllOtherInvestmentsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_FinancialInstrumentsDisclosureTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsFinancialInstrumentsDisclosureTextBlockTables

- us-gaap_InvestmentsAllOtherInvestmentsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_AvailableForSaleSecuritiesTextBlock
      - us-gaap_ScheduleOfCashAndCashEquivalentsTableTextBlock
      - us-gaap_ScheduleOfDerivativeInstrumentsInStatementOfFinancialPositionFairValueTextBlock
      - us-gaap_ScheduleOfDerivativeInstrumentsGainLossInStatementOfFinancialPerformanceTextBlock
      - aapl_NotionalAndCreditRiskAmountsOfOutstandingDerivativePositionsDisclosureTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsAdditionalFinancialInformationDisclosureTextBlock

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_AdditionalFinancialInformationDisclosureTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsAdditionalFinancialInformationDisclosureTextBlockTables

- us-gaap_OrganizationConsolidationAndPresentationOfFinancialStatementsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_PropertyPlantAndEquipmentTextBlock
      - us-gaap_OtherNoncurrentLiabilitiesTableTextBlock
      - us-gaap_InterestAndOtherIncomeTableTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsDebtDisclosureTextBlock

- us-gaap_DebtDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_DebtDisclosureTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsDebtDisclosureTextBlockTables

- us-gaap_DebtDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - aapl_CommercialPaperCashFlowSummaryTableTextBlock
      - us-gaap_ScheduleOfDebtInstrumentsTextBlock
      - us-gaap_ScheduleOfMaturitiesOfLongTermDebtTableTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsCompensationAndEmployeeBenefitPlansTextBlock

- us-gaap_PostemploymentBenefitsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_CompensationAndEmployeeBenefitPlansTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsCompensationAndEmployeeBenefitPlansTextBlockTables

- us-gaap_PostemploymentBenefitsAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfNonvestedRestrictedStockUnitsActivityTableTextBlock
      - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsCommitmentsAndContingenciesDisclosureTextBlock

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsCommitmentsAndContingenciesDisclosureTextBlockTables

- us-gaap_CommitmentsAndContingenciesDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfProductWarrantyLiabilityTableTextBlock
      - us-gaap_ScheduleOfFutureMinimumRentalPaymentsForOperatingLeasesTableTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsSegmentReportingDisclosureTextBlock

- us-gaap_SegmentReportingAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsSegmentReportingDisclosureTextBlockTables

- us-gaap_SegmentReportingAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
      - us-gaap_ReconciliationOfOperatingProfitLossFromSegmentsToConsolidatedTextBlock
      - us-gaap_RevenueFromExternalCustomersByGeographicAreasTableTextBlock
      - us-gaap_LongLivedAssetsByGeographicAreasTableTextBlock
      - us-gaap_ScheduleOfEntityWideInformationRevenueFromExternalCustomersByProductsAndServicesTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsQuarterlyFinancialInformationTextBlock

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_QuarterlyFinancialInformationTextBlock

### http://www.apple.com/taxonomy/role/NotesToFinancialStatementsQuarterlyFinancialInformationTextBlockTables

- us-gaap_QuarterlyFinancialInformationDisclosureAbstract
  - us-gaap_StatementTable
    - dei_LegalEntityAxis
      - dei_EntityDomain
    - us-gaap_StatementLineItems
      - us-gaap_ScheduleOfQuarterlyFinancialInformationTableTextBlock

