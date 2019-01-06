from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
'''
视图函数需要一个参数，类型 应该是  HttpRequest
'''
def do_normalmap(request):

    return HttpResponse("this is normalmap")

def withparam(request, year, month):
    return  HttpResponse("today is {0} {1}".format(year, month))

def do_app(request):
    return HttpResponse("成功！")

def do_param2(request, pn):
    return HttpResponse("page is {0}".format(pn))

def extremParam(request, name):
    return HttpResponse('my name is {0}'.format(name))


def revParse(request):
    return  HttpResponse("your are url is {0}".format(reverse("wzp")))