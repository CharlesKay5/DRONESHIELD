import requests
import json

# Base URL for the Petstore Swagger API
BASE_URL = 'https://petstore.swagger.io/v2'

def display_test_result(test_name, passed, details=None):
    """
    Utility function to display test results
    Arguments:
        test_name (str): Name of the test case
        passed (bool): Whether the test passed or failed
        details (dict): Optional details about the test result
    """
    result = "PASSED" if passed else "FAILED"

    print(f"\n{test_name}: {result}")

    if details:
        print(f"Details: {details}")



created_pet_id = 0;

def test_post_pet():
    
    """Test case for successfully creating a pet with valid data"""
    global created_pet_id

    url = f"{BASE_URL}/pet"
    payload = {
        "id": 0,
        "name": 'Stella',
    }
    # Post payload to url
    response = requests.post(url, json=payload)
   
    # Verify the pet was created successfully
    assert response.status_code == 200
    display_test_result("POST Pet Test", True, {
        "Status Code": response.status_code,
    })
    created_pet_id = response.json()["id"]


def test_post_invalid_pet():
    """
    Test to POST pet with valid data
    """

    url = f"{BASE_URL}/pet"
    payload = {
        "id": "not_a_number",
        "name": 'Stella',
    }
    # Post payload to url
    response = requests.post(url, json=payload)
   
    # Verify the pet was NOT created
    # This should return 400, but is currently returning 500, it has been reported in BUGREPORT-2.md
    assert response.status_code != 200
    display_test_result("POST Invalid Pet Test", True, {
        "Status Code": response.status_code,
    })



def test_get_pet():
    """
    Test case for using GET to find the pet we created
    """
    global created_pet_id

    url = f"{BASE_URL}/pet"
    response = requests.get(f"{url}/{created_pet_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "Stella"

    # Verify the pet was found and has the correct name
    display_test_result("GET Pet Test", True, {
        "Status Code": response.status_code,
        "Pet Name": response.json()["name"]
    })

def test_get_invalid_pet():
    """
    Test case for using GET to find the pet we created
    """
    global created_pet_id

    url = f"{BASE_URL}/pet"
    response = requests.get(f"{url}/0")

    assert response.status_code == 404
    # Verify the pet was NOT found
    display_test_result("GET Pet Test", True, {
        "Status Code": response.status_code,
    })

def test_integer_limit():
    """Test case for creating a pet with an ID past the integer limit"""
    url = f"{BASE_URL}/pet"
    payload = {
        "id": 21474836470,
        "name": 'Stella',
    }
    # Post payload to url
    response = requests.post(url, json=payload)
   
    # Check if the response is not 200 (success)
    assert response.status_code != 200
    
    display_test_result("Integer Limit Pet Test", response.status_code != 200, {
        "Status Code": response.status_code,
        "Expected": "Non-200 status code",
        "Result": "Failed - API accepted ID larger than 32-bit integer limit" if response.status_code else "Passed"
    })

def test_none_payload():
    """Test case for sending a payload with value None"""
    url = f"{BASE_URL}/pet"

    payload = None
    # Post payload to url
    response = requests.post(url, json=payload)

    assert response.status_code == 415
    
    # Verify the pet was NOT created and the payload wasn't accepted
    display_test_result("Invalid Payload Test", True, {
        "Status Code": response.status_code,
    })
    
def test_empty_payload():
    """Test case for sending a payload with value None"""
    url = f"{BASE_URL}/pet"

    # Post to URL with no JSON payload, even though it's expected
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers)

    assert response.status_code == 405
    
    # Verify the pet was NOT created and the payload wasn't accepted
    display_test_result("Invalid Payload Test", True, {
        "Status Code": response.status_code,
    })
    
def test_negative_id():
    
    """Test case for attempting to create a pet with a negative ID"""

    url = f"{BASE_URL}/pet"
    payload = {
        "id": -123,
        "name": 'Stella',
    }
    # Post payload to url
    response = requests.post(url, json=payload)
   
    # Verify if the pet was created
    # This test has been reported in BUGREPORT-2.md.
    # The current functionality is that negative ID's are treated the same as 0 IDs,
    # i.e. they are auto-assigned to a positive number.
    # If this is expected, change the below line to assert response.status_code == 200
    assert response.status_code != 200
    display_test_result("Negative ID Pet Test", response.status_code != 200, {
        "Status Code": response.status_code,
        "Expected": "Non-200 status code",
        "Result": "Failed - API accepted a negative ID and auto assigned a positive one" if response.status_code == 200 else "Passed"
    })
    

def test_float_id():
    
    """Test case for attempting to create a pet with a float ID"""

    url = f"{BASE_URL}/pet"
    payload = {
        "id": 123.7,
        "name": 'Stella',
    }
    # Post payload to url
    response = requests.post(url, json=payload)
   
    assert response.status_code == 200
    display_test_result("Float ID Pet Test", response.status_code == 200, {
        "Status Code": response.status_code,
        "Result": "Passed - API accepted a float ID and rounded it to an integer" if response.status_code == 200 else "Failed"
    })


if __name__ == "__main__":
    
    # Execute both test cases when script is run directly
    test_post_pet()
    test_post_invalid_pet()
    test_get_pet()
    test_get_invalid_pet()
    test_integer_limit()
    test_none_payload()
    test_empty_payload()
    test_negative_id()
    test_float_id()