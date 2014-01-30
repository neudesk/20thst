# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EventCategory'
        db.create_table(u'event_eventcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'event', ['EventCategory'])

        # Adding field 'Event.category'
        db.add_column(u'event_event', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['event.EventCategory']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'EventCategory'
        db.delete_table(u'event_eventcategory')

        # Deleting field 'Event.category'
        db.delete_column(u'event_event', 'category_id')


    models = {
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.EventCategory']"}),
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
        },
        u'event.eventcategory': {
            'Meta': {'object_name': 'EventCategory'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['event']