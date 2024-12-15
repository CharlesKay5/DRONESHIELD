# Bug Report

#### Bugs ordered by priority high-low

## Bug 1: Invalid payloads returning 500 instead of 400
#### **Summary**: 
- Posting an invalid payload to the endpoint is returning a 500 error
#### **Severity**: High
#### **Priority**: High
#### **Steps to Reproduce**:
  1. Post to the /pet endpoint with a pet ID in string format (only numerical values are accepted)
  2. Observe the endpoint return a 500 error (Unexpected Condition), when it should be 400 (Bad Request)
#### **Expected Result**: 
- Invalid payloads should return a 400 error
#### **Actual Result**: 
-  Invalid payloads return a 500 error.
- This is a security risk as the server is not handlind exceptions gracefully, leaving it potentially vulnerable to denial of service attacks.
- 500 is also a generic error, it lacks clarity for API users and makes debugging harder.

## Bug 2:
#### **Summary**: 
- The API allows IDs past the integer limit 
#### **Severity**: High
#### **Priority**: Medium
#### **Steps to Reproduce**:
  1. Post to the /pet endpoint with a pet ID greater than 2147483647.
  2. Observe the ID is accepted and the pet is created
#### **Expected Result**: 
- IDs greater than the integer limit should not be accepted unless the system is specifically built to handle them.
#### **Actual Result**: 
- IDs greater than the integer limit are accepted and assigned to pets.
- This opens the door to data corruption risks, as overflows, truncations or failures may occur when the backend attempts to handle this data.

## Bug 3:
#### **Summary**: 
- Empty strings are accepted in the payload
#### **Severity**: Medium
#### **Priority**: Medium
#### **Steps to Reproduce**:
  1. Post to the /pet endpoint with a pet whose name or other data contains an empty string ("").
  2. Observe the empty string is accepted an a pet is created with no name.
#### **Expected Result**: 
- Empty strings should not be accepted
#### **Actual Result**: 
-  Empty strings are accepted and pets with empty data are created.
- This has a negative impact on data integrity, as incomplete or meaningless data is stored.
- This will also result in a degraded user experience if this empty data is being displayed somewhere, for example, a pet may be displayed on a marketplace, but they are missing data and are simply taking space and resources on the page.


## Bug 4:
#### **Summary**: 
- Negative IDs are accepted and are auto assigned to a positive ID (this is likely intentional, but worth noting)
#### **Severity**: Low
#### **Priority**: Low
#### **Steps to Reproduce**:
  1. Post to the /pet endpoint with a pet whose ID is less than 0.
  2. Observe the pet is created and auto assigned a positive ID.
#### **Expected Result**: 
- Either we auto assign a positive ID, or the API should return a 400 error.
#### **Actual Result**: 
-  The pet is auto assigned a positive ID.