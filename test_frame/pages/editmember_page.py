from test_frame.pages.basepage import BasePage


class EditMember(BasePage):
    """编辑成员"""
    def del_member(self):
        # 删除成员
        self.parse_action("../pages/editmember_page.yaml", "del_member")

    def verify_ok(self):
        # 验证删除成功
        for ele in self._list:
            eles = self.driver.find_elements(*ele)
            a = len(eles)
            assert a == 0



