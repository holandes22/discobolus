from django.views.generic import ListView, DetailView
from discobolus.lvm.models import PhysicalVolume, VolumeGroup, LogicalVolume


class LVMBaseListView(ListView):

    def get_context_data(self, **kwargs):
        context = super(LVMBaseListView, self).get_context_data(**kwargs)
        if 'server_pk' in self.request.session:
            context['objects'] = self.model.objects.filter(server=self.request.session['server_pk'])
        return context


class PhysicalVolumeListView(LVMBaseListView):

    model = PhysicalVolume


class PhysicalVolumeDetailView(DetailView):

    model = PhysicalVolume
    context_object_name = 'object'


class VolumeGroupListView(LVMBaseListView):

    model = VolumeGroup


class VolumeGroupDetailView(DetailView):

    model = VolumeGroup
    context_object_name = 'object'


class LogicalVolumeListView(LVMBaseListView):

    model = LogicalVolume


class LogicalVolumeDetailView(DetailView):

    model = LogicalVolume
    context_object_name = 'object'
