import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

    def login_correct_credentials(self):
        login_url = self.url +'/login.php'
        self.browser.get(login_url)
        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
        self.browser.find_element(By.TAG_NAME, 'button').click()

    def index_page(self):
        expected_result = "admin"
        actual_result = self.browser.find_element(By.CSS_SELECTOR, "body > div.container > h2").text.split(', ')[1]
        self.assertIn(expected_result, actual_result)

    def create_contact_page(self):
        expected_result = "contact"
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/a").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/h5").text.split('new')[1]
        self.assertIn(expected_result, actual_result)

    def create_contact_form(self):
        self.browser.find_element(By.ID, 'name').send_keys('mufat')
        self.browser.find_element(By.ID, 'email').send_keys('mufat@gmail.com')
        self.browser.find_element(By.ID, 'phone').send_keys('0811111111111111')
        self.browser.find_element(By.ID, 'title').send_keys('Teman')
        self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/form/input[5]').click()
        index_page_title = "Dashboard"
        actual_title = self.browser.title
        self.assertEqual(index_page_title, actual_title)
    
    def search_contact_name(self):
        self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys('mufat')
        self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys(Keys.ENTER)
        searched_contact_name = self.browser.find_elements(By.XPATH, f"//td[contains(text(), 'mufat')]")
        self.assertTrue(searched_contact_name)

    def test_start(self):
        self.login_correct_credentials()
        self.index_page()
        self.create_contact_page()
        self.create_contact_form()
        self.search_contact_name()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')