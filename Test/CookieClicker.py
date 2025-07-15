import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.action_chains import ActionChains

PATH = r"C:\Program Files\chromedriver-win64\chromedriver.exe"

options = Options()
options.add_argument("--incognito")
service = Service(PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://cookieclicker.eu/cookieclicker/")
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# === FUNCTIONS ===
def find_el(by: str, element_identifier: str, search_method):
    try:
        return WebDriverWait(driver, 10).until(
            search_method((by, element_identifier))
        )
    except Exception as e:
        print(f"Exception detected:\n{e}")
        sys.exit()

# === MAIN PROGRAM ===
find_el(By.ID, "langSelect-EN", ec.element_to_be_clickable).click()

cookie = find_el(By.ID, "bigCookie", ec.element_to_be_clickable)
items = [find_el(By.ID, f"productPrice{i}", ec.presence_of_element_located) for i in range(1, - 1, -1)]

actions = ActionChains(driver)
actions.click(cookie)
while True:
    actions.perform()
    cookies_count = int(find_el(By.ID, "cookies", ec.presence_of_element_located).text.split(" ")[0])
    for item in items:
        if cookies_count >= int(item.text):
            click_item = ActionChains(driver)
            click_item.click(item)
            click_item.perform()