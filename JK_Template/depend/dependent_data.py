# -*- coding:utf-8 -*-
# author = "Alenr"
from post_get_1.opera_excel import OperaExcel
from post_get_1.run_method import RunMethod
from post_get_1.get_data import GetData
from jsonpath_rw import parse,jsonpath
import json
class DependentDate(object):
    def __init__(self,case_id):
        self.case_id = case_id
        self.opera = OperaExcel()
        self.data = GetData()


    #通过case拿到整行的数据
    def get_case_line_data(self):
        row_data = self.opera.get_row_data(self.case_id)
        return row_data

    #获取依赖case的返回数据
    def run_depend(self):
        run_method = RunMethod()
        row_num = self.opera.get_row_num(self.case_id)
        url = self.data.get_request_url(row_num)
        method_way = self.data.get_request_method(row_num)
        request_data = self.data.get_data_for_json(row_num)
        sign = self.data.get_sign(row_num)
        url = url+'?data='+json.dumps(request_data)+'&sign='+sign
        res = run_method.run_main(url,method_way)
        return json.loads(res)

    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_depend()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]

if __name__ == '__main__':
    order = {
		"data": {
			"_input_charset": "utf-8",
			"body": "慕课网订单-1710141907182334",
			"it_b_pay": "1d",
			"notify_url": "http://order.imooc.com/pay/notifyalipay",
			"out_trade_no": "1710141907182334",
			"partner": "2088002966755334",
			"payment_type": "1",
			"seller_id": "yangyan01@tcl.com",
			"service": "mobile.securitypay.pay",
			"sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
			"sign_type": "RSA",
			"string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
			"subject": "慕课网订单-1710141907182334",
			"total_fee": 299
			},
			"errorCode": 1000,
			"errorDesc": "成功",
			"status": 1,
			"timestamp": 1507979239100
		}
    res = "data.out_trade_no"
    json_exe = parse(res)
    madle = json_exe.find(order)
    print ([math.value for math in madle][0])
