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

    def test_start(self):
        def login_correct_credentials(self):
            login_url = self.url +'/login.php'
            self.browser.get(login_url)
            self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
            self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
            self.browser.find_element(By.TAG_NAME, 'button').click()

        def index_page(self):
            expected_result = "admin"
            actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/h2").text.split(', ')[1]
            self.assertIn(expected_result, actual_result)
        
        def create_contact_page(self):
            expected_result = "contact"
            self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/a").click()
            actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/h5").text.split('new')[1]
            self.assertIn(expected_result, actual_result)

        def create_contact_form(self):
            self.browser.find_element(By.ID, 'name').send_keys('mufat2')
            self.browser.find_element(By.ID, 'email').send_keys('mufat2@gmail.com')
            self.browser.find_element(By.ID, 'phone').send_keys('08111111111111111')
            self.browser.find_element(By.ID, 'title').send_keys('Teman2')
            self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/form/input[5]').click()
            index_page_title = "Dashboard"
            actual_title = self.browser.title
            self.assertEqual(index_page_title, actual_title)

        def search_contact_name(self):
            self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys('mufat2')
            self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys(Keys.ENTER)
            searched_contact_name = self.browser.find_elements(By.XPATH, f"//td[contains(text(), 'mufat2')]")
            self.assertTrue(searched_contact_name)

        def contact_edit(self):
            actions_section = self.browser.find_element(By.XPATH, "//tr[@role='row'][1]//td[contains(@class, 'actions')]")
            update_button = actions_section.find_element(By.XPATH, ".//a[contains(@class, 'btn-success')]")
            update_button.click()
            self.browser.find_element(By.ID, 'name').clear()
            self.browser.find_element(By.ID, 'name').send_keys("new mufat")
            self.browser.find_element(By.ID, 'email').clear()
            self.browser.find_element(By.ID, 'email').send_keys("newemail@gmail.com")
            self.browser.find_element(By.ID, 'phone').clear()
            self.browser.find_element(By.ID, 'phone').send_keys("08222222222222")
            self.browser.find_element(By.ID, 'title').clear()
            self.browser.find_element(By.ID, 'title').send_keys("new title")
            self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
            index_page_title = "Dashboard"
            actual_title = self.browser.title
            self.assertEqual(index_page_title, actual_title)

        def check_search_contact(self):
            self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys("new mufat")
            self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys(Keys.ENTER)
            updated_contact_exists = self.browser.find_elements(By.XPATH, f"//td[contains(text(), 'new title')]")
            self.assertTrue(updated_contact_exists)
            updated_contact_exists = self.browser.find_elements(By.XPATH, f"//td[contains(text(), 'newemail@gmail.com')]")
            self.assertTrue(updated_contact_exists)
            updated_contact_exists = self.browser.find_elements(By.XPATH, f"//td[contains(text(), '08222222222222')]")
            self.assertTrue(updated_contact_exists)

        login_correct_credentials(self)
        index_page(self)
        create_contact_page(self)
        create_contact_form(self)
        search_contact_name(self)
        contact_edit(self)
        check_search_contact(self)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')