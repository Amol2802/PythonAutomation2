import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver=webdriver.Chrome()   # luanch the chrome browser

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")   # eneter the url
#driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CLASS_NAME,"classone").send_keys("Amol")   # using Class Name


#driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()   # link text
#driver.find_element(By.PARTIAL_LINK_TEXT,"Inc").click()  # partial link text

time.sleep(10)


"""
totalLink:list[WebElement] =driver.find_elements(By.TAG_NAME,"a")  # using tagname
for x in totalLink:
      print(x.text)
      if(x.text=="OrangeHRM, Inc"):
            x.click()

time.sleep(10)

driver.find_element(By.NAME,"username").send_keys("Admin")  # enter the data in username field
time.sleep(2)
driver.find_element(By.NAME,"password").send_keys("admin123")  # enter the data in password field
time.sleep(2)
#driver.find_element(By.XPATH,"//button[@type='submit']").click()  # xpath
#driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()  # CSS Selector


#driver.close()   # close the BRowser
time.sleep(10)

"""
