import time
import unittest
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

class  LoginApplication(unittest.TestCase):

    def testlogin(self):
        """
        text=None
        driver = webdriver.Chrome()  # luanch the chrome browser
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        #https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
        driver.maximize_window()
        time.sleep(5)
        titleText=driver.title
        print(titleText)
        #self.assertEqual("Swag Labs",titleText,)
        #self.assertNotEqual("Swag Labs66",titleText)
        #self.assertTrue(titleText == "Swag Labs75")
        #self.assertFalse(titleText == "Swag Labs35")
        #self.assertIsNone(text)
        #self.assertIsNotNone(titleText)

        totalLink: list[WebElement] = driver.find_elements(By.TAG_NAME, "a")
        for x in totalLink:
            print(x.text)


        list=["Banana", "Apple", "Orange", "Graphs"]  # data structure list set tuple dic

        self.assertIn("Apple",list)
        #self.assertNotIn("Appleu53",list)
      """
        #Relation Comparison Assertion
        #self.assertGreater(50,50)
        #self.assertGreaterEqual(80,80)
        #self.assertLess(90,90)

        self.assertLessEqual(70,70)