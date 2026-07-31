from django import forms

from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=('title','isbn','pages_number','language','editorial','gender','unit_price','authores')