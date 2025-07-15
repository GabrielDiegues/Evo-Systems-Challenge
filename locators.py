# Allows you decide how you are going to search for the element in the page
from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_BUTTON = (By.ID, "login-button")
    USER_NAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")