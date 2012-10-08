from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required

from discobolus.server.views import ServerListView, ServerUpdateView
from discobolus.server.views import AddServerWizard, ADD_SERVER_WIZARD_FORMS

urlpatterns = patterns('discobolus.server.views',
        url(r'^selected/(?P<server_pk>\d+)/set/$', 'set_selected_server'),
        url(r'^list/$', login_required(ServerListView.as_view()), name='server-list'),
        url(r'^create/$', login_required(AddServerWizard.as_view(ADD_SERVER_WIZARD_FORMS)), name='server-create'),
        url(r'^(?P<pk>\d+)/update/$', login_required(ServerUpdateView.as_view()), name='server-update'),
        url(r'^test_query_task/$', 'test_query_task'),
        url(r'^test_pvs_task/$', 'test_pvs_task'),
        )
