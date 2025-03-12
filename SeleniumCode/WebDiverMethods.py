import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver=webdriver.Chrome()   # luanch the chrome browser

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
time.sleep(5)
# Check box selection
orangeCheckBox=driver.find_element(By.ID,"checkbox1")
print(orangeCheckBox.is_selected())
orangeCheckBox.click()

blueCheckBox=driver.find_element(By.ID,"checkbox2")
print(blueCheckBox.is_selected())
blueCheckBox.click()
print(blueCheckBox.is_selected())
time.sleep(5)
"""
textbox=driver.find_element(By.NAME,"lname")
print(textbox.is_enabled())

textBox2=driver.find_element(By.XPATH,"(//div[@class='widget-content']//textarea)[2]")
print(textBox2.is_enabled())
textBox2.send_keys("Testing completed")
time.sleep(5)

# radio button
female=driver.find_element(By.ID,"radio2")
female.click()
print(female.is_selected())    # check the element is selected or not on the page

texWeb=driver.find_element(By.XPATH,"//div[normalize-space(text())='This is a sample text in the Page One.']")
print(texWeb.is_displayed())    # check the element is dispaly/present or not on the page
print(texWeb.text)   # return the text

time.sleep(5)

print(driver.title)  # title method
time.sleep(5)

print(driver.current_url)  # get the current url
time.sleep(5)
driver.find_element(By.LINK_TEXT,"http://www.Selenium143.blogspot.com").click()
time.sleep(5)
#driver.quit()

driver.back()   # click navigation back button
time.sleep(4)
driver.forward()  # click navigation forward button
time.sleep(4)
driver.refresh()  # refreshing the page
time.sleep(4)
driver.quit()   # quiting/Close the all open browser
time.sleep(4)
"""
