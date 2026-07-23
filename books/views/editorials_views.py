from django.shortcuts import render

def list_editorials(request):
    return render(request, 'list_editorials.html')