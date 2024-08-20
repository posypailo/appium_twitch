from twitch.pages.base_page import BasePage
from twitch.components.header import Header


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)

    def open(self):
        self.driver.get("https://www.twitch.tv/")
        self.wait_for_page_to_load()

