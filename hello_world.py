import unittest
from unittest.main import main
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(cls):
        driver = cls.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(cls):
        cls.driver.get('https://es.wikipedia.org/wiki/Wikipedia:Portada')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))