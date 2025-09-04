# NVDA 2017 财务计算逻辑分析

## 资产负债表计算逻辑 (Balance Sheet Calculations)

### BalanceSheetComponentsDetails

#### us-gaap_InventoryNet

- us-gaap_InventoryNet + us-gaap_InventoryRawMaterials
- us-gaap_InventoryNet + us-gaap_InventoryWorkInProcess
- us-gaap_InventoryNet + us-gaap_InventoryFinishedGoods

#### us-gaap_OtherLiabilitiesNoncurrent

- us-gaap_OtherLiabilitiesNoncurrent + us-gaap_DeferredTaxLiabilitiesNoncurrent
- us-gaap_OtherLiabilitiesNoncurrent + us-gaap_AccruedIncomeTaxesNoncurrent
- us-gaap_OtherLiabilitiesNoncurrent + nvda_CharitableContributionPayableLongterm
- us-gaap_OtherLiabilitiesNoncurrent + us-gaap_DeferredRevenueNoncurrent
- us-gaap_OtherLiabilitiesNoncurrent + nvda_LiabilitesOtherNoncurrent

#### us-gaap_AccruedLiabilitiesCurrent

- us-gaap_AccruedLiabilitiesCurrent + us-gaap_DeferredRevenueCurrent
- us-gaap_AccruedLiabilitiesCurrent + nvda_AccruedCustomerProgramsCurrent
- us-gaap_AccruedLiabilitiesCurrent + us-gaap_EmployeeRelatedLiabilitiesCurrent
- us-gaap_AccruedLiabilitiesCurrent + us-gaap_RestructuringReserve
- us-gaap_AccruedLiabilitiesCurrent + us-gaap_AccruedProfessionalFeesCurrentAndNoncurrent
- us-gaap_AccruedLiabilitiesCurrent + us-gaap_InterestPayableCurrent
- us-gaap_AccruedLiabilitiesCurrent + nvda_AccruedTaxesPayable
- us-gaap_AccruedLiabilitiesCurrent + us-gaap_OtherAccruedLiabilitiesCurrent
- us-gaap_AccruedLiabilitiesCurrent + us-gaap_ProductWarrantyAccrualClassifiedCurrent
- us-gaap_AccruedLiabilitiesCurrent + us-gaap_AccruedRoyaltiesCurrent
- us-gaap_AccruedLiabilitiesCurrent + us-gaap_CapitalLeaseObligationsCurrent
- us-gaap_AccruedLiabilitiesCurrent + nvda_Charitablecontributionpayable

### ConsolidatedBalanceSheets

#### us-gaap_LiabilitiesAndStockholdersEquity

- us-gaap_LiabilitiesAndStockholdersEquity + us-gaap_LiabilitiesCurrent
- us-gaap_LiabilitiesAndStockholdersEquity + us-gaap_LongTermDebt
- us-gaap_LiabilitiesAndStockholdersEquity + us-gaap_OtherLiabilitiesNoncurrent
- us-gaap_LiabilitiesAndStockholdersEquity + us-gaap_TemporaryEquityValueExcludingAdditionalPaidInCapital
- us-gaap_LiabilitiesAndStockholdersEquity + us-gaap_PreferredStockValueOutstanding
- us-gaap_LiabilitiesAndStockholdersEquity + us-gaap_CommonStockValue
- us-gaap_LiabilitiesAndStockholdersEquity + us-gaap_AdditionalPaidInCapital
- us-gaap_LiabilitiesAndStockholdersEquity - us-gaap_TreasuryStockValue
- us-gaap_LiabilitiesAndStockholdersEquity + us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
- us-gaap_LiabilitiesAndStockholdersEquity + us-gaap_RetainedEarningsAccumulatedDeficit
- us-gaap_LiabilitiesAndStockholdersEquity + us-gaap_CapitalLeaseObligationsNoncurrent

#### us-gaap_LiabilitiesCurrent

- us-gaap_LiabilitiesCurrent + us-gaap_AccountsPayableCurrent
- us-gaap_LiabilitiesCurrent + us-gaap_AccruedLiabilitiesCurrent
- us-gaap_LiabilitiesCurrent + us-gaap_ConvertibleDebtCurrent

