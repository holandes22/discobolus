from django.contrib import admin
from discobolus.configuration.models import EmailNotification, NotificationSettings

admin.site.register(EmailNotification)
admin.site.register(NotificationSettings)
