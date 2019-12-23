# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from urllib import request

from scrapy.pipelines.images import ImagesPipeline
from Scrapy.car_home.car_home import settings

class CarHomePipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')

        if not os.path.exists(self.path):
            os.mkdir(self.path)

        else:
            print('images文件存在')
    def process_item(self, item, spider):
        con = item['con']
        url = item['url']
        category_path = os.path.join(self.path,con)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
            # for url in urls:
        name = url.split('/')[-1]
        request.urlretrieve(url,os.path.join(category_path,name)) #将远程的数据保留在本地


        return item

class IMAgesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 这个方法是在发送下载请求之前调用
        # 起始这个方法本身就是器发送下载请求的
        request_objs = super(IMAgesPipeline,self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item = item

        return request_objs

    def file_path(self, request, response=None, info=None):
        # 这个方法是在图片将要存储的时候调用，来获取这个图片存储的路径
        path = super(IMAgesPipeline,self).file_path(request,response,info)
        con = request.item.get('con')

        images_store = settings.IMAGES_STORE
        category_path = os.path.join(images_store, con)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = path.replace('full/','')
        image_path = os.path.join(category_path,image_name)
        return image_path