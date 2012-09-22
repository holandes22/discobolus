from django import forms
from discobolus.server.models import Server

class AgentNetworkAddressForm(forms.Form):
    agent_network_address = forms.GenericIPAddressField()

class AddServerConfirmationForm(forms.ModelForm):

    class Meta:
        model = Server
        exclude = ['user']
        readonly_fields = ['agent_network_address']
