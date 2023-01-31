from pages.home_page import HomePage
from pages.contact_page import ContactPage
from pages.login_page import LogInPage
from pages.register_page import RegisterPage
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.contact_page = ContactPage()
    context.login_page = LogInPage()
    context.register_page = RegisterPage()


def after_all(context):
    context.browser.close()
