import time
from idlelib.browser import browseable_extension_blocklist
from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

brower=input("Please Enter the Browsername")
#driver=webdriver.Chrome()
#driver=webdriver.Firefox()
#driver=webdriver.Edge()

if  brower=="Chrome":
    driver = webdriver.Chrome()
elif brower=="Firefoxe":
    driver = webdriver.Firefox()
else:
    driver = webdriver.Edge()

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()
time.sleep(2)
act=ActionChains(driver)

sorce=driver.find_element(By.XPATH,"//div[@id='DHTMLgoodies_dragableElement6']/following-sibling::div[1]")
time.sleep(2)
target=driver.find_element(By.XPATH,"//div[normalize-space(text())='Italy']")

# Drap and Drop
act.drag_and_drop(sorce,target).perform()
time.sleep(7)

driver.close()