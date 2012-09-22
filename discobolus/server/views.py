from django import forms
from django.http import HttpResponseRedirect
from django.contrib.formtools.wizard.views import CookieWizardView

from discobolus.server.models import Server

class AddServerWizard(CookieWizardView):

    def done(self, form_list, **kwargs):
        self.add_the_new_server(form_list)
        return HttpResponseRedirect('/')

    def add_the_new_server(self, form_list):
        pass

class AgentNetworkAddressForm(forms.Form):
    agent_network_address = forms.GenericIPAddressField()

class AddServerConfirmationForm(forms.ModelForm):

    class Meta:
        model = Server
        exclude = ['user']


    #alias = forms.CharField(max_length=200, help_text='Alias for this server')
    #hostname = forms.CharField(max_length=200)
    #architecture = forms.CharField(max_length=20)
    #machine = forms.CharField(max_length=200)
    #processor = forms.CharField(max_length=200)
    #system = forms.CharField(max_length=200)
    #release = forms.CharField(max_length=200)
    #agent_network_address = forms.GenericIPAddressField()

