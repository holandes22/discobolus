from django.db import models
from django.db.models import permalink
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from discobolus.core.models import BaseModel
from discobolus.server.models import Server

class PhysicalVolume(BaseModel):

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    disk_device = generic.GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=100)
    filepath = models.CharField(max_length=200)
    server = models.ForeignKey(Server)


    def __unicode__(self):
        return '{0}'.format(self.name)

    @permalink
    def get_absolute_url(self):
        return ('pv-detail', (), {'pk': self.pk})
