# -*- coding:utf-8 -*-


class Animal(object):

    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def run(self):
        print("Animal is running !")

    def getName(self):
        return self.__name

    def runTwice(self):
        self.run()
        self.run()
