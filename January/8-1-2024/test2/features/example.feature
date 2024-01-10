Feature: Login functionality

    Scenario: Try login with correct login credentials
        Given the user is on the login page
        When the user enters valid username and password
        Then the user should be logged in successfully

    Scenario: Try login with incorrect login credentials   
        Given the user is on the login page
        When the user enters invalid username and password
        Then the user should see an error message
