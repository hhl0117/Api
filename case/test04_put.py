import requests
import unittest


class TestPut(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://127.0.0.1:8000/api/departments/"
        self.header = {"Content-Type": "application/json"}
        pass
    def tearDown(self) -> None:
        pass
    def test03put(self):

        url03 = self.url + "python01/"

        data03 = r'{"data":[{"dep_id":"python01","dep_name":"Test学院","master_name":"Test-Master","slogan":"HereisSlogan"}]}'
        res03 = requests.put(url=url03,data=data03.encode('utf-8'),headers=self.header)

        code_act03 = res03.status_code

        code_expect03 = '200'

        self.assertEqual(str(code_act03), code_expect03)

    def test04put(self):

        url04 = self.url + "python02/"

        data04 = r'{"data":[{"dep_id":"python01","dep_name":"Test学院","master_name":"Test-Master","slogan":"HereisSlogan"}]}'
        res04 = requests.put(url=url04,data=data04.encode('utf-8'),headers=self.header)

        code_act04 = res04.status_code

        code_expect04 = '404'

        self.assertEqual(str(code_act04), code_expect04)

