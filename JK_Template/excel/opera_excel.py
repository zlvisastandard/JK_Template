import xlrd
from  xlutils.copy import copy
import os
class OperaExcel(object):
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = 'E:\PycharmProjects\JK_muban\json_2\case1.xls'
            self.sheet_id = 0
        self.sheet = self.get_sheet()

    def get_sheet(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        return self.sheet.nrows

    #获取单元格内容
    def get_value(self,row,col):
        tables = self.sheet
        return tables.cell_value(row,col)

    #写入数据
    def writer_values(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

if __name__ == '__main__':
    opera = OperaExcel()
    print(opera.get_lines())















