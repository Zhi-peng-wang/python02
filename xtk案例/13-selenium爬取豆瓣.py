'''
任务：
1. 利用selenium模拟鼠标下拉
2. 每次多出现几部电影的信息
'''

from selenium import webdriver
import time

driver = webdriver.Chrome('D://google//chromedriver.exe')

driver.get('https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=')

# 向下滚动10000像素
js = 'document.getElementsByTagName('"+body+"').scrollTop=10000'
driver.execute_script(js)
time.sleep(3)

driver.save_screenshot('d1.png')

driver.quit()