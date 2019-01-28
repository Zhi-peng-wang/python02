# 序列化器都存放在这里
from rest_framework import serializers


# 此文件用来存放序列化器

class StudentSer(serializers.Serializer):
    '''
    里面写的是每一个需要序列化/反序列化的字段
    跟定义模型基本一致
    '''
    name = serializers.CharField(label='姓名', max_length=5)
    age = serializers.IntegerField()
    score = serializers.IntegerField()
