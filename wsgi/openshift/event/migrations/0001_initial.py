# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'event_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('details', self.gf('ckeditor.fields.RichTextField')()),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('is_pub', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'event', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'event_event')


    models = {
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'details': ('ckeditor.fields.RichTextField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_pub': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        }
    }

    complete_apps = ['event']