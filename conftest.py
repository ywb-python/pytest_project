#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 23:28
# @Author  : ywb
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm
import pytest


def read_yaml():
    # return ['林黛玉', '鲁智深', '诸葛亮']
    return [{"红楼梦": '林黛玉'}, {"水浒传": '鲁智深'}, {"三国演义": '诸葛亮'}]


@pytest.fixture(scope='function', autouse=False, params=read_yaml(), ids=["01", "02", "03"], name="db")
def excute_sql(request):
    print('执行SQL查询')
    yield request.param
    print('关闭数据库连接')


@pytest.fixture(scope='session', autouse=True, name='all')
def login_status():
    print('登录前')
    yield "success"
    print('登录后')


@pytest.fixture(scope='class', autouse=False, name='fixture_class')
def fix_status():
    print('未使用fixture')
    yield "success"
    print('已使用fixture')
