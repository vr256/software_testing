import base64
import requests
import os


APP_KEY = "r0vgi9wz99ikbjk"
APP_SECRET = "fn5634v8muig30k"
REFRESH_TOKEN = "PP9slB-rKjYAAAAAAAAAAW3fDVvRA0lgfXmfCMx_Vg30ZaZy5NBZOVKr_wfhIWUz"
ROOT = os.path.abspath(os.path.join(__file__, "..", "..", ".."))


def get_access_token():
    url = "https://api.dropboxapi.com/oauth2/token"
    auth = base64.b64encode((APP_KEY + ":" + APP_SECRET).encode()).decode()
    data = {"grant_type": "refresh_token", "refresh_token": REFRESH_TOKEN}
    headers = {"Authorization": "Basic " + auth}
    response = requests.post(url, data=data, headers=headers)
    return response.json()["access_token"]


ACCESS_TOKEN = get_access_token()
