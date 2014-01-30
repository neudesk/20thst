# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.fr'
        db.add_column(u'event_event', 'fr',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 12, 26, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.to'
        db.add_column(u'event_event', 'to',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 12, 26, 0, 0)),
                      keep_default=False)


        # Changing field 'Event.end'
        db.alter_column(u'event_event', 'end', self.gf('django.db.models.fields.TimeField')())

        # Changing field 'Event.start'
        db.alter_column(u'event_event', 'start', self.gf('django.db.models.fields.TimeField')())

    def backwards(self, orm):
        # Deleting field 'Event.fr'
        db.delete_column(u'event_event', 'fr')

        # Deleting field 'Event.to'
        db.delete_column(u'event_event', 'to')


        # Changing field 'Event.end'
        db.alter_column(u'event_event', 'end', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Event.start'
        db.alter_column(u'event_event', 'start', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'details': ('ckeditor.fields.RichTextField', [], {}),
            'end': ('django.db.models.fields.TimeField', [], {}),
            'fr': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_pub': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'to': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['event']