# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JcGoodsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    material=scrapy.Field() #材质
    product=scrapy.Field() #产地
    price = scrapy.Field() #价格
    name =  scrapy.Field() #品名
    type = scrapy.Field() #规格
    decline = scrapy.Field() #下降幅度
    pass
