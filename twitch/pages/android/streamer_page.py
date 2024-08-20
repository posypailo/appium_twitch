from twitch.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class StreamerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._player_content = (AppiumBy.XPATH, "//div[contains(@class, 'playerContent-')]")
        self._button_play_pause = (AppiumBy.XPATH, "//button[@data-a-target='player-play-pause-button']")

    def verify_page_is_loaded(self):
        self.single_actions.click(self._player_content)
        return self.single_actions.is_displayed(self._button_play_pause)
