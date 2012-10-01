from django.contrib import admin
from discobolus.lvm.models import PhysicalVolume, VolumeGroup, LogicalVolume


admin.site.register(PhysicalVolume)
admin.site.register(VolumeGroup)
admin.site.register(LogicalVolume)

