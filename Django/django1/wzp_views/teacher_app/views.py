from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def teacher(r):
    return  HttpResponse("这是一个视图")
def execption(r):
    raise Http404
    return HttpResponse("ok")

def v10_1(request):
    return HttpResponseRedirect("/v11")

def v10_2(request):
    return HttpResponseRedirect(reverse("v11"))

def v11(request):
    return HttpResponse("哈哈，这是v11的访问返回呀")

def v8_get(request):
    rst = ""
    for k, v in request.GET.items():
        rst += k + "-->" + v
        rst += ","
    return HttpResponse("get返回的列表值为：{0}".format(rst))

def v9_get(request):
    # 渲染模板并且返回
    return render_to_response("for_post.html")

def v9_post(request):
    rst = ""
    for k, v in request.POST.items():
        rst += k + "-->" + v
        rst += ","
    return HttpResponse("post返回的列表值为：{0}".format(rst))

def render_test(request):
    # 环境变量
    # c = dict()

    rsp = render(request, "render.html" )
    # 等同于 rsp = HttpResponseRedirect(request, "render.html")
    return  rsp

def render2_test(request):
    # 环境变量
    c = dict()
    c["name"] = "wzp"
    c["name2"] = "wzp2"
    c["name3"] = "wzp3"
    # request , "请求的网页"， 请求的上下文环境也就是值传递
    rsp = render(request, "render2.html", context=c )
    return rsp

def render3_test(request):

    from django.template import loader

    # 得到模板
    t = loader.get_template("render2.html")

    r = t.render({"name": "wzp"})

    return HttpResponse(r)

def render4_test(request):

    # 反馈回模板render2.html
    rsp = render_to_response("render2.html", context=({"name": "wzp123"}))

    return rsp

def get404(r):

    from django.views import defaults

    return defaults.page_not_found(r, template_name="render.html")