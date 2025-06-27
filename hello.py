import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector

def wait_and_find_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def create_record(driver, name, email):
    driver.get("http://localhost/create_record.php")
    time.sleep(2)

    name_input = wait_and_find_element(driver, By.NAME, "name")
    name_input.clear()
    name_input.send_keys(name)

    email_input = wait_and_find_element(driver, By.NAME, "email")
    email_input.clear()
    email_input.send_keys(email)

    submit_button = wait_and_find_element(driver, By.XPATH, "//input[@type='submit']")
    submit_button.click()
    time.sleep(2)

def verify_record_in_db(name, email):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = %s AND email = %s", (name, email))
    result = cursor.fetchone()
    conn.close()
    return result

def main():
    driver = webdriver.Chrome()

    try:
        # Create a new record
        name = "John Doe"
        email = "john.doe@example.com"
        create_record(driver, name, email)
        print("✅ Record created through web interface.")

        # Verify the record in the database
        record = verify_record_in_db(name, email)
        if record:
            print("✅ Record found in database:", record)
        else:
            print("⚠️ Record not found in database.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
