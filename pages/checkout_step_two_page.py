from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutStepTwoPage(BasePage):
    finish_button = (By.ID, 'finish')

    def finish_checkout(self):
        self.find_element(*self.finish_button).click()
