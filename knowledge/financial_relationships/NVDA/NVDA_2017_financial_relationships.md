# NVDA 2017 财务关系分析

## 损益表结构 (Income Statement Structure)

### http://www.nvidia.com/role/ConsolidatedStatementsOfCashFlows

- nvda_AdjustmentsToReconcileNetIncomeLossToNetCashProvidedByOperatingActivities
  - us-gaap_DepreciationAndAmortization
  - us-gaap_ShareBasedCompensation
  - nvda_RestructuringchargesNoncash
  - us-gaap_AmortizationOfDebtDiscountPremium
  - nvda_GainsonSalesoflonglivedassetsandinvestment
  - us-gaap_GainsLossesOnExtinguishmentOfDebt
  - us-gaap_DeferredIncomeTaxExpenseBenefit
  - us-gaap_ExcessTaxBenefitFromShareBasedCompensationOperatingActivities
  - us-gaap_OtherNoncashIncomeExpense

### http://www.nvidia.com/role/ConsolidatedStatementsOfComprehensiveIncome

- nvda_StatementOfComprehensiveIncomeAbstract
  - us-gaap_StatementTable
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_StatementLineItems
      - us-gaap_NetIncomeLoss
      - us-gaap_AvailableforsaleSecuritiesGrossUnrealizedGainLoss1
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIForSaleOfSecuritiesNetOfTax
      - us-gaap_OtherComprehensiveIncomeUnrealizedHoldingGainLossOnSecuritiesArisingDuringPeriodNetOfTax
      - us-gaap_UnrealizedGainLossOnDerivatives
      - us-gaap_OtherComprehensiveIncomeLossReclassificationAdjustmentFromAOCIOnDerivativesNetOfTax
      - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodNetOfTax
      - us-gaap_OtherComprehensiveIncomeLossNetOfTax
      - us-gaap_ComprehensiveIncomeNetOfTax [totalLabel]

### http://www.nvidia.com/role/ConsolidatedStatementsOfIncome

- us-gaap_IncomeStatementAbstract
  - us-gaap_StatementTable
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_StatementLineItems
      - us-gaap_Revenues
      - us-gaap_CostOfRevenue
      - us-gaap_GrossProfit [totalLabel]
      - us-gaap_OperatingExpensesAbstract
      - us-gaap_OperatingIncomeLoss [totalLabel]
      - us-gaap_InvestmentIncomeInterest
      - us-gaap_InterestExpense
      - us-gaap_OtherNonoperatingIncomeExpense
      - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments [totalLabel]
      - us-gaap_IncomeTaxExpenseBenefit
      - us-gaap_NetIncomeLoss [totalLabel]
      - us-gaap_EarningsPerShareBasic
      - us-gaap_EarningsPerShareDiluted
      - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
      - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding
      - us-gaap_CommonStockDividendsPerShareCashPaid

### http://www.nvidia.com/role/IncomeTaxes

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_IncomeTaxDisclosureTextBlock

### http://www.nvidia.com/role/IncomeTaxesDetails

- nvda_NotesToFinancialStatementsAbstract
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
  - nvda_ChargeInLieuOfTaxesAttributableToEmployerStockOptionPlans
  - us-gaap_IncomeTaxExpenseBenefit
  - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestmentsAbstract
    - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic
    - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign
    - us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments
  - us-gaap_EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate
  - us-gaap_IncomeTaxExpenseBenefitContinuingOperationsIncomeTaxReconciliationAbstract
    - us-gaap_IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate
    - us-gaap_IncomeTaxReconciliationStateAndLocalIncomeTaxes
    - us-gaap_IncomeTaxReconciliationForeignIncomeTaxRateDifferential
    - us-gaap_IncomeTaxReconciliationTaxCreditsResearch
    - us-gaap_IncomeTaxReconciliationNondeductibleExpenseShareBasedCompensationCost
    - nvda_Taxexpenserelatedtointercompanytransaction
    - us-gaap_IncomeTaxReconciliationNondeductibleExpenseRestructuringCharges
    - us-gaap_IncomeTaxReconciliationOtherAdjustments
    - us-gaap_IncomeTaxExpenseBenefit
    - nvda_ExcessTaxBenefitRelatedToStockbasedcompensation
  - us-gaap_ComponentsOfDeferredTaxAssetsAndLiabilitiesAbstract
    - us-gaap_ComponentsOfDeferredTaxAssetsAbstract
      - us-gaap_DeferredTaxAssetsOperatingLossCarryforwards
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccruals
      - nvda_DeferredTaxAssetsPropertyEquipmentAndIntangibleAssets
      - us-gaap_DeferredTaxAssetsTaxCreditCarryforwards
      - us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
      - nvda_ConvertibledebtDTA
      - us-gaap_DeferredTaxAssetsGross [totalLabel]
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_DeferredTaxAssetsNet
    - us-gaap_ComponentsOfDeferredTaxLiabilitiesAbstract
      - nvda_DeferredTaxLiabilitiesIntangibleAssets
      - us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings
      - us-gaap_DeferredTaxLiabilities
    - us-gaap_DeferredTaxAssetsLiabilitiesNet
    - us-gaap_EffectiveIncomeTaxRateContinuingOperations
  - us-gaap_IncomeTaxExpenseBenefitContinuingOperationsAbstract
    - us-gaap_OperatingLossCarryforwardsTable
      - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_OperatingLossCarryforwardsLineItems

### http://www.nvidia.com/role/IncomeTaxesIncomeTaxesTables

- nvda_IncomeTaxesAbstract
  - us-gaap_ScheduleOfComponentsOfIncomeTaxExpenseBenefitTableTextBlock
  - us-gaap_ScheduleOfIncomeBeforeIncomeTaxDomesticAndForeignTableTextBlock
  - us-gaap_ScheduleOfEffectiveIncomeTaxRateReconciliationTableTextBlock
  - us-gaap_ScheduleOfDeferredTaxAssetsAndLiabilitiesTableTextBlock
  - us-gaap_SummaryOfIncomeTaxContingenciesTextBlock

### http://www.nvidia.com/role/IncomeTaxesUnrecognizedTaxBenefitsDetails

- nvda_IncomeTaxesAbstract
  - us-gaap_IncomeTaxContingencyTable
    - us-gaap_IncomeTaxAuthorityAxis
      - us-gaap_IncomeTaxAuthorityDomain
    - us-gaap_IncomeTaxContingencyLineItems
      - us-gaap_UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate
      - nvda_Unrecognizedtaxbenefitrelatedtostatetaxpositions
      - nvda_ReductionOfDeferredTaxAssetIncludedInUnrecognizedTaxBenefit
      - us-gaap_IncomeTaxReconciliationTaxContingenciesAbstract
      - us-gaap_UnrecognizedTaxBenefitsIncomeTaxPenaltiesAndInterestAccruedAbstract

