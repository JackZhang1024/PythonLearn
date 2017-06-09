# -*- coding:utf-8 -*-

#读取文件
# f=open('python.txt','r')
# print(f.read())

#一般用来读取配置文件使用
# f=open('baidu.txt','r')
# for line in f.readlines():
#     print(line.strip())

#按照字节数来读取内容
#读取二十个字符
# f=open('baidu.txt','r')
# print(f.name)
# print(f.read(20))
# f.close()

#写入文件
# f=open('write.txt','w')
# f.write('哈哈哈哈哈哈哈哈')
# f.close()


#文件读取的新的方法 不必写close()方法
with open('write.txt','r') as f:
    print(f.readline())
