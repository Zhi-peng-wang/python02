from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here.

class StudentListView(ListView):
    '''
    需要设置俩个主要内容
    1.queryset:数据来源集合
    2.template_name：模板名称
    '''
    # 添加过滤数据
    queryset = Student.objects.all().filter(gender="nan")

    template_name = "student_list.html"


def mySess(request):
    print(type(request.session))
    print(request.session)
    # 如果session中没有teacher_name的值，则返回NoName
    print(request.session.get("teacher_name", "NoName"))

    # 清除session中所有的值
    request.session.clear()
    print("in mysess")
    return None

def student(request):
    '''
    请求所有学生的详情列表
    :param request:
    :return:
    '''
    # 大约有一万名学生
    stus = student.objects.all()

    # 俩个参数
    # 1.数据来源，以及从数据库查询到的结果
    # 2.单页返回的数据量
    p = Paginator(stus, 50)

    # 对Paginator进行设置或者对变量属性的使用
    print(p.count)  # p中有多少条数据
    print(p.num_pages)  # 有多少页面
    print(p.page_range)  # 页码列表，从1开始

    # 取得第三页的内容
    # 如果页码不存在，报异常InvalidPage
    p.page(3)
    return stus