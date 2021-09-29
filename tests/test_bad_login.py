import time
from pers_data import pas, uname
from instagram_basic import Instagram as Inst
import pytest
import allure


class TestNegativeLogin:
    instagram = Inst()

    @allure.step("Шаг 1 - Проверка оповещения при вводе некорректных данных")
    @pytest.mark.negative_login
    def test_step1(self):
        self.instagram.login_page.negative_login(uname, pas)

    @allure.step('Шаг 2 - Ввод коррекных данных')
    @pytest.mark.login
    def test_step2(self):
        self.instagram.login_page.lets_login(uname, pas)
        self.instagram.functions.browser_quit()
