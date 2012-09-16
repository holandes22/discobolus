from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth import login, logout

from django.contrib import admin
admin.autodiscover()

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['request'] = self.request
        return context

urlpatterns = patterns('',
    url(r'^$', HomeTemplateView.as_view(), name='main'),
    url(r'^disk/', include('discobolus.disk.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="logout"),
    # Examples:
    # url(r'^$', 'discobolus.views.home', name='home'),
    # url(r'^discobolus/', include('discobolus.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
