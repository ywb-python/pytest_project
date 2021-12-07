#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 23:40
# @Author  : ywb
# @Site    : 
# @File    : test_user.py
# @Software: PyCharm

import pytest


class TestUser:
    @pytest.mark.usefixtures("user_fixture")
    def test_user_01(self):
        print('第一个用户管理模块测试用例')

    @pytest.mark.run(order=1)
    def test_user_02(self):
        print('第二个用户管理模块测试用例')

    def test_user_03(self):
        print('第三个用户管理模块测试用例')