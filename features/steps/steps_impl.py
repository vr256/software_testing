import os
import sys

ROOT = os.path.abspath(os.path.join(__file__, "..", "..", ".."))
sys.path.insert(1, ROOT)

from behave import given, when, then
from src.api_request import *


path = None
director = APIRequestDirector()


class Feature:
    def __init__(self, builder):
        self.builder = builder

    @given("I provided {file_path}")
    def step_impl(self, context, file_path):
        global path
        path = file_path

    @when("I send {function} request")
    def step_impl(self, context, function):
        director.set_builder(self.builder)
        request = director.build_api_request(path)
        context.response = request.send()

    @then("I should receive response with {status_code}")
    def step_impl(self, context, status_code):
        assert context.response.status_code == int(status_code)


class UploadFileFeature(Feature):
    def __init__(self):
        super().__init__(APIRequestBuilderFactory.get_builder("upload"))


class GetFileMetadataFeature(Feature):
    def __init__(self):
        super().__init__(APIRequestBuilderFactory.get_builder("get_metadata"))

    @then("{path_display}")
    def step_impl(self, context, path_display):
        assert "path_display" in context.response.json()

        assert context.response.json()["path_display"] == path_display


class DeleteFileFeature(Feature):
    def __init__(self):
        super().__init__(APIRequestBuilderFactory.get_builder("delete"))
