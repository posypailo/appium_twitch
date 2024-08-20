from appium.options.android import UiAutomator2Options
# import os


def get_android_chrome_capabilities():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        appActivity='com.google.android.apps.chrome.Main',
        browserName='Chrome',
        # chromedriverExecutable=os.path.abspath(os.path.join(os.path.dirname(__file__), '../drivers/chromedriver.exe')),
        chromeOptions={
            'args': ['--disable-fre',
                     '--no-first-run',
                     '--no-default-browser-check',
                     '--disable-notifications',
                     '--disable-popup-blocking']
        }
    )
    return UiAutomator2Options().load_capabilities(capabilities)
