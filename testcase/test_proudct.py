#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 20:22
# @Author  : ywb
# @Site    : 
# @File    : test_proudct.py
# @Software: PyCharm
import time

import pytest


class TestProduct:

    age = 19

    @pytest.mark.skip(reason='异常')
    def test_product_01(self):
        print('第一个商品测试用例')
        assert 1 == 2

    def test_product_02(self):
        print('第二个商品测试用例')


    @pytest.mark.skipif(age >= 18, reason='已成年')
    def test_03_product(self):
        time.sleep(3)
        print('测试商品')


if __name__ == '__main__':
    pytest.main()