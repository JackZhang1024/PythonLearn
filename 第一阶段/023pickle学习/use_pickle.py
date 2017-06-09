# -*- coding: utf-8 -*-
import pickle,json
from student import Student
import jsonpickle
# d=dict(name='zhang',age=10,score=88)
# pickle.dumps(d)


d=dict(name='zhang',age=10,score=88)
f=open('a.txt','wb')
pickle.dump(d,f)
f.close()

#从文件中读取将数据转化成对象
f2=open('a.txt','rb')
d2=pickle.load(f2)
f2.close()
print(d2)

#将对象转化成json字符串
d3=dict(name="lisi",age=34,score=90)
jsonStr=json.dumps(d3)
print(jsonStr)

#将json字符串转化成对像
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
print("d4 {0}".format(json_str))

#将Student对象转化成dict
# student=Student('haha',34,90)
# strStudent=json.dumps(student,default=student.student2dict())
# print("Student2Dict {0}".format(strStudent))
#
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str, object_hook=d))

student=Student('haha',34,90)
print("Obj2Dict {0}".format(jsonpickle.encode(student)))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print("Dict2Obj {0}".format(jsonpickle.decode(json_str)))
