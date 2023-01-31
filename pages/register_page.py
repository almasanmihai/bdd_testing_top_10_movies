from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    # Locators
    REGISTER_TEXT = (By.XPATH, '//h1[text()="Register"]')

    def navigate_to_register_page(self):
        self.driver.get('http://almasanmihai.pythonanywhere.com/register')

    def verify_register_text(self):
        self.wait_for_element(*self.REGISTER_TEXT)
        assert self.driver.find_element(*self.REGISTER_TEXT).is_displayed(), 'Register heading is not displayed'
