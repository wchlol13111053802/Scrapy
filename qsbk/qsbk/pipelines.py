# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import JsonItemExporter #以二进制写入,全部完成后写入
# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp=open('qsbk1.json','w',encoding="utf-8")
#     def open_spider(self,spider):
#         print('爬虫开始。。。。。')
#     def process_item(self, item, spider):
#         # item_json=json.dumps(dict(item),ensure_ascii=False)
#         # self.fp.write(item_json+'\n')
#
#         return item
#     def close_spider(self,spider):
#
#         self.fp.close()
#         print('爬虫结束。。。。。')


# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp=open('qsbk1.json','wb')
#         self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
#         self.exporter.start_exporting()
#     def open_spider(self,spider):
#         print('爬虫开始。。。。。')
#     def process_item(self, item, spider):
#         self.exporter.export_item(item) #二进制写入开始
#         return item
#     def close_spider(self,spider):
#         self.exporter.finish_exporting() #二进制写入关闭
#
#         self.fp.close()
#         print('爬虫结束。。。。。')


from scrapy.exporters import JsonLinesItemExporter #以二进制写入,完成一个就写入一个
class QsbkPipeline(object):
    def __init__(self):
        self.fp=open('qsbk2.json','wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
        self.exporter.start_exporting()
    def open_spider(self,spider):
        print('爬虫开始。。。。。')
    def process_item(self, item, spider):
        self.exporter.export_item(item) #二进制写入开始
        return item
    def close_spider(self,spider):
        self.fp.close()
        print('爬虫结束。。。。。')