#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: lesson01.py
@time: 2018/6/17 12:02
@description:
"""

import urllib2
import cookielib

# response = urllib2.urlopen('http://www.zhihu.com')
# html = response.read()
# print html

# 获取cookie信息
# cookie = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open('http://www.zhihu.com')
# for item in cookie:
#     print item.name + ":"+item.value

# 设置cookie信息
# opener = urllib2.build_opener()
# opener.addheaders.append(('Cookie', 'email='+"1120335370@qq.com"))
# req = urllib2.Request('http://www.zhihu.com')
# response = opener.open(req)
# print response.headers
# retdata = response.read()

# 设置超时
# request = urllib2.Request('http://www.zhihu.com')
# response = urllib2.urlopen(request, timeout=2)
# html = response.read()
# print html

# 获取HTTP相应码
# try:
#     response = urllib2.urlopen('http://www.google.com')
#     print response
# except urllib2.HTTPError as e:
#     if hasattr(e, 'code'):
#         print 'Error code :', e.code





