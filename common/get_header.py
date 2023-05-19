"""获取登录成功的令牌，拼接到请求头，返回"""

# 定义函数
import requests


def get_header():
    url = "http://ihrm2-test.itheima.net/api/sys/login"
    data = {"mobile": "13800000002", "password": "123456"}
    resp = requests.post(url=url, json=data)
    print(resp.json())
    # 从 响应体中，获取 data的值
    token = resp.json().get("data")

    header = {"Content-Type": "application/json",
              "Authorization": "Bearer " + token}

    return header
