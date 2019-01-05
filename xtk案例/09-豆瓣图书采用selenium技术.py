'''
https://book.douban.com/subject_search?search_text=python&cat=1001&start=0
使用selenium自动爬取页面信息
保存内容后xpath进行分析
'''
from selenium import webdriver
import time
from lxml import etree

def get_web(url):
    driver = webdriver.Chrome('D:/google/chromedriver.exe')
    driver.get(url)

    time.sleep(2)

    # 获取快照
    driver.save_screenshot('d.png')

    fn = 'douban.html'
    # 参数：fn，文件名称；‘w’,写入模式, encoding='utf-8',以utf编码格式编码
    with open(fn, 'w', encoding='utf-8') as f:
        # page_source获取网页中的内容
        f.write(driver.page_source)
    content(fn)

def content(fn):
    html = ''

    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()

    # 生成解析树
    tree = etree.HTML(html)

    # 查找book
    books = tree.xpath('//div[@class="item-root"]')

    for book in books:
        book_name = book.xpath('.//div[@class="title"]/a')
        print(book_name[0].text)


if __name__ == '__main__':
    get_web(r'https://book.douban.com/subject_search?search_text=python&cat=1001&start=0')


