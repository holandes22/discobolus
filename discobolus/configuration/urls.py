from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required

from discobolus.configuration.views import ConfigurationMainView
from discobolus.configuration.views import EmailNotificationListView
from discobolus.configuration.views import EmailNotificationCreateView, EmailNotificationUpdateView, EmailNotificationDeleteView
from discobolus.configuration.views import send_test_email_view

urlpatterns = patterns('discobolus.configuration.views',
        url(r'main/$', login_required(ConfigurationMainView.as_view()), name='configuration-main'),
        url(r'email-notification/list/$', login_required(EmailNotificationListView.as_view()), name='email-notification-list'),
        url(r'email-notification/create/$', login_required(EmailNotificationCreateView.as_view()), name='email-notification-create'),
        url(r'email-notification/(?P<pk>\d+)/update/$', login_required(EmailNotificationUpdateView.as_view()), name='email-notification-update'),
        url(r'email-notification/(?P<pk>\d+)/delete/$', login_required(EmailNotificationDeleteView.as_view()), name='email-notification-delete'),
        url(r'email-notification/(?P<pk>\d+)/send-test/$', send_test_email_view, name='email-notification-send-test'),
        )

