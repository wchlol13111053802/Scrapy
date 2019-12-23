# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree as et
from ..items import CarHomeItem
class CarAllSpider(scrapy.Spider):
    name = 'car_all'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/5393.html']


    def parse(self, response):
        print('starting..................')
        # print(response)
        html = requests.get('https://car.autohome.com.cn/pic/series/5393.html')
        con=et.HTML(html.text)

        ulbox = con.xpath('//div[@class="uibox"]')[1:]
        # print(ulbox)
        print('131321321321321---------------1561651321')
        for ul in ulbox:
            # category = ul.xpath('.//div[@class="uibox-title]')
            # print(category)
            img = ul.xpath('.//ul/li/a[1]/img/@src')
            text = ul.xpath('.//ul/li//text()')[0]
            # urls = ['https:'+url for url in img]

            urls = list(map(lambda url:response.urljoin(url),img))
            #
            # for url in urls:
            item = CarHomeItem(con=text,image_urls=urls)
            # print(item)
            yield item
            # for url in urls:


            # print('\n'.join(urls))
        print('ending....................')

