#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 23:28
# @Author  : ywb
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm
import pytest


@pytest.fixture(scope='function', autouse=False, name='api_status')
def api_setup():
    print('api准备')
    yield "success"
    print('api准备完成')

