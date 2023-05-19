import unittest

from api.ihrm_emp_curd import IhrmEmpCURD
from common.assert_util import assert_util
from common.db_util import DBUtil
from common.get_header import get_header
from common.read_json_util import read_json_data
from config import TEL, BASE_DIR

from parameterized import parameterized


class TestEmpAddParams(unittest.TestCase):
    # 类属性
    header = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.header = get_header()

    def setUp(self) -> None:
        # 删除手机号
        delete_sql = f"delete from bs_user where mobile = '{TEL}'"
        DBUtil.uid_db(delete_sql)

    def tearDown(self) -> None:
        # 删除手机号
        delete_sql = f"delete from bs_user where mobile = '{TEL}'"
        DBUtil.uid_db(delete_sql)

    path_filename = BASE_DIR + "/data/add_emp.json"

    # 通用测试方法 - 实现参数化
    @parameterized.expand(read_json_data(path_filename))
    def test_add_emp(self, desc, json_data, stauts_code, success, code, message):

        # 调用自己封装的 接口
        resp = IhrmEmpCURD.add_emp(self.header, json_data)
        print(desc, "：", resp.json())

        # 断言
        assert_util(self, resp, stauts_code, success, code, message)