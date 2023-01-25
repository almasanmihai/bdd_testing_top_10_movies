from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    # Locators
    LOGIN_LINK = (By.XPATH, '//a[text()="login"]')
    REGISTER_LINK = (By.XPATH, '//a[text()="register"]')
    HOME_NAVBAR = (By.XPATH, '//a[text()="Home"]')
    LOGIN_NAVBAR = (By.XPATH, '//a[text()="Log In"]')
    REGISTER_NAVBAR = (By.XPATH, '//a[text()="Register"]')
    CONTACT_NAVBAR = (By.XPATH, '//a[text()="Contact"]')

    def navigate_to_homepage(self):
        self.driver.get('http://almasanmihai.pythonanywhere.com/')

    def verify_login_link(self):
        self.wait_for_element(*self.LOGIN_LINK)
        assert self.driver.find_element(*self.LOGIN_LINK).is_displayed(), 'login link not displayed'

    def verify_register_link(self):
        self.wait_for_element(*self.REGISTER_LINK)
        assert self.driver.find_element(*self.REGISTER_LINK).is_displayed(), 'register link not displayed'

    def verify_home_navbar(self):
        self.wait_for_element(*self.HOME_NAVBAR)
        assert self.driver.find_element(*self.HOME_NAVBAR).is_displayed(), 'home navbar not displayed'

    def verify_login_navbar(self):
        self.wait_for_element(*self.LOGIN_NAVBAR)
        assert self.driver.find_element(*self.LOGIN_NAVBAR).is_displayed(), 'login navbar not displayed'

    def verify_register_navbar(self):
        self.wait_for_element(*self.REGISTER_NAVBAR)
        assert self.driver.find_element(*self.REGISTER_NAVBAR).is_displayed(), 'register navbar not displayed'

    def verify_contact_navbar(self):
        self.wait_for_element(*self.CONTACT_NAVBAR)
        assert self.driver.find_element(*self.CONTACT_NAVBAR).is_displayed(), 'contact navbar not displayed'

