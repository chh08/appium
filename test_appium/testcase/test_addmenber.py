from test_appium.pages.app import App
from test_appium.pages.informatioin_page import InformationPage


class TestAddmenber:
    def setup(self):
        self.app = App()

    def test_addmenber(self):
        self.app.goto_main().goto_maillist_page().goto_addmenber_page().goto_writeinfo_page().write()