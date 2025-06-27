from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
import time
import unittest
import random

class DemoBlazeAutomation(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.demoblaze.com/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        
        self.rand_num = random.randint(1000, 9999)
        self.username = f"johncarlo{self.rand_num}"
        self.password = "test123"
    
    def tearDown(self):
        self.driver.quit()
    
    def test_complete_workflow(self):
        try:
            self.signup_user()
            
            self.login_user()
            
            self.navigate_site()
            
            self.logout_user()
            
            print("Automation Completed.")
            
        except Exception as e:
            self.fail(f"Complete workflow test failed: {str(e)}")
    
    def signup_user(self):
        print(f"Signing up user: {self.username}")
        
        # Click signup button
        signup_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "signin2")))
        signup_btn.click()
        
        # Wait for modal to appear and fill registration form
        username_field = self.wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))
        username_field.clear()
        username_field.send_keys(self.username)
        
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "sign-password")))
        password_field.clear()
        password_field.send_keys(self.password)
        
        # Submit form
        signup_submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign up')]")))
        signup_submit.click()
        
        # Handle alert
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Signup alert: {alert_text}")
            alert.accept()
            
            # Check if registration was successful
            self.assertIn("Sign up successful", alert_text)
            print("✓ Signup successful!")
            
            # Wait a moment for modal to close
            time.sleep(1)
            
        except TimeoutException:
            self.fail("No alert appeared after signup attempt")
    
    def login_user(self):
        print(f"Logging in user: {self.username}")
        
        # Click login button
        login_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "login2")))
        login_btn.click()
        
        # Wait for modal to appear and fill login form
        username_field = self.wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
        username_field.clear()
        username_field.send_keys(self.username)
        
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "loginpassword")))
        password_field.clear()
        password_field.send_keys(self.password)
        
        # Submit form
        login_submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Log in')]")))
        login_submit.click()
        
        # Verify login success
        welcome_msg = self.wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
        self.assertIn(f"Welcome {self.username}", welcome_msg.text)
        print("✓ Login successful!")
    
    def navigate_site(self):
        print("Navigating through site categories...")
        
        # Navigate to Phones category
        print("→ Navigating to Phones")
        phones_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Phones")))
        phones_link.click()
        
        # Wait for page to load and verify phones page
        time.sleep(2)
        product = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Samsung galaxy s6")))
        self.assertTrue(product.is_displayed())
        print("✓ Phones category loaded")
        
        # Navigate to Laptops category
        print("→ Navigating to Laptops")
        laptops_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Laptops")))
        laptops_link.click()
        
        # Wait for page to load and verify laptops page
        time.sleep(2)
        product = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sony vaio i5")))
        self.assertTrue(product.is_displayed())
        print("✓ Laptops category loaded")
        
        # Navigate to Monitors category
        print("→ Navigating to Monitors")
        monitors_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Monitors")))
        monitors_link.click()
        
        # page to load monitors
        time.sleep(2)
        product = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Apple monitor 24")))
        self.assertTrue(product.is_displayed())
        print("✓ Monitors category loaded")
        
        # Navigate back to Home
        print("→ Navigating back to Home")
        time.sleep(1)
        home_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text(🙁'Home '] | //a[text(🙁'Home']")))
        home_link.click()
        time.sleep(2)
        print("✓ Home page loaded")
    
    def logout_user(self):
        print("Logging out user...")
        logout_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "logout2")))
        print("Logout button found, clicking...")
        logout_btn.click()
        print("Clicked logout, waiting for login button to reappear...")
        login_btn = self.wait.until(EC.visibility_of_element_located((By.ID, "login2")))
        self.assertTrue(login_btn.is_displayed())
        print("✓ Logout successful!")

