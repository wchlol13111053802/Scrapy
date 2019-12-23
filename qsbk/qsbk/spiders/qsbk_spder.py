# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from ..items import QsbkItem
class QsbkSpderSpider(scrapy.Spider):
    name = 'qsbk_spder'
    allowed_domains = ['budejie.com']
    start_urls = ['http://www.budejie.com/1']

    def parse(self, response):
        context = response.xpath('//div[@class="j-r-list-c-desc"]')
        for text in context:
            Text=text.xpath('.//a/text()').get().replace(' ','')
            # getall()

            # con={'con':Text}
            # print(Text)
            # yield con
            item = QsbkItem(con=Text)
            yield item
        next_url=response.xpath('//a[@class="pagenxt"]/@href').get()
        if not next_url:
            return
        else:
            yield scrapy.Request('http://www.budejie.com/'+next_url,callback=self.parse)