#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: boss_spider.py
@time: 2017/9/19 23:32
"""

import scrapy
from scrapyLearn.items import ScrapylearnItem


def get_boss_urls():
    urls = []
    boss_url = 'https://www.zhipin.com/c101010100/?page={0}&ka=page-{1}'
    for index in range(1, 40):
        print index
        request_url = boss_url.format(index, index)
        print 'request_url %s ' % request_url
        urls.append(request_url)
    return urls


class BossSpider(scrapy.Spider):
    name = "Boss"
    allowed_domains = ['www.zhipin.com']
    # start_urls = ['https://www.zhipin.com/c101010100/?page=1&ka=page-1']
    start_urls = get_boss_urls()

    def parse(self, response):
        # filename = response.url.split('/')[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        selector = scrapy.selector.Selector(response)

        # sites = selector.xpath('//div[@class="info-primary"]/h3')
        # for site in sites:
        #     work_position = site.xpath('a/text()').extract()
        #     work_link = site.xpath('a/@href').extract()
        #     salary = site.xpath('a/span/text()').extract()
        #     print 'work_position {0} work_link {1} salary {2}'.format(work_position, work_link, salary)

        items = []
        sites = selector.xpath('//div[@class="job-primary"]')
        for site in sites:
            scrapy_item = ScrapylearnItem()
            scrapy_item['work_position'] = site.xpath('div[@class="info-primary"]/h3/a/text()').extract()
            scrapy_item['work_link'] = site.xpath('div[@class="info-primary"]/h3/a/@href').extract()
            scrapy_item['salary'] = site.xpath('div[@class="info-primary"]/h3/a/span/text()').extract()
            scrapy_item['company'] = site.xpath('div[@class="info-company"]/div[@class="company-text"]/h3/a/text()').extract()
            items.append(scrapy_item)
        return items



