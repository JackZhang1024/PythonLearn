#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: encode01.py
@time: 2018/6/10 8:24
@description:
"""

import urllib
import chardet

try:
    import cPickle as pickle
except ImportError:
    import pickle
fp = open(r"test.json", "wb")
data = dict(url='http://www.baidu.com/', title='title', content='conntent')
pickle.dump(data, fp)
print pickle.dumps(data)
fp.close()

fp1 = open(r"test.json", "rb")
content = pickle.load(fp1)
print content
fp1.close()


# country = u"中国"
# print country.encode("GB2312")
# print urllib.quote(country.encode("GB2312"))
#
# icountry = u"美国"
# print icountry.encode("UTF-8")
# print urllib.quote(icountry.encode("UTF-8"))
#
# print chardet.detect(icountry.encode("gbk"))
#
# city = u"北京".encode("utf-8")
# district = u"朝阳区".encode("utf-8")
# bizArea = u"望京".encode("utf-8")
#
# query = {
#     'city': city,
#     'district': district,
#     'bizArea': bizArea
# }
#
# print chardet.detect(query['city'])
# print '-'*100
# print 'http://www.lagou.com/jobs/list_python?px=default&'+urllib.urlencode(query)+"#filterBox"
#
# keywords = u"手机及配件市场".encode('gbk')
#
# query = {
#     'keywords': keywords
# }
#
# print chardet.detect(query['keywords'])
# print urllib.urlencode(query)
# print 'http://s.1688.com/selloffer/offer_search.htm?'+urllib.urlencode(query)
#
#
# q = u"安全门".encode('gb2312')
#
# query = {'q': q}
# print chardet.detect(query['q'])
# print urllib.urlencode(query)
#
# print 'http://search.nowec.com/search?'+urllib.urlencode(query)









