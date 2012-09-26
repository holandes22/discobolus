import rpyc
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from django.contrib.formtools.wizard.views import CookieWizardView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from discobolus.core.models import get_permalink
from discobolus.server.models import Server
from discobolus.server.forms import AgentNetworkAddressForm, ServerForm

ADD_SERVER_WIZARD_FORMS = [
        ("agent_network_address",  AgentNetworkAddressForm),
        ("add_server_confirmation",  ServerForm),
                    ]

TEMPLATES = {
            "agent_network_address": "server/agent_network_address.html",
            "add_server_confirmation": "server/add_server_confirmation.html",
            }


@login_required
def set_selected_server(request, server_pk):
    request.session['server_pk'] = server_pk
    # TODO: Change to get_object_or_404
    server = Server.objects.get(pk=server_pk)
    request.session['selected_server_alias'] = server.alias
    return HttpResponse(server.alias)

class AddServerWizard(CookieWizardView):

    def __init__(self, *args, **kwargs):
        self.connection_failed = True
        super(AddServerWizard, self).__init__(*args, **kwargs)

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        self.add_the_new_server(form_list)
        return HttpResponseRedirect('/')

    def add_the_new_server(self, form_list):
        data = self.get_cleaned_data_for_step('add_server_confirmation')
        server = Server(**data)
        # user is ManyToMany field
        server.save()
        server.user.add(self.request.user)
        server.save()

    def get_context_data(self, form, **kwargs):
        context = super(AddServerWizard, self).get_context_data(form=form, **kwargs)
        context['connection_failed'] = self.connection_failed
        return context

    def get_form_initial(self, step):
        if step == 'add_server_confirmation':
            data = self.get_cleaned_data_for_step('agent_network_address')
            try:
                agent_network_address = data['agent_network_address']
                conn = rpyc.classic.connect(agent_network_address)
                remote_platinfo = conn.modules['dmtcore.os.platinfo']
                details = remote_platinfo.get_platform_details()
                self.connection_failed = False
                return {
                        'architecture': details.architecture,
                        'release': details.release,
                        'system': details.system,
                        'hostname': details.hostname,
                        'alias': details.hostname,
                        'machine': details.machine,
                        'processor': details.processor,
                        'agent_network_address': agent_network_address,
                        }
            except KeyError:
                pass
            except Exception:
                return {'agent_network_address': 'CANNNOT CONNECT'}
        return super(AddServerWizard, self).get_form_initial(step)

class ServerListView(ListView):

    model = Server

    def get_context_data(self, **kwargs):
        context = super(ServerListView, self).get_context_data(**kwargs)
        context['linux_servers'] = Server.objects.filter(system__icontains='linux',
                user=self.request.user)
        context['windows_servers'] = Server.objects.filter(system__icontains='windows',
                user=self.request.user)
        context['other_servers'] = Server.objects.filter(user=self.request.user).exclude(system__icontains='windows').exclude(system__icontains='linux')
        return context

class ServerUpdateView(UpdateView):

    form_class = ServerForm
    template_name = 'server/server_details.html'


    def get_object(self):
        return Server.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return get_permalink('server-list')

    def get_context_data(self, **kwargs):
        context = super(ServerUpdateView, self).get_context_data(**kwargs)
        context['submit_url'] = get_permalink('server-update', self.kwargs['pk'])
        return context
