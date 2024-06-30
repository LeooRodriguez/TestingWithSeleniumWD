from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    username_field = (By.ID, 'user-name')
    password_field = (By.ID, 'password')
    login_button = (By.ID, 'login-button')

    def login(self, username, password):
        self.find_element(*self.username_field).send_keys(username)
        self.find_element(*self.password_field).send_keys(password)
        self.find_element(*self.login_button).click()
