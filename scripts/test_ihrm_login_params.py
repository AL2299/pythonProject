
import unittest



from api.ihrm_login_api import IhrmLoginApi
from common.assert_util import assert_util
from common.read_json_util import read_json_data

from parameterized import parameterized

from config import BASE_DIR

"""
1. 导包 from parameterized import parameterized
2. 在 通用测试方法上一行，添加 @parameterized.expand()
3. 给 expand() 传入 元组列表数据（ 调用 自己封装的 读取 json 文件的 函数 read_json_data() ）
4. 修改 通用测试方法形参，与 json 数据文件中的 key 一致。
5. 在 通用测试方法内，使用形参
"""


class TestIhrmLoginParams(unittest.TestCase):

    path_filename = BASE_DIR + "/data/ihrm_login.json"

    # 通用测试方法（实现参数化）
    @parameterized.expand(read_json_data(path_filename))
    def test_login(self, desc, req_data, stauts_code, success, code, message):
        # 调用自己封装的接口
        resp = IhrmLoginApi.login(req_data)
        print(desc, "：", resp.json())

        # 断言
        assert_util(self, resp, stauts_code, success, code, message)

