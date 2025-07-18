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
    PRODUCTS_BTN = (
        (By.ID, "add-to-cart-sauce-labs-backpack"), 
        (By.ID, "add-to-cart-sauce-labs-bike-light"),
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
        (By.ID, "add-to-cart-sauce-labs-onesie"),
        (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"),
        )


class CartPageLocators():
    CART_LIST = (By.CSS_SELECTOR, '[data-test="cart-list"]') 
    PRODUCTS_TO_REMOVE_BTN = (
        (By.ID, "remove-sauce-labs-backpack"),
        (By.ID, "remove-sauce-labs-bike-light"),
        (By.ID, "remove-sauce-labs-bolt-t-shirt")
        )
    CHECKOUT_BTN = (By.ID, "checkout")