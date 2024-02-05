import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class LogoutTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        cls.browser = webdriver.Firefox(options=option)
        try:
            cls.url = os.environ['URL']
        except:
            cls.url = "http://localhost"

    def test_start(self):
        def login_correct_credentials(self):
            login_url = self.url +'/login.php'
            self.browser.get(login_url)
            self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
            self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
            self.browser.find_element(By.TAG_NAME, 'button').click()

        def index_page(self):
            expected_result = "admin"
            actual_result = self.browser.find_element(By.XPATH, "//h2[contains(text(),'Halo,')]").text.split(', ')[1]
            self.assertIn(expected_result, actual_result)
        
        def get_dropdown(self):
            select_element = self.browser.find_element(By.XPATH,'//*[@id="employee_length"]/label/select')
            select = Select(select_element)
            select.select_by_visible_text('100')
            element_tbody = self.browser.find_elements(By.XPATH,'//*[@id="employee"]/tbody/tr')
            tbody_count = len(element_tbody)
            check = tbody_count > 10
            self.assertTrue(check)

        login_correct_credentials(self)
        index_page(self)
        get_dropdown(self)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')