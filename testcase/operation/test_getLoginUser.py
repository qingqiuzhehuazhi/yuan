import requests
from testcase.request import get_token


class TestGetLoginUser:

    def test_getLoginUser(self, operation_fixture):
        """
        账户中心
        :param operation_fixture:
        :return:
        """
        token = get_token()
        url = "http://testapi.intranet.aduer.com/operation/v1/user/getLoginUser"
        headers = {
            "Content-Type": "application/json;charset=utf8",
            "accessToken": token
        }
        rep = requests.get(url=url, params=None, headers=headers)
        print(rep.json())
        assert rep.json()["code"] == 0
        assert rep.json()["status"] == 0 and rep.json()["data"]["phone"] == "15306501195"
        if rep.json()["status"] == 0 and rep.json()["data"]["phone"] == "15306501195":
            print("通过")
        else:
            print("失败")
