# Import necessary modules from the 'behave' library
from behave import given, when, then

# Step 1: Given the user is on the login page
@given('the user is on the login page')
def step_given_user_on_login_page(context):
    print("Print User is on loginpage")
    pass

# Step 2: When the user enters valid/invalid username and password
@when('the user enters valid username and password')
@when('the user enters invalid username and password')
def step_when_user_enters_credentials(context):
    print('Print Code for valid and invalid')
    pass

# Step 3: Then the user should be logged in successfully
@then('the user should be logged in successfully')
def step_then_user_logged_in(context):
    print("Print Login in code")
    pass

# Step 4: Then the user should see an error message
@then('the user should see an error message')
def step_then_user_sees_error_message(context):
    assert 2==3,"INcorrect"
    print("Print Error login")
    pass
