import pandas as pd
import numpy as np
# from src.analysis.cost_of_capital.capm import capm

def capm(Rf=0.294, Rm=0.979, beta=1):
    """
    Capital Asset Pricing Model
    r R e F = + β − i M [E(R ) RF ]
    where:
        [E(RM) − Rf] = Equity risk premium.
        RM = Expected return on the market.
        βi = Beta of stock. Beta measures the sensitivity of the stock’s returns to changes in market
        returns.
        RF = Risk‐free rate.
        r_e = Expected return on stock (cost of equity).
    """
    r_e = (Rf+beta*(Rm-Rf))
    return r_e


def growth_rate(metric, number_of_years=5):
    """
    Growth rate
    """

    current_year = metric[-1]
    past_year = metric[-number_of_years]
    # print(f'current year {current_year}\n past year {past_year}')
    if current_year*past_year>0:
        growth_rate = (current_year/past_year)**(1/(number_of_years-1))-1
    else:
        growth_rate = 0
    # print(f'growth rate {growth_rate}')
    return growth_rate

def discounted_cash_flow(cash_flow, growth_rate, discount_rate, share_outstanding):
    """
    Discounted cash flow
    """
    # if growth_rate > discount_rate:
    #     growth_rate = discount_rate
    discounted_cash_flow = [cash_flow *((1 + growth_rate) ** year)/ ((1 + discount_rate) ** year) for year, cash_flow in enumerate(cash_flow)]
    dcf = np.sum(discounted_cash_flow)/share_outstanding
    # print(cash_flow, growth_rate, discount_rate, share_outstanding)
    return dcf

def fcff(report_data, ticker, share_outstanding, price, tax_rate=0.2):
    """
    FCFF is the cash flow available to the company’s suppliers of debt and equity capital
    after all operating expenses (including income taxes) have been paid and necessary
    investments in working capital and fixed capital have been made. FCFF can be computed starting with net income as
    FCFF = NI + NCC + Int(1 – Tax rate) – FCInv – WCInv
    where
    NI = Net income
    NCC = Non-cash charges (such as depreciation and amortisation)
    Int = Interest expense
    FCInv = Capital expenditures (fixed capital, such as equipment)
    WCInv = Working capital expenditures
    """
    # share_outstanding = share_outstanding[ticker]
    # price = price[ticker]
    # total_liabilities = report_data[f'{ticker}_balancesheet'].loc['total_liabilities']
    depreciation = report_data[f'{ticker}_cashflow'].loc['depreciation']
    provision_expenses = report_data[f'{ticker}_cashflow'].loc['provision_expenses']
    cash_paid_for_purchase_of_fixed_assets_and_other_long_term_assets = report_data[f'{ticker}_cashflow'].loc['cash_paid_for_purchase_of_fixed_assets_and_other_long_term_assets']
    cash_received_from_disposal_of_fixed_assets = report_data[f'{ticker}_cashflow'].loc['cash_received_from_disposal_of_fixed_assets']
    increase_decrease_in_accounts_receivable = report_data[f'{ticker}_cashflow'].loc['increase_decrease_in_accounts_receivable']
    increase_decrease_in_inventory = report_data[f'{ticker}_cashflow'].loc['increase_decrease_in_inventory']
    increase_decrease_in_accounts_payable = report_data[f'{ticker}_cashflow'].loc['increase_decrease_in_accounts_payable']
    increase_decrease_in_prepaid_expenses = report_data[f'{ticker}_cashflow'].loc['increase_decrease_in_prepaid_expenses']
    interest_expense = report_data[f'{ticker}_incomestatement'].loc['interest_expense']
    revenue = report_data[f'{ticker}_incomestatement'].loc['revenue']
    net_profit = report_data[f'{ticker}_incomestatement'].loc['profit_attributable_to_shareholders_of_the_parent_company']

    non_cash_charge = depreciation + provision_expenses
    FCInv = cash_paid_for_purchase_of_fixed_assets_and_other_long_term_assets + cash_received_from_disposal_of_fixed_assets
    WCInv = increase_decrease_in_accounts_receivable\
          + increase_decrease_in_inventory\
          + increase_decrease_in_accounts_payable\
          + increase_decrease_in_prepaid_expenses

    # # Calculate debt ratio
    # total_liabilities = liabilities
    # total_assets = total_assets
    # debt_ratio = total_liabilities / total_assets

    # Calculate fcff (cash flow)
    fcff = np.array(
        net_profit - interest_expense * (1 - tax_rate) + FCInv + WCInv
    )

    # Assumption: Cash flow is constant for 10 years
    cash_flows = np.ones(10) * np.average(fcff[-3:])

    # Calculate discount rate using the Capital Asset Pricing Model (CAPM)
    discount_rate = capm(Rf=0.0294, Rm=0.1842, beta=1)

    # Determine the minimum growth rate
    growth = min(
        growth_rate(metric=fcff, number_of_years=5),
        growth_rate(metric=revenue, number_of_years=5),
        growth_rate(metric=fcff, number_of_years=8)
    )

    # Calculate discounted cash flow (dcf)
    dcf = discounted_cash_flow(cash_flows, growth, discount_rate, share_outstanding[ticker])

    return dcf