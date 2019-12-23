# -*- coding: utf-8 -*-
import scrapy
import json

class IphttpbinSpider(scrapy.Spider):
    name = 'iphttpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        origin = json.loads(response.text)['origin']
        print(origin)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)
        pass
