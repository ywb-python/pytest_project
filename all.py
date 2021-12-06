#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/28 16:06
# @Author  : ywb
# @Site    : 
# @File    : all.py
# @Software: PyCharm

import pytest

if __name__ == '__main__':
    pytest.main(['-vs'])
    pytest.main(['-vs', './testcase/test_login.py::TestLogin::test_interface_02',
                 './testcase/test_login.py::TestLogin::test_interface_03'])
    'interface_testcase/test_login.py::TestLogin::test_interface_03'
    pytest.main(['-vs', './testcase/test_login.py', '-n=3'])
