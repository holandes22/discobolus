from django.conf.urls.defaults import patterns, url

from discobolus.disk.views import DiskListView, DiskDetailView

urlpatterns = patterns('discobolus.disk.views',
        url(r'list/$', DiskListView.as_view(), name='disk-list'),
        url(r'(?P<pk>\d+)/details/$', DiskDetailView.as_view(), name='disk-detail'),
        )
