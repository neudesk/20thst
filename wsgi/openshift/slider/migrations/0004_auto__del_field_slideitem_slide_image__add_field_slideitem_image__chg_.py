# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SlideItem.slide_image'
        db.delete_column(u'slider_slideitem', 'slide_image_id')

        # Adding field 'SlideItem.image'
        db.add_column(u'slider_slideitem', 'image',
                      self.gf('imagekit.models.fields.ProcessedImageField')(default=1, max_length=100),
                      keep_default=False)


        # Changing field 'Slide.background_color'
        db.alter_column(u'slider_slide', 'background_color', self.gf('django.db.models.fields.CharField')(max_length=7, null=True))

    def backwards(self, orm):
        # Adding field 'SlideItem.slide_image'
        db.add_column(u'slider_slideitem', 'slide_image',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slider.SlideItemImage'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'SlideItem.image'
        db.delete_column(u'slider_slideitem', 'image')


        # Changing field 'Slide.background_color'
        db.alter_column(u'slider_slide', 'background_color', self.gf('django.db.models.fields.CharField')(default=1, max_length=7))

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
            'background_color': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
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
            'image': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'position_x_axis': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'position_y_axis': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'slide': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slider.Slide']"}),
            'slide_text': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'timing': ('django.db.models.fields.IntegerField', [], {'default': '300', 'max_length': '5'})
        },
        u'slider.slideitemimage': {
            'Meta': {'object_name': 'SlideItemImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
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