import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()   # luanch the chrome browser

driver.get("https://omayo.blogspot.com/")   # eneter the url
driver.maximize_window()

time.sleep(2)
driver.switch_to.frame("iframe1")     # switch to 1st frame
time.sleep(2)

driver.find_element(By.LINK_TEXT,"Google+").click()
time.sleep(4)

driver.switch_to.default_content()    # switch to your main page
time.sleep(4)
driver.switch_to.frame("iframe2")    # switch to 2nd frame
time.sleep(4)
driver.find_element(By.LINK_TEXT,"Google+").click()

driver.switch_to.parent_frame()    #  # switch to parrent frame

time.sleep(15)