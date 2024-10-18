from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FinancePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com/finance"
        self.stock_symbols_locator = ".sbnBtf a .COaKTb"  # Adjust according to actual DOM
        #self.stock_symbols_locator = ".sbnBtf a"  # Adjust according to actual DOM
    def load(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title

    def get_stock_symbols(self):
        # Wait until stock symbols are present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.stock_symbols_locator))
        )
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.stock_symbols_locator)
        return [element.text for element in elements]