### http://www.nvidia.com/role/IntangibleAssetsDetails

- nvda_AmortizationExpenseAssociatedWithIntangibleAssetsAbstract
  - us-gaap_AmortizationOfIntangibleAssets
- us-gaap_FiniteLivedIntangibleAssetsFutureAmortizationExpenseAbstract
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseNextTwelveMonths
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearTwo
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearThree
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFour
  - us-gaap_FiniteLivedIntangibleAssetsAmortizationExpenseYearFive

### http://www.nvidia.com/role/NetIncomePerShare

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_EarningsPerShareTextBlock

### http://www.nvidia.com/role/NetIncomePerShareDetails

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - us-gaap_DebtInstrumentLineItems
  - nvda_Numberofwarrantsterminated
  - us-gaap_ClassOfWarrantOrRightOutstanding
  - nvda_TotalnumberofsharesissuedrelatedtoterminatedWarrants [totalLabel]
  - us-gaap_ClassOfWarrantOrRightNumberOfSecuritiesCalledByEachWarrantOrRight
  - nvda_NumberofsharesissuedinQ118relatedtoterminatedwarrants
  - us-gaap_DebtInstrumentInterestRateStatedPercentage
  - us-gaap_DebtInstrumentConvertibleConversionPrice1
  - nvda_WarrantStrikePrice
  - nvda_Averagestockprice
  - nvda_NumeratorAbstract
    - us-gaap_NetIncomeLoss
  - nvda_DenominatorAbstract
    - us-gaap_WeightedAverageNumberOfSharesOutstandingBasic
    - nvda_EffectOfDilutiveSecuritiesAbstract
      - us-gaap_WeightedAverageNumberDilutedSharesOutstandingAdjustment
    - us-gaap_IncrementalCommonSharesAttributableToConversionOfDebtSecurities
    - us-gaap_IncrementalCommonSharesAttributableToCallOptionsAndWarrants
    - us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding
  - nvda_NetIncomeLossPerShareAbstract
    - us-gaap_EarningsPerShareBasic
    - us-gaap_EarningsPerShareDiluted
  - us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount

### http://www.nvidia.com/role/NetIncomePerShareTables

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_ScheduleOfWeightedAverageNumberOfSharesTableTextBlock

### http://www.nvidia.com/role/SegmentInformationRevenueAndAccountsReceivableByMajorCustomerDetails

- nvda_ScheduleOfRevenueByMajorCustomersAbstract
  - us-gaap_ScheduleOfEntityWideRevenueByMajorCustomersByReportingSegmentsTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_MajorCustomersAxis
      - us-gaap_NameOfMajorCustomerDomain
    - us-gaap_EntityWideRevenueMajorCustomerLineItems
      - nvda_RevenueFromSignificantCustomersInPercent

### http://www.nvidia.com/role/SegmentInformationRevenueAndLongLivedAssetsByRegionDetails

- nvda_RevenueandLonglivedbyRegionAbstract
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsTable
    - nvda_RevenueFromCustomersBasedInDifferentGeographicRegionsAxis
      - nvda_RevenueFromCustomersBasedInDifferentGeographicRegionsDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_RevenuesFromExternalCustomersAndLongLivedAssetsLineItems
      - us-gaap_Revenues
      - us-gaap_NoncurrentAssets

### http://www.nvidia.com/role/SegmentInformationScheduleOfRevenueByMarketDetails

- nvda_RevenuebyMarketAbstract
  - nvda_ScheduleofRevenuebyMarketsTable
    - nvda_MarketAxis
      - nvda_MarketDomain
    - nvda_ScheduleofRevenuebyMarketsLineItems
      - us-gaap_Revenues

### http://www.nvidia.com/role/StockBasedCompensationDetails

- nvda_SummaryofunearnedSBCexpenseAbstract
  - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized [totalLabel]
  - us-gaap_EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1 [totalLabel]
- nvda_AllocatedShareBasedCompensationExpenseNetOfAmountsCapitalizedAsInventoryRecognizedInStatementOfOperationsAbstract
  - us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable

## 资产负债表结构 (Balance Sheet Structure)

### http://www.nvidia.com/role/BalanceSheetComponents

- nvda_NotesToFinancialStatementsAbstract
  - nvda_BalanceSheetComponentsTextBlock

### http://www.nvidia.com/role/BalanceSheetComponentsDetails

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_InventoryNetAbstract
    - us-gaap_InventoryRawMaterials
    - us-gaap_InventoryWorkInProcess
    - us-gaap_InventoryFinishedGoods
    - us-gaap_InventoryNet [totalLabel]
  - us-gaap_ScheduleOfPropertyPlantAndEquipmentTable
    - us-gaap_PropertyPlantAndEquipmentByTypeAxis
      - us-gaap_PropertyPlantAndEquipmentTypeDomain
    - us-gaap_PropertyPlantAndEquipmentLineItems
      - us-gaap_PropertyPlantAndEquipmentGross
      - us-gaap_PropertyPlantAndEquipmentEstimatedUsefulLives
      - us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment
      - us-gaap_PropertyPlantAndEquipmentNet
  - nvda_OutstandingInventoryPurchaseObligation
  - us-gaap_Depreciation
  - nvda_AccumulatedamortizationofLHIandcapitallease
  - us-gaap_AccruedLiabilitiesCurrentAbstract
    - us-gaap_DeferredRevenueCurrent
    - nvda_AccruedCustomerProgramsCurrent
    - us-gaap_EmployeeRelatedLiabilitiesCurrent
    - us-gaap_RestructuringReserve
    - us-gaap_AccruedProfessionalFeesCurrentAndNoncurrent
    - us-gaap_ProductWarrantyAccrualClassifiedCurrent
    - us-gaap_AccruedRoyaltiesCurrent
    - us-gaap_CapitalLeaseObligationsCurrent
    - us-gaap_InterestPayableCurrent
    - nvda_AccruedTaxesPayable
    - nvda_Charitablecontributionpayable
    - us-gaap_OtherAccruedLiabilitiesCurrent
    - us-gaap_AccruedLiabilitiesCurrent [totalLabel]
  - us-gaap_OtherLiabilitiesNoncurrentAbstract
    - us-gaap_DeferredTaxLiabilitiesNoncurrent
    - us-gaap_AccruedIncomeTaxesNoncurrent
    - nvda_CharitableContributionPayableLongterm
    - us-gaap_DeferredRevenueNoncurrent
    - nvda_LiabilitesOtherNoncurrent
    - us-gaap_OtherLiabilitiesNoncurrent [totalLabel]

### http://www.nvidia.com/role/BalanceSheetComponentsTables

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_InventoryDisclosureTextBlock
  - us-gaap_PropertyPlantAndEquipmentTextBlock
  - us-gaap_AccountsPayableAndAccruedLiabilitiesDisclosureTextBlock
  - us-gaap_OtherLiabilitiesDisclosureTextBlock

