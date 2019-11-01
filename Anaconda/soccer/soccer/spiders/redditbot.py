# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['unafut.com']
    start_urls = ['http://unafut.com/']

    def parse(self, response):
        pass
