from test_frame.pages.basepage import BasePage
from test_frame.pages.editmember_page import EditMember


class MemberInfo(BasePage):
    """个人信息"""
    def goto_editmember(self):
        self.parse_action("../pages/memberinfo_page.yaml", "goto_editmember")
        return EditMember(self.driver)