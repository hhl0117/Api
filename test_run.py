import unittest
import HTMLTestRunnerNew
import time

suite01 = unittest.TestSuite()
cases = unittest.defaultTestLoader.discover('case/',pattern='test*.py')

suite01.addTest(cases)

path01 = 'report/'

file01 = time.strftime('%Y%m%d%H%M%S')

file02 = '_TestReport.html'

filename = path01 + file01 + file02

print('测试报告的路径为：',filename)

with open(filename,'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='学院信息接口测试',
                                              tester='胡海澜')
    runner.run(suite01)

if __name__ == '__main__':
    unittest.main()
