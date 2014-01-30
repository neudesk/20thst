# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.posted'
        db.add_column(u'event_event', 'posted',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 26, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.posted'
        db.delete_column(u'event_event', 'posted')


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
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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