#### us-gaap_StockholdersEquity

- us-gaap_StockholdersEquity + us-gaap_PreferredStockValueOutstanding
- us-gaap_StockholdersEquity + us-gaap_CommonStockValue
- us-gaap_StockholdersEquity + us-gaap_AdditionalPaidInCapital
- us-gaap_StockholdersEquity - us-gaap_TreasuryStockValue
- us-gaap_StockholdersEquity + us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax
- us-gaap_StockholdersEquity + us-gaap_RetainedEarningsAccumulatedDeficit

#### us-gaap_Assets

- us-gaap_Assets + us-gaap_AssetsCurrent
- us-gaap_Assets + us-gaap_PropertyPlantAndEquipmentNet
- us-gaap_Assets + us-gaap_Goodwill
- us-gaap_Assets + us-gaap_IntangibleAssetsNetExcludingGoodwill
- us-gaap_Assets + us-gaap_OtherAssetsNoncurrent

#### us-gaap_AssetsCurrent

- us-gaap_AssetsCurrent + us-gaap_CashAndCashEquivalentsAtCarryingValue
- us-gaap_AssetsCurrent + us-gaap_MarketableSecuritiesCurrent
- us-gaap_AssetsCurrent + us-gaap_AccountsReceivableNetCurrent
- us-gaap_AssetsCurrent + us-gaap_InventoryNet
- us-gaap_AssetsCurrent + us-gaap_PrepaidExpenseAndOtherAssetsCurrent

#### us-gaap_Liabilities

- us-gaap_Liabilities + us-gaap_LiabilitiesCurrent
- us-gaap_Liabilities + us-gaap_LongTermDebt
- us-gaap_Liabilities + us-gaap_OtherLiabilitiesNoncurrent
- us-gaap_Liabilities + us-gaap_CapitalLeaseObligationsNoncurrent

### IntangibleAssetsDetails

#### us-gaap_FiniteLivedIntangibleAssetsNet

- us-gaap_FiniteLivedIntangibleAssetsNet + us-gaap_FiniteLivedIntangibleAssetsGross
- us-gaap_FiniteLivedIntangibleAssetsNet - us-gaap_FiniteLivedIntangibleAssetsAccumulatedAmortization

## 现金流量表计算逻辑 (Cash Flow Calculations)

### ConsolidatedStatementsOfCashFlows

#### us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease

- us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease + us-gaap_NetCashProvidedByUsedInOperatingActivities
- us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease + us-gaap_NetCashProvidedByUsedInInvestingActivities
- us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease + us-gaap_NetCashProvidedByUsedInFinancingActivities

#### us-gaap_NetCashProvidedByUsedInOperatingActivities

- us-gaap_NetCashProvidedByUsedInOperatingActivities + us-gaap_NetIncomeLoss
- us-gaap_NetCashProvidedByUsedInOperatingActivities + us-gaap_DepreciationAndAmortization
- us-gaap_NetCashProvidedByUsedInOperatingActivities + us-gaap_ShareBasedCompensation
- us-gaap_NetCashProvidedByUsedInOperatingActivities + nvda_RestructuringchargesNoncash
- us-gaap_NetCashProvidedByUsedInOperatingActivities + us-gaap_AmortizationOfDebtDiscountPremium
- us-gaap_NetCashProvidedByUsedInOperatingActivities - nvda_GainsonSalesoflonglivedassetsandinvestment
- us-gaap_NetCashProvidedByUsedInOperatingActivities - us-gaap_GainsLossesOnExtinguishmentOfDebt
- us-gaap_NetCashProvidedByUsedInOperatingActivities + us-gaap_DeferredIncomeTaxExpenseBenefit
- us-gaap_NetCashProvidedByUsedInOperatingActivities - us-gaap_ExcessTaxBenefitFromShareBasedCompensationOperatingActivities
- us-gaap_NetCashProvidedByUsedInOperatingActivities - us-gaap_OtherNoncashIncomeExpense
- us-gaap_NetCashProvidedByUsedInOperatingActivities - us-gaap_IncreaseDecreaseInAccountsReceivable
- us-gaap_NetCashProvidedByUsedInOperatingActivities - us-gaap_IncreaseDecreaseInInventories
- us-gaap_NetCashProvidedByUsedInOperatingActivities - us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets
- us-gaap_NetCashProvidedByUsedInOperatingActivities + us-gaap_IncreaseDecreaseInAccountsPayable
- us-gaap_NetCashProvidedByUsedInOperatingActivities + us-gaap_IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities
- us-gaap_NetCashProvidedByUsedInOperatingActivities + us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities

