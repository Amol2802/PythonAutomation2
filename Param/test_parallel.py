import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def testloginBr1():
    driver = webdriver.Chrome()  # luanch the chrome browser

    # driver.get("https://demo.guru99.com/selenium/newtours/index.php")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    uname = driver.find_element(By.ID, "user-name")
    uname.clear()
    uname.send_keys("amol vd")

    passwd = driver.find_element(By.ID, "password")
    passwd.clear()
    passwd.send_keys("bvvadv")

    driver.find_element(By.ID, "login-button").click()
    time.sleep(4)

def testloginBr2():
    driver = webdriver.Chrome()  # luanch the chrome browser

    # driver.get("https://demo.guru99.com/selenium/newtours/index.php")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    uname = driver.find_element(By.ID, "user-name")
    uname.clear()
    uname.send_keys("tyvavd")

    passwd = driver.find_element(By.ID, "password")
    passwd.clear()
    passwd.send_keys(" bmgjxsgf")

    driver.find_element(By.ID, "login-button").click()
    time.sleep(4)

def testloginBr3():
    driver = webdriver.Chrome()  # luanch the chrome browser

    driver.get("https://demo.guru99.com/selenium/newtours/index.php")

    driver.maximize_window()


def testloginBr4():
    driver = webdriver.Chrome()  # luanch the chrome browser

    driver.get("https://demo.automationtesting.in/Windows.html")

    driver.maximize_window()