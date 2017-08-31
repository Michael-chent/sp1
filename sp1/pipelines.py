# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
from . import settings

class Sp1Pipeline(object):
    def process_item(self, item, spider):
        print(item)
        response = requests.get(item['url'],stream=True)
        file_name=os.path.join(settings.FILE_PATH,"%s.jpg"%item['name'])
        print("@#$",response,file_name)
        with open(file_name,mode='wb') as f:
            f.write(response.content)
        return item
