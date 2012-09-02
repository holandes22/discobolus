from django.contrib import admin
from discobolus.disk.models import Disk, Partition
from discobolus.disk.models import MultipathDisk, PathGroup, Path

admin.site.register(Disk)
admin.site.register(Partition)
admin.site.register(MultipathDisk)
admin.site.register(PathGroup)
admin.site.register(Path)


