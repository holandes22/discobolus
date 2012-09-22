from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required

from discobolus.server.views import AddServerWizard
from discobolus.server.forms import AgentNetworkAddressForm, AddServerConfirmationForm

urlpatterns = patterns('discobolus.server.views',
        #url(r'list/$', login_required(DiskListView.as_view()), name='server-list'),
        url(r'^create/$', AddServerWizard.as_view([AgentNetworkAddressForm, AddServerConfirmationForm]), name='server-create'),
        )
