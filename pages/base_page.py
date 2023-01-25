from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase
from selenium.webdriver.common.by import By


class BasePage(Browser, TestCase):
    HOME_NAVBAR = (By.XPATH, '//a[text()="Home"]/parent::li/parent::ul')
    LOGIN_NAVBAR = (By.XPATH, '//a[text()="Log In"]/parent::li/parent::ul')
    REGISTER_NAVBAR = (By.XPATH, '//a[text()="Register"]/parent::li/parent::ul')
    CONTACT_NAVBAR = (By.XPATH, '//a[text()="Contact"]/parent::li/parent::ul')

    def wait_for_element(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))

    def verify_page_title(self, expected):
        actual_title = self.driver.title
        assert actual_title == expected, 'title do not match'

    def verify_page_url(self, expected):
        actual_url = self.driver.current_url
        assert actual_url == expected, 'url do not match'

    def verify_navbar(self):
        self.wait_for_element(*self.HOME_NAVBAR)
        assert self.driver.find_element(*self.HOME_NAVBAR).is_displayed(), 'home in navbar not displayed'
        assert self.driver.find_element(*self.LOGIN_NAVBAR).is_displayed(), 'login in navbar not displayed'
        assert self.driver.find_element(*self.REGISTER_NAVBAR).is_displayed(), 'register in navbar not displayed'
        assert self.driver.find_element(*self.CONTACT_NAVBAR).is_displayed(), 'contact in navbar not displayed'
