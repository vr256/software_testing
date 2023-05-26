from abc import ABCMeta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, timeout):
        self._driver = driver
        self._timeout = timeout


class SidebarMixin(metaclass=ABCMeta):
    """Mixin class for sidebar options and page navigation"""

    def __init__(self):
        # to avoid circular imports
        from pages.dashboard_page import DashboardPage
        from pages.admin_page import AdminPage

        self._options = {
            "dashboard": DashboardPage,
            "admin": AdminPage
        }
        self._options_locators = {
            "dashboard": "//a[@href='/web/index.php/dashboard/index']",
            "admin": "//a[@href='/web/index.php/admin/viewAdminModule']",
        }

    def get_page(self, option):
        """Return page object of given sidebar option"""
        if option in self._options:
            return self._options[option](self._driver, self._timeout)

    def open_page(self, option):
        """Return page object of given sidebar option and open corresponding web page"""

        if option in self._options_locators:
            option_element = WebDriverWait(self._driver, self._timeout).until(
                EC.element_to_be_clickable((By.XPATH, self._options_locators[option])))
            option_element.click()
            return self.get_page(option)