### http://www.nvidia.com/role/ConsolidatedBalanceSheets

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
    - us-gaap_Goodwill
    - us-gaap_IntangibleAssetsNetExcludingGoodwill
    - us-gaap_OtherAssetsNoncurrent
    - us-gaap_Assets [totalLabel]
  - us-gaap_LiabilitiesAndStockholdersEquityAbstract
    - us-gaap_LiabilitiesCurrentAbstract
      - us-gaap_AccountsPayableCurrent
      - us-gaap_AccruedLiabilitiesCurrent
      - us-gaap_ConvertibleDebtCurrent
      - us-gaap_LiabilitiesCurrent [totalLabel]
    - us-gaap_LongTermDebt
    - us-gaap_OtherLiabilitiesNoncurrent
    - us-gaap_CapitalLeaseObligationsNoncurrent
    - us-gaap_Liabilities [totalLabel]
    - us-gaap_CommitmentsAndContingencies
    - us-gaap_TemporaryEquityValueExcludingAdditionalPaidInCapital
    - us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterestAbstract
      - us-gaap_PreferredStockValueOutstanding
      - us-gaap_CommonStockValue
      - us-gaap_AdditionalPaidInCapital
      - us-gaap_TreasuryStockValue
      - us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
      - us-gaap_RetainedEarningsAccumulatedDeficit
      - us-gaap_StockholdersEquity [totalLabel]
    - us-gaap_LiabilitiesAndStockholdersEquity [totalLabel]

### http://www.nvidia.com/role/ConsolidatedBalanceSheetsParentheticals

- nvda_ConsolidatedBalanceSheetsAbstract
  - us-gaap_StatementTable
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_StatementClassOfStockAxis
      - us-gaap_ClassOfStockDomain
    - us-gaap_StatementLineItems
      - us-gaap_AllowanceForDoubtfulAccountsReceivableCurrent
      - us-gaap_PreferredStockParOrStatedValuePerShare
      - us-gaap_PreferredStockSharesAuthorized
      - us-gaap_PreferredStockSharesIssued
      - us-gaap_CommonStockParOrStatedValuePerShare
      - us-gaap_CommonStockSharesAuthorized
      - us-gaap_CommonStockSharesIssued
      - us-gaap_CommonStockSharesOutstanding
      - us-gaap_TreasuryStockShares

### http://www.nvidia.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_StatementOfCashFlowsAbstract
  - us-gaap_StatementTable
  - us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract
    - us-gaap_NetIncomeLoss
    - nvda_AdjustmentsToReconcileNetIncomeLossToNetCashProvidedByOperatingActivities
    - us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
    - us-gaap_NetCashProvidedByUsedInOperatingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract
    - us-gaap_ProceedsFromSaleOfAvailableForSaleSecurities
    - us-gaap_ProceedsFromSaleAndMaturityOfMarketableSecurities
    - nvda_Proceedsfromsaleoflonglivedassetsandinvestments
    - us-gaap_PaymentsToAcquireMarketableSecurities
    - nvda_PurchasesOfPropertyAndEquipmentAndIntangibleAssets
    - nvda_Reimbursementofheadquartersbuildingdevelopmentcostsfromlessor
    - us-gaap_PaymentsForProceedsFromOtherInvestingActivities
    - us-gaap_NetCashProvidedByUsedInInvestingActivities [totalLabel]
  - us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract
    - us-gaap_ProceedsFromConvertibleDebt
    - us-gaap_PaymentsForRepurchaseOfCommonStock
    - us-gaap_RepaymentsOfConvertibleDebt
    - us-gaap_PaymentsOfDividends
    - nvda_Netproceedspaymentsrelatedtoemployeestockplans
    - us-gaap_PaymentsOfDebtIssuanceCosts
    - us-gaap_ExcessTaxBenefitFromShareBasedCompensationFinancingActivities
    - us-gaap_ProceedsFromPaymentsForOtherFinancingActivities
    - us-gaap_NetCashProvidedByUsedInFinancingActivities [totalLabel]
  - us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease [totalLabel]
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_CashAndCashEquivalentsAtCarryingValue
  - us-gaap_SupplementalCashFlowInformationAbstract
    - us-gaap_IncomeTaxesPaidNet
    - us-gaap_InterestPaidNet
  - us-gaap_OtherNoncashInvestingAndFinancingItemsAbstract
    - us-gaap_LiabilitiesAssumed1
    - nvda_Goodwilladjustmentrelatedtopreviouslyacquiredbusiness3dfx

### http://www.nvidia.com/role/ConsolidatedStatementsOfShareholdersEquity

- us-gaap_StatementOfStockholdersEquityAbstract
  - us-gaap_StatementTable
- us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
  - us-gaap_CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption
  - us-gaap_OtherComprehensiveIncomeLossNetOfTax
  - us-gaap_NetIncomeLoss
  - us-gaap_ClassOfWarrantOrRightNumberOfSecuritiesCalledByEachWarrantOrRight
  - nvda_Issuanceofcommonstockinexchangeforwarrants
  - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockOwnershipPlan
  - us-gaap_StockIssuedDuringPeriodValueEmployeeStockOwnershipPlan
  - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalConvertibleDebtWithConversionFeature
  - us-gaap_SharesPaidForTaxWithholdingForShareBasedCompensation
  - us-gaap_AdjustmentsRelatedToTaxWithholdingForShareBasedCompensation
  - us-gaap_DeferredTaxExpenseFromStockOptionsExercised
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodShares
  - us-gaap_StockRepurchasedAndRetiredDuringPeriodValue
  - nvda_SharesreceivedfromNoteHedges
  - nvda_Exerciseofconvertiblenotehedges
  - us-gaap_DividendsCommonStockCash
  - us-gaap_AllocatedShareBasedCompensationExpense
  - us-gaap_AdjustmentsToAdditionalPaidInCapitalEquityComponentOfConvertibleDebtSubsequentAdjustments
  - us-gaap_CommonStockSharesOutstanding
  - us-gaap_StockholdersEquity
- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_CommonStockMember
    - us-gaap_AdditionalPaidInCapitalMember
    - us-gaap_TreasuryStockMember
    - us-gaap_AccumulatedOtherComprehensiveIncomeMember
    - us-gaap_RetainedEarningsMember

### http://www.nvidia.com/role/FairValueOfFinancialAssetsAndLiabilities

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_FairValueDisclosuresTextBlock

