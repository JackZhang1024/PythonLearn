# -*- coding:utf-8 -*-

import sys


class Methods(object):

    @staticmethod
    def mymethod():
        print('我是被定义的静态方法')

    def __mymethod(self):
        print('我是私有的方法')

    def getMymethod(self):
        print('我是测试转化为静态的方法')

    conversion = staticmethod(getMymethod)
    conPrivate = staticmethod(__mymethod)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    methods = Methods()
    methods.getMymethod()
    methods.mymethod()
    Methods.mymethod()
    Methods.conversion()
    Methods.conPrivate()
    methods.conversion()
    methods.conPrivate()
