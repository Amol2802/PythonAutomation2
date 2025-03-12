
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Windows.html")

driver.maximize_window()

driver.find_element(By.XPATH,"//div[@id='Tabbed']//button[1]").click()

parrentWindow=driver.current_window_handle  # current window  F235F07BA79DE6B6485240B635D3083F

print(parrentWindow)

multipleWindows=driver.window_handles

for id in multipleWindows:
    #print(id)
   driver.switch_to.window(id)
   print(driver.title)

   if "Selenium" ==driver.title :
       driver.find_element(By.XPATH,"//span[normalize-space(text())='Projects']").click()
       driver.close()

time.sleep(6)


