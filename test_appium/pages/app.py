from appium import webdriver

from test_appium.pages.informatioin_page import InformationPage


class App:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        desired_caps = {}

        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        # 不清空缓存启动app
        desired_caps['noReset'] = 'true'
        # 设置等待页面空闲状态的时间为0s
        desired_caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def goto_main(self):
        return InformationPage(self.driver)