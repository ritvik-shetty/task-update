Feature: REST API DELETE Request Testing

  Scenario: Verify DELETE request to remove an employee
    Given the API endpoint is "http://127.0.0.1:5000/remove_employee/8"
    When a DELETE request is made
    Then the response status code should be 200
    And the response should contain "message"
    And the response message should be "Employee deleted successfully"
