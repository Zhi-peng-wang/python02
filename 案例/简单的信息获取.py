import requests
from lxml import etree

url = "http://www.wxstc.cn/detail.php?fn=8&type=content"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2767.400",
    "Accept-Language" :"zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0"
}

req = requests.get(url, headers=headers)

html = req.text

# 将html的文件通过etree方法转换成可xpath
html = etree.HTML(html)
print(type(html))

rst = html.xpath('//a[contains(@href, "http://www.wxstc.cn/detail.php?id=96")]')
print(type(rst))

for i in rst:
    jieguo = i.xpath('//span[@style="color: black;"]')[0].text
    print(jieguo)














