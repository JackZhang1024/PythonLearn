# -*- coding:utf-8 -*-

# Python模板

import time
import datetime


print(time.strftime('%Y%m%d%X', time.localtime()))
t = time.strptime('2011-3-8', '%Y-%m-%d')
y, m, d = t[0:3]
print(datetime.datetime(y, m, d))
now = datetime.datetime.now()
print now
