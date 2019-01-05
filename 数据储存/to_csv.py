'''
CSV(comma-Separated Value), 逗号分隔符
CSV文件是由任意的数据结构组成，记录间以某种换行符组成，每行记录由换行符组合
ID,UserName,Age,Country
1001,zhangsan,18,wuxi
2001,lisi,18,beijing
'''
import csv
headers = ['ID', 'UserName', 'Age', 'Country']
rows = [
    (1001,'zhangsan', '18', 'wuxi'),
    (1002, 'lishi', '18', 'beijing'),
    (1003, 'wangwu', '18', 'shanghai')
]

with open('test.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
    # C:\Users\王志鹏\PycharmProjects\spider\数据储存\test.csv