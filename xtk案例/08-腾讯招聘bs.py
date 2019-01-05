'''
爬取腾讯招聘网站
url:https://hr.tencent.com/

'''

from bs4 import BeautifulSoup
from urllib import request

def qq():
    # 获取页面内容
    url = 'https://hr.tencent.com/position.php'
    rsp = request.urlopen(url)
    html = rsp.read()

    # 使用bs解析页面
    soup = BeautifulSoup(html, 'lxml')

    # 创建css选择器，得到相应的tags
    tr1 = soup.select('tr[class="even"]')
    tr2 = soup.select('tr[class="odd"]')
    tr_list = tr1 + tr2

    for tr in tr_list:
        name = tr.select('td a')[0].get_text()
        print(name)
        href = tr.select('td a')[0].attrs['href']
        # print(href)
        a = tr.select('td')[1].get_text()
        b = tr.select('td')[3].get_text()
        print(a)
        print(b)

if __name__ == '__main__':
    qq()