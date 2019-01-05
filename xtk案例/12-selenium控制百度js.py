'''
任务：
通过selenium模拟对页面元素的控制
'''

from selenium import webdriver
import time

driver = webdriver.Chrome('D:/google/chromedriver.exe')

driver.get('http://www.baidu.com')

# 通过js控制网页内容
# 首先需要先把js编写出来
# 然后通过execute_script 执行

# 美化输入框
js = "var q = document.getElementById(\'kw\'); q.style.border=\'2px solid red\';"

driver.execute_script(js)

driver.save_screenshot("baidu.png")

# 隐藏百度的logo
# 有兴趣的可以试一试














