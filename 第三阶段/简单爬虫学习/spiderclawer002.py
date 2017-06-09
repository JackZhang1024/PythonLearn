# -*- coding:utf-8 -*-
"""
有道翻译
http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index
"""
import urllib.request
import urllib.parse
import json
import time

while True:
    inputField = input('请输入要翻译的内容,如果要退出则输入"q!"\n')
    if inputField == 'q!':
        break
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    data = {}
    data['type'] = 'AUTO'
    data['i'] = inputField
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_ENTER'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')
    # 第一种写法 直接在request构造方法中加入 head
    #request = urllib.request.Request(url, data, head)
    #response = urllib.request.urlopen(request)
    # 第二中写法 就是在request对象加add_header()方法
    request = urllib.request.Request(url,data)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    response = urllib.request.urlopen(request)
    # response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')
    dict = json.loads(html)
    result = dict['translateResult'][0][0]['tgt']
    print('要翻译的内容 %s 翻译的结果 %s ' % (inputField, result))
    time.sleep(5)
