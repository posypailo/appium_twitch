from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from twitch.utils.logger import configure_logging
from twitch.constants.global_data import DEFAULT_TIMEOUT


class SingleElementWaitUtils:
    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout
        self.logger = configure_logging()

    def wait_for_element(self, locator, timeout=None):
        timeout = timeout or self.timeout
        try:
            self.logger.info(f"Waiting for element {locator} for up to {timeout} seconds.")
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            self.logger.info(f"Element {locator} found.")
            return element
        except TimeoutException:
            self.logger.error(f"Element {locator} not found within {timeout} seconds.")
            raise

    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        timeout = timeout or self.timeout
        try:
            self.logger.info(f"Waiting for element {locator} to be clickable for up to {timeout} seconds.")
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            self.logger.info(f"Element {locator} is clickable.")
            return element
        except TimeoutException:
            self.logger.error(f"Element {locator} not clickable within {timeout} seconds.")
            raise

    def wait_for_element_to_disappear(self, locator, timeout=None):
        timeout = timeout or self.timeout
        try:
            self.logger.info(f"Waiting for element {locator} to disappear for up to {timeout} seconds.")
            result = WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
            self.logger.info(f"Element {locator} disappeared.")
            return result
        except TimeoutException:
            self.logger.error(f"Element {locator} did not disappear within {timeout} seconds.")
            raise

    def wait_for_text_to_be_present_in_element(self, locator, text, timeout=None):
        timeout = timeout or self.timeout
        try:
            self.logger.info(f"Waiting for text '{text}' to be present in element {locator} for up to {timeout} seconds.")
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            self.logger.info(f"Text '{text}' is present in element {locator}.")
            return result
        except TimeoutException:
            self.logger.error(f"Text '{text}' not present in element {locator} within {timeout} seconds.")
            raise

    def fluent_wait(self, condition, timeout=None, poll_frequency=0.5):
        timeout = timeout or self.timeout
        try:
            self.logger.info(f"Starting fluent wait for condition with timeout {timeout} seconds and poll frequency {poll_frequency} seconds.")
            result = WebDriverWait(self.driver, timeout, poll_frequency).until(condition)
            self.logger.info("Condition met.")
            return result
        except TimeoutException:
            self.logger.error("Condition not met within the timeout period.")
            raise
