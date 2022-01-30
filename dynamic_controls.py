import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.maximize_window()
        driver.find_element_by_link_text('Dynamic Controls').click()

    def test_dynamic_controls(self):
        driver = self.driver

        checkbox = driver.find_element_by_css_selector("#checkbox > input[type=checkbox]")
        checkbox.click()
        
        remove_add = driver.find_element_by_css_selector("#checkbox-example > button")
        remove_add.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example > button")))
        remove_add.click()

    def test_dynamic_controls_text(self):
        driver = self.driver

        button_enable = driver.find_element_by_css_selector("#input-example > button")
        button_enable.click()

        input_page = driver.find_element_by_css_selector("#input-example > input[type=text]")
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > input[type=text]")))
        input_page.send_keys('Danilo puto amo')
        button_enable.click()
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)