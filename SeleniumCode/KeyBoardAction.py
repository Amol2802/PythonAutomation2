import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver=webdriver.Chrome()   # luanch the chrome browser

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.NAME,"username").send_keys("Admin")

act=ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.key_down(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.ENTER).perform()

time.sleep(5)