from test_frame.pages.basepage import BasePage
from test_frame.pages.memberinfo_page import MemberInfo
from test_frame.pages.search_page import SearchPage


class MaillistPage(BasePage):
    """通讯录类"""
    def goto_search(self):
        # 点击搜索
        self.parse_action("../pages/maillist_page.yaml", "goto_search")
        # 复用driver
        return SearchPage(self.driver)
