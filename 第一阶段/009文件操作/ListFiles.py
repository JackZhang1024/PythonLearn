# -*- coding:utf-8 -*-
#查找当前目录下所有含有指定字符串的文件并输出文件对应的路径

#思路 分为两个步骤
# 1、拿到当前目录下的所有目录和文件集合
# 2、然后根据拿到的文件集合做出对比 去出符合条件的文件

import os
#a目录和文件列表
a=[]
#b是输出结果
b=[]
def search(name):
    currentDir=os.path.abspath('.')
    a=find(currentDir)
    for x in a:
        for y in x:
           if os.path.isfile(y) and os.path.splitext(y)[1]==name:
               b.append(os.path.join(currentDir,y))
    return b
def find(path):
    files=[os.path.join(path,x) for x in os.listdir(path)]
    #print(files)
    a.append(files)
    for file in files:
        if os.path.isdir(file):
            find(os.path.join(path,file))
    return a
print(search('.py'))
