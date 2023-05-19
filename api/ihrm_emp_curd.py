"""
员工管理模块的 接口对象层
"""
import requests


class IhrmEmpCURD(object):
    # 添加员工
    @classmethod
    def add_emp(cls, header, json_data):
        url = "http://ihrm2-test.itheima.net/api/sys/user"
        resp = requests.post(url=url, headers=header, json=json_data)
        return resp

    # 查询员工
    @classmethod
    def query_emp(cls, emp_id, header):
        url = "http://ihrm2-test.itheima.net/api/sys/user/" + emp_id
        resp = requests.get(url=url, headers=header)
        return resp

    # 修改员工
    @classmethod
    def modify_emp(cls, emp_id, header, modify_data):
        url = "http://ihrm2-test.itheima.net/api/sys/user/" + emp_id
        resp = requests.put(url=url, headers=header, json=modify_data)
        return resp

    # 删除员工
    @classmethod
    def delete_emp(cls, emp_id, header):
        url = "http://ihrm-test.itheima.net/api/sys/user/" + emp_id
        resp = requests.delete(url=url, headers=header)
        return resp


if __name__ == '__main__':
    header = {"Content-Type": "application/json", "Authorization": "Bearer 6abac104-84f4-4821-8000-69fd37065a54"}
    data_add = {
        "username": "业务猪001",
        "mobile": "1397873477",
        "workNumber": "9527"
    }
    resp = IhrmEmpCURD.add_emp(header, data_add)
    print("添加：", resp.json())

    emp_id = "1659277312094384128"
    resp = IhrmEmpCURD.query_emp(emp_id, header)
    print("查询：", resp.json())

    data = {"username": "齐天大圣"}
    resp = IhrmEmpCURD.modify_emp(emp_id, header, data)
    print("修改：", resp.json())

    resp = IhrmEmpCURD.delete_emp(emp_id, header)
    print("删除：", resp.json())
