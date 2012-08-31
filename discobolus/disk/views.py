from django.views.generic import ListView, DetailView
from discobolus.disk.models import Disk

class DiskListView(ListView):
    model = Disk

    def get_queryset(self):
        return Disk.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DiskListView, self).get_context_data(**kwargs)
        context['request'] = self.request
        context['disks'] = self.get_queryset()
        return context

class DiskDetailView(DetailView):

    model = Disk

    def get_queryset(self):
        return Disk.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(DiskDetailView, self).get_context_data(**kwargs)
        context['request'] = self.request
        context['disks'] = self.get_queryset()
        return context

