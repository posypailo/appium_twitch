from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from twitch.utils.logger import configure_logging
from twitch.constants.global_data import DEFAULT_TIMEOUT


class MultipleElementsWaitUtils:
    def __init__(self, driver, default_timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.default_timeout = default_timeout
        self.logger = configure_logging()

    def get_elements(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located(locator))
            self.logger.info(f"Found elements with locator {locator}.")
            return elements
        except TimeoutException as e:
            self.logger.error(f"Timeout while waiting for elements with locator {locator}. Exception: {e}")
            raise

    def wait_for_elements_to_be_present(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(lambda x: len(x.find_elements(*locator)) > 0)
            self.logger.info(f"Elements are present with locator {locator}.")
            return True
        except TimeoutException as e:
            self.logger.error(f"Timeout while waiting for elements with locator {locator}. Exception: {e}")
            raise
