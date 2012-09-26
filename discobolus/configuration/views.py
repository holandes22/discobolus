from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from discobolus.core.models import get_permalink
from discobolus.configuration.models import EmailNotification, EmailNotificationForm
from discobolus.configuration.models import NotificationSettings, NotificationSettingsForm
from discobolus.configuration.notification.email import send_test_email


@login_required
def send_test_email_view(request, pk):
    email_notification = EmailNotification.objects.filter(pk=pk)
    try:
        send_test_email(email_notification[0])
        msg = 'e-mail sent succesfully'
    except Exception as e:
        msg = 'An error occurred.\nPlease check details.\nError: %s' % (e,)
    return HttpResponse(msg)


class ConfigurationMainView(TemplateView):

    template_name = 'configuration/main.html'


    def get_context_data(self, **kwargs):
        # There should be one Settings per user.
        user = self.request.user
        try:
            notification_settings = NotificationSettings.objects.get(user=user)
        except ObjectDoesNotExist:
            notification_settings = NotificationSettings(user=user)
            notification_settings.save()
        context = super(ConfigurationMainView, self).get_context_data(**kwargs)
        context['notification_settings'] = notification_settings
        return context


class NotificationSettingsUpdateView(UpdateView):

    form_class = NotificationSettingsForm
    template_name = 'configuration/notification_settings.html'

    def get_object(self):
        return NotificationSettings.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return get_permalink('configuration-main')

    def get_context_data(self, **kwargs):
        context = super(NotificationSettingsUpdateView, self).get_context_data(**kwargs)
        context['submit_url'] = get_permalink('notification-settings-update', self.kwargs['pk'])
        return context


class EmailNotificationListView(ListView):

    def get_queryset(self):
        return EmailNotification.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(EmailNotificationListView, self).get_context_data(**kwargs)
        context['email_notifications'] = self.get_queryset()
        return context


class EmailNotificationCreateView(CreateView):

    form_class = EmailNotificationForm
    template_name = 'editor.html'

    def get_success_url(self):
        return get_permalink('configuration-main')

    def form_valid(self, form):
        self.instance = form.instance
        form.instance.user = self.request.user
        return super(EmailNotificationCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EmailNotificationCreateView, self).get_context_data(**kwargs)
        context['submit_url'] = get_permalink('email-notification-create')
        return context


class EmailNotificationUpdateView(UpdateView):

    form_class = EmailNotificationForm
    template_name = 'editor.html'

    def get_object(self):
        return EmailNotification.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return get_permalink('configuration-main')

    def get_context_data(self, **kwargs):
        context = super(EmailNotificationUpdateView, self).get_context_data(**kwargs)
        context['submit_url'] = get_permalink('email-notification-update', self.kwargs['pk'])
        return context


class EmailNotificationDeleteView(DeleteView):

    template_name = 'warning_dialog.html'

    def get_object(self):
        return EmailNotification.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return get_permalink('configuration-main')

    def get_context_data(self, **kwargs):
        context = super(EmailNotificationDeleteView, self).get_context_data(**kwargs)
        context['submit_url'] = get_permalink('email-notification-delete', self.kwargs['pk'])
        return context
