'''
利用selenium模拟登陆豆瓣
需要手动输入验证码：
思路：
1. 保存页面成快照
2. 等待用户手动输入验证码
3. 继续自动执行提交等动作
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://accounts.douban.com/login'
driver = webdriver.Chrome('D:/google/chromedriver.exe')
driver.get(url)

time.sleep(4)

# 生成快照，用来查看验证码
driver.save_screenshot('doubandenglukuaizhao.png')

# 输入账户信息
driver.find_element_by_id('email').send_keys('742349899@qq.com')
driver.find_element_by_id('password').send_keys('wzp981208')

driver.find_element_by_name('login').click()

time.sleep(4)

with open('doubandenglu.html', 'w', encoding='utf-8')as f:
    f.write(driver.page_source)

driver.save_screenshot('sucess.png')

driver.quit()