#### us-gaap_NetCashProvidedByUsedInInvestingActivities

- us-gaap_NetCashProvidedByUsedInInvestingActivities - us-gaap_PaymentsToAcquireMarketableSecurities
- us-gaap_NetCashProvidedByUsedInInvestingActivities + us-gaap_ProceedsFromSaleOfAvailableForSaleSecurities
- us-gaap_NetCashProvidedByUsedInInvestingActivities + us-gaap_ProceedsFromSaleAndMaturityOfMarketableSecurities
- us-gaap_NetCashProvidedByUsedInInvestingActivities - nvda_PurchasesOfPropertyAndEquipmentAndIntangibleAssets
- us-gaap_NetCashProvidedByUsedInInvestingActivities + nvda_Proceedsfromsaleoflonglivedassetsandinvestments
- us-gaap_NetCashProvidedByUsedInInvestingActivities + nvda_Reimbursementofheadquartersbuildingdevelopmentcostsfromlessor
- us-gaap_NetCashProvidedByUsedInInvestingActivities - us-gaap_PaymentsForProceedsFromOtherInvestingActivities

#### us-gaap_NetCashProvidedByUsedInFinancingActivities

- us-gaap_NetCashProvidedByUsedInFinancingActivities + nvda_Netproceedspaymentsrelatedtoemployeestockplans
- us-gaap_NetCashProvidedByUsedInFinancingActivities - us-gaap_PaymentsForRepurchaseOfCommonStock
- us-gaap_NetCashProvidedByUsedInFinancingActivities - us-gaap_PaymentsOfDividends
- us-gaap_NetCashProvidedByUsedInFinancingActivities + us-gaap_ExcessTaxBenefitFromShareBasedCompensationFinancingActivities
- us-gaap_NetCashProvidedByUsedInFinancingActivities + us-gaap_ProceedsFromPaymentsForOtherFinancingActivities
- us-gaap_NetCashProvidedByUsedInFinancingActivities + us-gaap_ProceedsFromConvertibleDebt
- us-gaap_NetCashProvidedByUsedInFinancingActivities - us-gaap_RepaymentsOfConvertibleDebt
- us-gaap_NetCashProvidedByUsedInFinancingActivities - us-gaap_PaymentsOfDebtIssuanceCosts

## 损益表计算逻辑 (Income Statement Calculations)

### ConsolidatedStatementsOfComprehensiveIncome

#### us-gaap_ComprehensiveIncomeNetOfTax

- us-gaap_ComprehensiveIncomeNetOfTax + us-gaap_OtherComprehensiveIncomeLossNetOfTax
- us-gaap_ComprehensiveIncomeNetOfTax + us-gaap_NetIncomeLoss

### ConsolidatedStatementsOfIncome

#### us-gaap_NetIncomeLoss

- us-gaap_NetIncomeLoss - us-gaap_IncomeTaxExpenseBenefit
- us-gaap_NetIncomeLoss + us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments

#### us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments

- us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments + us-gaap_InvestmentIncomeInterest
- us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments + us-gaap_OtherNonoperatingIncomeExpense
- us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments - us-gaap_InterestExpense
- us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments + us-gaap_OperatingIncomeLoss

#### us-gaap_OperatingIncomeLoss

- us-gaap_OperatingIncomeLoss + us-gaap_GrossProfit
- us-gaap_OperatingIncomeLoss - us-gaap_OperatingExpenses

#### us-gaap_GrossProfit

- us-gaap_GrossProfit + us-gaap_Revenues
- us-gaap_GrossProfit - us-gaap_CostOfRevenue

#### us-gaap_OperatingExpenses

- us-gaap_OperatingExpenses + us-gaap_ResearchAndDevelopmentExpense
- us-gaap_OperatingExpenses + us-gaap_SellingGeneralAndAdministrativeExpense
- us-gaap_OperatingExpenses + us-gaap_RestructuringCharges

