from test_frame.pages.basepage import BasePage
from test_frame.pages.memberinfo_page import MemberInfo


class SearchPage(BasePage):
    """搜索页类"""
    def search_member(self, name):
        """搜索成员"""
        self._params["name"] = name
        self.parse_action("../pages/search_page.yaml", "search_member")
        return MemberInfo(self.driver)



