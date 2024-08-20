from twitch.pages.android.main_page import MainPage
from  twitch.constants.global_data import STAR_CRAFT2


def test_starcraft_streamer(android_driver, switch_to_webview):
    twitch_main_page = MainPage(android_driver)
    twitch_main_page.open()
    search_page = twitch_main_page.header.open_search_page()
    search_page.enter_search_query(STAR_CRAFT2)
    starcraft2_page = search_page.click_search_result_starcraft2()
    assert starcraft2_page.verify_starcraft2_page_title_is_visible()
    starcraft2_page.scroll_down(2)
    streamer_page = starcraft2_page.select_first_visible_streamer()
    assert streamer_page.verify_page_is_loaded()
    streamer_page.take_screenshot()
