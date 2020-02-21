# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FangtianxiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field() #城市
    price = scrapy.Field() #房价
    area_name = scrapy.Field() #小区名字
    area = scrapy.Field() #房子面积
    container = scrapy.Field() #人居住量
    address= scrapy.Field() #行政区
    district = scrapy.Field()#是否再售
    origin_url = scrapy.Field()#原始链接
    pass


class FnagtianxiaOldItem(scrapy.Item):
    city = scrapy.Field()  # 城市
    price = scrapy.Field()  # 房价
    area_name = scrapy.Field()  # 小区名字
    area = scrapy.Field()  # 房子面积
    container = scrapy.Field()  # 人居住量
    address = scrapy.Field()  # 行政区

    origin_url = scrapy.Field()  # 原始链接

