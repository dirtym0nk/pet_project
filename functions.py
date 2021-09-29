from driver.driver_path import driver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Functions:

    def __init__(self):
        self.driver = driver

    def browser_quit(self):
        self.driver.quit()

    @staticmethod
    def if_xpath_exists(value):  # доработать
        try:
            value
        except NoSuchElementException:
            return False
        return True

    def wait(self, sec):
        timer = self.driver.implicitly_wait(sec)
        return timer

    # def explicit_expectation(self, locate):
    #     wait = WebDriverWait(driver, 10)
    #     try:
    #         element = WebDriverWait(driver, 5).until(
    #             EC.presence_of_element_located(locate)
    #         )
    #     finally:
    #         self.browser_quit()

    def implicitly_wait_some_time(self, value):
        self.driver.implicitly_wait(value)
