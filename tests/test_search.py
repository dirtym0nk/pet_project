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

    @allure.step("Шаг 2 - Переход на свою страницу")
    @pytest.mark.go_to_self_page
    def test_step2(self):
        self.instagram.lent_page.go_to_self_profile(uname)
        self.instagram.functions.implicitly_wait_some_time(5)

    @allure.step("Шаг 3 - Поиск")
    @pytest.mark.search
    def test_step3(self):
        self.instagram.lent_page.find_some_person(person)
        self.instagram.person_page.person_reels(person).click()
        self.instagram.functions.browser_quit()
