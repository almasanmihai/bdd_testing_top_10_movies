from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    LOGIN_LINK = (By.XPATH, '//a[text()="login"]')

    def navigate_to_homepage(self):
        self.driver.get('http://almasanmihai.pythonanywhere.com/')

    def verify_login_link(self):
        self.wait_for_element(*self.LOGIN_LINK)
        assert self.driver.find_element(*self.LOGIN_LINK).is_displayed(), 'login link not displayed'

