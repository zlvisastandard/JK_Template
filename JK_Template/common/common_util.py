# -*- coding:utf-8 -*-
# author = "Alenr"

class Commonutil(object):
    def is_contain(self,str_one,str_two):
        str_one = str(str_one)
        str_two = str(str_two)
        if str_one in str_two:
            return True
        else:
            return False