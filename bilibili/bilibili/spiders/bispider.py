# -*- coding: utf-8 -*-
from urllib.parse import urljoin, urlencode

import scrapy
import json
from scrapy import Request, Spider

from bilibili.items import BilibiliItem


class BispiderSpider(scrapy.Spider):
    name = 'bispider'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['https://www.bilibili.com/v/anime/finish/#/all/default/0/']

    def start_requests(self):

        for page in range(1, 20):
            url = urljoin(self.start_urls, page)
            yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)


    def parse(self, response):
        item = BilibiliItem()
        bis = response.css('.l-item')
        for bi in bis:
            item['title'] = bi.css('.title::text').extract_first()
            item['watch'] = bi.css('.v-info-i span::text').extract_first()
            item['image'] = bi.css('.lazy-img img::attr("scr")').extract_first()
            yield item
