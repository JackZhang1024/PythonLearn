# -*- coding:utf-8 -*-

from Animal import Animal
from Cat import Cat
from Dog import Dog

animal=Animal('pip','gray')
animal.run()
print(animal.getName())

cat=Cat('miaomiao','white')
cat.run()

dog=Dog('wangcai','black')
dog.run()


print(isinstance(dog,Animal))
print(isinstance(animal,Animal))
print(isinstance(animal,Dog))

cat.runTwice()



