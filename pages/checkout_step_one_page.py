from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutStepOnePage(BasePage):
    first_name_field = (By.ID, 'first-name')
    last_name_field = (By.ID, 'last-name')
    postal_code_field = (By.ID, 'postal-code')
    continue_button = (By.ID, 'continue')

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.find_element(*self.first_name_field).send_keys(first_name)
        self.find_element(*self.last_name_field).send_keys(last_name)
        self.find_element(*self.postal_code_field).send_keys(postal_code)

    def continue_to_next_step(self):
        self.find_element(*self.continue_button).click()
