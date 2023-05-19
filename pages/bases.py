class BasePage:
    def __init__(self, driver, timeout):
        self._driver = driver
        self._timeout = timeout


class SideBar(BasePage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)

    def get_module(self, module):
        # to avoid circullar imports
        from pages.dashboard_page import DashboardPage
        from pages.admin_page import AdminPage

        modules = {"dashboard": DashboardPage,
                   "admin": AdminPage}
        if module in modules:
            return modules[module](self._driver, self._timeout)
