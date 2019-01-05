'''
爬去糗事百科， 页面自己来找
分析：
1. 需要用到requests爬去页面，用xpath、re来提取数字
2. 可提取信息谁用户头像链接，段子内容，点赞，好评次数
3. 保存到json文件中

大致分三部分
1. down下页面
2。 利用xpath提取信息
3. 保存文件落地
'''
import requests
from lxml import etree

url = "https://www.qiushibaike.com/text/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2767.400",
    "Accept-Language" :"zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0"
}

req = requests.get(url, headers=headers)

html = req.text

# print(rst)

html = etree.HTML(html)

print(type(html))

# 把选出来的内容组成一个列表
rst = html.xpath('//div[@class="article block untagged mb15 typs_hot"]')
print(type(rst))

for i in rst:
    # strip的作用是将空白给省略
    rst = i.xpath('//div[@class="content"]/span')[0].text.strip()
    print(rst)