### http://www.nvidia.com/role/FairValueOfFinancialAssetsAndLiabilitiesDetails

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisTable
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_FairValueByFairValueHierarchyLevelAxis
      - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
    - us-gaap_FairValueByAssetClassAxis
      - us-gaap_FairValueAssetsMeasuredOnRecurringBasisUnobservableInputReconciliationByAssetClassDomain
    - us-gaap_FairValueAssetsAndLiabilitiesMeasuredOnRecurringAndNonrecurringBasisLineItems
      - us-gaap_AssetsFairValueDisclosureRecurring
      - us-gaap_ConvertibleDebtFairValueDisclosures
      - us-gaap_LongTermDebtFairValue
      - us-gaap_InterestRateDerivativeLiabilitiesAtFairValue
      - us-gaap_CashAndCashEquivalentsFairValueDisclosure
      - us-gaap_MarketableSecurities
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - us-gaap_LongTermDebtPercentageBearingFixedInterestRate

### http://www.nvidia.com/role/IntangibleAssets

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_IntangibleAssetsDisclosureTextBlock

### http://www.nvidia.com/role/IntangibleAssetsDetails

- nvda_NotesToFinancialStatementsAbstract
  - nvda_AmortizableIntangibleAssetsComponentsAbstract
    - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTable
      - us-gaap_FiniteLivedIntangibleAssetsByMajorClassAxis
      - nvda_AmortizableIntangibleAssetsComponentsLineItems

### http://www.nvidia.com/role/IntangibleAssetsTables

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_ScheduleOfFiniteLivedIntangibleAssetsTableTextBlock

### http://www.nvidia.com/role/MarketableSecuritiesDetails

- nvda_SummaryOfCashEquivalentsAndMarketableSecuritiesLineItems
  - nvda_ClassifiedAsAbstract
  - us-gaap_AvailableForSaleSecuritiesAmortizedCostBasisAbstract
  - us-gaap_FairValueDisclosuresAbstract
  - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionAbstract
- us-gaap_FairValueByAssetClassAxis
  - us-gaap_FairValueAssetsMeasuredOnRecurringBasisUnobservableInputReconciliationByAssetClassDomain
    - us-gaap_CorporateDebtSecuritiesMember
    - us-gaap_USGovernmentAgenciesDebtSecuritiesMember
    - us-gaap_USTreasurySecuritiesMember
    - us-gaap_AssetBackedSecuritiesMember
    - us-gaap_MortgageBackedSecuritiesIssuedByUSGovernmentSponsoredEnterprisesMember
    - us-gaap_MoneyMarketFundsMember
    - us-gaap_ForeignGovernmentDebtMember
- nvda_SummaryOfCashEquivalentsAndMarketableSecuritiesAbstract
  - us-gaap_ScheduleOfAvailableForSaleSecuritiesTable

### http://www.nvidia.com/role/StockBasedCompensationDetails

- nvda_SummaryofequityawardsgrantedAbstract
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
  - nvda_ShareBasedCompensationArrangementByShareBasedPaymentAwardRsuGrantsInPeriodGrantDateTotalFairValue [totalLabel]
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_StockIssuedDuringPeriodSharesEmployeeStockPurchasePlans
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardPerShareWeightedAveragePriceOfSharesPurchased
  - nvda_WeightedaveragegrantdatefairvalueofESPP

### http://www.nvidia.com/role/StockBasedCompensationEquityIncentivePlansDetails

- nvda_EquityIncentivePlanAbstract
  - nvda_A2007EquityIncentivePlanAbstract
    - nvda_NumberOfSharesMayBeIssuedUnderRestated2007Plan
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant
    - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardAwardVestingRightsPercentage
    - nvda_Quarterlyvestingscheduleoptions
    - nvda_SemiannualvestingscheduleRSUsforgrantsmadepriorto51816
    - nvda_QuarterlyvestingscheduleRSUsforgrantsmadeonorafter51816
    - nvda_SemiannualvestingschedulePSUs
    - nvda_MaximumissuablesharesofMarketBasedPSUspercentage
  - us-gaap_EmployeeStockOwnershipPlanESOPSharesInESOPAbstract
  - nvda_EquityAwardTransactionsAbstract
    - nvda_StockOptionsAbstract
    - nvda_RestrictedStockUnitsAbstract
    - nvda_MinimumnumberofmarketbasedPSUsissuable
    - nvda_MaximumnumberofmarketbasedPSUsissuable
    - us-gaap_SharePrice
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue [totalLabel]
    - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsVestedInPeriodFairValue1

### http://www.nvidia.com/role/SummaryOfSignificantAccountingPoliciesDetails

- us-gaap_StatementEquityComponentsAxis
  - us-gaap_EquityComponentDomain
    - us-gaap_RetainedEarningsMember
- us-gaap_FairValueByAssetClassAxis
  - us-gaap_FairValueAssetsMeasuredOnRecurringBasisUnobservableInputReconciliationByAssetClassDomain
    - us-gaap_MoneyMarketFundsMember

## 现金流量表结构 (Cash Flow Structure)

### http://www.nvidia.com/role/CommitmentsAndContingenciesDetails

- us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract
  - nvda_FutureminimumoperatingleasepaymentsHQ
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueCurrent
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInTwoYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInThreeYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFourYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueInFiveYears
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueThereafter
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDue
  - us-gaap_LeaseAndRentalExpense

### http://www.nvidia.com/role/ConsolidatedStatementsOfCashFlows

- us-gaap_StatementTable
  - us-gaap_StatementScenarioAxis
    - us-gaap_ScenarioUnspecifiedDomain
  - us-gaap_StatementLineItems
- us-gaap_IncreaseDecreaseInOperatingCapitalAbstract
  - us-gaap_IncreaseDecreaseInAccountsReceivable
  - us-gaap_IncreaseDecreaseInInventories
  - us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets
  - us-gaap_IncreaseDecreaseInAccountsPayable
  - us-gaap_IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities
  - us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities

### http://www.nvidia.com/role/FairValueOfCashEquivalentsAndMarketableSecuritiesTables

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_ScheduleOfFairValueAssetsAndLiabilitiesMeasuredOnRecurringBasisTableTextBlock

### http://www.nvidia.com/role/SegmentInformationDetails

- nvda_FinancialInformationByOperatingSegmentAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable

## 股东权益结构 (Equity Structure)

### http://www.nvidia.com/role/ConsolidatedStatementsOfShareholdersEquity

- us-gaap_StatementTable
  - us-gaap_StatementEquityComponentsAxis
  - us-gaap_StatementLineItems
    - us-gaap_IncreaseDecreaseInStockholdersEquityRollForward
    - us-gaap_CommonStockDividendsPerShareCashPaid

### http://www.nvidia.com/role/StockBasedCompensation

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_DisclosureOfCompensationRelatedCostsShareBasedPaymentsTextBlock

### http://www.nvidia.com/role/StockBasedCompensationDetails

