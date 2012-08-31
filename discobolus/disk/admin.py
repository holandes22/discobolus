from django.contrib import admin
from discobolus.disk.models import Disk, Partition

admin.site.register(Disk)
admin.site.register(Partition)

