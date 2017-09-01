# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
from . import settings

class Sp1Pipeline(object):
    def __init__(self):
        self.f = None

    def process_item(self, item, spider):
        """
        处理爬下来的数据
        :param item:  爬虫中yield回来的对象
        :param spider:  爬虫对象 obj=JianDanSpider()
        :return:
        """
        response = requests.get(item['url'],stream=True)
        file_name = os.path.join(settings.FILE_PATH,item['name'])
        with open(file_name,'wb')as f:
            f.write(response.content)
        return item

    # # 以下方法适合打开同一文件，进行操作时。
    # @classmethod
    # def from_crawler(cls, crawler):
    #     """
    #     初始化时候，用于创建pipeline对象
    #     :param crawler:
    #     :return:
    #     """
    #     # val = crawler.settings.getint('MMMM')
    #     return cls()
    #
    # def open_spider(self,spider):
    #     """
    #     爬虫开始执行时，调用
    #     :param spider:
    #     :return:
    #     """
    #     print('打开爬虫')
    #     file_name = settings.FILE_PATH
    #     self.f = open(file_name, mode='wb')
    #
    # def close_spider(self, spider):
    #     """
    #     爬虫关闭时，被调用
    #     :param spider:
    #     :return:
    #     """
    #     print('关闭爬虫')
    #     self.f.close()





