import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
@pytest.mark.parametrize("username, password",[("Amol12","Amol@12334"), ("Rahul12","Rahul@12334"), ("abc","abc@12334")])
def testlogin(username, password):
    print(username +"            "+ password)
"""

@pytest.mark.parametrize("username, password",[("standard_user","Amol@12334"), ("Rahul12","Rahul@12334"), ("standard_user","secret_sauce")])
def testloginBr(username, password):
    driver = webdriver.Chrome()  # luanch the chrome browser

    # driver.get("https://demo.guru99.com/selenium/newtours/index.php")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    uname = driver.find_element(By.ID, "user-name")
    uname.clear()
    uname.send_keys(username)

    passwd = driver.find_element(By.ID, "password")
    passwd.clear()
    passwd.send_keys(password)

    driver.find_element(By.ID, "login-button").click()
    time.sleep(4)
    
