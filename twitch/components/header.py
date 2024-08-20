from appium.webdriver.common.appiumby import AppiumBy
from twitch.pages.base_page import BasePage
from twitch.pages.android.search_page import SearchPage


class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._button_search = (AppiumBy.XPATH, '//a[@href="/search"]')

    def open_search_page(self):
        self.single_actions.click(self._button_search)
        return SearchPage(self.driver)
