from pers_data import pas, uname
from instagram_basic import Instagram as Inst
import pytest


class TestLogin:
    instagram = Inst()

    @pytest.mark.uitest
    @pytest.mark.login
    def test_login(self):
        self.instagram.login_page.lets_login(uname, pas)
        self.instagram.functions.browser_quit()
