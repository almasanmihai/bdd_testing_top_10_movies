from behave import *


@given('Contact: I navigate on contact page')
def step_impl(context):
    context.contact_page.navigate_to_contact()


@then('Contact: I see email link')
def step_impl(context):
    context.contact_page.verify_email_link()


@then('Contact: I see navbar')
def step_impl(context):
    context.contact_page.verify_navbar()
