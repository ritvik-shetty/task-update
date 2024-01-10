Feature: REST API POST Request Testing

  Scenario: Verify POST call for single user
    When User sends "POST" call to endpoint "api/users"
      | name     | address       | city      | salary |
      | New Name | 456 Updated St | New City  | 60000  |
    Then User verifies the status code is "201"
    And User verifies POST response body contains following information
      | name     | address       | city      | salary |
      | New Name | 456 Updated St | New City  | 60000  |