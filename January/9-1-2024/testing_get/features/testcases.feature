Feature: REST API GET Request Testing

  Scenario: Verify GET request for a specific employee
    Given the API endpoint is "http://127.0.0.1:5000/employee/2"
    When a GET request is made
    Then the response status code should be 200
    And the response should contain "id"
    And the response should contain "name"
    And the response should contain "address"
    And the response should contain "city"
    And the response should contain "salary"

  Scenario: Verify GET request for all employees
    Given the API endpoint is "http://127.0.0.1:5000/list_employees"
    When a GET request is made
    Then the response status code should be 200
    And the response should contain at least 1 employee
