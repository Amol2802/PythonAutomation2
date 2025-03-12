import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import ExcelUtility

driver=webdriver.Chrome()   # luanch the chrome browser

#driver.get("https://demo.guru99.com/selenium/newtours/index.php")
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

time.sleep(2)
path="C:\\Users\JAYA VYAWHARE\Documents\Book1.xlsx"

rows=ExcelUtility.getRowCount(path)
print(rows)
column=ExcelUtility.getColumnCount(path)
print(column)

for r in range(2,rows+1):
    userName=ExcelUtility.readData(path,r,1)
    password=ExcelUtility.readData(path,r,2)
    uname = driver.find_element(By.ID, "user-name")
    uname.clear()
    uname.send_keys(userName)

    passwd = driver.find_element(By.ID, "password")
    passwd.clear()
    passwd.send_keys(password)

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)


    #product=driver.find_element(By.XPATH,"//span[normalize-space(text())='Products']")
    if driver.current_url=="https://www.saucedemo.com/inventory.html":
        ExcelUtility.writeData(path,r,3,"Passed")
    else:
        ExcelUtility.writeData(path, r, 3, "Failed")