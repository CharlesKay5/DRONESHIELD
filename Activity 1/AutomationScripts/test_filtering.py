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

    def test_filtering_options(self):
        """Test all filtering options and verify correct ordering"""
        self.login_user("standard_user")
        self.verify_successful_login()

        sorting_tests = [
            {
                'option_text': 'Name (A to Z)',
                'get_items': lambda: [item.text for item in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")],
                'verify': lambda items: items == sorted(items) # Takes the list of items and compares to the sorted list
            },
            {
                'option_text': 'Name (Z to A)',
                'get_items': lambda: [item.text for item in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")],
                'verify': lambda items: items == sorted(items, reverse=True) # Takes the list of items and compares to the sorted list in reverse   
            },
            {
                'option_text': 'Price (low to high)',
                'get_items': lambda: [float(item.text.replace('$', '')) for item in self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")],
                'verify': lambda items: items == sorted(items) # Takes the list of items and compares to the sorted list
            },
            {
                'option_text': 'Price (high to low)',
                'get_items': lambda: [float(item.text.replace('$', '')) for item in self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")],
                'verify': lambda items: items == sorted(items, reverse=True) # Takes the list of items and compares to the sorted list in reverse
            }
        ]

        for test in sorting_tests:
            # Find the sort dropdown
            sort_dropdown = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
            )
            sort_dropdown.click()
            
            # Find and click the option
            option = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//option[text()='{test['option_text']}']"))
            )
            option.click()
            time.sleep(1)  # Wait for sorting to complete

            # Get all items after sorting
            items = test['get_items']()
            
            # Verify the order
            is_correct_order = test['verify'](items)
            
            # Print the results for visibility
            print(f"\nTesting {test['option_text']}:")
            print(f"Items in current order: {items}")
            print(f"Order is correct: {is_correct_order}")
            
            # Assert the order is correct
            self.assertTrue(is_correct_order, 
                           f"Items not in correct order for {test['option_text']}\nCurrent order: {items}")
            
            time.sleep(1)  # Delay to see the results

        self.logout_user()

if __name__ == "__main__":
    unittest.main()
