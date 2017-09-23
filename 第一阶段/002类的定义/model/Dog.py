# -*- coding:utf-8 -*-

from Animal import Animal

class Dog(Animal):

    def __init__(self,name,color):
        Animal.__init__(self,name,color)
        self.__name=name
        self.__color=color

    def run(self):
        print("Dog is running!")
