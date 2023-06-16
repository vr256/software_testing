from typing import Any

from pages.bases import BasePage, SidebarMixin


class DashboardPage(BasePage, SidebarMixin):
    def __init__(self, driver: Any, timeout: float | int = 1.5) -> None:
        BasePage.__init__(self, driver, timeout)
        SidebarMixin.__init__(self)
