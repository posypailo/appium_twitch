from appium import webdriver


class DriverFactory:
    @staticmethod
    def get_driver(platform, capabilities):
        appium_server_url = 'http://localhost:4723'
        print(f"Creating driver for platform: {platform}")
        return webdriver.Remote(appium_server_url, options=capabilities)
