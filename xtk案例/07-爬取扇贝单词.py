'''
扇贝单词：
1.把python单词列表download下来
2.主要练习目的是xpath
3.理论上讲不需要登陆
4.网址：https://www.shanbay.com/wordbook/187711/
'''
from urllib import request
from lxml import etree
import json

# 词汇表
words = []

def shanbei(page):
    url = "https://www.shanbay.com/wordlist/187711/540709/?page=%s"%page
    print(url)
    rsp = request.urlopen(url)
    rst = rsp.read()

    html = etree.HTML(rst)

    # 获取每一个单词
    tr_list = html.xpath('//table//tr')

    # 遍历单词，取出单词和单词的介绍
    for tr in tr_list:
        # 查找相应单词及其介绍
        word = {}

        strong = tr.xpath('./td/strong')
        if len(strong):
            # 此处进行数据的简单清晰，strip去除空格
            name = strong[0].text.strip()
            word['name'] = name
            # print(name)

        td_content = tr.xpath('./td[@class="span10"]')
        if len(td_content):
            cont = td_content[0].text.strip()
            word['content'] = cont
            # print(cont)
        print(word)

        if word != {}:
            words.append(word)


if __name__ == '__main__':
    shanbei(2)