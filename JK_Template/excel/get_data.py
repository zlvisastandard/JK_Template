# -*- coding:utf-8 -*-
from .opera_excel import OperaExcel
from excel import data_config
from .operation_json import OperationJson
import json
import hashlib
class GetData(object):
    def __init__(self):
        self.opera_excel = OperaExcel()

    #获取单元格的行数
    def get_lines(self):
        return self.opera_excel.get_lines()

    #获取是否执行该条case
    def get_is_run(self,row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #获取列的id
    def get_col_data(self,row):
        col = int(data_config.global_var.Id)
        col_data = self.opera_excel.get_value(row,col)
        return col_data

    #获取请求方式
    def get_request_method(self,row):
        col = int(data_config.get_run_way())
        request_method = self.opera_excel.get_value(row,col)
        return request_method

    #获取url
    def get_request_url(self,row):
        col = int(data_config.get_url())
        url = self.opera_excel.get_value(row,col)
        return url

    #获取是否携带header
    def is_header(self,row):
        col = int(data_config.get_header())
        header = self.opera_excel.get_value(row,col)
        if header != '':
            return header
        else:
            return None


    #获取预期结果
    def get_except_data(self,row):
        col = int(data_config.get_except())
        expect = self.opera_excel.get_value(row,col)
        if expect == '':
            return None
        else:
            return expect

    #result写入表格
    def write_result(self,row,value):
        col = int(data_config.get_result())
        self.opera_excel.writer_values(row,col,value)


    #获取Json的值
    def get_request_data(self,row):
        col = int(data_config.get_data())
        data = self.opera_excel.get_value(row,col)
        if data != '':
            return data
        else:
            return None

    #获取json内的内容
    def get_data_for_json(self,row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    #获取sign
    def get_sign(self,row):
        data = self.get_data_for_json(row)   #字典
        data_json = json.dumps(data)
        time_data = data["timestamp"]
        # time_data = time.strftime("%Y%m%d%H%M%S",time.localtime())
        token = '9b389216c3c5vtlwf535510b33b9e6ea8'
        m = hashlib.md5()
        m.update((data_json+'&'+time_data+token).encode())
        sign = m.hexdigest()
        return sign

    #拼装request的data
    def request_data(self,row):
        url_www = self.get_request_url(row)
        value = self.get_data_for_json(row)
        sign = self.get_sign(row)
        url = url_www+'?data='+json.dumps(value)+'&sign='+sign
        return url

if __name__ == '__main__':
    getdata = GetData()
    data = getdata.get_data_for_json(0)
    data = json.dumps(data,indent=2,sort_keys=True,ensure_ascii=False)
    print(type(data))

