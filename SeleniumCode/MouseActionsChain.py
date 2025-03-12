import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()

driver.get("https://omayo.blogspot.com/")

driver.maximize_window()
time.sleep(2)
act=ActionChains(driver)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)
#ele=driver.find_element(By.XPATH,"//button[normalize-space(text())='Double click Here']")
# Double click
#act.double_click(ele).perform()

#buttoncheckthis=driver.find_element(By.XPATH,"//button[normalize-space(text())='Check this']")

# Right click
#act.context_click(buttoncheckthis).perform()

# mouse over action
blogs=driver.find_element(By.ID,"blogsmenu")
linkselenum143=driver.find_element(By.LINK_TEXT,"Selenium143")

act.move_to_element(blogs).move_to_element(linkselenum143).click().perform()
time.sleep(6)