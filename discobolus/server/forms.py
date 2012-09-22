from django import forms
from discobolus.server.models import Server
from discobolus.core.models import make_custom_field_callback


class AgentNetworkAddressForm(forms.Form):

    agent_network_address = forms.GenericIPAddressField()


class ServerForm(forms.ModelForm):

    formfield_callback = make_custom_field_callback

    class Meta:
        model = Server
        exclude = ['user']
