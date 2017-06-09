#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: lesson1.py
@time: 2017/6/8 16:37
"""

from time import time
import requests
from bs4 import BeautifulSoup


def download_boos_page(page):
    base_url = 'http://www.zhipin.com/c101010100/?page={0}&ka=page-{1}'
    proxies = {'http': '127.0.0.1'}
    request_url = base_url.format(page, page)
    request = requests.get(request_url)
    text = request.text
    soup = BeautifulSoup(text, "lxml")
    job_list = soup.find_all('div', class_='job-primary')
    jobs = []
    for job_primary in job_list:
        job_soup = BeautifulSoup(str(job_primary), 'lxml')
        job_info_tag = job_soup.find('div', class_='info-primary')
        company_info_tag = job_soup.find('div', class_='info-company')
        job_item = "{0} {1} {2} {3}".format(
            job_info_tag.h3.getText(), job_info_tag.p.getText(),
            company_info_tag.h3.getText(), company_info_tag.p.getText()
        )
        print(job_item)
        jobs.append(job_item)
    return jobs


def download_all_pages():
    all_jobs = []
    for page in range(1, 100):
        jobs = download_boos_page(str(page))
        all_jobs.extend(jobs)
        # time.sleep(5)
    for job in all_jobs:
        print(job)

if __name__ == '__main__':
    download_all_pages()
