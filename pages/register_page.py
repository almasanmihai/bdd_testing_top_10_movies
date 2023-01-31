from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    # Locators
    def navigate_to_register_page(self):
        self.driver.get('http://almasanmihai.pythonanywhere.com/register')
