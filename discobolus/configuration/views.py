from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, UpdateView, DeleteView

from discobolus.core.models import get_permalink
from discobolus.configuration.models import EmailNotification, EmailNotificationForm


class ConfigurationMainView(TemplateView):

    template_name = 'configuration/main.html'


class EmailNotificationListView(ListView):

    def get_queryset(self):
        return EmailNotification.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(EmailNotificationListView, self).get_context_data(**kwargs)
        context['email_notifications'] = self.get_queryset()
        return context


class EmailNotificationCreateView(CreateView):

    form_class = EmailNotificationForm
    template_name = 'configuration/emailnotification_form.html'

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
    template_name = 'configuration/emailnotification_form.html'

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
