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


created_pet_id = ''
def test_create_pet():
    
    """Test case for successfully creating a pet with valid data"""
    
    global created_pet_id

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

        # The ID will be auto-generated, so we can store it for future use
        created_pet_id = response_data["id"]

        test_delete_pet()
    # Display results if test fails
    except AssertionError as e:
        display_test_result("Create Valid Pet Test", False, str(e))

# Delete the pet created from test_create_pet
def test_delete_pet():
    """
    Delete a pet using its ID
    Arguments:
        pet_id (int): ID of the pet to delete obtained from the test_create_pet() function
    """

    url = f"{BASE_URL}/pet/{created_pet_id}"
    response = requests.delete(url)

    try:
        assert response.status_code == 200
        display_test_result("Delete Pet Test", True, {
            "Status Code": response.status_code,
            "Deleted Pet ID": created_pet_id
        })
    except AssertionError as e:
        display_test_result("Delete Pet Test", False, {
            "Status Code": response.status_code,
            "Error": str(e)
        })

if __name__ == "__main__":
    # Execute both test cases when script is run directly
    test_create_pet()