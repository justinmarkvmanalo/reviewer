from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://jmvm.free.nf/teacherlogin.php")

txtUsername = driver.find_element(By.ID, "username")
txtUsername.send_keys("justin")
time.sleep(2)

txtPassword = driver.find_element(By.ID, "password")
txtPassword.send_keys("aHdbKh0")
time.sleep(2)

submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
submit_button.click()
time.sleep(10)