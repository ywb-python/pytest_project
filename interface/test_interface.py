#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/28 16:09
# @Author  : ywb
# @Site    : 
# @File    : test_interface.py
# @Software: PyCharm
import pytest
import requests

from common.request_util import RequestUtil
from common.yaml_util import read_yaml


def test_func_04():
    print('这是一个测试函数')


class TestInterface:
    access_token = " "
    request_util = RequestUtil()
    @pytest.mark.parametrize("caseinfo", read_yaml('./interface/user_manage/get_token.yaml'))
    def test_interface_01(self, caseinfo):
        print(caseinfo)
        print('第一个模块接口测试用例')
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        res = self.request_util.send_request(method=method, url=url, data=data)
        result = res.json()
        TestInterface.access_token = result['access_token']
        assert "access_token" in result

    @pytest.mark.parametrize("caseinfo", read_yaml('./interface/user_manage/edit_flag.yaml'))
    def test_interface_02(self, caseinfo):
        print(caseinfo)
        print('编辑标签接口')
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']+TestInterface.access_token
        data = caseinfo['request']['data']
        res = self.request_util.send_request(method=method, url=url, data=data)
        result = res.json()
        print(result)

    def test_interface_03(self):
        print('第三个接口测试用例')
