import numpy as np
import pandas as pd

class Company:
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry
        self.financials = {}

    def generate_balance_sheet(self, year=2023):
        # Example synthetic data generation for a balance sheet
        assets = np.random.randint(1e6, 1e8)
        liabilities = np.random.randint(1e6, assets)
        equity = assets - liabilities

        balance_sheet = {
            'Year': year,
            'Assets': assets,
            'Liabilities': liabilities,
            'Equity': equity,
        }
        self.financials['balance_sheet'] = balance_sheet
        return pd.DataFrame([balance_sheet])

    def generate_income_statement(self, year=2023):
        # Example synthetic data generation for an income statement
        revenue = np.random.randint(1e6, 1e7)
        cogs = np.random.randint(0.4 * revenue, 0.6 * revenue)
        gross_profit = revenue - cogs
        expenses = np.random.randint(0.2 * gross_profit, 0.4 * gross_profit)
        net_income = gross_profit - expenses

        income_statement = {
            'Year': year,
            'Revenue': revenue,
            'COGS': cogs,
            'Gross Profit': gross_profit,
            'Expenses': expenses,
            'Net Income': net_income,
        }
        self.financials['income_statement'] = income_statement
        return pd.DataFrame([income_statement])

    def generate_cash_flow_statement(self, year=2023):
        # Example synthetic data generation for a cash flow statement
        net_income = self.financials['income_statement']['Net Income']
        depreciation = np.random.randint(0.1 * net_income, 0.3 * net_income)
        changes_in_working_capital = np.random.randint(-0.1 * net_income, 0.1 * net_income)
        cash_from_operations = net_income + depreciation + changes_in_working_capital
        capital_expenditures = np.random.randint(0.1 * cash_from_operations, 0.3 * cash_from_operations)
        cash_from_investing = -capital_expenditures
        cash_from_financing = np.random.randint(-0.2 * cash_from_operations, 0.2 * cash_from_operations)
        net_change_in_cash = cash_from_operations + cash_from_investing + cash_from_financing

        cash_flow_statement = {
            'Year': year,
            'Net Income': net_income,
            'Depreciation': depreciation,
            'Changes in Working Capital': changes_in_working_capital,
            'Cash from Operations': cash_from_operations,
            'Capital Expenditures': capital_expenditures,
            'Cash from Investing': cash_from_investing,
            'Cash from Financing': cash_from_financing,
            'Net Change in Cash': net_change_in_cash,
        }
        self.financials['cash_flow_statement'] = cash_flow_statement
        return pd.DataFrame([cash_flow_statement])
