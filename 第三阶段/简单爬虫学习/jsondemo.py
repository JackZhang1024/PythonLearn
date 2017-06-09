# -*- coding:utf-8 -*-
import json

html = '{"type":"EN2ZH_CN","errorCode":0,"elapsedTime":11,"translateResult":[[{"src":"happy new  year","tgt":"新年快乐"}]],"smartResult":{"type":1,"entries":["","新年快乐"]}}'
dict = json.loads(html)
print(type(dict))
result = dict['translateResult'][0][0]['tgt']
print(result)
