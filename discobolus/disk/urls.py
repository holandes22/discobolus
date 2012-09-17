from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required

from discobolus.disk.views import DiskListView, DiskDetailView, MultipathDiskDetailView
from discobolus.disk.views import PartitionDetailView


urlpatterns = patterns('discobolus.disk.views',
        url(r'list/$', login_required(DiskListView.as_view()), name='disk-list'),
        url(r'^(?P<pk>\d+)/details/$', login_required(DiskDetailView.as_view()), name='disk-detail'),
        url(r'^(?P<parent_pk>\d+)/partition/(?P<pk>\d+)/details/$', login_required(PartitionDetailView.as_view()), name='partition-detail'),
        url(r'^multipath/(?P<pk>\d+)/details/$', login_required(MultipathDiskDetailView.as_view()), name='multipath-disk-detail'),
        )
