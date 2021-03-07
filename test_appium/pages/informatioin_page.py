from appium import webdriver

from test_appium.pages.basepage import BasePage
from test_appium.pages.maillist_page import MaillistPage


class InformationPage(BasePage):
    """定义信息页类"""

    def goto_maillist_page(self):
        """定义跳转通讯录方法"""
        # self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        self.parse_action("../pages/information_page.yaml", "goto_maillist_page")
        # 复用driver
        return MaillistPage(self.driver)