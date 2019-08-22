# -*- coding: utf-8 -*-
import json
from urllib.parse import urlencode

import scrapy
from scrapy import Request

from imagesTU.items import ImagestuItem


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        data = {
            'ch': 'photography',
            'listtype': 'new',

        }
        base_url = 'https://image.so.com/z?'
        for page in range(1, self.settings.get('MAX_PAGE')+1):
            data['sn'] = page*30
            url_1 = base_url + urlencode(data)
            url = base_url + url_1
            yield Request(url, self.parse)


    def parse(self, response):
        result = json.loads(response.json)
        for image in result.get('list'):
            item = ImagestuItem()
            item['id'] = image.get('id')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            yield item

