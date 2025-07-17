from elements import TextInputElement
from locators import LoginPageLocators, InventoryPageLocators, CartPageLocators
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
        # inventory_list = BaseElement(InventoryPageLocators.INVENTORY_LIST).find_el(
        #     self.driver, ec.presence_of_element_located, "couldn't access the iventory list"
        #     )
        # items = BaseElement(InventoryPageLocators.ITEM).find_el(
        #     inventory_list, 
        #     ec.presence_of_all_elements_located,
        #     "couldn't access the items",
        #     multiple=True
        #     )

        items = self.find_items(
            InventoryPageLocators.INVENTORY_LIST, 
            InventoryPageLocators.ITEM, 
            "Couldn't access the iventory list"
            )

        for item in items:
            self.click_button(InventoryPageLocators.PRODUCT_BTN, "Couldn't load the product button", item)

            # item_btn = BaseElement(InventoryPageLocators.PRODUCT_BTN).find_el(
            #     item, 
            #     ec.element_to_be_clickable, 
            #     "couldn't access the item button"
            #     )
            # item_btn.click()
            item_btn = BaseElement(InventoryPageLocators.PRODUCT_BTN).find_el(
                item, 
                ec.element_to_be_clickable, 
                "couldn't access the item button"
                )
            if item_btn.text.strip() == "Remove":
                CartPage.products_to_remove_btn.append((By.ID,item_btn.get_attribute("id")))

        self.click_button(InventoryPageLocators.SHOPPING_CART_BTN, "Couln't load the cart button")


        #
        # for product in InventoryPageLocators.PRODUCTS_BTN:
        #     self.click_button(product)
        # self.click_button(InventoryPageLocators.SHOPPING_CART_BTN)

        return self.driver.current_url == "https://www.saucedemo.com/cart.html"


class CartPage(BasePage):
    products_to_remove_btn = []
    def process_cart_step(self, product_buttons: tuple, next_step_button: tuple, url: str):
        for product in product_buttons:
            self.click_button(product, "Couldn't click on the product button")
        self.click_button(next_step_button, "couldn't click on the next step button")
        return self.driver.current_url == url