#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 23:28
# @Author  : ywb
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm
import pytest


@pytest.fixture(scope='class', autouse=False, name='user_fixture')
def user_fixture():
    print('用户管理的fixture')
    yield "usermanage"
