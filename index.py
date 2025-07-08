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
def find_element(by: str, element_identifier: str, search_method = ec.presence_of_element_located):
    try:
        return WebDriverWait(driver, 10).until(
            search_method((by, element_identifier))
        )
    except Exception as e:
        print(f"Exception detected:\n{e}")
        sys.exit()
# === LOGIN PAGE === 
# Filling the user name field
textInput = driver.find_element(By.ID, "user-name")
textInput.send_keys("standard_user")

# Filling the password field
textInput = driver.find_element(By.ID, "password")
textInput.send_keys("secret_sauce")

# Clicking on the login button
driver.find_element(By.ID, "login-button").click()

# === IVENTORY PAGE ===

# waiting for the iventory page to load and clicking on the add to cart button
addBtn = find_element(By.ID, "add-to-cart-sauce-labs-backpack", ec.element_to_be_clickable)
addBtn.click()
shopping_cart = find_element(By.CLASS_NAME, "shopping_cart_link", ec.element_to_be_clickable)
shopping_cart.click()

# try:
#     addBtn = WebDriverWait(driver, 10).until(
#         ec.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
#     )
#     addBtn.click()
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
# except:
#     print("Error while trying to click on the add to cart button")
#     sys.exit()

# === CART PAGE ===
try:
    checkoutBtn = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "checkout"))
    )
    checkoutBtn.click()
except:
    print("Error while trying to click on the checkout button")
    sys.exit()

# === CHECKOUT PAGE ===
try:
   # name field
   first_name_input = WebDriverWait(driver, 10).until(
       ec.presence_of_element_located((By.ID, "first-name"))
   )
   first_name_input.send_keys("fred")

   # last name field 
   last_name_input = WebDriverWait(driver, 10).until(
       ec.presence_of_element_located((By.ID, "last-name"))
   )
   last_name_input.send_keys("Grimmes")

   # Postal code field
   zip_input = WebDriverWait(driver, 10).until(
       ec.presence_of_element_located((By.ID, "postal-code"))
   )
   zip_input.send_keys("324")
   
   continue_btn = WebDriverWait(driver,10).until(
        ec.presence_of_element_located((By.ID, "continue"))
    )
   continue_btn.click()

except Exception as e:
    print(f"Error in the checkout page:\n${e}")
    sys.exit()

# === CHECKOUT OVERVIEW ===
try:
    root2 = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, "finish"))
    )
    root2.click()
except Exception as e:
    print(f"Error while clicking on the finish button:\n${e}")
    sys.exit()

time.sleep(20)