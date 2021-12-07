#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 22:41
# @Author  : ywb
# @Site    : 
# @File    : test_fixture.py
# @Software: PyCharm
import pytest

from common.common_util import CommonUtil


class TestLogin(CommonUtil):

    def test_01_db(self, db):
        print('数据库测试01')
        print(db)

    def test_02_db(self):
        print('数据库测试02')


@pytest.mark.usefixtures("fixture_class")
class TestFix:
    def test_fix(self, db):
        print('类级别的fixture固件测试')
        print(db)
