from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.page import Page


class LoginPage(Page):
    USERNAME = "[data-qa-id='email-input']"
    PASSWORD = "[data-qa-id='password-input']"
    BTN_LOGIN = "[data-qa-id='login-btn']"
    TEXT_ERROR = "[data-qa-id='error-display']"
    ERROR_HELP = "[data-qa-id='error-display'] a"
    LINK_HELP = "[data-qa-id='need-help-link']"
    BUTTON_PW_RESET = "[data-qa-id='password-reset-submit-btn']"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def enter_username(self, username):
        Page.enter_text(self, self.USERNAME, username)

    def enter_password(self, password):
        Page.enter_text(self, self.PASSWORD, password)

    def click_log_in(self):
        Page.click_element(self, self.BTN_LOGIN)

    def get_error_text(self):
        return Page.get_text(self, self.TEXT_ERROR)

    def click_help_link(self):
        Page.click_element(self, self.LINK_HELP)

    def click_help_link_error(self):
        Page.click_element(self, self.ERROR_HELP)

    def password_reset_button_appears(self):
        return Page.does_element_appear(self, self.BUTTON_PW_RESET)
