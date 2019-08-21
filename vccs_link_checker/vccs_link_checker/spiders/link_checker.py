# -*- coding: utf-8 -*-
import scrapy


class LinkCheckerSpider(scrapy.Spider):
    name = 'link_checker'
    allowed_domains = ['vccs-web-dev-1715195167.eu-west-2.elb.amazonaws.com/']
    start_urls = ['http://vccs-web-dev-1715195167.eu-west-2.elb.amazonaws.com/']

    def parse(self, response):
        for link  in response.css('a'):
            yield {'link': link.css('a ::text').get()} 
