#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 23:25
# @Author  : ywb
# @Site    : 
# @File    : test_api.py
# @Software: PyCharm


class TestApi:
    def test_01_get_token(self, api_status):
        print("api测试获取token")
        print(api_status)
