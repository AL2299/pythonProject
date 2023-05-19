import logging
import unittest

from api.ihrm_emp_curd import IhrmEmpCURD
from common.db_util import DBUtil
from common.get_header import get_header


class TestEmpQuery(unittest.TestCase):
    header = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.header = get_header()

    def setUp(self) -> None:
        insert_sql = "insert into bs_user(id, mobile, username) values('11232738248634', '13974837801', '随便打打');"
        DBUtil.uid_db(insert_sql)

    def tearDown(self) -> None:
        delete_sql = "delete from bs_user where id = '11232738248634';"
        DBUtil.uid_db(delete_sql)

    # 测试 查询员工
    def test01_query_emp(self):
        # 使用 数据库 切实存在的 emp_id 传入
        resp = IhrmEmpCURD.query_emp("11232738248634", self.header)
        print("查询员工：", resp.json())
