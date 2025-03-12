import time
import unittest
from itertools import product

from selenium import webdriver
from selenium.webdriver.common.by import By
"""
# Declare the global driver variable
driver = None

# Setup for the module (called once before any tests in the module)
def setUpModule():
    global driver
    print("Setup Module: setUpModule() - This runs once before any tests in the module.")
    # Initialize the WebDriver and set it as global
    driver = webdriver.Chrome()
    driver.maximize_window()

# Teardown for the module (called once after all tests in the module)
def tearDownModule():
    global driver
    print("Teardown Module: tearDownModule() - This runs once after all tests in the module.")
    driver.quit()
"""

class useOfSetupAndTearDown(unittest.TestCase):

    # Setup for the module (called once before any tests in the module)
    @classmethod
    def setUpClass(cls):
        print("Setup Module: setUpClass() - This runs once before the tests in the module.")
        # Initialize the web driver
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    # Teardown for the module (called once after all tests in the module)
    @classmethod
    def tearDownClass(cls):
        print("Teardown Module: tearDownClass() - This runs once after the tests in the module.")
        cls.driver.quit()

    # Setup for each individual test (called before each test)
    def setUp(self):
        print("Setup Test: setUp() - This runs before every individual test.")
        self.driver.get("https://www.saucedemo.com/")

    # Teardown for each individual test (called after every test)
    def tearDown(self):
        print("Teardown Test: tearDown() - This runs after every individual test.")
        # You can perform additional checks here if needed

    def test_HomePage(self):
        print("Test: test_title() - Verifying page title", self.driver.title)
        self.assertEqual(self.driver.title, 'Swag Labs')

    # verify title test case
    def test_title(self):
        print("Test: test_url() - Verifying page title",self.driver.title)

        self.assertEqual(self.driver.title, 'Swag Labs')

    # verify Login test case
    def test_Login(self):
        print("login the application")
        uname = self.driver.find_element(By.ID, "user-name")
        uname.clear()
        uname.send_keys("standard_user")

        passwd = self.driver.find_element(By.ID, "password")
        passwd.clear()
        passwd.send_keys("secret_sauce")

        self.driver.find_element(By.ID, "login-button").click()
        productText = self.driver.find_element(By.XPATH, "//span[normalize-space(text())='Products']")
        time.sleep(2)
        self.assertTrue(productText.is_displayed())


# Setup for the module (called once before any tests in the module)
def setUpModule():
    print("Setup Module: setUpModule() - This runs once before any tests in the module.")


# Teardown for the module (called once after all tests in the module)
def tearDownModule():
    print("Teardown Module: tearDownModule() - This runs once after all tests in the module.")


if __name__ == '__main__':
    unittest.main()
