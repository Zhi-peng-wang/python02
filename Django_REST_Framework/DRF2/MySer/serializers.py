# 序列化器都存放在这里
from rest_framework import serializers
from MySer.models import *

# 此文件用来存放序列化器

class StudentSer(serializers.Serializer):
    '''
    里面写的是每一个需要序列化/反序列化的字段
    跟定义模型基本一致
    '''
    # name = serializers.CharField(label='姓名', max_length=5)
    # age = serializers.IntegerField()
    # score = serializers.IntegerField()

    class Meta:
        # 告诉序列化器，对应哪个模型
        model = Student
        # fields = ['name', 'age', 'score']
        # all俩边是俩个下划线
        fields = '__all__'

