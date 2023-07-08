from test import DriverFactory
from typing import Any

from behave import given, then, when

from pages.login_page import LoginPage


@given("I am on the login page")
def _(context: Any) -> None:
    context.driver = DriverFactory.get_driver(context.browser)
    context.driver.get(context.base_url)
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver, timeout=5)


@when("I enter {username} and {password}")
def _(context: Any, username: str, password: str) -> None:
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)


@when("press to login")
def _(context: Any) -> None:
    context.dashboard_page = context.login_page.submit_authorization()


@then("I should be {logged_in}")
def _(context: Any, logged_in: str) -> None:
    actual_url = context.driver.current_url
    assert str(actual_url == context.expected_url) == logged_in
