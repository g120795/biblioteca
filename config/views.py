from django.shortcuts import render 

def home(request):
    return render(request, 'base.html')

def editorials(request):
    return render(request,'editorials.html')

def books(request):
    return render(request, 'books.html')

def auth(request):
    return render(request, 'auth.html')

def contact(request):
    return render(request, 'contact.html')

