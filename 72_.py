# Exercise 72:
# Create a script that let the user type in a search term and opens and search on the browser for that term on Google


# https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python&form=
# Automate Microsoft Edge


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get('https://www.google.com/')
driver.maximize_window()

element = driver.find_element(By.CLASS_NAME, 'gLFyf')
time.sleep(10)
element.send_keys('tomato types')
element.submit()

time.sleep(30)
driver.quit()

# #cool! This works :) 



