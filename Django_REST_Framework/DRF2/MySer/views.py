from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from MySer.models import *
from rest_framework.response import Response
from MySer.serializers import *
# Create your views here.

class StudentVS(viewsets.ModelViewSet):
    pass

class StudentAPIView(APIView):
    '''
    处理用户的get请求
    '''
    def get(self, request):
        # print("in APIView get")
        '''
        处理业务
        跟数据交互
        :param request:
        :return:
        '''
        stus = Student.objects.all()
        ser = StudentSer(many=True)
        return Response(data=ser,data)