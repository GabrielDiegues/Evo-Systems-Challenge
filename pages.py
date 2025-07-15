from elements import TextInputElement
from locators import LoginPageLocators
from base import BasePage, BaseElement


class LoginPage(BasePage):
    user_name = TextInputElement(LoginPageLocators.USER_NAME_FIELD)
    password = TextInputElement(LoginPageLocators.PASSWORD_FIELD)



    def is_login_successful(self, user_name):
        try:
            self.user_name = user_name
            self.password = "secret_sauce"
            self.click_button(LoginPageLocators.LOGIN_BUTTON)
            return self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        except:
            return False