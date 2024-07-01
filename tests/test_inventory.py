import sys
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    request.cls.inventory_page = InventoryPage(driver)
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestInventory:

    def test_inventory_page_load(self, username, password):
        self.login_page.go_to("")
        self.login_page.login(username, password)
        time.sleep(3)
        
        if username == 'locked_out_user':
            error_message = self.login_page.wait_for_element((By.CSS_SELECTOR, '.error-message-container'))
            assert error_message.is_displayed()
            assert "Epic sadface: Sorry, this user has been locked out." in error_message.text
        else:
            inventory_items = self.inventory_page.get_inventory_items()
            assert len(inventory_items) > 0, "No inventory items found"

    def test_add_item_to_cart(self, username, password):
        self.login_page.go_to("")
        self.login_page.login(username, password)
        time.sleep(3)
        
        if username == 'locked_out_user':
            error_message = self.login_page.wait_for_element((By.CSS_SELECTOR, '.error-message-container'))
            assert error_message.is_displayed()
            assert "Epic sadface: Sorry, this user has been locked out." in error_message.text
        else:
            self.inventory_page.add_first_item_to_cart()
            time.sleep(1)
            cart_count = self.inventory_page.get_cart_count()
            assert cart_count == '1', "Cart count should be 1 after adding one item"

    def test_remove_item_from_cart(self, username, password):
        self.login_page.go_to("")
        self.login_page.login(username, password)
        time.sleep(3)
        
        if username == 'locked_out_user':
            error_message = self.login_page.wait_for_element((By.CSS_SELECTOR, '.error-message-container'))
            assert error_message.is_displayed()
            assert "Epic sadface: Sorry, this user has been locked out." in error_message.text
        else:
            self.inventory_page.add_first_item_to_cart()
            time.sleep(1)
            self.inventory_page.find_element(By.CLASS_NAME, 'btn_secondary').click()
            time.sleep(1)
            cart_badge = self.inventory_page.driver.find_elements(*self.inventory_page.cart_badge)
            assert len(cart_badge) == 0, "Cart should be empty after removing the item"
