from django.db import models
from django.core.urlresolvers import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True, verbose_name='e-mail')

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Book(models.Model):
    # isbn = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.title


class BookManager(models.Manager):
    def create_book(self, **kwargs):
        book = self.create(**kwargs)
        # do something with the book
        return book


class AuthorBook(models.Model):
    author = models.ForeignKey(Author)
    book = models.ForeignKey(Book)

