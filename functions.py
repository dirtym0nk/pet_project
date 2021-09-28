from driver.driver_path import driver
from selenium.common.exceptions import NoSuchElementException


class Functions:

    def __init__(self):
        self.driver = driver

    def browser_quit(self):
        self.driver.quit()

    # def if_xpath_exists(self, value):
    #     try:
    #         value
    #         exist = True
    #     except NoSuchElementException:
    #         exist = False
    #     return exist

    def wait(self, sec):
        timer = self.driver.implicitly_wait(sec)
        return timer
