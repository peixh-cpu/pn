#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:peixh
# datetime:2020/8/6 17:49
# software: PyCharm
import json
import  pytest
from base.method import Requests
from utils.operationYaml import OperationYaml

obj=Requests()
objYaml=OperationYaml()

@pytest.mark.parametrize('datas',objYaml.readYaml())
def test_login(datas):
    r=obj.post(
        url=datas['url'],
        json=datas['data'])
    assert  datas['expect'] in json.dumps(r.json(),ensure_ascii=False)

# def add(a,b):
#     return a+b
#
# @pytest.mark.parametrize('a,b,result',[
#     (1,2,3),
#     (2,2,4),
#     (3,3,5)])
# def test_add(a,b,result):
#     assert add(a,b)==result

if __name__ == '__main__':
    pytest.main(["-s","-v","test_login.py"])