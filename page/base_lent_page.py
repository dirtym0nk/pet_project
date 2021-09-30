import driver.driver_path as dr
from selenium.webdriver.common.by import By


class BaseLentPage:
    driver = dr.driver

    @property
    def get_base_lent_url(self):
        url = 'https://www.instagram.com/'
        return url

    @property
    def search_input(self):
        areal_input = self.driver.find_element(By.XPATH, '//input[@class="XTCLo x3qfX "]')
        return areal_input

    @property
    def go_message(self):
        go_to_message_btn = self.driver.find_element(By.XPATH, '//a[@href="/direct/inbox/"]')
        return go_to_message_btn

    @property
    def exit_btn(self):
        btn = self.driver.find_element_by_xpath('//div[text()="Выйти"]')
        return btn

    def profile_mini_btn(self, uname):
        prof_min_btn = self.driver.find_element(By.XPATH, f'//img[@alt="Фото профиля {uname}"]')
        return prof_min_btn

    def accept_go_to_my_profile(self, uname):
        accept_btn = self.driver.find_element(By.XPATH, f'//a[@href="/{uname}/"]')
        return accept_btn

    def selector_of_found_person(self, person):
        selector_pers = self.driver.find_element_by_xpath(f'//a[@href="/{person}/"]')
        return selector_pers

    def go_to_self_profile(self, uname):
        self.profile_mini_btn(uname).click()
        self.driver.implicitly_wait(2)
        self.accept_go_to_my_profile(uname).click()

    def find_some_person(self, person):
        self.driver.refresh()
        self.driver.implicitly_wait(5)
        self.search_input.send_keys(person)
        self.driver.implicitly_wait(5)
        self.selector_of_found_person(person).click()


