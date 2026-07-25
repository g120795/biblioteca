from django.shortcuts import redirect, render

from books.forms import AuthorForm
from books.models import Author


def content_auth(request):
    return render(request, 'content_auth.html')

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()

    context = {
        'form':form
    }
    return render(request, 'create_author.html', context)


def read_authors(request):
    queryset = Author.objects.all()
    context = {
        'form':queryset
    }
    return render(request, 'read_authors.html', context)

def edit_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
    else:
        form = AuthorForm(instance=author)

    context = {
        'form': form
    }
    return render(request, 'edit_author.html', context)

def detail_author(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        'author':author
    }
    return render(request, 'detail_author.html', context)