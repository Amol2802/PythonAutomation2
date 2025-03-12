import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()   # luanch the chrome browser

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
time.sleep(5)

fileup=driver.find_element(By.XPATH,"//input[@type='file']")

driver.execute_script("arguments[0].scrollIntoView();", fileup)
time.sleep(5)
# File upload
fileup.send_keys("C://Users//JAYA VYAWHARE//Documents//Book1.xlsx")

time.sleep(5)