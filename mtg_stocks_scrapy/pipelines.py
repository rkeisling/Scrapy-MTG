# -*- coding: utf-8 -*-
import datetime
import json
from scrapy.utils.serialize import ScrapyJSONEncoder

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MtgStocksScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    all_dicts = []

    # def open_spider(self, spider):
    #     print("Opening file...")
    #     date = datetime.datetime.now().strftime('%m_%d_%y')
    #     self.file = open('{0}.json'.format(date), 'w')

    # def close_spider(self, spider):
    #     print("Closing file...")
    #     json.dumps(self.all_dicts, self.file, cls=ScrapyJSONEncoder)
    #     self.file.close()

    # def process_item(self, item, spider):
    #     print("Processing {0}".format(item['cardname']))
    #     self.all_dicts.append(item)
    #     return item
