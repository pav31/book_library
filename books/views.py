import datetime
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from models import Book, Author
from forms import AuthorForm
from registration.backends.simple.views import RegistrationView
from django.forms.models import modelform_factory


def index(request):
    return render(request, 'index.html')


class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'email']


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'email']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')


class BookCreate(CreateView):
    form = AuthorForm
    model = Book
    form_class = modelform_factory(Book,
                                   widgets={"authors": FilteredSelectMultiple(
                                       verbose_name="authors",
                                       is_stacked=True, )})
    fields = ['title', 'authors']


class BookUpdate(UpdateView):
    model = Book
    form_class = modelform_factory(Book,
                                   widgets={"authors": FilteredSelectMultiple(
                                       verbose_name="authors",
                                       is_stacked=True, )})
    fields = ['title', 'authors', 'publisher', 'publication_date']


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')


class AuthorDetailView(DetailView):
    model = Author

    def get_object(self):
        object = super(AuthorDetailView, self).get_object()
        return object


class BookDetailView(DetailView):
    model = Book

    def get_object(self):
        object = super(BookDetailView, self).get_object()
        return object


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return "/"


def search(request):
    errors = []
    if request.GET.get('query'):
        query = request.GET['query']
        # assert False, query
        if not query:
            errors.append('query is empty')
        elif len(query) > 10:
            errors.append('query is > 10 symbols')
        else:
            books = Book.objects.filter(title__icontains=query)
            authors = Author.objects.filter(first_name__icontains=query)
            if not authors:
                authors = Author.objects.filter(last_name__icontains=query)

            return render(request, 'search_results.html',
                          {'books': books,
                           'authors': authors,
                           'query': query,
                          })
    return render(request, 'search.html', {'errors': errors})