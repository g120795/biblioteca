from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from books.forms import AuthorForm
from books.models import Author


@login_required
def content_auth(request):
    return render(request, 'content_auth.html')

@login_required
def create_author(request):
    if not request.user.is_staff:
        messages.warning(request, 'no autorizado')
        return redirect('read_authors')
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


@login_required
def read_authors(request):
    queryset = Author.objects.all()
    context = {
        'form':queryset
    }
    return render(request, 'read_authors.html', context)


@login_required
def edit_author(request, author_id):
    if not request.user.is_staff:
        messages.warning(request, 'no autorizado')
        return redirect('read_authors')
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


@login_required
def detail_author(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        'author':author
    }
    return render(request, 'detail_author.html', context)


@login_required
def delete_author(request, author_id):
    if not request.user.is_staff:
        messages.warning(request, 'no autorizado')
        return redirect('read_authors')
    author = get_object_or_404(Author,id=author_id)
    if request.method == 'POST':
        author.delete()
        messages.success(request, 'author eliminado exitosamente')
        return redirect('read_authors')
    return render(request,'delete.html' )