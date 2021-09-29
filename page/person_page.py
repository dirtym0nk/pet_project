import driver.driver_path as dr
from selenium.webdriver.common.by import By


class PersonPage:
    driver = dr.driver

    def person_reels(self, person):
        reels = self.driver.find_element_by_xpath(f'//a[@href="/{person}/reels/"]')
        return reels

    def person_igtv(self, person):
        igtv = self.driver.find_element_by_xpath(f'//a[@href="/{person}/channel/"]')
        return igtv

    def person_targets(self, person):
        targets = self.driver.find_element_by_xpath(f'//a[@href="/{person}/tagged/"]')
        return targets
