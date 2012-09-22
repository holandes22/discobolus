import rpyc
from django.http import HttpResponseRedirect
from django.contrib.formtools.wizard.views import CookieWizardView

from discobolus.server.models import Server
from discobolus.server.forms import AgentNetworkAddressForm, AddServerConfirmationForm

ADD_SERVER_WIZARD_FORMS = [
        ("agent_network_address",  AgentNetworkAddressForm),
        ("add_server_confirmation",  AddServerConfirmationForm),
        ]

TEMPLATES = {
            "agent_network_address": "server/agent_network_address.html",
            "add_server_confirmation": "server/add_server_confirmation.html",
            }

class AddServerWizard(CookieWizardView):

    def __init__(self, *args, **kwargs):
        setattr(self, 'extra_content', {})
        return super(AddServerWizard, self).__init__(*args, **kwargs)

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        self.add_the_new_server(form_list)
        return HttpResponseRedirect('/')

    def add_the_new_server(self, form_list):
        pass

    def process_step(self, form):
        if self.steps.current == 'agent_network_address':
            self.extra_content['agent_network_address'] = form.cleaned_data.get('agent_network_address', None)
        return super(AddServerWizard, self).process_step(form)

    def get_form_initial(self, step):
        if step == 'add_server_confirmation':
            agent_network_address = self.extra_content['agent_network_address']
            conn = rpyc.classic.connect(agent_network_address)
            remote_platinfo = conn.modules['dmtcore.os.platinfo']
            details = remote_platinfo.get_platform_details()
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
        return super(AddServerWizard, self).get_form_initial(step)


