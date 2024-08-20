from twitch.pages.base_page import BasePage
from twitch.pages.android.starcraft2_page import StarCraft2Page
from appium.webdriver.common.appiumby import AppiumBy


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._input_search = (AppiumBy.XPATH, '//input')
        self._search_result_starcraft2 = (AppiumBy.XPATH, "//a[contains(@href, 'category/starcraft-ii')]")

    def enter_search_query(self, query):
        self.single_actions.input_text(self._input_search, query)

    def click_search_result_starcraft2(self):
        self.single_actions.click(self._search_result_starcraft2)
        return StarCraft2Page(self.driver)
