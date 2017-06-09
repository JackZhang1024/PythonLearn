# -*- coding:utf-8 -*-
#Python如何定义一个抽象类
def abstract():
    raise NotImplementedError('abstract')
class Person(object):
    def __init__(self):
        if self.__class__ is Person:
            abstract()
class Star(Person):
    def __init__(self):
        Person.__init__(self)
        print("我是一个大明星")
if __name__=='__main__':
    star=Star()
    # 发生错误
    # person = Person()