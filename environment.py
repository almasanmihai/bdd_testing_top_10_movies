from pages.home_page import HomePage
from pages.contact_page import ContactPage
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.contact_page = ContactPage()


def after_all(context):
    context.browser.close()
