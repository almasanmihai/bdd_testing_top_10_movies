from behave import *


@given('Home: I navigate on home page')
def step_impl(context):
    context.home_page.navigate_to_homepage()


@then('Home: I see login link')
def step_impl(context):
    context.home_page.verify_login_link()

@then('Home: I see register link')
def step_impl(context):
    context.home_page.verify_register_link()


@then('Home: The title is "{title}"')
def step_impl(context, title):
    context.home_page.verify_page_title(title)


@then('Home: The title url "{url}"')
def step_impl(context, url):
    context.home_page.verify_page_url(url)

@then('Home: I see home in navbar')
def step_impl(context):
    context.home_page.verify_home_navbar()

@then('Home: I see login in navbar')
def step_impl(context):
    context.home_page.verify_login_navbar()

@then('Home: I see register in navbar')
def step_impl(context):
    context.home_page.verify_register_navbar()

@then('Home: I see contact in navbar')
def step_impl(context):
    context.home_page.verify_contact_navbar()



