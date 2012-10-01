from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required

from discobolus.lvm.views import PhysicalVolumeListView, PhysicalVolumeDetailView
from discobolus.lvm.views import VolumeGroupListView, VolumeGroupDetailView
from discobolus.lvm.views import LogicalVolumeListView, LogicalVolumeDetailView


urlpatterns = patterns('discobolus.lvm.views',
        url(r'^pv/list/$', login_required(PhysicalVolumeListView.as_view()), name='pv-list'),
        url(r'^pv/(?P<pk>\d+)/details/$', login_required(PhysicalVolumeDetailView.as_view()), name='pv-detail'),
        url(r'^vg/list/$', login_required(VolumeGroupListView.as_view()), name='vg-list'),
        url(r'^vg/(?P<pk>\d+)/details/$', login_required(VolumeGroupDetailView.as_view()), name='vg-detail'),
        url(r'^lv/list/$', login_required(LogicalVolumeListView.as_view()), name='lv-list'),
        url(r'^lv/(?P<pk>\d+)/details/$', login_required(LogicalVolumeDetailView.as_view()), name='lv-detail'),
        #url(r'^(?P<parent_pk>\d+)/partition/(?P<pk>\d+)/details/$', login_required(PartitionDetailView.as_view()), name='partition-detail'),
        #url(r'^multipath/(?P<pk>\d+)/details/$', login_required(MultipathDiskDetailView.as_view()), name='multipath-disk-detail'),
        )
