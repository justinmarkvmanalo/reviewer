def test_button_exists(self, button_id, button_text):
    try:
        button = self.driver.find_element(By.ID, button_id)
        button = self.driver.find_element(By.XPATH, f"//button[contains(text(), '{button_text}')]")
        button = self.driver.find_element(By.CSS_SELECTOR, f"button[id='{button_id}']")
        return True
    except NoSuchElementException:
        return False

def test_button_visibility(self, button_selector):
    try:
        button = self.driver.find_element(By.CSS_SELECTOR, button_selector)
        is_visible = button.is_displayed()
        size = button.size
        is_properly_sized = size['width'] > 0 and size['height'] > 0
        opacity = button.value_of_css_property('opacity')
        visibility = button.value_of_css_property('visibility')
        return is_visible and is_properly_sized and opacity != '0' and visibility != 'hidden'
    except Exception:
        return False

def test_button_enabled_state(self, button_selector, should_be_enabled=True):
    try:
        button = self.driver.find_element(By.CSS_SELECTOR, button_selector)
        is_enabled = button.is_enabled()
        disabled_attr = button.get_attribute('disabled')
        is_disabled = disabled_attr is not None
        classes = button.get_attribute('class')
        has_disabled_class = 'disabled' in classes if classes else False
        if should_be_enabled:
            return is_enabled and not is_disabled and not has_disabled_class
        else:
            return not is_enabled or is_disabled or has_disabled_class
    except Exception:
        return False

def test_button_text_content(self, button_selector, expected_text):
    try:
        button = self.driver.find_element(By.CSS_SELECTOR, button_selector)
        actual_text = button.text.strip()
        button_value = button.get_attribute('value')
        inner_text = button.get_attribute('innerText')
        text_matches = (actual_text == expected_text or 
                       button_value == expected_text or 
                       inner_text == expected_text)
        return text_matches
    except Exception:
        return False

def test_button_click_response(self, button_selector):
    try:
        button = self.driver.find_element(By.CSS_SELECTOR, button_selector)
        initial_url = self.driver.current_url
        initial_title = self.driver.title
        button.click()
        time.sleep(2)
        new_url = self.driver.current_url
        new_title = self.driver.title
        response_detected = (new_url != initial_url or 
                           new_title != initial_title)
        return response_detected
    except Exception:
        return False

def test_navigation_button(self, button_selector, expected_url_part):
    try:
        button = self.driver.find_element(By.CSS_SELECTOR, button_selector)
        initial_url = self.driver.current_url
        button.click()
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url != initial_url
        )
        current_url = self.driver.current_url
        navigation_successful = expected_url_part in current_url
        return navigation_successful
    except Exception:
        return False

def test_form_submit_button(self, form_selector, submit_button_selector):
    try:
        form = self.driver.find_element(By.CSS_SELECTOR, form_selector)
        submit_button = self.driver.find_element(By.CSS_SELECTOR, submit_button_selector)
        initial_url = self.driver.current_url
        submit_button.click()
        time.sleep(3)
        current_url = self.driver.current_url
        success_indicators = [
            current_url != initial_url,
            "success" in current_url.lower(),
            "thank" in self.driver.page_source.lower(),
            "submitted" in self.driver.page_source.lower()
        ]
        return any(success_indicators)
    except Exception:
        return False

def test_button_styling(self, button_selector, expected_styles):
    try:
        button = self.driver.find_element(By.CSS_SELECTOR, button_selector)
        styling_correct = True
        for property_name, expected_value in expected_styles.items():
            actual_value = button.value_of_css_property(property_name)
            if actual_value != expected_value:
                styling_correct = False
                break
        return styling_correct
    except Exception:
        return False

def test_button_hover_effect(self, button_selector):
    try:
        from selenium.webdriver.common.action_chains import ActionChains
        button = self.driver.find_element(By.CSS_SELECTOR, button_selector)
        initial_bg_color = button.value_of_css_property('background-color')
        initial_cursor = button.value_of_css_property('cursor')
        ActionChains(self.driver).move_to_element(button).perform()
        time.sleep(1)
        hover_bg_color = button.value_of_css_property('background-color')
        hover_cursor = button.value_of_css_property('cursor')
        has_hover_effect = (hover_bg_color != initial_bg_color or 
                          hover_cursor == 'pointer')
        return has_hover_effect
    except Exception:
        return False

def test_button_accessibility(self, button_selector):
    try:
        button = self.driver.find_element(By.CSS_SELECTOR, button_selector)
        aria_label = button.get_attribute('aria-label')
        title = button.get_attribute('title')
        alt_text = button.get_attribute('alt')
        tab_index = button.get_attribute('tabindex')
        is_focusable = tab_index != '-1'
        button_text = button.text.strip()
        has_descriptive_text = len(button_text) > 0
        is_accessible = ((aria_label or title or alt_text or has_descriptive_text) 
                        and is_focusable)
        return is_accessible
    except Exception:
        return False

def test_button_response_time(self, button_selector, max_response_time=3):
    try:
        button = self.driver.find_element(By.CSS_SELECTOR, button_selector)
        start_time = time.time()
        button.click()
        time.sleep(1)
        end_time = time.time()
        response_time = end_time - start_time
        return response_time <= max_response_time
    except Exception:
        return False

def test_all_buttons(self):
    self.driver.get("https://www.theodinproject.com/sign_up")
    submit_exists = self.test_button_exists("", "Sign up")
    self.add_test_result("BTN_001", "Submit button exists", 
                        "Submit button should exist", 
                        f"Button found: {submit_exists}", 
                        "PASS" if submit_exists else "FAIL")
    
    if submit_exists:
        button_clickable = self.test_button_enabled_state('input[type="submit"]', True)
        self.add_test_result("BTN_002", "Submit button enabled", 
                            "Submit button should be enabled", 
                            f"Button enabled: {button_clickable}", 
                            "PASS" if button_clickable else "FAIL")
    
    navigation_buttons = [
        ("Dashboard", "dashboard"),
        ("All Paths", "paths"),
        ("About", "about")
    ]
    
    for button_name, url_part in navigation_buttons:
        self.driver.get("https://www.theodinproject.com/")
        nav_success = self.test_navigation_button(
            f"//a[contains(text(), '{button_name}')]", 
            url_part
        )
        self.add_test_result(f"BTN_NAV_{button_name.upper()}", 
                            f"{button_name} navigation button", 
                            f"Should navigate to {button_name} page", 
                            f"Navigation successful: {nav_success}", 
                            "PASS" if nav_success else "FAIL")

button = driver.find_element(By.ID, "submit-btn")
button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button = driver.find_element(By.XPATH, "//button[text()='Submit']")
button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
button = driver.find_element(By.CSS_SELECTOR, "[role='button']")