Feature: Testing employee PUT request using REST API

  Scenario: Verify PUT request to update an employee
    Given the API endpoint is "http://127.0.0.1:5000/update_employee/10"
    When PUT request is made with the following JSON data:
      """
      {
        "address": "Test address2",
        "city": "kolkatha",
        "name": "Charan",
        "salary": "660820"
      }
      """
    Then the response status code for successfull should be 200
    
  Scenario: Verify PUT request for wrong url
    Given the API endpoint is "http://127.0.0.1:5000/employees/9"
    When PUT request is made with the following JSON data:
      """
      {
        "address": "Banerghatta",
        "city": "Bangalore",
        "name": "Lewis",
        "salary": "850820"
      }
      """
    Then the response status code for unsuccessfull should be 404  


  Scenario: Verify PUT request to update an employee with missing field information
    Given the API endpoint is "http://127.0.0.1:5000/update_employee/9"
    When PUT request is made with the following JSON data:
      """
      {
        "address": "Test address2",
        "city": "kolkatha",
        "name": "Charan",
        "salary": ""
      }
      """
    Then the response status code for unsuccessfull should be 400