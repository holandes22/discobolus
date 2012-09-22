from django.db import models
from django.contrib.auth.models import User
from discobolus.core.models import BaseModel
from django.db.models import permalink


class Server(BaseModel):

    user = models.ForeignKey(User)
    alias = models.CharField(max_length=200, help_text='Alias for this server')
    hostname = models.CharField(max_length=200)
    architecture = models.CharField(max_length=20)
    machine = models.CharField(max_length=200)
    processor = models.CharField(max_length=200)
    system = models.CharField(max_length=200)
    release = models.CharField(max_length=200)
    agent_network_address = models.GenericIPAddressField()

    def __unicode__(self):
        return u'{0}'.format(self.hostname)


