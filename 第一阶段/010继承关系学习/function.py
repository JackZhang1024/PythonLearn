def max(a,b):
    if(a>b):
        print("result {0}".format(a))
    else:
        print("result {0}".format(b))
max(6,5)

def chooseRoom(name):
    if(name=="zhangsan"):
        return "America"
    elif(name=="lisi"):
        return "Japan"
print(chooseRoom("zhangsan"))

class student:

   def __init__(self,name):
       self._name=name
       print("parent {0}".format(self._name))

   def sayHello(self):
       print("sayHello {0} {1}".format("world",self._name))

s=student("wangyan xifu")
s.sayHello()

class primaryStudent(student):
    def __init__(self,name):
        student.__init__(self,name)

    def sayHi(self):
        print("sayHi {0}".format(self._name))

primary=primaryStudent("zhangsan")
primary.sayHi()
