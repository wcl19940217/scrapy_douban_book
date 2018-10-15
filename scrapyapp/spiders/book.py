# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.response.html import HtmlResponse
from ..items import BookItem


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=False),
    )
    # url加入到待爬取的队列url

    def parse_item(self, response):
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        subjects = response.xpath('//li[@class="subject-item"]')
        for subject in subjects:
            item = BookItem()
            item['title'] = subject.xpath('.//h2/a/text()')[0].extract().strip()
            rate = subject.xpath('.//span[@class="rating_nums"]/text()').extract()
            if rate:
                item['rate'] = rate[0]
            else:
                item['rate'] = 0
            yield item


class TestSpider(CrawlSpider):
    name = 'test'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']











