# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
"""
豆瓣美女爬虫学习
"""
url = 'http://t12.baidu.com/it/u=1023505538,1768666012&fm=72'
response = urllib.request.urlopen(url)
meinv = response.read()
with open('meinv.jpg','wb') as file:
     file.write(meinv)





