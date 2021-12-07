#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/28 16:06
# @Author  : ywb
# @Site    : 
# @File    : all.py
# @Software: PyCharm
import os
import time

import pytest

if __name__ == '__main__':
    # user_manage
    pytest.main(['-vs'])
    time.sleep(3)
    os.system("allure generate ./temps -o ./report --clean")
    # pytest.main(['-vs', './testcase/test_login.py::TestLogin::test_interface_02',
    #              './testcase/test_login.py::TestLogin::test_interface_03'])
    # 'interface_testcase/test_login.py::TestLogin::test_interface_03'
    # pytest.main(['-vs', './testcase/test_login.py', '-n=3'])
    # pytest.main(['-vs','./interface/test_fixture.py::TestLogin::test_01_db'])
    # pytest.main(['-vs', './interface/product_manage'])
