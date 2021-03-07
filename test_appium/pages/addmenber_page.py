from appium.webdriver.webdriver import WebDriver

from test_appium.pages.basepage import BasePage
from test_appium.pages.writeinformation_page import WriteinformationPage


class AddPage(BasePage):
    """添加联系人类"""

    def goto_writeinfo_page(self):
        # self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.parse_action("../pages/addmenber_page.yaml", "goto_writeinfo_page")
        return WriteinformationPage(self.driver)