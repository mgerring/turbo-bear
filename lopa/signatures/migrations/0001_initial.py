# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Signature'
        db.create_table(u'signatures_signature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('subscribe', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'signatures', ['Signature'])

        # Adding model 'ZipCode'
        db.create_table(u'signatures_zipcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('lon', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'signatures', ['ZipCode'])

        # Adding model 'StateCount'
        db.create_table(u'signatures_statecount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'signatures', ['StateCount'])


    def backwards(self, orm):
        # Deleting model 'Signature'
        db.delete_table(u'signatures_signature')

        # Deleting model 'ZipCode'
        db.delete_table(u'signatures_zipcode')

        # Deleting model 'StateCount'
        db.delete_table(u'signatures_statecount')


    models = {
        u'signatures.signature': {
            'Meta': {'object_name': 'Signature'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'subscribe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'signatures.statecount': {
            'Meta': {'object_name': 'StateCount'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'signatures.zipcode': {
            'Meta': {'object_name': 'ZipCode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'})
        }
    }

    complete_apps = ['signatures']