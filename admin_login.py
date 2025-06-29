from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://localhost/ocss/admin_login.php")

# Admin Login
driver.find_element(By.NAME, "admin_username").send_keys("admin")
time.sleep(1)
driver.find_element(By.NAME, "admin_pass").send_keys("admin")
time.sleep(1)
driver.find_element(By.NAME, "admin_login").click()
time.sleep(2)

# Open menu and modal
driver.find_element(By.ID, "menu").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'a[data-target="#facultyModal"]').click()
time.sleep(2)

# User Registration
# Valid Entry
driver.find_element(By.NAME, "emp_number").send_keys("EMP12345")
driver.find_element(By.NAME, "fname").send_keys("Dela Cruz, Juan M.")
date_field = driver.find_element(By.NAME, "date_hired")
driver.execute_script("arguments[0].type = 'date'; arguments[0].value = '2023-06-15';", date_field)
driver.find_element(By.NAME, "status").send_keys("Full-time Faculty")
driver.find_element(By.NAME, "background_field").send_keys("Computer Science")
driver.find_element(By.NAME, "address").send_keys("123 Tech Street")
driver.find_element(By.NAME, "contact_no").send_keys("09171234567")
driver.find_element(By.NAME, "email").send_keys("juan.delacruz@example.com")
driver.find_element(By.NAME, "pass").send_keys("SecurePass123")
driver.execute_script("arguments[0].click();", driver.find_element(By.NAME, "register_faculty"))
time.sleep(2)

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("ALERT TEXT:", alert.text)
    alert.accept()
    print("Alert closed successfully.")
except:
    print("No alert appeared after duplicate entry.")

# Duplicate Entry
driver.find_element(By.ID, "menu").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'a[data-target="#facultyModal"]').click()
time.sleep(2)

driver.find_element(By.NAME, "emp_number").send_keys("EMP12345")
driver.find_element(By.NAME, "fname").send_keys("Dela Cruz, Juan M.")
date_field = driver.find_element(By.NAME, "date_hired")
driver.execute_script("arguments[0].type = 'date'; arguments[0].value = '2023-06-15';", date_field)
driver.find_element(By.NAME, "status").send_keys("Full-time Faculty")
driver.find_element(By.NAME, "background_field").send_keys("Computer Science")
driver.find_element(By.NAME, "address").send_keys("123 Tech Street")
driver.find_element(By.NAME, "contact_no").send_keys("09171234567")
driver.find_element(By.NAME, "email").send_keys("juan.delacruz@example.com")
driver.find_element(By.NAME, "pass").send_keys("SecurePass123")
driver.execute_script("arguments[0].click();", driver.find_element(By.NAME, "register_faculty"))
time.sleep(2)

# JavaScript alert if it show pops up
try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("ALERT TEXT:", alert.text)
    alert.accept()
    print("Alert closed successfully.")
except:
    print("No alert appeared after duplicate entry.")


# invalid email Entry
driver.find_element(By.ID, "menu").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'a[data-target="#facultyModal"]').click()
time.sleep(2)

driver.find_element(By.NAME, "emp_number").send_keys("test001")
driver.find_element(By.NAME, "fname").send_keys("Test User")
date_field = driver.find_element(By.NAME, "date_hired")
driver.execute_script("arguments[0].type = 'date'; arguments[0].value = '2023-06-15';", date_field)
driver.find_element(By.NAME, "status").send_keys("Full-time Faculty")
driver.find_element(By.NAME, "background_field").send_keys("Physics")
driver.find_element(By.NAME, "address").send_keys("456 Science Ave")
driver.find_element(By.NAME, "contact_no").send_keys("09918200288")
driver.find_element(By.NAME, "email").send_keys("invalid email")
driver.find_element(By.NAME, "pass").send_keys("SecurePass123")
driver.execute_script("arguments[0].click();", driver.find_element(By.NAME, "register_faculty"))
time.sleep(2)

email_input = driver.find_element(By.NAME, "email")
email_input.clear()
driver.find_element(By.NAME, "email").send_keys("test.user@example.com")
time.sleep(2)
driver.execute_script("arguments[0].click();", driver.find_element(By.NAME, "register_faculty"))

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("ALERT TEXT:", alert.text)
    alert.accept()
    print("Alert closed successfully.")
except:
    print("No alert appeared after duplicate entry.")


# Data Management
# Test the addition of subjects, 
driver.find_element(By.ID, "menu").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'a[data-target="#subjectModal"]').click()
time.sleep(2)

driver.find_element(By.NAME, "subject_code").send_keys("OMP 2090")
driver.find_element(By.NAME, "subject_description").send_keys("College Algebra")
driver.find_element(By.NAME, "unit").send_keys("3")
driver.find_element(By.NAME, "lecture").send_keys("2")
driver.find_element(By.NAME, "laboratory").send_keys("2")
driver.execute_script("arguments[0].click();", driver.find_element(By.NAME, "add"))

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("ALERT TEXT:", alert.text)
    alert.accept()
    print("Alert closed successfully.")
except:
    print("No alert appeared after duplicate entry.")

# Test the addition of rooms, 
driver.find_element(By.ID, "menu").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'a[data-target="#roomModal"]').click()
time.sleep(2)

driver.find_element(By.NAME, "room").send_keys("107")
driver.execute_script("arguments[0].click();", driver.find_element(By.NAME, "add_room"))

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("ALERT TEXT:", alert.text)
    alert.accept()
    print("Alert closed successfully.")
except:
    print("No alert appeared after duplicate entry.")

# schedule
driver.find_element(By.ID, "menu").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'a[href="create_schedule.php"]').click()
time.sleep(2)

# Select subject description
desc = driver.find_element(By.ID, "subject_description")
desc.click()
time.sleep(1)
number = driver.find_element(By.ID, "4")
number.click()
time.sleep(1)

# Select day
day = driver.find_element(By.ID, "day_description")
day.click()
time.sleep(1)
select_day = driver.find_element(By.ID, "day_11")
select_day.click()
time.sleep(1)

# Select time
time_dropdown = driver.find_element(By.ID, "time_description")
time_dropdown.click()
time.sleep(1)
select_time = driver.find_element(By.ID, "time_2")
select_time.click()
time.sleep(1)

# Select room
room_dropdown = driver.find_element(By.ID, "room_description")
room_dropdown.click()
time.sleep(1)
select_room = driver.find_element(By.ID, "room_3")
select_room.click()
time.sleep(1)

# Select prof
professor = driver.find_element(By.ID, "fname")
professor.click()
time.sleep(1)
select_prof = driver.find_element(By.ID, "faculty_33")
select_prof.click()
time.sleep(1)

driver.find_element(By.NAME, "add_schedule").click()
time.sleep(2)

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("ALERT TEXT:", alert.text)
    alert.accept()
    print("Alert closed successfully.")
except:
    print("No alert appeared after duplicate entry.")

time.sleep(5)
driver.quit()