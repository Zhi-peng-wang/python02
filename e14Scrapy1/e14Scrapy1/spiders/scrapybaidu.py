'''\
要求导入scrapy
所有类一般是xxxSpider命名
所有爬虫类是 scrapy.Spider的子类

利用最简单的爬虫
爬取百度页面
关闭机器人协议  在settings.py中，将True改为False
scrapy startproject 项目名称   创建scrapy框架下的爬虫
scrapy crawl 爬虫名称          执行爬虫
'''

import scrapy


class BaiduSpider(scrapy.Spider):

    # name是爬虫的名称
    name = "baidu"

    # 起始url列表
    start_urls = ['https://www.baidu.com']

    #负责分析downloader下载得到的结果
    def parse(self, response):
        '''
        只是保存网页即可
        :param response:
        :return:
        '''

        with open('baidu.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode('utf-8'))






















