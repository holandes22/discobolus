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

class VolumeGroup(BaseModel):

    server = models.ForeignKey(Server)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=200)
    size = models.PositiveIntegerField()
    uuid = models.CharField(max_length=200)
    physical_volumes = models.ForeignKey(PhysicalVolume)

    def __unicode__(self):
        return '{0}'.format(self.name)

    @permalink
    def get_absolute_url(self):
        return ('vg-detail', (), {'pk': self.pk})


class LogicalVolume(BaseModel):

    server = models.ForeignKey(Server)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=200)
    size = models.PositiveIntegerField()
    volume_group = models.ForeignKey(VolumeGroup)
    uuid = models.CharField(max_length=200)
    status = models.CharField(max_length=100)

    def __unicode__(self):
        return '{0}'.format(self.name)

    @permalink
    def get_absolute_url(self):
        return ('vg-detail', (), {'pk': self.pk})

