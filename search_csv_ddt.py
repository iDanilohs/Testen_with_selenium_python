import csv, unittest
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)
    return rows

@ddt
class SearchCsvDdt(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()

    @data(*get_data('testdata.csv')) 
    @unpack

    def test_search_csv_ddt(self, search_value, expected_count):
        driver = self.driver

        search_filed = driver.find_element_by_name('q')
        search_filed.clear()
        search_filed.send_keys(search_value)
        search_filed.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')

        expected_count = int(expected_count)

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.', message)

        print(f'found {len(products)} products')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)