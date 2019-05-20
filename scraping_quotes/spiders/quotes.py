# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        print('Wait a moment, please. I am access the site: ' + response.url)
        for quote in response.css('div.quote'):
	        item = {
		        'author': quote.css('small.author::text').get(),
		        'text': quote.css('span.text::text').get(),
		        'tags': quote.css('a.tag::text').getall(),
	        }
        	yield item
