from django.shortcuts import render
from books.forms.book_form import BookForm

def list_books(request):
    return render(request, 'list_books.html')

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    context = {
        'form':form
    }
    return render(request, 'create_book.html', context)