from django.conf.urls import include, url
from django.contrib import admin
from my_template import views as v

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_templates.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^one/', v.one),

    url(r'^two/', v.two),
    url(r'^three/', v.three),

    url(r'^four/', v.four),
]
