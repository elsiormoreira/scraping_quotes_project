# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        print('Wait a moment, please. I am access the site: ' + response.url)
        yield {
	        'author': response.css('small.author::text').getall(),
	        'quote': response.css('span.text::text').getall(),
	        'tags': response.css('a.tag::text').getall(),
        }
        
