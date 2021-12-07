#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 23:28
# @Author  : ywb
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm
import pytest


def read_product():
    return ['足球', '图书', '百货']


@pytest.fixture(scope='function', autouse=False, params=read_product(), ids=["01", "02", "03"], name="goods")
def excute_sql(request):
    print('商品查询搜索开始')
    yield request.param
    print('商品查询搜索结束')