- us-gaap_ScheduleOfShareBasedCompensationArrangementsByShareBasedPaymentAwardTable
  - us-gaap_AwardTypeAxis
    - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardAwardTypeAndPlanNameDomain
      - us-gaap_EmployeeStockOptionMember
      - nvda_RSUsPSUsandMarketbasedPSUsMember
      - nvda_ShareBasedCompensationArrangementsByShareBasedPaymentAwardEmployeeStockPurchasePlanMember
  - nvda_FairValueOfStockOptionsGrantedUnderStockOptionPlansAndSharesIssuedUnderEmployeeStockPurchasePlanLineItems
    - nvda_AllocatedShareBasedCompensationExpenseNetOfAmountsCapitalizedAsInventoryRecognizedInCostOfRevenue
    - nvda_AllocatedShareBasedCompensationExpenseNetOfAmountsCapitalizedAsInventoryRecognizedInStatementOfOperations
    - nvda_AllocatedShareBasedCompensationExpenseNetOfAmountsCapitalizedAsInventoryRecognizedInSalesGeneralAndAdministrativeExpenses
    - us-gaap_ShareBasedCompensation
    - nvda_SummaryofequityawardsgrantedAbstract
    - nvda_ShareBasedCompensationExpenseRelatedToEquityAwardsNotExpectedToVest
    - nvda_SummaryofunearnedSBCexpenseAbstract
    - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsAndMethodologyAbstract
      - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardFairValueAssumptionsExpectedTerm1
      - nvda_Expectedlifemaximum
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsRiskFreeInterestRateMinimum
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsRiskFreeInterestRateMaximum
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsExpectedVolatilityRateMinimum
      - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardFairValueAssumptionsExpectedVolatilityRateMaximum
      - nvda_DividendYieldMinimum
      - nvda_DividendYieldMaximum
- nvda_NotesToFinancialStatementsAbstract
  - nvda_AllocatedShareBasedCompensationExpenseNetOfAmountsCapitalizedAsInventoryRecognizedInStatementOfOperationsAbstract

### http://www.nvidia.com/role/StockBasedCompensationEquityIncentivePlansDetails

- nvda_RestrictedStockUnitsAbstract
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardNonOptionEquityInstrumentsOutstandingNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriod
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeitedInPeriod
  - nvda_WeightedAverageGrantDateFairValueRSUsPSUsandMarketBasedPSUsOutstanding
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodWeightedAverageGrantDateFairValue
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsForfeituresWeightedAverageGrantDateFairValue
  - nvda_VestedandexpectedtovestRSUsPSUsandMarketbasedPSUs
  - nvda_WeightedAverageGrantDateFairValueRSUsandPSUsVestedandexpectedtovest
- nvda_StockOptionsAbstract
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingNumber
  - us-gaap_StockIssuedDuringPeriodSharesStockOptionsExercised
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingWeightedAverageExercisePrice
  - us-gaap_ShareBasedCompensationArrangementsByShareBasedPaymentAwardOptionsExercisesInPeriodWeightedAverageExercisePrice
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisableNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisableWeightedAverageExercisePrice
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestOutstandingNumber
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestOutstandingWeightedAverageExercisePrice
  - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsOutstandingWeightedAverageRemainingContractualTerm2
  - us-gaap_SharebasedCompensationSharesAuthorizedUnderStockOptionPlansExercisePriceRangeExercisableOptionsWeightedAverageRemainingContractualTerm2
  - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsVestedAndExpectedToVestOutstandingWeightedAverageRemainingContractualTerm1
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsOutstandingIntrinsicValue
  - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardOptionsExercisableIntrinsicValue1
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsVestedAndExpectedToVestOutstandingAggregateIntrinsicValue
- us-gaap_EmployeeStockOwnershipPlanESOPSharesInESOPAbstract
  - nvda_MaximumAggregatedNumberOfSharesUnder2012Espp
  - nvda_Totalsharespurchasedunder2012ESPPPlan [totalLabel]
  - nvda_Sharesreservedforfutureissuanceunder2012Plan
  - us-gaap_ShareBasedCompensationArrangementByShareBasedPaymentAwardMaximumEmployeeSubscriptionRate
  - nvda_ShareBasedCompensationArrangementByShareBasedPaymentAwardMaximumEmployeeSubscriptionRateBoardOfDirectorApproved
  - us-gaap_SharebasedCompensationArrangementBySharebasedPaymentAwardPurchasePriceOfCommonStockPercent
- nvda_NotesToFinancialStatementsAbstract
  - nvda_EquityIncentivePlanAbstract

### http://www.nvidia.com/role/StockBasedCompensationTables

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_ScheduleOfEmployeeServiceShareBasedCompensationAllocationOfRecognizedPeriodCostsTextBlock
  - nvda_SummaryofequityawardsgrantedunderequityincentiveplansTableTextBlock
  - nvda_SummaryofunearnedstockbasedcompensationexpenseTableTextBlock
  - us-gaap_ScheduleOfShareBasedPaymentAwardStockOptionsValuationAssumptionsTableTextBlock
  - us-gaap_ScheduleOfShareBasedCompensationActivityTableTextBlock

### http://www.nvidia.com/role/StockholdersEquity

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_StockholdersEquityNoteDisclosureTextBlock

### http://www.nvidia.com/role/StockholdersEquityDetails

- nvda_NotesToFinancialStatementsAbstract
  - nvda_Stockrepurchaseprogramadditionalauthorizedamount
  - us-gaap_StockRepurchasedDuringPeriodShares
  - us-gaap_PaymentsForRepurchaseOfCommonStock
  - us-gaap_PaymentsOfDividends
  - us-gaap_CommonStockDividendsPerShareCashPaid
  - nvda_AggregateNumberOfSharesRepurchasedUnderStockRepurchaseProgram
  - nvda_Aggregatedcostofsharesrepurchased
  - us-gaap_StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1
  - us-gaap_CommonStockSharesAuthorized
  - us-gaap_CommonStockParOrStatedValuePerShare

## 其他结构 (Other Structure)

### http://www.nvidia.com/role/CommitmentsAndContingencies

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_CommitmentsAndContingenciesDisclosureTextBlock

### http://www.nvidia.com/role/CommitmentsAndContingenciesDetails

