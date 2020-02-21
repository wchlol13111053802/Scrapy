# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_redis.spiders import RedisSpider

from ..items import FangtianxiaItem,FnagtianxiaOldItem

# scrapy.Spider

class SearchHouseSpider(RedisSpider):
    name = 'search_house'
    allowed_domains = ['fang.com']
    # start_urls = ['https://www.fang.com/SoufunFamily.htm']
    redis_key = "fangTainXia:start_urls"
    def parse(self, response):
        trs = response.xpath('//div[@class="onCont"]//tr')
        province = None

        for tr in trs:
            tds = tr.xpath('.//td[not(@class)]')


            city_td = tds[0]
            city_links = city_td.xpath('.//a')
            for city_link in city_links:
                city = city_link.xpath('.//text()').get()
                city_url = city_link.xpath('.//@href').get()
                print('城市',city)
                print('城市链接',
                      )
                if city=='北京':
                    print('新房链接', '.newhouse.' + ''.join(
                        city_url.split('.')[1]) + '.com/house/s/')
                    new_house = '.newhouse.' + ''.join(
                        city_url.split('.')[1]) + '.com/house/s/'
                    print('二手房链接','.esf.' + ''.join(city_url.split('.')[1]))
                    old_house = '.esf.' + ''.join(city_url.split('.')[1])+'com'
                else:
                    print('新房链接',''.join(city_url.split('.')[0]).replace('http','https')+'.newhouse.'+''.join(city_url.split('.')[1])+'.com/house/s/')
                    new_house = ''.join(city_url.split('.')[0]).replace('http','https')+'.newhouse.'+''.join(city_url.split('.')[1])+'.com/house/s/'
                    print('二手房链接', ''.join(city_url.split('.')[0]).replace('http','https') + '.esf.' + ''.join(
                        city_url.split('.')[1])+'com')
                    old_house = ''.join(city_url.split('.')[0]).replace('http','https') + '.esf.' + ''.join(
                        city_url.split('.')[1])+'.com'

                # yield scrapy.Request(url=new_house,callback=self.new_house,meta={'info':city})
                yield scrapy.Request(url=old_house, callback=self.old_house, meta={'info': city,'url':old_house})
                print('二手房:---------------->')
                # break

            # break


    def new_house(self,response):
        city = response.meta.get('info')
        origin_url='Null'
        next = response.xpath('//div[@class="page"]/ul/li[@class="fr"]/a[@class="next"]/@href').get()
        lis = response.xpath('//div[contains(@class,"nl_con")]/ul/li')
        for li in lis:
            name = li.xpath('.//div[@class="nlcd_name"]/a/text()').get()
            house_type_text = li.xpath('.//div[contains(@class,"house_type")]/a/text()').getall()
            house_type = ''.join(house_type_text).replace('\n','').replace('\t','')
            container = house_type
            area = ''.join(li.xpath('.//div[contains(@class,"house_type")]/text()').getall()).replace('\n','').replace('\t','').replace('/','').replace('－','')
            district = li.xpath('.//div[@class="fangyuan"]/span/text()').get()

            area_name = li.xpath('.//div[@class="address"]/a//text()').getall()
            address = ''.join(area_name).replace('\n', '').replace('\t', '').split(']')[-1]
            area_name = ''.join(area_name).replace('\n', '').replace('\t', '').split(']')[0].replace('[','')
            price = ''.join(li.xpath('.//div[@class="nhouse_price"]//text()').getall()).replace(' ','').replace('\n','').replace('\t','').replace('\r','')
            origin_url = 'https:'+str(li.xpath('.//div[@class="nlcd_name"]/a/@href').get())
            if name ==None:
                name1 = '空'
                print('名字为:空')
            else:
                name2 = str(name).strip()
                print('名字',str(name).strip())
            print('城市',city)
            print('小区名字',area_name)
            print('具体地址',address)
            print('房子在售情况',district)
            print('房子容量',container)
            print('房子面积',area)
            print('房子价钱',price)
            print('原始链接',origin_url)
            item = FangtianxiaItem(city=city,area_name=area_name,address=address,district=district,container=container,area=area,price=price,origin_url=origin_url)
            yield item
        next_url=0
        try:
            next_url = origin_url+str(next).lstrip('/')
        except:
            next_url=0
        print('下一页的链接',next_url)
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url),callback=self.new_house,meta={'info':city})



    def old_house(self,response):
        city = response.meta.get('info')
        url = response.meta.get('url')
        print('二手房城市',city)
        dls = response.xpath('//div/dl[@class="clearfix"]')
        for dl in dls:
            name = dl.xpath('.//dd/h4/a/span[@class="tit_shop"]//text()').get()
            area_name = str(name).split()[0]
            origin_url = str(url)+dl.xpath('//dd/h4[@class="clearfix"]/a/@href').get()
            address = ''.join(dl.xpath('.//p[@class="add_shop"]/a//text()').getall()).replace(' ','').replace('\n','').replace('\r','')
            container = ''.join(dl.xpath('.//dd/p[@class="tel_shop"]//text()').getall()).replace('\r','').replace('\n','').replace(' ','')
            try:
                area = str(container).split('|')[1]
            except:
                area = str(container).split('|')[0]
            price = ''.join(dl.xpath('.//dd[@class="price_right"]//text()').getall()).replace('\r','').replace('\n','').replace(' ','')
            print('每个原始链接',origin_url)
            print('二手房地址------------------------>',address)
            print('二手房面积',area)
            print('二手房小区',area_name)
            print('二手房价钱',price)
            print('二手房名字',name)
            print('二手房容量',container)
            item = FnagtianxiaOldItem(city=city,area_name=area_name,address=address,container=container,area=area,price=price,origin_url=origin_url)
            yield item
        next_url = 0
        try:
            next_url = str(url)+response.xpath('//div[@class="page_al"]/p[1]/a/@href').get()
        except:
            next_url =0
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url),callback=self.old_house, meta={'info': city, 'url': next_url})
        print('下一页的url',next_url)