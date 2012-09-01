from django.views.generic import ListView, DetailView
from discobolus.disk.models import Disk, MultipathDisk

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
        context['request'] = self.request
        context['disk'] = self.get_queryset()
        return context

class MultipathDiskDetailView(DetailView):

    model = MultipathDisk

    def get_queryset(self):
        return MultipathDisk.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(MultipathDiskDetailView, self).get_context_data(**kwargs)
        context['request'] = self.request
        context['multipath_disk'] = self.get_queryset()
        return context

