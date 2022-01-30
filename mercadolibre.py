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
        driver.get('https://mercadolibre.com/')
        driver.maximize_window()

    
    def test_search(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_partial_link_text('Bogotá D.C.')
        driver.execute_script("arguments[0].click();", location)
        driver.implicitly_wait(3)

        condition = driver.find_element_by_partial_link_text('Nuevo')
        driver.execute_script("arguments[0].click();", condition)
        driver.implicitly_wait(3)

        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        driver.execute_script("arguments[0].click();", order_menu)
        driver.implicitly_wait(3)
        higher_price = driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div > div.ui-search-sort-filter > div > div > div > ul > a:nth-child(3) > div.andes-list__item-first-column > div.andes-list__item-text > div')
        driver.execute_script("arguments[0].click();", higher_price)
        driver.implicitly_wait(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_css_selector(f'#root-app > div > div > section > ol > li:nth-child({i+1}) > div > div > div.ui-search-result__content-wrapper > div.ui-search-item__group.ui-search-item__group--title > a > h2').text
            articles.append(article_name)
            article_price = driver.find_element_by_css_selector(f'#root-app > div > div > section > ol > li:nth-child({i+1}) > div > div > div.ui-search-result__content-wrapper > div.ui-search-result__content-columns > div.ui-search-result__content-column.ui-search-result__content-column--left > div.ui-search-item__group.ui-search-item__group--price > div > div > span.price-tag.ui-search-price__part > span.price-tag-amount > span.price-tag-fraction').text
            prices.append(article_price)
        
        print(articles, prices)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
