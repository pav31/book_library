from django.db import models
from django.core.urlresolvers import reverse


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, verbose_name='e-mail')


    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})


    def wrote_books(self):
        # todo: fix display list of books in admin
        return self.book_set


class BookManager(models.Manager):
    def create_book(self, **kwargs):
        book = self.create(**kwargs)
        # do something with the book
        return book


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title


class AuthorBook(models.Model):
    author = models.ForeignKey(Author)
    book = models.ForeignKey(Book)

