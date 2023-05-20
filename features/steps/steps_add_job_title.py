from behave import given, when, then
from pages.login_page import LoginPage
from test import DriverFactory


@given("I am logged in")
def step_impl(context):
    context.driver = DriverFactory.get_driver(context.browser)
    context.driver.get(context.base_url)
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver, timeout=5)
    context.login_page.enter_username(context.correct_username)
    context.login_page.enter_password(context.correct_password)
    context.dashboard_page = context.login_page.submit_authorization()
    context.admin_page = context.dashboard_page.open_page('admin')


@given("I am on the 'Job titles' page")
def step_impl(context):
    context.admin_page.view_job_titles()


@given("I pressed 'Add job'")
def step_impl(context):
    context.admin_page.press_add_job_title()


@when("I add job with {title}, {description}, {note}")
def step_impl(context, title, description, note):
    context.title = title
    context.admin_page.add_job_title(title, description, note)


@then("I should see it {is_visible}")
def step_impl(context, is_visible):
    is_present = context.admin_page.check_for_job_title(context.title)
    assert str(is_present) == is_visible