- nvda_NotesToFinancialStatementsAbstract
  - nvda_CommitmentandContingencyTable
    - us-gaap_MajorPropertyClassAxis
      - us-gaap_MajorPropertyClassDomain
    - nvda_CommitmentandContingencyLineItems
      - nvda_GroundleasetoasyndicateofbanksSyntheticLease
      - nvda_TotalSyntheticLeaseterm [totalLabel]
      - nvda_EstimatedconstructionperiodSyntheticLease
      - nvda_Maximumnumberofrenewaloptions
      - us-gaap_LesseeLeasingArrangementsOperatingLeasesRenewalTerm
      - nvda_ExpectedconstructioncostsforSyntheticleasefinancing
      - nvda_Maximumresidualvalueguaranteepercentage
      - nvda_Maximumtotalleverageratio [totalLabel]
  - us-gaap_CommitmentsAndContingenciesDisclosureAbstract
    - nvda_OutstandingInventoryPurchaseObligation
    - nvda_OutstandingCapitalPurchaseObligations
    - nvda_LegalsettlementrecordedasCOGS
  - us-gaap_OperatingLeasesFutureMinimumPaymentsDueAbstract
  - us-gaap_CapitalLeasesFutureMinimumPaymentsDueAbstract
    - nvda_FutureminimumcapitalleasepaymentsHQ
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueCurrent
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDueInTwoYears
    - us-gaap_CapitalLeasesFutureMinimumPaymentsDue
    - us-gaap_CapitalLeasesFutureMinimumPaymentsPresentValueOfNetMinimumPayments
    - us-gaap_CapitalLeaseObligationsCurrent
    - us-gaap_CapitalLeaseObligationsNoncurrent

### http://www.nvidia.com/role/CommitmentsAndContingenciesTables

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_ScheduleOfFutureMinimumRentalPaymentsForOperatingLeasesTableTextBlock
  - us-gaap_ScheduleOfFutureMinimumLeasePaymentsForCapitalLeasesTableTextBlock

### http://www.nvidia.com/role/Debt

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtDisclosureTextBlock

### http://www.nvidia.com/role/DebtDetails

- us-gaap_DebtDisclosureAbstract
  - us-gaap_DebtInstrumentTable
    - us-gaap_SubsequentEventTypeAxis
      - us-gaap_SubsequentEventTypeDomain
    - us-gaap_LongtermDebtTypeAxis
      - us-gaap_LongtermDebtTypeDomain
    - us-gaap_DebtInstrumentAxis
      - us-gaap_DebtInstrumentNameDomain
    - us-gaap_DebtInstrumentLineItems
      - nvda_ConvertibleNotesInitialfacevalue
      - us-gaap_DebtInstrumentInterestRateStatedPercentage
      - nvda_PrincipalamountofNotes
      - us-gaap_DebtInstrumentConvertibleConversionRatio1
      - us-gaap_DebtInstrumentConvertibleConversionPrice1
      - us-gaap_DebtInstrumentConvertibleTermsOfConversionFeature
      - us-gaap_ExtinguishmentOfDebtAmount
      - us-gaap_SharePrice
      - us-gaap_DebtInstrumentConvertibleIfConvertedValueInExcessOfPrincipal
      - us-gaap_DebtConversionConvertedInstrumentSharesIssued1
      - nvda_SubsequentrepaymentofConvertibledebt
      - us-gaap_GainsLossesOnExtinguishmentOfDebt
      - nvda_DebtInstrumentConvertibleInitialLiabilityAmount
      - us-gaap_DebtInstrumentConvertibleCarryingAmountOfTheEquityComponent
      - nvda_PurchasersDiscountofConvertibleNotes
      - nvda_Initialunamortizeddebtdiscountatissuance
      - us-gaap_DebtInstrumentInterestRateEffectivePercentage
      - us-gaap_TemporaryEquityValueExcludingAdditionalPaidInCapital
      - us-gaap_ConvertibleDebtCurrent
      - us-gaap_DebtInstrumentFaceAmount
      - us-gaap_DebtInstrumentUnamortizedDiscount
      - us-gaap_ConvertibleDebt
      - us-gaap_DebtInstrumentConvertibleRemainingDiscountAmortizationPeriod1
      - us-gaap_InterestExpenseDebtExcludingAmortization
      - us-gaap_AmortizationOfFinancingCostsAndDiscounts
      - us-gaap_InterestExpenseDebt [totalLabel]
      - nvda_NoteHedgesStrikePrice
      - nvda_SharesreceivedfromNoteHedges
      - nvda_WarrantStrikePrice
      - nvda_Numberofwarrantsterminated
      - us-gaap_ClassOfWarrantOrRightOutstanding
      - nvda_TotalnumberofsharesissuedrelatedtoterminatedWarrants [totalLabel]
      - us-gaap_ClassOfWarrantOrRightNumberOfSecuritiesCalledByEachWarrantOrRight
      - nvda_NumberofsharesissuedinQ118relatedtoterminatedwarrants
      - us-gaap_LongTermDebtPercentageBearingFixedInterestRate
      - us-gaap_ProceedsFromIssuanceOfLongTermDebt
      - us-gaap_DebtInstrumentTerm
      - us-gaap_DebtInstrumentInterestRateDuringPeriod
      - us-gaap_DebtInstrumentCarryingAmount
      - us-gaap_DebtInstrumentUnamortizedDiscountPremiumAndDebtIssuanceCostsNet
      - us-gaap_LongTermDebt
      - us-gaap_LineOfCreditFacilityCurrentBorrowingCapacity
      - nvda_AdditionalborrowingcapacityfromRevolvingCreditFacility

### http://www.nvidia.com/role/DebtTable

- us-gaap_DebtDisclosureAbstract
  - us-gaap_ConvertibleDebtTableTextBlock
  - us-gaap_LongTermDebtTextBlock

### http://www.nvidia.com/role/DerivativeFinancialInstrumentDetails

- us-gaap_SummaryOfDerivativeInstrumentsAbstract
  - invest_DerivativeNotionalAmount
  - nvda_NotionalamountofFXforwardcontractdesignatedashedge
  - nvda_NotionalamountofFXforwardcontractnondesignatedashedge
  - us-gaap_OtherComprehensiveIncomeUnrealizedGainLossOnDerivativesArisingDuringPeriodNetOfTax

### http://www.nvidia.com/role/DerivativeFinancialInstrumentNotes

- us-gaap_SummaryOfDerivativeInstrumentsAbstract
  - us-gaap_DerivativeInstrumentsAndHedgingActivitiesDisclosureTextBlock

### http://www.nvidia.com/role/DocumentAndEntityInformationDocument

- nvda_DocumentAndEntityInformationAbstract
  - dei_DocumentInformationTable
    - dei_DocumentInformationDocumentAxis
      - dei_DocumentDomain
    - dei_DocumentInformationLineItems
      - dei_EntityRegistrantName
      - dei_EntityCentralIndexKey
      - dei_CurrentFiscalYearEndDate
      - dei_EntityFilerCategory
      - dei_DocumentType
      - dei_DocumentPeriodEndDate
      - dei_DocumentFiscalYearFocus
      - dei_DocumentFiscalPeriodFocus
      - dei_AmendmentFlag
      - dei_EntityCommonStockSharesOutstanding
      - dei_EntityWellKnownSeasonedIssuer
      - dei_EntityVoluntaryFilers
      - dei_EntityCurrentReportingStatus
      - dei_EntityPublicFloat

