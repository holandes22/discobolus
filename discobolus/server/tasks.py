import rpyc
from celery.task import task
from celery.utils.log import get_task_logger
from celery import current_task

from discobolus.disk.models import Disk, MultipathDisk, Partition
from discobolus.lvm.models import PhysicalVolume

logger = get_task_logger(__name__)


@task()
def build_disk_database(server):
    request = current_task.request
    logger.info('Executing {0}'.format(request.id))
    conn = rpyc.classic.connect(server.agent_network_address)
    remote_disk = conn.modules['dmtcore.disk']
    disks = remote_disk.get_disks()
    for disk in disks:
        if hasattr(disk, 'paths'):
            instance = MultipathDisk()
            instance.name = disk.get_name()
            instance.filepath = disk.get_filepath()
            instance.size = disk.get_size()
            instance.wwid = disk.wwid
            instance.server = server
            instance.save()
        else:
            instance = Disk()
            instance.name = disk.get_name()
            instance.filepath = disk.get_filepath()
            instance.size = disk.get_size()
            instance.uuid = disk.disk_identifier
            instance.server = server
            instance.save()

            for partition in disk.get_partitions():
                part = Partition()
                part.name = partition.get_name()
                part.filepath = partition.get_filepath()
                part.size = 2
                part.uuid = 'uuu-bbb'
                part.parent = instance
                part.save()


@task()
def build_lvm_database(server):
    conn = rpyc.classic.connect(server.agent_network_address)
    remote_lvm = conn.modules['dmtcore.lvm']
    vm = remote_lvm.VolumeManager()
    pvs = vm.get_physical_volumes()
    for pv in pvs:
        instance = PhysicalVolume()
        instance.name = pv.name
        instance.size = 555
        instance.uuid = pv.uuid
        instance.server = server
        instance.save()

@task()
def get_pvs(addr):
    conn = rpyc.classic.connect('192.168.1.120')
    remote_lvm = conn.modules['dmtcore.lvm']
    vm = remote_lvm.VolumeManager()
    return [pv.name for pv in vm.get_physical_volumes()]

@task
def get_disk_names(addr):
    conn = rpyc.classic.connect('192.168.1.120')
    remote_disk = conn.modules['dmtcore.disk']
    disks = remote_disk.get_disks()
    return [disk.get_name() for disk in disks]
