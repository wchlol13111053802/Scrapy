# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter

class FangtianxiaPipeline(object):
    def __init__(self):
        self.newHouse_fp = open('newHouse.json','wb')
        self.oldHouse_fp = open('oldHouse.json','wb')
        self.newHouse_exporter = JsonLinesItemExporter(self.newHouse_fp,ensure_ascii=False)
        self.oldHouse_exporter = JsonLinesItemExporter(self.oldHouse_fp,ensure_ascii=False)

    def process_item(self, item, spider):
        self.newHouse_exporter.export_item(item)
        self.oldHouse_exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.newHouse_fp.close()
        self.oldHouse_fp.close()
