from pages.bases import SidebarPage


class DashboardPage(SidebarPage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
