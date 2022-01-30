import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MercadoLibreTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.get('https://www.youtube.com/playlist?list=PLBMmw6ua26zR0CKGZtQi5V_OrySkB_v35')
        driver.maximize_window()

    
    def test_search(self):
        driver = self.driver



    def tearDown(self):
        # self.driver.close()
        pass


if __name__ == "__main__":
    unittest.main(verbosity = 2)