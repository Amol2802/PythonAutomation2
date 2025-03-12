import time
from tkinter.tix import Select

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By

#from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()   # luanch the chrome browser

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
time.sleep(5)



dropDown=driver.find_element(By.ID,"drop1")
s= Select(dropDown)
#s.select_by_index(3)
#s.select_by_value("def")
s.select_by_visible_text("doc 4")

time.sleep(5)