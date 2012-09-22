from django.conf.urls import patterns, include, url
from django.contrib import admin

from discobolus.views import HomeTemplateView

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', HomeTemplateView.as_view(), name='main'),
    url(r'^disk/', include('discobolus.disk.urls')),
    url(r'^configuration/', include('discobolus.configuration.urls')),
    url(r'^server/', include('discobolus.server.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="logout"),
    # Examples:
    # url(r'^$', 'discobolus.views.home', name='home'),
    # url(r'^discobolus/', include('discobolus.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
