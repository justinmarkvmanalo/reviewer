from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import os
from datetime import datetime

class TestResult:
    def __init__(self, test_id, description, expected, actual, status, details="", screenshot_path=""):
        self.test_id = test_id
        self.description = description
        self.expected = expected
        self.actual = actual
        self.status = status
        self.details = details
        self.screenshot_path = screenshot_path
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class OdinProjectTest:
    def __init__(self):
        self.driver = None
        self.setup_driver()
        self.wait = WebDriverWait(self.driver, 10)
        self.test_results = []
        self.screenshot_dir = self.create_screenshot_directory()
    
    def create_screenshot_directory(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = f"test_screenshots_{timestamp}"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        return screenshot_dir
    
    def setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
    
    
    def logout_if_logged_in(self):
        """Logout if user is currently logged in to ensure clean state"""
        try:
           
            logout_selectors = [
                "//a[contains(text(), 'Log out')]",
                "//a[contains(text(), 'Logout')]",
                "//a[contains(@href, 'logout')]",
                "//a[contains(@href, 'sign_out')]",
                "//button[contains(text(), 'Log out')]",
                "//button[contains(text(), 'Logout')]"
            ]
            
            for selector in logout_selectors:
                try:
                    logout_element = self.driver.find_element(By.XPATH, selector)
                    logout_element.click()
                    time.sleep(2)
                    print("Successfully logged out")
                    return True
                except NoSuchElementException:
                    continue
            
            
            self.driver.delete_all_cookies()
            time.sleep(1)
            return True
            
        except Exception as e:
            print(f"Logout attempt failed: {str(e)}")
            return False
    
    
    def take_screenshot(self, test_id, description=""):
        try:
            timestamp = datetime.now().strftime("%H%M%S")
            filename = f"{test_id}_{timestamp}.png"
            if description:
                clean_desc = "".join(c for c in description if c.isalnum() or c in (' ', '-', '_')).rstrip()
                clean_desc = clean_desc.replace(' ', '_')
                filename = f"{test_id}_{clean_desc}_{timestamp}.png"
            
            screenshot_path = os.path.join(self.screenshot_dir, filename)
            self.driver.save_screenshot(screenshot_path)
            return screenshot_path
        except Exception:
            return ""
    
   
    def add_test_result(self, test_id, description, expected, actual, status, details=""):
        screenshot_path = self.take_screenshot(test_id, description)
        result = TestResult(test_id, description, expected, actual, status, details, screenshot_path)
        self.test_results.append(result)
    
    
    def test_registration_flow_complete(self):
        try:
            
            self.logout_if_logged_in()
            
            
            unique_suffix = datetime.now().strftime("%H%M%S")
            test_username = f"testuser_{unique_suffix}"
            test_email = f"test_{unique_suffix}@example.com"
            test_password = "TestPassword123!"
            
            self.driver.get("https://www.theodinproject.com/sign_up")
            time.sleep(2)
            
            
            self.driver.find_element(By.NAME, 'user[username]').send_keys(test_username)
            self.driver.find_element(By.NAME, 'user[email]').send_keys(test_email)
            self.driver.find_element(By.NAME, 'user[password]').send_keys(test_password)
            self.driver.find_element(By.NAME, 'user[password_confirmation]').send_keys(test_password)
            
            
            self.take_screenshot("REG_FLOW_FORM_BEFORE_SUBMISSION", "Registration form before submission")
            
            
            submit_btn = self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"], button[type="submit"]')
            submit_btn.click()
            time.sleep(5)  
            
            current_url = self.driver.current_url.lower()
            page_title = self.driver.title.lower()
            
            
            dashboard_indicators = ['dashboard', 'welcome', 'profile', 'progress', 'learning', 'curriculum', 'paths']
            is_dashboard = any(indicator in current_url or indicator in page_title for indicator in dashboard_indicators)
            
            if is_dashboard:
                self.add_test_result("REG_FLOW_001", "Registration to dashboard redirect", 
                                   "Should redirect to dashboard after registration", 
                                   f"Successfully registered and redirected to: {current_url}", "PASS")
            else:
                
                if "sign_up" in current_url:
                    self.add_test_result("REG_FLOW_001", "Registration completion", 
                                       "Should complete registration successfully", 
                                       f"Still on registration page - possible validation errors", "FAIL")
                else:
                    self.add_test_result("REG_FLOW_001", "Registration navigation", 
                                       "Should redirect appropriately after registration", 
                                       f"Unexpected navigation to: {current_url}", "FAIL")
        
            
            self.take_screenshot("REG_FLOW_RESULT", "Registration flow result")
            
        except Exception as e:
            self.add_test_result("REG_FLOW_ERROR", "Complete registration flow test", 
                               "Test should complete without errors", 
                               f"Error: {str(e)}", "FAIL", str(e))
    
    
    def test_navigation(self):
        nav_tests = [
            ("NAV_001", "Dashboard", "Dashboard", "dashboard"),
            ("NAV_002", "All Paths", "All Paths", "paths")
        ]
        
        for test_id, name, target, expected_url_part in nav_tests:
            try:
                
                self.driver.get("https://www.theodinproject.com/")
                time.sleep(2)
                
                if target.startswith("http"):
                    
                    if self.driver.current_url != target:
                        self.driver.get(target)
                else:
                    
                    link_selectors = [
                        f"//a[contains(text(), '{target}')]",
                        f"//a[text()='{target}']",
                        f"//nav//a[contains(text(), '{target}')]",
                        f"//header//a[contains(text(), '{target}')]",
                        f"a[href*='{expected_url_part}']"
                    ]
                    
                    link_found = False
                    for selector in link_selectors:
                        try:
                            if selector.startswith("//"):
                                link = self.wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                            else:
                                link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                            link.click()
                            link_found = True
                            break
                        except (TimeoutException, NoSuchElementException):
                            continue
                    
                    if not link_found:
                        self.add_test_result(test_id, f"{name} navigation", 
                                           f"Should find and click {name} link", 
                                           f"Link not found for {target}", "FAIL")
                        continue
                
                time.sleep(3)
                current_url = self.driver.current_url.lower()
                page_title = self.driver.title.lower()
                
                
                success_indicators = [
                    expected_url_part.lower() in current_url,
                    expected_url_part.lower() in page_title,
                    
                    (expected_url_part == "The Odin Project" and 
                     ("theodinproject.com" in current_url and current_url.endswith("/"))),
                    
                    (name == "About" and any(indicator in current_url for indicator in ['about', 'team', 'mission']))
                ]
                
                if any(success_indicators):
                    self.add_test_result(test_id, f"{name} navigation", 
                                       f"Should navigate to {name} page", 
                                       f"Successfully navigated to {current_url}", "PASS")
                else:
                    
                    if "dashboard" in current_url:
                        self.add_test_result(test_id, f"{name} navigation", 
                                           f"Should navigate to {name} page", 
                                           f"Redirected to dashboard (user logged in) - URL: {current_url}", "FAIL",
                                           "User  appears to be logged in, causing redirect")
                    else:
                        self.add_test_result(test_id, f"{name} navigation", 
                                           f"Should navigate to {name} page", 
                                           f"Navigation failed - URL: {current_url}", "FAIL")
                    
            except Exception as e:
                self.add_test_result(test_id, f"{name} navigation", 
                                   f"Should navigate to {name} page", 
                                   f"Error: {str(e)}", "FAIL", str(e))
    
    
    def print_results(self):
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result.status == "PASS")
        failed_tests = sum(1 for result in self.test_results if result.status == "FAIL")
        
        print(f"\n{'='*60}")
        print(f"TEST RESULTS SUMMARY")
        print(f"{'='*60}")
        print(f"Total Tests: {total_tests}")
        print(f"Passed: {passed_tests}")
        print(f"Failed: {failed_tests}")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        print(f"{'='*60}")
        
        
        passed_results = [r for r in self.test_results if r.status == "PASS"]
        failed_results = [r for r in self.test_results if r.status == "FAIL"]
        
        if passed_results:
            print(f"\n✓ PASSED TESTS ({len(passed_results)}):")
            for result in passed_results:
                print(f"  ✓ {result.test_id}: {result.description}")
        
        if failed_results:
            print(f"\n✗ FAILED TESTS ({len(failed_results)}):")
            for result in failed_results:
                print(f"  ✗ {result.test_id}: {result.description}")
                print(f"    Expected: {result.expected}")
                print(f"    Actual: {result.actual}")
                if result.details:
                    print(f"    Details: {result.details}")
                print()
    
    
    def run_all_tests(self):
        print("Starting Odin Project Test Suite...")
        print(f"Screenshot directory: {self.screenshot_dir}")
        
        try:
            
            print("\n1. Testing Complete Registration Flow...")
            self.test_registration_flow_complete()
            
            print("2. Testing Navigation (while logged in)...")
            self.test_navigation()
            
            print("3. Logging out after all tests...")
            self.logout_if_logged_in()
            
            self.print_results()
            
        except Exception as e:
            print(f"Test suite failed: {str(e)}")
        
        finally:
            time.sleep(2)
    
    
    def cleanup(self):
        if self.driver:
            self.driver.quit()
            print(f"Browser closed. Screenshots saved in: {self.screenshot_dir}")

if __name__ == "__main__":
    test = OdinProjectTest()
    try:
        test.run_all_tests()
    finally:
        test.cleanup()
