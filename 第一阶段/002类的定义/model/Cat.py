# -*- coding:utf-8 -*-
# 原来Python也有包这一说法啊
from model.Animal import Animal

class Cat(Animal):

    def __init__(self,name,color):
        Animal.__init__(self,name,color)
        self.__name=name
        self.__color=color

    def run(self):
        print("Cat is running!")
