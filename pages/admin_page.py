from typing import Any, Self

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.bases import BasePage, SidebarMixin


class AdminPage(BasePage, SidebarMixin):
    def __init__(self, driver: Any, timeout: float | int = 1.5) -> None:
        BasePage.__init__(self, driver, timeout)
        SidebarMixin.__init__(self)
        # Job drowdown menu
        self._job_locator = "//li[@class='oxd-topbar-body-nav-tab --parent']"
        self._job_titles_locator = "//ul[@class='oxd-dropdown-menu']/li[1]"
        # Add/delete job buttons
        self._button_add_job_title_locator = "//button[contains(@class,'oxd-button')]"
        self._button_confim_deletion_locator = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
        # Job data entry
        self._enter_job_title_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'
        self._enter_job_description_locator = "//textarea[@placeholder='Type description here']"
        self._enter_notes_locator = "//textarea[@placeholder='Add note']"
        self._button_save_locator = "//button[contains(@class,'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')]"

    def view_job_titles(self) -> Self:
        # Click on "Job" dropdown menu first
        job_menu = WebDriverWait(self._driver, self._timeout).until(
            EC.element_to_be_clickable((By.XPATH, self._job_locator)))
        job_menu.click()
        # Then select "Job titles" option
        jot_titles_option = WebDriverWait(self._driver, self._timeout).until(
            EC.element_to_be_clickable((By.XPATH, self._job_titles_locator)))
        jot_titles_option.click()
        return self

    def press_add_job_title(self) -> Self:
        add_job_title_button = WebDriverWait(self._driver, self._timeout).until(
            EC.element_to_be_clickable((By.XPATH, self._button_add_job_title_locator)))
        add_job_title_button.click()
        return self

    def add_job_title(self, title: str, description: str, note: str) -> Self:
        # Enter title
        enter_job_title = WebDriverWait(self._driver, self._timeout).until(
            EC.presence_of_element_located((By.XPATH, self._enter_job_title_locator)))
        enter_job_title.send_keys(title)
        # Enter description
        enter_job_description = WebDriverWait(self._driver, self._timeout).until(
            EC.presence_of_element_located((By.XPATH, self._enter_job_description_locator)))
        enter_job_description.send_keys(description)
        # Enter note
        enter_notes = WebDriverWait(self._driver, self._timeout).until(
            EC.presence_of_element_located((By.XPATH, self._enter_notes_locator)))
        enter_notes.send_keys(note)
        # Click "save"
        button_save = WebDriverWait(self._driver, self._timeout).until(
            EC.element_to_be_clickable((By.XPATH, self._button_save_locator)))
        button_save.click()
        return self

    def check_for_job_title(self, title: str) -> bool:
        job_title_locator = f"//div[contains(text(), '{title}')]"
        try:
            WebDriverWait(self._driver, self._timeout).until(
                EC.presence_of_element_located((By.XPATH, job_title_locator)))
        except TimeoutException:
            return False
        else:
            return True

    def delete_job_title(self, title: str) -> Self:
        # Find job with given title
        button_delete_job_title_locator = f"""//div[contains(text(), '{title}')]/parent::div/following-sibling::\
            div//button[@class='oxd-icon-button oxd-table-cell-action-space' and .//i[@class='oxd-icon bi-trash']]"""
        button_delete_job_title = WebDriverWait(self._driver, self._timeout).until(
            EC.element_to_be_clickable((By.XPATH, button_delete_job_title_locator)))
        # Click "delete"
        button_delete_job_title.click()
        button_confim_deletion = WebDriverWait(self._driver, self._timeout).until(
            EC.element_to_be_clickable((By.XPATH, self._button_confim_deletion_locator)))
        # Confirm deletion
        button_confim_deletion.click()
        return self
