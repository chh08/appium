from appium.webdriver.common.mobileby import MobileBy

from test_appium.pages.basepage import BasePage


class MaillistPage(BasePage):
    """通讯录类"""

    def goto_addmenber_page(self):
        """跳转添加联系人页"""
        #使用滑动定位
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("添加成员").instance(0));').click()
        self.parse_action("../pages/maillist_page.yaml", "goto_addmenber_page")

        from test_appium.pages.addmenber_page import AddPage
        return AddPage(self.driver)