from behave import *

#Context is used to share the data across the different test step methods

@given('we have behave installed')
def step_impl_behave_installed(context):
    print("We Have Behave installed")

@when('we implement a test')
def step_impl_implement_a_test(context):
    print("We Implement a test")


@then('behave will test it for us!')
def step_impl_(context):
    print("Behave Will Test for us")

