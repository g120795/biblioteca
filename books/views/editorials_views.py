from django.shortcuts import get_object_or_404, redirect, render

from books.forms import EditorialForm
from books.models import Editorial


def content_editorials(request):
    return render(request, 'content_editorials.html')

def create_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditorialForm()
    context = {
        'form':form
    }

    return render(request, 'create_editorial.html', context)

def read_editorials(request):
    queryset = Editorial.objects.all()
    context = {
        'form':queryset
    }
    return render(request, 'read_editorials.html', context)


def detail_editorial(request, editorial_id):
    editorial = Editorial.objects.get(id=editorial_id)
    context = {
        'editorial':editorial
    }
    return render(request, 'detail_editorial.html', context)


def edit_editorial(request, editorial_id):
    editorial = Editorial.objects.get(id=editorial_id)
    if request.method == 'POST':
        form = EditorialForm(request.POST, instance=editorial)
        if form.is_valid():
            form.save()
            return redirect('read_editorials')
    else:
        form = EditorialForm(instance=editorial)

    context = {
        'form': form
    }
    return render(request, 'edit_editorial.html', context)


def delete_editorial(request, editorial_id):
    editorial = get_object_or_404(Editorial,id=editorial_id)
    if request.method == 'POST':
        editorial.delete()
        return redirect('read_editorials')
    context = {
        'editorial':editorial
    }
    return render(request,'delete_editorial.html', context )