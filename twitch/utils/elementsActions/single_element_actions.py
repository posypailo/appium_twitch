from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from twitch.utils.waits.single_element_wait_utils import SingleElementWaitUtils
from twitch.utils.logger import configure_logging
from twitch.constants.global_data import DEFAULT_TIMEOUT
import time


class SingleElementActions:
    def __init__(self, driver):
        self.wait_utils = SingleElementWaitUtils(driver)
        self.logger = configure_logging()

    def is_displayed(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            element = self.wait_utils.wait_for_element(locator, timeout)
            displayed = element.is_displayed()
            self.logger.info(f"Element {locator} is displayed: {displayed}")
            return displayed
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
            self.logger.error(f"Element {locator} is not displayed. Exception: {e}")
            return False

    def is_exist(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            self.wait_utils.wait_for_element(locator, timeout)
            self.logger.info(f"Element {locator} exists.")
            return True
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Element {locator} does not exist. Exception: {e}")
            return False

    def is_enabled(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            element = self.wait_utils.wait_for_element(locator, timeout)
            enabled = element.is_enabled()
            self.logger.info(f"Element {locator} is enabled: {enabled}")
            return enabled
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
            self.logger.error(f"Element {locator} is not enabled. Exception: {e}")
            return False

    def is_selected(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            element = self.wait_utils.wait_for_element(locator, timeout)
            selected = element.is_selected()
            self.logger.info(f"Element {locator} is selected: {selected}")
            return selected
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
            self.logger.error(f"Element {locator} is not selected. Exception: {e}")
            return False

    def click(self, locator, timeout=DEFAULT_TIMEOUT, retries=3):
        attempt = 0
        while attempt < retries:
            try:
                element = self.wait_utils.wait_for_element_to_be_clickable(locator, timeout)
                element.click()
                self.logger.info(f"Clicked on element with locator {locator}.")
                return
            except StaleElementReferenceException as e:
                self.logger.warning(
                    f"Stale element reference encountered when trying to click. Retrying... ({attempt + 1}/{retries})")
                attempt += 1
                time.sleep(1)
            except (NoSuchElementException, TimeoutException) as e:
                self.logger.error(f"Error clicking on element with locator {locator}. Exception: {e}")
                raise
        raise StaleElementReferenceException(
            f"Failed to click on element with locator {locator} after {retries} attempts.")

    def get_text(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            element = self.wait_utils.wait_for_element(locator, timeout)
            text = element.text
            self.logger.info(f"Text of element {locator}: {text}")
            return text
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
            self.logger.error(f"Error getting text of element with locator {locator}. Exception: {e}")
            raise

    def input_text(self, locator, text, timeout=DEFAULT_TIMEOUT):
        element = self.wait_utils.wait_for_element_to_be_clickable(locator, timeout)
        try:
            element.send_keys(text)
            self.logger.info(f"Sent text '{text}' to element with locator {locator} without clicking.")
            return
        except Exception as e:
            self.logger.warning(f"Failed to send keys directly to element {locator}. Exception: {e}")

        try:
            self.logger.info(f"Clicking on element {locator} and retrying to send keys.")
            element.click()
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Sent text '{text}' to element with locator {locator} after clicking.")
        except Exception as e:
            self.logger.error(f"Failed to send keys after clicking on element {locator}. Exception: {e}")
            raise
