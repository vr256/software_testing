from behave import given, when, then
from src.api_request import *


director = APIRequestDirector()


@given("I provided {file_path}")
def step_impl(context, file_path):
    context.path = file_path


@when("I send {function} request")
def step_impl(context, function):
    director.set_builder(context.builder)
    request = director.build_api_request(context.path)
    context.response = request.send()


@then("I should receive response with status code {status_code}")
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)


@then("displayed path {path_display}")
def step_impl(context, path_display):
    assert "path_display" in context.response.json()
    assert context.response.json()["path_display"] == path_display
