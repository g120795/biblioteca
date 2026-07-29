from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    return render(request, 'base.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def link_logout(request):
    return render(request, 'link_logout.html')

