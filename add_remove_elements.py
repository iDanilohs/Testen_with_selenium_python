import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.maximize_window()
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')
        sleep(3)

        for i in range(total_elements):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/button[1]')
                delete_button.click()
            except:
                print('You are try to delete more elements that exists')
                break

        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print("There 0 are elements on screen")

        sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)