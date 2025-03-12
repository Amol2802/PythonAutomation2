import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()

driver.get("https://www.sastasafar.com/flight-deal")

driver.maximize_window()
# by pixel
#driver.execute_script("window.scrollBy(0,1000)","")

# using Element
#google=driver.find_element(By.XPATH, "//img[contains(@class,'img-fluid d-none')]")

#driver.execute_script("arguments[0].scrollIntoView();", google)

#scroll bottom of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(10)
#scroll to Top of the page
driver.execute_script("window.scrollTo(0,0)")

time.sleep(10)