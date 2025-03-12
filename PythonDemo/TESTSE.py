"""
import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)
driver.find_element(By.ID,"email").send_keys("Amoll")
driver.find_element(By.ID,"pass").send_keys("Amohgtwdvgdll")
time.sleep(20)

"""