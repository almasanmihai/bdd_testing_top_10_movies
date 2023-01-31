from behave import *


@given('Login: I navigate to login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('Login: I enter email "{email}"')
def step_impl(context, email):
    context.login_page.input_email(email=email)


@when('Login: I enter password "{pswd}"')
def step_impl(context, pswd):
    context.login_page.input_pswd(pswd=pswd)

@when('Login: I click on Log Me In')
def step_impl(context):
    context.login_page.click_log_me_in()


@then('Login: I see navbar')
def step_impl(context):
    context.login_page.verify_navbar_home_link()
    context.login_page.verify_navbar_login_link()
    context.login_page.verify_navbar_register_link()
    context.login_page.verify_navbar_contact_link()
