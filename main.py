import unittest
from selenium import webdriver
import pages
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# === FUNCTION TO GENERATE TEST TO EACH SPECIFIC USER ===
def generate_test(user: str):
    def test(self: SauceDemoTests):
        print(f"Testing the user: {user}")
        # === LOGIN TEST ===
        login_page = pages.LoginPage(self.driver)
        warning_msg, login_result = login_page.attempt_login(user)
        self.validate_process(login_result, "login page", user, warning_msg)        
        # === IVENTORY TEST ===
        inventory_page = pages.InventoryPage(self.driver)
        self.validate_process(inventory_page.attempt_add_product(), "inventory", user)

        # === CART TEST ===
        cart_page = pages.CartPage(self.driver)
        self.validate_process(cart_page.attempt_delete_product(), "cart", user)

        # === CHECKOUT STEP ONE ===
        checkout_one = pages.CheckoutOnePage(self.driver)
        warning_msg, checkout_one_result = checkout_one.attempt_fill_info()
        self.validate_process(checkout_one_result, "checkout step one", user, warning_msg)

        # === CHECKOUT STEP TWO ===
        checkout_two = pages.CheckoutTwoPage(self.driver)
        self.validate_process(checkout_two.attempt_finish_order(), "checkout step two", user)

        # === CHECKOUT COMPLETE ===
        checkout_complete = pages.CheckoutCompletePage(self.driver)
        self.validate_process(checkout_complete.is_order_complete(), "checkout complete", user)
    return test

 # === TEST CLASS ===
class SauceDemoTests(unittest.TestCase):
    ALL_USER_NAMES = (
        "standard_user", 
        "locked_out_user", 
        "problem_user", 
        "performance_glitch_user", 
        "error_user", 
        "visual_user",
        )
    # === SETUP AND TEARDOWN FUNCTIONS ===
    def setUp(self):
        # chrome driver path (Change it to the path located on your computer)
        self.PATH = r"C:\Program Files\chromedriver-win64\chromedriver.exe"

        # === SETUP CHROME ===

        # setting the chrome to open a incognito window
        options = Options()
        options.add_argument("--incognito")

        # Setting up ChromeDriver to allow Selenium to control Google Chrome
        service = Service(self.PATH)
        self.driver = webdriver.Chrome(service=service, options=options)

        # Accessing the website
        self.driver.get("https://www.saucedemo.com/")


    def tearDown(self):
        self.driver.close()


    # === UTIL FUNCTIONS ===
    def validate_process(self, is_succedded: bool, page_name: str, user_name: str, warning_msg = ""):
        if warning_msg:
            warning_msg = f" (Warning message - {warning_msg})"
        self.assertTrue(is_succedded, f"Process failed at page: {page_name}. failed user: {user_name}{warning_msg}")
        

# === ADDING THE TEST FUNCTIONS TO THE SauceDemoTests class ===
for user in SauceDemoTests.ALL_USER_NAMES:
    test_name = f"test_login_with_{user}"
    test = generate_test(user)
    setattr(SauceDemoTests, test_name, test)


if __name__ == "__main__":
    unittest.main()