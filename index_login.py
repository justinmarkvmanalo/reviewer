from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost/ocss/index.php")

txtUsername = driver.find_element(By.NAME, "user_email")
txtUsername.send_keys("test.user@example.com")
time.sleep(2)

txtPassword = driver.find_element(By.NAME, "user_pass")
txtPassword.send_keys("SecurePass123")
time.sleep(2)

submit_button = driver.find_element(By.NAME, "Login")
submit_button.click()
time.sleep(10)

driver.quit()