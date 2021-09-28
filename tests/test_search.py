from pers_data import pas, uname, person
from instagram_basic import Instagram as Inst
import pytest
import allure


class TestSearch:
    instagram = Inst()

    @allure.step("Шаг 1 - Логин под своими данными")
    @pytest.mark.login
    def test_step1(self):
        self.instagram.login_page.lets_login(uname, pas)

    @allure.step("Шаг 2 - Переход в свой профиль/поиск")
    @pytest.mark.search
    def test_step2(self):
        self.instagram.lent_page.find_some_person(person)
        self.instagram.functions.browser_quit()
