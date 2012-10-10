from django.db import models
from django.db.models import permalink
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from discobolus.core.models import BaseModel
from discobolus.server.models import Server

class BaseLVMModel(BaseModel):

    name = models.CharField(max_length=100)
    uuid = models.CharField(max_length=200)
    size = models.PositiveIntegerField()
    server = models.ForeignKey(Server)

    class Meta:
        abstract = True

    def __unicode__(self):
        return '{0}'.format(self.name)

class PhysicalVolume(BaseLVMModel):

    #content_type = models.ForeignKey(ContentType)
    #object_id = models.PositiveIntegerField()
    #disk_device = generic.GenericForeignKey('content_type', 'object_id')

    @permalink
    def get_absolute_url(self):
        return ('pv-detail', (), {'pk': self.pk})

class VolumeGroup(BaseLVMModel):

    #path = models.CharField(max_length=200)
    #physical_volumes = models.ForeignKey(PhysicalVolume)

    @permalink
    def get_absolute_url(self):
        return ('vg-detail', (), {'pk': self.pk})


class LogicalVolume(BaseLVMModel):

    #path = models.CharField(max_length=200)
    #volume_group = models.ForeignKey(VolumeGroup)
    #status = models.CharField(max_length=100)

    @permalink
    def get_absolute_url(self):
        return ('lv-detail', (), {'pk': self.pk})

