'''
1. 创建项目
2. 编写item
3. 编写spider
4. 编写pipeline
5. 设置pipeline
'''

import scrapy
import re
from e16Scrapy3_qq.items import QQItem

class QqSpider(scrapy.Spider):

    name = 'qq'
    # 设置只能爬取腾讯域名的信息
    allowed_domains = ['hr,tencent.com']

    start_urls = [
        "https://hr.tencent.com/position.php"
    ]

    def parse(self, response):
        # 下载的结果自动放在response内储存
        for each in response.xpath('//*[@class="even"]'):
            # 对于得到的每一个工作信息内容
            # 把数据分装入相应的item中
            # 将该类实例化
            item =QQItem()

            name = each.xpath('./td[1]/a/text()').extract()[0]
            detalLink = each.xpath('./td[1]/a/@href').extract()[0]
            positionInfo = each.xpath('./td[2]/text()').extract()[0]
            workLocation = each.xpath('./td[4]/text()').extract()[0]

            item['name'] = name
            item['detalLink'] = detalLink
            item['positionInfo'] = positionInfo
            item['workLocation'] = workLocation

            # # 处理继续爬取的链接
            # # 通过得到当前页，提取数字，把数字加10.替换原来的数字，就是下一个页面地址
            # # 提取当前页面的地址
            # curpage = re.search('(\d+)', response.url).group(1)
            # # 生成下一页的数字值
            # page = int(curpage) + 10
            # # 生成下一页url，通过替换
            # url = re.sub('\d+', str(page), response.url)
            #
            # # 把地址通过yield返回
            # # 注意callback的写法
            # yield scrapy.Request(url, callback=self.parse)

            # 获取item提交给pipeline
            yield item
