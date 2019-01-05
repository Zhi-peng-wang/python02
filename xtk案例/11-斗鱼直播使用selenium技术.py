'''
任务：
爬取斗鱼直播内容
https://www.douyu.com/directory/all
思路：
1. 利用selenium得到页面内容
2. 利用xpath或者bs等在页面进行信息提取
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import time

class Douyu():
    # 初始化方法
    def setup(self):
        self.driver = webdriver.Chrome('D:/google/chromedriver.exe')
        self.url = 'https://www.douyu.com/directory/all'

    def douyu(self):
        self.driver.get(self.url)

        while True:
            soup = BeautifulSoup(self.driver.page_source, 'xml')

            # 返回当前页面所有房间的标题和观众人数
            titles = soup.find_all('h3', {'class': 'ellipsis'})
            nums = soup.find_all('span', {'class': 'dy-num fr'})

            for t, n in zip(titles, nums):
                print('房间{0}---------------人数为:{1}'.format(t.get_text().strip(), n.get_text().strip()))
        time.sleep(2)


    def down(self):
        self.driver.quit()

if __name__ == '__main__':
    d = Douyu()
    d.setup()
    d.douyu()
    d.down()














