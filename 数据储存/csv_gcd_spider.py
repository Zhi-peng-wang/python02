import csv
s = csv.reader(open('test.csv', 'r'))
for i in s:
    print(i)