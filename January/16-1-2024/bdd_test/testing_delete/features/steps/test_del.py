import requests
from behave import given, when, then

@given('the API endpoint is "{url}"')
def set_api_url(context, url):
    context.api_url = url

@when('a DELETE request is made')
def make_delete_request(context):
    context.response = requests.delete(context.api_url)

@then('the response status code for successfull should be {status_code:d}')
def check_status_code(context, status_code):
    assert context.response.status_code == status_code, f"Expected status code {status_code}, but got {context.response.status_code}"

@then('the response status code for unsuccessfull should be {status_code:d}')
def check_status_code(context, status_code):
    assert context.response.status_code == status_code, f"Expected status code {status_code}, but got {context.response.status_code}"

@then('the response should contain "{expected_key}"')
def check_response_content(context, expected_key):
    json_response = context.response.json()
    assert expected_key in json_response, f"Key '{expected_key}' not found in the response"

@then('the response message should be "{expected_message}"')
def check_response_message(context, expected_message):
    json_response = context.response.json()
    assert json_response.get('message') == expected_message, f"Expected message '{expected_message}', but got {json_response.get('message')}"
