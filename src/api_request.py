import json
import requests

from abc import ABCMeta, abstractmethod
from . import ACCESS_TOKEN


class EmptyRequest(Exception):
  pass


class APIRequest:
    def __init__(self):
        self.url = None
        self.header = None
        self.body = None

    def send(self):
       if None not in (self.url, self.header, self.body):
          return requests.post(url=self.url, headers=self.header, data=self.body)
       else:
          raise EmptyRequest('The request is empty')


class APIRequestBuilder(metaclass=ABCMeta):
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
    def set_header(self):
        ...

    @abstractmethod
    def set_body(self):
        ...

    @abstractmethod
    def get_request(self):
        ...


class UploadFileRequestBuilder(APIRequestBuilder):
    def __init__(self, api_request):
        self.api_request = api_request

    def reset(self):
        self.api_request.url = None
        self.api_request.header = None
        self.api_request.body = None

    def set_url(self):
        self.api_request.url = 'https://content.dropboxapi.com/2/files/upload'

    def set_header(self, path, mode='add', autorename=True, mute=False):
        self.api_request.header = {
            'Authorization': f'Bearer {ACCESS_TOKEN}',
            'Content-Type': 'application/octet-stream',
            'Dropbox-API-Arg': json.dumps({
                'path': path,
                'mode': mode,
                'autorename': autorename,
                'mute': mute
            })
        }

    def set_body(self, file_path):
        self.api_request.body  = open(file_path, 'rb').read()
        
    def get_request(self):
        return self.api_request
    

class GetFileMetadataRequestBuilder(APIRequestBuilder):
  def __init__(self, api_request):
    self.api_request = api_request

  def reset(self):
    self.api_request.url = None
    self.api_request.header = None
    self.api_request.body = None

  def set_url(self):
    self.api_request.url = 'https://api.dropboxapi.com/2/sharing/get_file_metadata'

  def set_header(self):
    self.api_request.header = {
      'Authorization': f'Bearer {ACCESS_TOKEN}',
      'Content-Type': 'application/json'
    }

  def set_body(self, path):
    self.api_request.body = json.dumps({
      'path': path
    })

  def get_request(self):
    return self.api_request


class DeleteFileRequestBuilder(APIRequestBuilder):
  def __init__(self, api_request):
    self.api_request = api_request

  def reset(self):
    self.api_request.url = None
    self.api_request.header = None
    self.api_request.body = None

  def set_url(self):
    self.api_request.url = 'https://api.dropboxapi.com/2/files/delete_v2'

  def set_header(self):
    self.api_request.header = {
      'Authorization': f'Bearer {ACCESS_TOKEN}',
      'Content-Type': 'application/json'
    }

  def set_body(self, path):
    self.api_request.body = json.dumps({
      'path': path
    })

  def get_request(self):
    return self.api_request



class APIRequestDirector:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def build_api_request(self):
        self.builder.set_url()
        self.builder.set_header('/test.txt')
        self.builder.set_body('test.txt')
        self.builder.get_request()

    
class APIRequestBuilderFactory:
    @staticmethod
    def get_builder(builder):
        builders = {
            'upload': UploadFileRequestBuilder, 
            'get_metadata': GetFileMetadataRequestBuilder,
            'delete': DeleteFileRequestBuilder,
                 }
        if builder.lower() not in builders:
            return False
        api_request = APIRequest()
        return builders[builder.lower()](api_request)