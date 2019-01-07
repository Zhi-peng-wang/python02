from django.conf.urls import include, url
from django.contrib import admin

from teacher_app import views as v
urlpatterns = [
    # Examples:
    # url(r'^$', 'wzp_views.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^teacher/', v.teacher),

    url(r'^execption/', v.execption),
]
