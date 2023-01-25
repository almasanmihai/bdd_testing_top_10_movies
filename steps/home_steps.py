from behave import *


@given('Home: I navigate on home page')
def step_impl(context):
    context.home_page.navigate_to_homepage()


@then('Home: I see login link')
def step_impl(context):
    context.home_page.verify_login_link()


@then('Home: The title is "{title}"')
def step_impl(context, title):
    context.home_page.verify_page_title(title)


@then('Home: The title url "{url}"')
def step_impl(context, url):
    context.home_page.verify_page_url(url)
