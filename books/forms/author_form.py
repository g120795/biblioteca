from django import forms

from books.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=('name','lastname','born','nationality','biograpy',)