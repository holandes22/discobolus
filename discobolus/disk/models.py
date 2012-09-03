from django.db import models
from discobolus.core.models import BaseModel
from django.db.models import permalink


class BaseDisk(BaseModel):

    name = models.CharField(max_length=200)
    filepath = models.CharField(max_length=250)
    size = models.IntegerField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'{0}'.format(self.filepath)


class Disk(BaseDisk):

    uuid = models.CharField(max_length=200)

    @permalink
    def get_absolute_url(self):
        return ('disk-detail', (), {'pk': self.pk})


class Partition(BaseDisk):
    parent = models.ForeignKey(Disk)
    uuid = models.CharField(max_length=200)

    @permalink
    def get_absolute_url(self):
        return ('partition-detail', (), {'parent_pk': self.parent.pk, 'pk': self.pk})


class MultipathDisk(BaseDisk):

    wwid = models.CharField(max_length=200)

    @permalink
    def get_absolute_url(self):
        return ('multipath-disk-detail', (), {'pk': self.pk})


class PathGroup(BaseModel):

    state = models.CharField(max_length=100)
    priority = models.IntegerField()
    multipath_disk = models.ForeignKey(MultipathDisk)

    def __unicode__(self):
        return u'{0}'.format(self.state)


class Path(BaseModel):

    name = models.CharField(max_length=150)
    physical_state = models.CharField(max_length=100, default='active')
    path_group = models.ForeignKey(PathGroup)

    def __unicode__(self):
        return u'{0}'.format(self.name)
