from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from discobolus.core.models import make_custom_field_callback, get_permalink, BaseModel
from discobolus.server.models import Server

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    def get_servers(self):
        return Server.objects.filter(user=self)


class NotificationSettings(BaseModel):

    user = models.OneToOneField(User, unique=True)
    notify = models.BooleanField(default=False)
    notify_on_agent_failure = models.BooleanField(default=True)
    notify_on_disk_failure = models.BooleanField(default=True)
    notify_on_path_failure = models.BooleanField(default=True)
    notify_on_logical_volume_manager_event = models.BooleanField(default=True,
            help_text='Notify of every action done with LVM')


    def __unicode__(self):
        return '{0} Notification Settings'.format(self.user)

    def get_update_url(self):
        return get_permalink('notification-settings-update', self.pk)



class NotificationSettingsForm(forms.ModelForm):
    formfield_callback = make_custom_field_callback

    class Meta:
        model = NotificationSettings
        readonly_fields = ['user']
        exclude = ['user']

class EmailNotification(BaseModel):

    user = models.OneToOneField(User, unique=True)
    smtp_server = models.CharField(max_length=200,
            help_text='SMTP server address and port. For example "smtp.gmail.com:587"')
    smtp_server_port = models.PositiveIntegerField()
    email_recipient = models.EmailField(max_length=200)
    email_sender = models.EmailField(max_length=200)
    account_name = models.EmailField(max_length=200)
    account_password = models.CharField(max_length=100)

    def __unicode__(self):
        return '{0} - {1}'.format(self.user, self.smtp_server)

    def get_update_url(self):
        return get_permalink('email-notification-update', self.pk)

    def get_delete_url(self):
        return get_permalink('email-notification-delete', self.pk)

    def get_send_test_email_url(self):
        return get_permalink('email-notification-send-test', self.pk)


class EmailNotificationForm(forms.ModelForm):
    formfield_callback = make_custom_field_callback
    #account_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = EmailNotification
        readonly_fields = ['user']
        exclude = ['user']
