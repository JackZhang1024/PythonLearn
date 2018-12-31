#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: hzjy02.py
@time: 2018/6/10 9:19
@description:
"""
import urllib2
import json

fp = open("hdgtjy.json", "w")
for page in range(1, 28):

    for i in range(5):
        try:
            send_headers = {'X-Requested-with': 'XMLHttpRequest',
                    'Content-Type': 'application/x-www-form-urlencoded'}
            request = urllib2.Request('http://www.hdgtjy.com/Index/PublicResults', data='page'+str(page) + '&size=10',
                                  headers=send_headers)
            response = urllib2.urlopen(request)
            data = response.read()
            # print data
            obj = json.loads(data)
            print obj['data'][0]['ADDRESS']
        except Exception, e:
            print e
    fp.write(data)
fp.close()
print 'end'

