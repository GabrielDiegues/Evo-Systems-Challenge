from elements import TextInputElement
from locators import *
from base import BasePage, BaseElement, BaseItems
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    IVENTORY_URL = "https://www.saucedemo.com/inventory.html"
    user_name = TextInputElement(LoginPageLocators.USER_NAME_FIELD)
    password = TextInputElement(LoginPageLocators.PASSWORD_FIELD)

    
    def attempt_login(self, user_name):
        self.user_name = user_name
        self.password = "secret_sauce"
        self.click_button(LoginPageLocators.LOGIN_BTN, "Couldn't click on the login button")
        return self.check_url(self.IVENTORY_URL, True)

class InventoryPage(BaseItems):
    CART_URL = "https://www.saucedemo.com/cart.html"


    def attempt_add_product(self):
        items = self.find_items(
            InventoryPageLocators.INVENTORY_LIST,  
            "Couldn't access the iventory list"
            )
        for item in items:
            self.click_button(BaseLocators.PRODUCT_BTN, "Couldn't load the product button", item)

        self.click_button(InventoryPageLocators.SHOPPING_CART_BTN, "Couldn't load the cart button")
        return self.driver.current_url == self.CART_URL


class CartPage(BaseItems):
    CHECKOUT_STEP_ONE_URL = "https://www.saucedemo.com/checkout-step-one.html"

    def attempt_delete_product(self):
        items = self.find_items(
            CartPageLocators.CART_LIST,
            "Couldn't access the iventory list"
            )
        
        for i in range(len(items) // 2 - 1):
            self.click_button(BaseLocators.PRODUCT_BTN, "Couldn't load the delete button", items[i])
        
        self.click_button(CartPageLocators.CHECKOUT_BTN, "Couldn't load the checkout button")
        return self.driver.current_url == self.CHECKOUT_STEP_ONE_URL
    

class CheckoutOnePage(BasePage):
    CHECKOUT_STEP_TWO = "https://www.saucedemo.com/checkout-step-two.html"
    first_name = TextInputElement(CheckoutOneLocators.FIRST_NAME_FIELD)
    last_name = TextInputElement(CheckoutOneLocators.LAST_NAME_FIELD)
    postal_code = TextInputElement(CheckoutOneLocators.ZIP_FIELD)

    def attempt_fill_info(self):
        self.first_name = "Gabriel"
        self.last_name = "Rocha"
        self.postal_code = "0457"
        self.click_button(CheckoutOneLocators.CONTINUE_BTN, "Couldn't click on the continue button")
        return self.check_url(self.CHECKOUT_STEP_TWO, True)


class CheckoutTwoPage(BasePage):
    CHECKOUT_COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"


    def attempt_finish_order(self):
        self.click_button(CheckoutTwoLocators.FINISH_BTN, "Couldn't click on the finish button")
        return self.check_url(self.CHECKOUT_COMPLETE_URL)


class CheckoutCompletePage(BasePage):
    def is_order_complete(self):
        CONTAINER = BaseElement(CheckoutCompleteLocators.CONTAINER).find_el(
            self.driver, 
            ec.presence_of_element_located, 
            "Couldn't find Checkout complete container"
            )
        header_txt = BaseElement(CheckoutCompleteLocators.COMPLETE_HEADER).find_el(
            CONTAINER,
            ec.presence_of_element_located,
            "Couldn't find the confimation header message"
        )
        div_txt = BaseElement(CheckoutCompleteLocators.COMPLETE_TEXT).find_el(
            CONTAINER, ec.presence_of_element_located,
            "Couldn't find confirmation text message"
        )
        return bool(header_txt.text and div_txt.text)