### IncomeTaxesDetails

#### us-gaap_DeferredTaxLiabilities

- us-gaap_DeferredTaxLiabilities + nvda_DeferredTaxLiabilitiesIntangibleAssets
- us-gaap_DeferredTaxLiabilities + us-gaap_DeferredTaxLiabilitiesUndistributedForeignEarnings

#### us-gaap_CurrentIncomeTaxExpenseBenefit

- us-gaap_CurrentIncomeTaxExpenseBenefit + us-gaap_CurrentFederalTaxExpenseBenefit
- us-gaap_CurrentIncomeTaxExpenseBenefit + us-gaap_CurrentStateAndLocalTaxExpenseBenefit
- us-gaap_CurrentIncomeTaxExpenseBenefit + us-gaap_CurrentForeignTaxExpenseBenefit

#### us-gaap_DeferredIncomeTaxExpenseBenefit

- us-gaap_DeferredIncomeTaxExpenseBenefit + us-gaap_DeferredFederalIncomeTaxExpenseBenefit
- us-gaap_DeferredIncomeTaxExpenseBenefit + us-gaap_DeferredStateAndLocalIncomeTaxExpenseBenefit
- us-gaap_DeferredIncomeTaxExpenseBenefit + us-gaap_DeferredForeignIncomeTaxExpenseBenefit

#### us-gaap_DeferredTaxAssetsGross

- us-gaap_DeferredTaxAssetsGross + us-gaap_DeferredTaxAssetsOperatingLossCarryforwards
- us-gaap_DeferredTaxAssetsGross + us-gaap_DeferredTaxAssetsTaxDeferredExpenseReservesAndAccruals
- us-gaap_DeferredTaxAssetsGross + nvda_DeferredTaxAssetsPropertyEquipmentAndIntangibleAssets
- us-gaap_DeferredTaxAssetsGross + us-gaap_DeferredTaxAssetsTaxCreditCarryforwards
- us-gaap_DeferredTaxAssetsGross + us-gaap_DeferredTaxAssetsTaxDeferredExpenseCompensationAndBenefitsShareBasedCompensationCost
- us-gaap_DeferredTaxAssetsGross + nvda_ConvertibledebtDTA

## 其他计算逻辑 (Other Calculations)

### DebtDetails

#### us-gaap_InterestExpenseDebt

- us-gaap_InterestExpenseDebt + us-gaap_InterestExpenseDebtExcludingAmortization
- us-gaap_InterestExpenseDebt + us-gaap_AmortizationOfFinancingCostsAndDiscounts

### MarketableSecuritiesDetails

#### us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis

- us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis + us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearAmortizedCost
- us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis + us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsAmortizedCost
- us-gaap_AvailableForSaleDebtSecuritiesAmortizedCostBasis + us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithoutSingleMaturityDateAmortizedCost

#### us-gaap_AvailableForSaleSecurities

- us-gaap_AvailableForSaleSecurities + us-gaap_CashEquivalentsAtCarryingValue
- us-gaap_AvailableForSaleSecurities + us-gaap_MarketableSecuritiesCurrent

#### us-gaap_AvailableForSaleSecuritiesDebtSecurities

- us-gaap_AvailableForSaleSecuritiesDebtSecurities + us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithinOneYearFairValue
- us-gaap_AvailableForSaleSecuritiesDebtSecurities + us-gaap_AvailableForSaleSecuritiesDebtMaturitiesAfterOneThroughFiveYearsFairValue
- us-gaap_AvailableForSaleSecuritiesDebtSecurities + us-gaap_AvailableForSaleSecuritiesDebtMaturitiesWithoutSingleMaturityDateFairValue

### RestructuringAndOtherChargesDetails

#### us-gaap_RestructuringCharges

- us-gaap_RestructuringCharges + us-gaap_SeveranceCosts1
- us-gaap_RestructuringCharges - nvda_TaxreservereleaserelatedtoIcera
- us-gaap_RestructuringCharges + nvda_Facilitiesandrelatedcostsrestructuringcharge
- us-gaap_RestructuringCharges + nvda_Otherexitcosts

## 主要计算公式总结

