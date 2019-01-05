import scrapy

# 导入需要导入的item
from e15Scrapy_meiju.items import MeijuItem

# 用来定义spider
class MeijuSpider(scrapy.Spider):

    name = 'meiju'

    start_urls = ['https://www.meijutt.com/new100.html']

    # 重写parse
    def parse(self, response):
        '''
        默认已经得到了网页
        反馈的内容用response表示
        其中包含需要的 所有数据
        :param response:
        :return:
        '''

        # 通过该xpath找到了所有的电影
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')

        for movie in movies:
            '''
            每个movie都需要装换成一个item
            需要生成一个Item实例对象
            '''
            item = MeijuItem()
            item['name'] = movie.xpath('./h5/a/@title').extract()[0]
            item['href'] = movie.xpath('./h5/a/@href').extract()[0]

            # 获取tv属性可能有问题将其放入if判断中
            tv = movie.xpath('./span/@class="mjtv"/text()')

            if len(tv):
                item['tv'] = tv.extract()[0]
            else:
                item['tv'] = ""

            # 此处返回值只能用yield返回
            yield item