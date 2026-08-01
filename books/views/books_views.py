from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from books.forms.book_form import BookForm
from books.models import Book


@login_required
def content_books(request):
    return render(request, 'content_books.html')


@login_required
def create_book(request):
    if not request.user.is_staff:
        messages.warning(request, 'no autorizado')
        return redirect('read_books')
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'libro creado exitosamente')
            
    else:
        form = BookForm()
    context = {
        'form':form
    }
    return render(request, 'create_book.html', context)


@login_required
def read_books(request):
    queryset = Book.objects.all()
    search = request.GET.get('search')
    if search:
        queryset = queryset.filter(title__icontains=search)
    paginator = Paginator(queryset, 2)
    page_num = request.GET.get('page')
    pagina = paginator.get_page(page_num)
    context = {
        'form':pagina
    }
    return render(request, 'read_books.html', context)


@login_required
def edit_book(request, book_id):
    if not request.user.is_staff:
        messages.warning(request, 'no autorizado')
        return redirect('read_books')
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        print(form.errors)
        if form.is_valid():
            print('form is valid')
            form.save()
            messages.success(request, 'libro actualizado exitosamente')
            return redirect('read_books')
    else:
        form = BookForm(instance=book)

    context = {
        'form': form
    }
    return render(request, 'edit_book.html', context)


@login_required
def detail_book(request, book_id):
    book = get_object_or_404(Book,id=book_id)
    context = {
        'book':book
    }
    return render(request, 'detail_book.html', context)


@login_required
def delete_book(request, book_id):
    if not request.user.is_staff:
        messages.warning(request, 'no autorizado')
        return redirect('read_books')
    libro = get_object_or_404(Book,id=book_id)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'libro eliminado exitosamente')
        return redirect('read_books')
    return render(request,'delete.html' )