# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Word'
        db.create_table(u'words_word', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('alignment', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('examples', self.gf('django.db.models.fields.TextField')()),
            ('usage', self.gf('django.db.models.fields.TextField')()),
            ('recommendations', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'words', ['Word'])


    def backwards(self, orm):
        # Deleting model 'Word'
        db.delete_table(u'words_word')


    models = {
        u'words.word': {
            'Meta': {'object_name': 'Word'},
            'alignment': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'examples': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recommendations': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'usage': ('django.db.models.fields.TextField', [], {}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['words']