# TEST-STRATEGY

## Purpose
- To ensure the following aspects of the SauceDemo application are working as intended and are at an appropriate standard through both manual and automation testing:
    - Functionality
    - Security
    - Design
    - Usability
    - Accessibility 

## Objectives
1. Validate core feature functionality such as login, checkout, and cart.
2. Identify bugs in functionality, security risks, design flaws or errors
3. Ensure the application meets accessibility and usability standards for end users.
4. Provide reproducible test cases for regression testing and automation for upkeep.
 

## Scope
- **In scope**:
    - Login and logout functionality
    - Product filtering
    - Adding and removing from cart
    - Checkout functionality
    - Security testing
    - Performance testing
    - Design review
    - Accessibility and useability testing
- **Out of scope**:
    - API/backend testing


## Tools and Frameworks
- **For manual testing**:
    - Chrome, Edge, Firefox, all up to date
    - In browser developer tools
- **For automation testing**:
    - Selenium for browser automation
    - Python/Pytest for test framework
    - Chromedriver for browser

<br>

# TEST-PLANS

## Log In and Log Out
### Test Cases:
- **Accepted usernames/passwords**  
    - **Expected results**: User should be logged in upon entering a valid username/password.
- **Failed login attempts**  
    - **Expected results**: User should NOT be logged in upon entering an invalid username, password, or both.
- **Session handling (cookies, session expiry)**  
    - **Expected results**: 
        - User should be logged out automatically after a certain period.
        - User should be logged out if browser cookies are cleared.

## Filtering
### Test Cases:
- **Filter functionality**  
    - **Expected results**: Filters should apply and reorder the items page.
- **Filter accuracy**  
    - **Expected results**: Filters are accurate and match their description.

## Product Listing Page
### Test Cases:
- **Validate product displays**  
    - **Expected results**: Product images, titles, descriptions, and prices should match.
- **Add/remove items from Cart**  
    - **Expected results**: Items should be addable and removable from the Cart via the product listing page.

## Product Details Page
### Test Cases:
- **Validate product displays**  
    - **Expected results**: Product images, titles, descriptions, and prices should match.
- **Interaction from product page**  
    - **Expected results**: 
        - Back to products button should navigate back to `inventory.html`.
        - Add/remove from cart should work on this page.

## Cart Page
### Test Cases:
- **Remove items**  
    - **Expected results**: Items should be removable from the cart in the Cart Page.
    - *Note*: Items should not be addable to the cart from this page (excluding quantity adjustments).
- **Quantity adjustments**  
    - **Expected results**: Quantity adjustments should be possible from the Cart Page. The user should be able to increase/decrease the quantity of cart items from this page.
- **Cart persistence across sessions**  
    - **Expected results**: Cart items should persist across sessions.
- **Continue Shopping**  
    - **Expected results**: The "Continue Shopping" button should navigate back to `inventory.html`.

## Checkout
### Test Cases:
- **Checkout flow**  
    - **Expected results**: Checkout flow should make sense, and some form of input validation should be present.
- **Input validation**  
    - **Expected results**: Inputs in the checkout process should be validated.
- **Successful transactions**  
    - **Expected results**: Successful transactions should be recorded.
- **Failed transactions**  
    - **Expected results**: Failed transactions should return to payment options.
- **Retries on failed transactions**  
    - **Expected results**: Failed transactions should be re-attemptable.

## Footer
### Test Cases:
- **Social media links**  
    - **Expected results**: Social media links in the footer should redirect appropriately.
- **Design**  
    - **Expected results**: Footer should be positioned at the bottom of the webpage.

## Security Testing
### Test Cases:
- **Input validation (prevent injection)**  
    - **Expected results**: Inputs at all input fields should be validated so correct data is entered.
- **Session management (hijacking)**  
    - **Expected results**: User’s session should not be hijackable with a session cookie or token.
- **Authentication**  
    - **Expected results**: Users should not be able to log in with incorrect details.
- **Role-based access**  
    - **Expected results**: Users with particular roles should have access in line with their permissions.
    - *Examples*: 
        - `standard_user`
        - `locked_out_user`
        - `problem_user`
        - `performance_glitch_user`
        - `error_user`
        - `visual_user`
- **Data privacy (password/payments)**  
    - **Expected results**: User’s usernames, passwords, and payment details should not be stored anywhere in plain text.

## Performance Testing
### Test Cases:
- **Load times**  
    - **Expected results**: Load times should be short or display a loading animation/message if they are expectedly long
- **Stress testing**  
    - **Expected results**: Page should load well with network throttling.
- **Concurrency**  
    - **Expected results**: Session count should be limited to one for security and data integrity.

## Compatibility Testing
### Test Cases:
- **Browser compatibility**  
    - **Expected results**: Site should work consistently across browsers.
- **Device compatibility**  
    - **Expected results**: Site should be compatible with mobile and tablet devices.
- **Responsiveness**  
    - **Expected results**: Site should respond to responsive resolutions appropriately.

## Usability
### Test Cases:
- **Ease of navigation**  
    - **Expected results**: Site should be simple to navigate and should contain a menu for ease of access.
- **Accessibility**  
    - **Expected results**: Site should contain the following:  
        - Alt tags on images  
        - Text descriptions for icons  
        - Accessibility via pressing Tab, Arrow Keys, and Enter  
        - High contrast/readable fonts  
        - Scalability via zoom  
        - Label elements on form fields
- **Error message accuracy**  
    - **Expected results**: Error messages should be accurate and appropriate for the occasion without revealing potentially secret information.

## General Design Notes
- Ensure all design elements are consistent with the overall user experience and branding.


<br>
# DECISIONS AND REASONS

## Tools and Frameworks
1. **Selenium**: I chose Selenium since I have experience using it from my previous job. It is also a widely accepted framework due to its automation capabilities, cross-browser support and integration with Python.
2. **Python**: I have experience with Python, but have never used it for automation testing before. My automation experience is in C#, but given the use of Python at DroneShield I decided to try it for myself since that is what I would likely be working with if hired.
3. **Chromedriver**: Chrome is the most commonly used browser, with nearly 70% market share. For this reason I chose ChromeDriver to perform my automation.