from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from books.forms import EditorialForm
from books.models import Editorial


@login_required
def content_editorials(request):
    return render(request, 'content_editorials.html')

@login_required
def create_editorial(request):
    if not request.user.is_staff:
        messages.warning(request, 'no autorizado')
        return redirect('read_editorials')
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

@login_required
def read_editorials(request):
    
    queryset = Editorial.objects.all()
    context = {
        'form':queryset
    }
    return render(request, 'read_editorials.html', context)


@login_required
def detail_editorial(request, editorial_id):
    editorial = Editorial.objects.get(id=editorial_id)
    context = {
        'editorial':editorial
    }
    return render(request, 'detail_editorial.html', context)

@login_required
def edit_editorial(request, editorial_id):
    if not request.user.is_staff:
        messages.warning(request, 'no autorizado')
        return redirect('read_editorials')
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

@login_required
def delete_editorial(request, editorial_id):
    if not request.user.is_staff:
        messages.warning(request, 'no autorizado')
        return redirect('read_editorials')
    editorial = get_object_or_404(Editorial,id=editorial_id)
    if request.method == 'POST':
        editorial.delete()
        return redirect('read_editorials')
    context = {
        'editorial':editorial
    }
    return render(request,'delete_editorial.html', context )