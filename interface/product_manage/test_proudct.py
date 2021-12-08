#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 20:22
# @Author  : ywb
# @Site    : 
# @File    : test_proudct.py
# @Software: PyCharm
import time

import pytest

from common.yaml_util import read_yaml
from interface.test_interface import TestInterface


class TestProduct:

    age = 19

    @pytest.mark.skip(reason='异常')
    def test_product_01(self, goods):
        print('第一个商品测试用例')
        print(goods)
        assert 1 == 2

    def test_product_02(self, goods, db):
        print('第二个商品测试用例')
        print(goods)
        print(db)



    @pytest.mark.skipif(age >= 18, reason='已成年')
    def test_03_product(self, goods):
        time.sleep(3)
        print('测试商品')
        print(goods)

    @pytest.mark.parametrize("caseinfo", read_yaml('./interface/product_manage/edit_flag.yaml'))
    def test_product_023(self, caseinfo):
        print(caseinfo)
        print('编辑标签接口')
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']+TestInterface.access_token
        data = caseinfo['request']['data']
        res = TestInterface.request_util.send_request(method=method, url=url, data=data)
        result = res.json()
        print(result)


if __name__ == '__main__':
    pytest.main()