# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import QuotesItem, QuotesItemLoader, AuthorItem, QuoteItem
from scrapy.loader import ItemLoader


class ExampleSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['example.com']
    start_urls = ['http://quotes.toscrape.com/']
    #start_urls = ['https://api6.ipify.org/?format=json']
    
    def parse(self, response):
        # print(response)
        quotes_t = response.xpath("//div[@class='quote']")

        for q in quotes_t:
            quote = q.xpath("*[@class='text']/text()").extract_first()
            author = q.xpath("*//*[@class='author']/text()").extract_first()

            quote_dict = {
                'quote': quote,
                'author': author,
                'some': 'some'
            }

            item = QuotesItem(quote_dict)
        


            il = QuotesItemLoader(QuotesItem(), q)
            il.add_xpath('quote', "*[@class='text']/text()")
            il.add_xpath('author', "*//*[@class='author']/text()")
            il.add_xpath('author', "span[2]/*/text()")
            il.add_value('some', "some")
            i = il.load_item()
            i = il.load_item()


            yield item
        
        
    def parse2(self, response):
        print('parse')
        #print(response)
        quote_t = response.xpath("//div[@class='quote']")[0]
        quote = quote_t.xpath("*[@class='text']/text()").extract_first()
        author = quote_t.xpath("*//*[@class='author']/text()").extract_first()
       
        quote_dict = {
            'quote': quote,
            'author': author

        }

        item = QuotesItem(quote_dict)
        # print(item)
        
        
        i_quote = QuoteItem()
        i_quote['quote'] = quote
        i_author = AuthorItem()
        i_author['author'] = author
        
      
        
        il = QuotesItemLoader(QuotesItem(), quote_t)
        il.add_xpath('quote', "*[@class='text']/text()")
        il.add_xpath('author', "*//*[@class='author']/text()")
        il.add_xpath('author', "span[2]/*/text()")
        il.add_value('some', "some")
        yield il.load_item()

        #yield i_quote

       
    # print(tuple(item.values()))
        

        

