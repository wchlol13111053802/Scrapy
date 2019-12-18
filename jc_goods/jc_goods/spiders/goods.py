# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import JcGoodsItem
import requests
from lxml import etree
class GoodsSpider(CrawlSpider):
    name = 'goods'
    allowed_domains = ['ztweixin.steelcn.cn']
    start_urls = ['http://ztweixin.steelcn.cn']

    def parse(self, response):
        # item = {}
        obj = requests.get('http://ztweixin.steelcn.cn/Price/')
        html = etree.HTML(obj.text)
        div = html.xpath('//div[@class="wrap"]')
        for i in div:
            print('loading....')
            namelist = i.xpath('//ul[1]/li[1]/text()') #名字列表
            typelist =  i.xpath('//ul[1]/li[2]/text()') #材料类型列表
            materiallist = i.xpath('//ul[2]/li[1]/text()') #材料规格列表
            productlist=i.xpath('//ul[2]/li[2]/text()') #厂家列表
            pricelist=i.xpath('//ul[1]/li[3]/text()') # 价格列表
            declinelist = i.xpath('//ul[2]/li[3]/text()') #价格下降幅度列表
            for j in range(len(namelist)):
                name = namelist[j]
                type = typelist[j]
                price = pricelist[j]
                product = productlist[j]
                material = materiallist[j]
                decline = declinelist[j]
                item = JcGoodsItem(name=name, type=type, price=price, product=product, material=material,
                                   decline=decline)
                print(item)
                yield item

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

