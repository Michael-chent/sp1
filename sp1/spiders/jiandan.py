# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector,Selector
from scrapy.http import Request
import re



class JiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/ooxx']
    has_request_set = {}

    def parse(self, response):
        # 要废弃
        # hxs = HtmlXPathSelector(response)
        # print(hxs)
        # result = hxs.select('//div[@id="comments"]')

        # 推荐
        hxs = Selector(response=response)
        comment_list = hxs.xpath('//ol[@class="commentlist"]')
        name = 1
        for item in comment_list:
            img_list = item.xpath('.//img')
            for img in img_list:
                src = img.xpath('@src').extract_first()
                if re.search(r'\w+.jpg$',src):
                    url="http:%s"%src
                    # print("*****", url)
                    from ..items import Sp1Item
                    obj = Sp1Item(name=name,url=url)
                    name += 1
                    yield obj

        page_urls = hxs.xpath('//div[@class="comments"]//a[re:test(@href,"http://jandan.net/ooxx/page-\d+#comments")]/@href').extract()
        # print(page_urls)
        # 规则
        for url in page_urls:
            key = self.md5(url)
            if key in self.has_request_set:
                pass
            else:
                self.has_request_set[key] = url
                req = Request(url=url,method='GET',callback=self.parse)
                yield req

    @staticmethod
    def md5(val):
        import hashlib
        ha = hashlib.md5()
        ha.update(bytes(val, encoding='utf-8'))
        key = ha.hexdigest()
        return key









