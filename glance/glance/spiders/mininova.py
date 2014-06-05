#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from glance.items import TorrentItem


class MiniovaSpider(CrawlSpider):
    name = 'mininova'
    allowed_domains = ['mininova.org']
    start_urls = ['http://www.mininova.org/today']
    rules = [
        Rule(SgmlLinkExtractor(allow=['/tor/\d+']), 'parse_torrent'),
    ]

    def parse_torrent(self, response):
        sel = Selector(response)
        _text = lambda sel: sel.extract()[0].strip().replace(u'\xa0', ' ')

        url = response.url
        name = _text(sel.xpath('//h1/text()'))
        description = _text(sel.xpath('//div[@id="description"]/text()[2]'))
        size = _text(sel.xpath('//div[@id="specifications"]/p[2]/text()[2]'))

        torrent = TorrentItem()
        torrent['url'] = url
        torrent['name'] = name
        torrent['description'] = description
        torrent['size'] = size
        return torrent
