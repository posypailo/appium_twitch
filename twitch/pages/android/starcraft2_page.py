from twitch.pages.base_page import BasePage
from twitch.pages.android.streamer_page import StreamerPage
from appium.webdriver.common.appiumby import AppiumBy
from twitch.constants.global_data import STAR_CRAFT2


class StarCraft2Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._page_title = (AppiumBy.XPATH, f"//h1[text()='{STAR_CRAFT2}']")
        self._stream_titles = (AppiumBy.XPATH, "//div/a[@class='ScCoreLink-sc-16kq0mq-0 gpIqoK tw-link']")

    def verify_starcraft2_page_title_is_visible(self):
        return self.single_actions.is_displayed(self._page_title)

    def select_first_visible_streamer(self):
        self.multiple_actions.click_first_visible_element(self._stream_titles)
        return StreamerPage(self.driver)
