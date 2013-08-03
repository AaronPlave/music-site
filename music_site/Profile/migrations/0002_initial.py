# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'Profile_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.Temp_User'], unique=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'Profile', ['Profile'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'Profile_profile')


    models = {
        u'Profile.profile': {
            'Meta': {'object_name': 'Profile'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['registration.Temp_User']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'registration.temp_user': {
            'Meta': {'object_name': 'Temp_User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['Profile']