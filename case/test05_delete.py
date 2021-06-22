import requests
import unittest


class TestDelete(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://127.0.0.1:8000/api/departments/"
        self.header = {"Content-Type": "application/json"}
        pass
    def tearDown(self) -> None:
        pass

    def test05delete(self):

        url05 = self.url + "python01/"

        res05 = requests.delete(url=url05)

        code_act05 = res05.status_code

        code_expect05 = '204'

        self.assertEqual(str(code_act05), code_expect05)

    def test06delete(self):

        url06 = self.url + "python05/"

        res06 = requests.delete(url=url06)

        code_act06 = res06.status_code

        code_expect06 = '404'

        self.assertEqual(str(code_act06), code_expect06)