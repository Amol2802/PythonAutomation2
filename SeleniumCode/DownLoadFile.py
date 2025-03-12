import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()   # luanch the chrome browser

driver.get("https://sourceforge.net/projects/geckodriver.mirror/files/latest/download")
time.sleep(4)
driver.maximize_window()
time.sleep(4)

driver.find_element(By.XPATH,"//a[normalize-space(text())='Download']").click()

time.sleep(10)