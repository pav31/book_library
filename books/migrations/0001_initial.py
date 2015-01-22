# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'books_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'books', ['Author'])

        # Adding model 'Book'
        db.create_table(u'books_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'books', ['Book'])

        # Adding M2M table for field authors on 'Book'
        m2m_table_name = db.shorten_name(u'books_book_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'books.book'], null=False)),
            ('author', models.ForeignKey(orm[u'books.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])

        # Adding model 'AuthorBook'
        db.create_table(u'books_authorbook', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Author'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Book'])),
        ))
        db.send_create_signal(u'books', ['AuthorBook'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'books_author')

        # Deleting model 'Book'
        db.delete_table(u'books_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table(db.shorten_name(u'books_book_authors'))

        # Deleting model 'AuthorBook'
        db.delete_table(u'books_authorbook')


    models = {
        u'books.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'books.authorbook': {
            'Meta': {'object_name': 'AuthorBook'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['books.Author']"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['books.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'books.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['books.Author']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['books']