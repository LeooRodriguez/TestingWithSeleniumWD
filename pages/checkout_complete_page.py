from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutCompletePage(BasePage):
    complete_message = (By.CLASS_NAME, 'complete-header')

    def get_complete_message(self):
        return self.find_element(*self.complete_message).text
