# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field comment on 'Event'
        db.delete_table(db.shorten_name(u'event_event_comment'))


        # Changing field 'Event.category'
        db.alter_column(u'event_event', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.EventCategory'], null=True))

        # Changing field 'Event.fr'
        db.alter_column(u'event_event', 'fr', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Event.cover'
        db.alter_column(u'event_event', 'cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Event.to'
        db.alter_column(u'event_event', 'to', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Event.place'
        db.alter_column(u'event_event', 'place', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

    def backwards(self, orm):
        # Adding M2M table for field comment on 'Event'
        m2m_table_name = db.shorten_name(u'event_event_comment')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'event.event'], null=False)),
            ('comment', models.ForeignKey(orm[u'comment.comment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'comment_id'])


        # Changing field 'Event.category'
        db.alter_column(u'event_event', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['event.EventCategory']))

        # Changing field 'Event.fr'
        db.alter_column(u'event_event', 'fr', self.gf('django.db.models.fields.DateTimeField')(default=1))

        # Changing field 'Event.cover'
        db.alter_column(u'event_event', 'cover', self.gf('django.db.models.fields.files.ImageField')(default=1, max_length=100))

        # Changing field 'Event.to'
        db.alter_column(u'event_event', 'to', self.gf('django.db.models.fields.DateTimeField')(default=1))

        # Changing field 'Event.place'
        db.alter_column(u'event_event', 'place', self.gf('django.db.models.fields.CharField')(default=1, max_length=250))

    models = {
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.EventCategory']", 'null': 'True', 'blank': 'True'}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'details': ('ckeditor.fields.RichTextField', [], {}),
            'fr': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_pub': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'parent_post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.Event']", 'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event_post_type'", 'to': u"orm['event.PostType']"}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'youtube_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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