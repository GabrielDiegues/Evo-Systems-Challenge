from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base import BasePage 
from base import BaseElement

class TextInputElement(BaseElement):
    def __set__(self, obj: BasePage, value: str):
        if not hasattr(obj, 'driver'):
            raise AttributeError("Expected 'driver' attribute in the object")
        
        TEXT_FIELD = self.find_el(obj.driver, ec.presence_of_element_located, "Failed to load the text field")
        if TEXT_FIELD:
            TEXT_FIELD.clear()
            TEXT_FIELD.send_keys(value)
