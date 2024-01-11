Feature: REST API DELETE Request Testing

  Scenario: Verify DELETE request to remove an employee
    Given the API endpoint is "http://127.0.0.1:5000/remove_employee/8"
    When a DELETE request is made
    Then the response status code for successfull should be 200
    And the response should contain "message"
    And the response message should be "Employee deleted successfully"

  Scenario: Verify DELETE request to remove a non existing employee
    Given the API endpoint is "http://127.0.0.1:5000/remove_employee/9"
    When a DELETE request is made
    Then the response status code for unsuccessfull should be 404
    And the response should contain "message"
    And the response message should be "Improper ID"

  Scenario: Verify DELETE request for wrong url
    Given the API endpoint is "http://127.0.0.1:5000/employees"
    When a DELETE request is made
    Then the response status code for unsuccessfull should be 404  