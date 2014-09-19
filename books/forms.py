from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import gettext as _
from django.forms import ModelForm, Textarea, CharField, EmailField, ModelMultipleChoiceField
from models import Book, Author, AuthorBook

class AuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']


class BookForm(ModelForm):
    title = CharField(max_length=100)
    authors = ModelMultipleChoiceField(queryset=Author.objects.all(),
                                       required=True,
                                       widget=FilteredSelectMultiple(
                                       verbose_name=_('Author'),
                                       is_stacked=False
                                       )
    )

    class Meta:
        model = Book