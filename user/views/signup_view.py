from django.contrib import messages
from django.shortcuts import redirect, render

from user.forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'usuario creado correctamente')
            return redirect('login')
    else:
        form = SignupForm()

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)