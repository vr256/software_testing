from behave import given, when, then
from pages.login_page import LoginPage


@given("I am on the login page")
def step_impl(context):
    context.driver.get(context.base_url)
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver, timeout=5)


@when("I enter {username} and {password}")
def step_impl(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)


@when("press to login")
def step_impl(context):
    context.dashboard_page = context.login_page.submit_authorization()


@then("I should be {logged_in}")
def step_impl(context, logged_in):
    actual_url = context.driver.current_url
    assert str(actual_url == context.expected_url) == logged_in
