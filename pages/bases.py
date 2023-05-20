from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, timeout):
        self._driver = driver
        self._timeout = timeout


class SideBar(BasePage):
    def __init__(self, driver, timeout):
        # to avoid circular imports
        from pages.dashboard_page import DashboardPage
        from pages.admin_page import AdminPage
        super().__init__(driver, timeout)
        self._modules = {"dashboard": DashboardPage,
                         "admin": AdminPage}
        self._modules_locators = {
            "dashboard": "//a[@href='/web/index.php/dashboard/index']",
            "admin": "//a[@href='/web/index.php/admin/viewAdminModule']",
        }

    def get_module(self, module):
        if module in self._modules:
            return self._modules[module](self._driver, self._timeout)

    def open_module(self, module):
        """Returns page object of given module and opens corresponding web page"""

        if module in self._modules_locators:
            module_element = WebDriverWait(self._driver, self._timeout).until(
                EC.element_to_be_clickable((By.XPATH, self._modules_locators[module])))
            module_element.click()
            return self.get_module(module)
