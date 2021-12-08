#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 20:49
# @Author  : ywb
# @Site    : 
# @File    : request_util.py
# @Software: PyCharm
import requests


class RequestUtil:
    session = requests.session()

    def send_request(self, method, url, data, **kwargs):
        method = str(method).lower()
        res = ''
        if method == 'get':
            res = RequestUtil.session.request(method, url, params=data, **kwargs)
        elif method == 'post':
            res = RequestUtil.session.request(method, url, json=data, **kwargs)
        return res