from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

try:
    driver.get('https://www.saucedemo.com/')
    username = driver.find_element(By.ID, 'user-name')
    password = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')
    username.send_keys('standard_user')
    password.send_keys('secret_sauce')
    login_button.click()
    time.sleep(2)

    assert "inventory.html" in driver.current_url, "Login failed"

    print("Login test passed")

finally:
    driver.quit()
