from behave import *

@given('Login: I navigate to login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()

@then('Login: I see navbar')
def step_impl(context):
    context.login_page.verify_navbar_home_link()
    context.login_page.verify_navbar_login_link()
    context.login_page.verify_navbar_register_link()
    context.login_page.verify_navbar_contact_link()