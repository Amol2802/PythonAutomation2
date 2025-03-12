import time

from selenium.common import ElementNotVisibleException
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

# implicitly_wait
driver.implicitly_wait(4)


#Explicite wait
wait=WebDriverWait(driver,10)
wait.until(ec.visibility_of_element_located((By.ID , "ta1")))

driver.find_element(By.ID, "ta1").send_keys("Automation")

wait.until(ec.presence_of_element_located((By.ID , "radio1")))

driver.find_element(By.ID, "radio1").click()

driver.find_element(By.XPATH,"//input[@class='gsc-input']").send_keys()
driver.find_element(By.XPATH, "//input[@class='gsc-search-button']").click()

wait.until(ec.presence_of_element_located((By.XPATH , "(//div[@class='status-msg-wrap']//div)[1]")))


"""
#Fluient wait or Polling Wait
wait=WebDriverWait(driver,20, 4, ignored_exceptions=[ElementNotVisibleException])
wait.until(ec.visibility_of_element_located((By.ID , "ta1")))

"""