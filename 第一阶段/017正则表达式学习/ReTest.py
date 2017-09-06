# -*- coding:utf-8 -*-

# 正则表达式的使用

"""
re.match()
re.search()
re.findAll()
re.compile()
re.split()
re.sub()
"""
import re
p = re.compile('\d+')
print(p.findall('one1tow22three3four4'))
text = 'Welcome+to+the+connection+window'
print(re.split('\+', text))
