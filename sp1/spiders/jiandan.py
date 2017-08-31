# -*- coding: utf-8 -*-
import scrapy


class JiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/']

    def parse(self, response):
        print(response.text)
