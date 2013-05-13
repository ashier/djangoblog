# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'works_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('sub_title', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='title', overwrite=False)),
            ('markdown_content', self.gf('django.db.models.fields.TextField')()),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('html_content', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'works', ['Project'])

        # Adding M2M table for field medium on 'Project'
        db.create_table(u'works_project_medium', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'works.project'], null=False)),
            ('media', models.ForeignKey(orm[u'works.media'], null=False))
        ))
        db.create_unique(u'works_project_medium', ['project_id', 'media_id'])

        # Adding M2M table for field categories on 'Project'
        db.create_table(u'works_project_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'works.project'], null=False)),
            ('category', models.ForeignKey(orm[u'works.category'], null=False))
        ))
        db.create_unique(u'works_project_categories', ['project_id', 'category_id'])

        # Adding model 'Media'
        db.create_table(u'works_media', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'works', ['Media'])

        # Adding model 'Category'
        db.create_table(u'works_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='title', overwrite=False)),
        ))
        db.send_create_signal(u'works', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'works_project')

        # Removing M2M table for field medium on 'Project'
        db.delete_table('works_project_medium')

        # Removing M2M table for field categories on 'Project'
        db.delete_table('works_project_categories')

        # Deleting model 'Media'
        db.delete_table(u'works_media')

        # Deleting model 'Category'
        db.delete_table(u'works_category')


    models = {
        u'works.category': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'False'})
        },
        u'works.media': {
            'Meta': {'object_name': 'Media'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'works.project': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Project'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'categories'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['works.Category']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'html_content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'markdown_content': ('django.db.models.fields.TextField', [], {}),
            'medium': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['works.Media']", 'symmetrical': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'False'}),
            'sub_title': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['works']