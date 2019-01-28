from django.conf.urls import include, url
from django.contrib import admin
# 导入视图
from MySer import views

# 导入drf的路由
from rest_framework import routers

# 定义一个DRF的简单路由
router = routers.SimpleRouter()

router.register(r'student', views.StudentVs)

urlpatterns = [
    # Examples:
    # url(r'^$', 'DRF2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(router.urls)),

]
