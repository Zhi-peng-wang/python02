from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.
def teacher(r):
    return  HttpResponse("这是一个视图")
def execption(r):
    raise Http404
    return HttpResponse("ok")