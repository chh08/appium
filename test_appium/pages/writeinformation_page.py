from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.pages.basepage import BasePage


class WriteinformationPage(BasePage):
    """填写信息类"""

    def write(self):
        """填写信息类"""
        # 填写姓名
        # self.driver.find_element_by_xpath('//*[@text="必填"]').send_keys('alex')
        # self.driver.find_element_by_xpath('//*[@text="手机号"]').send_keys('13111111111')
        # self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/av2"]').click()
        self.parse_action("../pages/writeinformation_page.yaml", "write")
        #使用显示等待
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.element_to_be_clickable((By.XPATH, '//*[@resource-id="com.tencent.wework:id/b2x"]'))
        # )
        # self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/b2x"]').click()
        #
        # self.driver.find_element_by_xpath('//*[@text="保存"]').click()

        from test_appium.pages.addmenber_page import AddPage
        return AddPage(self.driver)
