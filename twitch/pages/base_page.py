from twitch.utils.logger import configure_logging
from twitch.utils.elementsActions.single_element_actions import SingleElementActions
from twitch.utils.elementsActions.multiple_elements_actions import MultipleElementActions
from selenium.webdriver.support.ui import WebDriverWait
from twitch.constants.global_data import DEFAULT_TIMEOUT
from datetime import datetime
import time
import os


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = configure_logging()
        self.single_actions = SingleElementActions(driver)
        self.multiple_actions = MultipleElementActions(driver)

    def wait_for_page_to_load(self, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
        self.logger.info("Page is successfully loaded.")

    def scroll_down(self, n=1):
        screen_size = self.driver.get_window_size()
        screen_width = screen_size['width']
        screen_height = screen_size['height']

        for i in range(n):
            self.driver.execute_script('mobile: scrollGesture', {
                'left': 0,
                'top': 0,
                'width': screen_width,
                'height': screen_height,
                'direction': 'down',
                'percent': 1.0,
                'speed': 1000
            })

    def create_bookmark_and_get_title(self):
        """
        Prompts the user to bookmark the current page and returns the title of the page.
        """
        try:
            self.driver.execute_script("window.alert('Press Ctrl+D to bookmark this page.');")
            time.sleep(2)

            self.driver.switch_to.alert.accept()
            time.sleep(1)

            page_title = self.driver.title
            self.logger.info(f"Bookmark created for page with title: {page_title}")
            return page_title

        except Exception as e:
            self.logger.error(f"An error occurred while creating the bookmark: {e}")
            return None

    def take_screenshot(self, file_name=None):
        """
        Takes a screenshot of the current page and saves it to the 'screenshots' directory inside the 'twitch' folder.

        :param file_name: Optional name of the file. If not provided, the current timestamp will be used.
        :return: The file path of the saved screenshot.
        """
        root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'twitch'))
        directory = os.path.join(root_directory, 'screenshots')

        if not os.path.exists(directory):
            os.makedirs(directory)

        if not file_name:
            file_name = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

        file_path = os.path.join(directory, file_name)

        try:
            self.driver.get_screenshot_as_file(file_path)
            self.logger.info(f"Screenshot saved to {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to take screenshot. Exception: {e}")
            raise

        return file_path
