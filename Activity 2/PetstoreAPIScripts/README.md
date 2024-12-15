# API Automation Test Suite

This project contains automated tests for the SauceDemo website using **Python** and **Selenium**. The tests are designed to test core features such as login, cart functionality, and checkout process.

## Prerequisites

Before running the tests, ensure you have the following installed:

- **Python 3.9+**
- **Selenium**: Web automation framework for Python
- **WebDriver**: ChromeDriver - included in this project in the chromedriver-win64 folder
- **Pytest**: Testing framework for Python

## Installation

1. **Clone the repository**:
    If you haven’t already cloned the project, use this command:
    ```
    git clone <repository_url>
    ```
2. **Set up a virtual environment**:
    - Windows
    ```
    .\venv\Scripts\activate
    ```
    - Mac
    ```
    source venv/bin/activate
    ```
3. **Install required dependencies**: Inside your virtual environment, run:
    ```
    pip install -r requirements.txt
    ```

## Running the tests

1. Navigate to the PetstoreAPIScripts folder:
    ```
    cd '.\Activity 2\PetstoreAPIScripts\'
    ```
2. Run a single test
    - The tests to choose from are as follows:
        1. test_create_pet.py
        2. test_delete_pet.py
        3. test_edit_pet.py
        4. test_status_codes.py
    - Simply run this command and replace testname.py with any of the above:
    ```
    python testname.py
    ```
3. To run all the tests, use **Pytest**:
    ```
    pytest
    ```
4. **Generate a report with Pytest**: You can generate and HTML report of the test results using:
    ```
    pytest --html=report.html
    ```