import requests
import unittest


class TestGet(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://127.0.0.1:8000/api/departments/"
        self.header = {"Content-Type": "application/json"}
        pass
    def tearDown(self) -> None:
        pass

    def test01get(self):
        url01 = self.url + "python01/"

        res01 = requests.get(url=url01)

        code_act01 = res01.status_code

        code_expect01 = '200'

        self.assertEqual(str(code_act01), code_expect01)

    def test02get(self):
        url02 = self.url + "python/"

        res02 = requests.get(url=url02)

        code_act02 = res02.status_code

        code_expect02 = '404'

        self.assertEqual(str(code_act02), code_expect02)


