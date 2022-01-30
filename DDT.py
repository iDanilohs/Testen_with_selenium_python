import unittest
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()

    @data(('dress', 5), ('music', 5)) #This go to the def test_search_ddt for serch_value and expected_account
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_filed = driver.find_element_by_name('q')
        search_filed.clear()
        search_filed.send_keys(search_value)
        search_filed.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        print(f'found {len(products)} products')

        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)