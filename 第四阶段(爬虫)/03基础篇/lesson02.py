#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: lesson02.py
@time: 2018/6/17 15:54
@description:
"""

# 使用Requests
# import requests
#
# r = requests.get('http://www.baidu.com')
# print r.content

# import requests
# payload = {'keywords': 'blog', 'pageIndex': 1}
# r = requests.get('http://www.baiduc.com', params=payload)
# print r.url

# 响应码和编码
# import requests
# r = requests.get('http://www.baiduc.com')
# print 'content--->'+r.content
# # print 'text--->'+r.text
# print 'encoding--->'+r.encoding
# r.encoding = 'gbk'
# print 'new text--->'+r.text

# 自动检测网页编码的模块 chardet
# import chardet
# import requests
#
# r = requests.get('http://www.baidu.com')
# print chardet.detect(r.content)
# r.encoding = chardet.detect(r.content)['encoding']
# print r.text

# 流模式 读取指定字节数的数据
# import requests
# r = requests.get('http://www.baidu.com', stream=True)
# print r.raw.read(10)

# 请求头Headers处理
# import requests
# user_agent = 'Mozilla/4.0 (compatible, MSI 5.5; Windows NT)'
# headers = {'User-Agent':user_agent}
# r = requests.get('http://www.baidu.com', headers=headers)
# print r.content

# 请求头Headers处理
# import requests
# user_agent = 'Mozilla/4.0 (compatible, MSI 5.5; Windows NT)'
# headers = {'User-Agent':user_agent}
# r = requests.get('http://www.baidu.com', headers=headers)
# if r.status_code == requests.codes.ok:
#     print r.status_code
#     print r.headers
#     print r.headers.get('content-type')
#     print r.headers['content-type']  # 不推荐此种方式获取
# else:
#     r.raise_for_status()

# Cookie处理
# import requests
# user_agent = 'Mozilla/4.0 (compatible, MSI 5.5; Windows NT)'
# headers = {'User-Agent': user_agent}
# r = requests.get('http://www.baidu.com', headers=headers)
# for cookie in r.cookies.keys():
#     print cookie+":" + r.cookies.get(cookie)






