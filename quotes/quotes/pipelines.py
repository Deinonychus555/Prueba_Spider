# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QuotesPipeline(object):
    def process_item(self, item, spider):
        return item

class AuthorPipeline(object):
    def process_item(self, item, spider):
        if('Author' in item.__class__.__name__):
            print('AuthorPipeline.process_item')
            item['author']=item['author'] + "_author"
        return item

class QuotePipeline(object):
    def process_item(self, item, spider):
        if ('Quote' in item.__class__.__name__):
            print('QuotePipeline.process_item')
            item['quote']=item['quote'] + "_quote"
        return item
