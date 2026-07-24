from django.shortcuts import redirect, render

from books.forms import AuthorForm


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