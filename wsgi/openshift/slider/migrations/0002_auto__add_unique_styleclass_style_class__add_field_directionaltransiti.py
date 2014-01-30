# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'StyleClass', fields ['style_class']
        db.create_unique(u'slider_styleclass', ['style_class'])

        # Adding field 'DirectionalTransition.name'
        db.add_column(u'slider_directionaltransition', 'name',
                      self.gf('django.db.models.fields.CharField')(default=1, unique=True, max_length=30),
                      keep_default=False)

        # Adding unique constraint on 'DirectionalTransition', fields ['directional_transition']
        db.create_unique(u'slider_directionaltransition', ['directional_transition'])

        # Adding unique constraint on 'Easing', fields ['easing']
        db.create_unique(u'slider_easing', ['easing'])


    def backwards(self, orm):
        # Removing unique constraint on 'Easing', fields ['easing']
        db.delete_unique(u'slider_easing', ['easing'])

        # Removing unique constraint on 'DirectionalTransition', fields ['directional_transition']
        db.delete_unique(u'slider_directionaltransition', ['directional_transition'])

        # Removing unique constraint on 'StyleClass', fields ['style_class']
        db.delete_unique(u'slider_styleclass', ['style_class'])

        # Deleting field 'DirectionalTransition.name'
        db.delete_column(u'slider_directionaltransition', 'name')


    models = {
        u'slider.directionaltransition': {
            'Meta': {'object_name': 'DirectionalTransition'},
            'directional_transition': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'slider.easing': {
            'Meta': {'object_name': 'Easing'},
            'easing': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'slider.slide': {
            'Meta': {'object_name': 'Slide'},
            'background': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'background_color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slot_amount': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'transition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slider.Transition']"})
        },
        u'slider.slideitem': {
            'Meta': {'object_name': 'SlideItem'},
            'animation_easing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slider.Easing']"}),
            'animation_speed': ('django.db.models.fields.IntegerField', [], {'default': '100', 'max_length': '5'}),
            'caption_style_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slider.StyleClass']"}),
            'directional_transition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slider.DirectionalTransition']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position_x_axis': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'position_y_axis': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'slide': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slider.Slide']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'timing': ('django.db.models.fields.IntegerField', [], {'default': '300', 'max_length': '5'})
        },
        u'slider.styleclass': {
            'Meta': {'object_name': 'StyleClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'style_class': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'slider.transition': {
            'Meta': {'object_name': 'Transition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transition': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['slider']