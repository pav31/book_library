import datetime
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, DetailView, ListView
from django.core.urlresolvers import reverse_lazy
# from django.core.urlresolvers import reverse
from models import Book, Author, Publisher
from forms import AuthorForm



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
    model = Book
    fields = ['title', 'authors', 'publisher', 'publication_date']


class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'authors', 'publisher', 'publication_date']


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')


class PublisherDetailView(DetailView):

    context_object_name = "publisher"
    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context

#
# class PublisherBookListView(ListView):
#
#     context_object_name = "book_list"
#     template_name = "books/books_by_publisher.html"
#
#     def get_queryset(self):
#         self.publisher = get_object_or_404(Publisher, name__iexact=self.args[0])
#         return Book.objects.filter(publisher=self.publisher)
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(PublisherBookListView, self).get_context_data(**kwargs)
#         # Add in the publisher
#         context['publisher'] = self.publisher
#         return context


class AuthorDetailView(DetailView):
    queryset = Author.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(AuthorDetailView, self).get_object()
        # Record the last accessed date
        # object.last_accessed = datetime.datetime.now()
        object.save()
        # Return the object
        return object


class BookDetailView(DetailView):
    queryset = Book.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(BookDetailView, self).get_object()
        # Record the last accessed date
        # object.last_accessed = datetime.datetime.now()
        object.save()
        # Return the object
        return object


def about_pages(request, page):
    try:
        return direct_to_template(request, template="about/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404()


def index(request):
    return render(request, 'index.html')


def books_all(request):
    # data = serializers.serialize( "python", Book.objects.all())
    return render_to_response('books_all.html',
                          RequestContext(request, {'data': data,}))



def add_author(request):
    # if this is a POST request we need to process the form data
    form = AuthorForm(request.POST or None)
    # assert False,
    authors = Author.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.instance.save()
            return HttpResponseRedirect('/author_form/')

    return render(request, 'books/author_form.html', {'form': form, 'authors': authors})


def search(request):
    errors = []
    if request.GET.get('query'):
        query = request.GET['query']
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
    return render(request, 'search.html',
                  {'errors': errors})