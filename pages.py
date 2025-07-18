from elements import TextInputElement
from locators import LoginPageLocators, InventoryPageLocators, CartPageLocators, BaseLocators
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
        return ("", True) if self.driver.current_url == "https://www.saucedemo.com/inventory.html" else self.get_warning_message()


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
    # Delete this function
    def process_cart_step(self, product_buttons: tuple, next_step_button: tuple, url: str):
        for product in product_buttons:
            self.click_button(product, "Couldn't click on the product button")
        self.click_button(next_step_button, "couldn't click on the next step button")
        return self.driver.current_url == url