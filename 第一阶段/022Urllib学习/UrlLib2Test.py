# -*- coding:utf-8 -*-


# urllib2的使用方法
import urllib2
import urllib


# 调用urllib2中的urlopen()
response = urllib2.urlopen('http://www.baidu.com/')

# 方法打开远程文件
html=response.read()  # 读取文件
print(html)

# 使用urllib模块中的urlretrieve()方法下载文件保存至本地
urllib.urlretrieve('http://www.baidu.com', 'D:\\python_webpage.html')
urllib.urlcleanup()