from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.bases import SideBar


class DashboardPage(SideBar):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)

    def open_module(self, module):
        ''' Returns page object of given module and opens corresponding web page'''

        modules_locators = {
            'admin': "//a[@href='/web/index.php/admin/viewAdminModule']"
        }
        if module in modules_locators:
            module_element = WebDriverWait(self._driver, self._timeout).until(
                EC.element_to_be_clickable((By.XPATH, modules_locators[module])))
            module_element.click()
            return self.get_module(module)
