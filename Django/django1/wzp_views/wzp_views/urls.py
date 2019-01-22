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


    url(r'^v10_1/', v.v10_1),
    url(r'^v10_2/', v.v10_2),
    url(r'^v11/', v.v11, name="v11"),

    url(r'^v8/', v.v8_get),
    url(r'^v9_get/', v.v9_get),
    url(r'^v9_post/', v.v9_post),
    url(r'^render_test/', v.render_test),
    url(r'^render2_test/', v.render2_test),
    url(r'^render3_test/', v.render3_test),

    url(r'^render_to_response/', v.render4_test),
]
