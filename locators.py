# Allows you decide how you are going to search for the element in the page
from selenium.webdriver.common.by import By

class BaseLocators():
    WARNING_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')
    ITEM = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
    PRODUCT_BTN = (By.TAG_NAME, "button")

class LoginPageLocators():
    LOGIN_BTN = (By.ID, "login-button")
    USER_NAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")


class InventoryPageLocators():
    INVENTORY_LIST = (By.CSS_SELECTOR, '[data-test="inventory-list"]')
    SHOPPING_CART_BTN = (By.CLASS_NAME, "shopping_cart_link")


class CartPageLocators():
    CART_LIST = (By.CSS_SELECTOR, '[data-test="cart-list"]') 
    CHECKOUT_BTN = (By.ID, "checkout")


class CheckoutOneLocators():
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    ZIP_FIELD = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")


class CheckoutTwoLocators():
    FINISH_BTN = (By.ID, "finish")


class CheckoutCompleteLocators():
    CONTAINER = (By.ID, "checkout_complete_container")
    COMPLETE_HEADER = (By.CSS_SELECTOR, '[data-test="complete-header"]')
    COMPLETE_TEXT = (By.CSS_SELECTOR, '[data-test="complete-text"]')