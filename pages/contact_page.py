from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ContactPage(BasePage):
    # Locators
    EMAIL_LINK = (By.XPATH, '//a[@href="mailto:almasanmihai@gmail.com"]')

    def navigate_to_contact(self):
        self.driver.get('http://almasanmihai.pythonanywhere.com/contact')

    def verify_email_link(self):
        self.wait_for_element(*self.EMAIL_LINK)
        assert self.driver.find_element(*self.EMAIL_LINK).is_displayed(), 'email link not displayed'
