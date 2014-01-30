# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.category'
        db.delete_column(u'event_event', 'category_id')

        # Deleting field 'Event.youtube_url'
        db.delete_column(u'event_event', 'youtube_url')

        # Adding field 'Event.youtube_video_id'
        db.add_column(u'event_event', 'youtube_video_id',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Event.cover'
        db.alter_column(u'event_event', 'cover', self.gf('django.db.models.fields.files.ImageField')(default=1, max_length=100))

    def backwards(self, orm):
        # Adding field 'Event.category'
        db.add_column(u'event_event', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.EventCategory'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Event.youtube_url'
        db.add_column(u'event_event', 'youtube_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Event.youtube_video_id'
        db.delete_column(u'event_event', 'youtube_video_id')


        # Changing field 'Event.cover'
        db.alter_column(u'event_event', 'cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    models = {
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'details': ('ckeditor.fields.RichTextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_pub': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'parent_post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Event']", 'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event_post_type'", 'to': u"orm['event.PostType']"}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'youtube_video_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'event.eventcategory': {
            'Meta': {'object_name': 'EventCategory'},
            'category': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'event.posttype': {
            'Meta': {'object_name': 'PostType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['event']