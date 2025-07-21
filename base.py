from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import BaseLocators
from selenium.webdriver.remote.webelement import WebElement
from typing import overload, Literal
from typing import Callable

class BasePage():
    def __init__(self, driver: WebDriver):
        self.driver = driver
    

    def click_button(self, locator: tuple, except_msg: str, element = None):
        element = element or self.driver
        BUTTON = BaseElement(locator).find_el(element, ec.element_to_be_clickable, except_msg)
        BUTTON.click()
    

    def get_warning_message(self) -> tuple[str, bool]:
        msg = BaseElement(BaseLocators.WARNING_MESSAGE).find_el(
            self.driver, 
            ec.presence_of_element_located, 
            "Couldn't load the warning message"
            )
        return (msg.text, False) if msg else ("", False)
    

    @overload
    def check_url(self, url: str, warning: Literal[True]) -> tuple[str, bool]: ...

    @overload
    def check_url(self, url: str) -> bool: ...
        


    def check_url(self, url: str, warning = False):
        is_url_correct = self.driver.current_url == url
        if warning:
            return ("", True) if is_url_correct else self.get_warning_message()
        return is_url_correct
    

class BaseItems(BasePage):
    def find_items(self, available_items_locator: tuple, except_message: str):
        available_items_container = BaseElement(available_items_locator).find_el(
            self.driver, ec.presence_of_element_located, except_message
            )
        items = BaseElement(BaseLocators.ITEM).find_el(
            available_items_container, 
            ec.presence_of_all_elements_located,
            "couldn't access the items",
            multiple_el=True
            )
        
        return items

class BaseElement:
    def __init__(self, locator: tuple):
        self.locator = locator


    @overload
    def find_el(self, driver, search_method, exception_text, multiple_el: Literal[True]) -> list[WebElement]: ...

    @overload
    def find_el(self, driver, search_method, exception_text) -> WebElement: ...


    def find_el(self, driver: WebElement, search_method: Callable, exception_text: str, multiple_el=False):
        try:
            return WebDriverWait(driver, 10).until(
                search_method(self.locator)
            )
        except Exception as e:
            print(f"{exception_text}\n{e}")