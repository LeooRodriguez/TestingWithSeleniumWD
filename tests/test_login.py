import sys
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By  
from pages.login_page import LoginPage


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        time.sleep(3)

    def test_successful_login(self):
        self.login_page.go_to("")
        time.sleep(3)
        self.login_page.login('standard_user', 'secret_sauce')
        time.sleep(3)
        self.assertIn("inventory.html", self.driver.current_url)

    def test_unsuccessful_login(self):
        self.login_page.go_to("")
        time.sleep(3)
        self.login_page.login('invalid_user', 'invalid_password')
        time.sleep(3)
        error_message = self.login_page.wait_for_element((By.CSS_SELECTOR, '.error-message-container'))
        self.assertTrue(error_message.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
