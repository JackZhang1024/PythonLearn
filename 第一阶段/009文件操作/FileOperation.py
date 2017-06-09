#-*- coding:utf-8 -*-

#关于文件和目录的操作

#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

import os

#查看当前文件所处的目录
print(os.path.abspath('.'))

#在当前目录下创建一个文件目录
# dir=os.path.abspath('.')
# dir2=os.path.join(dir,'data')
# os.mkdir(dir2)

#删除指定目录下的目录
# dir3=os.path.join(os.path.abspath('.'),'data')
# os.rmdir(dir3)

# print(os.path.split('F:\PythonLearn\Learn001\write.txt'))
# print(os.path.splitext('F:\PythonLearn\Learn001\write.txt'))
#
# 获取当目录下所有python文件名称
# # dirs=[x for x in os.listdir('.') if os.path.isfile(x)]
# dirs=[x for x in os.listdir('.') if os.path.isdir(x)]
# print(dirs)
files=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(files)

