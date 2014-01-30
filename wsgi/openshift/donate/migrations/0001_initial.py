# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Donation'
        db.create_table(u'donate_donation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('donated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
        ))
        db.send_create_signal(u'donate', ['Donation'])

        # Adding model 'Donor'
        db.create_table(u'donate_donor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donate.Donation'])),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'donate', ['Donor'])


    def backwards(self, orm):
        # Deleting model 'Donation'
        db.delete_table(u'donate_donation')

        # Deleting model 'Donor'
        db.delete_table(u'donate_donor')


    models = {
        u'donate.donation': {
            'Meta': {'object_name': 'Donation'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'donated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'})
        },
        u'donate.donor': {
            'Meta': {'object_name': 'Donor'},
            'donation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donate.Donation']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['donate']