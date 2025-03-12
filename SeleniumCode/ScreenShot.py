import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver=webdriver.Chrome()   # luanch the chrome browser

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

#driver.save_screenshot("C://Users/JAYA VYAWHARE/Documents/ScreenShots/hrm.png")
driver.get_screenshot_as_file("C://Users/JAYA VYAWHARE/Documents/ScreenShots/hrm2.png")
time.sleep(2)