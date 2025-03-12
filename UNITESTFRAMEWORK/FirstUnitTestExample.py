import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login (unittest.TestCase):

     def test_launchAppAutomationtesting(self):
         self.driver = webdriver.Chrome()
         self.driver.get("https://demo.automationtesting.in/Windows.html")
         self.driver.maximize_window()
         print(self.driver.title)

     def test_launchAppOmayo(self):
         self.driver = webdriver.Chrome()
         self.driver.get("https://omayo.blogspot.com/")
         self.driver.maximize_window()
         print(self.driver.title)

if __name__== "__main__":
    unittest.main()
