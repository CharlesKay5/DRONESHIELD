import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSauceDemo(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test case"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "https://www.saucedemo.com/"
        self.standard_password = "secret_sauce"
        
    def tearDown(self):
        """Clean up after each test case"""
        if self.driver:
            self.driver.quit()
            
    def login_user(self, username):
        """Helper method to perform login actions"""
        self.driver.get(self.base_url)
        
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        password_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        
        username_field.send_keys(username)
        password_field.send_keys(self.standard_password)
        login_button.click()

    def logout_user(self):
        """Helper method to perform logout actions"""
        menu_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        )
        menu_button.click()
        
        logout_link = self.wait.until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_link.click()
        
        # Verify return to login page
        self.wait.until(EC.url_to_be(self.base_url))
        self.assertEqual(self.driver.current_url, self.base_url)
        time.sleep(2)  # Delay to see the login page

    def verify_successful_login(self):
        """Helper method to verify successful login and add delay"""
        self.wait.until(EC.url_contains("inventory.html"))
        self.assertIn("inventory.html", self.driver.current_url)
        time.sleep(2)  # Delay to see the inventory page

    def test_standard_user_login_logout(self):
        """Test successful login and logout with standard_user"""
        self.login_user("standard_user")
        # self.assertIn("wrong_page.html", self.driver.current_url)  # This will fail for debugging
        self.verify_successful_login()
        self.logout_user()

    def test_locked_out_user_login(self):
        """Test locked_out_user cannot login"""
        self.login_user("locked_out_user")
        error_message = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-button"))
        )
        self.assertTrue(error_message.is_displayed())
        self.assertNotIn("inventory.html", self.driver.current_url)
        time.sleep(2)  # Delay to see the error

    def test_problem_user_login_logout(self):
        """Test successful login and logout with problem_user"""
        self.login_user("problem_user")
        self.verify_successful_login()
        self.logout_user()

    def test_performance_glitch_user_login_logout(self):
        """Test successful login and logout with performance_glitch_user"""
        self.wait = WebDriverWait(self.driver, 20)  # Increased wait time for page to render
        self.login_user("performance_glitch_user")
        self.verify_successful_login()
        self.logout_user()

    def test_error_user_login_logout(self):
        """Test successful login and logout with error_user"""
        self.login_user("error_user")
        self.verify_successful_login()
        self.logout_user()

    def test_visual_user_login_logout(self):
        """Test successful login and logout with visual_user"""
        self.login_user("visual_user")
        self.verify_successful_login()
        self.logout_user()

if __name__ == "__main__":
    unittest.main()
