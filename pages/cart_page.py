from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    cart_items = (By.CLASS_NAME, 'cart_item')
    checkout_button = (By.ID, 'checkout')

    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)

    def checkout(self):
        self.find_element(*self.checkout_button).click()
