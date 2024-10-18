import unittest
import time
from selenium import webdriver
from page_objects.finance_page import FinancePage

class FinanceTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  
        self.finance_page = FinancePage(self.driver)
        self.test_data = ["NFLX", "MSFT", "TSLA"]

    def tearDown(self):
        self.driver.quit()

    def test_full(self):
        self.finance_page.load()

        # Verify the page is loaded by asserting the page title
        self.assertIn("Google Finance", self.finance_page.get_title())

        print("Title confirmed ")

        # Retrieve stock symbols from the page
        retrieved_symbols = self.finance_page.get_stock_symbols()

        # Compare with given test data
        print("Retrieved symbols: ", retrieved_symbols)

        # Find symbols in retrieved but not in test data
        missing_from_test_data = [symbol for symbol in retrieved_symbols if symbol not in self.test_data]
        print("Symbols in retrieved but not in test data:", missing_from_test_data)

        # Find symbols in test data but not in retrieved
        missing_from_retrieved = [symbol for symbol in self.test_data if symbol not in retrieved_symbols]
        print("Symbols in test data but not in retrieved:", missing_from_retrieved)

    # Test case 5: Symbols in retrieved but not in test data
    def test_case_5(self):
        self.finance_page.load()

        # Retrieve stock symbols from the page
        retrieved_symbols = self.finance_page.get_stock_symbols()

        # Symbols in retrieved but not in test data
        missing_from_test_data = [symbol for symbol in retrieved_symbols if symbol not in self.test_data]
        print("Symbols in retrieved but not in test data:", missing_from_test_data)

    # Test case 6: Symbols in test data but not in retrieved
    def test_case_6(self):
        self.finance_page.load()

        # Retrieve stock symbols from the page
        retrieved_symbols = self.finance_page.get_stock_symbols()

        # Symbols in test data but not in retrieved
        missing_from_retrieved = [symbol for symbol in self.test_data if symbol not in retrieved_symbols]
        print("Symbols in test data but not in retrieved:", missing_from_retrieved)


if __name__ == "__main__":
    unittest.main()
