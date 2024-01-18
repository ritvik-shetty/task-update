import requests
from behave import given, when, then

#given the api url for the get request
@given('the API endpoint is "{url}"')
def set_api_url(context, url):
    context.api_url = url

#when the GET request for the api is made
@when('a GET request is made')
def make_get_request(context):
    context.response = requests.get(context.api_url)

# Code to check successful status code
@then('the response status code for successfull should be {status_code:d}')
def check_status_code(context, status_code):
    assert context.response.status_code == status_code, f"Expected status code {status_code}, but got {context.response.status_code}"

# Code to check unsuccessful status code
@then('the response status code for unsuccessfull should be {status_code:d}')
def check_status_code(context, status_code):
    assert context.response.status_code == status_code, f"Expected status code {status_code}, but got {context.response.status_code}"

# Code to check if response contains the expected keys
@then('the response should contain "{expected_key}"')
def check_response_content(context, expected_key):
    json_response = context.response.json()
    assert expected_key in json_response[0], f"Key '{expected_key}' not found in the response"

# Code to check if response contains employee data
@then('the response should contain employee')
def check_at_least_one_employee(context):
    json_response = context.response.json()
    assert len(json_response) >= 0, "Expected employee in the response"
