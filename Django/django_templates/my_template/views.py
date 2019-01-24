from django.shortcuts import render
from django.http import *
# Create your views here.
def one(request):
    # return HttpResponse(request)
    return render(request, template_name="one.html")

def two(request):
    ct = dict()
    ct['name'] = '梓鹏'
    ct['name1'] = '大鹏'
    ct['name2'] = '小鹏'
    return render(request, template_name="two.html", context=ct)

def three(request):
    ct = dict()
    ct['score'] = [98, 65, 99, 97, 95, 23]
    return render(request, template_name='three.html', context=ct)

def four(request):
    ct = dict()
    ct['name'] = '梓鹏'
    return render(request, template_name='four.html',context=ct)

def five_get(request):
    return render(request, template_name='five_get.html')

def five_post(request):
    print(request.POST)
    return render(request, template_name='one.html')

