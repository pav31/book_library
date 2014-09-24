from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib import admin
from books import views, models


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index),

    (r'^publishers/$', ListView.as_view(
        queryset=models.Publisher.objects.all(),
        context_object_name="publisher_list",
    )),


    (r'^authors/$', ListView.as_view(
        queryset=models.Author.objects.all(),
        context_object_name="author_list",
    )),

    (r'^books/$', ListView.as_view(
        queryset=models.Book.objects.order_by("title"),
        context_object_name="book_list",
    )),

    # (r'^books/(\w+)/$', views.PublisherBookListView.as_view()),

    # Detail View
    (r'^publishers/(?P<pk>\d+)/$', views.PublisherDetailView.as_view()),
    (r'^authors/(?P<pk>\d+)/$', views.AuthorDetailView.as_view()),
    (r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),

    url(r'^books_all/$', views.books_all),
    url(r'^add_author/$', views.add_author),
    url(r'^search/$', views.search),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^register/$', views.MyRegistrationView.as_view(), name='registration_register',),

    # Edit Authors
    url(r'author/add/$', login_required(views.AuthorCreate.as_view(success_url='/authors')), name='author_add'),
    url(r'author/(?P<pk>\d+)/update/$', login_required(views.AuthorUpdate.as_view(success_url='/authors')), name='author_update',),
    url(r'author/(?P<pk>\d+)/delete/$', login_required(views.AuthorDelete.as_view(success_url='/authors')), name='author_delete'),
    url(r'book/add/$', login_required(views.BookCreate.as_view(success_url='/books')), name='book_add'),
    url(r'book/(?P<pk>\d+)/update/$', login_required(views.BookUpdate.as_view(success_url='/books')), name='book_update'),
    url(r'book/(?P<pk>\d+)/delete/$', login_required(views.BookDelete.as_view(success_url='/books')), name='book_delete'),
)
