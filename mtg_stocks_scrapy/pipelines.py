# -*- coding: utf-8 -*-
import datetime
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MtgStocksScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        date = datetime.datetime.now().strftime('%m_%d_%y')
        self.file = open('{0}.json'.format(date), 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        json.dumps(item, self.file)
        return item
