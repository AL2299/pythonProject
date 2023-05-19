import requests


class IhrmLoginApi(object):
    # 登录方法
    @classmethod
    def login(cls, json_data):
        url = "http://ihrm2-test.itheima.net/api/sys/login"
        header = {"Content-Type": "application/json"}
        resp = requests.post(url=url, headers=header, json=json_data)
        return resp


if __name__ == '__main__':
    data = {"mobile": "13800000002", "password": "123456"}
    resp = IhrmLoginApi.login(data)
    print(resp.json())
