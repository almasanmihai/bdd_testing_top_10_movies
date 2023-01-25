from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase


class BasePage(Browser, TestCase):
    def wait_for_element(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))

    def verify_page_title(self, expected):
        actual_title = self.driver.title
        assert actual_title == expected, 'title do not match'

    def verify_page_url(self, expected):
        actual_url = self.driver.current_url
        assert actual_url == expected, 'url do not match'
