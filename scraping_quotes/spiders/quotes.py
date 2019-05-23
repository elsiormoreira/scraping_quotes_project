# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    # gigve a spider name
    name = 'quotes'
    # list of url where spider will begin to crawl
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # print what the spider is doing
        print('Wait a moment, please. I am access the site: ' + response.url)
        
        # loop on each quote on page and extract info using css selector
        for quote in response.css('div.quote'): 
        	# create a dictionary to store the scraped info
            item = {
                # extract author info
                'author':  quote.css('small.author::text').get(), 
                # extract quote text
                'text': quote.css('span.text::text').get(),
                # extract tags
                'tag': quote.css('a.tag::text').getall(),
            }
            # give the scraped info to scrapy
            yield item

        # extract new page url
        next_page_url = response.css('li.next > a::attr(href)').get()
        # check if there is a new page
        if next_page_url:
            # create an absolute url
            next_page_url = response.urljoin(next_page_url)
            # create a request for the new page
            yield scrapy.Request(url = next_page_url, callback = self.parse)