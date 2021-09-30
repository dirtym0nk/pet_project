from page.start_login_page import StartLoginPage as LoginPage
from page.person_page import PersonPage
from driver.driver_path import driver
from page.base_lent_page import BaseLentPage as LentPage
from page.self_profile_page import SelfProfile
from functions import Functions as Func


class Instagram:
    def __init__(self):
        self.login_page = LoginPage()
        self.lent_page = LentPage()
        self.functions = Func()
        self.person_page = PersonPage()
        self.driver = driver
        self.self_profile = SelfProfile()







