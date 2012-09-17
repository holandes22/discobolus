from django.views.generic import ListView, DetailView
from discobolus.disk.models import Disk, Partition
from discobolus.disk.models import MultipathDisk, PathGroup, Path

class DiskListView(ListView):

    model = Disk

    def get_context_data(self, **kwargs):
        context = super(DiskListView, self).get_context_data(**kwargs)
        context['request'] = self.request
        context['disks'] = Disk.objects.all()
        context['multipath_disks'] = MultipathDisk.objects.all()
        return context

class DiskDetailView(DetailView):

    model = Disk

    def get_queryset(self):
        return Disk.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(DiskDetailView, self).get_context_data(**kwargs)
        disk = self.get_queryset()
        context['request'] = self.request
        context['disk'] = disk
        context['partitions'] = Partition.objects.filter(parent=disk)
        return context

class PartitionDetailView(DetailView):

    model = Partition

    def get_context_data(self, **kwargs):
        context = super(PartitionDetailView, self).get_context_data(**kwargs)
        parent = Disk.objects.filter(pk=self.kwargs['parent_pk'])
        context['request'] = self.request
        context['parent'] = parent
        context['partition'] = Partition.objects.filter(pk=self.kwargs['pk'])
        return context

class MultipathDiskDetailView(DetailView):

    model = MultipathDisk

    def get_queryset(self):
        return MultipathDisk.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(MultipathDiskDetailView, self).get_context_data(**kwargs)
        context['request'] = self.request
        multipath_disk = self.get_queryset()
        context['multipath_disk'] = multipath_disk
        path_groups = PathGroup.objects.filter(multipath_disk=multipath_disk)
        context['path_groups'] = path_groups
        return context

