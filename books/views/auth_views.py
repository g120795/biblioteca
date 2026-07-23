from django.shortcuts import render, redirect

def list_auth(request):
    return render(request, 'list_books.html')