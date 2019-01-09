# -*- coding:utf-8 -*-
# author = "Alenr"
import requests
import json
class RunMethod(object):
    def post_main(self,url):
        response = requests.post(url)
        data = response.json()
        return data

    def get_main(self,url):
        response = requests.get(url)
        return response.json()

    def run_main(self,method,url):
        if method == 'Post':
            res = self.post_main(url)
        else:
            res = self.get_main(url)
        return json.dumps(res,indent=2,sort_keys=True,ensure_ascii=False)

if __name__ == '__main__':
    url = 'http://www.imooc.com/api3/getbanneradvertver2'
    data = {"timestamp":"1507272377898",
            "uid":"5249191",
            "uuid":"5ae7d1a22c82fb89c78f603420870ad7",
            "secrect":"7d33829ecc354f0b4e00fb3764cb4207",
            "marking":"androidbanner","type":"1",
            "token":"50609fd5ffd05c734195d4bbc8dd5092"}
    run = RunMethod()
    data = run.run_main(url,'Post',data)
    # print(data)

