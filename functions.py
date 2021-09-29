from driver.driver_path import driver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Functions:

    def __init__(self):
        self.driver = driver

    def browser_quit(self):
        self.driver.quit()

    def if_xpath_exists(self, value):  # доработать
        try:
            self.driver.implicitly_wait(5)
            self.driver.find_element(value)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    def wait(self, sec):
        timer = self.driver.implicitly_wait(sec)
        return timer

    def explicit_expectation(self, locate):
        wait = WebDriverWait(driver, 10)
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(locate)
            )
        finally:
            self.browser_quit()

    def implicitly_wait_some_time(self, value):
        self.driver.implicitly_wait(value)
