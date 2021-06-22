import requests
import unittest

class TestPost01(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://127.0.0.1:8000/api/departments/"
        self.header = {"Content-Type": "application/json"}
        pass
    def tearDown(self) -> None:
        pass

    # 001-正向用例-所有必选参数填写正常值，不填写可选参数
    def test01post(self):
        data01 = \
            {
                        "data": [
                                {
                                    "dep_id":"T01",
                                    "dep_name":"Test学院",
                                    "master_name":"Test-Master"
                                }
                          ]
                    }

        res01 = requests.post(self.url,json=data01,headers=self.header)

        print("学院-新增1结果为：",res01.text)

    # HTTP请求-002-逆向用例-dep_id缺失
    def test02post(self):
        data02 = \
            {
                "data": [
                    {
                        "dep_name": "Test学院",
                        "master_name": "Test-Master",
                        "slogan": "Here is Slogan"
                    }
                ]
            }

        res02 = requests.post(self.url,json=data02,headers=self.header)

        print("学院-新增2结果为：",res02.text)

    # HTTP请求-003-逆向用例-dep_name缺失
    def test03post(self):

        data03 = \
            {
                "data": [
                    {
                        "dep_id": "T006",
                        "master_name": "Test-Master",
                        "slogan": "Here is Slogan"
                    }
                ]
            }

        res03 = requests.post(self.url,json=data03,headers=self.header)

        print("学院-新增3结果为：",res03.text)

    # HTTP请求-004-逆向用例-master_name缺失
    def test04post(self):

        data04 = \
            {
                "data": [
                    {
                        "dep_id": "T007",
                        "dep_name": "Test",
                        "slogan": "Here is Slogan"
                    }
                ]
            }

        res04 = requests.post(self.url,json=data04,headers=self.header)

        print("学院-新增4结果为：",res04.text)

    # HTTP请求-005-正向向用例-多一个参数
    def test05post(self):

        data05 = \
    {
                "data": [
                        {
                            "dep_id":"T005",
                            "dep_name":"Test学院",
                            "master_name":"Test-Master",
                            "slogan":"Here is Slogan",
                            "other":"other"
                        }
                  ]
            }

        res05 = requests.post(self.url,json=data05,headers=self.header)

        print("学院-新增5结果为：",res05.text)

    # HTTP请求-006-逆向用例-dep_id类型错误
    def test06post(self):

        data06 = \
            {
                        "data": [
                                {
                                    "dep_id":True,
                                    "dep_name":"Test学院",
                                    "master_name":"Test-Master",
                                    "slogan":"Here is Slogan"
                                }
                          ]
                    }

        res06 = requests.post(self.url,json=data06,headers=self.header)

        print("学院-新增6结果为：",res06.text)

    # HTTP请求-007-逆向用例-dep_name类型错误
    def test07post(self):

        data07 = \
            {
                        "data": [
                                {
                                    "dep_id":"T008",
                                    "dep_name":True,
                                    "master_name":"Test-Master",
                                    "slogan":"Here is Slogan"
                                }
                          ]
                    }

        res07 = requests.post(self.url,json=data07,headers=self.header)
        print("学院-新增7结果为：",res07.text)

    # HTTP请求-008-逆向用例-master_name类型错误
    def test08post(self):

        data08 = \
            {
                        "data": [
                                {
                                    "dep_id":"T009",
                                    "dep_name":"softtest",
                                    "master_name":True,
                                    "slogan":"Here is Slogan"
                                }
                          ]
                    }

        head = {"Content-Type":"application/json"}

        res08 = requests.post(self.url,json=data08,headers=self.header)

        print("学院-新增8结果为：",res08.text)

    # HTTP请求-009-逆向用例-.可选参数类型错误
    def test09post(self):

        data09 = \
            {
                        "data": [
                                {
                                    "dep_id":"T0010",
                                    "dep_name":"softtest",
                                    "master_name":"王",
                                    "slogan":True
                                }
                          ]
                    }

        res09 = requests.post(self.url,json=data09,headers=self.header)

        print("学院-新增9结果为：",res09.text)

    # HTTP请求-010-逆向用例-添加一组合法另一组不合法的数据
    def test10post(self):

        data010 = \
            {
                        "data": [
                                {
                                    "dep_id":"T044",
                                    "dep_name":"softtest",
                                    "master_name":"王",
                                    "slogan":"Test yourself!"
                                } ,
                                {
                                    "dep_id":True,
                                    "dep_name":True,
                                    "master_name":True,
                                    "slogan":True
                                }
                          ]
                    }

        res010 = requests.post(self.url,json=data010,headers=self.header)

        print("学院-新增10结果为：",res010.text)

    # HTTP请求-011-正向用例-添加两组合法数据
    def test11post(self):

        data011 = \
            {
                        "data": [
                                {
                                    "dep_id":"T042",
                                    "dep_name":"softtest",
                                    "master_name":"王五",
                                    "slogan":"Test yourself!"
                                } ,
                                {
                                    "dep_id":"T043",
                                    "dep_name":"softtest",
                                    "master_name":"麻子",
                                    "slogan":"Test yourself!"
                                }
                          ]
                    }

        res011 = requests.post(self.url,json=data011,headers=self.header)

        print("学院-新增11结果为：",res011.text)