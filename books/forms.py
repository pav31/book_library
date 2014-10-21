from django.utils.translation import gettext as _
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from models import Book, Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author



class BookForm(ModelForm):
    class Meta:
        model = Book
        widgets = {'authors': FilteredSelectMultiple(verbose_name="authors",
                                                     is_stacked=True,) }
    class Media:
        css = {'all':['admin/css/widgets.css']}
        js = ['/admin/jsi18n/']