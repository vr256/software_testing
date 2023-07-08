from typing import Any, Optional, Protocol

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: Any, timeout: float | int = 1.5) -> None:
        self._driver = driver
        self._timeout = timeout


class SidebarProtocol(Protocol):
    _driver: Any
    _timeout: float | int
    _options: dict[str, Any]
    _options_locators: dict[str, str]

    def get_page(self, option: str) -> Optional[BasePage]:
        ...

    def open_page(self, option: str) -> Optional[BasePage]:
        ...


class SidebarMixin:
    """Mixin class for sidebar options and page navigation"""

    def __init__(self) -> None:
        # to avoid circular imports
        from pages.admin_page import AdminPage
        from pages.dashboard_page import DashboardPage

        self._options = {"dashboard": DashboardPage, "admin": AdminPage}
        self._options_locators = {
            "dashboard": "//a[@href='/web/index.php/dashboard/index']",
            "admin": "//a[@href='/web/index.php/admin/viewAdminModule']",
        }

    def get_page(self: SidebarProtocol, option: str) -> Optional[BasePage]:
        """Return page object of given sidebar option"""

        if option in self._options:
            return self._options[option](self._driver, self._timeout)
        else:
            return None

    def open_page(self: SidebarProtocol, option: str) -> Optional[BasePage]:
        """Return page object of given sidebar option and open corresponding web page"""

        if option in self._options_locators:
            option_element = WebDriverWait(self._driver, self._timeout).until(
                EC.element_to_be_clickable((By.XPATH, self._options_locators[option]))
            )
            option_element.click()
            return self.get_page(option)
        else:
            return None
