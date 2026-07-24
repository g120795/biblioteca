from django.shortcuts import render

from books.forms import EditorialForm


def content_editorials(request):
    return render(request, 'content_editorials.html')

def create_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EditorialForm()
    context = {
        'form':form
    }

    return render(request, 'create_editorial.html', context)