from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.bases import BasePage
from pages.dashboard_page import DashboardPage


class LoginPage(BasePage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self._username_locator = "//input[@name='username']"
        self._password_locator = "//input[@name='password']"
        self._login_button_locator = "//button[contains(@class,'orangehrm-login-button')]"

    def enter_username(self, username):
        login_element = WebDriverWait(self._driver, self._timeout).until(
            EC.presence_of_element_located((By.XPATH, self._username_locator)))
        login_element.send_keys(username)
        return self

    def enter_password(self, password):
        password_element = WebDriverWait(self._driver, self._timeout).until(
            EC.presence_of_element_located((By.XPATH, self._password_locator)))
        password_element.send_keys(password)
        return self

    def submit_authorization(self):
        login_button_element = WebDriverWait(self._driver, self._timeout).until(
            EC.element_to_be_clickable((By.XPATH, self._login_button_locator)))
        login_button_element.click()
        return DashboardPage(self._driver, self._timeout)
