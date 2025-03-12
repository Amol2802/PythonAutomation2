import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()   # luanch the chrome browser

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID,"alert1").click()
time.sleep(2)

# Alert Handle
driver.switch_to.alert.accept()   # accepting the alert
driver.switch_to.alert.dismiss()  # dismissing the alert
textBox2=driver.find_element(By.XPATH,"(//div[@class='widget-content']//textarea)[2]")
textBox2.send_keys("Automation Testing")

time.sleep(5)