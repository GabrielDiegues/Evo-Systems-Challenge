import unittest
from selenium import webdriver
import pages
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from locators import CartPageLocators, InventoryPageLocators
# === FUNCTION TO GENERATE TEST TO EACH SPECIFIC USER ===
def generate_test(user: str):
    def test(self):
        print(f"Testing the user: {user}")
        # === LOGIN TEST ===
        login_page = pages.LoginPage(self.driver)
        warning_msg, login_result = login_page.attempt_login(user)
        self.assertTrue(login_result, f"Login failed for user: {user} (Warning message - {warning_msg})")
        
        # === IVENTORY TEST ===
        inventory_page = pages.InventoryPage(self.driver)
        self.assertTrue(inventory_page.attempt_add_product(), f"navigation to the cart failed for user: {user}")
        # self.assertTrue(inventory_page.process_cart_step(InventoryPageLocators.PRODUCTS_BTN, 
        #                                                 InventoryPageLocators.SHOPPING_CART_BTN, 
        #                                                 "https://www.saucedemo.com/cart.html"
        #                                                 ), 
        #                                                 f"navigation to the cart failed for user: {user}")

        # === CART TEST ===
        # self.assertTrue(iventory_page.process_cart_step(CartPageLocators.PRODUCTS_TO_REMOVE_BTN, 
        #                                                 CartPageLocators.CHECKOUT_BTN, 
        #                                                 "https://www.saucedemo.com/checkout-step-one.html"
        #                                                 ),
        #                                                 f"navigation to the checkout-step-one failed for user: {user}")
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
        # chrome driver path
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

    
    # === TEST FUNCTIONS ===
    # @unittest.skip("")
    # def test_login(self):
    #     user = ""
    #     login_page = pages.LoginPage(self.driver)
    #     warning_msg, login_result = login_page.attempt_login(user)
    #     self.assertTrue(login_result, f"Login failed for user: {user} (Warning message - {warning_msg})")

# === ADDING THE TEST FUNCTIONS TO THE SauceDemoTests class ===
for user in SauceDemoTests.ALL_USER_NAMES:
    test_name = f"test_login_with_{user}"
    test = generate_test(user)
    setattr(SauceDemoTests, test_name, test)


if __name__ == "__main__":
    unittest.main()