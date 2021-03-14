from test_frame.pages.app import App


class TestDleMember:
    def setup(self):
        self.app = App()

    def test_del(self):
        name = "jojo"
        editpage = self.app.goto_main().goto_maillist_page().goto_search().search_member(name).goto_editmember()
        editpage.del_member()
        editpage.verify_ok()