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
        areal_input = self.driver.find_element(By.XPATH, '//input[@class="XTCLo x3qfX"]')
        return areal_input

    @property
    def go_message(self):
        go_to_message_btn = self.driver.find_element(By.XPATH, '//a[@class="xWeGp"]')
        return go_to_message_btn

    @property
    def profile_mini_btn(self):
        prof_min_btn = self.driver.find_element(By.XPATH, '//div[@class="XrOey"]/span')
        return prof_min_btn

    @property
    def accept_go_to_my_profile(self):
        accept_btn = self.driver.find_element(By.XPATH, '//div[@class="_01UL2"]/a[@class="-qQT3"]'
                                                        '/div[@class="            qF0y9          Igw0E'
                                                        '   rBNOH        eGOV_     ybXk5    _4EzTm      '
                                                        '                                                 '
                                                        '                            XfCBB          HVWg4   '
                                                        '               La5L3 ZUqME"]')
        return accept_btn

    @property
    def selector_of_found_person(self):
        selector_pers = self.driver.find_element(By.XPATH, '//div[@class="yPP5B"]/div/div/div')
        return selector_pers

    def go_to_self_profile(self):
        self.profile_mini_btn.click()
        self.accept_go_to_my_profile.click()

    def find_some_person(self, person):
        self.search_input.click()
        self.search_input.send_keys(person)
        self.search_input.send_keys("ENTER")
        self.search_input.send_keys("ENTER")