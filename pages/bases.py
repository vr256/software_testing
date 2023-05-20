from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, timeout):
        self._driver = driver
        self._timeout = timeout


class SidebarPage(BasePage):
    def __init__(self, driver, timeout):
        # to avoid circular imports
        from pages.dashboard_page import DashboardPage
        from pages.admin_page import AdminPage
        super().__init__(driver, timeout)
        self._pages = {
            "dashboard": DashboardPage,
            "admin": AdminPage
        }
        self._pages_locators = {
            "dashboard": "//a[@href='/web/index.php/dashboard/index']",
            "admin": "//a[@href='/web/index.php/admin/viewAdminModule']",
        }

    def get_page(self, page):
        if page in self._pages:
            return self._pages[page](self._driver, self._timeout)

    def open_page(self, page):
        """Returns page object of given module and opens corresponding web page"""

        if page in self._pages_locators:
            page_element = WebDriverWait(self._driver, self._timeout).until(
                EC.element_to_be_clickable((By.XPATH, self._pages_locators[page])))
            page_element.click()
            return self.get_page(page)
