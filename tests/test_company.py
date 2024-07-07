import unittest
from pysimons.company import Company

class TestCompany(unittest.TestCase):
    def setUp(self):
        self.company = Company(name='TestCorp', industry='Technology')

    def test_generate_balance_sheet(self):
        balance_sheet = self.company.generate_balance_sheet()
        self.assertIn('Assets', balance_sheet.columns)
        self.assertIn('Liabilities', balance_sheet.columns)
        self.assertIn('Equity', balance_sheet.columns)

    def test_generate_income_statement(self):
        income_statement = self.company.generate_income_statement()
        self.assertIn('Revenue', income_statement.columns)
        self.assertIn('Net Income', income_statement.columns)

    def test_generate_cash_flow_statement(self):
        self.company.generate_income_statement()  # Need income statement first
        cash_flow_statement = self.company.generate_cash_flow_statement()
        self.assertIn('Net Change in Cash', cash_flow_statement.columns)

if __name__ == '__main__':
    unittest.main()
