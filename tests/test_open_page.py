import time
from selenium.webdriver.common.by import By
from selenium import webdriver


def login():
    driver = webdriver.Chrome('/home/alexey/Документы/hohoho/driver/chromedriver')
    url = "https://www.instagram.com/"
    driver.get(url)
    time.sleep(5)
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("123556")
    password.send_keys("8947392")
    time.sleep(10)
    password.send_keys()
