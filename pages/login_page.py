from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LogInPage(BasePage):
    def navigate_to_login_page(self):
        self.driver.get('http://almasanmihai.pythonanywhere.com/login')
