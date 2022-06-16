import requests
from testcase.request import get_token


class TestGetNewShop:

    def test_getNewShop(self, operation_fixture):
        """
        新增门店统计
        :param operation_fixture:
        :return:
        """
        token = get_token()
        url = "http://testapi.intranet.aduer.com/operation/v1/statistic/getNewShop"
        headers = {
            "Content-Type": "application/json;charset=utf8",
            "accessToken": token
        }
        params = {
            "currentPage": "1",
            "pageSize": "2"
        }
        rep = requests.get(url=url, params=params, headers=headers)
        print(rep.json())
