import requests,json
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

rsp = requests.get('http://www.seputu.com/', headers=headers)
# print(rsp.text)

soup = BeautifulSoup(rsp.text, 'lxml')
content = []
for s in soup.find_all(class_='mulu'):# 查询类的时候要加下划线
    # print(s)
    h2 = s.find('h2')
    if h2 != None:
        h2_title = h2.string  # 获取标题
        # print(h2_title)

        # 获取章节内容和文章内容
        list = []
        for a in s.find(class_="box").find_all("a"):
            # print(a)
            href = a.get('href')
            box_title = a.get('title')
            # print(href, box_title)
            list.append({'href':href, 'box-title': box_title})

        content.append({'title':h2_title, 'content': list})

with open('aaa.json', 'a', encoding='utf-8') as fp:
    json.dump(content, fp=fp, indent=4, ensure_ascii=False)