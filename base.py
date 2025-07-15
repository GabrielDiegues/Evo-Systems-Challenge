from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage():
    def __init__(self, driver: WebDriver):
        self.driver = driver
    

    def click_button(self, locator):
        BUTTON = BaseElement(locator).find_el(self.driver)
        if BUTTON:
            BUTTON.click()


class BaseElement:
    def __init__(self, locator: tuple):
        self.locator = locator


    def find_el(self, driver):
        try:
            return WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(self.locator)
            )
        except Exception as e:
            print(f"Exception detected:\n{e}\n")