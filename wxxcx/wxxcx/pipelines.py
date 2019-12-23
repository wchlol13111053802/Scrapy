# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter

class WxxcxPipeline(object):
    def __init__(self):
        self.fp = open('wxjo.json','ab')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    def close_spider(self,spider):
        self.fp.close()