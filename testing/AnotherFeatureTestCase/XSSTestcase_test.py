import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        
        def xss_page(self):
            expected_result = "Profil"
            self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/a[2]").click()
            actual_title = self.browser.title
            self.assertEqual(expected_result, actual_title)

        def test_xss(self):
            input_field = self.browser.find_element(By.NAME, 'thing')
            input_value = '<script>alert("Cross Site Scripting is COOL");</script>'
            input_field.send_keys(input_value)
            submit_button = self.browser.find_element(By.NAME, 'submit')
            submit_button.click()
            alert = self.browser.switch_to.alert
            self.assertEqual('Cross Site Scripting is COOL', alert.text)
            alert.accept()

        login_correct_credentials(self)
        index_page(self)
        xss_page(self)
        test_xss(self)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')