### http://www.nvidia.com/role/EmployeeRetirementPlans

- nvda_EmployeeRetirementPlansAbstract
  - us-gaap_PensionAndOtherPostretirementBenefitsDisclosureTextBlock

### http://www.nvidia.com/role/EmployeeRetirementPlansDetails

- nvda_EmployeeRetirementPlansAbstract
  - nvda_EmployeeRetirementPlansMaximumContributionPercentageOfEarnings
  - nvda_A401KPlanemployercontributionexpense
  - us-gaap_DefinedContributionPlanCostRecognized

### http://www.nvidia.com/role/Goodwill

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_GoodwillDisclosureTextBlock

### http://www.nvidia.com/role/GoodwillDetails

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_ScheduleOfGoodwillTable
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - us-gaap_GoodwillLineItems
      - us-gaap_Goodwill

### http://www.nvidia.com/role/GoodwillTables

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_ScheduleOfGoodwillTextBlock

### http://www.nvidia.com/role/Guarantees

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_GuaranteesTextBlock

### http://www.nvidia.com/role/GuaranteesDetails

- nvda_NotesToFinancialStatementsAbstract
  - nvda_SHIELDwarrantycharge
  - nvda_EstimatedProductWarrantyLiabilitiesAbstract
    - us-gaap_ProductWarrantyAccrualClassifiedCurrent
    - us-gaap_ProductWarrantyAccrualWarrantiesIssued
    - us-gaap_ProductWarrantyAccrualPayments
    - us-gaap_ProductWarrantyAccrualClassifiedCurrent

### http://www.nvidia.com/role/GuaranteesTables

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_ProductWarrantyDisclosureTextBlock

### http://www.nvidia.com/role/MarketableSecurities

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_MarketableSecuritiesTextBlock

### http://www.nvidia.com/role/MarketableSecuritiesDetails

- us-gaap_AvailableForSaleSecuritiesAmortizedCostBasisAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearAmortizedCost
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsAmortizedCost
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithoutSingleMaturityDateAmortizedCost
  - us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis [totalLabel]
- nvda_NotesToFinancialStatementsAbstract
  - nvda_SummaryOfCashEquivalentsAndMarketableSecuritiesAbstract
- us-gaap_FairValueDisclosuresAbstract
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithoutSingleMaturityDateFairValue
  - us-gaap_AvailableForSaleSecuritiesDebtSecurities [totalLabel]
- us-gaap_ScheduleOfAvailableForSaleSecuritiesTable
  - us-gaap_FairValueByFairValueHierarchyLevelAxis
    - us-gaap_FairValueMeasurementsFairValueHierarchyDomain
  - us-gaap_FairValueByAssetClassAxis
  - nvda_SummaryOfCashEquivalentsAndMarketableSecuritiesLineItems
- nvda_ClassifiedAsAbstract
  - us-gaap_CashEquivalentsAtCarryingValue
  - us-gaap_MarketableSecuritiesCurrent
  - us-gaap_AvailableForSaleSecurities [totalLabel]
  - us-gaap_AvailableForSaleSecuritiesAmortizedCost
  - us-gaap_AvailableForSaleSecuritiesAccumulatedGrossUnrealizedGainBeforeTax
  - us-gaap_AvailableForSaleDebtSecuritiesAccumulatedGrossUnrealizedLossBeforeTax
- us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionAbstract
  - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionFairValueAbstract
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionLessThanTwelveMonthsFairValue
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionTwelveMonthsOrLongerFairValue
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionFairValue
  - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionAccumulatedLossAbstract
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionLessThan12MonthsAccumulatedLoss
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPosition12MonthsOrLongerAccumulatedLoss
    - us-gaap_AvailableForSaleSecuritiesContinuousUnrealizedLossPositionAccumulatedLoss

### http://www.nvidia.com/role/MarketableSecuritiesTables

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_AvailableForSaleSecuritiesTextBlock
  - us-gaap_InvestmentsClassifiedByContractualMaturityDateTableTextBlock

### http://www.nvidia.com/role/QuartelySummary

- us-gaap_QuarterlyFinancialDataAbstract
  - us-gaap_QuarterlyFinancialInformationTextBlock

### http://www.nvidia.com/role/QuartelySummaryDetails

- us-gaap_QuarterlyFinancialDataAbstract
  - us-gaap_NewAccountingPronouncementEarlyAdoptionTable
    - us-gaap_StatementScenarioAxis
      - us-gaap_ScenarioUnspecifiedDomain
    - us-gaap_NewAccountingPronouncementEarlyAdoptionLineItems
      - us-gaap_SelectedQuarterlyFinancialInformationAbstract

### http://www.nvidia.com/role/QuartelySummaryTables

- us-gaap_QuarterlyFinancialDataAbstract
  - us-gaap_ScheduleOfQuarterlyFinancialInformationTableTextBlock

### http://www.nvidia.com/role/RestructuringAndOtherChargesDetails

- nvda_RestructuringandOtherChargesAbstract
  - us-gaap_RestructuringCharges [totalLabel]
  - us-gaap_SeveranceCosts1
  - nvda_TaxreservereleaserelatedtoIcera
  - nvda_Facilitiesandrelatedcostsrestructuringcharge
  - nvda_Otherexitcosts
  - us-gaap_RestructuringReserve
  - us-gaap_PaymentsForRestructuring
  - us-gaap_RestructuringReserveSettledWithoutCash2
  - us-gaap_RestructuringReserve

### http://www.nvidia.com/role/RestructuringAndOtherChargesNotes

- nvda_RestructuringandOtherChargesAbstract
  - us-gaap_RestructuringAndRelatedActivitiesDisclosureTextBlock

### http://www.nvidia.com/role/RestructuringAndOtherChargesTables

- nvda_RestructuringandOtherChargesAbstract
  - us-gaap_ScheduleOfRestructuringAndRelatedCostsTextBlock
  - us-gaap_ScheduleOfRestructuringReserveByTypeOfCostTextBlock

### http://www.nvidia.com/role/ScheduleIi

- us-gaap_ValuationAndQualifyingAccountsAbstract
  - us-gaap_ValuationAndQualifyingAccountsDisclosureTable
    - us-gaap_ValuationAllowancesAndReservesTypeAxis
      - us-gaap_ValuationAllowancesAndReservesDomain
    - us-gaap_ValuationAndQualifyingAccountsDisclosureLineItems
      - us-gaap_ScheduleOfValuationAndQualifyingAccountsDisclosureTextBlock

### http://www.nvidia.com/role/ScheduleIiDetails

