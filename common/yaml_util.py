#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 0:28
# @Author  : ywb
# @Site    : 
# @File    : yaml_util.py
# @Software: PyCharm
import os

import yaml


def get_obj_path():
    return os.path.dirname(__file__).split('common')[0]


def read_yaml(yaml_path):
    with open(get_obj_path()+yaml_path, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


if __name__ == '__main__':
    print(read_yaml('./interface/user_manage/get_token.yaml'))
