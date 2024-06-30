from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    inventory_items = (By.CLASS_NAME, 'inventory_item')
    add_to_cart_buttons = (By.CLASS_NAME, 'btn_inventory')
    cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')

    def add_first_item_to_cart(self):
        self.find_element(*self.add_to_cart_buttons).click()

    def get_cart_count(self):
        return self.find_element(*self.cart_badge).text
