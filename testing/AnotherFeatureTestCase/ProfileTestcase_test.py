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

        def profile_page(self):
            expected_result = "Profil"
            self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/a[1]").click()
            actual_title = self.browser.title
            self.assertEqual(expected_result, actual_title)
        
        def upload_profile_picture(self):
            file_input = self.browser.find_element(By.ID, 'formFile')
            image_path = os.path.join(os.getcwd(),'testing' ,'images', 'images.jpg')
            file_input.send_keys(image_path)
            submit_button = self.browser.find_element(By.CSS_SELECTOR, 'button.btn-secondary')
            submit_button.click()
            redirected_url = self.url + '/profil.php'
            self.assertEqual(redirected_url, self.browser.current_url)
            new_profile_picture = self.browser.find_element(By.CSS_SELECTOR, 'img[src="image/profile.jpg"]')
            self.assertIsNotNone(new_profile_picture)

        login_correct_credentials(self)
        index_page(self)
        profile_page(self)
        upload_profile_picture(self)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')