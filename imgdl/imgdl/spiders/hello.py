#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urlparse import urljoin

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector

from imgdl.items import ImgdlItem


class HelloSpider(CrawlSpider):
    name = 'hello'
    allowed_domains = ['github.com']
    start_urls = [
        'https://github.com',
    ]
    # 规则
    rules = [
        # 处理页面内容，调用解析方法
        Rule(SgmlLinkExtractor(allow=['/$']), callback='parse_img',
             follow=True),
        Rule(SgmlLinkExtractor(allow=['/explore/?$']), callback='parse_img',
             follow=False),
        # # 不处理，进入页面查找下一层 url
        # Rule(SgmlLinkExtractor(allow=("/explore$", )), follow=True)
    ]

    # 方法名不能是 parse, 否则会变成单页抓取(depth=0)
    # http://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.contrib.spiders.Rule
    def parse_img(self, response):
        sel = Selector(response)
        sites = sel.xpath('//img')
        url = response.url

        for site in sites:
            item = ImgdlItem()
            img_urls = site.xpath('@src').extract()
            img_urls = map(lambda x, url=url: urljoin(url, x), img_urls)
            item['referrer'] = url
            item['image_urls'] = img_urls
            yield item
