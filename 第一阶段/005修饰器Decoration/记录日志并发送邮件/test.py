#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: test.py
@time: 2017/9/23 10:11
@description:
"""

from logit import Logit
from email_logit import EmailLogit


@Logit()
def test_log1():
    pass


@EmailLogit()
def test_email_log():
    pass


def do_some_test():
    test_log1()
    test_email_log()




