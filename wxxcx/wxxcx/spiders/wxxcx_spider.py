# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items  import WxxcxItem

class WxxcxSpiderSpider(CrawlSpider):
    name = 'wxxcx_spider'
    allowed_domains = ['developers.weixin.qq.com']
    start_urls = ['https://developers.weixin.qq.com/community/develop/question?page=%d&tag=&type=0#post-list' % 2]

    rules = (
        Rule(LinkExtractor(allow=r'.+/develop/question?page=[\d]*&tag=&type=0#post-list'), follow=True),
        Rule(LinkExtractor(allow=r'.+/community/develop/doc/[\d\w\s]*'),callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        # item = {}
        title=response.xpath('//span[@class="post_title_content"]/text()').get()
        con = response.xpath('//div[@class="post_content"]//text()').get()
        item = WxxcxItem(title=title, con=con)
        print(item)
        yield item

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
