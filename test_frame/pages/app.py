from appium import webdriver

from test_frame.pages.informatioin_page import InformationPage


class App:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        caps = {}
        pass
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空缓存启动app
        caps["noReset"] = "true"
        # 设置等待页面空闲状态的时间为0s
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 显式等待10s
        self.driver.implicitly_wait(5)

    def goto_main(self):
        return InformationPage(self.driver)
