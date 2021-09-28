import time
import driver.driver_path as dr
from selenium.webdriver.common.by import By
from functions import Functions as Func


class StartLoginPage:
    driver = dr.driver
    func = Func
    @property
    def get_login_url(self):
        url = 'https://www.instagram.com/'
        return url

    @property
    def get_username(self):
        # username = self.driver.find_element(By.NAME, "username")
        username = self.driver.find_element_by_name('username')
        return username

    @property
    def get_password(self):
        # password = self.driver.find_element(By.NAME, "password")
        password = self.driver.find_element_by_name('password')
        return password

    @property
    def get_submit_btn(self):
        submit = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        return submit

    @property
    def ask_safe_data_btn(self):
        not_now = self.driver.find_element(By.XPATH, '//button[@class="sqdOP yWX7d    y3zKF     "]')
        return not_now

    @property
    def not_ask_send_notification(self):
        no_btn = self.driver.find_element(By.XPATH, '//div[@class="piCib"]//button[@class="aOOlW   HoLwm "]')
        return no_btn

    def lets_login(self, uname, pas):
        self.driver.get(self.get_login_url)
        self.driver.implicitly_wait(5)
        self.get_password.send_keys(pas)
        self.get_username.send_keys(uname)
        self.get_submit_btn.click()
        time.sleep(3)
        self.ask_safe_data_btn.click()
        time.sleep(3)
        self.not_ask_send_notification.click()


