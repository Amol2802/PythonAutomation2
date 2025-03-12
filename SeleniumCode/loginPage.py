import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()   # luanch the chrome browser

driver.get("https://demo.automationtesting.in/Register.html")   # eneter the url

driver.maximize_window()   # Maximaze the BR
time.sleep(2)

driver.find_element(By.XPATH,"//span[@aria-labelledby='select2-country-container']").click()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("Japan")
time.sleep(2)

driver.find_element(By.XPATH,"//ul[@aria-hidden='false']//li[1]").click()

time.sleep(10)

"""
driver.find_element(By.ID,"user-name").send_keys("standard_user")  # enter the data in username field
time.sleep(2)
driver.find_element(By.ID,"password").send_keys("secret_sauce")  # enter the data in password field
time.sleep(2)
driver.find_element(By.ID,"login-button").click()  # click on login button
driver.close()   # close the BRowser
time.sleep(10)   # wait time for 10 sec.
"""