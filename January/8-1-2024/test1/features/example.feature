# -- FILE: features/example.feature
Feature: Facebook Login functionality

  Scenario: Try login with correct login cred
    Given credentials are given
     When we input correct credentials
     Then Login will be successful

