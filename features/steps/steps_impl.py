from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage


BASE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
EXPECTED_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'


@given("I am on the login page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(BASE_URL)
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
    assert str(actual_url == EXPECTED_URL) == logged_in
