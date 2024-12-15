# TEST-STRATEGY

## Purpose
- To ensure the following aspects of the Swagger Petstore API are working as intended and are at an appropriate standard through automation testing:
    - Functionality
    - Security
    - Usability
    - Accessibility 

## Objectives
1. Validate core feature functionality such as creating, editing, deleting pets.
2. Identify bugs in functionality, security risks or errors
3. Provide automation testing for the API.
 

## Scope
- **In scope**:
    - Create pets
    - Edit pets
    - Delete pets
    - Check status codes
    - Test edge cases
    - Test invalid data
    - Security testing


## Tools and Frameworks
- **For automation testing**:
    - Python/Pytest for test framework
    - JSON for response data handling

<br>

# TEST-PLANS

## Creating a pet
### Test Cases:
- **Creating a pet with valid data**  
    - **Expected results**: Pet should be created successfully with accurate data.
- **Creating a pet with invalid data**  
    - **Expected results**: Pet should not be created wiht inaccurate data.

## Editing a pet
### Test Cases:
- **Edit pet with valid data**  
    - **Expected results**: Pet should be editable with valid data.
- **Edit pet with invalid data**  
    - **Expected results**: Pet should not be editable with invalid data.

## Deleting a pet
### Test Cases:
- **Deleting an existing pet**  
    - **Expected results**:  Pet should be successfully deleted. No other pets should be affected.

## Status Codes
### Test Cases:
- **POST a valid pet**  
    - **Expected results**: API should return a 200 repsone code.
- **POST an invalid pet**  
    - **Expected results**: API should return a 400 repsone code. 
- **GET a valid pet**  
    - **Expected results**: API should return a 200 repsone code. 
- **GET an invalid pet**  
    - **Expected results**: API should return a 404 repsone code. 
- **POST a pet with an ID past the integer limit**  
    - **Expected results**: API should return a non-200 repsone code. 
- **POST a pet with a payload of value None**  
    - **Expected results**: API should return a 415 repsone code. 
- **POST a pet with an empty payload**  
    - **Expected results**: API should return a 405 repsone code. 
- **POST a pet with a negative ID**  
    - **Expected results**: API should return a non-200 repsone code. 
- **POST a pet with a float ID**  
    - **Expected results**: API should return a 200 repsone code and floor the ID.

<br>
# DECISIONS AND REASONS

## Tools and Frameworks
1. **Python**: I have experience with Python, but have never used it for automation testing before. My automation experience is in C#, but given the use of Python at DroneShield I decided to try it for myself since that is what I would likely be working with if hired.
2. **JSON**: I chose JSON to handle my response data because I am familiar with it thanks to my background in web development. JSON is highly readable and intuitive, and is supported in Python.