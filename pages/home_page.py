from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    # Locators
    LOGIN_LINK = (By.XPATH, '//a[text()="login"]')
    REGISTER_LINK = (By.XPATH, '//a[text()="register"]')
    WELCOME_BACK_TEXT = (By.XPATH, '//p[contains(text(), "Welcome back")]')

    def navigate_to_homepage(self):
        self.driver.get('http://almasanmihai.pythonanywhere.com/')

    def verify_login_link(self):
        self.wait_for_element(*self.LOGIN_LINK)
        assert self.driver.find_element(*self.LOGIN_LINK).is_displayed(), 'login link not displayed'

    def verify_register_link(self):
        self.wait_for_element(*self.REGISTER_LINK)
        assert self.driver.find_element(*self.REGISTER_LINK).is_displayed(), 'register link not displayed'

    def verify_welcome_back_text(self):
        self.wait_for_element(*self.WELCOME_BACK_TEXT)
        assert self.driver.find_element(*self.WELCOME_BACK_TEXT).is_displayed()
