# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Disk'
        db.create_table('disk_disk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('filepath', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('disk', ['Disk'])

        # Adding model 'Partition'
        db.create_table('disk_partition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('filepath', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disk.Disk'])),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('disk', ['Partition'])

        # Adding model 'MultipathDisk'
        db.create_table('disk_multipathdisk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('filepath', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('wwid', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('disk', ['MultipathDisk'])

        # Adding model 'PathGroup'
        db.create_table('disk_pathgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
            ('multipath_disk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disk.MultipathDisk'])),
        ))
        db.send_create_signal('disk', ['PathGroup'])

        # Adding model 'Path'
        db.create_table('disk_path', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('path_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['disk.PathGroup'])),
        ))
        db.send_create_signal('disk', ['Path'])


    def backwards(self, orm):
        # Deleting model 'Disk'
        db.delete_table('disk_disk')

        # Deleting model 'Partition'
        db.delete_table('disk_partition')

        # Deleting model 'MultipathDisk'
        db.delete_table('disk_multipathdisk')

        # Deleting model 'PathGroup'
        db.delete_table('disk_pathgroup')

        # Deleting model 'Path'
        db.delete_table('disk_path')


    models = {
        'disk.disk': {
            'Meta': {'object_name': 'Disk'},
            'filepath': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'disk.multipathdisk': {
            'Meta': {'object_name': 'MultipathDisk'},
            'filepath': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'wwid': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'disk.partition': {
            'Meta': {'object_name': 'Partition'},
            'filepath': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disk.Disk']"}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'disk.path': {
            'Meta': {'object_name': 'Path'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'path_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disk.PathGroup']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'disk.pathgroup': {
            'Meta': {'object_name': 'PathGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multipath_disk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['disk.MultipathDisk']"}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['disk']