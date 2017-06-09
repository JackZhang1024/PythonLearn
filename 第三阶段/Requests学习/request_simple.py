#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: request_simple.py
@time: 2017/6/7 17:31
"""

import requests
from bs4 import BeautifulSoup


def download_boos_page():
    url = 'http://www.zhipin.com/c101010100/?page=1&ka=page-1#null'
    request = requests.get(url)
    text = request.text
    soup = BeautifulSoup(text, "lxml")
    print(soup.prettify(encoding='gbk'))
    # print(soup.prettify())
    # print(soup.find_all(attrs={"class": "job-primary"}))
    # jobs = soup.find_all(attrs={"class": "job-primary"})
    # print(soup.find_all(class_="job-primary"))
    # job_list = soup.find_all(class_='job-list')

if __name__ == '__main__':
    download_boos_page()
