from django.views.generic import ListView, DetailView
from discobolus.disk.models import Disk, Partition
from discobolus.disk.models import MultipathDisk


class DiskListView(ListView):

    model = Disk

    def get_context_data(self, **kwargs):
        context = super(DiskListView, self).get_context_data(**kwargs)
        if 'server_pk' in self.request.session:
            context['disks'] = Disk.objects.filter(server=self.request.session['server_pk'])
            context['multipath_disks'] = MultipathDisk.objects.filter(
                server=self.request.session['server_pk'])
        return context


class BaseDetailView(DetailView):

    def get_object(self):
        # precaching related objects for performance. One less db hit
        return self.model.objects.select_related().get(pk=self.kwargs['pk'])


class DiskDetailView(BaseDetailView):

    model = Disk


class PartitionDetailView(BaseDetailView):

    model = Partition


class MultipathDiskDetailView(DetailView):

    model = MultipathDisk
