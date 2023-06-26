
# pip install selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://sakshingp.github.io/assignment/login.html')

name = 'imvickykumar999'
xpath = driver.find_element(By.XPATH, '//*[@id="username"]')
xpath.send_keys(name)

xpath = driver.find_element(By.XPATH, '//*[@id="password"]')
xpath.send_keys(name)

xpath = driver.find_element(By.XPATH, '//*[@id="log-in"]')
xpath.click()
time.sleep(3)

xpath = driver.find_element(By.XPATH, '//*[@id="amount"]')
xpath.click()
time.sleep(10)
