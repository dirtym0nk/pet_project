import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import driver.driver_path as dr
from selenium.webdriver.common.by import By
from functions import Functions as Func


class SelfProfile:
    driver = dr.driver

    def self_publications(self, uname):
        publications = self.driver.find_element_by_xpath(f'//a[@href="/{uname}/"]')
        return publications

    def self_igtv(self, uname):
        igtv = self.driver.find_element_by_xpath(f'//a[@href="/{uname}/channel/"]')
        return igtv

    def self_saved_posts(self, uname):
        posts = self.driver.find_element_by_xpath(f'//a[@href="/{uname}/saved/"]')
        return posts

    def self_followers(self, uname):
        followers = self.driver.find_element_by_xpath(f'//a[@href="/{uname}/followers/"]')
        return followers

    def self_following(self, uname):
        following = self.driver.find_element_by_xpath(f'//a[@href="/{uname}/following/"]')

    def self_profile_edit(self):
        edit_profile = self.driver.find_element_by_xpath(f'//a[@href="/accounts/edit/"]')
        return edit_profile

    def home_button(self):
        button = self.driver.find_element_by_xpath('//a[@href="/"]')
        return button

    @property
    def param_btn(self):
        btn = self.driver.find_element_by_xpath('//button[@class="wpO6b  "]')
        return btn

    @property
    def in_param_exit_btn(self):
        btn = self.driver.find_element_by_xpath('//div[@class="mt3GC"]/button[text()="Выйти"]')
        return btn

    def exit(self):
        self.param_btn.click()
        self.in_param_exit_btn.click()