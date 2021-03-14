import json
from typing import List, Dict

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_frame.conftest import log



class BasePage:
    # 定义一个字典，要替换得内容放在字典里
    _params = {}
    # 黑名单列表
    _blacklist = [(MobileBy.ID, 'com.tencent.wework:id/gu_')]
    # 次数上限
    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_click(self, by, locator):
        self.find(by, locator).click()

    def find(self, by, locator):
        log.info(f"find: by={by}, locator = {locator}")

        try:
            element = self.driver.find_element(by, locator)
            self._error_num = 0
            return element
        # 黑名单处理
        except Exception as e:
            self.driver.get_screenshot_as_file("tmp.png")
            allure.attach.file("tmp.png", attachment_type=allure.attachment_type.PNG)
            # 判断错误次数与次数上线，超过次数时抛出异常
            if self._error_num > self._max_num:
                # 重置次数
                self._error_num = 0
                raise e
            # 每次进except一次操作+1
            self._error_num += 1
            # 处理黑名单
            for ele in self._blacklist:
                # find_elements会返回元素的列表，如果没有会返回空列表
                eles = self.driver.find_elements(*ele)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(by, locator)
            # 如果黑名单处理完，仍然没有找到想要的元素，则抛出异常
            raise e

    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def find_sendkeys(self, by, locator, word):
        self.find(by, locator).send_keys(word)

    def wait(self, locator):
        """显示等待"""
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, locator))
        )

    def parse_action(self, path, fun_name):
        with open(path, "r", encoding="utf-8") as f:
            funciton = yaml.safe_load(f)
            steps: List[Dict] = funciton[fun_name]
        # json序列化与反序列化
        # json.dumps()序列化 python对象转化成字符串
        # JSON.load（）反序列化 python字符串转化成python对象
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace("${"+key+"}", value)
        steps = json.loads(raw)
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "find":
                self.find(step["by"], step["locator"])
            elif step["action"] == "find_sendkeys":
                self.find_sendkeys(step["by"], step["locator"], step["word"])
            elif step["action"] == "wait":
                self.wait(step["locator"])
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "swip_click":
                self.swip_click(step["text"])
