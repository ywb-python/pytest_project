#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/28 16:09
# @Author  : ywb
# @Site    : 
# @File    : test_interface.py
# @Software: PyCharm
import pytest


def test_func_04():
    print('这是一个测试函数')


class TestInterface:

    def test_interface_01(self):
        print('第一个接口测试用例')

    @pytest.mark.run(order=1)
    def test_interface_02(self):
        print('第二个接口测试用例')

    def test_interface_03(self):
        print('第三个接口测试用例')
