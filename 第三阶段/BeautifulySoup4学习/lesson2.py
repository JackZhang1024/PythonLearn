#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: lesson2.py
@time: 2017/6/8 18:15
"""
from bs4 import BeautifulSoup
import requests


"""
https://www.lagou.com/zhaopin/Android/3/?filterOption=3
221.130.202.206  80
"""


def download_lagou(page):
    url = 'https://www.lagou.com/zhaopin/Android/{0}/?filterOption=3'
    request_url = url.format(page,)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
    proxies = {'http': '115.183.11.158'}
    request = requests.get(request_url, headers=headers, proxies=None, timeout=30000)
    text = request.text
    soup = BeautifulSoup(text, 'lxml')
    job_list = soup.find_all('li', class_='con_list_item default_list')
    jobs = []
    for job_item in job_list:
        attrs = job_item.attrs
        data_salary = attrs['data-salary']
        data_company = attrs['data-company']
        data_positionname = attrs['data-positionname']
        # print('公司{0} 职位{1} 薪水{2}'.format(data_company, data_positionname, data_salary))
        # print '公司 %s 职位 %s 薪水 %s' % (data_company, data_positionname, data_salary)
        print '%s %s %s' % (data_company, data_positionname, data_salary)
        job = '{0} {1} {2}'.format(data_company, data_positionname, data_salary)
        jobs.append(job)
    return jobs


def download_all_android_jobs():
    all_jobs = []
    for page in range(0, 100):
        jobs = download_lagou(str(page))
        all_jobs.extend(jobs)
    for job in all_jobs:
        print(job)

if __name__ == '__main__':
    download_all_android_jobs()
