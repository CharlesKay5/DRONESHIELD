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




def test_create_pet():
    
    """Test case for successfully creating a pet with valid data"""
    
    url = f"{BASE_URL}/pet"
    payload = {
        "id": 0,
        "name": 'Beans',
        "status": "available"
    }
    # Post payload to url
    response = requests.post(url, json=payload)
    
    try:
        # Verify the response meets all success criteria
        assert response.status_code == 200
        
        # Get the response data
        response_data = response.json()
        
        # Verify the returned data matches what we sent
        assert response_data["name"] == "Beans"
        assert response_data["status"] == "available"

        # The ID will be auto-generated, so we can store it for future use
        created_pet_id = response_data["id"]

        # Call utility function to display the results
        display_test_result("Create Valid Pet Test", True, {
            "Status Code": response.status_code,
            "Pet ID": created_pet_id,
            "Pet Name": response_data["name"],
            "Pet Status": response_data["status"]
        })

    # Display results if test fails
    except AssertionError as e:
        display_test_result("Create Valid Pet Test", False, str(e))

def test_create_invalid_pet():
    
    """Test case for handling invalid pet creation (using string instead of integer for ID)"""
    
    url = f"{BASE_URL}/pet"
    payload = {
        "id": 'testing',  # Invalid ID type (string instead of integer)
        "name": 'Beans',
        "status": "available"
    }
    # Post response to url
    response = requests.post(url, json=payload)
    
    try:
        # Verify the API rejects invalid data
        assert response.status_code != 200
        display_test_result("Create Invalid Pet Test", True, {
            "Status Code": response.status_code
        })
    # Display results if test fails
    except AssertionError as e:
        display_test_result("Create Invalid Pet Test", False, {
            "Status Code": response.status_code,
            "Error": str(e)
        })

if __name__ == "__main__":
    # Execute both test cases when script is run directly
    test_create_pet()
    test_create_invalid_pet()