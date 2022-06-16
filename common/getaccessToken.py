import json
import pytest
import requests
import yaml


def get_token():
    """
    请求登录接口，获取token
    :return:
    """
    headers = {"Content-Type": "application/json;charset=utf8"}
    url = "http://testapi.intranet.aduer.com/common/v1/user/login"
    _data = {
        "password": "123456",
        "phone": "15306501195",
        "system": "operation",
        "type": "password"
    }
    res = requests.post(url=url, headers=headers, json=_data).text
    res = json.loads(res)
    accessToken = res['data']["accessToken"]
    print("accessToken" + accessToken)
    write_yaml(accessToken)


def write_yaml(accessToken):
    """
    写入yaml文件
    :param token:
    :return:
    """
    t_data = {
        "accessToken": accessToken
    }
    with open("../accessToken.yaml", "w", encoding="utf-8") as f:
        yaml.dump(data=t_data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    token = get_token()  # 获取token
