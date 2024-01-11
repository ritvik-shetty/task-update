Feature: POST Request for a REST API

  Scenario: Create a new resource
    Given the API endpoint is "http://127.0.0.1:5000/create_employee"
    When I make a POST request with the following JSON data:
      """
      {
        "address": "Banerghatta",
        "city": "Bangalore",
        "name": "Lewis",
        "salary": "850820"
      }
      """
    Then the response status code should be 201
    
