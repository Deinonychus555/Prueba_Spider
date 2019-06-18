# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class EAItem(scrapy.Item):
    def tuple_of_values(self):
        return tuple(self.values())

    def list_of_values(self):
        return list(self.values())

    def list_of_keys(self):
        return list(self.keys())

    def tuple_of_keys(self):
        return tuple(self.keys())

    def get_dict(self):
        return dict(self.items())

    def get_list_of_tuples(self):
        return list(self.items())

class QuotesItem(EAItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    quote = scrapy.Field()
    author = scrapy.Field()
    some = scrapy.Field()
    #tags = scrapy.Field()


    
class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    quote = scrapy.Field()
    
class AuthorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
  
    
class QuotesItemLoader(ItemLoader):
    
    def lower_processor(self, values):
        print('uppercase_processor: %s' %values)
        for v in values:
            yield v.lower()

    def lower_processor_mp(value):
        print('uppercase_processor: %s' % value)
        return value.lower()

    def capitalize_processor_mp(value):
        return value.capitalize()
    
    def wrap_mp(value):
        yield [value]

    def uppercase_processor_mp(value):
        print('uppercase_processor_mp: %s' % value)
        yield value.upper()

    author_mp = MapCompose(lower_processor_mp, capitalize_processor_mp, wrap_mp)

    
        

    default_input_processor = MapCompose(uppercase_processor_mp)
    default_output_processor = TakeFirst()
    
    author_in = MapCompose(lower_processor_mp, capitalize_processor_mp, wrap_mp)
    quote_in = lower_processor