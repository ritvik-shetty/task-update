Feature: REST API PUT Request Testing

  Scenario: Verify PUT request to update an employee
    Given the API endpoint is "http://127.0.0.1:5000/update_employee/7"
    When a PUT request is made with the following data:
      | name     | address       | city      | salary |
      | New Name | 456 Updated St | New City  | 60000  |
    Then the response status code should be 200
    And the response should contain "message"
    And the response message should be "Employee updated successfully New Name"
