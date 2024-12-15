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

# Creating global variables for pytest's standalone functions
pet_original_name = ''
created_pet_id = 0
def test_create_pet():
    
    """Test case for successfully creating a pet with valid data"""
    global pet_original_name
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

        # The ID will be auto-generated, so we can store it and the name for future use
        pet_original_name = response_data["name"]
        created_pet_id = response_data["id"]

        # Call the function to edit the pet's name by ID. We pass in the name so that we can compare to it once we've edited.
        test_edit_pet()
        test_edit_invalid_pet()
    # Display results if test fails
    except AssertionError as e:
        display_test_result("Create Valid Pet Test", False, str(e))

# Edit the name of the pet created from test_create_pet
def test_edit_pet():
    """
    Edit a pet using its ID
    """
    global pet_original_name
    global created_pet_id

    url = f"{BASE_URL}/pet"

    # Our new payload with the updated pet name
    update_payload = {
        "id": created_pet_id,
        "name": "Flint",
        "status": "available"
    }
    
    # Send the new payload
    update_response = requests.put(url, json=update_payload)
    
    # Get the updated data
    get_url = f"{BASE_URL}/pet/{created_pet_id}"
    response = requests.get(get_url)
    updated_pet = response.json()

    try:
        # Check to see if the pet was correctly updated.
        assert update_response.status_code == 200, "Update failed"
        assert response.status_code == 200
        assert updated_pet["name"] != pet_original_name
        assert updated_pet["name"] == "Flint"
        
        display_test_result("Edit Pet Test", True, {
            "Status Code": response.status_code,
            "Edited Pet ID": created_pet_id,
            "Previous Name": pet_original_name,
            "New Name": updated_pet["name"]
        })
    except AssertionError as e:
        display_test_result("Edit Pet Test", False, {
            "Status Code": response.status_code,
            "Error": str(e)
        })

def test_edit_invalid_pet():
    """
    Test case for attempting to edit a pet with invalid data
    """
    
    url = f"{BASE_URL}/pet"

    # Our new payload with the invalid pet data
    invalid_payload = {
        "id": "not_a_number",
        "name": "", # Empty Name
        "status": 123 # Invalid status
    }
    
    # Send the new payload
    update_response = requests.put(url, json=invalid_payload)
    

    try:
        # API should reject invalid data
        assert update_response.status_code != 200, "Invalid update was accepted"
        
        display_test_result("Edit Invalid Pet Test", True, {
            "Status Code": update_response.status_code,
            "Invalid ID": invalid_payload["id"],
            "Invalid Name": invalid_payload["name"],
            "Invalid Status": invalid_payload["status"]
        })
    except AssertionError as e:
        display_test_result("Edit Invalid Pet Test", False, {
            "Status Code": update_response.status_code,
            "Error": str(e)
        })

if __name__ == "__main__":
    # Execute both test cases when script is run directly
    test_create_pet()