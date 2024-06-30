import sys
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By  
from pages.login_page import LoginPage
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'pages'))

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        #time.sleep(3)

    def test_successful_login_standard_user(self):
        self.login_page.go_to("")
        #time.sleep(3)
        self.login_page.login('standard_user', 'secret_sauce')
        #time.sleep(3)
        self.assertIn("inventory.html", self.driver.current_url)
        
    def test_login_locked_out_user(self):
        self.login_page.go_to("")
        #time.sleep(1)
        self.login_page.login('locked_out_user', 'secret_sauce')
        #time.sleep(1)
        error_message = self.login_page.wait_for_element((By.CSS_SELECTOR, '.error-message-container'))
        self.assertTrue(error_message.is_displayed())
        self.assertIn("Epic sadface: Sorry, this user has been locked out.", error_message.text)
        
    def test_successful_login_problem_user(self):
        self.login_page.go_to("")
        #time.sleep(1)
        self.login_page.login('problem_user', 'secret_sauce')
        #time.sleep(1)
        self.assertIn("inventory.html", self.driver.current_url)
        
    def test_successful_login_performance_glitch_user(self):
        self.login_page.go_to("")
        #time.sleep(1)
        self.login_page.login('performance_glitch_user', 'secret_sauce')
        #time.sleep(1)
        self.assertIn("inventory.html", self.driver.current_url)
        
    def test_successful_login_visual_user(self):
        self.login_page.go_to("")
        #time.sleep(1)
        self.login_page.login('visual_user', 'secret_sauce')
        #time.sleep(1)
        self.assertIn("inventory.html", self.driver.current_url)

    def test_unsuccessful_login(self):
        self.login_page.go_to("")
        #time.sleep(1)
        self.login_page.login('invalid_user', 'invalid_password')
        #time.sleep(1)
        error_message = self.login_page.wait_for_element((By.CSS_SELECTOR, '.error-message-container'))
        self.assertTrue(error_message.is_displayed())
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
