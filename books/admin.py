from django.contrib import admin
from models import Author, Book, AuthorBook


class AuthorBookInline(admin.TabularInline):
    model = AuthorBook
    list_display = ('book', 'author')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
    search_fields = ('first_name', 'last_name', 'email',)
    inlines = [AuthorBookInline,]

class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('authors',)
    inlines = [AuthorBookInline,]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)


