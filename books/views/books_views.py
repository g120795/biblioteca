from django.shortcuts import render

from books.forms.book_form import BookForm


def content_books(request):
    return render(request, 'content_books.html')

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