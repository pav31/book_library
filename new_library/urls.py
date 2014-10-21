from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib import admin
from books import views, models


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index),

    (r'^authors/$', ListView.as_view(
        queryset=models.Author.objects.all(),
        context_object_name="author_list",
    )),

    (r'^books/$', ListView.as_view(
        queryset=models.Book.objects.order_by("title"),
        context_object_name="book_list",
    )),

    # Detail View
    (r'^authors/(?P<pk>\d+)/$', views.AuthorDetailView.as_view()),
    (r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),

    url(r'^search/$', views.search),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^register/$', views.MyRegistrationView.as_view(), name='registration_register',),

    # Edit Authors
    url(r'authors/add/$', login_required(views.AuthorCreate.as_view(success_url='/authors')), name='author_add'),
    url(r'authors/(?P<pk>\d+)/update/$', login_required(views.AuthorUpdate.as_view(success_url='/authors')), name='author_update',),
    url(r'authors/(?P<pk>\d+)/delete/$', login_required(views.AuthorDelete.as_view(success_url='/authors')), name='author_delete'),
    url(r'books/add/$', login_required(views.BookCreate.as_view(success_url='/books')), name='book_add'),
    url(r'books/(?P<pk>\d+)/update/$', login_required(views.BookUpdate.as_view(success_url='/books')), name='book_update'),
    url(r'books/(?P<pk>\d+)/delete/$', login_required(views.BookDelete.as_view(success_url='/books')), name='book_delete'),
)
