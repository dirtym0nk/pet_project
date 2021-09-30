from pers_data import pas, uname, person
from selenium.common.exceptions import NoSuchElementException
from instagram_basic import Instagram as Inst
import pytest
import allure


class TestMovement:
    instagram = Inst()

    @allure.step('Шаг 1 - Логин под корректными данными')
    @pytest.mark.login
    def test_login(self):
        self.instagram.login_page.lets_login(uname, pas)

    @allure.step('Шаг 2 - Поиск человека и переход на его страницу')
    @pytest.mark.search
    def test_step2(self):
        self.instagram.lent_page.find_some_person(person)
        # with pytest.raises(NoSuchElementException):
        self.instagram.person_page.person_reels(person).click()
        self.instagram.functions.wait(5)
        self.instagram.person_page.person_igtv(person).click()
        self.instagram.functions.wait(5)

    @allure.step('Шаг 3 - Переход на свою страницу')
    @pytest.mark.self_page
    def test_step3(self):
        self.instagram.lent_page.go_to_self_profile(uname)
        self.instagram.functions.wait(4)
        # with pytest.raises(NoSuchElementException):
        self.instagram.self_profile.self_igtv(uname).click()
        self.instagram.self_profile.exit()
        self.instagram.functions.browser_quit()




