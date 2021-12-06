#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/28 15:47
# @Author  : ywb
# @Site    : 
# @File    : test_login.py
# @Software: PyCharm
import time

import pytest


class TestLogin:

    def test_login_01(self):
        time.sleep(3)
        print('第一个UI测试用例')

    @pytest.mark.smoke
    def test_login_02(self):
        time.sleep(3)
        print('第二个UI测试用例')

    @pytest.mark.usermange
    def test_login_03(self):
        time.sleep(3)
        print('第三个UI测试用例')
