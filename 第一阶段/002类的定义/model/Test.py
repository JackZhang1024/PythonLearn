# -*- coding:utf-8 -*-

from model.Animal import Animal
from model.Cat import Cat
from model.Dog import Dog

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



