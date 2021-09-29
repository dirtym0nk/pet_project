import time
from pers_data import pas, uname
from instagram_basic import Instagram as Inst
import pytest


class TestNegativeLogin:
    instagram = Inst()

    @pytest.mark.uitest
    @pytest.mark.negative_login
    def test_step1(self):
        self.instagram.login_page.negative_login(uname, pas)
        time.sleep(5)
        self.instagram.functions.browser_quit()
#  в работе
