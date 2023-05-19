from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

import time

# make browser factory

BASE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
LOGIN = 'Admin'
PASSWORD = 'admin123'


def run():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    login_page = LoginPage(driver, timeout=5)
    login_page.enter_username(LOGIN)
    login_page.enter_password(PASSWORD)
    dashboard_page = login_page.submit_authorization()
    admin_page = dashboard_page.open_module('admin')
    admin_page.view_job_titles()
    time.sleep(5)
    driver.close()


if __name__ == '__main__':
    run()
