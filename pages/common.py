from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CommonPage:
    def __init__(self, driver):
        self.driver = driver

    def does_url_equal(self, url):
        try:
            WebDriverWait(self.driver, 5).until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False

    def check_for_alert(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False
