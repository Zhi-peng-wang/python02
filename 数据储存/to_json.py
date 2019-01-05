'''
python对json文件操作分为编码和解码
编码：
    dumps：解析的是字符串
    dump：解析的是fp的文件流   可以通过fp文件流写入文件
解码：
    load：
    loads： 也是争对字符串 

'''
import json

str = "[{'uesrname':'王志鹏'},{'password':'123456'}]"
# print(type(str))
json_str = json.dumps(str, ensure_ascii=False)# ensure_ascii=False表示非ascii编码，不写的话汉字会变成\u...
print(json_str)
print(type(json_str))

# 进行解码
new_str = json.loads(json_str)
print(type(new_str))
print(new_str)

















