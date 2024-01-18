Feature: Testing employee POST request using REST API

  Scenario: Verify POST request to add a new employee
    Given the API endpoint is "http://127.0.0.1:5000/create_employee"
    When POST request is made with the following JSON data:
      """
      {
        "address": "Banerghatta",
        "city": "Bangalore",
        "name": "Lewis",
        "salary": "850820"
      }
      """
    Then the response status code for successfull should be 201
    
  Scenario: Verify POST request for wrong url
    Given the API endpoint is "http://127.0.0.1:5000/employees"
    When POST request is made with the following JSON data:
      """
      {
        "address": "Banerghatta",
        "city": "Bangalore",
        "name": "Lewis",
        "salary": "850820"
      }
      """
    Then the response status code for unsuccessfull should be 404  

  Scenario: Verify POST request for missing fields
    Given the API endpoint is "http://127.0.0.1:5000/employees"
    When POST request is made with the following JSON data:
      """
      {
        "address": "Banerghatta",
        "city": "Bangalore",
        "name": "Lewis"
      }
      """
    Then the response status code for unsuccessfull should be 404  


  Scenario: Verify POST request for missing field information
    Given the API endpoint is "http://127.0.0.1:5000/employees"
    When POST request is made with the following JSON data:
      """
      {
        "address": "",
        "city": "Bangalore",
        "name": "Lewis",
        "salary": "850820"
      }
      """
    Then the response status code for unsuccessfull should be 404  


