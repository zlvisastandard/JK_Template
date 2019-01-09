# -*- coding:utf-8 -*-
import sys
sys.path.append("E:/PycharmProjects/JK_muban")
from excel.get_data import GetData
from runmethod.run_method import RunMethod
from common.common_util import Commonutil
from send.send_email import SendEmail
class RunTest(object):
    def __init__(self):
        self.data = GetData()
        self.run_method = RunMethod()
        self.com_util = Commonutil()
        self.send_email = SendEmail()

    def go_on_test(self):
        pass_count = []
        fail_count = []
        row_count = self.data.get_lines()
        for i in range(1,row_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                method = self.data.get_request_method(i)
                request_data = self.data.request_data(i)
                expect = self.data.get_except_data(i)
                res = self.run_method.run_main(method,request_data)
                if self.com_util.is_contain(expect,res):
                    print("测试通过%s"%i)
                    print(res)
                    # self.data.write_result(i,"pass")
                    pass_count.append(i)
                else:
                    print("测试失败%s"%i)
                    print(res)
                    # self.data.write_result(i,"file")
                    fail_count.append(i)
        self.send_email.send_main(pass_count,fail_count)

if __name__ == '__main__':
    runtest = RunTest()
    data = runtest.go_on_test()



