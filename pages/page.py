from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
    def does_url_equal(self, url):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False

    def check_for_alert(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False

    def get_element(self, selector):
        return  WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    def click_element(self, selector):
        self.get_element(selector).click()

    def enter_text(self, selector, text):
        return self.get_element(selector).send_keys(text)

    def get_text(self, selector):
        return self.get_element(selector).text

    def does_element_appear(self, selector):
        try:
            self.get_element(selector)
            return True
        except TimeoutException:
            return False    
