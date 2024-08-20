import pytest
from twitch.utils.driver_factory import DriverFactory
from twitch.configs.android_chrome_config import get_android_chrome_capabilities


@pytest.fixture(scope="session")
def android_driver():
    capabilities = get_android_chrome_capabilities()
    driver = DriverFactory.get_driver('android', capabilities)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def switch_to_webview(android_driver):
    contexts = android_driver.contexts
    print(f"Available contexts: {contexts}")

    for context in contexts:
        if "CHROMIUM" in context:
            android_driver.switch_to.context(context)
            print(f"Switched to {context}")
            break
