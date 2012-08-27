from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['request'] = self.request
        return context

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactTemplateView, self).get_context_data(**kwargs)
        context['request'] = self.request
        return context

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data(**kwargs)
        context['request'] = self.request
        return context


urlpatterns = patterns('',
        url(r'^$', HomeTemplateView.as_view()),
        url(r'contact/$', ContactTemplateView.as_view()),
        url(r'about/$', AboutTemplateView.as_view()),
    # Examples:
    # url(r'^$', 'discobolus.views.home', name='home'),
    # url(r'^discobolus/', include('discobolus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