if _name_ == "_main_":
    suite = unittest.TestSuite()
    suite.addTest(DemoBlazeAutomation("test_complete_workflow"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
John Carlo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Generate a unique username for each run
username = f"Robert{random.randint(1000,9999)}"
password = "Robert123"

# Start the browser
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# 1. Go to Parabank registration page
print("Navigating to Parabank registration page...")
driver.get("https://parabank.parasoft.com/parabank/register.htm")
time.sleep(1)

# 2. Fill out the registration form with human-like typing
first_name_elem = wait.until(EC.presence_of_element_located((By.ID, "customer.firstName")))
first_name_elem.send_keys("Robert")
time.sleep(0.7)

last_name_elem = driver.find_element(By.ID, "customer.lastName")
last_name_elem.send_keys("Macalam")
time.sleep(0.7)

address_elem = driver.find_element(By.ID, "customer.address.street")
address_elem.send_keys("Road Street")
time.sleep(0.7)

city_elem = driver.find_element(By.ID, "customer.address.city")
city_elem.send_keys("Manila")
time.sleep(0.7)

state_elem = driver.find_element(By.ID, "customer.address.state")
state_elem.send_keys("NCR")
time.sleep(0.7)

zip_elem = driver.find_element(By.ID, "customer.address.zipCode")
zip_elem.send_keys("5432")
time.sleep(0.7)

phone_elem = driver.find_element(By.ID, "customer.phoneNumber")
phone_elem.send_keys("09090457982")
time.sleep(0.7)

ssn_elem = driver.find_element(By.ID, "customer.ssn")
ssn_elem.send_keys("123-45-6789")
time.sleep(0.7)

username_elem = driver.find_element(By.ID, "customer.username")
username_elem.send_keys(username)
time.sleep(0.7)

password_elem = driver.find_element(By.ID, "customer.password")
password_elem.send_keys(password)
time.sleep(0.7)

repeat_password_elem = driver.find_element(By.ID, "repeatedPassword")
repeat_password_elem.send_keys(password)
time.sleep(0.7)

# Submit registration
print(f"Registering new user: {username}")
driver.find_element(By.XPATH, '//input[@value="Register"]').click()
time.sleep(1)

# Wait for registration confirmation
wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Your account was created successfully")]')))
print("Registration successful!")
time.sleep(1)

# 3. Log out if automatically logged in
try:
    logout_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log Out")))
    time.sleep(0.5)
    logout_link.click()
    print("Logged out after registration.")
except:
    print("Not logged in after registration, continuing...")

time.sleep(1)

# 4. Go to login page
print("Navigating to login page...")
driver.get("https://parabank.parasoft.com/parabank/index.htm")
time.sleep(1)

# 5. Log in with the new user
username_login_elem = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username_login_elem.send_keys(username)
time.sleep(0.7)

password_login_elem = driver.find_element(By.NAME, "password")
password_login_elem.send_keys(password)
time.sleep(0.7)
driver.find_element(By.XPATH, '//input[@value="Log In"]').click()
time.sleep(1)

# 6. Wait for account overview page
wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Accounts Overview")]')))
print("Logged in and navigated to Accounts Overview page!")

# 7. Click the first account number to view account details
account_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "activity.htm?id=")]')))
account_link.click()
print("Viewed account details.")
time.sleep(2)

# 8. Go to 'Transfer Funds'
driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
print("Navigated to Transfer Funds page.")
time.sleep(2)

# Fill out transfer form
amount_elem = wait.until(EC.presence_of_element_located((By.ID, "amount")))
amount_elem.send_keys("100")
time.sleep(0.7)
from_account = driver.find_element(By.ID, "fromAccountId")
to_account = driver.find_element(By.ID, "toAccountId")
from_account.click()
to_account.click()
driver.find_element(By.XPATH, '//input[@value="Transfer"]').click()
print("Submitted a fund transfer.")
time.sleep(2)

# 9. Go to 'Request Loan'
driver.find_element(By.LINK_TEXT, "Request Loan").click()
print("Navigated to Request Loan page.")
time.sleep(2)

# Fill out loan form
loan_elem = wait.until(EC.presence_of_element_located((By.ID, "amount")))
loan_elem.send_keys("500")
time.sleep(0.7)
down_elem = driver.find_element(By.ID, "downPayment")
down_elem.send_keys("50")
time.sleep(0.7)
driver.find_element(By.XPATH, '//input[@value="Apply Now"]').click()
print("Submitted a loan request.")
time.sleep(2)

# 10. Log out
driver.find_element(By.LINK_TEXT, "Log Out").click()
print("Logged out.")
time.sleep(1)

time.sleep(2)
driver.quit()
print("Automation complete.")
