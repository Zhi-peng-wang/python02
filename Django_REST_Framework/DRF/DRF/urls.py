from django.conf.urls import url, include
from django.contrib import admin

# 导入路由
from rest_framework import routers
from case01 import views


router = routers.SimpleRouter()

router.register(r'student', views.StudentVS)

urlpatterns = [
    # Examples:
    # url(r'^$', 'DRF.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # 需要把drf路由当成子路由进行配置好
    url(r'^api/', include(router.urls)),


]
