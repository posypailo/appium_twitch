from twitch.utils.waits.multiple_elements_wait_utils import MultipleElementsWaitUtils
from twitch.utils.logger import configure_logging
from twitch.constants.global_data import DEFAULT_TIMEOUT
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException


class MultipleElementActions:
    def __init__(self, driver):
        self.elements_utils = MultipleElementsWaitUtils(driver)
        self.logger = configure_logging()

    def are_elements_displayed(self, locator, timeout=DEFAULT_TIMEOUT):
        elements = self.elements_utils.get_elements(locator, timeout)
        all_displayed = all(element.is_displayed() for element in elements)
        if all_displayed:
            self.logger.info(f"All elements {locator} are displayed: {all_displayed}")
        else:
            self.logger.warning(f"Not all elements {locator} are displayed.")
        return all_displayed

    def are_elements_enabled(self, locator, timeout=DEFAULT_TIMEOUT):
        elements = self.elements_utils.get_elements(locator, timeout)
        all_enabled = all(element.is_enabled() for element in elements)
        if all_enabled:
            self.logger.info(f"All elements {locator} are enabled: {all_enabled}")
        else:
            self.logger.warning(f"Not all elements {locator} are enabled.")
        return all_enabled

    def are_elements_selected(self, locator, timeout=DEFAULT_TIMEOUT):
        elements = self.elements_utils.get_elements(locator, timeout)
        all_selected = all(element.is_selected() for element in elements)
        if all_selected:
            self.logger.info(f"All elements {locator} are selected: {all_selected}")
        else:
            self.logger.warning(f"Not all elements {locator} are selected.")
        return all_selected

    def perform_action_on_elements(self, locator, action, timeout=DEFAULT_TIMEOUT):
        elements = self.elements_utils.get_elements(locator, timeout)
        for element in elements:
            try:
                action(element)
                self.logger.info(f"Performed action on element with locator {locator}.")
            except Exception as e:
                self.logger.error(f"Error performing action on element with locator {locator}. Exception: {e}")

    def get_elements_text(self, locator):
        """
        Get and return the list of texts from elements located by the given locator.

        :param locator: Locator tuple (By.XPATH, value) or other By strategies.
        :return: List of texts from the located elements.
        """
        elements = self.elements_utils.get_elements(locator)
        texts = [element.text for element in elements]
        self.logger.info(f"Texts of elements: {texts}")
        return texts

    def click_first_visible_element(self, locator, timeout=DEFAULT_TIMEOUT, retries=3):
        elements = self.elements_utils.get_elements(locator, timeout)

        for element in elements:
            if element.is_displayed():
                attempt = 0
                while attempt < retries:
                    try:
                        element_href = element.get_attribute('href')
                        element.click()
                        self.logger.info(f"Clicked on the first visible element: {element_href}")
                        return
                    except StaleElementReferenceException:
                        self.logger.warning("Stale element reference encountered. Retrying...")
                        elements = self.elements_utils.get_elements(locator, timeout)
                        element = elements[attempt]
                        attempt += 1
                    except ElementClickInterceptedException:
                        self.logger.warning("Element click intercepted. Trying the next element.")
                        break

        self.logger.error("No visible element found to click.")
        raise Exception("No visible element found to click")
