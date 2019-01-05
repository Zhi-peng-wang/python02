# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class E16Scrapy3QqPipeline(object):
    def process_item(self, item, spider):
        return item

class QQPipiline(object):
    '''
    假设数据需要写入文件
    那么在什么时候打开关闭文件
    需要些方法
    '''

    # def __int__(self):
    #     self.file = open('qq.json', 'wb')

    def process_item(self, item, spider):
        # item可以直接转换成字典
        # content = json.dumps(dict(item), ensure_ascii=False)
        # self.file.write(content)
        print(item['name'])
        print(item['detalLink'])
        print(item['positionInfo'])
        print(item['workLocation'])


        return item

    # def close_spider(self):
    #     self.file.close()