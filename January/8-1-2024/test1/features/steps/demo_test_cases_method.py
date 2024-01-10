# -- FILE: features/steps/example_steps.py
from behave import *

@given('credentials are given')
def step_impl(context):
    pass

@when('we input correct credentials')
def step_impl(context, number):  
    assert 2==2,"This eq is not correct"

@then('Login will be successful')
def step_impl(context):
    print("Login successful")