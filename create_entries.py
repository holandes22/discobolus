import os
import random
from discobolus.disk.models import Disk, MultipathDisk, Partition, PathGroup, Path

letters = map(chr, range(97, 123))
switch = True
switch_pg = True
for l in letters[0:3]:
    name = 'sd{0}'.format(l)
    d = Disk(
            name=name,
            filepath=os.path.join('/', 'dev', name),
            size=random.randint(1,2048),
            uuid='uuid-{0}'.format(random.choice('chuck'))
            )
    d.save()
    if switch:
        count = 1
        for lp in letters[0:2]:
            p = Partition(
                    name=name + str(count),
                    filepath=os.path.join('/', 'dev', name),
                    size=random.randint(1,11048),
                    uuid='uuid-{0}'.format(random.choice('comando')),
                    parent = d
                    )
            count += 1
            p.save()

    name = 'mpath{0}'.format(l)
    mpd = MultipathDisk(
            name=name,
            filepath=os.path.join('/', 'dev', 'mapper', name),
            size=random.randint(1,5000),
            wwid='wwid-{0}-mp'.format(random.choice('walkertexasranger')),
            )
    mpd.save()

    iterations = 2 if switch_pg else 1
    for i in xrange(0, iterations):
        pg = PathGroup(state='ACTIVE', priority=random.randint(1,9), multipath_disk=mpd)
        pg.save()
        r = 6 if switch else 8
        for lpath in letters[4:r]:
            p = Path(name='sd{0}'.format(lpath), state='Active', path_group=pg)
            p.save()
    switch_pg = False
    switch = not switch
print 'Done'
