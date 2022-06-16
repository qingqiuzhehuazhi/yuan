from testcase.request import get_token
import requests


class TestGetActiveShop:

    def test_getActiveShop(self, operation_fixture):
        """
        首页
        :param operation_fixture:
        :return:
        """
        token = get_token()
        url = "http://testapi.intranet.aduer.com/operation/v1/statistic/getActiveShop"
        params = {
            "currentPage": "1",
            "pageSize": "5"
        }
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "accessToken": token
        }
        res = requests.get(url=url, headers=headers, params=params)
        print(res.json())
        assert res.json()["code"] == 0
        if res.json()["totalCount"] != 2 and res.json()["code"] == 0:
            print("失败")
        else:
            print("成功")




