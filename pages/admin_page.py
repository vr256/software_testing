from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.bases import SideBar


class AdminPage(SideBar):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self._job_locator = "//span[text()='Job']"
        self._job_titles_locator = "//a[text()='Job Titles']"

    def open_module(self, module):
        '''Returns page object of given module and opens corresponding web page'''

        modules_locators = {
            "dashboard": "//a[@href='/web/index.php/dashboard/index']"
        }
        if module in modules_locators:
            module_element = WebDriverWait(self._driver, self._timeout).until(
                EC.element_to_be_clickable((By.XPATH, modules_locators[module])))
            module_element.click()
            return self.get_module(module)

    def view_job_titles(self):
        action = ActionChains(self._driver)
        menu = WebDriverWait(self._driver, self._timeout).until(
            EC.element_to_be_clickable((By.XPATH, self._job_locator)))
        action.click(menu).perform()

        option = WebDriverWait(self._driver, self._timeout).until(
            EC.element_to_be_clickable((By.XPATH, self._job_titles_locator)))
        action.click(option).perform()

        return self
