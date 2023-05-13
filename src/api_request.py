import json
import requests
import os

from abc import ABCMeta, abstractmethod
from . import ACCESS_TOKEN, ROOT


__all__ = [
    "APIRequestBuilderFactory",
    "APIRequestDirector",
    "DeleteFileRequestBuilder",
    "GetFileMetadataRequestBuilder",
    "UploadFileRequestBuilder",
    "APIRequestBuilder",
    "APIRequest",
    "EmptyRequest",
]


class EmptyRequest(Exception):
    """Raises when the request is empty"""

    pass


class APIRequest:
    def __init__(self):
        self.url = None
        self.headers = None
        self.body = None

    def send(self):
        if None not in (self.url, self.headers, self.body):
            return requests.post(url=self.url, headers=self.headers, data=self.body)
        else:
            raise EmptyRequest("The request is empty")


class APIRequestBuilder(metaclass=ABCMeta):
    """Builder interface"""

    @abstractmethod
    def __init__(self, api_request):
        ...

    @abstractmethod
    def reset(self):
        ...

    @abstractmethod
    def set_url(self):
        ...

    @abstractmethod
    def set_headers(self, path):
        ...

    @abstractmethod
    def set_body(self, path):
        ...

    @abstractmethod
    def get_request(self):
        ...


class UploadFileRequestBuilder(APIRequestBuilder):
    def __init__(self, api_request):
        self.api_request = api_request

    def reset(self):
        self.api_request.url = None
        self.api_request.headers = None
        self.api_request.body = None

    def set_url(self):
        self.api_request.url = "https://content.dropboxapi.com/2/files/upload"

    def set_headers(self, path):
        self.api_request.headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/octet-stream",
            "Dropbox-API-Arg": json.dumps(
                {
                    "path": path,
                    "mode": "add",
                    "autorename": True,
                    "mute": False,
                    "strict_conflict": False,
                }
            ),
        }

    def set_body(self, path):
        self.api_request.body = open(os.path.join(ROOT, path[1:]), "rb").read()

    def get_request(self):
        return self.api_request


class GetFileMetadataRequestBuilder(APIRequestBuilder):
    def __init__(self, api_request):
        self.api_request = api_request

    def reset(self):
        self.api_request.url = None
        self.api_request.headers = None
        self.api_request.body = None

    def set_url(self):
        self.api_request.url = "https://api.dropboxapi.com/2/sharing/get_file_metadata"

    def set_headers(self, path):
        self.api_request.headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }

    def set_body(self, path):
        # getting file id first using get_metadata API call
        url = "https://api.dropboxapi.com/2/files/get_metadata"
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }
        body = json.dumps({"path": path})
        response = requests.post(url=url, headers=headers, data=body)
        id = response.json()["id"]
        # using id to make get_file_metadata API call
        self.api_request.body = json.dumps({"file": id})

    def get_request(self):
        return self.api_request


class DeleteFileRequestBuilder(APIRequestBuilder):
    def __init__(self, api_request):
        self.api_request = api_request

    def reset(self):
        self.api_request.url = None
        self.api_request.headers = None
        self.api_request.body = None

    def set_url(self):
        self.api_request.url = "https://api.dropboxapi.com/2/files/delete_v2"

    def set_headers(self, path):
        self.api_request.headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }

    def set_body(self, path):
        self.api_request.body = json.dumps({"path": path})

    def get_request(self):
        return self.api_request


class APIRequestDirector:
    """Defines order of builder"s methods execution"""

    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def build_api_request(self, path):
        self.builder.reset()
        self.builder.set_url()
        self.builder.set_headers(path)
        self.builder.set_body(path)
        return self.builder.get_request()


class APIRequestBuilderFactory:
    @staticmethod
    def get_builder(builder):
        builders = {
            "Upload file": UploadFileRequestBuilder,
            "Get file metadata": GetFileMetadataRequestBuilder,
            "Delete file": DeleteFileRequestBuilder,
        }
        if builder not in builders:
            return None
        api_request = APIRequest()
        return builders[builder](api_request)
