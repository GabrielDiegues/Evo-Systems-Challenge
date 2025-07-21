from elements import TextInputElement
from locators import *
from base import BasePage, BaseElement, BaseItems
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    user_name = TextInputElement(LoginPageLocators.USER_NAME_FIELD)
    password = TextInputElement(LoginPageLocators.PASSWORD_FIELD)

    
    def attempt_login(self, user_name):
        self.user_name = user_name
        self.password = "secret_sauce"
        self.click_button(LoginPageLocators.LOGIN_BTN, "Couldn't click on the login button")
        return self.check_url("https://www.saucedemo.com/inventory.html", True)

class InventoryPage(BaseItems):

    def attempt_add_product(self):
        items = self.find_items(
            InventoryPageLocators.INVENTORY_LIST,  
            "Couldn't access the iventory list"
            )
        for item in items:
            self.click_button(BaseLocators.PRODUCT_BTN, "Couldn't load the product button", item)

        self.click_button(InventoryPageLocators.SHOPPING_CART_BTN, "Couldn't load the cart button")
        return self.driver.current_url == "https://www.saucedemo.com/cart.html"


class CartPage(BaseItems):
    def attempt_delete_product(self):
        items = self.find_items(
            CartPageLocators.CART_LIST,
            "Couldn't access the iventory list"
            )
        
        for i in range(len(items) // 2 - 1):
            self.click_button(BaseLocators.PRODUCT_BTN, "Couldn't load the delete button", items[i])
        
        self.click_button(CartPageLocators.CHECKOUT_BTN, "Couldn't load the checkout button")
        return self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
    

class CheckoutOnePage(BasePage):
    first_name = TextInputElement(CheckoutOneLocators.FIRST_NAME_FIELD)
    last_name = TextInputElement(CheckoutOneLocators.LAST_NAME_FIELD)
    postal_code = TextInputElement(CheckoutOneLocators.ZIP_FIELD)

    def attempt_fill_info(self):
        self.first_name = "Gabriel"
        self.last_name = "Rocha"
        self.postal_code = "0457"
        self.click_button(CheckoutOneLocators.CONTINUE_BTN, "Couldn't click on the continue button")
        return self.check_url("https://www.saucedemo.com/checkout-step-two.html", True)


class CheckoutTwoPage(BasePage):
    def attempt_finish_order(self):
        self.click_button(CheckoutTwoLocators.FINISH_BTN, "Couldn't click on the finish button")
        return self.check_url("https://www.saucedemo.com/checkout-complete.html")


class CheckoutCompletePage(BasePage, BaseElement):
    def is_order_complete(self):
        CONTAINER = BaseElement(CheckoutCompleteLocators.CONTAINER).find_el(
            self.driver, 
            ec.presence_of_element_located, 
            "Couldn't find Checkout complete container"
            )
        HEADER_TXT = BaseElement(CheckoutCompleteLocators.COMPLETE_HEADER).find_el(
            CONTAINER,
            ec.presence_of_element_located,
            "Couldn't find the confimation header message"
        )
        DIV_TXT = BaseElement(CheckoutCompleteLocators.COMPLETE_TEXT).find_el(
            CONTAINER, ec.presence_of_element_located,
            "Couldn't find confirmation text message"
        )
        return bool(HEADER_TXT.text and DIV_TXT.text)