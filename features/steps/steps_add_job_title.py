from test import DriverFactory
from typing import Any

from behave import given, then, when

from pages.login_page import LoginPage


@given("I am logged in")
def _(context: Any) -> None:
    context.driver = DriverFactory.get_driver(context.browser)
    context.driver.get(context.base_url)
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver, timeout=5)
    context.login_page.enter_username(context.correct_username)
    context.login_page.enter_password(context.correct_password)
    context.dashboard_page = context.login_page.submit_authorization()
    context.admin_page = context.dashboard_page.open_page("admin")


@given("I am on the 'Job titles' page")
def _(context: Any) -> None:
    context.admin_page.view_job_titles()


@given("I pressed 'Add job'")
def _(context: Any) -> None:
    context.admin_page.press_add_job_title()


@when("I add job with {title}, {description}, {note}")
def _(context: Any, title, description, note) -> None:
    context.title = title
    context.admin_page.add_job_title(title, description, note)


@then("I should see it {is_visible}")
def _(context: Any, is_visible) -> None:
    is_present = context.admin_page.check_for_job_title(context.title)
    assert str(is_present) == is_visible
