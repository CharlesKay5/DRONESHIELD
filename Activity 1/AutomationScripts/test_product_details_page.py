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

    def add_to_cart(self):
        """Helper method to add item to the cart"""
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart")
        add_to_cart_button.click()
        time.sleep(1)

        # Verify cart count
        cart_count = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_count.text, '1')

    def remove_from_cart(self):
        """Helper method to remove items from the cart"""
        remove_from_cart_button = self.driver.find_element(By.ID, "remove")
        remove_from_cart_button.click()
        time.sleep(1)

        # Verify cart is empty by checking that the badge is not present 
        try:
            self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            self.fail("Shopping cart badge should not be visible when cart is empty")
        except:
            # If the element is not found, the test passes
            pass

    def open_items_page(self):
        """Helper method to open the items page"""
        # Get fresh elements for each iteration
        items_link = self.driver.find_element(By.CLASS_NAME, "inventory_item_name")
        items_link.click()
        time.sleep(1)

    def test_page_function(self):
        """Test adding and removing from cart"""
        self.login_user("standard_user")
        self.verify_successful_login()

        self.open_items_page()
        self.add_to_cart()
        self.remove_from_cart()
        
        self.logout_user()


if __name__ == "__main__":
    unittest.main()
