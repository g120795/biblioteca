from django import forms

from books.models import Editorial


class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ('name','adress','city','region','country')