- us-gaap_ValuationAndQualifyingAccountsAbstract
  - us-gaap_ValuationAndQualifyingAccountsDisclosureTable
    - us-gaap_ValuationAllowancesAndReservesTypeAxis
      - us-gaap_ValuationAllowancesAndReservesDomain
    - us-gaap_ValuationAndQualifyingAccountsDisclosureLineItems
      - us-gaap_ValuationAllowancesAndReservesBalance
      - us-gaap_ValuationAllowancesAndReservesChargedToCostAndExpense
      - us-gaap_ValuationAllowancesAndReservesDeductions
      - us-gaap_ValuationAllowancesAndReservesBalance

### http://www.nvidia.com/role/SegmentInformation

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_SegmentReportingDisclosureTextBlock

### http://www.nvidia.com/role/SegmentInformationDetails

- us-gaap_ScheduleOfSegmentReportingInformationBySegmentTable
  - us-gaap_StatementBusinessSegmentsAxis
    - us-gaap_SegmentDomain
      - nvda_GpuMember
      - nvda_TegraProcessorMember
      - nvda_AllOtherMember
  - us-gaap_SegmentReportingInformationLineItems
    - us-gaap_DepreciationAndAmortization
    - us-gaap_Revenues
    - us-gaap_OperatingIncomeLoss
    - us-gaap_ReconciliationFromSegmentTotalsToConsolidatedAbstract [totalLabel]
      - nvda_UnallocatedCorporateExpensesAndOtherExpenses
      - us-gaap_ShareBasedCompensation
      - us-gaap_RestructuringCharges
      - nvda_OtherAcquisitionRelatedCosts
      - us-gaap_PaymentsForLegalSettlements
      - nvda_Contributionexpense
      - nvda_Productwarrantychargerelatedtorecall
      - nvda_ReconciliationTotalInAllOther [totalLabel]
- nvda_NotesToFinancialStatementsAbstract
  - nvda_FinancialInformationByOperatingSegmentAbstract

### http://www.nvidia.com/role/SegmentInformationScheduleOfAccountsReceivableByMajorCustomersDetails

- nvda_AccountsReceivableByMajorCustomersAbstract
  - nvda_ScheduleOfAccountsRecevableByMajorCustomersBySegmentTableTable
    - us-gaap_MajorCustomersAxis
      - us-gaap_NameOfMajorCustomerDomain
    - us-gaap_StatementBusinessSegmentsAxis
      - us-gaap_SegmentDomain
    - nvda_ScheduleOfAccountsRecevableByMajorCustomersBySegmentTableLineItems
      - nvda_AccountsReceivableFromSignificantCustomersInPercent

### http://www.nvidia.com/role/SegmentInformationTables

- nvda_NotesToFinancialStatementsAbstract
  - us-gaap_ScheduleOfSegmentReportingInformationBySegmentTextBlock
  - us-gaap_ScheduleOfRevenuesFromExternalCustomersAndLongLivedAssetsByGeographicalAreasTableTextBlock
  - nvda_ScheduleofRevenuebyMarketsTableTextBlock
  - us-gaap_LongLivedAssetsByGeographicAreasTableTextBlock
  - us-gaap_ScheduleOfRevenueByMajorCustomersByReportingSegmentsTableTextBlock
  - nvda_ScheduleofaccountsreceivablepercentagesfromsignificantcustomerstextblockTableTextBlock

### http://www.nvidia.com/role/SummaryOfSignificantAccountingPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_SignificantAccountingPoliciesTextBlock

### http://www.nvidia.com/role/SummaryOfSignificantAccountingPoliciesDetails

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_ScheduleOfAvailableForSaleSecuritiesTable
    - us-gaap_FairValueByAssetClassAxis
    - us-gaap_ScheduleOfAvailableForSaleSecuritiesLineItems
      - us-gaap_AdvertisingExpense
      - us-gaap_ForeignCurrencyTransactionGainLossRealized
      - us-gaap_DeferredTaxAssetsValuationAllowance
      - us-gaap_CashAndCashEquivalentsAtCarryingValue
      - us-gaap_AvailableForSaleSecuritiesAmortizedCost
      - nvda_AccountsReceivableFromSignificantCustomersInPercent
      - nvda_NumberOfCustomersExceeded10PercentOfTotalConsolidatedAccountsReceivable [totalLabel]
  - us-gaap_NewAccountingPronouncementEarlyAdoptionTable
    - us-gaap_NewAccountingPronouncementEarlyAdoptionAxis
      - us-gaap_NewAccountingPrinciplesEarlyAdoptionMember
    - us-gaap_AdjustmentsForNewAccountingPronouncementsAxis
      - us-gaap_TypeOfAdoptionMember
    - us-gaap_StatementEquityComponentsAxis
    - us-gaap_NewAccountingPronouncementEarlyAdoptionLineItems
      - us-gaap_CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption
      - nvda_ExcessTaxBenefitRelatedToStockbasedcompensation
      - nvda_Fullvaluationallowancerelatedtostatenetoperatinglossandstateresearchcreditcarryforwards

### http://www.nvidia.com/role/SummaryOfSignificantAccountingPoliciesPolicies

- us-gaap_AccountingPoliciesAbstract
  - us-gaap_NatureOfOperations
  - us-gaap_FiscalPeriod
  - us-gaap_PriorPeriodReclassificationAdjustmentDescription
  - us-gaap_ConsolidationPolicyTextBlock
  - us-gaap_UseOfEstimates
  - us-gaap_RevenueRecognitionPolicyTextBlock
  - us-gaap_CostsAssociatedWithExitOrDisposalActivitiesOrRestructuringsPolicyTextBlock
  - us-gaap_AdvertisingCostsPolicyTextBlock
  - us-gaap_LeasePolicyTextBlock
  - us-gaap_CommitmentsAndContingenciesPolicyTextBlock
  - us-gaap_CompensationRelatedCostsPolicyTextBlock
  - us-gaap_LegalCostsPolicyTextBlock
  - us-gaap_ForeignCurrencyTransactionsAndTranslationsPolicyTextBlock
  - us-gaap_IncomeTaxPolicyTextBlock
  - us-gaap_ComprehensiveIncomePolicyPolicyTextBlock
  - us-gaap_EarningsPerSharePolicyTextBlock
  - us-gaap_CashAndCashEquivalentsPolicyTextBlock
  - us-gaap_MarketableSecuritiesPolicy
  - us-gaap_InvestmentPolicyTextBlock
  - us-gaap_ConcentrationRiskCreditRisk
  - us-gaap_ReceivablesPolicyTextBlock
  - us-gaap_InventoryPolicyTextBlock
  - us-gaap_PropertyPlantAndEquipmentPolicyTextBlock
  - us-gaap_GoodwillAndIntangibleAssetsPolicyTextBlock
  - us-gaap_ImpairmentOrDisposalOfLongLivedAssetsPolicyTextBlock
  - us-gaap_NewAccountingPronouncementsPolicyPolicyTextBlock

