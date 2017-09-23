#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: email_logit.py
@time: 2017/9/23 10:07
@description:
"""
from logit import Logit


class EmailLogit(Logit):
    def __init__(self, email='1120335370@qq.com', logfile='email.log'):
        Logit.__init__(self, logfile)
        self.email = email

    def notify(self):
        print 'email send successfully...'
