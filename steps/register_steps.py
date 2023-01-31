from behave import *


@given('Register: I navigate on register page')
def step_impl(context):
    context.register_page.navigate_to_register_page()


@then('Register: I see navbar')
def step_impl(context):
    context.register_page.verify_navbar_home_link()
    context.register_page.verify_navbar_login_link()
    context.register_page.verify_navbar_register_link()
    context.register_page.verify_navbar_contact_link()

@then('Register: I see Register text heading')
def step_impl(context):
    context.register_page.verify_register_text()
