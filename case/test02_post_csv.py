import requests
import unittest
import ddt
from data import getcsv

datalist = getcsv.datalist

@ddt.ddt()
class TestPost(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://127.0.0.1:8000/api/departments/"
        self.header = {"Content-Type": "application/json"}
        pass
    def tearDown(self) -> None:
        pass

    @ddt.data(*datalist)
    def test01post(self,dptinfo):
        url01 = self.url
        if dptinfo['dep_id'] == None:
            dptinfo['dep_id'] = ''
        if dptinfo['dep_name'] == None:
            dptinfo['dep_name'] = ''
        if dptinfo['master_name'] == None:
            dptinfo['master_name'] = ''
        if dptinfo['slogan'] == None:
            dptinfo['slogan'] = ''
        data01 = '{"data":[{"dep_id":"' \
                 +dptinfo['dep_id']+ \
                 '","dep_name":"' \
                 +dptinfo['dep_name']+ \
                 '","master_name":"' \
                 +dptinfo['master_name']+ \
                 '","slogan":"' \
                 +dptinfo['slogan']+ \
                 '"}]}'

        res01 = requests.post(url=url01,data=data01.encode("utf-8"),headers=self.header)
        code_act01 = res01.status_code
        code_expect01 = int(dptinfo['code'])
        self.assertEqual(str(code_act01),str(code_expect01))

