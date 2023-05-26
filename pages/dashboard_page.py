from pages.bases import BasePage, SidebarMixin


class DashboardPage(BasePage, SidebarMixin):
    def __init__(self, driver, timeout):
        BasePage.__init__(self, driver, timeout)
        SidebarMixin.__init__(self)
