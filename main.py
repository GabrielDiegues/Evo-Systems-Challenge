import unittest
from selenium import webdriver
import pages
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# === FUNCTION TO GENERATE TEST TO EACH SPECIFIC USER ===
def generate_test(user):
    def test(self):
        login_page = pages.LoginPage(self.driver)
        self.assertTrue(login_page.is_login_successful(user), f"Login failed for user: {user}")
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
    # def test_login(self):
    #     for user in self.ALL_USER_NAMES:
    #         login_page = pages.LoginPage(self.driver)
    #         self.assertTrue(login_page.is_login_successful(user), f"Login failed for user: {user}")


# === ADDING THE TEST FUNCTIONS TO THE SauceDemoTests class ===
for user in SauceDemoTests.ALL_USER_NAMES:
    test_name = f"test_login_with_{user}"
    test = generate_test(user)
    setattr(SauceDemoTests, test_name, test)


if __name__ == "__main__":
    unittest.main()