from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import sys

# Allows sending special keyboard keys like Enter or Tab
from selenium.webdriver.common.keys import Keys

# Allows you decide how you are going to search for the element in the page
from selenium.webdriver.common.by import By

# Provides a way to wait for elements to be loaded or conditions to be met before interacting with the page
from selenium.webdriver.support.ui import WebDriverWait

# 
from selenium.webdriver.support import expected_conditions as ec
import time
from typing import NewType
# chrome driver path
PATH = r"C:\Program Files\chromedriver-win64\chromedriver.exe"

# === SETUP CHROME ===

# setting the chrome to open a incognito window
options = Options()
options.add_argument("--incognito")

# Setting up ChromeDriver to allow Selenium to control Google Chrome
service = Service(PATH)
driver = webdriver.Chrome(service=service, options=options)

# Accessing the website
driver.get("https://www.saucedemo.com/")

# === FUNCTIONS ===
def find_el(by: str, element_identifier: str, search_method):
    try:
        return WebDriverWait(driver, 10).until(
            search_method((by, element_identifier))
        )
    except Exception as e:
        print(f"Exception detected:\n{e}")
        sys.exit()


def type_text(text: str, by: str, element_identifier: str, search_method):
    text_field = find_el(by, element_identifier, search_method)
    text_field.clear()
    text_field.send_keys(text)

# === LOGIN PAGE === 
# Filling the user name field
type_text("standard_user", By.ID, "user-name", ec.presence_of_element_located)
# text_field = driver.find_element(By.ID, "user-name")
# text_field.clear()
# text_field.send_keys("standard_user")

# Filling the password field
type_text("secret_sauce", By.ID, "password", ec.presence_of_element_located)
# text_field = driver.find_element(By.ID, "password")
# text_field.clear()
# text_field.send_keys("secret_sauce")

# Clicking on the login button
login_btn = find_el(By.ID, "login-button", ec.element_to_be_clickable)
login_btn.click()
#driver.find_element(By.ID, "login-button").click()

# === IVENTORY PAGE ===

# waiting for the iventory page to load and clicking on the add to cart button
addBtn = find_el(By.ID, "add-to-cart-sauce-labs-backpack", ec.element_to_be_clickable)
addBtn.click()
shopping_cart = find_el(By.CLASS_NAME, "shopping_cart_link", ec.element_to_be_clickable)
shopping_cart.click()

# === CART PAGE ===
checkoutBtn = find_el(By.ID, "checkout", ec.presence_of_element_located)
checkoutBtn.click()

# === CHECKOUT PAGE ===
first_name_field = find_el(By.ID, "first-name", ec.presence_of_element_located)
first_name_field.send_keys("fred")

last_name_field = find_el(By.ID, "last-name", ec.presence_of_element_located)
last_name_field.send_keys("grimmes")

zip_field = find_el(By.ID, "postal-code", ec.presence_of_element_located)
zip_field.send_keys("0302")

continue_btn = find_el(By.ID, "continue", ec.element_to_be_clickable)
continue_btn.click()

# === CHECKOUT OVERVIEW ===
finish_btn = find_el(By.ID, "finish", ec.element_to_be_clickable)
finish_btn.click()

time.sleep(20)