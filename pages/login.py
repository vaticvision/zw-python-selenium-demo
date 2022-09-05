from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class LoginPage:
    USERNAME = "[data-qa-id='email-input']"
    PASSWORD = "[data-qa-id='password-input']"
    BTN_LOGIN = "[data-qa-id='login-btn']"
    TEXT_ERROR = "[data-qa-id='error-display']"
    ERROR_HELP = "[data-qa-id='error-display'] a"
    LINK_HELP = "[data-qa-id='need-help-link']"

    BUTTON_PW_RESET = "[data-qa-id='password-reset-submit-btn']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.USERNAME)))
        el.send_keys(username)

    def enter_password(self, password):
        el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.PASSWORD)))
        el.send_keys(password)

    def click_log_in(self):
        el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.BTN_LOGIN)))
        el.click()

    def get_error_text(self):
        el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.TEXT_ERROR)))
        return el.text

    def click_help_link(self):
        el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.LINK_HELP)))
        el.click()

    def click_help_link_error(self):
        el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.ERROR_HELP)))
        el.click()

    def password_reset_button_appears(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.BUTTON_PW_RESET)))
            return True
        except TimeoutException:
            return False
