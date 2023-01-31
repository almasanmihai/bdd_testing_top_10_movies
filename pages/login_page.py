from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LogInPage(BasePage):
    # Locators
    EMAIL_INPUT = (By.XPATH, '//input[@id="email"]')
    PSW_INPUT = (By.XPATH, '//input[@id="password"]')
    LOG_ME_IN_BUTTON = (By.XPATH, '//input[@id="submit"]')

    def navigate_to_login_page(self):
        self.driver.get('http://almasanmihai.pythonanywhere.com/login')

    def input_email(self, email):
        self.wait_for_element(*self.EMAIL_INPUT)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def input_pswd(self, pswd):
        self.wait_for_element(*self.PSW_INPUT)
        self.driver.find_element(*self.PSW_INPUT).send_keys(pswd)

    def click_log_me_in(self):
        self.wait_for_element(*self.LOG_ME_IN_BUTTON)
        self.driver.find_element(*self.LOG_ME_IN_BUTTON).click()
