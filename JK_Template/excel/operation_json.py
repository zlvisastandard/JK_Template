# -*- coding:utf-8 -*-
import json
class OperationJson(object):
    def __init__(self,file_path=None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = 'E:\PycharmProjects\JK_muban\json_2\\user.json'
        self.data = self.read_data()
    def read_data(self):
        with open(self.file_path,encoding='utf-8') as fp:
            data = json.load(fp,)
            return data
    def get_data(self,id):
        return self.data[id]

if __name__ == '__main__':
    opera = OperationJson()
    data = opera.get_data('uu_6')
    print(type(data))