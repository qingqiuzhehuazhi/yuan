import pytest
import requests


def get_token():
    headers = {"Content-Type": "application/json;charset=utf8"}
    url = "http://testapi.intranet.aduer.com/common/v1/user/login"
    _data = {
        "password": "123456",
        "phone": "15306501195",
        "system": "operation",
        "type": "password"
    }
    res = requests.post(url=url, headers=headers, json=_data)
    print(res.json())
    token = res.json()["data"]["accessToken"]
    return token
