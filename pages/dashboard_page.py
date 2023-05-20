from pages.bases import SideBar


class DashboardPage(SideBar):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
