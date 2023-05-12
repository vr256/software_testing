import base64
import requests


APP_KEY = 'f3wsei6pijitdbr'
APP_SECRET = 'onx1i4yg6xcq7ml'
REFRESH_TOKEN = 'tEjo45F0q9gAAAAAAAAAAf0gVDDhIAu3FAtUCRaIoIQPfpOWNX_hlEMBLKp9bBK8'


def get_access_token():
    url = 'https://api.dropboxapi.com/oauth2/token'
    auth = base64.b64encode((APP_KEY + ':' + APP_SECRET).encode()).decode()
    data = {'grant_type': 'refresh_token', 
            'refresh_token': REFRESH_TOKEN}
    headers = {'Authorization': 'Basic ' + auth}
    response = requests.post(url, data=data, headers=headers)
    return response.json()['access_token']


ACCESS_TOKEN = get_access_token()