from pages.home_page import HomePage
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()


def after_all(context):
    context.browser.close()
