from django.views.generic import ListView, DetailView
from discobolus.lvm.models import PhysicalVolume

class PhysicalVolumeListView(ListView):

    model = PhysicalVolume

    def get_context_data(self, **kwargs):
        context = super(PhysicalVolumeListView, self).get_context_data(**kwargs)
        if 'server_pk' in self.request.session:
            context['pvs'] = PhysicalVolume.objects.filter(server=self.request.session['server_pk'])
        return context

class PhysicalVolumeDetailView(DetailView):

    model = PhysicalVolume
    context_object_name = 'pv'
