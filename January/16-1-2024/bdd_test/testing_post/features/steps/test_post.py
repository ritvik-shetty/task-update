import json
import requests
from behave import given, when, then

api_endpoint = "http://127.0.0.1:5000/create_employee"

@given('the API endpoint is "{endpoint}"')
def set_api_endpoint(context, endpoint):
    context.api_endpoint = endpoint

@when('POST request is made with the following JSON data')
def make_post_request_with_json(context):
    data = json.loads(context.text)
    context.response = requests.post(f"{context.api_endpoint}", json=data)

@then('the response status code for successfull should be {status_code:d}')
def check_response_status(context, status_code):
    assert context.response.status_code == status_code, f"Expected status code {status_code}, but got {context.response.status_code}"

@then('the response status code for unsuccessfull should be {status_code:d}')
def check_response_status(context, status_code):
    assert context.response.status_code == status_code, f"Expected status code {status_code}, but got {context.response.status_code}"
