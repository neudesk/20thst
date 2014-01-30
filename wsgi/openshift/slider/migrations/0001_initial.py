# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Transition'
        db.create_table(u'slider_transition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transition', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'slider', ['Transition'])

        # Adding model 'Slide'
        db.create_table(u'slider_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('transition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slider.Transition'])),
            ('slot_amount', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('background_color', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('background', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100)),
        ))
        db.send_create_signal(u'slider', ['Slide'])

        # Adding model 'DirectionalTransition'
        db.create_table(u'slider_directionaltransition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('directional_transition', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'slider', ['DirectionalTransition'])

        # Adding model 'Easing'
        db.create_table(u'slider_easing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('easing', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'slider', ['Easing'])

        # Adding model 'StyleClass'
        db.create_table(u'slider_styleclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('style_class', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'slider', ['StyleClass'])

        # Adding model 'SlideItem'
        db.create_table(u'slider_slideitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slide', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slider.Slide'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('directional_transition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slider.DirectionalTransition'])),
            ('animation_easing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slider.Easing'])),
            ('animation_speed', self.gf('django.db.models.fields.IntegerField')(default=100, max_length=5)),
            ('timing', self.gf('django.db.models.fields.IntegerField')(default=300, max_length=5)),
            ('position_x_axis', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4)),
            ('position_y_axis', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4)),
            ('caption_style_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slider.StyleClass'])),
        ))
        db.send_create_signal(u'slider', ['SlideItem'])


    def backwards(self, orm):
        # Deleting model 'Transition'
        db.delete_table(u'slider_transition')

        # Deleting model 'Slide'
        db.delete_table(u'slider_slide')

        # Deleting model 'DirectionalTransition'
        db.delete_table(u'slider_directionaltransition')

        # Deleting model 'Easing'
        db.delete_table(u'slider_easing')

        # Deleting model 'StyleClass'
        db.delete_table(u'slider_styleclass')

        # Deleting model 'SlideItem'
        db.delete_table(u'slider_slideitem')


    models = {
        u'slider.directionaltransition': {
            'Meta': {'object_name': 'DirectionalTransition'},
            'directional_transition': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'slider.easing': {
            'Meta': {'object_name': 'Easing'},
            'easing': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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
            'style_class': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'slider.transition': {
            'Meta': {'object_name': 'Transition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transition': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['slider']