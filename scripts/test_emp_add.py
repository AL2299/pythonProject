import unittest

from api.ihrm_emp_curd import IhrmEmpCURD
from common.assert_util import assert_util
from common.db_util import DBUtil
from common.get_header import get_header
from config import TEL


class TestEmpAdd(unittest.TestCase):
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

    # 必选参数
    def test01_add_emp(self):
        json_data = {
            "username": "业务猪001",
            "mobile": TEL,
            "workNumber": "9527"
        }
        # 调用自己封装的 接口
        resp = IhrmEmpCURD.add_emp(self.header, json_data)
        print("添加-必选：", resp.json())

        # 断言
        assert_util(self, resp, 200, True, 10000, "操作成功")

    # 组合参数
    def test02_add_emp(self):
        # 准备数据
        json_data = {
            "username": "业务猪001",
            "mobile": TEL,
            "workNumber": "9527",
            "formOfEmployment": "2"
        }
        # 调用自己封装的 接口
        resp = IhrmEmpCURD.add_emp(self.header, json_data)
        print("添加-组合：", resp.json())

        # 断言
        assert_util(self, resp, 200, True, 10000, "操作成功")

    # 全部参数
    def test03_add_emp(self):
        # 准备数据
        json_data = {"username": "大猪乔治",
                     "mobile": TEL,
                     "timeOfEntry": "2021-12-01", "formOfEmployment": 1,
                     "workNumber": "777888", "departmentName": "测试",
                     "departmentId": "1452603344685203456",
                     "correctionTime": "2021-12-30T16:00:00.000Z"}
        # 调用自己封装的 接口
        resp = IhrmEmpCURD.add_emp(self.header, json_data)
        print("添加 - 全部 =", resp.json())

        # 断言
        assert_util(self, resp, 200, True, 10000, "操作成功")
