from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import BaseLocators, InventoryPageLocators
from selenium.webdriver.remote.webelement import WebElement
from typing import overload, Literal

class BasePage():
    def __init__(self, driver: WebDriver):
        self.driver = driver
    

    def click_button(self, locator: tuple, except_msg, element = None):
        element = element or self.driver
        BUTTON = BaseElement(locator).find_el(element, ec.element_to_be_clickable, except_msg)
        BUTTON.click()
    

    def get_warning_message(self):
        MSG = BaseElement(BaseLocators.WARNING_MESSAGE).find_el(
            self.driver, 
            ec.presence_of_element_located, 
            "Couldn't load the warning message"
            )
        return (MSG.text, False) if MSG else ("", False)
    

class BaseItems(BasePage):
    def find_items(self, available_items_locator: tuple, item_locator: tuple, except_message: str):
        available_items = BaseElement(available_items_locator).find_el(
            self.driver, ec.presence_of_element_located, except_message
            )
        items = BaseElement(item_locator).find_el(
            available_items, 
            ec.presence_of_all_elements_located,
            "couldn't access the items",
            multiple=True
            )
        
        return items

class BaseElement:
    def __init__(self, locator: tuple):
        self.locator = locator


    @overload
    def find_el(self, driver, search_method, exception_text, multiple: Literal[True]) -> list[WebElement]: ...

    @overload
    def find_el(self, driver, search_method, exception_text) -> WebElement: ...


    def find_el(self, driver, search_method, exception_text, multiple=False):
        try:
            return WebDriverWait(driver, 10).until(
                search_method(self.locator)
            )
        except Exception as e:
            print(exception_text)
            print(f"Exception detected:\n{e}\n")