# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Path.state'
        db.delete_column('disk_path', 'state')

        # Adding field 'Path.physical_state'
        db.add_column('disk_path', 'physical_state',
                      self.gf('django.db.models.fields.CharField')(default='active', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Path.state'
        db.add_column('disk_path', 'state',
                      self.gf('django.db.models.fields.CharField')(default='active', max_length=100),
                      keep_default=False)

        # Deleting field 'Path.physical_state'
        db.delete_column('disk_path', 'physical_state')


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
            'physical_state': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '100'})
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